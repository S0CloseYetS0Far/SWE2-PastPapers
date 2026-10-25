from qb import *

S = "F24b"
src(S, "Final — 2nd Semester 2024", "Exams/Final/2024/Final_2nd_2024.pdf")

mcq("F24b-1-1", 6, 14, "Threat types",
    "__________ threats allow an attacker to gain access to an asset.",
    ["Interruption", "Interception", "Fabrication", "Modification"], "b",
    "Security slide 14: \"<b>Interception</b> threats that allow an attacker to gain access to an asset.\" Interruption = make part of the system unavailable; modification = tamper with an asset; fabrication = insert false information.",
    S, "Q1.1", 1)
mcq("F24b-1-2", 4, 9, "Code smell",
    "What does the term \"Code Smell\" refer to?",
    ["A pleasant aroma in the development environment", "A coding style that is universally accepted",
     "Comments in the code that are too verbose", "Indications of potential issues in the code"], "d",
    "Source Code Quality slide 9: \"Programmers often describe bad code as having a '<b>bad smell</b>' that needs to be removed.\" A code smell is a sign of a problem in the code.",
    S, "Q1.2", 1)
mcq("F24b-1-3", 7, 17, "Reliability achievement",
    "What is the term for a development process organised such that faults in the system are detected and repaired before delivery to the customer?",
    ["Fault avoidance", "Fault detection", "Fault tolerance", "None of the mentioned"], "b",
    "Dependability slide 17 (reliability achievement): <b>fault avoidance</b> — development techniques that minimise the possibility of mistakes; <b>fault detection (and removal)</b> — verification and validation techniques that discover and remove faults <i>before the system is delivered</i>; <b>fault tolerance</b> — run-time techniques so faults do not cause failures.",
    S, "Q1.3", 1)
mcq("F24b-1-4", 4, "3, 12, 13", "Code readability",
    "What is code readability?",
    ["The ability to execute code without errors", "The efficiency of code execution",
     "The number of lines of code in a program", "The ease with which code can be understood by humans"], "d",
    "Source Code Quality slide 3 (legibility issues): \"Code should document itself; code should be easy to read.\" Slides 12–13 show how meaningful names make code understandable.",
    S, "Q1.4", 1)
mcq("F24b-1-5", 8, "", "Testing terms",
    "Identify the term which is <b>not</b> related to testing.",
    ["Failure", "Error", "Test bot", "Test case"], "c",
    "Failure, error and test case are standard testing terms (a test case produces a failure caused by an error/fault). \"Test bot\" is not a testing term in the course. (Software testing has no deck in your slides.)",
    S, "Q1.5", 1)
mcq("F24b-1-6", 7, 13, "Reliability terminology",
    "A characteristic of a software system that can lead to a system error is known as?",
    ["Human error or mistake", "System fault", "System error", "System failure"], "b",
    "Dependability slide 13: \"<b>System fault</b> — a characteristic of a software system that can lead to a system error.\"",
    S, "Q1.6", 1)
mcq("F24b-1-7", 10, "", "Model checking",
    "A disadvantage of model checking in formal verification is:",
    ["Scalability", "Weak debugging capabilities", "It requires deep training", "Cannot be integrated within industrial development cycle"], "a",
    "Model checking explores <b>every reachable state</b> of a finite-state model, so the number of states explodes as the system grows (the 'state explosion' problem) — it does not scale well to large systems. It gives good counter-examples for debugging and is used in industry. (Not in your slide decks.)",
    S, "Q1.7", 2)
mcq("F24b-1-8", 7, 4, "Causes of failure",
    "Operational failure means:",
    ["Hardware fails because of design and manufacturing errors", "Software fails due to errors in its specification, design or implementation",
     "Human operators make mistakes", "All of the above"], "c",
    "Dependability slide 4: \"<b>Operational failure</b> — human operators make mistakes.\" (a) is hardware failure, (b) is software failure.",
    S, "Q1.8", 2)
mcq("F24b-1-9", 7, 24, "ROCOF",
    "Which reliability metric sets out the probable number of system failures that are likely to be observed relative to a certain time period?",
    ["POFOD", "ROCOF", "MTBF", "AVAIL"], "b",
    "Dependability slide 24: ROCOF — \"probable number of failures over a period of time or number of system executions.\"",
    S, "Q1.9", 2)
mcq("F24b-1-10", 6, 6, "Layers of protection",
    "Which of the following is a layer of protection for security?",
    ["Platform-level protection", "Application-level protection", "Record-level protection", "All of the above"], "d",
    "Security slide 6 (system layers where security may be compromised): security is applied at the <b>platform</b> level, the <b>application</b> level and the <b>record</b> level — all three are layers of protection.",
    S, "Q1.10", 2)

TF = [
    (1, 10, "", "Model checking is proven unsuccessful in detecting problems in the early stages of the development cycle.", False,
     "Model checking is <b>successful</b> at finding problems early (on design models). Official model answer: F. (Not in your slide decks.)"),
    (2, 6, 3, "Security engineering is only concerned with maintenance of systems such that they can resist malicious attacks.", False,
     "Security slide 3: tools, techniques and methods to support the <b>development and maintenance</b> of systems that can resist malicious attacks — not only maintenance."),
    (3, 4, 8, "Code reviews are an essential component of ensuring software quality.", True,
     "Source Code Quality slides 8–9: code review improves the code and the programmer; at Google no code can be pushed without a review."),
    (4, 7, "3, 6", "Dependability is not relevant in non-critical systems, as failures in such systems do not have significant consequences.", False,
     "Dependability slide 3: failures cost money, time, lives and reputation; slide 6: dependability reflects the user's trust in <i>any</i> system."),
    (5, 7, 25, "Mean Time Between Failures (MTBF) is a measure of reliability, representing the average time a system operates before a failure occurs.", True,
     "Dependability slide 25: MTBF \"measures the average length of time between observed failures.\""),
    (6, 10, "", "Model checking is a technique used in formal methods to verify the correctness of a system by exhaustively exploring all possible states.", True,
     "Model checking builds a finite-state model and exhaustively checks every reachable state against the specification. (Not in your slide decks.)"),
    (7, 4, 33, "Formal methods are always more expensive than traditional testing techniques.", False,
     "\"Always\" is wrong — formal methods have high up-front cost but can reduce later testing and rework costs, especially for critical systems. Source Code Quality slide 33 introduces formal methods."),
    (8, 7, 16, "A fault-tolerant system requires manual intervention to recover from faults.", False,
     "Dependability slide 16: fault tolerance means the system <b>can continue in operation</b> in spite of software failure — automatically."),
    (9, 8, "", "Coverage monitoring is vital for white-box testing.", True,
     "White-box testing aims to exercise the code structure (statements, branches, paths), so coverage must be measured. Official model answer: T."),
    (10, 8, "", "The goal of a software tester is to find bugs, find them as early as possible and make sure they get fixed.", True,
     "This is the classic definition of the tester's goal (Patton, Software Testing)."),
]
for n, ch, sl, q, a, e in TF:
    tf("F24b-2-%d" % n, ch, sl, "True / False", q, a, e, S, "Q2.%d" % n, 3)

short("F24b-3", 6, "6, 8, 12, 44", "Match security terms",
      "Write the number of the appropriate definition in front of each term."
      + table(["Term", "Definition"],
              [["Vulnerability", "1. Something of value which has to be protected. This may be the software system itself or data used by that system."],
               ["Application-level protection", "2. System security testing by simulating attacks on the system."],
               ["System Reliability", "3. A weakness in a computer-based system that may be exploited to cause loss or harm."],
               ["Asset", "4. The probability that the system will correctly deliver services as expected by users."],
               ["Penetration testing", "5. Possible loss or harm to a computing system (loss or damage to data, or loss of time and effort if recovery is necessary)."],
               ["System Security", "6. A judgment of how likely it is that the system will cause damage to people or its environment."],
               ["System Safety", "7. Specific protection mechanisms built into the application itself, e.g. additional password protection."],
               ["Exposure", "8. A judgment of how likely it is that the system can resist accidental or deliberate intrusions."]]),
      table(["Term", "No."],
            [["Vulnerability", "<b>3</b>"], ["Application-level protection", "<b>7</b>"], ["System Reliability", "<b>4</b>"], ["Asset", "<b>1</b>"],
             ["Penetration testing", "<b>2</b>"], ["System Security", "<b>8</b>"], ["System Safety", "<b>6</b>"], ["Exposure", "<b>5</b>"]]),
      "Security slide 12: asset, exposure, vulnerability. Slide 44: penetration testing simulates attacks. Slide 6: application-level protection. Dependability slide 8: reliability, safety and security definitions.",
      S, "Q3", 4)

short("F24b-4", 8, "", "Testing terminology fill-in",
      "Match the blank with the most appropriate term (no duplication).<br><b>Terms:</b> Verification · Automation Testing · Privacy · Model Checking · Regression Testing · Manual Testing · Reliability · Smoke testing · Test Oracles · Control · Validation · Load Testing"
      + ol(["______ performed on a newly developed software build.",
            "______ refers to a different set of tasks that ensure that the software that has been built is traceable to customer requirements.",
            "______ determines whether a system behaves correctly for test execution.",
            "______ refers to the verification of changes in software after bug fixes or changes in requirements did not affect current features.",
            "______ is used to re-run the test scenarios quickly and repeatedly, that were performed manually in manual testing.",
            "______ refers to the set of tasks that ensure that the software correctly implements a specific function."]),
      ol(["<b>Smoke testing</b>", "<b>Validation</b>", "<b>Test Oracles</b>", "<b>Regression Testing</b>", "<b>Automation Testing</b>", "<b>Verification</b>"]),
      "Verification = \"are we building the product right?\" (implements a function correctly); validation = \"are we building the right product?\" (traceable to customer requirements). A test oracle decides whether the output is correct. (Software testing has no deck in your slides.)",
      S, "Q4", 6)

SYS = [
    (1, "In a railway signalling system, the primary focus is to control the movement of trains and ensure safety on the tracks. It is essential to minimize the risk of signalling failures that could lead to accidents or disruptions in train operations. The system must undergo rigorous testing and continuous monitoring to ensure the reliable and safe operation of railway traffic.",
     ["POFOD", "ROCOF", "Availability"], 0, "23",
     "A signalling/protection system is called on when a train approaches — a failure <i>on demand</i> could cause an accident. Slide 23: POFOD \"should be used as a reliability metric in situations where a failure on request is serious.\""),
    (2, "An Internet server provided by an ISP (Internet Service Provider) with thousands of customers.",
     ["Security", "Safety", "Availability"], 2, "8, 26",
     "Thousands of customers depend on the server being up and able to deliver its services at any time → <b>availability</b> (slide 8). Official model answer (Final 1st 2024): Availability."),
    (3, "In a data management system of a financial institution, the system is dedicated to preserving the integrity of data while preventing any unauthorized exposure.",
     ["Security", "Safety", "Availability"], 0, "8",
     "Integrity and preventing unauthorized exposure are security concerns — slide 8: security is how likely the system can resist accidental or deliberate intrusions. Official model answer: Security."),
    (4, "In a hospital patient monitoring system, the main goal is to continuously track patients' vital signs such as heart rate, blood pressure, and oxygen levels. It ensures that healthcare professionals have real-time access to vital patient data, enabling timely interventions and improving patient care.",
     ["Security", "Safety", "Availability"], 2, "8",
     "The description stresses <b>continuous</b> tracking and <b>real-time access</b> — the system must be up and able to deliver its service whenever needed → availability (slide 8). <i>Some students argue Safety because patients could be harmed; the wording here points to availability.</i>"),
]
for n, desc, opts, a, sl, e in SYS:
    mcq("F24b-5-%d" % n, 7, sl, "Most critical dependability attribute",
        "Choose the most appropriate dependability attribute that is crucial to the system:<br>" + desc, opts, a, e, S, "Q5.%d" % n, 5)

mcq("F24b-5-5", 7, "26, 29", "Availability calculation",
    "A power plant operates continuously with a significant system impact upon failure. After 8050 total service requests in one year (8760 hours), with 5 failures and an average repair time of 5 hours per failure, the availability of the power plant ≈",
    ["0.9994", "0.00062", "0.00057", "0.9971"], "d",
    "Downtime = 5 failures × 5 h = 25 h. Availability = (8760 − 25) / 8760 = 8735 / 8760 = <b>0.9971</b>. Same method as Dependability slide 29.",
    S, "Q5.5", 5)
mcq("F24b-5-6", 7, 24, "ROCOF calculation",
    "Same power plant (8050 requests in 8760 hours, 5 failures, 5 hours average repair). The Rate of Occurrence of Failure (ROCOF) ≈",
    ["0.9994", "0.00062", "0.00057", "0.9971"], "c",
    "ROCOF = failures / time = 5 / 8760 = <b>0.00057</b> failures per hour (slide 24). Note 0.00062 = 5 / 8050 is the POFOD (failures per request).",
    S, "Q5.6", 5)
