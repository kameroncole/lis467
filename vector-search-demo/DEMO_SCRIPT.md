# Demo Video Script — Vector Search & Semantic Indexing

Target length: ~6-8 minutes. Record screen + voice (QuickTime/OBS). Have the
PowerPoint deck open for the first ~3 minutes, then switch to terminal/browser.

---

## 1. Slide intro (talking over PowerPoint, ~2 min)

**Say:**
> "Today I'm presenting Vector Search and Semantic Indexing in full-stack
> apps. Traditional databases — relational or document-based — retrieve data
> by exact matches: a SQL `WHERE` clause, a Mongo `$regex`. But modern AI
> applications need to search by *meaning*, not exact words. That's where
> vector embeddings and cosine similarity come in."

Walk through slides: concept → why it matters → architecture diagram →
where this fits in a full stack (Node.js backend, JSON documents, embedding
model, vector index).

**Say (transition to demo):**
> "Let's see this in action with a small Node.js app I built. It has 16
> documents on different topics, and we'll compare keyword search against
> semantic search on the same query."

## 2. Show the dataset (~30 sec)

Open `data/documents.json` in the editor. Scroll through a few entries.

**Say:**
> "Here's our document collection — library science, computer science,
> history, cooking, gardening topics. Just plain JSON, no special format."

## 3. Show the indexing step (~1 min)

Open `scripts/buildIndex.js` and `src/embeddings.js` briefly.

**Say:**
> "To make these searchable by meaning, each document gets converted into a
> 384-number vector using a local embedding model — all-MiniLM-L6-v2, running
> right in Node.js via transformers.js. No API key, no cloud call. This
> vector captures the semantic content of the text."

Run in terminal (if not already built):
```bash
npm run build-index
```

**Say:**
> "That produces index.json — same documents, but now each one carries its
> embedding vector alongside it."

## 4. Show the search logic (~1 min)

Open `src/vectorStore.js`.

**Say:**
> "At query time, we embed the user's search text the same way, then compute
> cosine similarity between the query vector and every document vector.
> Since our vectors are normalized, that's just a dot product. Sort by score,
> take the top K — that's the whole algorithm. Compare that to keyword
> search right next to it, which is just counting substring matches."

## 5. Live demo in the browser (~2-3 min) — the core "wow" moment

Run:
```bash
npm start
```
Open `http://localhost:3000`.

**Query 1 — weak keyword overlap:**
Type: `organizing books so people can find them`

**Say:**
> "Notice this query shares almost no words with any document title. Watch
> what keyword search returns on the right — [read the irrelevant result,
> e.g. French Pastry]. Now look at semantic search on the left — it correctly
> surfaces 'Cataloging and Classification in Libraries,' because the *meaning*
> of the query matches, even though the words don't."

**Query 2 — reinforce the pattern:**
Type: `turning food scraps into soil`

**Say:**
> "Same pattern — semantic search finds 'Composting for Beginners' instantly.
> Keyword search has nothing to work with."

**Query 3 (optional) — show where keyword search *does* work, for balance:**
Type: `machine learning`

**Say:**
> "When the query word appears literally in the text, both approaches find
> it — keyword search isn't useless, it's just blind to synonyms, paraphrase,
> and conceptual similarity. That's the gap semantic search fills."

## 6. Wrap-up / real-world connection (~30-45 sec, back to slides or camera)

**Say:**
> "In production, you wouldn't loop over every document — you'd use an
> approximate nearest-neighbor index like HNSW, available in MongoDB Atlas
> Vector Search or PostgreSQL's pgvector extension. And this retrieval step
> is exactly what powers retrieval-augmented generation — RAG — where an LLM
> answers questions grounded in your own documents instead of just its
> training data. That's the bridge between full-stack database skills and
> modern AI application architecture."

**Closing line:**
> "Full code is in the repo — thanks for watching."

---

## Recording checklist

- [ ] Close unrelated browser tabs/terminal history before recording
- [ ] Pre-run `npm run build-index` once before recording (model download can
      take a minute on first run — don't do this live)
- [ ] Increase terminal/editor font size for screen recording legibility
- [ ] Test both demo queries beforehand to confirm current result ordering
- [ ] Keep `npm start` running in one terminal tab throughout the demo
