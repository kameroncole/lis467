/**
 * search.js — wires search-results.html to ask.php.
 *
 * On page load:
 *   1. Reads ?q= and ?audience= from the URL.
 *   2. POSTs to ask.php and receives { answer, persona, results[] }.
 *   3. Replaces the placeholder content with real results and the LLM answer.
 *
 * The PHP endpoint (ask.php) does keyword retrieval from index.json and
 * calls Claude Haiku. If the endpoint fails, results degrade gracefully.
 */

const ASK_URL = "ask.php";   // relative — works on any host

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
  const imgSrc = exhibitImgSrc(r.title);
  return `
    <article class="exhibit-result">
      <div class="info">
        <h3><a href="${esc(r.url)}" target="_blank" rel="noopener">${esc(r.title)}</a></h3>
        <p>${esc(r.snippet)}</p>
        <p class="standards">${esc(r.category)}</p>
        <a class="btn" href="${esc(r.url)}" target="_blank" rel="noopener">More</a>
      </div>
      <figure>
        <img src="${esc(imgSrc)}" alt="${esc(r.title)}" loading="lazy"
             onerror="this.closest('figure').innerHTML='<div class=placeholder-img>${esc(r.title)}</div>'">
        <small class="credit">Photo: Museum of Science</small>
      </figure>
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

// --- Render results ------------------------------------------------------
function render(data) {
  const { answer, results } = data;

  // LLM answer
  if (queryLabel) queryLabel.textContent = query;
  if (llmPara)    llmPara.textContent = answer;

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

function renderError(msg) {
  if (queryLabel) queryLabel.textContent = query;
  if (llmPara)    llmPara.textContent = msg;
}

// --- Fetch results -------------------------------------------------------
if (!query) {
  renderError("No query provided. Please use the search box and try again.");
} else {
  if (queryLabel) queryLabel.textContent = "Searching…";
  if (llmPara)    llmPara.textContent   = "";

  fetch(ASK_URL, {
    method:  "POST",
    headers: { "Content-Type": "application/json" },
    body:    JSON.stringify({ query, persona: audience }),
  })
    .then((res) => {
      if (!res.ok) throw new Error(`Server error: HTTP ${res.status}`);
      return res.json();
    })
    .then(render)
    .catch((err) => renderError(`Search failed: ${err.message}. Please try again.`));
}
