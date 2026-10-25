from qb import *

S = "M25a"
src(S, "Midterm — 1st Semester 2025", "Exams/Midterm/2025/Midterm_1st_2025.pdf")

mcq("M25a-1-1", 1, 12, "Evolutionary process models",
    "__________ is considered as an Evolutionary Process Model.",
    ["Waterfall Model", "Prototyping Model", "Incremental Model", "Rapid Application Development"], "c",
    "Intro slide 12: Evolutionary process models = <b>Incremental</b>, Spiral, Component Assembly, Concurrent Development. Waterfall, Prototyping and RAD are classical process models.",
    S, "Q1.1", 1)
mcq("M25a-1-2", 1, 9, "Maintenance types",
    "Which type of software maintenance focuses on fixing defects that have been discovered after the software has been released?",
    ["Corrective maintenance", "Adaptive maintenance", "Preventive maintenance", "Enhancement maintenance"], "a",
    "Intro slide 9: \"<b>Corrective</b> — fix uncovered defect.\" Adaptive = platform change, enhancement = perfective/additional functionality, preventive = re-engineering.",
    S, "Q1.2", 1)
mcq("M25a-1-3", 2, 6, "Management activities",
    "Which management activity involves estimating, scheduling project development, and assigning people to tasks?",
    ["Project planning", "Reporting", "Risk management", "People management"], "a",
    "PM slide 6: \"<b>Project planning</b> — project managers are responsible for planning, estimating and scheduling project development and assigning people to tasks.\"",
    S, "Q1.3", 1)
mcq("M25a-1-4", 2, "10, 17", "Risk planning",
    "Which stage of risk management involves developing a strategy to minimize risk effects?",
    ["Risk analysis", "Risk identification", "Risk planning", "Risk monitoring"], "c",
    "PM slide 10: \"<b>Risk planning</b> — draw up plans to avoid or minimise the effects of the risk.\" Slide 17: consider each risk and develop a strategy to manage it.",
    S, "Q1.4", 1)
mcq("M25a-1-5", 2, 8, "Definition of risk",
    "What best defines a <u>risk</u> in the context of risk management in software development?",
    ["A confirmed issue that must be resolved in the project", "A known defect in the software design or code",
     "A probability that some adverse circumstance will occur", "An unexpected change in project requirements"], "c",
    "PM slide 8: \"A risk is a <b>probability that some adverse circumstance will occur</b>.\"",
    S, "Q1.5", 1)
mcq("M25a-1-6", 2, 18, "Strategy for staff illness",
    "As part of risk management, what should a manager do when a team member becomes ill and is unable to continue working on the project?",
    ["Alert the customer to potential delays in delivery", "Reorganize the team so that there is more overlap of work and people",
     "Reduce the project requirements to fit the smaller team", "Request additional funding to hire a backup resource"], "b",
    "PM slide 18 (strategies): \"<b>Staff illness</b> — Reorganize team so that there is more overlap of work and people therefore understand each other's jobs.\" (Option A is the strategy for recruitment problems.)",
    S, "Q1.6", 1)
mcq("M25a-1-7", 3, 4, "Independent quality team",
    "Why should the quality team be independent from the development team?",
    ["To work faster than the development team", "To take an objective view without being influenced by development issues",
     "To share development resources and experiences", "To focus on coding new software features"], "b",
    "Quality slide 4: \"The quality team should be independent from the development team so that they can take an <b>objective view</b> of the software. This allows them to report on software quality without being influenced by software development issues.\"",
    S, "Q1.7", 1)
mcq("M25a-1-8", 2, 26, "Self-realization needs",
    "How can managers support self-realization needs in software teams?",
    ["Offer health insurance", "Offer appropriate rewards", "Offer social networking", "Offer training to learn"], "d",
    "PM slide 26 (need satisfaction): Social — communal facilities, informal communication; Esteem — recognition, appropriate rewards; <b>Self-realization — training (people want to learn more), responsibility</b>.",
    S, "Q1.8", 2)
mcq("M25a-1-9", 3, "29, 30", "Measuring complexity",
    "How can we measure properties such as complexity in software?",
    ["By running the software and measuring response time", "By reviewing the requirements document of the software",
     "By measuring the speed of the system during execution", "By using static metrics that analyze the software code"], "d",
    "Quality slide 29: \"<b>Static metrics</b> help assess complexity, understandability and maintainability.\" Dynamic metrics (measured during execution) assess efficiency and reliability.",
    S, "Q1.9", 2)
mcq("M25a-1-10", 2, 23, "People management factors",
    "Which people management factor involves treating the team members in a comparable way without favourites?",
    ["Consistency", "Respect", "Inclusion", "Honesty"], "a",
    "PM slide 23: \"<b>Consistency</b> — team members should all be treated in a comparable way without favourites or discrimination.\"",
    S, "Q1.10", 2)

TF = [
    (1, "A quality plan sets out the desired product qualities and how these are assessed.", True, 6,
     "Slide 6: \"A quality plan sets out the desired product qualities and how these are assessed and defines the most significant quality attributes.\""),
    (2, "Improving one quality attribute, like robustness, may reduce another, such as performance.", True, 12,
     "Slide 12 (quality conflicts): \"improving robustness may lead to loss of performance.\""),
    (3, "Quality plans should be long and detailed documents.", False, 7,
     "Slide 7: quality plans should be <b>short, succinct</b> documents — if they are too long, no-one will read them."),
    (4, "Customer quality requirements are the same as developer quality requirements in software systems.", False, 8,
     "Slide 8: \"There is a <b>tension</b> between customer quality requirements (efficiency, reliability, etc.) and developer quality requirements (maintainability, reusability, etc.).\""),
    (5, "When a large system is being developed, agile approaches to quality management may be impractical.", True, 21,
     "Slide 21: \"When a large system is being developed for an external customer, agile approaches to quality management with minimal documentation may be impractical.\""),
    (6, "If the software's functionality is not what is expected, then users will work around this and find other ways to do what they want to do.", True, 10,
     "Slide 10: \"if the software's functionality is not what is expected, then users will often just work around this and find other ways to do what they want to do.\""),
    (7, "Software measurement is concerned with deriving a numeric value for an attribute of a software.", True, 22,
     "Slide 22: \"Software measurement is concerned with deriving a numeric value for an attribute of a software product or process.\""),
    (8, "Quality management in agile development is informal rather than document-based.", True, 16,
     "Slide 16: \"Quality management in agile development is informal rather than document-based.\""),
    (9, "One of the uses of software measurements is to identify the system time and budget.", False, 25,
     "Slide 25 gives the two uses of measurement: to <b>assign a value to system quality attributes</b> and to <b>identify system components whose quality is sub-standard</b>. Time and budget are not mentioned."),
    (10, "Length of code is a measure of the average length of words and sentences in documents.", False, "31, 32",
     "That is the <b>Fog index</b> (slide 32). Length of code (slide 31) measures the size of a program."),
]
for n, q, a, sl, e in TF:
    tf("M25a-2-%d" % n, 3, sl, "Quality management T/F", q, a, e, S, "Q2.%d" % n, 2)

short("M25a-3A-1", 5, "19, 25", "OO design patterns",
      "Mention two patterns of the OO design patterns.",
      "Any two of: <b>Singleton</b> (only one instance of a class can exist), <b>Adapter</b> (match interfaces of different classes), <b>Façade</b> (a single class that represents an entire subsystem).",
      "OOAD slide 19: \"Three Design Patterns: Singleton, Adapter, Façade\"; slide 25 summarises each.",
      S, "Q3 Part A.1", 3)
short("M25a-3A-2", 5, 15, "Open/Closed principle",
      "What is the Open/Closed OO design principle?",
      "Classes should be <b>open for extension but closed for modification</b> — you add new behaviour by extending (e.g. subclassing or new implementations) without changing existing, tested code.",
      "OOAD slide 15 (SOLID): \"Open/Closed Principle — Classes should be open for extension but closed for modification.\"",
      S, "Q3 Part A.2", 3)
short("M25a-3B", 4, "12–16, 23, 27–29", "Refactor for readability",
      "The following code snippet is supposed to calculate and return a person's age based on their birth year. Refactor the code snippet to make it more readable by using code quality practices.<pre>int fun(int y)\nint a = 2025 - y;\nreturn a;</pre>",
      "<pre>/**\n * Calculates a person's age from their birth year.\n * @param birthYear  the year the person was born (must not be after currentYear)\n * @return           the person's age in years\n */\nint calculateAge(int birthYear) {\n    final int CURRENT_YEAR = 2025;\n    int age = CURRENT_YEAR - birthYear;\n    return age;\n}</pre>",
      "Code structure: meaningful identifiers (verb for the function name, nouns for variables), avoid magic numbers, one naming style, explicit curly brackets and indentation (slides 12–17, 23). Documentation: a JavaDoc comment stating what the code does, its parameter, restrictions and return value (slides 27–29).",
      S, "Q3 Part B", 3)

short("M25a-4A-1", 7, 7, "Principal dependability properties",
      "Mention four of the five principal dependability properties/attributes.",
      "Any four of: <b>Availability</b>, <b>Reliability</b>, <b>Safety</b>, <b>Security</b>, <b>Resilience</b>.",
      "Dependability slide 7 (principal dependability properties diagram).",
      S, "Q4 Part A.1", 4)
short("M25a-4A-2", 7, 16, "Fault tolerance",
      "What is the meaning of fault tolerance?",
      "Fault tolerance means that the <b>system can continue in operation in spite of software failure</b> (faults). It is required where there are high availability requirements or where failure costs are very high.",
      "Dependability slide 16: \"Fault tolerance means that the system can continue in operation in spite of software failure.\"",
      S, "Q4 Part A.2", 4)
short("M25a-4B", 7, "23, 24, 26, 31", "POFOD, ROCOF, availability",
      "A banking application handles 2,500 transactions per day. While the system gets into operation, it recorded 8 total failures (5 caused by unexpected shutdowns and 3 due to incorrect processing results). On average, it takes 10 minutes to restart after a shutdown.<br>1) Calculate the POFOD.<br>2) Calculate the ROCOF in minutes.<br>3) Calculate the Availability of the system.",
      "1) POFOD = 8 / 2500 = <b>0.0032</b><br>"
      "2) One day = 1440 minutes → ROCOF = 8 / 1440 = <b>0.0056 failures per minute</b><br>"
      "3) Downtime = 5 shutdowns × 10 min = 50 min → Availability = (1440 − 50) / 1440 = <b>0.965</b> (≈ 96.5%)",
      "Slide 23: POFOD = failures / requests. Slide 24: ROCOF = failures / time. Slide 26: availability = uptime / total time; only the shutdowns make the system unavailable (incorrect results are partial failures, as in the slide 31 activity).",
      S, "Q4 Part B", 4)
