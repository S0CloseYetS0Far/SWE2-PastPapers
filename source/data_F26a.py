from qb import *

S = "F26a"
src(S, "Final — 1st Semester 2026", "Exams/Final/2026/Final_1st_2026.pdf")

mcq("F26a-1-1", 3, 16, "Agile quality management",
    "In agile development, how is quality management primarily approached?",
    ["Through extensive documentation", "Through formal audits and compliance checks",
     "Informally, with team responsibility for quality", "By outsourcing quality checks"], "c",
    "Slide 16: \"Quality management in agile development is <b>informal</b> rather than document-based. It relies on establishing a quality culture, where all team members feel responsible for software quality.\"",
    S, "Q1.1", 1)
mcq("F26a-1-2", 3, 11, "Quality attributes",
    "Which of the following is a software quality attribute related to how well the software can be modified?",
    ["Adaptability", "Efficiency", "Usability", "Portability"], "a",
    "Slide 11 lists the quality attributes. <b>Adaptability</b> is how easily the software can be changed/adapted to new requirements. Efficiency is about resource use, usability about ease of use, and portability about moving the software to another platform.",
    S, "Q1.2", 1)
mcq("F26a-1-3", 3, 32, "Fog index",
    "What does the \"Fog Index\" measure in software documentation?",
    ["The number of spelling errors per page", "The average length of words and sentences to determine readability",
     "The amount of technical jargon used in a document", "The visual layout and formatting of a manual"], "b",
    "Slide 32: \"Fog index — a measure of the average length of words and sentences in documents. The higher the value of a document's Fog index, the more difficult the document is to understand.\"",
    S, "Q1.3", 1)
mcq("F26a-1-4", 3, 20, "Pair programming weaknesses",
    "What is a weakness of pair programming?",
    ["It always leads to faster development", "Mutual misunderstandings where both may make the same mistake",
     "It reduces knowledge sharing", "It eliminates all bugs"], "b",
    "Slide 20 (pair programming weaknesses): \"<b>Mutual misunderstandings</b> — both members of a pair may make the same mistake in understanding the system requirements.\" The other weaknesses are pair reputation and working relationships.",
    S, "Q1.4", 1)
mcq("F26a-1-5", 3, "15, 16", "Quality culture",
    "What does a \"quality culture\" emphasize in software development?",
    ["Strict adherence to deadlines only", "Everyone taking responsibility for quality", "Maximizing profits", "Minimizing documentation"], "b",
    "Slide 15: quality managers develop a 'quality culture' \"where everyone responsible for software development is committed to achieving a high level of product quality\". Slide 16: all team members feel responsible for software quality.",
    S, "Q1.5", 1)
mcq("F26a-1-6", 4, 31, "Formally correct program",
    "What is a \"formally correct\" program?",
    ["One that compiles without warnings", "One that follows naming conventions",
     "One whose correctness can be mathematically proved", "One that is fully documented"], "c",
    "Slide 31: \"A 'formally correct' program is one whose correctness can be <b>proved mathematically</b>, at least to a point that designers and users are convinced about its relative absence of errors.\"",
    S, "Q1.6", 1)
mcq("F26a-1-7", 4, 32, "Runtime errors",
    "Which type of errors are detected at \"runtime\" because they cannot be found by the compiler?",
    ["Syntax errors", "Static semantic errors", "Spelling errors in comments", "Dynamic semantic errors and logical errors"], "d",
    "Slide 32: \"Runtime errors: <b>dynamic semantic errors, and logical errors</b>, that cannot be detected by the compiler (debugging).\" Syntax and static semantic errors are compile-time errors.",
    S, "Q1.7", 2)
mcq("F26a-1-8", 4, "14, 15", "Choosing identifiers",
    "What is recommended for choosing identifiers in code structure?",
    ["Use small variations like s1, s2", "Mix CamelCase and underscores freely",
     "Use meaningful names and coherent styles", "Always use non-English keywords"], "c",
    "Slide 14: use <b>meaningful names</b> and avoid small variations like s1, s2. Slide 15: use coherent identifiers — one language, one variable style.",
    S, "Q1.8", 2)
mcq("F26a-1-9", 4, 10, "SRP",
    "According to SRP (Single Responsibility Principle), what should a function do?",
    ["As many things as possible", "One thing only, and do it well", "Whatever the programmer wants", "Only mathematical calculations"], "b",
    "Slide 10: SRP — \"Functions should do one thing. They should do it well. They should do it only.\" (Robert C. Martin)",
    S, "Q1.9", 2)
mcq("F26a-1-10", 4, 15, "Naming style",
    "Regarding variable naming styles (like CamelCase vs. underscores), the slides advise:",
    ["Always use underscores for Java and CamelCase for C", "Use both styles in the same project to show versatility",
     "Never use CamelCase as it is hard for compilers to read", "Use one variable style and stick to it; do not use both"], "d",
    "Slide 15: \"Use one variable style — either CamelCaseIdentifiers or underscores_identifiers, <b>but not both!</b>\"",
    S, "Q1.10", 2)

short("F26a-3-1", 7, "13, 14", "Fault vs failure",
      "What is the difference between a <i>system fault</i> and a <i>system failure</i>?",
      "A <b>system fault</b> is a characteristic of the software (e.g. a bug in the code) that <i>can</i> lead to a system error. "
      "A <b>system failure</b> is an <i>event</i> that occurs at some point in time when the system does not deliver a service as expected by its users.<br>"
      "A fault does not necessarily cause a failure (the faulty code may never run, or the error may be corrected).",
      "Slide 13 (reliability terminology) defines fault, error and failure; slide 14: faults do not necessarily result in errors, and errors do not necessarily lead to failures.",
      S, "Q3 Part 1.1", 3)
short("F26a-3-2", 7, 24, "ROCOF calculation",
      "Calculate the ROCOF of a system that experiences 12 failures during 240 hours of operation.",
      "ROCOF = failures / operating time = 12 / 240 = <b>0.05 failures per hour</b> (5 failures per 100 hours).",
      "Slide 24: ROCOF is the probable number of failures over a period of time — \"ROCOF of 0.02 means that 2 failures are likely per 100 time units\".",
      S, "Q3 Part 1.2", 3)
short("F26a-3-3", 7, 25, "Comparing MTBF",
      "If system X has an MTBF = 250 hours, and system Y has an MTBF = 200 hours, which system is more reliable? Justify your answer by calculating how many failures occur in 1,000 hours for each system.",
      "Failures in 1,000 h: X = 1000 / 250 = <b>4 failures</b>; Y = 1000 / 200 = <b>5 failures</b>.<br>"
      "<b>System X is more reliable</b> — it has a longer average time between failures, so fewer failures in the same period.",
      "Slide 25: MTBF measures the average length of time between observed failures; a longer MTBF means fewer failures. Number of failures = operating time / MTBF.",
      S, "Q3 Part 1.3", 3)
short("F26a-3-4", 7, 3, "Cost of failures",
      "Software failures are costly. Mention two of the software failure cost impacts.",
      "Any two of: <b>Financial</b>, <b>Time</b>, <b>Lives</b>, <b>Reputation</b>.",
      "Slide 3 (Cost of software failures): \"Cost of software application failures impact: Financial, Time, Lives, Reputation.\"",
      S, "Q3 Part 1.4", 3)
short("F26a-3-5", 6, "4, 14, 16, 24, 40", "Match security terms",
      "Choose the correct security engineering term for each description.<br>"
      "<b>Terms:</b> Confidentiality · Integrity · Operational Security · Security Risk Assessment · Attack Detection and Elimination · "
      "Vulnerability Avoidance · Exposure Limitation and Recovery · Interception Threat · Modification Threat · Infrastructure Security · Security Design Guidelines"
      + ol(["Evaluating the possible losses that might result from attacks on the system",
            "Balance security and usability where sometimes weaker security is accepted to make the system more usable",
            "Designing the system so that security weaknesses do not occur",
            "When an attacker gains unauthorized access to assets",
            "Consequences and damage after a successful attack are minimised",
            "Ensuring that information remains accurate and unaltered"]),
      ol(["<b>Security Risk Assessment</b>", "<b>Security Design Guidelines</b>", "<b>Vulnerability Avoidance</b>",
          "<b>Interception Threat</b>", "<b>Exposure Limitation and Recovery</b>", "<b>Integrity</b>"]),
      "1 → slide 24: risk assessment is \"assessing the possible losses that might ensue from attacks on the system\". "
      "2 → slide 40, design guideline 4 \"Balance security and usability\". "
      "3, 5 → slide 16 (security assurance): vulnerability avoidance / exposure limitation and recovery. "
      "4 → slide 14: interception threats allow an attacker to gain access to an asset. "
      "6 → slide 4: integrity — information must not be damaged or corrupted.",
      S, "Q3 Part 2", 4)

short("F26a-4-1", 8, "", "CFG, cyclomatic complexity, basis paths",
      "Given the pseudocode:<pre>System.out.println(\"Welcome\");\ndo {\n   System.out.print(\"Enter your rank, or 4 to Exit \");\n   a = scanner.nextInt();\n   switch (a) {\n      case 1: System.out.println(\"Gold Medal\");   break;\n      case 2: System.out.println(\"Silver Medal\"); break;\n      case 3: System.out.println(\"Bronze Medal\"); break;\n   }\n} while (a != 4);\nSystem.out.println(\"Good Luck\");</pre>"
      "1) Draw a control flow graph. 2) Calculate the cyclomatic complexity. 3) List the basic path set.",
      "<b>Nodes:</b> 1 = print Welcome · 2 = prompt, read a, switch(a) · 3 = Gold · 4 = Silver · 5 = Bronze · 6 = while (a != 4) · 7 = Good Luck<br>"
      "<b>Edges (10):</b> 1→2, 2→3, 2→4, 2→5, 2→6 (no case matches), 3→6, 4→6, 5→6, 6→2 (loop), 6→7<br>"
      "<b>V(G)</b> = E − N + 2 = 10 − 7 + 2 = <b>5</b> (check: 4 decisions — 3 extra switch branches + the while — plus 1).<br>"
      "<b>Basis paths:</b><br>1) 1-2-6-7 (input 4)<br>2) 1-2-3-6-2-6-7 (input 1, then 4)<br>3) 1-2-4-6-2-6-7 (input 2, then 4)<br>4) 1-2-5-6-2-6-7 (input 3, then 4)<br>5) 1-2-6-2-6-7 (input 5, then 4)",
      "This is a software-testing question (no deck in your slides folder). Cyclomatic complexity V(G) = E − N + 2 = number of decisions + 1; each basis path adds at least one new edge.",
      S, "Q4 Part 1", 5)
short("F26a-4-2", 8, "", "Equivalence partitions and BVA",
      "A method checkPass() accepts values between 60 and 100 inclusive [60 … 100].<br>a) Identify the equivalence partitions.<br>b) Using Boundary Value Analysis, list the values to be tested.",
      "a) Three partitions: <b>invalid &lt; 60</b> (e.g. 30) · <b>valid 60–100</b> (e.g. 80) · <b>invalid &gt; 100</b> (e.g. 120).<br>"
      "b) Test at and around each boundary: <b>59, 60, 61, 99, 100, 101</b> (minimum set: 59, 60, 100, 101).",
      "Software-testing question (no deck in your slides). Equivalence partitioning picks one value per class; boundary value analysis tests the edges of each class.",
      S, "Q4 Part 2.1", 6)
short("F26a-4-3", 8, "", "Automated testing advantages",
      "Mention two advantages of Automated Testing.",
      "Any two: tests run <b>faster</b> and can be <b>re-run cheaply</b> after every change (regression testing); results are <b>consistent/repeatable</b> with fewer human errors; tests are <b>reusable</b>; more tests can be run, increasing coverage.",
      "Software-testing question (no deck in your slides).",
      S, "Q4 Part 2.2", 6)
short("F26a-5", 9, "", "Evolution vs servicing vs refactoring",
      "Complete the table using only <b>Yes</b> or <b>No</b>:"
      + table(["", "Can involve major changes?", "Can add new functionality?", "Can modify/repair functionality?", "Aims to make system easier to maintain?", "Preventive maintenance?"],
              [["Evolution", "Yes", "Yes", "Yes", "No", "No"], ["Servicing", "No", "", "", "", ""], ["Phase-out", "", "", "", "", ""],
               ["Maintenance", "", "", "", "", ""], ["Re-engineering", "", "", "", "", ""], ["Refactoring", "", "", "", "", ""]]),
      table(["", "Major changes", "New functionality", "Modify/repair", "Easier to maintain", "Preventive"],
            [["Evolution", "Yes", "Yes", "Yes", "No", "No"],
             ["Servicing", "No", "No", "Yes", "No", "No"],
             ["Phase-out", "No", "No", "No", "No", "No"],
             ["Maintenance", "Yes", "Yes", "Yes", "No", "No"],
             ["Re-engineering", "Yes", "No", "No", "Yes", "Yes"],
             ["Refactoring", "No", "No", "No", "Yes", "Yes"]]),
      "Software evolution has no deck in your slides; the answer follows Sommerville ch. 9. <b>Servicing</b> only makes small changes and repairs (no new functionality). In <b>phase-out</b> the software is still used but no further changes are made. "
      "<b>Re-engineering</b> restructures/rewrites the system without changing its functionality to make it easier to maintain — your Intro slide 9 lists \"Preventive — re-engineering, make system more maintainable\". "
      "<b>Refactoring</b> is small continuous improvement that slows degradation — Sommerville calls it \"preventative maintenance\". The Maintenance row is the general term (corrective, adaptive, perfective changes).",
      S, "Q5", 6, nb="Related slide: Introduction slide 9 (maintenance types — preventive = re-engineering)")
