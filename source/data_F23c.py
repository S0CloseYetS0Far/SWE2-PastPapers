from qb import *

S = "F23c"
src(S, "Final — 3rd Semester 2023", "Exams/Final/2023/Final_3rd_2023.pdf")

mcq("F23c-1-2", 7, 13, "Human error",
    "A characteristic of human behaviour that results in the introduction of faults into a system is a:",
    ["Human error or mistake", "System fault", "System error", "System failure"], "a",
    "Dependability slide 13: \"<b>Human error or mistake</b> — human behavior that results in the introduction of faults into a system.\"",
    S, "Q1.2", 1)
mcq("F23c-1-3", 8, "", "Execution-based verification",
    "__________ is/are considered as an execution-based verification.",
    ["Inspections", "Load testing", "Formal verification", "Static code analysis"], "b",
    "Execution-based (dynamic) verification <b>runs the program</b> — load testing does. Inspections, formal verification and static analysis examine the code without running it. (Software testing — no deck in your slides.)",
    S, "Q1.3", 1)
mcq("F23c-1-4", 9, "", "Phase-out",
    "__________ means that a software may still be used but without any further changes.",
    ["Evolution", "Maintenance", "Servicing", "Phasing out"], "d",
    "Sommerville ch. 9: in <b>phase-out</b> the software may still be used but no further changes are made to it. In servicing, only small changes needed to keep it operational are made.",
    S, "Q1.4", 1)
mcq("F23c-1-5", 6, 44, "Security validation techniques",
    "Which testing technique may <b>not</b> be directly related to security verification?",
    ["Unit testing", "Experience-based testing", "Penetration testing", "Formal verification"], "a",
    "Security slide 44 lists the security validation techniques: <b>experience-based testing, penetration testing, tool-based analysis and formal verification</b>. Unit testing checks individual components' functionality, not security.",
    S, "Q1.5", 1)
mcq("F23c-1-6", 5, 15, "SOLID",
    "Which of the following is <b>not</b> one of the SOLID software design principles?",
    ["Single Responsibility Principle", "Open-Closed Principle", "DRY Principle", "Liskov Substitution Principle"], "c",
    "OOAD slide 15 (SOLID): Single Responsibility, Open/Closed, Liskov Substitution, Injection of Dependency, Demeter. <b>DRY</b> is a clean-code principle (Source Code Quality slide 10).",
    S, "Q1.6", 2)
mcq("F23c-1-7", 3, 11, "Efficiency",
    "Minimal use of resources is best used to measure:",
    ["Efficiency", "Adaptability", "Complexity", "Robustness"], "a",
    "<b>Efficiency</b> (Quality slide 11) is about using minimal resources (time, memory, CPU) for the required performance.",
    S, "Q1.7", 2)
mcq("F23c-1-8", 8, "", "Load testing",
    "Which type of testing involves testing the software's ability to handle concurrent user requests?",
    ["Functional testing", "Smoke testing", "Load testing", "Code auditing"], "c",
    "<b>Load testing</b> puts the system under many concurrent users/requests to check its behaviour under load. (Software testing — no deck in your slides.)",
    S, "Q1.8", 2)
mcq("F23c-1-9", 8, "", "Good test cases",
    "Which of the following is <b>not</b> a characteristic of good test cases?",
    ["They should be repeatable", "They should be understandable", "They should be automated", "They should be testable"], "c",
    "Good test cases are repeatable, understandable and testable (clear expected result). They do <b>not have to be automated</b> — manual test cases can be good test cases.",
    S, "Q1.9", 2)
mcq("F23c-1-10", 8, "", "Performance issue",
    "You are testing a desktop spreadsheet application. During testing, you notice that the application freezes when a user tries to sort a large dataset. Which type of testing issue is this?",
    ["Functional issue", "Performance issue", "Safety issue", "Security issue"], "b",
    "Sorting works but the app <b>freezes on a large data set</b> — it cannot handle the load in acceptable time → performance issue.",
    S, "Q1.10", 2)

TF = [
    (1, 9, "", "Reverse engineering is the process of re-writing part or all of a legacy system without changing its functionality.", False,
     "That describes <b>re-engineering</b>. Reverse engineering analyses a program to understand its structure and how it delivers functionality."),
    (2, 9, "", "We can assess maintainability by measuring metrics such as the average time required for impact analysis.", True,
     "Sommerville ch. 9 maintainability metrics: number of change requests, average time for impact analysis, average time to implement a change request, number of outstanding change requests."),
    (3, 8, "", "The cost of software testing is often less than the costs of other software development processes.", False,
     "Testing is one of the most expensive activities — often around half of development cost."),
    (4, 9, "", "The maintainability of a software product increases when the number of change requests increases.", False,
     "An <b>increase</b> in the number of (corrective) change requests indicates a <b>decline</b> in maintainability (Sommerville ch. 9). <i>The solved copy marked True — that is wrong.</i>"),
    (5, 8, "", "One difference between sanity testing and regression testing is that regression testing is unscripted.", False,
     "It is the other way round: <b>sanity</b> testing is unscripted and undocumented; regression testing re-runs scripted test cases (Final Fall 2023 model answer definitions)."),
    (6, 8, "", "Testing can detect bugs, but it cannot guarantee the absence of bugs.", True,
     "Dijkstra: testing can show the presence of bugs, not their absence. Intro slide 16: exhaustive testing is infeasible."),
    (7, 8, "", "When the complexity of the system increases, then the testing cost and effort increase as well.", True,
     "More paths and states (higher cyclomatic complexity) need more test cases."),
    (8, 4, 31, "When a program is proven to be correct using formal verification, then we can indicate that the program is formally correct.", True,
     "Source Code Quality slide 31: a 'formally correct' program is one whose correctness can be proved mathematically. (The official Fall 2023 key says True; the solved copy of this exam marked False — that is wrong.)"),
    (9, 10, "", "The model checking method uses a sequence diagram as the system model for formal verification.", False,
     "Model checking uses a <b>finite state machine</b> model."),
    (10, 10, "", "Model checking is the only method of formal verification.", False,
     "Formal verification also includes theorem proving / deductive verification (e.g. JML specifications, Source Code Quality slide 33)."),
]
for n, ch, sl, q, a, e in TF:
    tf("F23c-2-%d" % n, ch, sl, "True / False", q, a, e, S, "Q2.%d" % n, 3)

short("F23c-3", 7, "16, 25, 26", "Hospital system — MTBF and availability",
      "You are developing a software system that is critical to the operation of a hospital (patient records, appointments, medical payments). After extensive testing, the system has a mean time between failures (MTBF) of 200 hours. Each failure takes an average of 30 minutes to repair. Additionally, a fault-tolerance mechanism allows the system to continue functioning even if a single component fails, with a mean time to repair (MTTR) of 5 minutes. Assume the system operates 24/7 and failures are independent.<br>"
      "1) Approximately how many times would you expect the system to fail in a month?<br>2) What is the availability of the system? (formula + calculation)<br>3) How does the fault-tolerance mechanism affect the system's reliability and dependability?<br>4) Can you calculate the POFOD of the system?",
      "1) A month ≈ 30 × 24 = 720 h → 720 / 200 ≈ <b>3.6, i.e. about 3–4 failures per month</b>.<br>"
      "2) Availability = MTBF / (MTBF + MTTR).<br>Without fault tolerance: 200 / (200 + 0.5) = <b>0.9975</b> (99.75%).<br>With fault tolerance (MTTR = 5 min = 0.083 h): 200 / (200 + 0.083) = <b>0.9996</b> (99.96%).<br>"
      "3) Fault tolerance lets the system <b>keep operating in spite of a component failure</b>, so downtime drops from 30 to 5 minutes — availability and dependability increase and users experience fewer service failures (higher perceived reliability). It does not reduce the number of underlying faults.<br>"
      "4) <b>No</b> — POFOD = failures / requests, and the number of requests is not given.",
      "Dependability slide 16 (fault tolerance), slide 25 (MTBF), slide 26 (availability takes repair time into account), slide 23 (POFOD needs the number of requests).",
      S, "Q3.2", 4)
