# LIS 467 — Session 1 Review: Client-Server, HTTP & History of the WWW

**Course:** LIS 467 — Web Development & Information Architecture
**Topic:** Review of Session 1 — Client-Server Architecture, HTTP, and the History of the World Wide Web
**Source:** Panopto lecture transcript — "Session 1 review - Client-Server; HTTP; History of WWW"

---

## 1. Session Overview

This session opens by previewing upcoming topics — why web design matters, gathering requirements for a web design project, responsive and mobile-first design, project management, and version control — and then reviews the core concepts from Session 1:

- Distinguishing between **client** and **server**
- The **HTTP** request/response cycle
- Key developments in the **history of the Internet and the World Wide Web**

---

## 2. Client vs. Server

🔑 **Key question:** Can one computer perform both roles?
✅ **Yes.** One computer can act as both a client and a server — you can install server software on your local computer.

| Role | Definition |
|------|------------|
| **Client** | Anything that *requests* services |
| **Server** | A computer that *provides* services to clients |

### Architecture Tiers

| Architecture | Description |
|--------------|-------------|
| **Two-tier** | Client ↔ Server (simple) |
| **Three-tier** | Client ↔ Application server ↔ Database server (database separated from application logic) |
| **N-tier** | Multiple separated layers — various applications and services each on their own tier |

💡 Separating the database and applications into their own tiers is what moves you from two-tier to three-tier (and beyond) architecture.

---

## 3. The HTTP Request/Response Cycle

The typical process:

1. The **end user** acts on the **client** (browser).
2. The client sends a **request** (e.g., an HTTP `GET` to fetch something) over the **network** to the **server**.
3. The server — often with a **database** attached — processes the request.
4. The server returns a **response** to the client: HTML pages, CSS, JavaScript, and so on.

### GET vs. POST

| Method | Purpose | Example |
|--------|---------|---------|
| **GET** | Request/retrieve a resource; server returns an acknowledgment (e.g., `200 OK`) and content | Fetching a web page |
| **POST** | Submit data to the server | Logging in with a username/password — the server checks credentials against the database to see if you're authorized |

⚠️ Remember: the connection between client and server is a *stateless* request/acknowledgment exchange — each request gets its own response.

---

## 4. History of the World Wide Web (Timeline: 1989–2019)

### The Beginning

| Year | Event |
|------|-------|
| **1989 (March)** | ⭐ English engineer/computer scientist **Tim Berners-Lee** writes the *Information Management: A Proposal* — his vision for what would become the World Wide Web |
| **1990** | First version of a search engine conceived; Internet users reach ~2.6 million; Berners-Lee creates **HTTP**, **URLs**, and the **very first browser** (WorldWideWeb) |
| **1993** | World Wide Web software released into the **public domain**; early domains registered |
| **1994** | **Yahoo!** directory service born; **WebCrawler**, the first full-text search engine, launches; first banner ads appear; Internet users reach ~44 million |

### The Browser Wars & Web 1.0

| Year | Event |
|------|-------|
| **1995** | **Microsoft Internet Explorer** launches (~a year after **Netscape Navigator**) and quickly becomes one of the most popular browsers, displacing Netscape |
| **1997** | Pop-up ads appear |
| **1998** | **Google** search introduced to consumers |
| **1999** | **Napster** released — peer-to-peer file sharing for music/movies, later shut down over piracy; **Blogger** launches, empowering ordinary people to publish without depending on news media or being computer experts |
| **2000** | Internet users ~412 million; the **dot-com bubble bursts**, wiping out many online startup companies |

### Web 2.0 and Social Media

| Year | Event |
|------|-------|
| **2001** | **Wikipedia** launches |
| **2002** | **Firefox** browser emerges as open-source software |
| **2003** | **WordPress** released; **MySpace** launches — a precursor whose ideas eventually lead to Facebook |
| **2004** | ⭐ **Facebook** founded (launched publicly Feb 2005 per timeline); **Gmail** era begins |
| **2005** | **YouTube** created by three former PayPal employees |
| **2006** | **Twitter** founded; **Netflix** begins shifting from mailing physical DVDs to online video streaming |
| **2007** | The **#hashtag** becomes common; **iPhone** era begins |
| **2008** | **App Store** and **Android Market** launch |

### The Mobile & Billion-User Era

| Year | Event |
|------|-------|
| **2010** | Internet users reach ~1.9 billion; **Instagram** founded (Kevin Systrom et al.); **Pinterest** released later that year |
| **2012** | Continued platform growth |
| **2016** | Internet users ~3.4 billion |
| **2018** | A tough year for **Facebook** — data-privacy scandals and controversies |
| **2019** | The "world record egg" — a simple photo of an egg on Instagram breaks the world record (~18 million likes) within ten days; by 2019+ the photo passed 54 million likes |

💡 **Big picture:** In 30 years the web went from one engineer's proposal to billions of users, transforming publishing (blogs), commerce (dot-coms, Amazon), media (Netflix, YouTube), and social interaction (Facebook, Twitter, Instagram).

---

## 5. Key Terms Glossary

| Term | Definition |
|------|------------|
| **Client** | Any computer/program that requests services from a server |
| **Server** | A computer/program that provides services to clients |
| **Two-tier architecture** | Direct client ↔ server model |
| **Three-tier architecture** | Client ↔ application server ↔ database server |
| **HTTP** | HyperText Transfer Protocol — governs request/response between client and server |
| **GET** | HTTP method for requesting/retrieving resources |
| **POST** | HTTP method for submitting data (e.g., login credentials) to the server |
| **Tim Berners-Lee** | Inventor of the World Wide Web (1989 proposal; created HTTP, URLs, first browser) |
| **Dot-com bubble** | Speculative boom in Internet startups that collapsed around 2000 |
| **Web 2.0** | Era of user-generated content and social platforms (blogs, wikis, social media) |

---

## 6. Quick Review Questions

1. Can a single computer act as both a client and a server? Explain.
2. What is the difference between two-tier and three-tier architecture?
3. Describe what happens between the client and server when a user logs into a website (which HTTP method is used, and what does the server check?).
4. Who proposed the World Wide Web, in what year, and what three foundational technologies did he create?
5. Which browser did Internet Explorer displace in the mid-1990s?
6. What happened to Internet startup companies around the year 2000?
7. Name two 2004–2006 launches that defined the social media era.
8. Roughly how many Internet users were there in 1990, 2000, 2010, and 2016?
