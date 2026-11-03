// Browser-side test of the vector search stack. Runs on any static host: no Node.js or PHP needed.
const TRANSFORMERS_URL = "https://cdn.jsdelivr.net/npm/@xenova/transformers@2.17.2";
const MODEL = "Xenova/all-MiniLM-L6-v2";
const INDEX_URL = "data/index.json";

const checksEl = document.getElementById("checks");
const summaryEl = document.getElementById("summary");
const resultsEl = document.getElementById("results");
const form = document.getElementById("search-form");
const queryInput = document.getElementById("query");
const goButton = document.getElementById("go");

const state = { docs: null, embedder: null };
let failures = 0;

function addRow(name) {
  const tr = document.createElement("tr");
  const nameCell = document.createElement("td");
  const resultCell = document.createElement("td");
  const detailCell = document.createElement("td");
  nameCell.textContent = name;
  resultCell.textContent = "running...";
  resultCell.className = "wait";
  tr.append(nameCell, resultCell, detailCell);
  checksEl.appendChild(tr);
  return {
    detail: (text) => { detailCell.textContent = text; },
    done: (ok, text) => {
      resultCell.textContent = ok ? "PASS" : "FAIL";
      resultCell.className = ok ? "pass" : "fail";
      if (text) detailCell.textContent = text;
    },
  };
}

async function check(name, fn) {
  const row = addRow(name);
  const started = performance.now();
  try {
    const detail = await fn(row.detail);
    row.done(true, `${detail} (${((performance.now() - started) / 1000).toFixed(1)}s)`);
    return true;
  } catch (err) {
    failures += 1;
    row.done(false, String(err && err.message ? err.message : err));
    return false;
  }
}

function dot(a, b) {
  let sum = 0;
  for (let i = 0; i < a.length; i++) sum += a[i] * b[i];
  return sum;
}

async function embed(text) {
  const output = await state.embedder(text, { pooling: "mean", normalize: true });
  return Array.from(output.data);
}

function search(queryVector, topK = 5) {
  return state.docs
    .map((doc) => ({ doc, score: dot(queryVector, doc.embedding) }))
    .sort((a, b) => b.score - a.score)
    .slice(0, topK);
}

function renderResults(results) {
  resultsEl.replaceChildren();
  for (const { doc, score } of results) {
    const li = document.createElement("li");
    const link = document.createElement("a");
    link.href = doc.url;
    link.textContent = doc.title;
    link.target = "_blank";
    link.rel = "noopener";
    const meta = document.createElement("div");
    meta.textContent = `${score.toFixed(3)} · ${doc.type} · ${doc.category}`;
    li.append(link, meta);
    resultsEl.appendChild(li);
  }
}

async function run() {
  await check("Page served over http(s)", async () => {
    if (location.protocol === "file:") {
      throw new Error("Opened from disk. Upload to the web server (or use a local web server) and reload.");
    }
    return `${location.protocol}//${location.host}${location.pathname} (secure context: ${window.isSecureContext})`;
  });

  await check("ES modules and WebAssembly supported by this browser", async () => {
    if (typeof WebAssembly !== "object") throw new Error("WebAssembly is not available");
    return navigator.userAgent;
  });

  await check("Load data/index.json from the server", async (detail) => {
    detail("downloading...");
    const resp = await fetch(INDEX_URL, { cache: "no-store" });
    if (!resp.ok) throw new Error(`HTTP ${resp.status} for ${INDEX_URL}`);
    const type = resp.headers.get("content-type") || "unknown content-type";
    state.docs = await resp.json();
    const dims = state.docs[0].embedding.length;
    if (dims !== 384) throw new Error(`Expected 384-dimension vectors, got ${dims}`);
    return `${state.docs.length} documents, ${dims}-dimension vectors, ${type}`;
  });

  let lib = null;
  await check("Load Transformers.js from the CDN", async () => {
    lib = await import(TRANSFORMERS_URL);
    lib.env.allowLocalModels = false;
    return `@xenova/transformers 2.17.2 from ${new URL(TRANSFORMERS_URL).host}`;
  });

  await check("Download and start the embedding model", async (detail) => {
    if (!lib) throw new Error("Skipped: Transformers.js did not load");
    const seen = {};
    state.embedder = await lib.pipeline("feature-extraction", MODEL, {
      progress_callback: (p) => {
        if (p.status === "progress" && p.file) {
          seen[p.file] = Math.round(p.progress);
          detail(Object.entries(seen).map(([f, pct]) => `${f.split("/").pop()} ${pct}%`).join(", "));
        }
      },
    });
    return `${MODEL} ready`;
  });

  await check("Embed a query (384 numbers, unit length)", async () => {
    if (!state.embedder) throw new Error("Skipped: model did not load");
    const v = await embed("hands-on engineering for kids");
    const norm = Math.sqrt(dot(v, v));
    if (v.length !== 384 || Math.abs(norm - 1) > 1e-3) throw new Error(`length ${v.length}, norm ${norm}`);
    return `length ${v.length}, norm ${norm.toFixed(4)}`;
  });

  await check("Browser vectors match the index built in Node", async () => {
    if (!state.embedder || !state.docs) throw new Error("Skipped: model or index not loaded");
    const sims = [];
    for (const doc of state.docs.slice(0, 3)) {
      const v = await embed(`${doc.title}. ${doc.text}`);
      sims.push(dot(v, doc.embedding));
    }
    const min = Math.min(...sims);
    if (min < 0.99) throw new Error(`similarity to stored vectors only ${min.toFixed(4)}`);
    return `cosine similarity to stored vectors: ${sims.map((s) => s.toFixed(4)).join(", ")}`;
  });

  await check("Semantic search returns relevant results", async () => {
    if (!state.embedder || !state.docs) throw new Error("Skipped: model or index not loaded");
    const results = search(await embed("earthquake-proof buildings for kids"));
    renderResults(results);
    if (!results.slice(0, 3).some((r) => /earthquake/i.test(r.doc.title))) {
      throw new Error(`Top results do not mention earthquakes: ${results.map((r) => r.doc.title).join(" | ")}`);
    }
    return `top result: ${results[0].doc.title}`;
  });

  if (failures === 0) {
    summaryEl.textContent = "All checks passed: this server can host the in-browser vector search.";
    summaryEl.className = "pass";
  } else {
    summaryEl.textContent = `${failures} check(s) failed. See the details column.`;
    summaryEl.className = "fail";
  }
  goButton.disabled = !(state.embedder && state.docs);
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  const query = queryInput.value.trim();
  if (!query) return;
  goButton.disabled = true;
  renderResults(search(await embed(query)));
  goButton.disabled = false;
});

run();
