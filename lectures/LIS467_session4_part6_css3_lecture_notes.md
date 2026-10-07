# LIS 467 — Session 4, Part 6: CSS3

**Course:** LIS 467 — Web Development & Information Architecture
**Topic:** Separating content from design, what CSS is, selectors/properties/values, where CSS lives, CSS modules and standards maturity, learning resources, and media queries for responsive design
**Source:** Panopto lecture transcript — "Session 4 Part 6 CSS3"

---

## 1. Design and Development Each Week

Each week the course covers **some design elements** and **some development elements**. This week's development focus: after learning HTML, begin **CSS3** — **a lot to learn**.

---

## 2. The Big Idea: Separate Content from Design

🔑 **CSS (Cascading Style Sheets)** separates **content** from **presentation**:

| Layer | Technology | Role |
|-------|-----------|------|
| **Content / structure** | **HTML** | What the page says |
| **Presentation / design** | **CSS** | How it looks |

- ⭐ In the old days, **content and design were mixed together**, making changes **very difficult**.
- With CSS, you can **change the design on the fly** without touching the content.
- Because styling lives in style sheets, it can be **reused across multiple pages** — efficient and consistent.

### History and standards

- CSS was proposed by **Håkon Wium Lie** in **1994**.
- It is a **World Wide Web Consortium (W3C)** standard for the **visual presentation of webpages**.
- Formal definition: a **language for describing the rendering of structured documents** (such as HTML and XML) **on screen, on paper**, and in other media.
- It can style **other structured documents** (e.g., XML where tags aren't predefined), not just HTML.

### What CSS can do

- Change **colors**, add **backgrounds and borders**
- Style **fonts, text, and links**
- Control the **entire page layout** and **positioning**
- ⭐ **HTML gives structure; CSS gives beauty.**

---

## 3. Demonstration: CSS Zen Garden

The lecture demonstrates a site (the well-known **CSS Zen Garden**) where the **same HTML content** appears with **completely different designs** just by switching the **style sheet**. The content never changes — only the CSS. This is the clearest demonstration of the **content/design separation**.

---

## 4. Learning CSS

- Go through the **W3Schools CSS tutorial** — you are expected to work through **pretty much the entire tutorial**; you must be **well versed in CSS to succeed in web design and development**.
- Topics in the tutorial, roughly in order of priority:
  1. **Styling basics** — colors, backgrounds, borders, **padding**, **margins**, text, fonts
  2. **Positioning** and the **box model** — an important concept
  3. **Advanced** — animations (do these only if time allows)
  4. **Flexbox** and **CSS Grid** layouts
  5. **Media queries** — essential for **responsive design**
- Other resources: **LinkedIn Learning** (formerly Lynda.com, free through Simmons login), textbooks, and online video courses.

---

## 5. CSS Syntax

🔑 A CSS rule has a **selector**, then a **declaration block** of **property: value** pairs:

```css
selector {
  property: value;
  property: value;
}
```

| Part | Meaning | Example |
|------|---------|---------|
| **Selector** | The **HTML element** (or other target) you want to style | `p`, `body`, `h1` |
| **Property** | The **aspect** you want to change | `color`, `text-align`, `background-color` |
| **Value** | The **setting** for that property | `red`, `center`, `lightblue` |

**Syntax rules:**

- Curly braces `{ }` enclose the declarations.
- A **colon** `:` separates property from value.
- A **semicolon** `;` ends each declaration.

### Example 1: Style all paragraphs

```css
p {
  text-align: center;
  color: red;
}
```

All `<p>` elements on the page become **centered and red**. Change `center` to `left` or `red` to `green` and the page updates **immediately**.

### Example 2: Style the body

```css
body {
  background-color: lightblue;
}
```

Change `lightblue` to `red` and the **entire page background** changes.

### Page structure you can style

Modern HTML5 pages include structural elements such as `header`, `nav`, `section`, `article`, `aside`, and `footer`. **Each can have its own CSS rules** controlling how it looks.

---

## 6. Where CSS Lives

| Method | Location | Notes |
|--------|----------|-------|
| **Inline** | `style="…"` attribute on a single element | Quick, but hard to maintain |
| **Internal** | `<style>` tag in the `<head>` of the HTML file | Good for single pages / demos (the lecture's example uses this) |
| **External** | A **separate `.css` file** linked from the HTML | ✅ **Best practice** — one file styles many pages |

```html
<head>
  <link rel="stylesheet" href="style.css">
</head>
```

---

## 7. CSS Modules and Standards Maturity

CSS is **split into modules** that progress through stages at different rates. The W3C maturity levels:

| Stage | Meaning |
|-------|---------|
| **Working Draft (WD)** | Earliest public stage — still being worked on |
| **Candidate Recommendation (CR)** | **Almost ready** |
| **Proposed Recommendation (PR)** | Close to final approval |
| **Recommendation (REC)** | **Approved — the standard** |

- Examples of modules that reached **Recommendation**: **Media Queries** (June 2012), **Color Level 3** and **Basic User Interface Level 3** (reached REC later, around June 2018).
- **CSS1** covered fundamentals: **fonts, colors, backgrounds, text properties, the cascade**. **CSS2** added **media types, positioning, tables**, and more. **CSS3** is organized into **many modules** (selectors, media queries, color, backgrounds, flexbox, grid, etc.).
- ⭐ Some parts are **stable**, while others are **still changing** — the W3C publishes a **status page** showing each module's current stage.
- Parts of **CSS Grid** and related layout features are newer and still evolving.

---

## 8. Media Queries and Responsive Design

🔑 **Media queries** are a CSS3 module that lets **content rendering adapt to conditions** such as **screen size/resolution** (smartphone vs. tablet vs. desktop). They are the **core technology of responsive design**.

```css
body {
  background-color: white;
}

@media screen and (max-width: 600px) {
  body {
    background-color: lightblue;
  }
  h1 {
    font-size: 1.2em;
  }
}
```

- You specify `@media screen` and a **condition** such as `min-width` / `max-width` in **pixels**.
- Rules inside apply **only when the condition is met** — for example on a phone or an iPad-sized screen.
- ⭐ **Nearly every modern, responsive CSS file contains media queries.**
- Connects to **Session 2** topics: **responsive web design** and **mobile-first** design.

---

## 9. Session 4 Wrap-Up

Today's session covered:

1. **Use cases and scenarios**
2. **Information architecture**
3. **Card sorting** (and tree testing, first-click testing)
4. **Wireframes**
5. **Test vs. production sites**
6. **CSS3**

---

## 10. Key Takeaways

- 🔑 **HTML = content/structure; CSS = presentation.** Keep them separate.
- 🔑 A CSS rule = **selector { property: value; }**.
- ✅ Prefer **external style sheets** linked to all pages.
- ⭐ **Media queries** make pages **responsive** to different screen sizes.
- 💡 Work through the **W3Schools CSS tutorial** thoroughly — styling and positioning are the priority.
- 💡 CSS modules mature at different speeds: **WD → CR → PR → REC**.

---

## Review Questions

1. Why is separating content from design valuable?
2. Identify the selector, property, and value in `p { color: red; }`.
3. What are the three ways to include CSS in a page, and which is best practice?
4. What does a media query do, and why is it essential for responsive design?
5. List the W3C maturity stages for a CSS module in order.
6. How does the CSS Zen Garden demonstrate the power of CSS?
