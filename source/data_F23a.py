from qb import *

S = "F23a"
src(S, "Final — 1st Semester 1445 (Fall 2023), official model answer", "Exams/Final/2024/FinalExam_MA.docx  (student notes on the same exam: Exams/Final/2023/FINAL-1st-2023.pdf)")

mcq("F23a-1-1", 10, "", "TDD cycle",
    "Which of the following is <b>not</b> part of a Test Driven Development (TDD) cycle?",
    ["Write a successful test", "Write a failing test", "Make the test pass", "Refactoring"], "a",
    "The TDD cycle is red → green → refactor: write a <b>failing</b> test first, make it pass, then refactor. You never start by writing a test that already succeeds. Official key: a.",
    S, "Q1.1")
also("F24b-1-1", S, "Q1.2")
mcq("F23a-1-3", 10, "", "Object responsibilities",
    "What type of object responsibility is \"references to other objects\"?",
    ["Doing responsibility", "Knowing responsibility", "Delegation responsibility", "Initiation responsibility"], "b",
    "In responsibility-driven design, <b>knowing</b> responsibilities are what an object knows: its private data, <b>references to related objects</b>, and things it can derive. Doing responsibilities are actions it performs. Official key: b. (Not on your slides.)",
    S, "Q1.3")
mcq("F23a-1-4", 4, "31, 33", "Formal verification advantage",
    "Which of the following is a key advantage of formal verification?",
    ["Quick and easy to apply", "Can detect all possible defects in a software system",
     "Provides mathematical proof of correctness", "Requires no formal specification of software behaviour"], "c",
    "Source Code Quality slide 31: a 'formally correct' program's correctness can be <b>proved mathematically</b>; slide 33: formal methods use mathematical modelling for specification and verification. Official key: c.",
    S, "Q1.4")
mcq("F23a-1-5", 1, 9, "Preventive maintenance",
    "What is the primary goal of \"Preventive Maintenance\" in software evolution?",
    ["Fixing defects and issues", "Enhancing software functionality",
     "Identifying and addressing potential issues before they cause problems", "Rewriting the entire software application"], "c",
    "Intro slide 9: \"Preventive — re-engineering, make system more maintainable\" — i.e. improving the system <i>before</i> problems happen. Fixing defects is corrective; enhancing functionality is perfective. Official key: c.",
    S, "Q1.5")
mcq("F23a-1-6", 6, "", "Third-party library security",
    "Scenario: a software development team is considering the integration of a third-party API library for image processing. What security practice should the team follow to ensure the library is safe to use?",
    ["Conduct code reviews of the library", "Implement strong access controls", "Enforce secure coding standards", "Apply patch management practices"], "a",
    "Before trusting external code you must <b>inspect/review it</b> for vulnerabilities (experience-based review against known attacks, Security slide 44). Access controls and coding standards protect your own system/code, not the library. Official key: a.",
    S, "Q1.6")
mcq("F23a-1-7", 7, "26, 29", "Availability calculation",
    "A server crashes on average once in 30 days. When this happens, it takes 12 hours to reboot it. What is the availability of the server?",
    ["0.983", "0.017", "0.996", "0.4"], "a",
    "30 days = 720 h. Uptime = 720 − 12 = 708 h → Availability = 708 / 720 = <b>0.983</b>. (0.017 is the unavailability.) Same method as Dependability slide 29. Official key: a.",
    S, "Q1.7")
mcq("F23a-1-8", 7, 25, "MTBF",
    "In the context of dependability properties, what does \"MTBF\" stand for?",
    ["Mean Time Between Failures", "Maximum Time for Backup", "Minimum Time for Recovery", "Most Time for Buffering"], "a",
    "Dependability slide 25: <b>Mean Time Between Failures</b>.",
    S, "Q1.8")
mcq("F23a-1-9", 7, 16, "Fault tolerance",
    "Which of the following best defines \"fault tolerance\"?",
    ["The system's ability to avoid all faults", "The system's ability to support and continue functioning in the presence of faults",
     "The system's capacity to anticipate and prevent faults", "The system's capability to identify faults in real-time"], "b",
    "Dependability slide 16: \"Fault tolerance means that the system can <b>continue in operation</b> in spite of software failure.\" (a, c = fault avoidance; d = fault detection.)",
    S, "Q1.9")
mcq("F23a-1-10", 10, "", "Strategy pattern",
    "Which design pattern is used when you want to define a family of algorithms, encapsulate each one, and make them interchangeable?",
    ["Singleton Pattern", "Façade Design Pattern", "Strategy Pattern", "Observer Pattern"], "c",
    "That is the intent of the <b>Strategy</b> pattern (also used in the Final 2021 model answer). Singleton = only one instance; Façade = a single class representing a subsystem (OOAD slide 25). Official key: c.",
    S, "Q1.10")

TF = [
    (1, 9, "The majority of the software budget in large companies is devoted to changing and evolving existing software rather than developing new software.", True,
     "Sommerville ch. 9: most of the budget goes to evolving existing software. Official key: T."),
    (2, 9, "Proposals for change are the driver for system evolution.", True,
     "Sommerville ch. 9: change proposals drive system evolution. Official key: T."),
    (3, 9, "Reengineering aims to enhance the functionality of the software without making changes to its structure.", False,
     "It is the opposite: re-engineering restructures or rewrites the system <b>without changing its functionality</b> to make it more maintainable (Intro slide 9: preventive maintenance). Official key: F."),
    (4, 9, "Ageing software can have high support costs.", True,
     "Legacy/ageing software is expensive to maintain (outdated languages, degraded structure). Official key: T."),
    (5, 9, "Refactoring is the process of making improvements to a program to accelerate degradation through change.", False,
     "Refactoring improves a program to <b>slow down</b> degradation through change. Official key: F."),
    (7, 10, "Using finite state machines is a limitation of model checking.", True,
     "Model checking needs the system expressed as a finite-state model, which limits it (large or infinite state spaces cannot be fully explored). Official key: T."),
    (8, 4, "When a program is proven to be correct using formal verification, then we can say that the program is formally correct.", True,
     "Source Code Quality slide 31: a 'formally correct' program is one whose correctness can be proved mathematically. Official key: T."),
    (9, 10, "The model checking method uses a data flow diagram as the system model for formal verification.", False,
     "Model checking uses a <b>finite state machine</b> (state transition model), not a data flow diagram. Official key: F."),
]
for n, ch, q, a, e in TF:
    tf("F23a-2-%d" % n, ch, "31" if ch == 4 else "", "True / False", q, a, e, S, "Q2.%d" % n)
also("F24b-2-1", S, "Q2.6")
also("F24b-2-9", S, "Q2.10")

short("F23a-3", 8, "", "Match testing terms",
      "Match each term to its definition number."
      + table(["Term", "#", "Definition"],
              [["Cluster Testing", "1", "Using specialized software tools and scripts to automate the execution of test cases and the comparison of actual outcomes with expected results."],
               ["Sanity Testing", "2", "A quick and preliminary test to verify whether the most critical and basic functionalities are working, often performed before more comprehensive testing."],
               ["Use-Based Testing", "3", "Evaluating the concurrent and multi-aspects of an OO system: how a set of classes and objects respond to one input or event."],
               ["Smoke Testing", "4", "A mechanism, such as a set of expected outcomes or rules, used to determine whether the software under test is functioning correctly."],
               ["Automated Testing", "5", "Re-running previously executed test cases to ensure that new changes do not introduce new defects or break existing features."],
               ["Test Oracle", "6", "Testing the software from the perspective of how users will interact with it."],
               ["Regression Testing", "7", "A subset of regression testing that is undocumented and unscripted and quickly checks that recent changes have not affected main functionality."],
               ["Thread-Based Testing", "8", "Assessing the interactions and behaviours of groups of related classes or objects within an OO system."]]),
      table(["Term", "Definition #"],
            [["Cluster Testing", "<b>8</b>"], ["Sanity Testing", "<b>7</b>"], ["Use-Based Testing", "<b>6</b>"], ["Smoke Testing", "<b>2</b>"],
             ["Automated Testing", "<b>1</b>"], ["Test Oracle", "<b>4</b>"], ["Regression Testing", "<b>5</b>"], ["Thread-Based Testing", "<b>3</b>"]]),
      "Official model answer. Smoke = quick check of critical functions on a new build; sanity = unscripted subset of regression after a change; thread-based = classes responding to one event; cluster = a group of collaborating classes. (Software testing has no deck in your slides.)",
      S, "Q3")
short("F23a-4", 6, "12, 13", "Security terminology — XYZ Corp",
      "Scenario: XYZ Corp is concerned about the security of its sensitive customer data stored in an online database. Fill each blank with the most appropriate term (no duplication).<br>"
      "<b>Terms:</b> Vulnerability · Asset · Privacy · Attack · Availability · Threat · Reliability · Modification · Impersonation · Control · Denial of service · Exposure"
      + ol(["______ : Online database contains information such as names, addresses, and credit card numbers of their customers.",
            "______ : Attempts happened to gain unauthorized access to the online database.",
            "______ : XYZ Corp implements multi-factor authentication and intrusion detection systems.",
            "______ : Customer database is at risk or could be compromised.",
            "______ : An unauthorized individual will make an attempt to breach the database.",
            "______ : A weak password system which makes it easy to set guessable passwords."]),
      ol(["<b>Asset</b>", "<b>Attack</b>", "<b>Control</b>", "<b>Exposure</b>", "<b>Threat</b>", "<b>Vulnerability</b>"]),
      "Security slide 12 (definitions) and slide 13 (Mentcare examples: weak password system = vulnerability; password checking = control). Official model answer.",
      S, "Q4")

SYS = [
    (1, "The Internet of Things (IoT) project on the DHT11 sensor provides a continuous way to measure and monitor temperature and humidity in a variety of environments, storing the data in a database for analysis, climate-control decisions, user alerts and long-term trend tracking.",
     ["POFOD", "ROCOF", "Availability"], 2, "26",
     "The sensor must run <b>continuously</b> to monitor the environment — the key requirement is that it is up and delivering data → availability. Official key: Availability."),
    (2, "In an air traffic control system, the primary focus is to ensure the uninterrupted and error-free operation of flying activities, minimizing the potential for accidents or incidents.",
     ["Security", "Safety", "Reliability"], 1, "8, 18",
     "Minimizing accidents → <b>safety</b> (slide 8: how likely the system will cause damage to people or its environment). Official key: Safety."),
    (3, "In a financial trading platform, the system's primary goal is to execute transactions reliably and swiftly, even in high-pressure trading environments.",
     ["POFOD", "ROCOF", "Security"], 0, "23",
     "Each trade request must succeed — a failure on a request is serious → <b>POFOD</b> (slide 23). Official key: POFOD."),
    (5, "In an online payment processing platform. This system operates in a fast-paced digital landscape, handling countless online payments daily.",
     ["Security", "Safety", "Reliability"], 2, "8",
     "Countless payments must each be processed correctly → <b>reliability</b> (slide 8: correctly deliver services as expected). Official key: Reliability."),
]
for n, desc, opts, a, sl, e in SYS:
    mcq("F23a-5-%d" % n, 7, sl, "Most critical dependability attribute",
        "Choose the most appropriate dependability attribute that is crucial to the system:<br>" + desc, opts, a, e, S, "Q5.%d" % n)
also("F24b-5-3", S, "Q5.4")
also("F24b-5-2", S, "Q5.6")
