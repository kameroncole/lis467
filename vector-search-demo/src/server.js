import express from "express";
import { readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { embedText } from "./embeddings.js";
import { semanticSearch, keywordSearch } from "./vectorStore.js";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const INDEX_PATH = path.join(__dirname, "..", "data", "index.json");

const app = express();
app.use(express.json());
app.use(express.static(path.join(__dirname, "..", "public")));

let indexedDocs = [];

app.get("/api/search", async (req, res) => {
  const query = (req.query.q || "").trim();
  if (!query) {
    return res.status(400).json({ error: "Missing query parameter 'q'" });
  }

  const topK = Number(req.query.k) || 5;
  const queryVector = await embedText(query);

  res.json({
    query,
    semantic: semanticSearch(queryVector, indexedDocs, topK),
    keyword: keywordSearch(query, indexedDocs, topK)
  });
});

app.get("/api/health", (req, res) => {
  res.json({ status: "ok", documentsIndexed: indexedDocs.length });
});

const PORT = process.env.PORT || 3000;

async function start() {
  try {
    indexedDocs = JSON.parse(await readFile(INDEX_PATH, "utf-8"));
  } catch {
    console.error(
      `Could not read ${INDEX_PATH}. Run "npm run build-index" first to generate embeddings.`
    );
    process.exit(1);
  }

  app.listen(PORT, () => {
    console.log(`Vector search demo running at http://localhost:${PORT}`);
    console.log(`Loaded ${indexedDocs.length} indexed documents.`);
  });
}

start();
