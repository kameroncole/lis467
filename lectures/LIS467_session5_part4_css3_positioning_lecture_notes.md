# LIS 467 — Session 5, Part 4: CSS3 Positioning

**Course:** LIS 467 — Web Development & Information Architecture
**Topic:** The CSS `position` property — static, relative, fixed, absolute, and sticky
**Source:** Panopto lecture transcript — "Session 5 Part 4 - CSS3 Positioning"

---

## 1. Why Learn Positioning?

- CSS **layout** is a big topic; understanding **positioning** is essential.
- Positioning is about the **different ways you can place elements** on your HTML page, specified **in your CSS**.
- Later topics (e.g., **flexbox** and **grid**) provide even more help in making pages **responsive**, but positioning is the **starting point**.
- **Resources for learning CSS3:** **W3Schools** (the captions say "double three schools"), other online CSS tutorials and learning platforms, and the course **textbooks**.

---

## 2. The `position` Property

At **W3Schools → Learn CSS → CSS Layout → Position**: the `position` property **specifies the type of positioning method used for an element**.

Values: **`static`**, **`relative`**, **`fixed`**, **`absolute`**, **`sticky`**
(`sticky` is **not supported by some browsers**, e.g., Internet Explorer.)

The **four commonly used** values are **static, relative, fixed, and absolute**.

---

## 3. `position: static` (the default)

- Elements are **not positioned in any special way**; they appear in the **normal flow** of the page, in the order they occur in the HTML.
- Even if you don't specify a position, the element is **`static`**.
- `top`, `right`, `bottom`, `left` have **no effect** on a static element.

```css
div.static {
  position: static;
  border: 3px solid #73AD21;
}
```

---

## 4. `position: relative`

- The element is positioned **relative to its normal position**.
- Setting `top`, `right`, `bottom`, or `left` **moves it away from where it would normally be**.
- **Other content is not adjusted** to fill the gap or fit around it.

```css
div.relative {
  position: relative;
  left: 30px;          /* 30px away from its normal position */
  border: 3px solid #73AD21;
}
```

💡 Demo from the lecture: changing the value to `static` moves the element back to its normal position.

---

## 5. `position: fixed`

- The element is positioned **relative to the viewport (browser window)**, so it **stays in the same place even when the page is scrolled**.
- Use it for things that should **remain visible while scrolling** — e.g., a **chat button** at the bottom-right corner or a fixed header.

```css
div.fixed {
  position: fixed;
  bottom: 0;
  right: 0;
  width: 300px;
  border: 3px solid #73AD21;
}
```

💡 Demo: switching to `static` returns it to its normal place; switching to `absolute` moves it but it **won't stay put when scrolling** (a fixed element does).

---

## 6. `position: absolute`

- Slightly harder to understand, but not difficult.
- An absolutely positioned element is positioned **relative to its nearest *positioned* ancestor** — an ancestor whose position is **anything other than `static`** (i.e., `relative`, `absolute`, `fixed`, or `sticky`).
- ⚠️ If an absolute element has **no positioned ancestors**, it uses the **document body** and **moves along with page scrolling**.

```css
div.relative {
  position: relative;
  width: 400px;
  height: 200px;
  border: 3px solid #73AD21;
}
div.absolute {
  position: absolute;
  top: 80px;
  right: 0;
  width: 200px;
  height: 100px;
  border: 3px solid #73AD21;
}
```

**Rule of thumb:** use `absolute` when you want to place one element **in relation to another** (positioned) element — the second element's position is **relative to the first**.

---

## 7. `position: sticky`

- Toggles between **relative and fixed**, depending on the **scroll position**.
- It is **relative** until a given **offset position** is met in the viewport, then it **"sticks" in place** like `fixed`.
- Because it is **not supported by all browsers**, the lecturer suggests **not relying on it**.

---

## 8. Summary Table

| Value | Positioned relative to | Moves with scrolling? | Notes |
|---|---|---|---|
| **static** | Normal flow (default) | Yes | `top/right/bottom/left` ignored |
| **relative** | Its own normal position | Yes | Offsets shift it; others aren't adjusted |
| **fixed** | The viewport | **No** — stays put | Headers, chat buttons |
| **absolute** | Nearest positioned ancestor (else `body`) | With its ancestor | Place relative to another element |
| **sticky** | Relative until a scroll offset, then fixed | Partly | Limited browser support |

**Practice:** experiment with these in an **online editor** (the W3Schools "Try it" editor or similar); you'll get comfortable as you build your own site.

---

## 9. Review Questions

1. What does the `position` property do, and what are its five values?
2. What is the default position, and do `top/left` affect it?
3. How does `relative` differ from `static`? What happens to surrounding content?
4. Give a use case for `fixed`. What is it positioned relative to?
5. What does an `absolute` element position itself against? What if there is no positioned ancestor?
6. Why might you avoid `sticky`?
7. Which later CSS tools help make pages responsive beyond positioning?

> ⚠️ **Transcript note:** Captions are auto-generated. Code samples above are standard W3Schools-style examples illustrating the behaviors described in the lecture; exact values in the lecture's demo may have differed. The learning-resource names in the transcript were garbled, so they are described generically.
