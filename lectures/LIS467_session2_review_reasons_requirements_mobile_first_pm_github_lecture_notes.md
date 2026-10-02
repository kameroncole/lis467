# LIS 467 — Session 2 Review: Reasons, Requirements, Mobile First, Project Management, GitHub

**Course:** LIS 467 — Web Development & Information Architecture
**Topic:** Recap of Session 2 (reasons for web design, requirements, responsive/mobile-first design, project management, Git/GitHub) and preview of Session 3
**Source:** Panopto lecture transcript — "Session 2 review - reasons, requirements, mobile first, project mgmt, github"

---

## 1. Session 3 Preview

This session covers:

- ⭐ The importance of understanding and describing your **audience**, and building **personas**
- **Design considerations** for websites, with examples of **good and not-so-good** websites
- The full suite of **web development tools** you need to know
- Starting to learn **HTML5**

---

## 2. Recap: What Session 2 Covered

| Session 2 Topic | Key Idea |
|-----------------|----------|
| **Reasons for designing a website** | Why we build sites at all and what a web designer/developer needs to know |
| **Requirements** | Gathering what the site must do before building |
| **Desktop-first vs. mobile-first** | Designing for large screens vs. small screens first |
| **Project management** | Phases of a project; triple constraint |
| **GitHub & version control** | Managing versions of code across a team |

### Discussion questions from Session 2

- What are the **top five skills** you need to be a good web designer/developer? Which do you have, which do you wish to acquire, and what piece of technology would you learn right away?
- How would you describe **responsive design**? What skills are needed to make a website responsive?
- Is it better to design **desktop-first** or **mobile-first**? Why?
- What is your experience with **project management**? What is involved in managing a project?

---

## 3. Technology Influences on Design

Different users experience your site through very different technology, so you must know **which user group** you are designing for.

| Factor | Variation |
|--------|-----------|
| **Browsers** | Different users use different browsers — know which ones your audience uses |
| **Operating systems** | Desktop: Windows, macOS, Linux · Mobile: iOS, Android |
| **Connection speeds** | Vary by state, region, and country |
| **Screen sizes** | Many phone sizes, tablets, laptops of different sizes, desktops |

---

## 4. Desktop-First vs. Mobile-First (Recap)

| Approach | How it works |
|----------|-------------|
| **Desktop-first** (graceful degradation) | Design for the **large screen** first, then decide what to **cut** for smaller screens |
| **Mobile-first** (progressive enhancement) | Design for the **minimum** first, then decide what to **add** as space increases |

💡 **Decluttering-a-house analogy:**
- One way to declutter is to ask *"what should I throw out?"* — hard, because you find yourself wanting to keep almost everything.
- The other way is to ask *"what should I keep?"* — you start with nothing and choose only what you really want.
- ⭐ Mobile-first is like the second approach: it **forces you to think carefully about what is really necessary** versus what is not.

---

## 5. Project Management Recap: The Triple Constraint

Quality in any project depends on balancing **time**, **cost**, and **scope**. Changing one affects the others:

| If… | Then… |
|-----|-------|
| **Scope increases** | You need **more time** and probably **more cost** |
| **Time gets shorter** | **Costs increase** and/or **scope** may need to be reduced |
| **Budget is tight** | You may need **more time** (can't hire many people) and/or must **reduce scope** |

### Planning considerations for a web project

Before building, consider:

- **Audience** — who the site is for and what content goes into it
- **Technical requirements** — what technology is needed
- **Site structure** — what the site will look like structurally
- **Team** — who is on it and what experience they need
- **Timeline** — a few days, a few months, or a year or more?
- **Budget**

⚠️ Small websites may not need much time for each step, but **large websites require all of these to be thought through**.

---

## 6. Git & GitHub Recap

```
 LOCAL COMPUTER                                        REMOTE SERVER
 ┌─────────────────┐  add  ┌──────────┐ commit ┌────────────┐ push  ┌──────────┐
 │ Working directory│ ───▶ │ Staging  │ ─────▶ │ Local repo │ ────▶ │ GitHub   │
 └─────────────────┘       │ area     │        └────────────┘ ◀──── │ (remote) │
                           └──────────┘                       pull  └──────────┘
```

- **Working directory** — where you edit files
- **Staging area** — where you put the files you want to commit
- **Local repository** — your committed history
- **Remote (GitHub.com)** — shared copy; you **push** to it and **pull** from it

⭐ **Team workflow:** one person pushes changes; before another person makes changes, they **pull first** to get the latest version, make their changes, then push. This lets multiple people work on the same website/software **without overwriting each other** and preserves the integrity of the final code.

💡 Git is one of many version control systems, but it's the most widely used.

---

## Key Terms Glossary

| Term | Definition |
|------|-----------|
| **Responsive design** | Design whose layout adapts to different screen sizes |
| **Mobile-first** | Designing for the smallest screen first, then adding features for larger screens |
| **Desktop-first** | Designing for large screens first, then removing features for smaller screens |
| **Triple constraint** | The interdependence of time, cost, and scope in a project |
| **Scope** | The features and work a project includes |
| **Working directory** | Local folder where files are edited |
| **Staging area** | Holding area for changes about to be committed |
| **Local repository** | Committed version history on your computer |
| **Push / Pull** | Send commits to / fetch commits from a remote repository |

---

## Quick Review Questions

1. Name four technology factors that vary across users and influence design.
2. How does the "what to keep" decluttering analogy explain mobile-first design?
3. If a project's scope increases, what happens to time and cost?
4. What planning considerations should be addressed before building a large website?
5. Describe the path a file takes from the working directory to GitHub.
6. Why should you pull before making changes in a team repository?
