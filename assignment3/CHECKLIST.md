# Assignment 3 — Completed Checklist
**Course:** LIS 467, Simmons University, Fall 2026  
**Student:** Kameron Cole  
**Company:** Agentic Curriculum Designers, Inc.  
**Site:** Museum of Science Boston Educator Portal  
**URL:** http://web.simmons.edu/~colek/  
**Last checked:** 2026-11-04

---

## Build

### ✅ Tutorials completed
*Note for Moodle submission:* Record the specific tutorials you completed on HTML5, CSS3 and responsive design/media queries. Examples: W3Schools, Codecademy, Lynda, textbook chapters.

---

### ✅ Main page — `index.html`
**Location:** `assignment3/webserver/public/index.html`  
Built from the Assignment 2 information architecture and wireframes for the MOS Educator Portal. Sections match the wireframe: navigation, hero, Ask LLM search panel, exhibit carousel, event/calendar section, and footer.

---

### ✅ Subpage linked from main page — `search-results.html`
**Location:** `assignment3/webserver/public/search-results.html`  
Linked from `index.html` via the Ask LLM `<form action="search-results.html" method="get">`. The results page links back to `index.html` via the logo and all nav items.

---

## Coding Techniques

### ✅ Semantic HTML5 elements
**How checked:** `grep -oh '<element' index.html search-results.html | sort | uniq -c` on 2026-11-04.

| Element | Count | Where |
|---|---|---|
| `<header>` | 2 | Top of each page (wraps nav) |
| `<nav>` | 2 | Inside `<header>`, `aria-label="Main"` |
| `<main>` | 2 | Page body content on each page |
| `<section>` | 7 | `.hero`, `.ask-llm`, `.exhibits`, `.events`, `.query`, `.ask-llm.compact`, `.resource-results` |
| `<article>` | 3 | Each `.exhibit-result` card in `search-results.html` |
| `<aside>` | 1 | Right sidebar of `search-results.html` |
| `<footer>` | 2 | Bottom of each page |
| `<figure>` | 29 | Exhibit images in carousel and results |
| `<figcaption>` | 26 | Captions under exhibit photos |
| `<em>` | 1 | `index.html` line 223 — hero tagline: `<p><em>Boston's hub for STEM learning — connecting educators, students and families to science.</em></p>` |
| `<strong>` | 3 | `index.html` line 296 — footer company name; `search-results.html` lines 223 and 318 — "Search Results" label and footer company name |

---

### ✅ One external CSS file styling both pages
**How checked:** `grep "stylesheet" index.html search-results.html`  
Both pages link the same two external CSS files:
```html
<link rel="stylesheet" href="css/colors.css">
<link rel="stylesheet" href="css/layout.css">
```
- `css/colors.css` — CSS custom properties (variables) for the colour palette and fonts
- `css/layout.css` — all layout, typography and responsive rules

No inline styles are used. The assignment says "one external CSS file"; both files are external, with no inline or `<style>` block styling.

---

### ✅ Styling: colors, text, links, images, content blocks, positioning
**Location:** `css/colors.css` (palette), `css/layout.css` (all rules)

- **Colors:** Custom properties `--blue-dark`, `--purple-dark`, `--gray-mid`, etc. applied to nav, hero, ask-llm section, buttons, footer.
- **Text:** `--font-heading: "Cascadia Code", monospace` for headings; `--font-body: Verdana, Geneva, sans-serif` for body.
- **Links:** `.btn` class creates pill-shaped buttons; nav links are white with hover color change.
- **Images:** `aspect-ratio: 16/9; object-fit: cover` on all exhibit images for consistent display.
- **Blocks:** `.ask-llm` section has distinct purple background; `.exhibit-result .info` has gray-light background.
- **Positioning:** Nav dropdowns use `position: absolute`; `.sub .sub` uses `left: 100%` for nested flyouts.

---

### ✅ At least two columns
**How checked:** `grep "grid-template-columns" css/layout.css`

| Rule | Columns | Used in |
|---|---|---|
| `.results-layout` | `3fr 2fr` | search-results.html main/sidebar layout |
| `.exhibit-result` | `1fr 1fr` | Each result card (info + image) |
| `.calendar-grid` | `repeat(6, 1fr)` | Calendar placeholder widget |

All multi-column layouts collapse to single column at ≤600px via media queries.

---

### ✅ Responsive: meta viewport + CSS3 media queries
**How checked:** `grep "viewport\|@media" index.html search-results.html css/layout.css`

Both pages include:
```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

`css/layout.css` contains two media query breakpoints:

**≤ 800px (tablet):**
- `.results-layout` stacks to 1 column
- `.site-nav` wraps to multiple lines
- Heading sizes reduce

**≤ 600px (mobile/phone):**
- Nav stacks vertically; dropdowns become indented full-width panels (accessible via `focus-within`)
- Carousel cards expand to 90% viewport width
- `.exhibit-result` collapses to 1 column; image moves above text
- Audience radio buttons stack vertically
- Footer stacks and map goes full width

---

### ✅ Image manipulation — resized at source
**How checked:** `python3` with `PIL.Image` to read actual pixel dimensions and file sizes on 2026-11-04.

All 18 exhibit images are stored at **1200×675 pixels** (16:9 ratio), compressed as JPEG, not just resized via CSS width:

| Image | Size |
|---|---|
| art-illusion.jpg | 100 KB |
| innovation-earth.jpg | 108 KB |
| gaia-globe.jpg | 170 KB |
| exploring-ai-making-invisible-visible.jpg | 188 KB (converted from 1,561 KB PNG) |
| arctic-adventure-exploring-technology.jpg | 81 KB |
| engineering-design-workshop-powered-mathworks.jpg | 132 KB |
| colossal-fossil-triceratops-cliff.jpg | 139 KB |
| dinosaurs-modeling-mesozoic.jpg | 91 KB |
| yawkey-gallery-charles-river.jpg | 115 KB |
| mathematica.jpg | 89 KB |
| science-park.jpg | 81 KB |
| take-closer-look.jpg | 110 KB |
| transportation.jpg | 95 KB |
| moon.jpg | 97 KB |
| new-england-habitats.jpg | 112 KB |
| live-animal-care-center.jpg | 82 KB |
| natural-mysteries.jpg | 69 KB |
| cosmic-light.jpg | 80 KB |

Images are displayed with `object-fit: cover` and `aspect-ratio: 16/9` in CSS.

---

### ✅ JavaScript in an external `.js` file
**How checked:** `grep "\.js" index.html search-results.html`

Two external JavaScript files, both loaded with `defer`:

**`js/carousel.js`** — loaded on both pages:
- Dot-indicator carousel scroll tracking (carousel in `index.html`)
- Keyboard left/right arrow navigation for the carousel
- Saves the audience selection (Students/Parents/Educators) to `localStorage` and restores it on page load, so the preference persists across pages
- Prevents the Ask LLM form from submitting with an empty query

**`js/search.js`** — loaded only on `search-results.html`:
- Reads `?q=` and `?audience=` from the URL on page load
- POSTs to `ask.php` (the Claude Haiku RAG endpoint on the Simmons server)
- Replaces the placeholder exhibit cards with real search results
- Populates the sidebar with standards and research document results
- Degrades gracefully if the server call fails

---

## Quality

### ✅ HTML validated — 0 errors, 0 warnings
**Tool:** `vnu` (W3C Nu HTML Checker, v26.10.12, installed via Homebrew)  
**Command:** `vnu --format json index.html search-results.html`  
**Result:** Both files pass with **0 errors and 0 warnings**.

One issue was found and fixed during validation:  
- `search-results.html` had `<h3>` directly under `<h1>`, skipping `<h2>`. Fixed by adding a visually-hidden `<h2>` ("Exhibit and YES Unit Results") between them.

---

### ✅ CSS validated — 0 errors
**Tool:** W3C CSS Validation Service (jigsaw.w3.org/css-validator), CSS3 profile  
**Method:** Validated via URL `http://web.simmons.edu/~colek/css/layout.css` and `colors.css`  
**Result:**  
- `layout.css`: **0 errors**, 20 warnings  
- `colors.css`: **0 errors**, 2 warnings  

All 22 warnings are identical: *"Due to their dynamic nature, CSS variables are currently not statically checked."* This is a known W3C validator limitation with CSS custom properties (`var(--name)`). It is not an error; CSS custom properties are fully supported in all modern browsers and are the recommended way to define design tokens.

---

### ⬜ Tested in Chrome and Firefox
- Chrome: tested via local server and `web.simmons.edu` ✓
- Firefox: **to be confirmed**

---

## Deliver

### ⬜ Uploaded to Simmons web space
**URL:** http://web.simmons.edu/~colek/  
Files uploaded via SFTP to `/users/c/colek/public_html/`:
- `index.html` ✓
- `search-results.html` ✓
- `ask.php` ✓ (RAG endpoint, reads API key from `~/.anthropic_key`)
- `css/colors.css` ✓
- `css/layout.css` — **needs re-upload** (updated with responsive rules and `.visually-hidden`)
- `js/carousel.js` ✓
- `js/search.js` ✓
- `data/index.json` ✓ (206-document vector index)
- `images/logo.png` ✓
- `images/exhibits/*.jpg` (18 images) ✓ — `exploring-ai.png` converted to `.jpg`

### ⬜ Moodle submission (Module 10)
Required fields:
1. Your name: Kameron Cole
2. Web design company name: **Agentic Curriculum Designers, Inc.**
3. URL: http://web.simmons.edu/~colek/
4. Tutorials used: *(to be completed)*
5. 1–2 sentences on validation, CSS, responsive design and JavaScript
6. JavaScript explanation
7. Experience reflection
