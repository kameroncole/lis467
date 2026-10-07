# LIS 467 — Session 4, Part 3: Card Sorting

**Course:** LIS 467 — Web Development & Information Architecture
**Topic:** Card sorting (open and closed), tree testing, and first-click testing as methods for designing and evaluating information architecture
**Source:** Panopto lecture transcript — "Session 4 Part 3 Card Sorting"

---

## 1. Why Test Your Information Architecture?

You have a draft IA — now how do you know it makes sense to **real users**? **Card sorting** is a powerful technique that can be used to **both design and evaluate** a website's information architecture. Related methods — **tree testing** and **first-click testing** — help validate it.

---

## 2. What Is Card Sorting?

🔑 **Card sorting** is a method for discovering the **latent structure** in a list of statements, ideas, or content items by asking people to **group them**.

### Procedure

1. Write **each content item or label** from the site (every page, topic, or term) on its **own index card** (about **3 × 5 inches**; typical studies use roughly **30 to 200 cards**).
2. Ask participants to **sort the cards into groups** that make sense to them.
3. Have participants **work on their own**, then collect each person's results.
4. **Analyze** the results — informally, or **statistically** if needed — to find where participants agree.

### Who should participate?

- Ideally, **representative members of your user population** — people for whom you are designing.
- A small group can be useful: the lecture mentions roughly **four to six** participants, depending on who is available.
- ⭐ If you cannot reach real users, even a **friend, colleague, or family member** can show whether your groupings and category names make sense to someone other than you.

### What you learn

- How **other people group and label** your content.
- Which **categories make sense to them**, and what **names** they would give those groups.
- It reflects **the structure in which users expect ideas or concepts to be presented** — rather than the structure that makes sense only to the site's creators.

---

## 3. Two Types of Card Sorting

### 3.1 Open card sorting

- Participants **sort cards into groups they create themselves** and **write their own category names**.
- Captures **participants' mental models** — how *they* structure information.
- ✅ An **exploratory** technique: best used **early**, when you **don't yet know** how to structure the information.

### 3.2 Closed card sorting

- Participants are **given predefined categories** and **place cards** where they think each belongs.
- Example: for a **grocery store**, print cards with items (cucumber, milk, bread…) and give categories ("Produce," "Dairy," "Bakery"); see where people put each item.
- ✅ A **validation** technique: use it when you **already have categories** and want to test whether they work.

| | **Open sort** | **Closed sort** |
|---|---|---|
| **Categories** | Created by participants | Provided in advance |
| **Purpose** | **Exploratory** — discover how users group | **Validation** — test a proposed structure |
| **When** | Early design | After you have draft categories |
| **Output** | Groupings **and** labels | Which category each card lands in |

⭐ The fundamental difference: **open sorting captures participants' own models; closed sorting checks an existing one.**

💡 In practice, some people use **hybrid** approaches — participants sort into provided categories but may also **create new ones** (the lecture notes that the continuum between open and closed is flexible).

---

## 4. Other Methods for Improving IA

The author the instructor cites argues that closed card sorting is not always the best validation tool — **other techniques may be equally or more useful**.

### 4.1 Tree testing (reverse card sorting)

🔑 **Tree testing** evaluates the **findability** of topics in a **text-only version of the site hierarchy**, stripped of navigation aids and design elements. It is sometimes called **reverse card sorting**, since it starts with the structure rather than the cards.

- Present participants with the **tree** (a nested hierarchy of headings; one branch can be expanded at a time).
- Give a **task**: e.g., *"You want to find your photos from your vacation in Greece."*
- Observe the **path** they click through the folders/headings and whether they **find the right place**.
- Example analogy: finding a file on your computer by moving through nested **folders**.

**Advantages:** it yields **navigation information** (the path taken), not just final placement as in a closed sort.
**Disadvantage:** it takes **longer** — more time to **design the test** and for the user to complete it.

### 4.2 First-click testing

🔑 **First-click testing** shows users a **screenshot** (a design or wireframe) and asks them to indicate **where they would click first** to complete a task.

- Example: show an **online grocery store** screenshot and ask, *"Find a cucumber."* If they click the menu heading **"Produce,"** the label works.
- Question it answers: **"Where would you click to get where you need to go?"** for a particular use case.
- ✅ **Fast and efficient** — takes very little time and helps a team **get unstuck on a design decision**.

---

## 5. Choosing a Method

| Method | Answers | Stage | Effort |
|--------|---------|-------|--------|
| **Open card sort** | How do users group and name content? | Early / generating IA | Moderate |
| **Closed card sort** | Do users put items where I expect? | Validating categories | Moderate |
| **Tree test** | Can users **find** items in my hierarchy? | Validating a proposed structure | Higher |
| **First-click test** | Do users know where to start on this screen? | Validating labels/layout | Low |

Open card sorting helps **create** the architecture; closed sorting, tree testing, and first-click testing help **validate** the structure and labels you have come up with.

---

## 6. Key Takeaways

- 🔑 **Card sorting** shows how users **group and label** content; **open** = generate, **closed** = validate.
- 🔑 **Tree testing** tests **findability** in the hierarchy and gives **path information**.
- 🔑 **First-click testing** is a **quick** check of whether labels lead users the right way first.
- ⭐ Test with **representative users** whenever possible; otherwise use **colleagues or friends** rather than guessing.
- ✅ Combine methods: use **open sorting** to build, then **tree/first-click tests** to confirm.

---

## Review Questions

1. How do you physically conduct a card sort?
2. What is the main difference between open and closed card sorting, and when would you use each?
3. Why is tree testing sometimes called "reverse card sorting"?
4. What extra information does tree testing provide compared with a closed card sort? What is the cost?
5. Describe a first-click test for a library website: what task would you give and what would you look for?
