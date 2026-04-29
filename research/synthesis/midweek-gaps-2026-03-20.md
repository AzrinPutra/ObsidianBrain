# Midweek Gaps Analysis — Week of April 20–26, 2026

## Summary
This analysis reviews learning materials and daily notes from April 20–26, 2026 to identify topics started but not explored, questions raised but not answered, and concepts repeated. The goal is to surface gaps for further research and consolidation.

## Sources Reviewed
- **Daily notes:** None for this week (2026‑04‑20 through 2026‑04‑22)
- **Memory notes:** 2026‑04‑20.md, 2026‑04‑21.md, 2026‑04‑22.md (all empty)
- **Learning modules:** No updates this week (all module files last modified March 22)
- **Learning web development:**  
  - `javascript_notes.md` (updated this week) – JavaScript date/time, form‑validation basics  
  - `xml_xsl_xsd_notes.md` (updated this week) – XML/XSL/XSD summary and bug fixes  
  - `html_fundamentals.md` – HTML fundamentals with a `TODO: Add navigation bar here`
- **Previous research:** `weekly‑synthesis‑2026‑04‑20.md` (covers April 13–19)

## Key Findings

### 1. Topics Started but Not Explored

**HTML Navigation Bar**
- A `TODO: Add navigation bar here` remains in `html_fundamentals.md`. This indicates intent to practice building a navigation bar but no implementation yet.

**XML/XSL/XSD Deeper Concepts**
- The updated `xml_xsl_xsd_notes.md` covers basic structure, bug fixes, and simple XSL templates. No exploration of advanced XSLT (modes, parameters, keys), XSD constraints (pattern, min/max inclusive), or XML validation pipelines.

**JavaScript Regex Mastery**
- Identified as a gap in last week’s synthesis. The updated JavaScript notes include regex for validation but no practice building custom patterns or exploring security‑filtering applications.

**Python OOP Practical Application**
- Identified as a gap in last week’s synthesis. No new OOP code appears this week; the gap between theory and implementation remains.

**Form‑Validation Security**
- Client‑side validation is covered; server‑side validation and the security implications of relying solely on client‑side checks are still unaddressed.

**Time‑Handling Edge Cases**
- JavaScript date‑handling notes mention 12‑hour conversion and leading zeros, but edge cases (time‑zone handling, daylight saving, internationalization) are absent.

**Cross‑Module Integration**
- No visible connection between Web Dev (front‑end) and OOP (back‑end) concepts; how Python classes could serve as models for form data, or how validation logic could be shared across tiers, is unexplored.

### 2. Questions Raised but Not Answered

**From Last Week’s Synthesis (Weekly‑Synthesis‑2026‑04‑20.md)**
The following five open questions remain unanswered:
1. **From JavaScript Regex to Security Filtering:** If an attacker knows the exact regex used for client‑side validation, how could they craft a payload that passes the regex but still exploits a server‑side vulnerability? What does this teach us about the limits of regex‑based input filtering?
2. **From Python Dunder Methods to Form‑Field Equality:** How would you extend a Python `FormField` class with `__eq__` to support deep equality of nested forms, and what performance pitfalls might arise?
3. **From Real‑Time Date Updates to Anomaly Detection:** What statistical anomalies in `setInterval` timing could indicate a compromised browser or network‑timing side‑channel attack? How could you detect such anomalies?
4. **From Client‑Side Validation to Trust Boundaries:** What architectural changes are required to enforce the same validation on the server side while maintaining a smooth user experience? How can validation logic be written once and shared across client and server?
5. **From OOP Access Specifiers to API Design:** How would you design endpoint permissions (read‑only, read‑write, admin‑only) that mirror the same principle of controlled exposure as Python’s `@property` decorator?

**No new questions were raised in this week’s notes.**

### 3. Concepts Repeated

**JavaScript Date/Time Basics**
- The same date‑handling patterns (12‑hour conversion, leading‑zero fix, `setInterval`) are repeated in `javascript_notes.md` without extension into edge‑case handling or alternative approaches.

**HTML Fundamentals**
- Core HTML tags and syntax are reiterated in `html_fundamentals.md`. This repetition is useful for reference but does not advance practical skill.

## Priority Gaps

### High‑Priority (Immediate Study Impact)
1. **HTML Navigation Bar Implementation** – Complete the TODO in `html_fundamentals.md` by building a functional navigation bar with internal links.
2. **JavaScript Regex Mastery** – Build a regex playground to solidify pattern‑building skills and explore security‑filtering applications.
3. **Python OOP Practical Application** – Implement a Python class with a full dunder suite (`__add__`, `__sub__`, `__mul__`, `__truediv__`, `__eq__`, `__lt__`, `__str__`) and use `@property` for safe attribute access.

### Medium‑Priority (Connective Insight)
4. **Form‑Validation Security** – Add server‑side validation to a toy web app, demonstrating the trust‑boundary principle and re‑using validation regex across client and server.
5. **XML/XSL/XSD Deeper Understanding** – Create a small project that validates an XML file against an XSD and applies an XSLT transformation with advanced features (modes, parameters).
6. **Cross‑Module Integration** – Sketch a simple web form backed by a Python class, showing how OOP models can mirror front‑end field structure.

### Low‑Priority (Administrative/Edge Cases)
7. **Time‑Handling Edge Cases** – Research and document time‑zone handling, daylight‑saving adjustments, and internationalization for JavaScript date displays.
8. **Daily‑Note Discipline** – Daily notes remain empty; need to capture learning logs, questions, and reflections.

## Recommended Actions

1. **Schedule a 30‑minute session** to build the HTML navigation bar and commit the change.
2. **Create a regex playground** (HTML/JS page) that lets you test regex patterns against sample inputs, with explanations of each part of the pattern.
3. **Implement a `Vector` or `Matrix` class** in Python with full dunder methods and properties.
4. **Extend the CSIT128 assignment form** with a simple Flask/Django backend that re‑uses the same validation regex on the server.
5. **Design a small XML‑validation pipeline** using `lxml` or a similar library, and write an XSLT that uses modes or parameters.
6. **Sketch a cross‑layer model** that maps Python class attributes to HTML form fields and validation rules.

## Next Steps
- Add task to `system/inbox.md` for the assistant to send a Telegram summary.
- Schedule the 30‑minute navigation‑bar session for the next available study block.
- Review the five open questions from last week’s synthesis and allocate time to answer at least one per week.

---
*Analysis generated by midweek‑gaps cron job on 2026‑04‑22 23:00 SGT.*