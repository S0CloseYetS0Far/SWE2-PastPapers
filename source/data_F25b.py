from qb import *

S = "F25b"
src(S, "Final — 2nd Semester 2025", "Exams/Final/2025/Final_2nd_2025.pdf  +  solved copy: Exams/Final/2025/Final_2nd_2025_sol.pdf")

TF = [
    (1, 2, 10, "In the risk management process, risk identification is concerned with assessing the likelihood and consequences of these risks.", False,
     "Slide 10: that is <b>risk analysis</b> (\"Assess the likelihood and consequences of these risks\"). Risk identification only identifies project, product and business risks."),
    (2, 2, 3, "Project management is needed because software development is always subject to budget and schedule constraints.", True,
     "Slide 3: \"Project management is needed because software development is always subject to budget and schedule constraints that are set by the organisation.\""),
    (3, 3, 29, "Dynamic metrics help assess efficiency and reliability while static metrics are collected by measurements made of the system representations.", True,
     "Slide 29: static metrics are collected from system representations; \"Dynamic metrics help assess efficiency and reliability.\""),
    (4, 3, 16, "Quality management in agile development is informal rather than document-based.", True,
     "Slide 16: \"Quality management in agile development is informal rather than document-based.\""),
    (5, 3, "29, 32", "Cyclomatic complexity is an example of dynamic software product metrics.", False,
     "Slide 32 lists cyclomatic complexity under <b>static</b> software product metrics (it is measured from the code, not from the running program)."),
    (6, 4, 8, "Code review really has two main purposes: improving the code and improving the programmer.", True,
     "Source Code Quality slide 8: \"Code review really has two purposes: Improving the code. Improving the programmer.\""),
    (7, 2, 17, "In risk planning, avoidance strategies mean the probability that the risk will arise is reduced.", True,
     "Slide 17: \"Avoidance strategies — the probability that the risk will arise is reduced.\""),
    (8, 2, 24, "An important role of a manager is to motivate the people working on a project.", True,
     "Slide 24: \"An important role of a manager is to motivate the people working on a project.\""),
]
for n, ch, sl, q, a, e in TF:
    tf("F25b-1-%d" % n, ch, sl, "Project & quality management T/F", q, a, e, S, "Q1.%d" % n, 1)

mcq("F25b-2-1", 7, 8, "Reliability definition",
    "__________ : The probability that the system will correctly deliver services as expected by users.",
    ["Reliability", "Availability", "Security", "Robustness"], "a",
    "Dependability slide 8: \"<b>Reliability</b> — the probability that the system will correctly deliver services as expected by users.\" Availability is the probability the system is up and running.",
    S, "Q2.1", 2)
mcq("F25b-2-2", 3, 3, "Quality plan contents",
    "What should a quality plan include?",
    ["The company's marketing strategy", "Quality goals for the project and the standards to be used",
     "A list of competitors in the market", "The software's user interface design"], "b",
    "Quality slide 3: \"The quality plan should set out the quality goals for the project and define what processes and standards are to be used.\" Slide 7 lists the structure: product introduction, product plans, process descriptions, quality goals, risks.",
    S, "Q2.2", 2)
mcq("F25b-2-3", 6, 12, "Security terminology — threat",
    "__________ means circumstances that have potential to cause loss or harm.",
    ["Attack", "Control", "Threat", "Vulnerability"], "c",
    "Security slide 12: \"<b>Threat</b> — circumstances that have potential to cause loss or harm.\"",
    S, "Q2.3", 2)
mcq("F25b-2-4", 6, 6, "Protection levels",
    "__________ : Protection that is invoked when access to specific information is requested.",
    ["Platform-level", "Record-level", "Application-level", "All of the above"], "b",
    "Slide 6 (system layers where security may be compromised) comes from Sommerville ch. 13, which defines three protection levels: platform-level (the OS/platform), application-level (built into the application), and <b>record-level — protection invoked when access to specific information is requested</b>. <i>Note: the solved copy circled D, but only record-level matches this definition.</i>",
    S, "Q2.4", 2)
mcq("F25b-2-5", 3, "8, 9", "Fitness for purpose",
    "What is the main focus of software 'fitness for purpose'?",
    ["Conforming strictly to specification", "Reducing project costs",
     "Meeting the practical needs and expectations of users", "Simplifying code structures"], "c",
    "Quality slide 8: \"The focus may be 'fitness for purpose' <b>rather than specification conformance</b>.\" Slide 9 lists the questions: tested? dependable? acceptable performance? usable? — i.e. does it meet users' practical needs.",
    S, "Q2.5", 2)
mcq("F25b-2-6", 3, "18, 19", "Pair programming benefit",
    "What is one of the key benefits of pair programming in agile development?",
    ["It eliminates the need for testing", "It ensures constant code review by another team member",
     "It reduces the time needed for coding by 50%", "It guarantees perfect code without errors"], "b",
    "Quality slide 18: \"In Extreme Programming, pair programming ensures that code is constantly being examined and reviewed by another team member.\"",
    S, "Q2.6", 2)
mcq("F25b-2-7", 7, 15, "Types of system failure",
    "__________ happens when the system does not deliver a service correctly to users.",
    ["Loss of service", "Incorrect service delivery", "System/data corruption", "Human error"], "b",
    "Dependability slide 15: \"<b>Incorrect service delivery</b> — the system does not deliver a service correctly to users.\" Loss of service = system unavailable; data corruption = damage to the system or its data.",
    S, "Q2.7", 2)
mcq("F25b-2-8", 6, 39, "Design guideline — fail securely",
    "In design guidelines, __________ means when systems fail, for whatever reason, ensure that sensitive information cannot be accessed by unauthorized users.",
    ["Avoid a single point of failure", "Log user actions", "Use redundancy and diversity", "Fail securely"], "d",
    "Security slide 39, guideline 3: \"<b>Fail securely</b> — when systems fail, for whatever reason, ensure that sensitive information cannot be accessed by unauthorized users.\"",
    S, "Q2.8", 3)
mcq("F25b-2-9", 4, 10, "DRY principle",
    "DRY: Don't Repeat Yourself is one of the common clean code principles, which means …",
    ["Leave the campground cleaner than you found it", "Functions should do one thing and should do it well",
     "Avoid code duplications", "Function names are verbs"], "c",
    "Source Code Quality slide 10: \"DRY: Don't Repeat Yourself — to avoid code duplications.\" (a) is the Boy Scout rule, (b) is SRP.",
    S, "Q2.9", 3)
mcq("F25b-2-10", 4, 6, "Clean code",
    "Clean code means …",
    ["Compact and literate", "Contains only what is necessary", "Readable, simple and direct", "All of the above"], "d",
    "Source Code Quality slide 6 (What is clean code): readable, simple and direct; compact and literate; contains only what is necessary; … — all three are listed.",
    S, "Q2.10", 3)

short("F25b-3A-1", 7, 7, "Five dependability properties",
      "List the five principal dependability quality attributes of a system.",
      "<b>Availability</b>, <b>Reliability</b>, <b>Safety</b>, <b>Security</b>, <b>Resilience</b>.",
      "Dependability slide 7 (principal dependability properties diagram): availability — deliver services when requested; reliability — deliver services as specified; safety — operate without catastrophic failure; security — protect itself against intrusion; resilience — resist and recover from damaging events.",
      S, "Q3 Part A.1", 4)
short("F25b-3A-2", 7, 23, "POFOD calculation",
      "Calculate the POFOD if a system fails 40 times out of 10000 requests during 8 hours runtime.",
      "POFOD = failures / requests = 40 / 10000 = <b>0.004</b> (= 1/250). The 8 hours is not needed for POFOD.",
      "Slide 23: POFOD is the likelihood that a service request will result in a failure (failures / requests). It is independent of time.",
      S, "Q3 Part A.2", 4)
short("F25b-3A-3", 7, 25, "MTBF meaning",
      "What does the reliability metric 'Mean Time Between Failures (MTBF)' measure?",
      "The <b>average length of time between observed failures</b> (MTBF = total operating time / number of failures). It requires the timestamp of each failure and of when the system resumed service.",
      "Slide 25: \"Measures the average length of time between observed failures. Requires the timestamp of each failure and the timestamp of when the system resumed service.\"",
      S, "Q3 Part A.3", 4)
short("F25b-3B", 6, "4, 5, 14, 15", "Match security terms",
      "Match each term with its description."
      + table(["Column A", "Column B (descriptions)"],
              [["1- Confidentiality", "Ensuring that data remains accurate and unaltered"],
               ["2- Integrity", "Ensuring the security of networks, servers, and shared IT hardware"],
               ["3- Interruption Threat", "Ensuring that the system remains accessible when needed"],
               ["4- Modification Threat", "Ensuring that system information is not disclosed to unauthorized individuals"],
               ["5- Infrastructure Security", "Ensuring the security of individual software applications"],
               ["6- Application Security", "Tampering with or corrupting a system asset"],
               ["7- Availability", "Making a system unavailable"]]),
      table(["Description", "Term"],
            [["Data remains accurate and unaltered", "<b>2 Integrity</b>"],
             ["Security of networks, servers, shared IT hardware", "<b>5 Infrastructure Security</b>"],
             ["System remains accessible when needed", "<b>7 Availability</b>"],
             ["Information not disclosed to unauthorized individuals", "<b>1 Confidentiality</b>"],
             ["Security of individual software applications", "<b>6 Application Security</b>"],
             ["Tampering with or corrupting a system asset", "<b>4 Modification Threat</b>"],
             ["Making a system unavailable", "<b>3 Interruption Threat</b>"]]),
      "Slide 4: security dimensions (confidentiality, integrity, availability). Slide 5: security levels (infrastructure, application, operational). Slides 14–15: interruption threats make part of the system unavailable; modification threats tamper with an asset.",
      S, "Q3 Part B", 4)

short("F25b-4A", 8, "", "CFG for bubble sort",
      "Given the pseudocode for a function that sorts an array using Bubble Sort and finds the second largest element:"
      "<pre> 1. function find_second_largest(A, N){\n 2.   for (i = 1 To N){\n 3.     for (j = i-1 to N){\n 4.       if (A[j] > A[j + 1]){\n 5.         temp = A[j]\n 6.         A[j] = A[j + 1]\n 7.         A[j + 1] = temp }}}\n 8.   if (N &lt; 2)\n 9.     return None\n10.   else\n11.     return A[N - 2] }</pre>"
      "1) Draw a control flow graph. 2) Calculate the cyclomatic complexity. 3) Find the basic path set.",
      "<b>Nodes:</b> 1 = start · 2 = outer for (i ≤ N?) · 3 = inner for (j ≤ N?) · 4 = if A[j] &gt; A[j+1] · 5 = swap (lines 5–7) · 6 = j++ · 7 = i++ · 8 = if N &lt; 2 · 9 = return None · 10 = return A[N−2] · 11 = end<br>"
      "<b>Edges:</b> 1→2, 2→3 (T), 2→8 (F), 3→4 (T), 3→7 (F), 4→5 (T), 4→6 (F), 5→6, 6→3, 7→2, 8→9 (T), 8→10 (F), 9→11, 10→11 → E = 14, N = 11<br>"
      "<b>V(G)</b> = 14 − 11 + 2 = <b>5</b> (4 decisions: outer for, inner for, if, if N&lt;2 → 4 + 1 = 5)<br>"
      "<b>Basis paths:</b><br>1) 1-2-8-9-11<br>2) 1-2-8-10-11<br>3) 1-2-3-7-2-8-10-11<br>4) 1-2-3-4-6-3-7-2-8-10-11<br>5) 1-2-3-4-5-6-3-7-2-8-10-11",
      "Software-testing question (no deck in your slides). Every loop condition and if-statement is a decision node; V(G) = E − N + 2 = decisions + 1. Each basis path adds one new edge.",
      S, "Q4 Part A", 5)
short("F25b-4B-1", 8, "", "Equivalence classes and BVA",
      "Function validateAge checks whether an integer input age falls within an acceptable range for a particular service. The valid age range is 18 to 65, inclusive.<br>a) What are the equivalence classes for black-box testing validateAge?<br>b) What values should be tested using Boundary Value Analysis?",
      "a) <b>age &lt; 18</b> (invalid) · <b>18 ≤ age ≤ 65</b> (valid) · <b>age &gt; 65</b> (invalid)<br>"
      "b) <b>17, 18, 65, 66</b> (optionally also 19 and 64)",
      "Software-testing question (no deck in your slides). Boundary value analysis tests just below, on, and just above each boundary.",
      S, "Q4 Part B.1–2", 6)
short("F25b-4B-2", 8, "", "Black-box vs white-box",
      "What is the main difference between black-box testing and white-box testing?",
      "<b>White-box</b> testing tests the internal <b>structure</b> of the code (paths, branches) and finds design and code errors, but cannot find missing functions. "
      "<b>Black-box</b> testing tests the <b>function</b> from the specification without looking at the code; it can find requirements/specification errors and missing functions.",
      "Software-testing question (no deck in your slides); this is the white-box vs black-box table used in the course.",
      S, "Q4 Part B.3", 6)
short("F25b-4B-3", 10, "", "Test-driven development",
      "What is the main idea of Test-Driven Development (TDD)? Give one advantage of using TDD.",
      "<b>Test first:</b> write a (failing) unit test <i>before</i> writing the functional code, then write just enough code to pass it, then refactor.<br>"
      "<b>Advantages:</b> more tests → increased confidence in the code; yields many regression test cases; simpler, better-designed code; bugs found early.",
      "TDD is not in your slide decks (Source Code Quality slide 35 only links to a TDD reading).",
      S, "Q4 Part B.4–5", 6)
short("F25b-5", 9, "", "Software evolution fill-in",
      "Choose the correct term to fill each blank.<br><b>Terms:</b> Software Evolution · Reverse Engineering · System Re-engineering · Software Change · Software Requirements · Software Maintenance · System Refactoring · Servicing · Phase-out · Software Architecture · Maintenance Prediction · Software Testing"
      + ol(["Software change is inevitable because new ______ emerge when the software is used.",
            "______ does not normally involve major changes to the system's architecture.",
            "______ involves modifying a program to improve its structure, reduce its complexity, or make it easier to understand.",
            "______ is a process that takes place after a system has been maintained for some time.",
            "During ______, you need to understand how the program is structured and how it delivers functionality.",
            "When software enters the ______ stage, it may still be used, but no further changes are made to it."]),
      ol(["<b>Software Requirements</b>", "<b>Software Maintenance</b>", "<b>System Refactoring</b>",
          "<b>System Re-engineering</b>", "<b>Reverse Engineering</b>", "<b>Phase-out</b>"]),
      "Software evolution has no deck in your slides (Sommerville ch. 9). Maintenance does not normally involve major architectural changes; refactoring improves structure; re-engineering happens after a system has been maintained for some time and costs rise; reverse engineering recovers the program's structure; in phase-out no further changes are made.",
      S, "Q5", 8)
