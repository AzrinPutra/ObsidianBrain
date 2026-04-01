# Midweek Gaps Analysis — Week of March 25–April 1, 2026

## Summary
This analysis reviews learning materials and daily notes from March 25–April 1, 2026 (mid‑week of semester start) to identify topics started but not explored, questions raised but not answered, and concepts repeated. The goal is to surface gaps for further research and consolidation.

## Sources Reviewed
- Daily notes: 2026‑03‑25.md (empty), 2026‑03‑30.md (Python OOP practice), 2026‑04‑01.md (planned tasks)
- Learning modules: Python OOP (module + rich comparisons note), HTML Fundamentals (new), Networks (CSIT127), Systems Analysis (CSIT114), Cyber Fundamentals (CSIT123)
- Notes: Python_OOP_Rich_Comparisons.md (created Apr 1)
- Previous research: midweek‑gaps‑2026‑03‑20.md (previous week’s gaps)

## Key Findings

### 1. Topics Started but Not Explored

**Python OOP – Inheritance & Case Study**
- Supplier class inheritance example stops before implementing `order()` method.
- Notebook case study `search()` method returns first matching note only; should return a list.
- No discussion of polymorphism, abstraction, or practical OOP patterns beyond basic inheritance.
- The `functools.total_ordering` decorator introduced but not yet applied to any class in active code.

**Python OOP – Syntax & Correctness**
- Practice code in 2026‑03‑30.md contains multiple syntax errors:
  - `init` instead of `__init__`
  - `__str` instead of `__str__`
  - `__eq` instead of `__eq__`
  - Private attribute access (`self.__length`, `self.__width`) mismatched with `self.length`, `self.__width`.
- These errors indicate confusion about dunder method names and private attribute conventions.

**Web Development – HTML Fundamentals**
- Day 1 notes are comprehensive but stop after basic HTML; no follow‑up on forms, CSS, or JavaScript (mentioned as “Coming Up Next”).
- No practical exercises or project started to apply the tags and structures described.

**Networks (CSIT127)**
- Digital encoding schemes (NRZ‑L, NRZI, Manchester, Differential Manchester) introduced but no examples of decoding or real‑world applications (Ethernet, Wi‑Fi).
- OSI model layers described but no mapping to TCP/IP or modern protocols.
- ARP/DHCP/DNS relationship mentioned but not elaborated.

**Systems Analysis (CSIT114)**
- Many rhetorical questions in module notes left unanswered:
  - “Why do IT projects fail despite good developers?”
  - “What components make up an information system?”
  - “Why are stakeholders important?”
  - “How does Agile SDLC differ from traditional approaches?”

**Cyber Security Fundamentals (CSIT123)**
- Logic gates and DeMorgan’s Law covered, but no connection to cryptographic circuits or hardware security.
- Overflow detection explained but not linked to buffer‑overflow vulnerabilities.

### 2. Questions Raised but Not Answered

From previous weekly synthesis (March 20) – still unanswered:
- How might Python's `__init__` patterns apply to malware analysis sandbox initialization?
- Could CSS specificity rules inform security policy precedence models?
- What parallels exist between OOP polymorphism and polymorphic malware detection?
- How do HTML semantic tags relate to threat intelligence taxonomy development?
- Can Python's exception handling inform SIEM alert triage workflows?

From daily notes (2026‑04‑01):
- No explicit questions logged, but learning logs are sparse; the “Learning Log” section is empty for most days.

From pending tasks (2026‑04‑01):
- “Watch CSIT121 Web Dev lecturer” – not yet started.
- “Create and do some examples based on the lecture” – not yet started.
- “Read CSIT128 OOP lecturer notes 1‑3” – not yet started.
- “Refresh what you practised yesterday based on the examples” – not yet started.

### 3. Concepts Repeated

**Python OOP**
- `__init__`, attributes, classes reiterated across multiple sections (module, rich‑comparisons note, practice code).
- Notebook case study appears both as UML diagram and code, but same core concepts repeated.

**Networks**
- Internet/Intranet/Extranet definitions repeated with similar diagrams.
- Hub vs Switch vs Router table appears in multiple forms.

**Binary/Logic Fundamentals**
- Two’s complement, overflow detection repeated across CSIT123 notes.

## Priority Gaps

### High‑Priority (Direct Study Impact)
1. **Python OOP syntax correction** – fix dunder method names and private attribute usage in practice code.
2. **Python OOP completeness** – finish inheritance example (implement `order()`), fix `search()` to return list, introduce polymorphism.
3. **Web Dev practical application** – create a simple HTML page using all tags from fundamentals, then move to forms/CSS.
4. **Systems‑analysis unanswered questions** – answer the “why” and “how” questions that appear in notes.

### Medium‑Priority (Connective Insight)
5. **Security‑development parallels** – explore the weekly‑synthesis questions linking Python/OOP to malware analysis, SIEM workflows.
6. **Networks encoding practicals** – connect Manchester encoding to Ethernet frames, show real‑world traces.
7. **Logic‑gates to hardware‑security** – show how DeMorgan’s Law applies to secure circuit design.

### Low‑Priority (Administrative)
8. **Daily‑note discipline** – learning logs are minimal; need consistent capture of what was studied, what questions arose.
9. **Module prioritization** – which modules are active vs. reference? Clear focus needed as term began March 25.

## Recommended Actions

1. **Create focused research tasks** for each high‑priority gap:
   - “Fix Python OOP practice code dunder methods and private attributes”
   - “Complete Supplier class with order() method”
   - “Implement Notebook search returning list of notes”
   - “Build a simple HTML page using all fundamental tags”
2. **Schedule Q&A sessions** to answer the unanswered questions from CSIT114 and weekly synthesis.
3. **Enhance daily notes** with explicit “Questions Raised” and “Concepts to Explore” sections.
4. **Update learning modules** with completed examples and connections to security/cyber themes.

## Next Steps
- Add task to system/inbox.md for assistant to send Telegram summary.
- Schedule 30‑minute review session to address one high‑priority gap per day.
- Set up cron reminder for end‑of‑week synthesis (Friday evening).

---
*Analysis generated by midweek‑gaps cron job on 2026‑04‑01 23:00 SGT.*