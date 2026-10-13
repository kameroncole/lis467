# LIS 467 — Session 5, Part 1: Usability

**Course:** LIS 467 — Web Development & Information Architecture
**Topic:** Learning objectives; defining usability; components of usability; common web design mistakes; user interface guidelines; minimalist vs. information-rich design
**Source:** Panopto lecture transcript — "Session 5 Part 1 - Usability"

---

## 1. Session 5 Learning Objectives

By the end of this lecture and this week's learning you should be able to:

1. **Describe the importance of usability**
2. **Explain and predict the design aspects** (look and feel) users look for in a website
3. **Design a mood board** (used in the design/planning process)
4. **Create stylesheets using CSS3**
5. **Begin learning CSS3 layout and positioning**

---

## 2. Why Usability Matters

- Usability is a **very important topic** — an entire later week is dedicated to **how to do usability testing**.
- But usability must be considered **at various stages**, so it is important to **start early**.

### What is usability?

- Many people associate it with **software systems and websites**, but usability applies to **any product or service**.
  - *Examples from the lecture:* a **headset/microphone** for recording (a set-up that produced noise was a usability problem; noise-canceling models are more usable); a **classroom whiteboard**; even **non-technology** things.
- 💡 **Exercise:** pause and write down keywords describing what usability means to you.

### Definitions

| Source | Definition / idea |
|---|---|
| **ISO 9241-11** (the "nine two four one" in the captions) | The **extent to which a product can be used by specified users to achieve specified goals with effectiveness, efficiency, and satisfaction in a specified context of use** |
| **"User-friendliness"** | How **easy** it is for a person to use something — **ease of use** |
| **Convenience & practicality** | The **degree of convenience and practicality in use** |
| **For a website** | The **efficiency** with which a **patron** can accomplish a task and the **overall satisfaction** with the process |

---

## 3. Dimensions (Components) of Usability

The lecture's figure places **usability** inside a larger model: **system acceptability** → *social acceptability* and *practical acceptability* (cost, etc.) → **usefulness** → **usability**. Usability itself is described by these components:

| Component | Question to ask (applied to a website, e.g., a library or archive site) |
|---|---|
| **Easy to learn** (learnability) | Is the site usable **by a first-time visitor** on the first visit? |
| **Efficient to use** | Does it support the user's **productivity**? |
| **Easy to remember** (memorability) | Can users **return and remember** how to use it, or is it confusing where to click next time? |
| **Few errors** | Does it **minimize errors** — e.g., clicking the wrong navigation item — and let users **recover**? |
| **Pleasing / satisfying** | Is it **pleasant** to use overall? |

- Some people count **aesthetics/look and feel** as part of usability; others treat it as **separate** (covered in Part 2).
- Others emphasize **interaction**: minimizing errors and giving **clear feedback** on users' actions.
- Anything that **makes the site easy to use and the experience nice** contributes to usability.

### Designer's view vs. user's view

⭐ The difficulty: designers/developers think from the **design/developer point of view**, while users think from **their own** point of view. It is **hard for developers to think like users** without **training** and a deliberate focus on **users and their needs first**.

- The lecture's **cartoon** frames usability testing as the process of helping the **user get to the information they need, in a timely manner, without frustration**.

---

## 4. Planning a Usable Site

- **Utility is crucial:** What is the site for? Which users? What are you offering of value to them?
- Develop **user-based scenarios and use cases** (Session 4) and **focus on value to the user**.
- ⚠️ **Don't compromise early** based on what you can or cannot implement — first think of everything users need, and **apply constraints later**.
- Build a **simple prototype**, **test it**, and **repeat** the cycle until it works well (iterative design).

---

## 5. Common Web Design Mistakes

The lecture walked through an article on the **"seven most common web design mistakes to avoid"** plus related lists.

| Mistake | Notes |
|---|---|
| **Lack of a call to action (CTA)** | Tell the user **what to do, where to go, how to feel**. A CTA is a **persuasive, clearly worded command attached to a link or button**, using **action verbs**: *Get started*, *Contact us*, *Sign me up*, *Buy now*. Marketing sites focus heavily on this, but libraries/archives can use CTAs too (e.g., *Join* / *Become a member*). Example: the **ASIS&T** website's redesign moved its **Join** button to a more prominent position. |
| **Failing to measure performance** | Gather data from **user feedback, usage, and traffic** (covered later in the semester). |
| **Unclear brand messaging** | Know your message and **tell a story**; communicate in a way that is **compelling and connects emotionally**, as if talking to a close friend. Visitors who feel connected **stay longer** and are likelier to use your library/archive or **collaborate** with you. |
| **Ignoring search engine optimization (SEO)** | Strategies to make the site **rank higher in search**; covered later. |
| **Hard-to-find contact information** | Must be **early, clear, and easy to find** from any page — users may decide at any point that they want to contact you. |
| **Slow load times** | Pages shouldn't be too slow. |
| **Poor mobile experience** | Very important — tie to **responsive design**, **media queries**, **Bootstrap**, etc., since more users are on mobile. |
| **Non-responsive designs / fixed heights and widths** | Dimensions must be **changeable** for responsiveness; don't assume **one size fits all**. |
| **Misplaced/misused elements, deprecated web standards, outdated site** | Use current standards; **update periodically**. |
| **Using Flash** | Obsolete technology. |
| **Massive images** | Don't force users to download huge images just to view the page. **Flickr** is a good model: it offers **multiple download sizes** (thumbnail first, larger on demand). |
| **Overuse of animation** | Distracting. |

### Jakob Nielsen's usability points

**Jakob Nielsen** is a leading usability expert. Items mentioned:

- **Bad search** is a poor feature.
- **PDFs for online reading** are discouraged — PDFs are mostly for **downloading and printing**. Online-reading text should be **HTML**.
  - Nuance from the lecture: newer **ebook formats (ePub, Kindle)** exist; **PDF is fine** when you need **fixed formatting** (e.g., a **CV** or formatted **report**). Many sites offer **both** HTML and PDF.
- **Not changing the color of visited links**, and **fixed font sizes** users cannot change.

---

## 6. User Interface Guidelines

Key guidelines (the list corresponds to well-known design principles such as Shneiderman's golden rules and Nielsen's heuristics):

- ✅ **Strive for consistency** (consistency and standards)
- ✅ Cater to **universal usability**
- ✅ Provide **informative feedback** to the user
- ✅ **Design dialogs that yield closure** — help users complete a task (e.g., on a shopping site, let them finish or abandon a purchase; on a library site, guide users through checking out a book, requesting something, or reaching **online chat** if they need help)
- ✅ **Prevent errors**
- ✅ **Easy reversal of actions**
- ✅ Make users feel **in control**
- ✅ **Visibility of system status**
- ✅ **Recognition rather than recall**

⭐ These guidelines were made **keeping human psychology in mind** — **perceptual and cognitive psychology**: how people **perceive, learn, reason, remember, and convert intentions into action**. They are **old but have stood the test of time**.

### Aesthetic and minimalist design

- Minimalist design helps fight **information overload** — giving information in **chunks** helps users.
- But an **advanced user** looking for something specific may prefer **lots of information they can scan quickly**.
- *Examples:* a **minimalist** page (the captions say "good academy"; most likely **Google**) vs. **W3Schools**, which presents **a lot of information at once**.
- 💡 Different user bases call for different designs.

---

## 7. Key Terms

| Term | Definition |
|---|---|
| **Usability** | Extent to which users can achieve goals effectively, efficiently, and satisfactorily in a context of use |
| **Learnability / memorability** | Ease of learning the site; ease of remembering it on return |
| **Call to action (CTA)** | Persuasive action-verb prompt on a link/button telling the user what to do next |
| **Universal usability** | Designing for the widest range of users |
| **Information overload** | Too much information at once; mitigated by chunking and minimalism |
| **Prototype** | A simple early version used for testing and iteration |
| **SEO** | Strategies to improve visibility in search results |

---

## 8. Review Questions

1. Give two non-software examples to which usability applies.
2. State the ISO 9241-11 definition of usability in your own words.
3. List the components of usability and apply each to a library website.
4. Why is it hard for designers to think from the user's point of view?
5. What is a call to action? Give three examples with action verbs.
6. Why are massive images and fixed widths/heights design mistakes? How does Flickr handle image sizes?
7. When is PDF appropriate and when is HTML better, according to the lecture?
8. Explain how minimalist design and information-rich design each serve different users.

> ⚠️ **Transcript note:** Captions are auto-generated and contain errors; uncertain terms were interpreted from context (e.g., "good academy" → likely Google; "double three schools" → W3Schools).
