# LIS 467 — Session 10: jQuery and Usability Testing

**Course:** LIS 467 — Web Development & Information Architecture  
**Topic:** jQuery fundamentals, usability evaluation, and think-aloud testing  
**Source:** [LIS467-Session10.pdf](./session10/LIS467-Session10.pdf) — lecture slides

> These notes summarize the available slides. They are not a transcript of the Panopto recording.

---

## 1. jQuery

jQuery is a lightweight JavaScript library intended to make common website tasks easier, following the idea “write less, do more.” It wraps frequent operations in concise methods and works across browsers.

Its features include:

- HTML and DOM manipulation
- CSS manipulation
- HTML event methods
- Effects and animations
- AJAX and other utilities
- A large ecosystem of open-source plugins

### Selectors and functions

Selectors identify the elements a jQuery operation should affect. They use familiar CSS-style patterns:

- `button` selects `<button>` elements.
- `a` selects anchor elements.
- `span` selects `<span>` elements.
- `div` selects `<div>` elements.
- ID and class selectors target particular elements or groups of elements.

The slides also identify anonymous functions as the preferred method for supplying behavior to jQuery operations.

---

## 2. Usability

The slides present several complementary definitions of usability:

- **Shackel (1981):** how easily and effectively a specified range of users can use a system, with specified training and support, to complete specified tasks in specified environments.
- **ISO 9241:** the effectiveness, efficiency, and satisfaction with which specified users achieve specified goals in particular environments.
- **Nielsen (2003):** a quality attribute that assesses how easy user interfaces are to use.

Nielsen's five usability components are:

1. **Learnability** — how easily users can accomplish basic tasks the first time.
2. **Efficiency** — how quickly users can perform tasks once they have learned the design.
3. **Memorability** — how easily returning users can reestablish proficiency.
4. **Errors** — how many errors users make, how severe they are, and how easily they recover.
5. **Satisfaction** — how pleasant the interface is to use.

---

## 3. Usability Evaluation Methods

| Method | What it does |
|---|---|
| **Quick, informal evaluation** | Collects informal feedback from users or consultants. |
| **Usability testing** | Measures typical users' performance on carefully prepared, representative tasks; gathers performance and preference data. |
| **Field study** | Studies what people naturally do in their real environment, using unobtrusive or participant observation. |
| **Predictive evaluation** | Experts use their knowledge of users, often with heuristics, to predict usability problems. |

Usability matters for library resources because many are accessed online, including OPACs, interlibrary loan, electronic databases, pathfinders, and archival finding aids. Their interfaces can affect how often and how effectively people use them.

---

## 4. Start With Users' Tasks

Usability is tied to what users are trying to do. Researchers need a deep understanding of those tasks before evaluating an interface.

1. Brainstorm the tasks the interface needs to support.
2. Try those tasks and consider what could obstruct users.
3. Use realistic examples based on tasks people are expected to perform.

Tasks should be representative of real-life use, and real task examples are preferable when available.

---

## 5. Think-Aloud Testing

In a think-aloud study, participants say what they are thinking as they complete tasks. This helps the researcher understand both what participants do and why they do it.

### Choosing and ordering tasks

- For maximum control, give every participant the same tasks.
- To reduce ordering effects, vary or randomize task order across participants.
- For a more naturalistic approach, describe a type of task but let participants choose some details. For example: “Use the online catalog to search for works by an author you particularly like.”

### Formative and summative use

Think-aloud testing can be:

- **Formative:** used before or during development to inform design and improve the interface iteratively.
- **Summative:** used to evaluate an existing interface and identify usability issues.

### Participants

- Identify the target population and recruit as representative a sample as possible.
- A study may focus on a subpopulation, with multiple studies used to cover distinct groups.
- Relevant participant characteristics may include computer expertise, workplace role, and domain expertise; gather these with a questionnaire before or after the protocol.
- The slides suggest that **8–10 participants** from a population are generally enough to reveal most usability problems in a think-aloud study, given the richness of the data.

### Running the session

1. Explain the process: “I will give you a task. Please keep talking out loud while performing the task.”
2. Give a practice task so participants can try thinking aloud. Keep it similar to the real tasks without making it one of them.
3. Let participants work with as little interruption as possible.
4. If a participant stops speaking, prompt them neutrally: “Please keep talking.”
5. After tasks, ask about difficult moments and invite participants to summarize what they liked and disliked.

---

## 6. Recording and Analyzing Data

The fullest recording could combine:

- Video of the participant's face, screen, and keyboard
- Screen capture
- Keystroke capture
- Observer notes

It may not be practical or possible to collect all of these. When taking notes by hand, record what participants say and where they struggle—even if they do not consistently think aloud—so those moments can be explored at the end.

### Coding the findings

1. Transcribe the data.
2. Develop a coding scheme, usually bottom-up: create codes for behaviors as they appear.
   - Example: difficulty locating the full-text databases link could be coded as a **navigation problem**.
3. Re-read the data and apply the codes consistently to each occurrence.
4. When possible, have two independent coders apply the scheme. Comparing their results can help limit experimenter bias; statistical measures can assess inter-rater reliability.

The slides identify two key outputs: **problems participants encountered** and **recommendations for solving those problems**.

---

## 7. Strengths and Limitations of Think-Aloud Testing

### Strengths

- Provides a deep understanding of how users perform tasks.
- Helps identify usability problems in a particular interface.
- Requires relatively little specialized training or expertise.
- Captures feedback while the user is doing the task.

### Limitations

- Participants' comments are subjective and may be selective.
- Findings depend on how completely the session is recorded.
- Analysis can take substantial time.
- Interrupting participants can distort what they report.

---

## 8. Aesthetics and Further Reading

The slides include references on color theory and aesthetics:

- [Color theory introduction — Tiger Color](http://www.tigercolor.com/color-lab/color-theory/color-theory-intro.htm)
- [Understanding aesthetics](https://www.lynda.com/Design-Techniques-tutorials/Welcome/506078/539532-4.html)

They also link to two usability-testing resources:

- [Usability testing, Part 1 — UX Knowledge Base](https://uxknowledgebase.com/usability-testing-part-1-e00a94974c79)
- [Usability testing, Part 2 — UX Knowledge Base](https://uxknowledgebase.com/usability-testing-part-2-4f27e8a6521e)

The final slide defines **cognitive bias** as an error in reasoning, evaluation, memory, or another cognitive process, often related to retaining preferences or beliefs despite contrary information.

---

## 9. Key Takeaways

- jQuery simplifies common JavaScript work such as DOM changes, events, effects, and AJAX.
- Usability concerns effectiveness, efficiency, and satisfaction for specified users, goals, and environments.
- Evaluate interfaces using realistic user tasks; usability problems are inseparable from what people are trying to accomplish.
- Think-aloud testing reveals users' actions and reasoning, and can support both iterative design and evaluation of existing interfaces.
- Use representative participants, neutral prompts, and careful recording; transcribe and code observations systematically.
- Balance the depth of think-aloud findings against subjective reporting, recording limitations, interruption effects, and analysis time.

---

## Review Questions

1. What kinds of work does jQuery simplify, and how do selectors determine which elements are affected?
2. Name Nielsen's five usability components.
3. How does usability testing differ from a field study or predictive evaluation?
4. Why should usability tasks be realistic and representative?
5. What is the difference between formative and summative think-aloud testing?
6. How can task order and participant selection affect a study?
7. What should a moderator do if a participant stops thinking aloud?
8. How does a bottom-up coding scheme help analyze observations? Why might independent coders be useful?
9. What are the main strengths and limitations of think-aloud testing?
