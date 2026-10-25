from qb import *

# ---------------- 2022 online (Blackboard) quizzes ----------------
S = "Q22a"
src(S, "Online Quiz A — 2022", "Exams/Quiz/2022/Online Quiz/Image_1–5 2022-11-29.png")
mcq("Q22a-1", 3, 16, "Agile vs standards",
    "The agile community is opposed to the ______ of the standards.",
    ["Continuity", "Best practices", "Attributes", "Bureaucratic overhead"], "d",
    "Quality slide 16: \"The agile community is fundamentally opposed to what it sees as the <b>bureaucratic overheads</b> of standards-based approaches.\"",
    S, "Q1")
mcq("Q22a-2", 1, 8, "TDD and agile",
    "The ______ method embraces Test Driven Development.",
    ["Spiral", "P&amp;D", "Agile", "Waterfall"], "c",
    "TDD comes from <b>agile</b> methods (Extreme Programming): short cycles of test → code → refactor. Intro slide 8 names Agile as the process layer; plan-and-document (P&amp;D) methods such as waterfall test after implementation.",
    S, "Q2")
tf("Q22a-3", 3, "8, 12", "Fitness for purpose",
   "In software quality we focus on fitness for purpose rather than optimizing all quality attributes.", True,
   "Quality slide 8: \"The focus may be 'fitness for purpose' rather than specification conformance\"; slide 12: no system can be optimized for all attributes, so the plan picks the most important ones.",
   S, "Q3")
tf("Q22a-4", 10, "", "SaaS example",
   "Zoom is a SaaS company.", True,
   "Zoom delivers its software as a service: it runs on Zoom's servers and users access it over the Internet by subscription. (SaaS is not on your slides.)",
   S, "Q4")
short("Q22a-5", 3, 11, "Crucial quality attributes for a banking app",
      "You are required to develop a banking application for a bank's customers to use for account and monetary transactions. Pick the <b>two</b> most crucial quality attributes for the developers:<br>Reusability · Security · Adaptability · Usability · Complexity · Testability · Modularity",
      "<b>Security</b> (money and personal data must be protected) and <b>Usability</b> (ordinary customers, not experts, must be able to use it easily).",
      "Quality slide 11 (quality attributes) and slide 12: the quality plan must pick the <i>most important</i> attributes for the specific system. Reusability, modularity, testability etc. are developer-side attributes (slide 8).",
      S, "Q5")

S = "Q22b"
src(S, "Online Quiz B — 2022", "Exams/Quiz/2022/Online Quiz/Image_6–9 2022-11-29.png")
mcq("Q22b-1", 6, "10, 17, 18", "Robot at a fun park",
    "A hacker was able to attack a robot operation via the network. The robot received a huge number of service requests, which caused it to crash under the heavy load. If the purpose of the robot is to entertain children with songs at a fun park, what is the most important requirement for the children that could not be compromised?",
    ["Usability", "Maintainability", "Security", "Testability"], "c",
    "The robot was taken over through the network; if it can be attacked it may behave unpredictably around children. Security slide 10: \"Security is an essential pre-requisite for availability, reliability and <b>safety</b>\"; slide 18: an attack means assumptions about safety may not hold. Of the options, <b>security</b> is the one that protects the children.",
    S, "Q1")
short("Q22b-3", 6, "12, 13", "Match security terms to examples",
      "Match each term with the appropriate example.<br><b>Terms:</b> Control · Attack · Vulnerability · Asset"
      + ol(["Ability to access the system without a username and password", "Sending a virus through an e-mail attachment",
            "Database of sales records", "Scanning a system for viruses periodically"]),
      ol(["<b>Vulnerability</b>", "<b>Attack</b>", "<b>Asset</b>", "<b>Control</b>"]),
      "Security slide 12: vulnerability = a weakness that may be exploited; attack = exploitation of a vulnerability; asset = something of value to protect; control = a protective measure that reduces vulnerability.",
      S, "Q3")
mcq("Q22b-4", 6, 14, "Denial of service",
    "A hacker was able to attack a robot operation via the network. The robot received a huge number of service requests, which placed a load on the robot's system and caused it to crash. What type of attack is this?",
    ["Modification", "Interruption", "Interception", "Fabrication"], "b",
    "Security slide 14: \"<b>Interruption</b> threats allow an attacker to make part of the system unavailable — e.g. a denial of service attack.\"",
    S, "Q4")

# ---------------- 2021 quizzes (Dr Lamees Alhazzaa) ----------------
S = "Q21"
src(S, "Quizzes 1–3 & 6 — 1st Semester 1443 (2021)", "Exams/Quiz/2021/Quizes 1-4/*.pdf, Quizzes1-4-2021.zip, Q6.37x.docx")
short("Q21-1a", 10, "", "SaaS",
      "What does \"SaaS\" stand for? What does it mean?",
      "<b>Software as a Service</b> — the software is hosted by a provider and delivered to users over the Internet (usually through a browser, by subscription) instead of being installed on their own computers.",
      "Quiz 1 model answer. (Not on your slides.)",
      S, "Quiz 1 (sec 372) Q1")
mcq("Q21-1b", 3, 16, "ISO 9001 — process control",
    "According to ISO 9001, inspection and testing come under which management responsibility?",
    ["Process control", "Document control", "Product control"], "a",
    "In ISO 9001, inspection and testing are part of <b>process control</b>. Quiz 1 model answer: process control. (Quality slide 16 mentions ISO 9001 quality processes.)",
    S, "Quiz 1 (sec 372) Q2a")
mcq("Q21-1c", 1, 15, "Who verifies corrections?",
    "Who identifies, documents, and verifies that corrections have been made to the software?",
    ["Project manager", "Project team", "Software Quality Assurance group", "Testing team"], "c",
    "Intro slide 15: the <b>Software QA</b> department improves the organization's quality processes and checks them. Quiz 1 model answer: SQA group.",
    S, "Quiz 1 (sec 372) Q2b")
short("Q21-1d", 3, 4, "Quality management activities",
      "Give two of the main activities provided by quality management.",
      "1) Quality management provides an <b>independent check</b> on the software development process.<br>2) It <b>checks the project deliverables</b> to ensure they are consistent with organisational standards and goals.",
      "Quality slide 4 (quiz model answer).",
      S, "Quiz 1 (sec 373) Q1")
also("M22a-1-1", S, "Quiz 1 (sec 373) Q2a")
mcq("Q21-1f", 10, "", "SaaS advantage",
    "An advantage of using SaaS is:",
    ["Safety of data storage", "Higher privacy of individual's data", "Most suitable for critical systems", "All of the above"], "a",
    "The provider stores and backs up the data professionally (safe storage). Privacy is actually a <i>concern</i> with SaaS (data sits with a third party), and critical systems usually avoid it. Quiz 1 model answer: a.",
    S, "Quiz 1 (sec 373) Q2b")
short("Q21-1g", 10, "", "P&amp;D",
      "What does \"P&amp;D\" stand for? What does it mean?",
      "<b>Plan and Document</b> — a heavyweight process (e.g. waterfall, spiral) where the project is planned up front and every phase produces extensive documentation, as opposed to agile.",
      "Quiz 1 model answer.",
      S, "Quiz 1 (sec 371) Q1")
mcq("Q21-1h", 3, 2, "Benefit of standards",
    "The benefit of standards is that they:",
    ["Are up-to-date", "Provide continuity", "Are usually supported by software tools", "All of the above"], "b",
    "Standards capture best practice and <b>provide continuity</b> — new staff can understand and follow the organisation's practices. Quiz 1 model answer: b.",
    S, "Quiz 1 (sec 371) Q2a")
mcq("Q21-1i", 3, 16, "ISO 9001 is a…",
    "ISO 9001 is a:",
    ["Standard", "Standard framework", "Software measurement", "All of the above"], "b",
    "ISO 9001 is a general <b>framework</b> for quality management systems that organisations instantiate with their own standards and processes. Quiz 1 model answer: b.",
    S, "Quiz 1 (sec 371) Q2b")
mcq("Q21-2a", 4, 15, "CamelCase",
    "A CamelCase identifier is a:",
    ["Pattern", "Code problem", "Variable style", "Documentation style"], "c",
    "Source Code Quality slide 15: \"Use one <b>variable style</b> — either CamelCaseIdentifiers or underscores_identifiers.\"",
    S, "Quiz 2 (sec 371) Q1a")
mcq("Q21-2b", 10, "", "TDD green phase",
    "In TDD, the \"Green\" phase is about:",
    ["How to improve the existing code", "How to make your test fail", "How to make your test pass", "What to develop"], "c",
    "Red = write a failing test; <b>Green = write just enough code to make the test pass</b>; Refactor = improve the code.",
    S, "Quiz 2 (sec 371) Q1b")
short("Q21-2c", 4, "12–14, 19, 26–29", "Evaluate test code",
      "Evaluate the quality of the following code (write two problems):<pre>public void testCompareTo() throws Exception\n{\nWikiPagePath a = PathParser.parse(\"PageA\");\nWikiPagePath ab = PathParser.parse(\"PageA.PageB\");\nWikiPagePath b = PathParser.parse(\"PageB\");\nWikiPagePath aa = PathParser.parse(\"PageA.PageA\");\nWikiPagePath bb = PathParser.parse(\"PageB.PageB\");\nWikiPagePath ba = PathParser.parse(\"PageB.PageA\");\nassertTrue(a.compareTo(a) == 0);    // a == a\nassertTrue(a.compareTo(b) != 0);    // a != b\nassertTrue(ab.compareTo(ab) == 0);  // ab == ab\nassertTrue(a.compareTo(b) == -1);   // a &lt; b\n…</pre>",
      "Problem 1: identifiers are <b>not meaningful</b> (a, ab, b, aa, bb, ba).<br>Problem 2: <b>no vertical alignment</b> (or: the code has no documentation).",
      "Quiz 2 model answer. Source Code Quality slides 12–14 (meaningful names), 19 (vertical alignment), 26–29 (documentation).",
      S, "Quiz 2 (sec 371) Q2")
tf("Q21-2d", 4, 5, "Testing on every change",
   "Code should be tested on every change.", True,
   "Source Code Quality slide 5: \"Code should be tested on every change!\"",
   S, "Quiz 2 (sec 372) Q1a")
tf("Q21-2e", 1, 10, "Cost of changes",
   "Changes before software deployment and release are more expensive than changes after software deployment and release.", False,
   "It is the opposite — the relative cost of correcting defects grows the later they are found (Intro slide 10, Pressman). Source Code Quality slide 7: once in production it is harder to apply fixes.",
   S, "Quiz 2 (sec 372) Q1b")
short("Q21-2f", 10, "", "TDD circle of life",
      "Draw the TDD circle of life.",
      "<pre>   ┌──────────────► RED ───────────────┐\n   │      write a failing test          │\n   │                                    ▼\nREFACTOR ◄──────────────────────── GREEN\n clean up the code          write just enough code\n (tests still pass)          to make the test pass</pre>Repeat the cycle for every small piece of functionality.",
      "TDD (not on your slide decks).",
      S, "Quiz 2 (sec 372) Q2")
short("Q21-2g", 4, "10, 14–18, 24", "Match clean-code terms",
      "Match the term with the expression that describes it the most.<br><b>Terms:</b> a) Refactoring b) DRY c) SRP d) Coherent identifiers e) Coherent code structure"
      + ol(["Avoid code duplications", "Concerned with variable style", "The process of maintaining and improving the existing code", "Implement related data as a data structure"]),
      ol(["<b>b) DRY</b>", "<b>d) Coherent identifiers</b>", "<b>a) Refactoring</b>", "<b>e) Coherent code structure</b>"]),
      "Quiz 2 model answer. Source Code Quality slide 10 (DRY), slide 15 (coherent identifiers = one variable style), slide 18/24 (structure, proper data structures).",
      S, "Quiz 2 (sec 373) Q1")
short("Q21-2h", 4, "17, 18, 26", "Evaluate one-line method",
      "Evaluate the quality of the following code (write two problems):<pre>public static String renderPageWithSetupsAndTeardowns( PageData pageData, boolean isSuite) throws Exception { if (isTestPage(pageData)) includeSetupAndTeardownPages(pageData, isSuite); return pageData.getHtml(); }</pre>",
      "Problem 1: it doesn't use a <b>standard code structure</b> — everything is on one line with no indentation, and the if-statement has no curly brackets.<br>Problem 2: the code has <b>no documentation</b>.",
      "Quiz 2 model answer. Source Code Quality slides 17–18 (indentation, standard structure), 20–23 (be explicit with brackets), 26 (documentation).",
      S, "Quiz 2 (sec 373) Q2")
short("Q21-3a", 5, 7, "Traceability matrix and participating actor",
      "Fill in the blanks:<br>a) ______ is used to check that all requirements are covered by the use cases and to prioritize the work on use cases.<br>b) A(n) ______ is one of the use case's actors but does not initiate it.",
      "a) <b>Traceability matrix</b><br>b) <b>Participating actor</b>",
      "Quiz 3 model answer. OOAD slide 7: a use case is initiated by an actor; other actors participate.",
      S, "Quiz 3 (sec 371) Q1")
short("Q21-3b", 5, 20, "Write a Singleton",
      "Complete the following class to follow the Singleton design pattern:<pre>public final class Singleton {\n\n}</pre>",
      "<pre>public final class Singleton {\n    private static Singleton instance = new Singleton();\n    private Singleton() {}                 // nobody else can create one\n    public static Singleton getInstance() {\n        return instance;                   // global access point\n    }\n}</pre>",
      "Quiz 3 model answer. OOAD slide 20: Singleton restricts creation of more than one object of the class.",
      S, "Quiz 3 (sec 371) Q2")
short("Q21-3c", 10, "", "Types of object responsibilities",
      "List two types of an object's responsibilities.",
      "<b>Knowing</b> responsibility and <b>Doing</b> responsibility.",
      "Quiz 3 model answer. (Not on your slides.)",
      S, "Quiz 3 (sec 372) Q1")
short("Q21-3d", 5, 25, "Match pattern to description",
      "Match the design pattern with its description.<br><b>Patterns:</b> 1 Singleton · 2 Observer · 3 Façade · 4 Strategy · 5 Adapter"
      + ol(["Match interfaces of different classes", "A single class that represents an entire subsystem", "A way of notifying change to a number of classes", "Encapsulates an algorithm inside a class"]),
      ol(["<b>5 Adapter</b>", "<b>3 Façade</b>", "<b>2 Observer</b>", "<b>4 Strategy</b>"]),
      "Quiz 3 model answer. OOAD slide 25 gives the Adapter and Façade definitions word for word.",
      S, "Quiz 3 (sec 372) Q2")
tf("Q21-3e", 5, 13, "Design sequence diagrams",
   "The design sequence diagrams represent interactions of external actors.", True,
   "Official quiz key: True. (Compare Midterm 1 2021: <i>system</i> sequence diagrams do not show internal modules.) OOAD slide 13: sequence diagrams depict the interaction among objects over time.",
   S, "Quiz 3 (sec 373) Q1a")
tf("Q21-3f", 5, "15, 24", "Cohesion and coupling",
   "One of the goals in designing a system is to have low cohesion and high coupling.", False,
   "The goal is the opposite: <b>high cohesion and low coupling</b> (OOAD slide 24: Façade gives low coupling between a subsystem and its clients).",
   S, "Quiz 3 (sec 373) Q1b")
short("Q21-3g", 5, 21, "Adapter class diagram",
      "Draw a class diagram for the Adapter design pattern.",
      "<pre>Client ──uses──▶ «interface» Target\n                    +request()\n                        ▲ implements\n                     Adapter ──adaptee──▶ Adaptee\n                    +request()            +specificRequest()\n                    { adaptee.specificRequest() }</pre>",
      "OOAD slide 21: convert the interface of a class into another interface clients expect.",
      S, "Quiz 3 (sec 373) Q2")
mcq("Q21-6a", 8, "", "White box testing",
    "The testing in which the code is checked is:",
    ["Black box testing", "White box testing", "User acceptance testing", "Release testing"], "b",
    "<b>White-box</b> testing looks inside the code (structure, paths).",
    S, "Quiz 6 (sec 371) Q1a")
mcq("Q21-6b", 8, "", "Cyclomatic complexity",
    "Cyclomatic complexity measures:",
    ["The number of nodes in a CFG", "The number of predicates in a CFG", "The number of partitions of input data", "The number of linearly-independent paths through a program module"], "d",
    "V(G) is the number of <b>linearly independent paths</b> through the program (= predicates + 1), i.e. the size of the basis path set. Quality slide 32 lists it as a static metric of control complexity.",
    S, "Quiz 6 (sec 371) Q1b")
short("Q21-6c", 8, "", "BVA and EP — pizza order",
      "Order Pizza text box: values 1 to 10 are valid (a success message is shown); values 11 to 99 are invalid and an error message appears: \"Only 10 Pizza can be ordered\".<br>a) Identify the equivalence partitions.<br>b) Using Boundary Value Analysis, identify the boundary values.",
      "a) Partitions: <b>invalid ≤ 0</b> · <b>valid 1–10</b> · <b>invalid 11–99</b> (and &gt; 99 if the box allows 3 digits).<br>"
      "b) <b>0, 1, 2, 9, 10, 11</b> (and 98, 99, 100 for the upper limit of the invalid range).",
      "Software testing (no deck in your slides).",
      S, "Quiz 6 (sec 371/373) Q2")
mcq("Q21-6d", 8, "", "BVA is black box",
    "Boundary value analysis belongs to:",
    ["White box testing", "Black box testing", "Regression testing", "Release testing"], "b",
    "BVA is designed from the specification of the inputs, not the code → <b>black box</b> (Final 2021 model answer).",
    S, "Quiz 6 (sec 372) Q1a")
mcq("Q21-6e", 8, "", "Non-functional testing",
    "Which of the following is non-functional testing?",
    ["White box testing", "Black box testing", "Performance testing", "Unit testing"], "c",
    "<b>Performance</b> testing checks a quality attribute (speed/response time), not a function.",
    S, "Quiz 6 (sec 372) Q1b")
short("Q21-6f", 8, "", "Cyclomatic complexity of if/else",
      "What is the cyclomatic complexity of the following code?<pre>A = 10\nIF B &gt; C THEN\n   A = B\nELSE\n   A = C\nENDIF\nPrint A\nPrint B\nPrint C</pre>",
      "One decision (IF) → V(G) = 1 + 1 = <b>2</b>. (Graph: nodes A=10/IF, A=B, A=C, Print → E = 4, N = 4, V = 4 − 4 + 2 = 2.)",
      "Software testing (no deck in your slides).",
      S, "Quiz 6 (sec 372) Q2")
mcq("Q21-6g", 8, "", "Acceptance testing",
    "Acceptance testing is also known as:",
    ["Release testing", "White box testing", "Regression testing", "Beta testing"], "d",
    "Acceptance testing by real customers/users in their environment is called <b>beta testing</b> (alpha = at the developer's site).",
    S, "Quiz 6 (sec 373) Q1a")
mcq("Q21-6h", 8, "", "Debugging",
    "Debugging is:",
    ["Concerned with confirming the presence of faults", "Concerned with locating and repairing these faults",
     "Concerned with locating errors before code execution", "Concerned with integrating components to create a version of the system"], "b",
    "Testing shows the presence of faults; <b>debugging locates and repairs</b> them. Source Code Quality slide 32: runtime errors are found by debugging.",
    S, "Quiz 6 (sec 373) Q1b")
