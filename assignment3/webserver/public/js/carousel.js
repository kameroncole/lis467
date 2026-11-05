/**
 * carousel.js — exhibit carousel with keyboard and touch support.
 * Required for assignment: external JavaScript file.
 * Also persists audience preference and validates the Ask LLM form.
 */

// --- Carousel ------------------------------------------------------------
(function () {
  const carousel = document.querySelector(".carousel");
  if (!carousel) return;

  const dots = document.querySelectorAll(".dots span");
  const cards = carousel.querySelectorAll(".card");

  function updateDots() {
    const idx = Math.round(carousel.scrollLeft / carousel.scrollWidth * dots.length);
    dots.forEach((d, i) => d.classList.toggle("active", i === idx));
  }

  dots.forEach((dot, i) => {
    dot.addEventListener("click", () => {
      const target = (carousel.scrollWidth / dots.length) * i;
      carousel.scrollTo({ left: target, behavior: "smooth" });
    });
  });

  carousel.addEventListener("scroll", updateDots, { passive: true });
  updateDots();

  // Keyboard: left/right arrows scroll the carousel when it has focus
  carousel.setAttribute("tabindex", "0");
  carousel.setAttribute("role", "region");
  carousel.setAttribute("aria-label", "Museum exhibits carousel");
  carousel.addEventListener("keydown", (e) => {
    const card = cards[0];
    if (!card) return;
    if (e.key === "ArrowRight") carousel.scrollBy({ left: card.offsetWidth + 16, behavior: "smooth" });
    if (e.key === "ArrowLeft")  carousel.scrollBy({ left: -(card.offsetWidth + 16), behavior: "smooth" });
  });
})();

// --- Persist audience selection across pages -----------------------------
(function () {
  const KEY = "mos-audience";

  const saved = localStorage.getItem(KEY);
  if (saved) {
    document.querySelectorAll(`input[name="audience"][value="${saved}"]`)
      .forEach((r) => { r.checked = true; });
  }

  document.querySelectorAll('input[name="audience"]').forEach((radio) => {
    radio.addEventListener("change", () => {
      localStorage.setItem(KEY, radio.value);
      // On the results page, switching audience re-runs the current question
      const form = radio.form;
      const q = form && form.querySelector('input[name="q"]');
      if (form && q && q.value.trim() && location.pathname.endsWith("search-results.html")) {
        form.requestSubmit();
      }
    });
  });

  // Require a non-empty query before submitting
  document.querySelectorAll("form").forEach((form) => {
    form.addEventListener("submit", (e) => {
      const q = form.querySelector('input[name="q"]');
      if (q && !q.value.trim()) {
        e.preventDefault();
        q.focus();
        q.setCustomValidity("Please enter a question.");
        q.reportValidity();
      } else if (q) {
        q.setCustomValidity("");
      }
    });
  });
})();
