# LIS 467 — Session 3, Part 3: Web Development Tools

**Course:** LIS 467 — Web Development & Information Architecture
**Topic:** HTML/CSS/JavaScript roles, editors, browser developer tools, text editors, image editors, web developer roadmaps, front-end vs. back-end vs. full stack
**Source:** Panopto lecture transcript — "Session 3 Part 3 Web development tools"

---

## 1. The Core Front-End Languages

⭐ Understanding the tools is important as the course moves into **HTML, CSS, and JavaScript**.

| Language | Role | Example |
|----------|------|---------|
| **HTML** (HyperText Markup Language; current version **HTML5**) | **Content / structure** | Headings, paragraphs, images, links |
| **CSS** (Cascading Style Sheets) | **Presentation** | Colors, fonts, positioning, layout |
| **JavaScript** | **Behavior** | Hover over an image → text appears; dynamic changes |

🔑 A key principle (covered later): **separate content (HTML) from presentation (CSS)** and **behavior (JavaScript)**.

---

## 2. Categories of Tools

### 2.1 WYSIWYG editors

- e.g., **Adobe Dreamweaver** and similar
- Offer a **"What You See Is What You Get"** interface — looks like Microsoft Word — alongside the code view

### 2.2 Browser extensions & validators

| Tool | Purpose |
|------|---------|
| **Web Developer toolbar** (Firefox/Chrome extension) | Inspect and manipulate parts of a page |
| **W3C Markup Validator** | Check HTML against standards |
| **Browser developer tools** | Inspect elements, CSS, console, device emulation |

### 2.3 Chrome Developer Tools (demo)

Open via **⋮ menu → More tools → Developer tools**:

- ✅ **Device toolbar** — see how a page looks on a **mobile screen**
- ✅ **Elements** panel — view the HTML; select an element to see what's connected to it; expand/collapse nested elements
- ✅ **Styles** — the CSS applied to the selected element
- ✅ **Console** — JavaScript messages/errors
- ✅ Other info: file types loaded, memory use, etc.

Chrome Web Store → search **"web development"** for extensions: Web Developer toolbar, **mobile responsive** testers, eye-trackers/color tools, and other design utilities.

💡 Whatever browser you use, there are developer tools to help you inspect and understand websites easily.

### 2.4 Text editors

You need a **text editor** to write code:

| Platform / Editor | Notes |
|-------------------|-------|
| **Notepad++** (Windows) | Free; color-codes code by language |
| **TextEdit / BBEdit** (Mac) | Built-in / lightweight options |
| **Sublime Text**, **Brackets**, **Komodo Edit**, etc. | Cross-platform code editors |

**Notepad++ demo:**

1. Copy sample HTML (e.g., from **W3Schools**) into a new file.
2. Before saving, Notepad++ doesn't know the file type — **no color coding**.
3. **Save as `.html`** → syntax highlighting is applied automatically (tags turn blue, etc.), and you can **collapse/expand** opening and closing tags.

⭐ Syntax highlighting makes code much easier to read and debug.

### 2.5 Image editors

| Tool | Notes |
|------|-------|
| **GIMP** | ✅ **Free and open source** image editor — crop, resize, apply filters/effects |
| **Adobe Photoshop** | Commercial alternative |

---

## 3. The Web Developer Landscape (Roadmaps)

The lecture shows several articles/roadmaps (2018, 2019, **2020 Web Developer Roadmap**) listing what a web developer could learn. ⚠️ **Not all of this is covered in the course** — it's an overview of what exists.

### Typical roadmap sections

| Area | Examples |
|------|---------|
| **Introduction / core competencies** | Concepts, languages, data, intermediate skills, **soft skills**, glossary |
| **Languages** | **JavaScript**; libraries like **jQuery** (covered in this course); **PHP**; others |
| **Data** | Database options; **SQL** (standard query language); NoSQL |
| **Frameworks** | Front-end: **React**, **Angular**, **Vue**; back-end frameworks |
| **Utilities** | Package managers, build tools |
| **Version control** | Git / GitHub |
| **Deployment** | How to deploy code; hosting platforms |

### Front-end roadmap essentials (what this course focuses on)

- **HTML:** basics, **semantic HTML**, **SEO** (search engine optimization), **accessibility**
- **CSS:** basics, **layouts**, **media queries**, **responsive** pages, positioning elements
- **JavaScript:** syntax basics, manipulating the **DOM** (Document Object Model)

---

## 4. Front-End vs. Back-End vs. Full Stack

| Term | Meaning |
|------|---------|
| **Front-end (client-side)** | What runs in the browser — HTML, CSS, JavaScript; design and development of the user-facing site |
| **Back-end (server-side)** | Server logic, databases, APIs |
| **Full stack** | A developer who can program **both** front-end and back-end |

⭐ **This course focuses on the front-end / client side.** Server-side development is not covered in depth.

---

## 5. Takeaways

- 💡 Web development is a **learning journey** — you pick up more over time.
- ✅ For this class, choose **one or two tools in each category** (editor, browser tools, image editor, validator) to support your front-end design and development process.

---

## Key Terms Glossary

| Term | Definition |
|------|-----------|
| **HTML5** | Current version of HyperText Markup Language — defines content/structure |
| **CSS** | Cascading Style Sheets — controls presentation and layout |
| **JavaScript** | Scripting language that adds behavior/interactivity |
| **WYSIWYG** | "What You See Is What You Get" visual editor |
| **Developer tools** | Browser-built tools for inspecting HTML, CSS, JS, and device views |
| **Validator** | Tool that checks code against standards (e.g., W3C) |
| **Syntax highlighting** | Color-coding of code by language element |
| **GIMP** | Free, open-source image editor |
| **jQuery** | JavaScript library simplifying DOM manipulation |
| **Framework** | Pre-built structure for building large apps (React, Angular, Vue) |
| **DOM** | Document Object Model — the browser's tree representation of a page |
| **Front-end / Back-end / Full stack** | Client-side / server-side / both |

---

## Quick Review Questions

1. What are the roles of HTML, CSS, and JavaScript?
2. How do you open Chrome Developer Tools, and what can you do with them?
3. Why does Notepad++ only color-code after saving as `.html`?
4. What free tool can replace Photoshop for basic image editing?
5. What front-end skills does a typical roadmap list for HTML, CSS, and JavaScript?
6. Define front-end, back-end, and full-stack development. Which does this course cover?
