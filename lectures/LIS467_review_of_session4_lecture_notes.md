# LIS 467 — Review of Session 4

**Course:** LIS 467 — Web Development & Information Architecture
**Topic:** Session 5 preview and recap of Session 4 — use cases and scenarios, information architecture, card sorting, wireframes, test vs. production sites, and CSS3
**Source:** Panopto lecture transcript — "Review of Session 4"

---

## 1. Preview of Session 5

This week's session covers:

- **Usability**
- **Look and feel** (aesthetics)
- **CSS3** — continuing last week's introduction, now with **CSS layout and positioning**

The review recaps the six Session 4 topics below.

---

## 2. Use Cases and Scenarios

- A **use case** starts from the **typical users** (user groups/personas) you have identified. For each user, identify the **tasks/goals** they want to accomplish using your website. Each task for each type of user gives rise to a use case.
- A **scenario** is a series of tasks put together as a **narrative or story**. Each step is followed along an overarching framework, and the story includes the **questions that arise** and **ideas for addressing** them.
  - *Example from the lecture:* buying flowers online. The story follows the sequence of steps in the buying process; questions arise (e.g., a policy that doesn't allow a certain choice), and the scenario exposes where the site needs a better way of handling them.
- ⭐ **Why they matter:** both use cases and scenarios help you **understand the behavior users will exhibit** when using your website.

---

## 3. Information Architecture (IA)

IA is concerned with:

- **Labeling** — what **metadata/labels** to use, e.g., the labels for your **menu items**
- **Classifying** — how to categorize the items on a webpage
- **Sequencing/structuring** — arranging items in a **hierarchical** manner
- **Navigation** — which **navigation pattern** the website uses
- **Social features** — what social features are offered to users

---

## 4. Card Sorting

🔑 **Card sorting** is a technique used both to **design** and to **evaluate** your information architecture.

| Type | How it works |
|---|---|
| **Open card sort** | No predefined categories — participants **create their own categories** |
| **Closed card sort** | Categories are **predefined**; participants sort cards into them |

- Items/parts of the website are written on **index cards**; the people helping you test sort them into categories.
- Result: you can see **whether the items on your webpage are organized in a sensible way** from the users' point of view.

---

## 5. Wireframes

- Wireframes **put your information architecture into a design format** you can begin to **visualize**.
- They show **layout and positioning of components** on the site — e.g., where the **logo** goes, where **menu items** go, whether there is a **hero image**, where **social media** links go, and how things are laid out.
- They deliberately **do not include colors or images** yet.
- You can draw them **on paper** or with **wireframing software**.

---

## 6. Test vs. Production Sites

- Servers can be **production**, **development**, or **testing** web servers.
- ✅ You do **not** want to do development/testing on your **production** web server; keep **testing separate** from production **as far as possible**.

---

## 7. CSS3

- CSS3 is **modular**: **some modules are completed while others are still being developed**, so it's a **work in progress** — but it is now **highly usable**, and most of it can be used without major issues.
- **Best practice:** keep CSS in a **separate `.css` file**, separate from the HTML.
- A CSS rule consists of a **selector** (an element/HTML tag to match), **properties**, and the **values** assigned to them:

```css
p { color: red; }   /* selector: p | property: color | value: red */
```

---

## 8. Quick Review Questions

1. How does a use case differ from a scenario?
2. List the components of information architecture covered in Session 4.
3. Contrast open and closed card sorts.
4. What does a wireframe show, and what does it intentionally leave out?
5. Why keep test and production environments separate?
6. Why is it best practice to put CSS in a separate file? Identify the selector, property, and value in a rule.

> ⚠️ **Transcript note:** The auto-captions of this recording are quite garbled; the content above is reconstructed from the recoverable passages and consistent with the Session 4 lecture notes.
