from qb import *

S = "M25b"
src(S, "Midterm — 2nd Semester 2025", "Exams/Midterm/2025/Midterm_2nd_2025.pdf")

also("M25a-1-1", S, "Q1.1", 1)
also("M25a-1-4", S, "Q1.2", 1)
mcq("M25b-1-3", 2, 27, "Personality types",
    "In a project team, which personality type is the one where work is a means to an end, which is the achievement of individual goals?",
    ["Task-oriented", "Self-oriented", "Interaction-oriented", "Team-oriented"], "b",
    "PM slide 27: \"<b>Self-oriented</b> — the work is a means to an end which is the achievement of individual goals, e.g. to get rich, to play tennis, to travel.\"",
    S, "Q1.3", 1)
mcq("M25b-1-4", 3, 32, "Fog index",
    "__________ is a measure of the average length of words and sentences in documents.",
    ["Length of identifiers", "Fog index", "Cyclomatic complexity", "Fan-in"], "b",
    "Quality slide 32: \"<b>Fog index</b> — a measure of the average length of words and sentences in documents.\"",
    S, "Q1.4", 1)
mcq("M25b-1-5", 2, 13, "Risk types",
    "It is considered as __________ when it is difficult to recruit staff with the skills required.",
    ["Technology risks", "Organisational risks", "Requirements risks", "People risks"], "d",
    "PM slide 13: <b>People</b> risks — \"It is impossible to recruit staff with the skills required\", key staff are ill, required training not available.",
    S, "Q1.5", 1)
mcq("M25b-1-6", 2, 12, "Risk identification checklist",
    "Which is <b>not</b> a common risk type used to identify project risk?",
    ["Technology risks", "Adaptive risks", "Requirements risks", "Estimation risks"], "b",
    "PM slide 12: the checklist of common risks is technology, people, organisational, requirements and estimation risks (slide 13 adds tools). There is no 'adaptive' risk type.",
    S, "Q1.6", 1)
mcq("M25b-1-7", 2, 18, "Strategy for financial problems",
    "What should a manager do when organizational financial problems appear?",
    ["Alert customer to potential difficulties and the possibility of delays",
     "Reorganize team so that there is more overlap of work and people",
     "Replace potentially defective components with bought-in components of known reliability",
     "Prepare a briefing document for senior management showing how the project is making a very important contribution to the goals of the business and presenting reasons why cuts to the project budget would not be cost-effective"], "d",
    "PM slide 18: Organizational financial problems → prepare a briefing document for senior management. (A = recruitment problems, B = staff illness, C = defective components.)",
    S, "Q1.7", 1)
mcq("M25b-1-8", 2, 17, "Minimisation strategy",
    "Which of the following is a risk minimization strategy?",
    ["Ignoring the risk until it happens", "Increasing the project scope", "Reducing the effect of the risk on the product", "Changing the project team members"], "c",
    "PM slide 17: \"<b>Minimisation strategies</b> — the impact of the risk on the project or product will be reduced.\"",
    S, "Q1.8", 1)
mcq("M25b-1-9", 2, 21, "Risk indicators",
    "What is a common indicator of organizational risks in a project?",
    ["Poor relationships among team members", "Lack of action by senior management", "Inefficient database performance", "Inability to recruit skilled staff"], "b",
    "PM slide 21 (risk indicators): Organizational — \"organizational gossip; <b>lack of action by senior management</b>\". Poor relationships is a <i>people</i> indicator.",
    S, "Q1.9", 2)
also("M25a-1-10", S, "Q1.10", 2)

TF = [
    (1, "At the project level, quality management involves applying specific quality processes and checking that these planned processes are followed.", True, 3,
     "Slide 3: \"At the project level, quality management involves the application of specific quality processes and checking that these planned processes have been followed.\""),
    (2, "The quality team should become independent of the development team so that they can take an objective view of the software.", True, 4,
     "Slide 4: the quality team should be independent so they can take an objective view of the software."),
    (3, "A quality plan sets out the desired product qualities and how these are assessed, and there is no need to set up organizational standards.", False, 6,
     "Slide 6: the quality plan \"should set out <b>which organizational standards should be applied</b> and, where necessary, define new standards.\""),
    (4, "A software is fit for purpose if it is properly tested, sufficiently dependable, and has acceptable performance for normal use.", True, 9,
     "Slide 9 (software fitness for purpose): properly tested? sufficiently dependable? acceptable performance for normal use? usable? well-structured?"),
    (5, "The quality of a developed product is completely separate from the quality of the production process.", False, 13,
     "Slide 13: \"The quality of a developed product is <b>influenced by</b> the quality of the production process.\""),
    (6, "One of the major problems with software standards is that they usually involve too much official form filling.", True, "",
     "Not on your slides — Sommerville ch. 24 (problems with standards): standards \"often involve too much bureaucratic form filling\" and may not be seen as relevant by engineers."),
    (7, "Process standards apply to the software product being developed, including document standards and coding standards.", False, "",
     "Those are <b>product standards</b> (document standards, coding standards). Process standards define the processes to be followed during development (Sommerville ch. 24 — not on your slides)."),
    (8, "It is possible for any system to be optimized for all of the quality attributes.", False, 12,
     "Slide 12: \"It is not possible for any system to be optimized for all of these attributes.\""),
    (9, "'Never break the build' means team members should not check in code that causes the system to fail.", True, 17,
     "Slide 17: \"Never break the build — team members should not check in code that causes the system to fail.\""),
    (10, "Pair reputation is considered a weakness since pairs may be reluctant to look for errors because they do not want to slow down the progress of the project.", True, 20,
     "Slide 20: \"Pair reputation — pairs may be reluctant to look for errors because they do not want to slow down the progress of the project.\""),
]
for n, q, a, sl, e in TF:
    tf("M25b-2-%d" % n, 3, sl, "Quality management T/F", q, a, e, S, "Q2.%d" % n, 3)

short("M25b-3A-1", 4, 6, "Clean code",
      "What is clean code?",
      "Clean code is code that is <b>readable, simple and direct</b>; compact and literate; contains only what is necessary; makes it easy for other developers to enhance it; has clean tests; contains no duplicates; is built on tiny abstractions; and gives fast productivity during maintenance.",
      "Source Code Quality slide 6 (What is clean code after all?).",
      S, "Q3 Part A.1", 4)
short("M25b-3A-2", 4, 10, "SRP",
      "What is SRP: Single Responsibility Principle?",
      "\"<b>Functions should do one thing. They should do it well. They should do it only.</b>\" — a function/class should have one responsibility (one and only one reason to change).",
      "Source Code Quality slide 10 (Robert C. Martin); OOAD slide 15: a class should have one and only one reason to change.",
      S, "Q3 Part A.2", 4)
short("M25b-3B", 4, "12–16, 20–23, 27–29", "Refactor for readability",
      "The following code snippet is supposed to check the age of a user. Refactor the code snippet to make it more readable by using code quality practices.<pre>static void checkA(int A) {\nif (A &lt; 18) {\nSystem.out.println(\"Access denied - You are not old enough!\");\n} else\n{System.out.println(\"Access granted - You are old enough!\");\n}\n}</pre>",
      "<pre>/**\n * Checks whether a user is old enough to get access.\n * @param userAge  the user's age in years (must be &gt;= 0)\n */\nstatic void checkUserAge(int userAge) {\n    final int MINIMUM_AGE = 18;\n    if (userAge &lt; MINIMUM_AGE) {\n        System.out.println(\"Access denied - You are not old enough!\");\n    } else {\n        System.out.println(\"Access granted - You are old enough!\");\n    }\n}</pre>",
      "Meaningful identifiers (verb for the method, noun for the variable), no magic numbers, one brace style with consistent indentation (slides 12–18), explicit curly brackets (slides 20–23), and JavaDoc documentation (slides 27–29).",
      S, "Q3 Part B", 5)

short("M25b-4A-1", 7, 4, "Causes of failure",
      "What are the three main causes of failure?",
      "1) <b>Hardware failure</b> — design/manufacturing errors or components reaching the end of their life.<br>2) <b>Software failure</b> — errors in specification, design or implementation.<br>3) <b>Operational failure</b> — human operators make mistakes (now perhaps the largest single cause).",
      "Dependability slide 4 (Causes of failure).",
      S, "Q4 Part A.1", 6)
short("M25b-4A-2", 7, "8, 26", "Availability definition",
      "What is the definition of availability?",
      "Availability is <b>the probability that the system will be up and running and able to deliver useful services to users</b> at a given time (availability = uptime / total time).",
      "Dependability slide 8 (principal properties) and slide 26 (uptime / total time; takes repair and restart time into account).",
      S, "Q4 Part A.2", 6)
also("M25a-4A-2", S, "Q4 Part A.3", 6)
short("M25b-4B", 7, "23, 24, 26, 31", "POFOD, ROCOF, availability",
      "Your system processes 12,000 requests per week. During testing, it failed on 18 requests (12 due to system crashes and 6 due to incorrect outputs). The average repair time after a system crash is 5 minutes.<br>1) Calculate the POFOD.<br>2) Calculate the ROCOF in minutes.<br>3) Calculate the Availability for the system.",
      "1) POFOD = 18 / 12000 = <b>0.0015</b><br>"
      "2) One week = 7 × 24 × 60 = 10,080 minutes → ROCOF = 18 / 10080 = <b>0.0018 failures per minute</b><br>"
      "3) Downtime = 12 crashes × 5 min = 60 min → Availability = (10080 − 60) / 10080 = <b>0.994</b> (≈ 99.4%)",
      "Slides 23–24: POFOD = failures / requests, ROCOF = failures / time. Slide 26: availability = uptime / total time — only crashes cause downtime (same method as the slide 31 activity).",
      S, "Q4 Part B", 6)

X = "F25x"
src(X, "Extra question bundled with the solved Final 2025 (2nd semester)", "Exams/Final/2025/Final_2nd_2025_sol.pdf")
short("F25x-4", 7, "23, 24, 26, 30–32", "Does the system meet the spec?",
      "A critical medical image processing system processes 5,000 MRI scans per day. During a week of operation, the system encountered failures in 25 scans: 10 were due to hardware malfunctions and 15 were due to software errors. The average time to restore the system after hardware malfunctions is 8 minutes.<br>"
      "The customer's quality specification expects software availability above 97% and ROCOF per hour lower than 6%.<br>"
      "A) Does the system meet the customer quality specification and why?<br>B) Calculate: 1) POFOD 2) ROCOF in faults per hour 3) Availability.",
      "1) Requests in a week = 5000 × 7 = 35,000 → POFOD = 25 / 35000 = <b>0.00071</b><br>"
      "2) One week = 7 × 24 = 168 hours → ROCOF = 25 / 168 = <b>0.149 faults per hour (≈ 14.9%)</b><br>"
      "3) Downtime = 10 hardware failures × 8 min = 80 min; one week = 10,080 min → Availability = (10080 − 80) / 10080 = <b>0.992 (99.2%)</b><br>"
      "A) <b>No.</b> Availability (99.2%) is above 97%, but ROCOF (14.9% per hour) is far above the 6% limit — so the system does not meet the specification.",
      "Same method as the Dependability slides 30–32 activity: compute ROCOF over the operating time, POFOD over the requests, availability from downtime; the product ships only if <i>every</i> requirement is met (slide 32: \"Availability/POFOD are good, but ROCOF is too low\").",
      X, "Q4", 9)
