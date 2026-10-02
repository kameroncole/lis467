const form = document.getElementById("search-form");
const input = document.getElementById("query");
const semanticList = document.getElementById("semantic-results");
const keywordList = document.getElementById("keyword-results");

function renderResults(listEl, results) {
  listEl.innerHTML = "";
  if (!results.length) {
    listEl.innerHTML = '<li class="empty">No results</li>';
    return;
  }
  for (const r of results) {
    const li = document.createElement("li");
    li.innerHTML = `
      <span class="score">${r.score.toFixed(3)}</span>
      <div class="title">${r.title}</div>
      <div class="category">${r.category}</div>
      <div class="text">${r.text}</div>
    `;
    listEl.appendChild(li);
  }
}

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const query = input.value.trim();
  if (!query) return;

  semanticList.innerHTML = '<li class="empty">Searching...</li>';
  keywordList.innerHTML = '<li class="empty">Searching...</li>';

  const res = await fetch(`/api/search?q=${encodeURIComponent(query)}&k=5`);
  const data = await res.json();

  renderResults(semanticList, data.semantic);
  renderResults(keywordList, data.keyword);
});
