from qb import *

S = "M24a"
src(S, "Midterm — 1st Semester 2024", "Exams/Midterm/2024/Midterm-1st-2024.pdf")

mcq("M24a-1-1", 2, "3, 4", "Project management concern",
    "What is the primary concern of software project management?",
    ["Hardware development", "Ensuring software is delivered on time and within budget", "Designing user interfaces", "Testing software performance"], "b",
    "PM slide 3: ensuring that software is delivered on time and on schedule; slide 4 success criteria: deliver at the agreed time and keep overall costs within budget.",
    S, "Q1.1", 1)
mcq("M24a-1-2", 2, 5, "Software management distinctions",
    "Why is software project management different from traditional project management?",
    ["Software is intangible and cannot be seen", "Software is cheaper to produce", "Software projects are always identical", "Software is always developed by large teams"], "a",
    "PM slide 5: \"The product is <b>intangible</b>. Software cannot be seen or touched. Software project managers cannot see progress by simply looking at the artefact.\"",
    S, "Q1.2", 1)
also("M25a-1-4", S, "Q1.3", 1)
mcq("M24a-1-4", 2, 18, "Strategy for staff illness",
    "What should a manager do when a staff member is ill at critical times?",
    ["Ignore the problem", "Increase project scope", "Reorganize the team for overlapping tasks", "Hire a consultant"], "c",
    "PM slide 18: \"Staff illness — Reorganize team so that there is more overlap of work and people therefore understand each other's jobs.\"",
    S, "Q1.4", 1)
also("M26b-1-5", S, "Q1.5", 1)
mcq("M24a-1-6", 3, 31, "Fan-in",
    "What is FAN-IN a measure of?",
    ["The number of functions that call another function", "The number of bugs in a system", "The number of classes in a program", "The number of code lines written"], "a",
    "Quality slide 31: \"Fan-in is a measure of the number of functions or methods that call another function or method (say X).\" Fan-out is the number of functions called by X.",
    S, "Q1.6", 1)
mcq("M24a-1-7", 2, 21, "Risk indicators",
    "Which is a potential indicator of technology risk?",
    ["Low staff morale", "Organizational restructuring", "Late hardware delivery", "Customer complaints"], "c",
    "PM slide 21: Technology indicators — \"<b>late delivery of hardware</b> or support software; many reported technology problems.\" Low morale = people; customer complaints = requirements.",
    S, "Q1.7", 2)
also("M25b-1-9", S, "Q1.8", 2)
also("M25b-1-8", S, "Q1.9", 2)
mcq("M24a-1-10", 2, "29, 30", "Team cohesiveness",
    "Why is team cohesiveness important in software development?",
    ["It allows individuals to focus solely on their personal goals", "It improves group performance and encourages collective problem solving",
     "It enables managers to control every detail of the project", "It ensures tasks are distributed unevenly"], "b",
    "PM slide 29: a good group is cohesive and has team spirit; group interaction is a key determinant of group performance. Slide 30: members work collectively to deliver high quality results and fix problems.",
    S, "Q1.10", 2)

TF = [
    (1, "Quality management provides a dependent check on the software development process based on the project deliverables.", False, 4,
     "Quality slide 4: quality management provides an <b>independent</b> check on the software development process."),
    (2, "The quality team should become a part of the development team so that they can take an objective view of the software.", False, 4,
     "Slide 4: the quality team should be <b>independent from</b> the development team to take an objective view."),
    (3, "A software is fit for purpose if it is properly tested, sufficiently dependable, well-structured, and has acceptable performance for normal use.", True, 9,
     "Slide 9 (software fitness for purpose) lists exactly these questions."),
    (4, "Process standards are applied to the software product being developed, which include document standards, such as the structure of requirements documents.", False, "",
     "Standards applied to the <b>product</b> (document structure, coding standards) are <b>product standards</b>; process standards define how development is carried out. (Sommerville ch. 24 — not on your slides.)"),
    (7, "The agile community is deeply supportive of the bureaucratic overheads of standards-based approaches because it improves quality processes.", False, 16,
     "Slide 16: \"The agile community is fundamentally <b>opposed</b> to what it sees as the bureaucratic overheads of standards-based approaches.\""),
    (8, "'Check before check-in' means team members should not check in code that causes the system to fail.", False, 17,
     "Slide 17: that describes <b>never break the build</b>. 'Check before check-in' means programmers organise their own code reviews with other team members before checking code in."),
    (9, "Pair programming leads to a profound knowledge of a program, as both programmers have to understand the program to continue development.", True, 19,
     "Slide 19: \"Pair programming leads to a deep knowledge of a program, as both programmers have to understand the program in detail to continue development.\""),
    (10, "The review process in agile software development is usually informal.", True, 18,
     "Slide 18: \"The review process in agile software development is usually informal.\""),
]
for n, q, a, sl, e in TF:
    tf("M24a-2-%d" % n, 3, sl, "Quality management T/F", q, a, e, S, "Q2.%d" % n, 3)
also("M25b-2-6", S, "Q2.5", 3)
also("F25b-1-4", S, "Q2.6", 3)

short("M24a-3A-1", 4, 8, "Purpose of code review",
      "What is the primary purpose of code review?",
      "Code review (careful, systematic study of code by people who are not its author) has two purposes: <b>improving the code</b> and <b>improving the programmer</b>.",
      "Source Code Quality slide 8.",
      S, "Q3 Part A.1", 4)
short("M24a-3A-2", 4, 32, "Compile-time errors",
      "What type of errors can be caught during compile time?",
      "<b>Syntax errors</b> and <b>static semantic errors</b> — these are reported by the compiler. (Dynamic semantic and logical errors appear only at runtime.)",
      "Source Code Quality slide 32: \"Compile time errors: syntax errors and static semantic errors indicated by the compiler.\"",
      S, "Q3 Part A.2", 4)
short("M24a-3A-3", 4, "4, 7, 27", "Why documentation matters",
      "Why is code documentation important?",
      "Maintenance is the most expensive part of the software lifetime, and we don't know who will change the code later. Documentation explains <b>what the code does, its parameters, return values, input restrictions and exceptions</b>, so other developers can understand, use and maintain it without having to reverse-engineer it.",
      "Source Code Quality slide 4 (documentation should exist, follow standards and document), slide 7 (why: maintenance is most expensive) and slide 27 (what to include).",
      S, "Q3 Part A.3", 4)
short("M24a-3A-4", 4, 10, "Boy Scout rule",
      "What is the \"Boy Scout Rule\" in clean coding?",
      "\"<b>Leave the campground cleaner than you found it</b>\" — every time you touch code, leave it a little cleaner (better names, less duplication) than it was.",
      "Source Code Quality slide 10 (Some clean code principles).",
      S, "Q3 Part A.4", 4)
short("M24a-3B", 4, "12–16, 23, 27–29", "Refactor longest-string code",
      "The following code snippet is supposed to find the length of the longest string from a string array. Refactor the code snippet to make it more readable by using code quality practices.<pre>int x(string g[]){\nstring p = g[0];\nint o = p.length();\nfor (int z=1;z&lt;g.length; z++)\nif (g[z].length()&gt;o) {\np = g[z];\no = p.length();\n}\nreturn o;\n}</pre>",
      "<pre>/**\n * Given an array of strings, computes the length of the longest string.\n * This method will not work for empty lists.\n * @param list  the list of strings to be processed\n * @return      the size of the longest string in the array\n */\nint longestStringLength(string list[]) {\n    string maxString = list[0];\n    int maxSize = maxString.length();\n    for (int i = 1; i &lt; list.length; i++) {\n        if (list[i].length() &gt; maxSize) {\n            maxString = list[i];\n            maxSize = maxString.length();\n        }\n    }\n    return maxSize;\n}</pre>",
      "This is the exact example from Source Code Quality slides 12–13 (meaningful identifiers), 17 (indentation), 23 (curly brackets) and 29 (JavaDoc).",
      S, "Q3 Part B", 4)

short("M24a-4A", 7, 13, "Fault, error, failure with examples",
      "What is the difference among system fault, system error, and system failure? Give examples for your answer.",
      "<b>System fault</b> — a characteristic of the software that can lead to an error. <i>Example: code that adds 1 hour to the last transmission time without checking if the time is ≥ 23:00.</i><br>"
      "<b>System error</b> — an erroneous system state that can lead to unexpected behaviour. <i>Example: the transmission time is set to 24:XX instead of 00:XX.</i><br>"
      "<b>System failure</b> — an event where the system does not deliver a service as users expect. <i>Example: no weather data is transmitted because the time is invalid.</i>",
      "Dependability slide 13 (reliability terminology — the wilderness weather station example).",
      S, "Q4 A", 5)
short("M24a-4B", 7, "23–26, 30–32", "Is the product ready to ship?",
      "Your customers want an availability of at least 99%, a POFOD of less than 0.1, and a ROCOF of less than 2 failures per 8-hour work period.<br>"
      "After testing your code for 10 full days, 1500 requests were made. The product failed 70 times (45 system crashes, 25 bad calculations) and it took an average of 2 minutes to restart after each failure.<br>"
      "1) Calculate the availability. 2) Calculate POFOD. 3) Calculate ROCOF. 4) Can we calculate MTBF? 5) Is the product ready to ship, and why?",
      "10 days = 240 h = 14,400 min.<br>"
      "1) Downtime = 45 crashes × 2 min = 90 min → Availability = (14400 − 90) / 14400 = <b>0.994</b> (99.4%)<br>"
      "2) POFOD = 70 / 1500 = <b>0.047</b><br>"
      "3) ROCOF = 70 / 240 h = 0.29 per hour = <b>2.33 failures per 8-hour period</b><br>"
      "4) <b>No</b> — we need the timestamp of each failure; we only know the average restart time.<br>"
      "5) <b>No.</b> Availability (99.4%) and POFOD (0.047) are good, but ROCOF (2.33 per 8 h) is above the required 2.",
      "Identical method to the Dependability slides 30–32 activity (64 failures in 7 days, 37 crashes × 2 min, \"No — need timestamps\", \"ROCOF is too low\").",
      S, "Q4 B", 5)
