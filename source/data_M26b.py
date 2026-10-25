from qb import *

S = "M26b"
src(S, "Midterm — 2nd Semester 2026", "Exams/Midterm/2026/Midterm/SWE2_Midterm_2nd.pdf")

mcq("M26b-1-1", 1, 9, "Maintenance types",
    "What type of maintenance involves fixing uncovered defects?",
    ["Adaptive", "Perfective", "Corrective", "Preventive"], "c",
    "Slide 9: \"Corrective — fix uncovered defect; Adaptive — platform change; Enhancement — perfective, additional functionality; Preventive — re-engineering, make system more maintainable.\"",
    S, "Q1.1", 1)
mcq("M26b-1-2", 1, 11, "Iterative model",
    "Which process model is described as \"develop increasingly more complex versions of the software\"?",
    ["Waterfall", "Prototyping", "Iterative model", "Spiral model"], "c",
    "Slide 11 (Software evolution): \"<b>Iterative model</b> — Develop increasingly more complex versions of the software.\"",
    S, "Q1.2", 1)
mcq("M26b-1-3", 1, 12, "Evolutionary process models",
    "Which of the following is categorized as an \"Evolutionary Process Model\"?",
    ["Waterfall", "Spiral Model", "Prototyping Model", "Rapid Application Development"], "b",
    "Slide 12: Evolutionary process models = Incremental, <b>Spiral</b>, Component Assembly, Concurrent Development. Waterfall, Prototyping and RAD are listed as <i>classical</i> process models.",
    S, "Q1.3", 1)
mcq("M26b-1-4", 2, 17, "Risk planning strategies",
    "Which risk management strategy aims to reduce the probability that a risk will arise?",
    ["Avoidance strategies", "Minimization strategies", "Contingency plans", "Acceptance strategies"], "a",
    "Slide 17: \"<b>Avoidance strategies</b> — the probability that the risk will arise is reduced; Minimisation strategies — the impact of the risk is reduced; Contingency plans — plans to deal with the risk if it arises.\"",
    S, "Q1.4", 1)
mcq("M26b-1-5", 2, 27, "Personality types",
    "A personality type motivated primarily by the work itself is referred to as:",
    ["Self-oriented", "Interaction-oriented", "Goal-oriented", "Task-oriented"], "d",
    "Slide 27: \"<b>Task-oriented</b> — the motivation for doing the work is the work itself.\" Self-oriented = work is a means to personal goals; interaction-oriented = motivated by co-workers.",
    S, "Q1.5", 1)
mcq("M26b-1-6", 2, 30, "Group cohesiveness",
    "What is a key advantage of a \"cohesive\" group in teamwork?",
    ["Knowledge is shared among members", "The group is more expensive to maintain",
     "Members work independently of group goals", "It requires a strictly hierarchical structure"], "a",
    "Slide 30 (advantages of a cohesive group): group quality standards, team members learn from each other, <b>knowledge is shared</b> (continuity if a member leaves), refactoring and continual improvement are encouraged.",
    S, "Q1.6", 1)
mcq("M26b-1-7", 1, 15, "Quality = fitness for use",
    "According to the quality perspective, software quality is defined as:",
    ["Zero defects", "Fitness for use", "Maximum performance", "Lowest cost"], "b",
    "Introduction slide 15: \"Quality == '<b>fitness for use</b>'\".",
    S, "Q1.7", 1)
mcq("M26b-1-8", 2, 23, "People management factors",
    "Which people management factor states that all team members should be treated in a comparable way without favorites or discrimination?",
    ["Respect", "Inclusion", "Consistency", "Honesty"], "c",
    "Slide 23: \"<b>Consistency</b> — team members should all be treated in a comparable way without favourites or discrimination.\"",
    S, "Q1.8", 2)
mcq("M26b-1-9", 2, 10, "Risk management process order",
    "What is the correct order of the risk management process?",
    ["Planning → Identification → Monitoring → Analysis", "Identification → Analysis → Planning → Monitoring",
     "Analysis → Identification → Planning → Monitoring", "Identification → Planning → Analysis → Monitoring"], "b",
    "Slide 10: 1- Risk identification, 2- Risk analysis, 3- Risk planning, 4- Risk monitoring.",
    S, "Q1.9", 2)
mcq("M26b-1-10", 2, 8, "Risk categories",
    "A risk that affects the quality or performance of the software is called a:",
    ["Project risk", "Product risk", "Business risk", "Technical risk"], "b",
    "Slide 8: project risks affect schedule or resources; <b>product risks affect the quality or performance</b> of the software; business risks affect the organisation.",
    S, "Q1.10", 2)

TF = [
    (1, "The quality team should be independent from the development team to take an objective view of the software.", True, 4,
     "Slide 4: \"The quality team should be independent from the development team so that they can take an objective view of the software.\""),
    (2, "A quality plan should be long and detailed to cover all possible scenarios.", False, 7,
     "Slide 7: \"Quality plans should be <b>short, succinct</b> documents. If they are too long, no-one will read them.\""),
    (3, "It is possible for a software system to be optimized for all quality attributes simultaneously (e.g., robustness and performance).", False, 12,
     "Slide 12: \"It is <b>not</b> possible for any system to be optimized for all of these attributes — for example, improving robustness may lead to loss of performance.\""),
    (4, "Quality managers should aim to develop a 'quality culture' where everyone is committed to achieving high product quality.", True, 15,
     "Slide 15: quality managers should develop a 'quality culture' where everyone responsible for software development is committed to achieving a high level of product quality."),
    (5, "Dynamic software metrics are collected by making measurements while a program is in execution.", True, 29,
     "Slide 29: \"Dynamic metrics which are collected by measurements made of a program <b>in execution</b>.\""),
    (6, "Pair programming ensures that code is constantly reviewed, but it can still lead to mutual misunderstandings of system requirements.", True, "19, 20",
     "Slide 19: code is constantly examined and reviewed by another team member. Slide 20: weakness — mutual misunderstandings."),
    (7, "A high \"Fog index\" indicates that a document is written in a way that is very simple and easy for most people to understand.", False, 32,
     "Slide 32: \"The <b>higher</b> the value of a document's Fog index, the <b>more difficult</b> the document is to understand.\""),
    (8, "One weakness of pair programming is that both members may share the same misunderstanding of system requirements.", True, 20,
     "Slide 20: \"Mutual misunderstandings — both members of a pair may make the same mistake in understanding the system requirements.\""),
    (9, "Static metrics, such as cyclomatic complexity, have a direct and easily measured relationship with quality attributes like maintainability.", False, 30,
     "Slide 30: \"Static metrics have an <b>indirect</b> relationship with quality attributes.\" It is dynamic metrics that are closely related to quality attributes."),
    (10, "Generally, the larger the size of a code component, the more complex and error-prone it is likely to be.", True, 31,
     "Slide 31 (Length of code): \"Generally, the larger the size of the code of a component, the more complex and error-prone that component is likely to be.\""),
]
for n, q, a, sl, e in TF:
    tf("M26b-2-%d" % n, 3, sl, "Quality management T/F", q, a, e, S, "Q2.%d" % n, 3)

short("M26b-3A-1", 5, 15, "SOLID principles",
      "Mention three principles of the SOLID design principles.",
      "Any three of: <b>S</b>ingle Responsibility Principle · <b>O</b>pen/Closed Principle · <b>L</b>iskov Substitution Principle · <b>I</b>njection of Dependency · <b>D</b>emeter Principle.",
      "Slide 15 (OO Design Principles — SOLID): SRP — a class should have one and only one reason to change; OCP — open for extension, closed for modification; LSP — substituting a subclass should preserve correct behaviour; Injection of Dependency; Demeter — speak only to your friends.",
      S, "Q3 Part A.1", 4)
short("M26b-3A-2", 5, 22, "Adapter drawback",
      "The <i>Adapter</i> design pattern converts the interface of a class into another interface clients expect. However, this might have a negative/bad effect. What is this bad effect?",
      "<b>The overall complexity of the code increases</b> (you add new interfaces and adapter classes).",
      "Slide 22 lists the Adapter pros (SRP, Open/Closed) and the con: \"The overall complexity of the code increases.\"",
      S, "Q3 Part A.2", 4)
short("M26b-3B", 4, "12–16, 23, 27–29", "Refactor for readability",
      "The following code is intended to compute and return the area of a rectangle using its length and width. Refactor the code to improve its readability by applying good coding practices of <b>code structure</b> and <b>code documentation</b>.<pre>int f(int l,int w)\nint r=l*w;\nreturn r;</pre>",
      "<pre>/**\n * Computes the area of a rectangle.\n * @param length  the rectangle's length (must be &gt;= 0)\n * @param width   the rectangle's width (must be &gt;= 0)\n * @return        the area (length * width)\n */\nint computeRectangleArea(int length, int width) {\n    int area = length * width;\n    return area;\n}</pre>",
      "Code structure: meaningful identifiers — the function name is a verb, variables are nouns, one naming style (slides 12–16); be explicit with curly brackets and consistent indentation (slide 23). "
      "Documentation: use a standard such as JavaDoc describing what the code does, its parameters, restrictions and return value (slides 27–29).",
      S, "Q3 Part B", 4)

short("M26b-4A-1", 7, "7, 8", "Principal dependability properties",
      "Mention four of the five principal dependability properties/attributes.",
      "Any four of: <b>Availability</b>, <b>Reliability</b>, <b>Safety</b>, <b>Security</b>, <b>Resilience</b>.",
      "Slide 7 shows the principal dependability properties diagram; slide 8 defines availability, reliability, safety and security. Resilience is the fifth property in the diagram (Sommerville ch. 10).",
      S, "Q4 Part A.1", 5)
short("M26b-4A-2", 7, "13, 14", "Fault → error → failure",
      "What is the relation between System Fault, System Error, and System Failure?",
      "A human <b>mistake</b> introduces a <b>fault</b> (a characteristic of the software, e.g. buggy code). When the faulty code executes it can produce a <b>system error</b> (an erroneous system state). If the error is not corrected it can lead to a <b>system failure</b> (the system does not deliver the expected service).<br>"
      "<b>Fault → Error → Failure</b> — but faults do not necessarily cause errors, and errors do not necessarily cause failures.",
      "Slide 13 (reliability terminology) and slide 14: \"Failures are usually a result of system errors that are derived from faults in the system. However, faults do not necessarily result in system errors … Errors do not necessarily lead to system failures.\"",
      S, "Q4 Part A.2", 5)
short("M26b-4B", 7, "23, 24, 26, 31", "POFOD, ROCOF, availability",
      "An online shopping system processes 3,000 orders per day. During operation, the system experienced 12 failures (7 caused by system shutdowns and 5 due to incorrect order processing). On average, it takes 8 minutes to recover from each failure.<br>1) Calculate the POFOD.<br>2) Calculate the ROCOF per minute.<br>3) Calculate the Availability of the system.",
      "1) POFOD = failures / requests = 12 / 3000 = <b>0.004</b><br>"
      "2) One day = 24 × 60 = 1440 minutes → ROCOF = 12 / 1440 = <b>0.0083 failures per minute</b><br>"
      "3) Only the 7 shutdowns make the system unavailable: downtime = 7 × 8 = 56 min.<br>Availability = (1440 − 56) / 1440 = <b>0.961</b> (≈ 96.1%)<br>"
      "<i>If your instructor counts all 12 failures as downtime: (1440 − 96) / 1440 = 0.933.</i>",
      "Slide 23: POFOD = failures / requests. Slide 24: ROCOF = failures over a period of time. Slide 26: availability = uptime / total time, and it \"does not tend to take incorrect computations (partial failures) into account\" — the same approach as the slide 31 activity, where only the system crashes (37 × 2 min) count as downtime.",
      S, "Q4 Part B", 5)
