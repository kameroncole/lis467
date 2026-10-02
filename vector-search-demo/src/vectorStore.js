// Vectors produced by embedText() are already L2-normalized, so the dot
// product below *is* the cosine similarity (no extra magnitude division needed).
export function cosineSimilarity(a, b) {
  let dot = 0;
  for (let i = 0; i < a.length; i++) {
    dot += a[i] * b[i];
  }
  return dot;
}

export function semanticSearch(queryVector, indexedDocs, topK = 5) {
  return indexedDocs
    .map((doc) => ({
      id: doc.id,
      title: doc.title,
      category: doc.category,
      text: doc.text,
      score: cosineSimilarity(queryVector, doc.embedding)
    }))
    .sort((a, b) => b.score - a.score)
    .slice(0, topK);
}

// Naive exact/substring match, shown side-by-side to contrast with semantic search.
export function keywordSearch(query, docs, topK = 5) {
  const terms = query.toLowerCase().split(/\s+/).filter(Boolean);
  return docs
    .map((doc) => {
      const haystack = `${doc.title} ${doc.text}`.toLowerCase();
      const matches = terms.filter((term) => haystack.includes(term)).length;
      return { id: doc.id, title: doc.title, category: doc.category, text: doc.text, score: matches };
    })
    .filter((doc) => doc.score > 0)
    .sort((a, b) => b.score - a.score)
    .slice(0, topK);
}
