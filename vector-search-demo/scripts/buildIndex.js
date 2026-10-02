import { readFile, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { embedText } from "../src/embeddings.js";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const DOCS_PATH = path.join(__dirname, "..", "data", "documents.json");
const INDEX_PATH = path.join(__dirname, "..", "data", "index.json");

async function main() {
  const docs = JSON.parse(await readFile(DOCS_PATH, "utf-8"));
  console.log(`Embedding ${docs.length} documents with Xenova/all-MiniLM-L6-v2...`);

  const indexed = [];
  for (const doc of docs) {
    const embedding = await embedText(`${doc.title}. ${doc.text}`);
    indexed.push({ ...doc, embedding });
    console.log(`  embedded ${doc.id}: ${doc.title}`);
  }

  await writeFile(INDEX_PATH, JSON.stringify(indexed, null, 2));
  console.log(`Wrote vector index to ${INDEX_PATH}`);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
