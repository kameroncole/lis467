/**
 * search.js — hybrid vector search + Claude Haiku RAG.
 *
 * Flow:
 *  1. Fetch data/index.json from the server (206 docs with 384-dim embeddings).
 *  2. Load Transformers.js + all-MiniLM-L6-v2 from the CDN (cached after first visit).
 *  3. Embed the query in the browser → 384-dim unit vector.
 *  4. Cosine-rank every document filtered by persona.
 *  5. POST the top 6 doc IDs to ask.php → Claude Haiku writes a grounded answer.
 *  6. Render the LLM answer + result cards.
 *
 * Falls back to keyword-only retrieval (PHP side) if the model fails to load.
 */

const ASK_URL          = "ask.php";
const INDEX_URL        = "data/index.json";
const TRANSFORMERS_URL = "https://cdn.jsdelivr.net/npm/@xenova/transformers@2.17.2";
const MODEL            = "Xenova/all-MiniLM-L6-v2";
const TOP_K            = 6;

// Persona → allowed document types (null = all)
const PERSONA_TYPES = {
  students:  ["exhibit", "yes-unit", "yes-overview"],
  parents:   ["exhibit"],
  educators: null,
};

// --- Read URL params -----------------------------------------------------
const params   = new URLSearchParams(location.search);
const query    = (params.get("q") || "").trim();
const audience = params.get("audience") || localStorage.getItem("mos-audience") || "educators";

// --- DOM refs ------------------------------------------------------------
const queryLabel   = document.querySelector(".query h1");
const llmPara      = document.querySelector(".query p:last-of-type");
const mainResults  = document.querySelector(".results-main");
const sideResults  = document.querySelector(".resource-results");
const audienceRadios = document.querySelectorAll('input[name="audience"]');
const queryInputs    = document.querySelectorAll('input[name="q"]');

// --- Set audience radio and query inputs to current values ---------------
audienceRadios.forEach((r) => { r.checked = r.value === audience; });
queryInputs.forEach((inp) => { inp.value = query; });

// --- Helpers -------------------------------------------------------------
function esc(str) {
  return str.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;");
}

function typeIcon(type) {
  const icons = {
    "exhibit":          "🏛",
    "yes-unit":         "🔧",
    "yes-overview":     "📋",
    "ste-standard":     "📐",
    "ste-overview":     "📐",
    "research-document":"📄",
  };
  return icons[type] || "🔗";
}

function exhibitImgSrc(title) {
  // Map exhibit title to local image if we have one
  const slug = title.toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-|-$/g, "");
  return `images/exhibits/${slug}.jpg`;
}

function buildExhibitCard(r) {
  const isExhibit = r.type === "exhibit";
  const imgSrc    = exhibitImgSrc(r.title);
  const btnLabel  = isExhibit ? "More" : "View Unit";
  const media     = isExhibit
    ? `<figure>
        <img src="${esc(imgSrc)}" alt="${esc(r.title)}"
             onerror="this.closest('figure').innerHTML='<div class=placeholder-img>${esc(r.title)}</div>'">
        <small class="credit">Photo: Museum of Science</small>
       </figure>`
    : `<div class="yes-media">
        <div class="yes-badge">${r.type === "yes-overview" ? "YES Overview" : "YES Unit"}</div>
        <div class="yes-category">${esc(r.category)}</div>
       </div>`;
  return `
    <article class="exhibit-result${isExhibit ? "" : " yes-card"}">
      <div class="info">
        <h3><a href="${esc(r.url)}" target="_blank" rel="noopener">${esc(r.title)}</a></h3>
        <p>${esc(r.snippet)}</p>
        <p class="standards">${esc(r.category)}</p>
        <a class="btn" href="${esc(r.url)}" target="_blank" rel="noopener">${btnLabel}</a>
      </div>
      ${media}
    </article>`;
}

function buildDocCard(r) {
  const label = r.type === "research-document" ? "PDF" : typeIcon(r.type);
  return `
    <div class="doc">
      <div class="icon">${label}</div>
      <div>
        <h3><a href="${esc(r.url)}" target="_blank" rel="noopener">${esc(r.title)}</a></h3>
        <p>${esc(r.snippet)}</p>
      </div>
    </div>`;
}

// Convert minimal markdown to safe HTML (only **bold** and *italic*)
function mdToHtml(text) {
  return esc(text)
    .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>")
    .replace(/\*([^*]+)\*/g,     "<em>$1</em>");
}

// --- Render results ------------------------------------------------------
function render(data) {
  const { answer, results } = data;

  // LLM answer (render markdown bold/italic; esc() already ran inside mdToHtml)
  if (queryLabel) queryLabel.textContent = query;
  if (llmPara)    llmPara.innerHTML = mdToHtml(answer);

  // Split results: exhibits get the main column, everything else the sidebar
  const exhibits = results.filter((r) => r.type === "exhibit" || r.type === "yes-unit");
  const docs     = results.filter((r) => !exhibits.includes(r));

  // Main column: replace static articles
  if (mainResults) {
    const existing = mainResults.querySelectorAll("article.exhibit-result");
    existing.forEach((el) => el.remove());
    if (exhibits.length) {
      const frag = document.createDocumentFragment();
      exhibits.forEach((r) => {
        const div = document.createElement("div");
        div.innerHTML = buildExhibitCard(r);
        frag.appendChild(div.firstElementChild);
      });
      mainResults.appendChild(frag);
    } else {
      mainResults.insertAdjacentHTML("beforeend",
        '<p class="no-results">No exhibit or YES unit results for this query.</p>');
    }
  }

  // Sidebar resource results
  if (sideResults) {
    sideResults.querySelectorAll(".doc").forEach((el) => el.remove());
    if (docs.length) {
      docs.forEach((r) => sideResults.insertAdjacentHTML("beforeend", buildDocCard(r)));
    } else {
      sideResults.insertAdjacentHTML("beforeend",
        '<p class="no-results">No additional resources found.</p>');
    }
  }
}

function setStatus(msg) {
  if (llmPara) llmPara.textContent = msg;
}

function renderError(msg) {
  if (queryLabel) queryLabel.textContent = query || "Search";
  if (llmPara)    llmPara.textContent = msg;
}

// --- Vector search helpers -----------------------------------------------
function dot(a, b) {
  let s = 0;
  for (let i = 0; i < a.length; i++) s += a[i] * b[i];
  return s;
}

function vectorSearch(queryVec, docs, persona) {
  const allowed = PERSONA_TYPES[persona] || null;
  return docs
    .filter((d) => allowed === null || allowed.includes(d.type))
    .map((d) => ({ doc: d, score: dot(queryVec, d.embedding) }))
    .sort((a, b) => b.score - a.score)
    .slice(0, TOP_K);
}

// --- Main search flow ----------------------------------------------------
async function runSearch() {
  if (!query) {
    renderError("No query provided. Please use the search box and try again.");
    return;
  }

  if (queryLabel) queryLabel.textContent = "Searching…";
  setStatus("⏳ Loading search index…");

  // 1. Fetch index and load Transformers.js in parallel
  let indexDocs, lib;
  try {
    [indexDocs, lib] = await Promise.all([
      fetch(INDEX_URL).then((r) => { if (!r.ok) throw new Error(`index.json: HTTP ${r.status}`); return r.json(); }),
      import(TRANSFORMERS_URL),
    ]);
    lib.env.allowLocalModels = false;
  } catch (err) {
    // Fall back to keyword-only retrieval on the server
    setStatus("⏳ Using server-side search…");
    return serverFallback();
  }

  // 2. Load the embedding model (downloads once, then cached)
  let embedder;
  try {
    setStatus("⏳ Starting embedding model…");
    embedder = await lib.pipeline("feature-extraction", MODEL, {
      progress_callback: (p) => {
        if (p.status === "progress" && p.file) {
          const pct = Math.round(p.progress || 0);
          setStatus(`⏳ Loading model: ${p.file.split("/").pop()} ${pct}%`);
        }
      },
    });
  } catch (err) {
    setStatus("⏳ Using server-side search…");
    return serverFallback();
  }

  // 3. Embed the query in the browser
  setStatus("⏳ Ranking results…");
  const output = await embedder(query, { pooling: "mean", normalize: true });
  const queryVec = Array.from(output.data);

  // 4. Cosine-rank, filtered by persona
  const ranked = vectorSearch(queryVec, indexDocs, audience);
  const doc_ids = ranked.map((r) => r.doc.id);

  // 5. Ask PHP for the LLM answer, sending the ranked IDs
  setStatus("⏳ Generating AI answer…");
  try {
    const res = await fetch(ASK_URL, {
      method:  "POST",
      headers: { "Content-Type": "application/json" },
      body:    JSON.stringify({ query, persona: audience, doc_ids }),
    });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    render(await res.json());
  } catch (err) {
    // Server call failed — render vector results without an LLM answer
    if (queryLabel) queryLabel.textContent = query;
    render({ answer: "(AI answer unavailable — showing search results only)", results: ranked.map((r) => ({
      id: r.doc.id, title: r.doc.title, category: r.doc.category,
      type: r.doc.type, url: r.doc.url, score: r.score,
      snippet: r.doc.text.slice(0, 200),
    }))});
  }
}

// Pure server fallback: keyword search + LLM via PHP alone
function serverFallback() {
  fetch(ASK_URL, {
    method:  "POST",
    headers: { "Content-Type": "application/json" },
    body:    JSON.stringify({ query, persona: audience }),
  })
    .then((res) => { if (!res.ok) throw new Error(`HTTP ${res.status}`); return res.json(); })
    .then(render)
    .catch((err) => renderError(`Search failed: ${err.message}. Please try again.`));
}

runSearch();
