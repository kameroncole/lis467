# LIS 467 — Session 4, Part 1: Use Cases and Scenarios

**Course:** LIS 467 — Web Development & Information Architecture
**Topic:** Session 4 learning outcomes, use cases (actors, goals, triggers, flows), metadata, scenarios, and how both drive site design
**Source:** Panopto lecture transcript — "Session 4 Part 1 Use Cases and Scenarios"

---

## 1. Session 4 Learning Outcomes

By the end of Session 4 you should be able to:

1. **Describe use cases and scenarios**
2. **Explain the importance of information architecture (IA)**
3. **Outline the process of creating a site information architecture**
4. **Explain what a wireframe is** and how to create one
5. **Distinguish test sites from production sites**
6. **Begin learning CSS3**

This first part covers outcome 1.

---

## 2. What Is a Use Case?

🔑 A **use case** describes **why a person would use a website or system** — a goal they want to accomplish — in a simple, structured way. It gives the team a simple means to **decide on and discuss the purpose of a project**.

### Two core components

| Component | Meaning | Example |
|-----------|---------|---------|
| **Actor** | The **user** — the person (e.g., a library **patron**) who uses the site | A library patron |
| **Goal** | What the actor wants to **achieve** | Check out a book |

⭐ Every use case must have a **specific goal** and an **actor** who performs tasks to reach that goal. Goals are often small and ordinary: reading a review, checking an account, placing a hold, checking out a book.

### Example: a library OPAC

An **OPAC (Online Public Access Catalog)** is the public interface to library resources. A patron might use it to:

- Manage their account
- Search the catalog
- Find books and other resources
- Place a hold on a particular item
- Provide feedback

✅ **Each of these is a separate use case.**

### What a use case is (and is not)

- A **written description** of how users perform tasks on a website, told from the **user's point of view**, including how the **system responds** to each request.
- A **sequence of simple steps** that **begins with a goal and ends when the goal is fulfilled**.
- It describes **what the user does and how the site should respond** — it does **not** include implementation details, interface language, or screen layouts.

---

## 3. Anatomy of a Detailed Use Case

| Element | Description |
|---------|-------------|
| **Name / goal** | What the actor is trying to accomplish |
| **Actor** | Who performs it |
| **Trigger** | What **causes the use case to be initiated** |
| **Basic (main) flow** | The normal sequence of steps to success |
| **Alternate flows** | Variations that occur under certain conditions |

### Steps for writing use cases

1. **Identify the users** of the site and decide **what each wants to do**.
2. Treat **each thing a user does on the site** as a **use case**.
3. Write the **normal course of events** (basic flow).
4. Add **alternate scenarios** (variations and exceptions).

---

## 4. Worked Examples

### 4.1 The housekeeper (a non-web illustration)

**Use case: Do Laundry** — Actor: **housekeeper**

| Part | Content |
|------|---------|
| **Trigger** | It is Wednesday (laundry day) |
| **Basic flow** | Collect laundry → wash → dry → fold → put away |
| **Alternate flows** | If an item is **wrinkled**, iron it and hang it on a hanger; if an item is **still dirty**, wash it again; if an item has **shrunk**, set it aside / handle it separately |

The main sequence is simple; the alternate flows capture the conditional branches.

### 4.2 The prospective student (a web example)

A **prospective student** visits the Simmons website:

1. Looks over the site to see whether the university **offers the degree** she wants.
2. **Alternate flow:** notices a **different degree** that interests her and explores it.
3. **Alternate flow:** discovers the program she wanted is **not offered** (or not offered the way she wants) and **leaves the site**.
4. **Success flow:** finds the program, locates the **Admissions** link, and **e-mails to inquire further**.

💡 The same user can follow **different flows** depending on what they find — good IA must support all of them.

---

## 5. Metadata: The Data That Makes Content Findable

🔑 **Metadata** is **"information about information"** — data that **describes the content** of a site. Content may be shown on paper, on a device, or on a larger screen, but metadata gives it **structure, context, and meaning**.

- Metadata is all the **words and labels** you use to describe a piece of information.
- It is what helps users **find the content they are looking for**.
- Example: you want to find a **German artist** on a library website. If the content exists but you **cannot find it by browsing or searching**, that signals **bad metadata**.
- Getting metadata right is **an early step in site design**: decide **what information to store** and **how to label it** so it can be found.
- ⭐ People search with **familiar terms and jargon of their own**, so labels should **use the terms users actually use**.

---

## 6. Scenarios

🔑 A **scenario** is closely related to a use case but **richer in narrative detail**: **a story about a specific person using your website to accomplish a specific goal** — e.g., checking out a book, looking up interlibrary loan, or asking a reference question.

- Scenarios **work together with use cases**, adding the **story and motivation** behind why a particular person comes to the site.
- They focus on **the user and the user's tasks**, **not on your site's organization or internal structure**.
- They help you see **what content the site must have** and **how it should be organized**.
- ⭐ They force you to design from the **user's point of view**, rather than the **web designer/developer's point of view**.
- Scenarios are **critical for designing the interface and for usability testing**.

### Questions to ask when writing a scenario

- **Who** is the user? (Make them a realistic, specific person.)
- **What** do they want to do on the site?
- **What motivations and questions** do they bring?
- **What context** are they in when they arrive?

---

## 7. Example Scenario: Ordering Flowers

**Fall**, an **online student**, is ordering **flowers for her mom's birthday** from a flower-delivery website. Think of the scenario as a **series of linked steps**, each raising a design question and an idea.

| Step in the story | Design question | Design idea / implication |
|-------------------|-----------------|---------------------------|
| 1. Fall arrives at the site (via a search engine, ad, or link) | How did she find us? | Make the site findable; optimize for search |
| 2. She looks for a **Birthday flowers** option in the menu | Is there a clear, expected menu label? | Provide a **"Birthday" category** in the main menu |
| 3. She wants to see popular choices and delivery information | What should the home page show? | Show **most popular items** and **delivery information** on the home page |
| 4. She can spend **no more than 25** (currency units) | How can she filter by price? | Add a **"flower finder" / filter by price** |
| 5. She is shown results and must decide among them | What does she need to compare? | Show an **image, title, price, and short description** for each arrangement |
| 6. She wants to choose a type of flower | How do we help someone who is not a florist? | Offer a **quick guide to flower types** |
| 7. She checks details for one arrangement, including **whether it can arrive before her mom's birthday** | What information will she need? | Show **delivery costs and availability**, **size information**, and **customer reviews** |
| 8. She is unsure of the right **size** for her mom | How do we reduce uncertainty? | Provide a **size guide / sizing policy** |

✅ Notice that the steps are **not isolated** — each links to the previous and next. A scenario can therefore be thought of as **a series of use cases** strung together by one person's story.

---

## 8. More Scenario Examples (from usability.gov-style guidance)

Scenarios can be short or detailed. Examples cited in the lecture:

- A **parent** is worried that her **ten-year-old refuses to drink milk** and is getting very little calcium — what can the site tell her?
- A **traveler** is going to a **job interview next week** and wants to check **whether meals and other expenses will be reimbursed**.
- **Retired schoolteachers in their seventies** for whom **Social Security checks** are an important part of income; they have just **sold their large house** — why would they come to a government site, and what do they need to know?

⭐ A good scenario captures **the story and context behind why a specific user group comes to your site**, so the team knows the **goals and questions** to be addressed and how users can achieve them. More detailed scenarios give the design team a fuller picture of **user characteristics and context**, which also feeds into **screen design**.

---

## 9. Use Cases vs. Scenarios at a Glance

| | **Use case** | **Scenario** |
|---|-------------|--------------|
| **Form** | Structured steps: actor, goal, trigger, flows | A narrative story about a specific person |
| **Focus** | What the system must support | Why and how a particular user comes to the site |
| **Detail** | Concise, generic | Rich in context, motivation, and constraints |
| **Perspective** | System behavior responding to the actor | The user's point of view and situation |
| **Used for** | Defining project purpose and requirements | Designing the interface and usability testing |

---

## 10. Key Takeaways

- 🔑 A **use case** = **actor + goal**, with a trigger, a basic flow, and alternate flows.
- 🔑 A **scenario** = a **story** about a specific person with a specific goal; it supplies the **context** use cases lack.
- ⭐ **Metadata and labels** determine whether users can actually find content — use **their** vocabulary.
- ✅ Design from the **user's point of view**, not the developer's.
- 💡 Use cases and scenarios feed directly into **information architecture** (next part).

---

## Review Questions

1. What are the two core components of a use case?
2. What is the difference between a **basic flow** and an **alternate flow**? Give an example.
3. Why does the lecture say a use case should *not* include screen or interface details?
4. How does a scenario differ from a use case?
5. For the flower-ordering scenario, name three design decisions that follow from the story.
6. Why is bad metadata a sign the content may be effectively "lost" to users?
