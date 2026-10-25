from qb import *

S = "F24a"
src(S, "Final — 1st Semester 2024", "Exams/Final/2024/Final_1st_2024.pdf  +  solved copy: Exams/Final/2024/فاينل الترم الاول Renad-2024.pdf")

TF = [
    (1, 2, 3, "Software project management is concerned with ensuring that software is delivered on time and on budget.", True,
     "PM slide 3: project management is \"concerned with activities involved in ensuring that software is delivered on time and on schedule and in accordance with the requirements\"; slide 4 success criteria include keeping costs within budget."),
    (2, 2, 6, "Risk management involves assessing risks that may affect a project and taking action when problems arise.", True,
     "PM slide 6: \"Project managers assess the risks that may affect a project, monitor these risks and take action when problems arise.\""),
    (3, 2, 5, "All software projects are similar, making it easy for experienced managers to anticipate problems.", False,
     "PM slide 5: many software projects are 'one-off' projects — \"Even managers who have lots of previous experience may find it difficult to anticipate problems.\""),
    (4, 2, 22, "Poor people management can lead to project failure.", True,
     "PM slide 22: \"Poor people management is an important contributor to project failure.\""),
    (5, 2, 30, "Group cohesiveness can lead to shared knowledge and continuity if a member leaves the team.", True,
     "PM slide 30: \"Knowledge is shared. Continuity can be maintained if a group member leaves.\""),
    (6, 3, 29, "Static metrics are used to measure the performance and reliability of software.", False,
     "Quality slide 29: <b>dynamic</b> metrics help assess efficiency and reliability; static metrics help assess complexity, understandability and maintainability."),
    (7, 3, 23, "A software metric can be used to quantify aspects of the software development process.", True,
     "Quality slide 23: metrics \"allow the software and the software process to be quantified.\""),
    (8, 2, 8, "Product risks affect the quality or performance of the software being developed.", True,
     "PM slide 8: \"Product risks affect the quality or performance of the software being developed.\""),
]
for n, ch, sl, q, a, e in TF:
    tf("F24a-1-%d" % n, ch, sl, "Project management T/F", q, a, e, S, "Q1.%d" % n, 1)

mcq("F24a-2-1", 3, 3, "Quality management concern",
    "What is the primary concern of software quality management?",
    ["Cost reduction", "Ensuring software meets the required quality level", "Increasing development speed", "Reducing team size"], "b",
    "Quality slide 3: software quality management is \"concerned with ensuring that the <b>required level of quality is achieved</b> in a software product.\"",
    S, "Q2.1", 2)
mcq("F24a-2-2", 3, 3, "Project-level concerns",
    "What is one of the three principal concerns of quality management at the project level?",
    ["Marketing strategies", "Defining a quality plan", "Software pricing", "Hiring more developers"], "b",
    "Quality slide 3: \"At the project level, quality management is also concerned with <b>establishing a quality plan</b> for a project.\"",
    S, "Q2.2", 2)
mcq("F24a-2-3", 3, 8, "Fitness for purpose",
    "The concept of 'fitness for purpose' in software quality focuses on:",
    ["Aesthetic design", "Specification conformance", "How well the software meets user needs", "Code efficiency"], "c",
    "Quality slide 8: \"The focus may be 'fitness for purpose' <b>rather than specification conformance</b>\" — i.e. whether the software meets its users' needs.",
    S, "Q2.3", 2)
mcq("F24a-2-4", 3, 16, "Agile quality management",
    "Agile quality management relies on:",
    ["Strict adherence to documentation", "Informal, culture-driven quality practices", "Reducing team interactions", "Outsourcing testing processes"], "b",
    "Quality slide 16: agile QM is informal rather than document-based and relies on establishing a <b>quality culture</b>.",
    S, "Q2.4", 2)
mcq("F24a-2-5", 3, 12, "Quality conflicts",
    "Quality conflicts in software development can occur because:",
    ["Developers prefer working on different platforms", "Improving one quality attribute may negatively impact another",
     "Software specifications are always clear and concise", "All teams have the same quality priorities"], "b",
    "Quality slide 12 (quality conflicts): \"It is not possible for any system to be optimized for all of these attributes — for example, improving robustness may lead to loss of performance.\"",
    S, "Q2.5", 2)
mcq("F24a-2-6", 3, 15, "Quality culture",
    "When developing a quality culture, quality managers should:",
    ["Focus on documentation", "Restrict communication between teams", "Encourage teams to take ownership of quality improvement", "Assign quality tasks to few key members"], "c",
    "Quality slide 15: \"They should encourage teams to take responsibility for the quality of their work and to develop new approaches to quality improvement.\"",
    S, "Q2.6", 2)
mcq("F24a-2-7", 3, 11, "Quality attributes",
    "Which of these is a software quality attribute focused on safety and resilience?",
    ["Reliability", "Portability", "Usability", "Modularity"], "a",
    "Quality slide 11 groups <b>Safety, Security, Reliability, Resilience, Robustness</b> together (the dependability-related attributes). Portability, usability and modularity are not about safety.",
    S, "Q2.7", 3)
mcq("F24a-2-8", 4, 8, "Code review purpose",
    "What is the primary purpose of a code review?",
    ["To improve the code and the programmer", "To update project documentation", "To clean up unnecessary files", "To enhance user interface design"], "a",
    "Source Code Quality slide 8: \"Code review really has two purposes: Improving the code. Improving the programmer.\"",
    S, "Q2.8", 3)
mcq("F24a-2-9", 4, "20–23", "Be explicit — curly brackets",
    "What issue is often associated with not using curly brackets in conditional statements?",
    ["Reduced performance", "Syntax errors", "Increased ambiguity and potential errors", "Better readability"], "c",
    "Source Code Quality slides 20–23 (Be explicit): without braces, adding a second statement or nesting if/else makes the code ambiguous (dangling else) — \"Does that do what you mean?\" — so use curly brackets.",
    S, "Q2.9", 3)
mcq("F24a-2-10", 4, 31, "Correct program",
    "What does a \"correct\" program mean?",
    ["A program that is well-documented", "A program that compiles without errors",
     "A program that meets its design and user requirements", "A program that has no user interface bugs"], "c",
    "Source Code Quality slide 31: \"A 'correct' program is one that does exactly what its designers and users intend it to do — no more and no less.\"",
    S, "Q2.10", 3)

also("F25b-3A-1", S, "Q3.1", 6)
also("M25a-4A-2", S, "Q3.2", 6)
also("F25b-3A-3", S, "Q3.3", 6)
short("F24a-3-4", 6, 4, "Security dimensions",
      "What are the three key security dimensions?",
      "<b>Confidentiality</b>, <b>Integrity</b>, <b>Availability</b> (CIA).",
      "Security slide 4: confidentiality — information may be disclosed to unauthorized people; integrity — information may be damaged or corrupted; availability — access to the system or its data may not be possible.",
      S, "Q3.4", 6)
short("F24a-3-5", 6, "5, 7", "Application security",
      "What is application security primarily concerned with?",
      "Application security is concerned with the <b>security of individual application systems or related groups of systems</b>. It is a software engineering problem: the system is designed to resist attacks.",
      "Security slide 5 (security levels) and slide 7: \"Application security is a software engineering problem where the system is designed to resist attacks.\"",
      S, "Q3.5", 6)
short("F24a-3-6", 6, "20, 24", "Security risk assessment purpose",
      "What is the purpose of security risk assessment?",
      "To <b>assess the possible losses that might ensue from attacks</b> on the system and <b>balance these losses against the costs of security procedures</b> that may reduce them — so that security decisions are made in a cost-effective way.",
      "Security slide 24: \"Risk assessment and management is concerned with assessing the possible losses that might ensue from attacks on the system and balancing these losses against the costs of security procedures.\" Slide 20: no point spending more than the asset's value.",
      S, "Q3.6", 6)
short("F24a-3-7", 6, 39, "Fail securely",
      "What does 'fail securely' mean in security design?",
      "When systems fail, for whatever reason, ensure that <b>sensitive information cannot be accessed by unauthorized users</b> even though the normal security procedures are unavailable.",
      "Security slide 39, design guideline 3.",
      S, "Q3.7", 6)
short("F24a-3-8", 6, 12, "Threat",
      "What is a 'threat' in security terminology?",
      "<b>Circumstances that have potential to cause loss or harm</b> — you can think of it as a system vulnerability that is subjected to an attack.",
      "Security slide 12 (security terminology).",
      S, "Q3.8", 6)
short("F24a-3-9", 6, 15, "Fabrication threat",
      "What is a 'fabrication threat'?",
      "A threat that allows an attacker to <b>insert false information into a system</b> — e.g. adding false transactions to a banking system that transfer money to the attacker's account.",
      "Security slide 15, threat type 4.",
      S, "Q3.9", 6)
short("F24a-3-10", 6, 44, "Penetration testing",
      "What is 'penetration testing'?",
      "A security validation technique in which <b>a team is established whose goal is to breach the security of the system by simulating attacks</b> on it.",
      "Security slide 44 (security validation): experience-based testing, penetration testing, tool-based analysis, formal verification.",
      S, "Q3.10", 6)

also("F25b-4B-1", S, "Q4 Part 2.1–2", 4)
also("F25b-4B-2", S, "Q4 Part 2.3", 4)
also("F25b-4B-3", S, "Q4 Part 2.4–5", 4)
also("F25b-5", S, "Q5", 7)
