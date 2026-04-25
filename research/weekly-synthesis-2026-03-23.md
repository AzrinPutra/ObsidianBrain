# Weekly Synthesis: April 20–25, 2026

## This Week In Review

### Learning Progress
- **Web Development (CSIT128)**: Completed **Assignment 1** (JavaScript Form) on April 20. Started **Assignment 2** (XML, XSL, XSD) – progressed on XML structure, XSD validation, XSL template matching, attribute‑value templates, and CSS fixes. Key lessons: XML‑stylesheet placement, enum case sensitivity in XSD, XSL `xsl:choose/when` for month‑name conversion, and Chrome security restrictions for local XSLT (requiring a local HTTP server).
- **Python OOP (CSIT121)**: Completed **Assignment 1** on April 20. **Assignment 2** (due May 2) likely started; OOP concepts (access specifiers, `@classmethod`, `@property`, dunder methods) reviewed but not yet applied in new code.
- **Cybersecurity Wellness Schedule**: Created a weekly reminder plan (`notes/cyber_ wellness_schedule.md`) balancing Splunk study, TryHackMe SOC Level 1, gym, run, and social time, with explicit override rules for uni deadlines.
- **CSIT128 Quiz**: Attended on April 20 (no attendance marking required).

### Tasks & Deadlines
- ✅ CSIT128 Web Dev Assignment 1 – submitted April 20
- ✅ CSIT121 OOP Assignment 1 – submitted April 20
- ✅ CSIT128 Quiz – completed April 20
- 🔄 CSIT128 Web Dev Assignment 2 – due May 11, 2026
- 🔄 CSIT121 OOP Assignment 2 – due May 2, 2026
- 🎯 Splunk Core User Certification – target May 29, 2026
- 🔄 TryHackMe SOC Level 1 – ongoing through April–June

### Knowledge Gaps Identified
- **XML/XSL Security Blind‑Spot**: No consideration of XML injection (XXE), XSLT code‑injection vulnerabilities, or DTD‑based attacks that could affect web applications processing user‑supplied XML/XSL.
- **Web‑Dev ↔ Cybersecurity Integration**: XML/XSL skills are being learned in isolation; no attempt to apply them to security‑relevant data (e.g., transforming Splunk logs, creating custom SIEM visualizations).
- **OOP Practical Application Deficit**: While dunder methods (`__eq__`, `__lt__`, `__add__`, `__truediv__`) and `@property` are listed in notes, there is no evidence of implementing them in actual code (e.g., a `Vector` class with operator overloading or a `FormField` class with validation).
- **Time‑Management Optimization**: The schedule includes fixed weekly blocks but no feedback loop to measure actual time spent vs. planned, nor an algorithm to dynamically reschedule when uni deadlines override sessions.
- **Splunk Study vs. Hands‑On Lab**: Certification target is set, but no visible lab environment (Splunk instance, sample logs, ingestion pipelines) to practice the concepts being studied.

## Key Connections (Non‑Obvious)

### 1. XML/XSLT as a Security Log Transformation Pipeline
XML is a common format for configuration files (Splunk configs, Windows Event Log) and log data. XSLT can transform raw XML logs into human‑readable reports, dashboards (HTML), or other formats (CSV, JSON) for analysis. The web‑dev assignment’s focus on XSL templates and attribute‑value templates directly equips you to build custom log‑transformation scripts—a skill used in threat‑hunting to convert vendor‑specific log formats into a uniform schema for correlation.

### 2. OOP Encapsulation and Role‑Based Access Control (RBAC)
Private attributes with getters/setters enforce controlled access to object state, similar to RBAC where direct resource access is restricted and permissions are validated. Modeling security principals (users, roles) as Python objects with `@property`‑based accessors could provide a clean abstraction for implementing and auditing access‑control policies, bridging OOP design patterns with cybersecurity principle of least privilege.

### 3. Weekly Schedule Override Rules as a Priority‑Queue Algorithm
The rule “Uni Deadlines Rule: Always override Monday/Wednesday sessions” is a simple priority‑based preemption policy. This mirrors scheduling algorithms used in operating systems and resource‑management systems. Formalizing this as a priority‑queue simulation could help optimize personal productivity by predicting conflicts and dynamically rescheduling lower‑priority tasks, a concept applicable to automated task‑scheduling in DevOps pipelines.

## Open Questions (Socratic)

1. **From XML/XSL to Log Injection Attacks**: If an attacker can inject malicious XML entities into a log file that later gets processed by XSLT, what types of attacks (XXE, XSLT code injection) become possible, and how could XSD validation be extended to detect or prevent such injections while still allowing legitimate log‑transformation workflows?

2. **From OOP Getters/Setters to Audit Trails**: If every attribute access goes through a getter/setter, how could you automatically generate an audit log of who accessed what and when? How would this pattern apply to a cybersecurity monitoring system that needs to track access to sensitive configuration data?

3. **From Schedule Overrides to Dynamic Resource Allocation**: If uni deadlines override scheduled wellness sessions, how could a dynamic scheduling algorithm predict future conflicts and reschedule wellness sessions proactively, minimizing disruption? What data (deadline dates, estimated effort, session flexibility) would such an algorithm need?

4. **From XSLT Templates to SIEM Dashboard Visualization**: XSLT transforms XML data into HTML tables. How could this be used to build custom SIEM dashboards that transform raw log XML into interactive visualizations? What security considerations arise from allowing users to upload custom XSLT stylesheets (e.g., script injection, denial‑of‑service via complex transformations)?

5. **From Python Dunder Methods to Threat‑Indicator Comparisons**: If threat indicators (IP addresses, file hashes) are modeled as Python objects with `__eq__`, `__lt__`, how could you build a threat‑intelligence lookup system that efficiently compares incoming indicators against a large database using these dunder methods? What performance bottlenecks might arise from naïve comparison of thousands of indicators per second?

## Recommended Next Topics

### Immediate (Next 7 Days)
1. **Build a Simple XML Log Transformer**: Using the XSLT skills from Assignment 2, create a script that transforms a sample Windows Event Log XML file into an HTML report, practicing security‑relevant data transformation.
2. **Implement a Python Class with Full Dunder Suite**: Write a `Vector` or `Matrix` class that implements `__add__`, `__sub__`, `__mul__`, `__truediv__`, `__eq__`, `__lt__`, and `__str__`, and uses `@property` for validated attribute access. This bridges the OOP theory‑practice gap.
3. **Conduct a Time Audit**: For three days, track actual time spent on uni work, wellness activities, and cybersecurity study. Compare with the planned schedule to identify systematic deviations and adjust the plan accordingly.

### Medium‑Term (Next 2–3 Weeks)
4. **Set Up a Splunk Lab Environment**: Using Docker or a free Splunk instance, ingest sample logs (e.g., Apache access logs, Windows security events) and run basic searches, creating a hands‑on foundation for the certification target.
5. **Develop a Priority‑Based Scheduler Algorithm**: Model the weekly schedule as a priority queue where tasks have deadlines, estimated duration, and flexibility. Implement a simple algorithm that reschedules lower‑priority tasks when higher‑priority deadlines appear.

### Long‑Term (Monthly)
6. **Design a Unified Validation Framework**: Combine XSD for structural validation, regex for content validation, and Python classes for business‑logic validation into a reusable library that can be applied both in web‑dev assignments and security‑tooling (e.g., validating configuration files, filtering malicious input).

## Reflection
This week saw the completion of two major assignments (Web Dev and OOP), clearing the deck for deeper focus on XML/XSL/XSD and OOP practical work. The creation of a cybersecurity wellness schedule shows intentionality about balancing study, fitness, and security skill‑building. However, the gaps highlight a tendency to learn concepts in isolation—XML/XSL detached from security applications, OOP theory without implementation, scheduling without feedback loops. The non‑obvious connections suggest that stepping back and asking “How could this be used in a security context?” or “What algorithmic pattern does this resemble?” can turn academic exercises into cross‑domain insights. Moving forward, each learning session should include a small “cross‑pollination” step: after learning an XSL template, ask how it could transform a security log; after writing a Python class, consider how its encapsulation could model a security principal. This habit will build a more integrated, versatile skill set.

---
*Generated by weekly‑synthesis cron job on 2026‑04‑26 02:00 SGT.*