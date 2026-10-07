# LIS 467 — Session 4, Part 5: Test versus Production Sites

**Course:** LIS 467 — Web Development & Information Architecture
**Topic:** Production, testing, and development web servers; why to separate them; and the typical workflow from local machine to live site
**Source:** Panopto lecture transcript — "Session 4 Part 5 Test versus Production sites"

---

## 1. Terminology

Several terms are used for the **servers** involved in building a website: **production web server**, **development web server**, and **testing web server**. They are used somewhat differently across organizations, so it helps to define them clearly. Throughout, the **designer/developer** works on **site pages and graphics files** that are eventually stored on a server.

---

## 2. Types of Servers

### 2.1 Production web server

🔑 A **production web server** hosts the **webpages and content that are ready for the public** — the **live site**.

- It is **connected to the Internet** and delivers content to real visitors.
- In a **small company** or simple setup, you may have **only** this server plus your **local computer**.
- Workflow in that simple case: design and test **locally** on your own machine, then use an **FTP (file transfer) program** to **transfer files from your local computer to the production server**.

### 2.2 Testing web server

🔑 A **testing server** lets you **try new pages and designs on a web server that is not visible to customers/public visitors**.

⭐ **Why it matters:** the production server may have **hundreds or thousands of users connected** at once. You do **not** want to put **untested pages** there — **if something goes wrong, live pages could be affected**.

- Gives a safe place to check that things work **on a real server environment**, not just your laptop.
- Typically paired with **version control** so every change is **recorded**.

### 2.3 Development web server

🔑 A **development server** is similar, but is used when the site includes **server-side logic and applications** — **scripts and programs** written by **developers** (the **back end**, e.g., databases and server code).

- **Designers** work on **designs on their local machines**.
- **Developers** write scripts and programs on the **development server**.
- Multiple people collaborate using a **version control system**.

💡 The **back-end** work is not a major focus of this course, but you should know the environments exist.

---

## 3. The Typical Workflow

```
 Local machine  ──►  Development server  ──►  Testing server  ──►  Production server
 (design/edit)       (scripts, programs)      (QA / approval)       (live to the public)
```

1. **Design and edit locally** on your own computer (as in the first labs).
2. **Move to development** (if the site has application code) and integrate with developers' work.
3. **Move to the testing server** for review and approval.
4. Once **approved and ready**, **deploy to the production server** — the new addition **goes live**.
5. Throughout, use **version control** (e.g., Git/GitHub) to track changes among team members.

✅ **Minimum setup:** at least a **test** environment separate from **production**. A single server may serve both development and testing in smaller organizations, but you should always keep **production** separate.

---

## 4. Comparison Table

| | **Local machine** | **Development** | **Testing** | **Production** |
|---|---|---|---|---|
| **Who uses it** | Individual designer | Developers (and designers) | QA / team / client | **The public** |
| **Content** | Work in progress | Code being written | Candidate release | **Approved, live** |
| **Visible to public?** | No | No | **No** | **Yes** |
| **Risk if broken** | None | Low | Low | **High** |
| **Version control** | Local repo | Shared | Shared | Deployed from approved version |

---

## 5. Key Takeaways

- 🔑 **Production** = the **live site** the public sees.
- 🔑 **Testing** = a **non-public copy** for verifying changes before they go live.
- 🔑 **Development** = where **developers** build and integrate **server-side code**.
- ⭐ **Never test on the production server** — mistakes affect real users.
- ✅ Use **FTP** (or deployment tools) to publish, and **version control** to track changes.
- 💡 Keep **production separate** from the machine where you do most of your design work.

---

## Review Questions

1. What is a production web server?
2. Why is a separate testing server valuable?
3. How does a development server differ from a testing server?
4. Describe the path of a change from your local machine to the live site.
5. In a small organization with only a local computer and a production server, how are files moved to the live site?
6. What role does version control play in this workflow?
