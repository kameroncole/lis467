# Vector Search & Semantic Indexing Demo

A minimal Node.js app that demonstrates **semantic search** (vector embeddings +
cosine similarity) side-by-side with **naive keyword search**, over a small
collection of JSON documents. No external database or API key required —
embeddings are generated locally in Node using [`@xenova/transformers`](https://github.com/xenova/transformers.js)
(a JS port of Hugging Face `sentence-transformers`, model: `all-MiniLM-L6-v2`, 384 dimensions).

## Why this matters (the concept)

Traditional search (SQL `LIKE`, Mongo `$regex`, full-text indexes) matches
**exact words**. Semantic search instead converts text into a high-dimensional
vector ("embedding") that captures *meaning*. Two sentences with zero words in
common — "organizing books so people can find them" and "cataloging and
classification in libraries" — land close together in vector space, so cosine
similarity ranks them as related even though keyword search can't connect them
at all. This is the foundation of retrieval-augmented generation (RAG) in
production systems (MongoDB Atlas Vector Search, PostgreSQL `pgvector`,
Pinecone, Milvus, etc.) — this demo reimplements the same idea in plain
JavaScript so the mechanics are visible.

## Project structure

```
vector-search-demo/
├── data/
│   ├── documents.json   # 16 sample documents (source of truth)
│   └── index.json       # generated: documents + embeddings (gitignored)
├── scripts/
│   └── buildIndex.js    # embeds documents.json -> index.json
├── src/
│   ├── embeddings.js    # loads the local transformer model, embeds text
│   ├── vectorStore.js   # cosine similarity + semantic/keyword search
│   └── server.js        # Express API: GET /api/search?q=...
├── public/              # simple browser UI (side-by-side comparison)
└── matlab/
    └── build_embeddings_demo.m   # standalone MATLAB version: builds + visualizes the vector space
```

## Setup

```bash
npm install
npm run build-index   # downloads the model on first run, embeds all documents
npm start              # http://localhost:3000
```

Open `http://localhost:3000` in a browser, or query the API directly:

```bash
curl "http://localhost:3000/api/search?q=computers%20that%20learn%20from%20data&k=3"
```

## Good demo queries (no shared words with the target doc)

| Query | Expected top semantic hit | Keyword search result |
|---|---|---|
| `computers that learn from data` | *Introduction to Machine Learning* | Also finds it (shares "computers", "learn", "data") — use for a baseline |
| `organizing books so people can find them` | *Cataloging and Classification in Libraries* | Finds unrelated docs ("French Pastry", "Machine Learning") on weak word overlap |
| `turning food scraps into soil` | *Composting for Beginners* | Little/no overlap, weak or empty results |
| `stone walls built to defend territory` | *Medieval Castles and Fortifications* | Weak/empty results |

The second and third rows are the strongest "wow" moments — semantic search
finds the right document while keyword search returns nothing or something
wrong.

## How it works

1. **Indexing** (`scripts/buildIndex.js`): each document's title + text is run
   through the embedding model, producing a 384-dimension vector. Vectors are
   stored alongside the original document in `data/index.json`.
2. **Query time** (`src/server.js`): the incoming query string is embedded the
   same way, then compared against every stored vector using **cosine
   similarity** (`src/vectorStore.js`). Because vectors are L2-normalized, cosine
   similarity is just the dot product. Results are sorted by score, descending.
3. **Keyword search** is implemented naively (substring match count) purely as
   a contrast baseline — not a production-grade text search.

## Mapping to real-world systems

| This demo | Production equivalent |
|---|---|
| `data/index.json` flat array | MongoDB Atlas Vector Search index / pgvector column |
| In-memory cosine similarity loop | HNSW / IVFFlat approximate nearest-neighbor index |
| `@xenova/transformers` local model | OpenAI/Cohere embeddings API, or a hosted embedding model |
| `GET /api/search` | A RAG retrieval endpoint feeding results into an LLM prompt |

## MATLAB companion demo

`matlab/build_embeddings_demo.m` is a standalone script (core MATLAB only, no
toolboxes required) that builds a high-dimensional embedding space from the
same `data/documents.json` dataset, using TF-IDF vectors instead of a neural
model — simpler math, same underlying idea. It then:

- Reduces the space to 2D with SVD (the math behind PCA) and plots every
  document, colored by category, so you can **see** semantically similar
  documents cluster together.
- Embeds a query the same way and ranks documents by cosine similarity,
  mirroring `src/vectorStore.js`.

Run it in MATLAB:
```matlab
cd matlab
build_embeddings_demo
```

## Known limitations (for class discussion)

- Brute-force O(n) similarity scan — fine for 16 docs, not for millions (real
  systems use ANN indexes like HNSW).
- `npm audit` flags transitive vulnerabilities in `onnxruntime-web`/`sharp`
  (pulled in by `@xenova/transformers` for local model execution). They are
  not reachable via user input in this demo but would need review before any
  production use.
- No persistence/database — this is intentionally a teaching-sized example.
