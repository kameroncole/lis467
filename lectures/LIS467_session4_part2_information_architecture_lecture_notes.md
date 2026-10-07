# LIS 467 — Session 4, Part 2: Information Architecture

**Course:** LIS 467 — Web Development & Information Architecture
**Topic:** Definition and components of information architecture, organization/labeling/navigation/search systems, the three circles (users, content, context), the instructor's context research, and a case study of the Stanford Center for Internet and Society
**Source:** Panopto lecture transcript — "Session 4 Part 2 Information Architecture"

---

## 1. Why Information Architecture Matters

🔑 **Information architecture (IA)** appears in the **course title** — *Web Development and Information Architecture* — and is a **key concept** of the course.

**Definition:** IA is **the art and science of organizing and labeling websites, intranets, online communities, and software to support usability.**

⭐ IA is **not limited to websites**; it applies to many kinds of information environments. At its core it answers: **how do we organize the content we have, and how do we label it?**

### IA work products

| Deliverable | Purpose |
|-------------|---------|
| **Site maps / boxes-and-lines diagrams** | Show how the site is organized |
| **Wireframes** | Blueprints for the page designs that follow |
| **Taxonomy** | A specified way of organizing and classifying content/products |
| **Prototypes** | Illustrate how information changes on screen as a user clicks |

The goal is to **consciously organize the content flow** of a website based on **principles derived from evidence gathering**, not guesswork.

---

## 2. The Four Systems of IA

| System | Question it answers | Examples |
|--------|--------------------|----------|
| **Organization systems** | How do we **categorize** information? | By subject, task, audience, topic; hierarchies |
| **Labeling systems** | What do we **call** things? | "Maple" (common name) vs. *Acer* (scientific name) |
| **Navigation systems** | How do users **move through** the information? | Menus, clicking through a hierarchy, breadcrumbs |
| **Searching systems** | How do users **look up** information? | Search box / magnifying-glass icon, indexes |

💡 **Search is often easier than navigation**: if a user doesn't know where something lives in the hierarchy, a search box gets them there faster.

### What IA accomplishes

- **Connects people to the content** they're looking for (text, images, video, documents).
- Makes it **easier for the people who create and maintain content** to do their jobs.
- **Links content to other content** — and people to content, to other people, and even to conversations — making the site more usable and findable.

---

## 3. The Three Circles of Information Architecture

**Louis Rosenfeld and Peter Morville** describe IA as the intersection of three concerns:

```
          ┌───────────┐
          │   USERS   │
          └─────┬─────┘
        ┌───────┴───────┐
   ┌────┴────┐      ┌───┴─────┐
   │ CONTENT │──IA──│ CONTEXT │
   └─────────┘      └─────────┘
```

| Circle | What to consider |
|--------|------------------|
| **Users** | Who they are; **information-seeking behaviors**; needs. Build **personas**; conduct **usability testing**, **ethnographic studies**; document **user experience requirements** |
| **Content** | **Volume**, **formats**, **metadata**, **structure**, **organization**; site architecture, **content management**, navigation, labeling |
| **Context** | **Business goals, funding, politics, culture, technology, resources, constraints**; **project scope and definition** |

⭐ These concerns **overlap**, and good IA happens where all three are balanced. The site map **makes or breaks** a site's success, so IA must be worked out **early** in development.

### Mapping the user flow

- Map out **which page links to which**, thinking in terms of a **use case or scenario**: when the user tries to perform a task, which page do they land on, and where does each link take them?
- ⭐ **Each page must do two things:** (1) **help the user accomplish their goal**, and (2) **make the next page interesting** so they continue.

---

## 4. Context in More Depth: The Instructor's Research

The instructor became interested in the term **context** during **PhD research**, and it became a major part of the dissertation and a **2018 book** on **context and information behavior** (seeker, situation, surroundings, and shared identities).

**Simplified view:** context is the **whole story behind why a user comes to a website** and navigates to particular content.

From that research, context can be described through several attributes, as presented in the lecture:

| Attribute | Meaning for a website user |
|-----------|----------------------------|
| **The user (actor)** | Demographics, habits, abilities, disabilities, familiarity |
| **Environment** | The surroundings — physical, social, cultural, the **information culture** |
| **Problem situation** | The circumstances the user is engaged in (this is where **use cases** come from) |
| **Task** | What they need to do |
| **Need for information** | What information the user requires to complete the task |
| **Relationship** | The user's relationship with the **website** — familiar or first-time? Trusted? |
| **Time and space** | When and where interaction happens; how complex or important the task is; how much the user already knows about the topic |

✅ Design takeaway: IA is concerned with **users, content, and context together**.

---

## 5. Examples: The Instructor's Personal Websites

### Version 1 (older site)

The instructor first brainstormed key categories to highlight:

- **Profile:** teaching, research, service
  - *Teaching* — internal-facing (courses taught to students)
  - *Research and publications* — external-facing; lists interests, presentations, and collaborations; publications are important to **reference and share**
  - *Service* — college and professional accomplishments
- **Timeline** — growing up → school → university → industry work → PhD → later work
- **Identity/thoughts** — more personal reflections
- **Creativity** — painting and other media, writing, poems, cross-cultural work
- **Places** — places visited or lived in; travel
- A **site map**

### Version 2 (rebuilt ~2017–2018, **responsive**)

The earlier version was **not responsive** (did not adapt to different screens). In the rebuild, the instructor:

- Kept a small set of top-level categories: **About** (description plus **Contact**), **Research** (with research interests as a **subcategory**), **Publications** (articles, conference proceedings, abstracts, with links to full text), **Service**, **Teaching**
- Promoted **a few favorite sections** (e.g., painting) directly to links
- Still kept **Timeline** and **Places**
- **Distilled** many sections down to **two or three categories that matter most**

⭐ Lesson: there are **multiple valid ways to organize the same content** (by role, chronology, place, creativity), but you must **think carefully** about labels and grouping and about **why** it matters to the audience.

---

## 6. Case Study: Stanford Center for Internet and Society (CIS)

This (circa 2011) IA study shows a real proposed architecture.

### Proposed navigation

**Primary ("family") navigation** — the site's main sections:

| Section | Notes |
|---------|-------|
| **Focus areas** | Topics such as **privacy, fair use and copyright, public policy, robotics** |
| **Experts** | Organized by name, topic, or focus |
| **Events** | |
| **Project initiatives** | |
| **Publications** | |
| **About** | |

**Utility navigation** — items needed right away: **Blog, Multimedia, Contact Us, Get Involved, Press**, plus **Home** and **Contact** along the top.

### Labeling and structure questions raised

- Where should items live in different parts of the site?
- It was recommended to **rename "programs and initiatives"** because the current use of the term "program" was confusing; *projects* and *initiatives* needed clearer organization.
- **Expert** organization and the label **"focus"** might confuse visitors who don't understand the jargon.
- How should **academics**, **multimedia**, and **news** be labeled and positioned?

⭐ These are exactly the kinds of **label and placement questions** an IA project must answer.

### Research methods used

- **Stakeholder interviews** with the **project lead, director, a fellow, and a student**, covering the **purpose and audience** of the site.
- **Audiences identified:** students, **journalists**, academics, **lawyers**, **policymakers**, and others.
- **Weaknesses and pain points** of the current site: visually dated, lacking character, **content scattered across different kinds of content**, confusing and unintuitive navigation.
- **Strengths** to retain: things that were already working well.
- Further notes on **home page and navigation**, **look and feel**, **model sites**, and **how success is measured**, ending in **recommendations**.
- The project also compared **vendor proposals**, which varied widely in cost and scope (the exact dollar figures are unclear in the transcript).

---

## 7. Key Takeaways

- 🔑 IA = **organizing + labeling + navigation + search** to support usability.
- 🔑 The **three circles**: **users, content, context** (Rosenfeld & Morville).
- ⭐ Work out the **site map early**; it largely determines the user's success.
- ✅ Each page should **help the user reach their goal** and **lure them to the next page**.
- 💡 There is rarely one "correct" organization; **test** your choices with users (see **card sorting**, next part).

---

## Review Questions

1. Define information architecture in one sentence.
2. Name the four systems IA designs and give an example of each.
3. What are the three circles of information architecture? What belongs in each?
4. What two things should each page accomplish?
5. Why might "focus areas" or "programs and initiatives" be poor labels for a site's audience?
6. How did the instructor's second website differ from the first in how it organized content?
