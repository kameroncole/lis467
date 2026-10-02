# LIS 467 — Session 3, Part 4: HTML5

**Course:** LIS 467 — Web Development & Information Architecture
**Topic:** What HTML5 adds, learning resources, CodePen, basic HTML elements and attributes, block vs. inline elements, session wrap-up
**Source:** Panopto lecture transcript — "Session 3 Part 4 HTML5"

---

## 1. What Is HTML5?

🔑 **HTML5** is the current standard for **HTML (HyperText Markup Language)**. It keeps the stable elements and attributes of earlier versions and adds:

| New capability | Examples |
|----------------|---------|
| **Multimedia** | Native `<video>` and `<audio>` |
| **Graphics** | `<canvas>`, SVG |
| **Storage** | **Local storage** in the browser; client-side SQL database |

⭐ HTML5 is a **big improvement** over previous versions.

---

## 2. Learning Resources

| Resource | Notes |
|----------|-------|
| **Lynda.com → LinkedIn Learning** | Free via Simmons — log in with your Simmons email/credentials for HTML5 and design tutorials |
| **W3Schools** | Tutorials and "Try it" examples |
| **Textbooks** | Many HTML5 texts available |

---

## 3. Editing HTML Locally (Recap)

1. Write code in **Notepad++** (or another text editor).
2. **Save as `.html`** → color coding appears.
3. Open the file in a **browser** to view the rendered page.

---

## 4. CodePen

🔑 **CodePen** (codepen.io) is an online playground for front-end code. Create a free account, then create a new **Pen**:

```
┌────────────┬────────────┬────────────┐
│   HTML     │    CSS     │    JS      │
├────────────┴────────────┴────────────┤
│        Live rendered preview         │
└──────────────────────────────────────┘
```

- Paste HTML in one panel, add CSS and JavaScript in the others.
- ✅ See the result **immediately** — a nice way to **play around with code** and try tutorial examples.

---

## 5. Basic HTML Elements & Attributes

### Elements and nesting

- 🔑 An **element** = opening tag + content + closing tag, e.g. `<p>Hello</p>`
- Elements can be **nested** inside other elements.

### Attributes

🔑 **Attributes** provide extra information about an element, written as `name="value"` inside the opening tag.

```html
<a href="https://www.simmons.edu">Simmons University</a>
<img src="library.jpg" alt="Front entrance of the library">
```

### Common elements

| Element | Purpose | Notes |
|---------|---------|-------|
| `<h1>` … `<h6>` | **Headings** | `<h1>` most important → `<h6>` least |
| `<p>` | **Paragraph** | |
| `<a href="…">` | **Anchor / link** | `href` attribute holds the destination URL |
| `<img src="…" alt="…">` | **Image** | `src` = image source; ⭐ **always provide `alt` text** — it helps **accessibility** |
| `target="_blank"` | Attribute on `<a>` | Opens the link in a **new tab** |
| `<div>` | **Block-level** container | Starts on a new line, takes full width |
| `<span>` | **Inline** container | Stays within the line of text |

### Example

```html
<h1>My Library</h1>
<p>Welcome to our <span>community</span> library.</p>
<a href="https://www.w3schools.com" target="_blank">
  <img src="logo.png" alt="Library logo">
</a>
<div>
  <p>This paragraph sits inside a block-level div.</p>
</div>
```

### Block vs. inline

| Type | Behavior | Examples |
|------|----------|---------|
| **Block-level** | New line; full available width | `<div>`, `<p>`, `<h1>` |
| **Inline** | Flows within text; only as wide as content | `<span>`, `<a>`, `<img>` |

💡 Practice these on **W3Schools**, **CodePen**, or other resources.

---

## 6. Session 3 Wrap-Up

This session covered:

- ✅ The importance of **audience** and **personas**
- ✅ **Design considerations** for websites, with good and bad examples
- ✅ **Web development tools** — including the full stack (front-end + back-end); ⚠️ this course focuses on **client-side / front-end** development
- ✅ An introduction to **HTML5**

---

## Key Terms Glossary

| Term | Definition |
|------|-----------|
| **HTML5** | Current HTML standard; adds multimedia, graphics, and storage features |
| **Element** | Opening tag, content, and closing tag |
| **Tag** | Markup like `<p>` or `</p>` defining an element |
| **Attribute** | Name/value pair in an opening tag giving extra info (e.g., `href`, `src`, `alt`) |
| **`href`** | Link destination attribute of `<a>` |
| **`src`** | Source file attribute of `<img>` |
| **`alt`** | Alternative text for images; essential for accessibility |
| **Block-level element** | Starts on a new line and spans full width (`<div>`) |
| **Inline element** | Flows within a line of text (`<span>`) |
| **CodePen** | Online HTML/CSS/JS editor with live preview |
| **Local storage** | Browser-based client-side data storage introduced with HTML5 |

---

## Quick Review Questions

1. What new capabilities did HTML5 introduce?
2. How can Simmons students access LinkedIn Learning tutorials?
3. What does CodePen provide, and why is it useful for practice?
4. Write the HTML for a link that opens W3Schools in a new tab.
5. Why should every `<img>` have an `alt` attribute?
6. What's the difference between `<div>` and `<span>`?
