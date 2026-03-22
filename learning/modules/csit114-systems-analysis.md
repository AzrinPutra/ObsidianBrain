---
title: CSIT114 – Systems Analysis
path: "SIM-UOW / CSIT114 – Systems Analysis"
url: https://www.notion.so/CSIT114-Systems-Analysis-2debd926b4e48050af84e3526a6997b2
created_by: Azrin Putra
last_edited_by: Azrin Putra
last_edited_time: 2026-02-13T03:25:00.000Z
---

# CSIT114 – Systems Analysis
M - Models
M - Methodology
T - Tools
T - Techniques

Information System Components
(Using Mrt as an example)
People:
- Commuters
- Management Staff (ie. Operations manager)
- Security
Processes:
- Communications between trains and control rooms
- Access gates
Software:
- Software for card reader

### Week 1 - Introduction to System Analysis
___
### 🎯 What is System Analysis?
**System Analysis** is the set of activities that enable us to:
> Understand and specify what an information system should accomplish
📌 It focuses on **business needs**, **user requirements**, and **problem understanding**
📌 It comes **before system design**, which focuses on **how** the system will work
___
### 🧠 Why System Analysis Matters
Many IT projects fail not because of poor coding, but because:
- The **wrong problem** was solved
- User needs were **misunderstood**
- Requirements were **unclear or incomplete**
💡 Good system analysis:
- Reduces rework
- Improves project success rate
- Aligns IT systems with business goals
___
### 🧩 Information System vs Computer Application
#### 💻 Computer Application
- A software program
- Performs specific functions
- Narrow scope
**Example:** Calculator app
#### 🗂️ Information System
- A **set of interrelated components**
- Includes:
	- People
	- Processes
	- Data
	- Software
	- Hardware
- Supports **business operations**
**Example:** Sales Order Processing System
📌 **Key exam idea:**
> An information system is broader than just software.
___
### 🧱 Components of an Information System
An information system consists of:
- 👥 **People** – users, managers, analysts
- 🔁 **Processes** – workflows and procedures
- 🗃️ **Data** – stored and processed information
- 💾 **Software** – applications and programs
- 🖥️ **Hardware** – servers, computers, networks
___
### 🔄 System Analysis vs System Design

|Aspect|System Analysis|System Design|
|---|---|---|
|Focus|What the system should do|How the system will do it|
|Goal|Understand the problem|Build the solution|
|Output|Requirements, models|Architecture, detailed design|
📌 **Common exam question**
___
### 🔁 System Development Life Cycle (SDLC)
The **SDLC** is the overall process used to build and maintain information systems.
#### 🛠️ Six Core SDLC Processes
1. **Identify the problem & obtain approval**
2. **Plan and monitor the project**
3. **Discover & specify requirements**
4. **Design the system**
5. **Build, test & integrate**
6. **Deploy and maintain**
📌 System analysis mainly happens in **Steps 1–3**
___
### 🔄 Agile & Iterative Development
#### ⚡ Agile Development
- Emphasises flexibility
- Welcomes changing requirements
- Frequent user feedback
#### 🔁 Iterative Development
- System is built in **small increments**
- Each iteration improves or extends the system
📌 Modern systems development uses **Agile + Iterative SDLC**
___
### 👥 Stakeholders in System Analysis
**Stakeholders** are individuals or groups who have an interest in the system.
#### Types of Stakeholders
- **Users** – use the system daily
- **Managers** – make decisions using system outputs
- **Clients/Sponsors** – fund the project
- **System Analysts** – gather & model requirements
- **Developers** – build the system
- **External parties** – regulators, vendors
📌 Stakeholders are the **primary source of requirements**
___
### 🧠 What Does a System Analyst Do?
A system analyst:
- Understands business problems
- Identifies system requirements
- Models processes, data, and interactions
- Acts as a bridge between **business and technical teams**
📌 Key skills:
- Communication
- Critical thinking
- Modelling
- Problem solving
___
### 🧩 Core Concepts You Must Know (Week 1)
- Stakeholders
- Information systems
- SDLC
- System analysis vs design
- Processes
- Work Breakdown Structure (WBS)
- Use cases
- Activity diagrams
- Class (domain) diagrams
___
### 🔁 Processes Explained
A **process** is:
> A sequence of activities with a beginning, an end, inputs, and outputs
Processes:
- Use the information system
- Develop the information system
- Are interrelated
___
### 🗂️ Example: Sales Order (Order-to-Cash)
Typical business process flow:
7. Sales order entry
8. Check availability
9. Pick & pack materials
10. Ship goods
11. Invoice customer
12. Receive payment
📌 Used to demonstrate **process modelling**
___
### 📌 Key Takeaways (Exam-Focused)
- System analysis defines **what**, not **how**
- Information systems include **people + processes + technology**
- SDLC provides a structured approach
- Stakeholders are critical to requirement accuracy
- Agile & iterative development are industry standards
___
### 📝 Self-Check Questions
- What is the difference between system analysis and system design?
- Why do IT projects fail despite good developers?
- What components make up an information system?
- Why are stakeholders important?
- How does Agile SDLC differ from traditional approaches?
### Week 2: System Investigation & Project Management
___
### 🎯 Week 2 Learning Outcomes
By the end of this week, I should be able to:
- Explain **what systems analysis is**
- Differentiate **functional vs non-functional requirements**
- Identify **stakeholders** and analyze their influence
- Understand **project management’s role** in systems analysis
- Describe **Core Process 1 & 2** in the SDLC
- Explain **cost/benefit analysis, feasibility & risk**
___
### 🧠 Big Picture (How This Fits in the Course)
> Systems Analysis is about understanding the problem before building the solution.
**Focus of Week 2:**
- Discovering business needs
- Justifying projects
- Planning before development starts
___
### 🔍 What Is Systems Analysis?
**Systems Analysis** involves:
- Understanding the **business problem**
- Gathering and defining **requirements**
- Communicating findings using **models**
- Supporting decision-making before design & coding
🔑 Key idea:
> “Systems analysis activities involve discovery and understanding.”
___
### 📌 Systems Analysis Activities
#### Core Activities
- Gather detailed information
- Define requirements
- Prioritize requirements
- Develop user-interface dialogs
- Evaluate requirements with users
#### Information Gathering Methods
- Interviews
- Surveys / questionnaires
- Document analysis
- Observation of business processes
- Research (vendors, systems, best practices)
___
### 🧩 Requirements Explained
#### What Are System Requirements?
System requirements describe **what the system must do** and **how well it must do it**.
___
#### ✅ Functional Requirements
- **What the system does**
- Business processes & user actions
- Often documented using **use cases**
📌 Example:
> “The system must allow customers to place online orders.”
___
#### ⚙️ Non-Functional Requirements
- **How the system performs**
- Constraints, quality attributes, limits
📌 Example:
> “The system must process payments within 3 seconds.”
___
#### 🧠 FURPS+ Framework (Very Exam-Important)
Use this to classify non-functional requirements:

|Letter|Meaning|
|---|---|
|F|Functional|
|U|Usability|
|R|Reliability|
|P|Performance|
|S|Security|
|+|Other constraints (legal, design, hardware, etc.)|
___
### 📊 Models & Modeling
#### What Is a Model?
A **model** is a simplified representation of part of the system.
#### Types of Models
- **Textual** – written descriptions
- **Graphical** – diagrams (UML)
- **Mathematical** – formulas, algorithms
#### Why We Model
- Reduce complexity
- Improve communication
- Capture requirements clearly
- Document decisions for future maintenance
___
### 👥 Stakeholders
#### Who Are Stakeholders?
Anyone who has an **interest in the system’s success**.
> Stakeholders are the primary source of requirements.
___
#### Types of Stakeholders

|Type|Description|
|---|---|
|Internal|Within the organisation|
|External|Outside the organisation|
|Operational|Daily system users|
|Executive|Decision-makers & sponsors|
___
#### Stakeholder Analysis Matrix
Stakeholders are analysed by:
- **Interest**
- **Power / Influence**

|Strategy|When to Use|
|---|---|
|Manage closely|High power, high interest|
|Keep satisfied|High power, low interest|
|Keep informed|Low power, high interest|
|Monitor|Low power, low interest|
___
### 🧑‍💼 Project Management Basics
#### What Is Project Management?
> Organising and directing people to achieve results on time, within budget, and within scope.
___
#### Why Projects Fail (Common Reasons)
- Unclear business needs
- Poor project management practices
- Inadequate user involvement
- Weak executive support
- Inexperienced project managers
📌 **Key insight:**
Projects usually fail due to **management issues**, not technical skills.
___
### 🦸 Role of the Project Manager
#### Internal Responsibilities
- Develop schedules
- Assign tasks
- Manage risks
- Monitor deliverables
#### External Responsibilities
- Report progress
- Communicate with stakeholders
- Secure resources
___
### 🔁 SDLC Core Processes (Week 2 Focus)
___
#### 🟢 Core Process 1: Identify the Problem & Obtain Approval
#### Activities:
13. Identify the problem or opportunity
14. Define system vision
15. Quantify approval factors
16. Analyze risk & feasibility
17. Obtain formal approval
___
#### 📄 System Vision Document
Includes:
- Problem description
- System capabilities
- Business benefits (tangible & intangible)
___
#### 💰 Cost / Benefit Analysis
Key concepts:
- Tangible vs intangible benefits
- Net Present Value (NPV)
- Break-even point
- Payback period
___
#### ⚠️ Risk & Feasibility Types

|Type|Focus|
|---|---|
|Organizational|Culture & impact|
|Technical|Skills & technology|
|Resource|People & tools|
|Schedule|Time constraints|
___
#### 🔵 Core Process 2: Plan & Monitor the Project
#### Activities:
18. Establish project environment
19. Schedule work
20. Allocate staff & resources
21. Evaluate processes
22. Monitor progress & adjust
___
### 📅 Scheduling the Work
#### Key Tools
- Work Breakdown Structure (WBS)
- Task dependencies
- Critical Path
- Gantt Chart
📌 Rule of thumb:
> Tasks should be 1–5 working days long.
___
### 🔄 Continuous Improvement
#### Retrospective Questions
- What worked well?
- What caused delays?
- Were communication processes effective?
- How can we improve next iteration?
___
### 🧠 Exam & Assignment Tips
- Always link **requirements → stakeholders → business value**
- Use **FURPS+** for non-functional requirements
- Mention **System Vision Document** when discussing approval
- For project questions, structure answers using **Core Process 1 & 2**
___
### 📍 Weekly Reflection (Recommended Notion Block)
> What I understood well this week:
**What I need to revisit:**
**Questions to ask in tutorial:**

## Week 3 - System Modelling
### 🔹 Use Case Modeling – Notion Study Guide
___
### 🧠 Topic Overview
**System Modeling 1 focuses on defining functional requirements using Use Cases.**
> Use cases answer the question:
**“What does the system do for its users?”**
They are the **foundation** for:
- Functional requirements
- System design
- Later UML diagrams (SSD, DCD, etc.)
___
### 🎯 Learning Objectives (Know These for Exams)
You should be able to:
- Explain **why use cases are key to functional requirements**
- Identify use cases using:
	- **User Goal Technique**
	- **Event Decomposition Technique**
- Apply the **CRUD technique** to validate use cases
- Understand and draw **Use Case Diagrams**
- Draw use case diagrams:
	- By **actor**
	- By **subsystem**
___
### 📌 What Is a Use Case?
**Definition**
A **use case** is:
> An activity the system performs in response to a request by a user or event.
#### Key Characteristics
- Represents **functional requirements**
- Describes **what** the system does (not how)
- Named using **Verb–Noun**
	- Example: `Create Order`, `Track Shipment`, `Update Customer Details`
___
### 🧩 Use Case Models
There are **two types** of models used:
#### 1️⃣ Use Case Description (Textual)
- Short written description
- Often **one sentence**
- Explains the main goal of the use case
📌 Example:
> Customer places an order by selecting products and confirming payment.
___
#### 2️⃣ Use Case Diagram (Graphical – UML)
Shows:
- Actors
- Use cases
- System boundary
- Relationships
___
### 👤 Actors
- **Actor** = an external user or system interacting with the system
- Can be:
	- Human (Customer, Staff)
	- External system (Payment Gateway)
⚠️ Actors are **outside** the system boundary
___
### 🔍 Identifying Use Cases – 3 Techniques
___
### ① User Goal Technique (Most Common in Industry)
#### Core Idea
> Identify what goals users want to achieve using the system.
#### Steps
23. Identify all potential users
24. Classify users by:
	- Functional role (sales, shipping, admin)
	- Organizational level (operational, management, executive)
25. Interview users
26. Ask:
**“What tasks do you want the system to help you do?”**
27. Turn tasks into **user goals**
28. Convert goals into **use cases**
29. Remove duplicates
30. Review with users and stakeholders
📌 Example Goals → Use Cases
- “I need to ship items” → `Ship Items`
- “I need to track orders” → `Track Shipment`
___
### ② Event Decomposition Technique (More Complete)
#### Core Idea
> Identify events that occur and require the system to respond.
#### Definition: Event
An **event**:
- Occurs at a specific time/place
- Is meaningful to the business
- Requires system response
- Should be remembered by the system
___
#### Types of Events
#### 🔹 External Events
Triggered by outside actors
- Customer places order
- Customer updates address
- Manager requests report
#### 🔹 Temporal Events
Triggered by time
- Daily sales report
- Monthly payroll
- End-of-day processing
#### 🔹 State Events
Triggered by system state change
- Inventory reaches reorder level
- Account becomes overdue
___
#### Event Decomposition Steps
31. Identify **external events**
32. Define a use case for each
33. Identify **temporal events**
34. Define time-triggered use cases
35. Identify **state events**
36. Define use cases for state changes
37. Apply **Perfect Technology Assumption**
___
### 🧠 Perfect Technology Assumption (IMPORTANT)
When identifying use cases:
- ❌ Do NOT include:
	- Login
	- Logout
	- Backup
	- Password change
- ✅ Focus only on **business-required functionality**
- System controls are added later during design
___
### ③ CRUD Technique (Validation Tool)
CRUD =
**Create – Read – Update – Delete**
⚠️ CRUD is **NOT** for discovering use cases
✔️ It is used to **check completeness**
___
#### CRUD Steps
38. Identify all **domain classes** (data entities)
39. For each domain class, check:
	- Is there a use case to **Create** it?
	- **Read/Report** it?
	- **Update** it?
	- **Delete/Archive** it?
40. If missing → add use case
41. Clarify which system owns the data (for integrated systems)
📌 Often shown as a **Use Case vs Domain Class matrix**
___
### 🖼️ Use Case Diagram (UML)
#### Purpose
- Visually shows system functionality
- Helps communicate with stakeholders
___
#### Key Components
- **Actors** (stick figures)
- **Use Cases** (ovals)
- **System Boundary**
- **Relationships**
___
#### <<includes>> Relationship
- One use case always uses another
- Arrow points **to the included use case**
- Similar to a subroutine
📌 Example:
- `Place Order` <<includes>> `Process Payment`
___
### 🛠️ Drawing Use Case Diagrams – Best Practices
42. Identify stakeholders
43. Decide what each stakeholder needs to see
44. Draw diagrams:
	- By actor (e.g., Customer)
	- By subsystem
45. Name diagrams clearly
46. Use diagrams for **review and validation**
___
### 🧠 Exam & Assignment Tips
- Always name use cases using **Verb–Noun**
- Be able to:
	- Explain **why use cases define functional requirements**
	- Compare **User Goal vs Event Decomposition**
- Remember:
	- CRUD = validation
	- Use cases = WHAT, not HOW
- Do **not** include system controls as use cases
___
### 🧾 One-Page Mental Summary
- Use cases = system functions
- Identified via:
	- User goals
	- Events
- Validated via:
	- CRUD
- Represented via:
	- Use case descriptions
	- Use case diagrams

## Week 4 System Analysis – Deep Dive into System Modelling
> Mentor mindset: Think like a systems analyst. Modelling is not about drawing diagrams for marks — it is about thinking clearly, communicating unambiguously, and reducing risk before anything is built.
___
### 1. Why Modelling Matters (Big Picture)
#### What is a Model?
A **model** is an abstraction of reality that:
- Captures *important* properties of a system
- Suppresses irrelevant detail
- Focuses on what matters for a specific purpose
📌 **Key idea**: A model is *not* the real thing — it is a thinking and communication tool.
#### Why Systems Analysts Use Models
Models allow us to:
- Predict system behaviour
- Explore alternatives cheaply
- Communicate with stakeholders
- Validate requirements early
- Reduce development and testing risk
> 💡 Rule of thumb: If a requirement is complex, it must be modelled.
___
### 2. UML as a Modelling Language
#### What is UML?
**UML (Unified Modeling Language)** is the standard visual language for modelling software systems.
Think of UML like:
- **Blueprints** for buildings
- **Circuit diagrams** for electronics
- **Maps** for navigation
It provides a **shared vocabulary** between:
- Business users
- Systems analysts
- Designers
- Developers
___
### 3. The 3 Core Perspectives of Modelling

|Perspective|Question Answered|Typical Diagrams|
|---|---|---|
|Functional|What must the system do?|Use Case, Activity|
|Structural|What is the system made of?|Class, Object|
|Behavioural|How does the system behave over time?|Sequence, State Machine|
> 🎯 This lecture focuses heavily on behavioural modelling.
___
### 4. Use Case Modelling (Foundation)
#### Use Case Diagrams
- Show **what** the system does
- External, user-focused view
- No internal logic
**Elements**:
- Actor (who interacts)
- Use Case (goal)
- System boundary
#### Use Case Descriptions (Textual Models)
#### Levels of Detail
47. **Brief** – summary only
48. **Intermediate** – main flow
49. **Fully Developed** – complete behavioural specification
#### Fully Developed Use Case Template
- Use case name (verb–noun)
- Actors
- Triggering event
- Preconditions
- Postconditions
- Flow of activities
- Exception conditions
- Stakeholders
- Related use cases (<>)
📌 **Exam tip**: Preconditions & postconditions are critical for **test case design**.
___
### 5. Activity Diagrams (Flow Modelling)
#### Purpose
- Show **workflow logic**
- Sequence of activities
- Decision points
- Parallel processing
#### Key Symbols
- Rounded rectangle → activity
- Diamond → decision/merge
- Solid bar → fork/join (parallel)
- Swimlanes → responsibility
#### When to Use
- Complex business logic
- Multi-actor workflows
- Use cases with many decision paths
> 🧠 Difference from State Machine:
- Activity = *what happens next*
- State = *what condition the object is in*
___
### 6. System Sequence Diagrams (SSD)
#### What is an SSD?
A **System Sequence Diagram**:
- Shows interactions between **actor and system**
- Treats the system as a **black box**
- Focuses on *input/output messages*
#### SSD Characteristics
- One actor
- One system object (:System)
- Messages are **system operations**
#### Message Notation
- Verb–noun naming
- Parameters included
- Return values shown
#### Control Frames
- **Loop** – repetition
- **Alt** – if/else
- **Opt** – optional
📌 **SSD = contract between user and system**
___
### 7. Finite State Machines (FSM)
#### What is a State?
A **state** is a condition where an object:
- Satisfies a criterion
- Performs an action
- Waits for an event
#### FSM Components
- States
- Transitions
- Events
- Guard conditions
- Actions
#### Why FSMs Matter
FSMs model **object lifecycle behaviour**, not workflows.
Examples:
- ATM card states
- Order processing states
- Printer modes
- Lift operation
___
### 8. State Machine Diagrams (Deep Dive)
#### Core Elements

|Element|Meaning|
|---|---|
|Initial state|Start point (black dot)|
|State|Rounded rectangle|
|Transition|Arrow|
|Guard|[condition]|
|Action|/action|
|Final state|Termination|
#### Transition Syntax
Event [Guard] / Action
___
### 9. Composite & Concurrent States
#### Composite States
- State containing sub-states
- Used to manage complexity
Example:
- Printer ON
	- Idle
	- Working
#### Concurrent States
- Parallel behaviours
- Independent state paths
📌 Use when objects do **multiple things at once**.
___
### 10. Developing a State Machine Diagram (Step-by-Step)
50. Identify classes with lifecycle behaviour
51. List all possible states
52. Identify transitions
53. Sequence states logically
54. Identify composite states
55. Look for concurrent paths
56. Add events, guards, actions
57. Validate against lifecycle
#### Validation Checklist
- All states reachable?
- All exceptions handled?
- Real states (not actions)?
- Clear start and end?
___
### 11. Integrating Models (Systems Thinking)
#### How Models Work Together

|Model|Role|
|---|---|
|Use Case|Scope & goals|
|Activity|Workflow logic|
|SSD|System interface|
|State Machine|Object behaviour|
|Class Diagram|Structure|
> 🎯 Golden Rule: No model stands alone.
___
### 12. Analysis vs Design (Critical Distinction)

|Analysis|Design|
|---|---|
|What is needed|How it will be built|
|Business-focused|Technology-focused|
|Logical models|Physical models|
State machines sit at the **boundary** — logical behaviour, but implementation-aware.
___
### 13. Common Modelling Mistakes (Exam Gold)
❌ Confusing activity diagrams with state diagrams
❌ Modelling UI screens instead of system behaviour
❌ Using actions as states
❌ Over-modelling simple use cases
❌ Missing exception paths
___
### 14. How to Think Like a High-Scoring Student
Ask yourself:
- *What problem does this diagram solve?*
- *Who is this diagram for?*
- *What risk does this model reduce?*
> 🧠 Modelling is structured thinking, not drawing.
___
### 15. Exam Strategy Summary
- Always state **assumptions**
- Use correct UML notation
- Prefer clarity over completeness
- Justify model choice
- Be consistent across diagrams

## Focus: UML Diagrams
## **Use Case Diagram**
**Purpose:**
- Shows **what the system does from a user perspective**
- Highlights **actors (users/external systems)** and **their goals (use cases)**
- Answers: *“What services/functions are provided?”*
**Key Elements:**

|Element|Symbol / Notation|Notes|
|---|---|---|
|Actor|Stick figure|External user/system|
|Use Case|Oval|Verb + Noun, goal-focused (e.g., `Purchase Ticket`)|
|System Boundary|Rectangle|Groups all use cases inside the system|
|Association|Line|Actor ↔ Use Case|
|<<include>>|Stereotype on line|Mandatory sub-step (always happens)|
|<<extend>>|Stereotype on line|Optional behaviour|
**Best Practices:**
- Name use cases as **Verb + Noun**: `Select Seat`, `Make Payment`
- Connect actors **only to use cases they initiate**
- Use <<include>> for mandatory steps, <<extend>> for optional paths (e.g., discounts, cancel)
- Keep system boundary clear
**Common Mistakes:**
- Including internal components (DB, UI) as actors ❌
- Using actions instead of goals as use cases ❌
- Connecting actors to everything ❌

**MTM Example (Use Case):**
### Actors
```plain text
Customer
Staff
Payment System
```
### Use Cases
```sql
Search Movie
Select Showtime
Select Seat
Purchase Ticket
Make Payment
Apply Discount
Verify Discount
```
### Relationships (write beside connectors)
```sql
Customer — Purchase Ticket
Customer — Search Movie
Customer — Select Showtime
Customer — Select Seat

Purchase Ticket <<include>> Make Payment

Apply Discount <<extend>> Purchase Ticket
Verify Discount <<include>> Apply Discount

Payment System — Make Payment
Staff — Verify Discount

```
## **Activity Diagram**
**Purpose:**
- Models **workflow or process**, step by step
- Shows **sequence, branching, parallel activities**
- Answers: *“How does the process happen?”*
**Key Elements:**

|Element|Symbol|Notes|
|---|---|---|
|Initial Node|Filled circle ●|Start of workflow|
|Action|Rounded rectangle|Observable step, not goal|
|Decision / Branch|Diamond|Conditional paths, guards `[condition]`|
|Merge|Diamond|Merge alternative paths|
|Fork / Join|Thick bar|Parallel activities|
|Final Node|Bullseye|Workflow end|
|Swimlane|Vertical column|Actor / subsystem responsibility|
|Control Flow|Arrow|Sequence of actions|
|Object Flow|Arrow with object|Shows data passing between actions|
**Best Practices:**
- Start with **trigger**: `Ticket Machine: Show Movies`
- Alternate swimlanes: Actor → System → Actor → System
- Use diamonds for decisions: `[cash]`, `[credit]`, `[discounted]`
- Fork/join for concurrent actions: ticket printing + confirmation email
**Common Mistakes:**
- Starting with goals like `Purchase Ticket` ❌
- Mixing abstraction in swimlanes ❌
- Skipping start or end nodes ❌
- Using UI buttons as actions ❌

**MTM Activity Example:**
### Swimlanes
Search Movie
Select Showtime
Select Seat
Purchase Ticket
Make Payment
Apply Discount
Verify Discount
```plain text
Customer | Ticket Machine | Staff | Payment Gateway
```
### Flow (write inside actions exactly like this)
```yaml
● Start

Ticket Machine: Display Movies
Customer: Select Movie
Ticket Machine: Display Showtimes
Customer: Select Showtime
Ticket Machine: Display Seats
Customer: Select Seat

Customer: Choose Ticket Type

◇ [discount selected]
    Staff: Verify Discount
    ◇ [valid] → continue
    ◇ [invalid] → Ticket Machine: Display Error

Ticket Machine: Request Payment Method

◇ [credit]
    Customer: Insert Card
    Ticket Machine: Send Authorization Request
    Payment Gateway: Authorize Payment

◇ [cash]
    Customer: Insert Cash
    Ticket Machine: Validate Amount

Ticket Machine: Print Ticket
◎ End
```
___
## **Sequence Diagram**
**Purpose:**
- Shows **interaction between actors and system components over time**
- Answers: *“Who communicates with whom, in what order?”*
**Key Elements:**

|Element|Notation|Notes|
|---|---|---|
|Lifeline|Vertical dashed line|Actor or object|
|Message|Horizontal arrow|Actor → System: action(parameters)|
|Activation / Execution|Thin rectangle on lifeline|Shows active processing|
|Combined Fragment|Rectangle with label `alt`, `loop`|For conditional or repeated flows|
**Best Practices:**
- Identify **actors and system components**
- Messages = **events/actions**, not UI clicks
- Show alternative paths using `alt` fragment (e.g., cash vs credit)
- Use **single scenario per diagram** (one flow of events)
**Common Mistakes:**
- Including internal objects when it’s an SSD ❌
- Mixing sequence with activity flow logic ❌
- Omitting message order ❌

**MTM SSD Example (Discount Ticket, Credit Payment):**
### Lifelines
```plain text
Customer | MTM | Staff | Payment Gateway
```
### Messages (write exactly beside arrows)
```yaml
Customer → MTM: startSession()

MTM → Customer: displayMovies()

Customer → MTM: selectMovie(movieID)
MTM → Customer: displayShowtimes()

Customer → MTM: selectShowtime(showtimeID)
MTM → Customer: displaySeats()

Customer → MTM: selectSeat(seatNo)
Customer → MTM: chooseDiscount(type)

MTM → Staff: verifyDiscount(customerID)
Staff → MTM: verificationResult(valid)

Customer → MTM: payByCredit(cardInfo)
MTM → Payment Gateway: authorizePayment(amount)
Payment Gateway → MTM: paymentApproved

MTM → Customer: printTicket(ticketInfo)

```
#### Alternative Fragment (write above frame)
Alternative payment paths (cash vs credit) can be shown using `alt` fragments.
```scss
alt Payment Method

[credit]
    payByCredit(cardInfo)

[cash]
    insertCash(amount)

```
___
## **4️⃣ State Machine Diagram**
**Purpose:**
- Shows **system behaviour or modes over time**
- Tracks **states and transitions** caused by events
- Answers: *“What is the system doing at any moment?”*
**Key Elements:**

|Element|Symbol|Notes|
|---|---|---|
|State|Rounded rectangle|Mode or behaviour (e.g., Idle, MovingUp)|
|Initial|Filled circle ●|Start state|
|Final|Bullseye|End state|
|Transition|Arrow|State change triggered by event/guard/action|
|Guard|`[condition]`|Transition only if condition is true|
|Action on Transition|`/action()`|Optional effect of transition|
**Best Practices:**
- States = **behaviours**, not data values (floors = data, not state)
- Transitions triggered by **events**
- Include **guards** and optional **actions**
**Common Mistakes:**
- Using data as states ❌ (`Level 5`)
- Omitting guards ❌
- Starting at abstract goals instead of initial system state ❌

**MTM State Machine Example (Simplified):**
### States
```sql
Idle
Selecting Movie
Selecting Showtime
Selecting Seat
Selecting Ticket Type
Awaiting Verification
Selecting Payment Method
Processing Payment
Printing Ticket
Out Of Service
```
### Transitions (write on arrows)
```yaml
● → Idle

Idle → Selecting Movie : screenTouched

Selecting Movie → Selecting Showtime : movieSelected
Selecting Showtime → Selecting Seat : showtimeSelected
Selecting Seat → Selecting Ticket Type : seatConfirmed

Selecting Ticket Type → Awaiting Verification : discountSelected
Awaiting Verification → Selecting Payment Method : verificationPassed
Awaiting Verification → Selecting Ticket Type : verificationFailed

Selecting Ticket Type → Selecting Payment Method : ticketTypeConfirmed

Selecting Payment Method → Processing Payment : cardTapped
Selecting Payment Method → Processing Payment : cashInserted

Processing Payment → Printing Ticket : paymentApproved
Processing Payment → Selecting Payment Method : paymentRejected

Printing Ticket → Idle : ticketPrinted

```

Discount verification can be modeled as **branch in PaymentProcessing** with guards.
___
## **5️⃣ Domain / Class Diagram**
**Purpose:**
- Shows **static structure of system**
- Models **classes, attributes, operations, and relationships**
- Answers: *“What objects exist and how are they related?”*
**Key Elements:**

|Element|Notation|Notes|
|---|---|---|
|Class|Rectangle (three compartments)|Name / Attributes / Operations|
|Association|Line|Relationship between classes|
|Multiplicity|`0..1`, `1..*`|How many instances|
|Inheritance|Triangle arrow|Generalisation / Specialisation|
|Aggregation|Hollow diamond|Whole-part relationship|
|Composition|Filled diamond|Strong ownership|
**Best Practices:**
- Use **meaningful class names** (noun)
- Attributes = data / properties
- Operations = functions / methods
- Keep diagram focused: classes relevant to system behaviour
**MTM Domain Class Example:**
```plain text
+------------------+
| Movie            |
+------------------+
| title            |
| duration         |
| rating           |
+------------------+
| getShowtimes()   |
+------------------+

+------------------+
| Ticket           |
+------------------+
| seatNumber       |
| price            |
| discountApplied  |
+------------------+
| printTicket()    |
+------------------+

+------------------+
| Customer         |
+------------------+
|name             |
| idNumber         |
+------------------+
| selectSeat()     |
| makePayment()    |
+------------------+

+------------------+
| Payment          |
+------------------+
| amount           |
| paymentType      |
+------------------+
| authorize()      |
+------------------+
```
Relationships:
- Customer 1..* → Ticket
- Ticket 1 → Movie
- Payment 1 → Ticket
___
## **6️⃣ Summary Table: When to Use Each Diagram**

|Diagram|Focus|Key Tip|
|---|---|---|
|Use Case|What system does (goals)|Actors → Goals|
|Activity|How process flows|Actions, decisions, swimlanes|
|Sequence|Who talks to who & order|Messages over time, alt/loop|
|State Machine|System modes & transitions|States = behaviours, not data|
|Domain / Class|Static structure|Nouns: classes, attributes, associations|