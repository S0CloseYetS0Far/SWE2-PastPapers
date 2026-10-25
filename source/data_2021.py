from qb import *

# ---------------- Final, 1st semester 1443 (Dec 2021) — official model answer ----------------
S = "F21a"
src(S, "Final — 1st Semester 1443 (Dec 2021), official model answer", "Exams/Final/2021/Final2021_ModelAnswer.pdf  (also pages 7–13 of Exams/Final/2023/_Final_2nd_CS392_2023.pdf)")

mcq("F21a-1-1", 8, "", "Code inspection advantages",
    "Which of the following is <b>not</b> one of the code inspection advantages?",
    ["It can check non-functional characteristics of the code", "It can check conformance with a specification",
     "It can check incomplete versions of the code", "It costs less than software testing"], "a",
    "Inspections are static: they can check incomplete code, conformance with the specification and standards, and cost less than testing — but they <b>cannot check non-functional characteristics</b> such as performance or usability (Sommerville ch. 8). Official key: a.",
    S, "Q1.1", 2)
mcq("F21a-1-2", 9, "", "Change management",
    "Which process is concerned with analyzing the costs and benefits of proposed changes?",
    ["System building", "Version management", "Release management", "Change management"], "d",
    "<b>Change management</b> analyses the costs and benefits of proposed changes, approves them, and tracks which components changed. Official key: d. (Configuration management — not in your slides.)",
    S, "Q1.2", 2)
also("F23b-1-2", S, "Q1.3", 2)
mcq("F21a-1-4", 9, "", "Checksums",
    "__________ is a signature on the source code file calculated from the source code text.",
    ["Deltas", "Checksums", "Timestamps", "Change requests"], "b",
    "A <b>checksum</b> is calculated from the file's text, so any change to the text changes the checksum. Official key: b.",
    S, "Q1.4", 2)
mcq("F21a-1-5", 8, "", "Integration testing",
    "In which test level do you focus on possible defects in the interfaces and in the interaction between integrated components?",
    ["Acceptance testing", "Regression testing", "Integration testing", "Unit testing"], "c",
    "<b>Integration testing</b> combines components and tests their interfaces and interactions. Official key: c.",
    S, "Q1.5", 2)
also("M26b-1-5", S, "Q1.6", 2)
mcq("F21a-1-7", 8, "", "Equivalence classes — days",
    "A software accepts days as numbers (1 = Sunday, 2 = Monday, …, 7 = Saturday). Which values would cover all equivalence classes?",
    ["0, 8", "0, 1, 7", "0, 6, 14", "1, 2, 3, 4, 5, 6, 7"], "c",
    "Classes: invalid &lt; 1, valid 1–7, invalid &gt; 7. <b>0, 6, 14</b> takes one value from each class. (0, 8 misses the valid class; 0, 1, 7 misses the &gt; 7 class.) Official key: c.",
    S, "Q1.7", 3)
mcq("F21a-1-8", 8, "", "Boundary values — days",
    "A software accepts days as numbers (1 = Sunday, …, 7 = Saturday). Which values would cover all boundary values?",
    ["0, 8", "0, 1, 7, 8", "0, 6, 14", "1, 2, 3, 4, 5, 6, 7"], "b",
    "The boundaries are 1 and 7: test just outside and on each → <b>0, 1, 7, 8</b>. Official key: b.",
    S, "Q1.8", 3)
mcq("F21a-1-9", 2, 26, "Self-realization needs",
    "As a project manager, you notice that deep knowledge of the system is held by a very small number of team members. The remaining team members are frustrated that they do not understand the system very well. What type of human need (according to the human needs hierarchy) is not met for the majority of the team?",
    ["Physiological needs", "Social needs", "Safety needs", "Self-realization needs"], "d",
    "PM slide 26: self-realization is satisfied by <b>training — people want to learn more</b> — and responsibility. The team can't learn/grow in the system. Official key: d.",
    S, "Q1.9", 3)
mcq("F21a-1-10", 2, "13, 21", "Potential risk",
    "Same scenario (system knowledge held by a few people; the rest are frustrated). As a project manager, what potential risk do you find?",
    ["Poor relationships amongst team members can lead to high staff turnover", "It is impossible to recruit staff with the skills required",
     "The size of the software is underestimated", "There is no risk"], "a",
    "PM slide 21: people-risk indicators are \"poor staff morale; poor relationships amongst team members; high staff turnover\"; slide 9: staff turnover — experienced staff leave before the project is finished. Official key: a.",
    S, "Q1.10", 3)
short("F21a-2", 10, "", "Strategy — universal decompressor",
      "A professor is trying to open emailed homework that students compressed in various formats (zip, tar, jar, rar, etc.) on OSX. OSX has built-in support only for zip, so the professor has to install various command-line tools, which is cumbersome. Design a universal compression tool that can deal with various compression formats.<br>"
      "<b>Which?</b> pattern + intent · <b>Why?</b> · <b>How?</b> class diagram for this case.",
      "<b>Which:</b> <b>Strategy</b> — defines a family of algorithms, encapsulates each one and makes them interchangeable.<br>"
      "<b>Why:</b> we need different decompression behaviours; new formats may be added later, and we want to call a single <code>decompress()</code> method. Strategy gives one unified interface for all formats.<br>"
      "<b>How:</b><pre>FileExplorer ──uses──▶ «interface» Strategy\n  (context)              +decompress(file)\n                             ▲ implements\n              ┌──────────────┼──────────────┐\n            Zip             Rar             Tar   (Jar, …)\n       +decompress()   +decompress()   +decompress()</pre>",
      "Official model answer (Strategy is not one of the three patterns in your OOAD deck).",
      S, "Q2", 4)
short("F21a-3-1", 8, "", "White box or black box?",
      "Decide whether each test design method / test type is white box or black box:<br>Boundary value analysis · Cyclomatic complexity · Acceptance testing · Control flow graph · Code inspection · Equivalence partitioning",
      table(["Method", "Type"], [["Boundary value analysis", "<b>Black box</b>"], ["Cyclomatic complexity", "<b>White box</b>"], ["Acceptance testing", "<b>Black box</b>"],
                                 ["Control flow graph", "<b>White box</b>"], ["Code inspection", "<b>White box</b>"], ["Equivalence partitioning", "<b>Black box</b>"]]),
      "Official model answer: methods that look at the code's structure are white box; methods based only on the specification are black box.",
      S, "Q3.1", 5)
short("F21a-3-2", 8, "", "Cyclomatic complexity — fuel warning",
      "The flow graph represents a program that shows a car's fuel level (check fuel; if low show a yellow warning light; if very low also show a red warning light; then show the litres). It has 6 nodes (A–F) and 7 edges.<br>"
      "1) What is the cyclomatic complexity? 2) Write the independent paths. 3) Write a test case and expected output for each path.",
      "1) V(G) = E − N + 2 = 7 − 6 + 2 = <b>3</b><br>"
      "2) <b>A-B-C-D-E-F</b> · <b>A-B-C-E-F</b> · <b>A-B-F</b><br>"
      "3)" + table(["Test case", "Expected output"], [["5 litres", "Show litres"], ["3 litres", "Show yellow light warning, show litres"], ["1 litre", "Show red light warning, show yellow light warning, show litres"]]),
      "Official model answer.",
      S, "Q3.2", 5, img="F21_cfg.jpg")
short("F21a-4-1", 6, "37, 40", "Security vs usability trade-off",
      "When designing software systems there can be trade-offs: a highly secure system may compromise usability and vice versa. Give an example of a <b>real system you used</b> that compromises between security and usability, state its main functionality, which feature is compromised, and why the compromise is necessary.",
      table(["", ""], [["Software name", "e.g. Al Ahli (SNB) banking app"], ["Functionality", "Mobile banking"], ["Compromised feature", "<b>Usability</b>"],
                       ["Explanation", "Sessions are very short: if the user is idle the app signs out automatically and asks for login + OTP again. This is annoying (less usable) but protects the user's financial information if the phone is left unattended."]]),
      "Security slide 37 (design compromises: security measures may require users to remember information or do extra interactions, making the system less usable) and slide 40 (guideline 4: balance security and usability). Any proper real example is accepted.",
      S, "Q4.1", 6)
short("F21a-4-2", 6, "14, 15", "Misuse case for an online shop",
      "Complete the use case diagram (Customer: Register, Submit review, Order goods; Shop clerk: Prepare order) to include one misuse case, then specify the type of threat of that misuse case.",
      "Add an <b>Outside crook</b> actor with misuse cases linked by <code>&lt;&lt;threaten&gt;&gt;</code>, for example:<ul>"
      "<li><i>Flood system</i> → threatens Order goods → <b>Interruption</b></li><li><i>Steal card info</i> → threatens Order goods → <b>Interception</b></li>"
      "<li><i>Reveal customer info</i> → <b>Interception</b></li><li><i>Get privileges</i> / <i>Spread malicious code</i> → <b>Modification</b></li><li><i>Submit fake reviews</i> → <b>Fabrication</b></li></ul>",
      "Official model answer (answers vary). Security slides 14–15 define the four threat types.",
      S, "Q4.2–3", 6)
also("M22b2-3-1", S, "Q5.1", 7)
mcq("F21a-5-2", 7, "8, 18", "Train protection — critical attribute",
    "A train protection system automatically applies the brakes if the speed limit is exceeded or if the train enters a red-signalled segment. Which dependability attribute is most critical for this system?",
    ["Availability", "Security", "Safety"], "c",
    "It is a critical system — a failure may cause a catastrophic accident and harm people → <b>safety</b> (Dependability slide 8). Official key: c.",
    S, "Q5.2", 7)
mcq("F21a-5-3", 7, 23, "Train protection — reliability metric",
    "Giving reasons, choose a reliability metric that might be used to specify the required reliability for the train protection system:",
    ["POFOD", "ROCOF", "Availability"], "a",
    "Slide 23: POFOD \"should be used as a reliability metric in situations where a failure on request is serious\" — protection systems are called on intermittently and infrequently, and must respond correctly each time. Official key: a.",
    S, "Q5.3", 7)
mcq("F21a-5-4", 7, 25, "Train protection — MTBF",
    "For the past month, the train protection system failed for one hour on three different occasions. What is the Mean Time Between Failures? (MTBF = total operational time / total number of failures)",
    ["240 hours", "0.33 hours", "717 hours", "3 hours"], "a",
    "One month = 30 × 24 = 720 hours → MTBF = 720 / 3 = <b>240 hours</b> (official model answer).",
    S, "Q5.4", 7)

# ---------------- Midterm 1, 1st semester 1443 (Oct 2021) ----------------
S = "M21a"
src(S, "Midterm 1 — 1st Semester 1443 (Oct 2021), official model answer", "Exams/Midterm/2021/Midterm1_Answers.pdf")

mcq("M21a-1-1", 3, 16, "Agile quality management",
    "Quality management in agile development is:",
    ["A document-based process", "A bureaucratic process", "A stage-by-stage process", "An informal process"], "d",
    "Quality slide 16: \"Quality management in agile development is <b>informal</b> rather than document-based.\" Official key: d.",
    S, "Q1.1", 2)
also("M22b1-1-2", S, "Q1.2", 2)
also("M22b1-2c", S, "Q1.3", 2)
mcq("M21a-1-4", 10, "", "Prioritizing use cases",
    "To prioritize the work on use cases we use:",
    ["Class diagram", "Activity diagram", "Traceability matrix", "System sequence diagram"], "c",
    "A traceability matrix links requirements to use cases (with priorities), showing which use cases cover the most important requirements. Official key: c.",
    S, "Q1.4", 2)
mcq("M21a-1-5", 5, 15, "Open/Closed principle",
    "The Open/Closed design principle means:",
    ["A class should have only one reason to change", "A class can be extended but not modified",
     "A class speaks to only friend classes", "Substituting a subclass for a class should preserve correct program behavior"], "b",
    "OOAD slide 15: \"Classes should be open for extension but closed for modification.\" (a = SRP, c = Demeter, d = Liskov.) Official key: b.",
    S, "Q1.5", 2)
mcq("M21a-1-6", 5, 21, "Delegation — Adapter",
    "The __________ design pattern provides delegation of responsibility:",
    ["Adapter", "Singleton", "Observer", "Publisher-Subscriber"], "a",
    "An Adapter <b>delegates</b> each client call to the adaptee object after converting the interface (OOAD slide 21). Official key: a.",
    S, "Q1.6", 2)
TF = [
    (1, 7, 18, "Software safety is equivalent to software reliability.", False,
     "Dependability slide 18: \"Safety and reliability are related but distinct.\" Reliability is about conformance to the specification; safety is about not causing damage, whether or not the system conforms."),
    (2, 3, 2, "Quality standards aren't usually up-to-date.", True,
     "A known problem with standards: they are often out-of-date / not seen as relevant (Sommerville ch. 24). Official key: T."),
    (3, 10, "", "In TDD, we write white-box tests before writing the code.", False,
     "TDD writes unit tests before the code, but they are written against the required behaviour (the code doesn't exist yet), so they are not white-box tests. Official key: F."),
    (4, 5, 13, "System sequence diagrams represent interactions of modules inside the software system.", False,
     "A <b>system</b> sequence diagram treats the system as a black box and shows interactions between the external actors and the system — not the internal modules. Official key: F."),
]
for n, ch, sl, q, a, e in TF:
    tf("M21a-2-%d" % n, ch, sl, "True / False", q, a, e, S, "Q2.%d" % n, 3)
short("M21a-3", 5, "21, 22", "Adapter — document printers",
      "In a document-editing system, Document objects know how to print themselves using a <code>PostscriptPrinter</code> object. There are other types of printers with slightly different interfaces. Use a design pattern to refactor the design so different printers can be easily swapped.<br>"
      "1) Which pattern(s) and why? 2) Draw a design class diagram. 3) What effect did the new design have on the coupling between Document and PostscriptPrinter?",
      "1) <b>Adapter</b> (or Adapter + Strategy) — each printer has a slightly different interface; adapters convert them all to one <code>Printer</code> interface that Document uses, so printers can be swapped without changing Document.<br>"
      "2)<pre>Document ──uses──▶ «interface» Printer\n                     +print(doc)\n                         ▲ implements\n          ┌──────────────┼───────────────┐\n PostscriptAdapter   InkjetAdapter    LaserAdapter\n        │ adaptee        │ adaptee        │ adaptee\n PostscriptPrinter   InkjetPrinter    LaserPrinter</pre>"
      "3) <b>Reduced their coupling</b> — Document now depends only on the Printer interface.",
      "Official model answer: \"Adapter OR Adapter + Strategy\"; coupling: reduced. OOAD slides 21–22.",
      S, "Q3", 3)

# ---------------- Midterm 1, 1st semester 1443 (Dec 2021) ----------------
S = "M21b"
src(S, "Midterm 1 (re-sit) — 1st Semester 1443 (Dec 2021), official model answer", "Exams/Midterm/2021/Midterm1_2021_Answers.pdf")
also("M22a-1-1", S, "Q1.1", 2)
also("M22b1-2b", S, "Q1.2", 2)
also("M22b1-1-1", S, "Q1.3", 2)
also("F23a-1-1", S, "Q1.4", 2)
also("M22a-1-6", S, "Q1.5", 2)
also("M22b1-1-3", S, "Q1.6", 2)
also("M22b1-2a", S, "Q2", 3)
also("M22b1-3-1", S, "Q3.1", 4)
also("M22b1-3-2", S, "Q3.2", 4)

# ---------------- Midterm 2, 1st semester 1443 (2021) ----------------
S = "M21c"
src(S, "Midterm 2 — 1st Semester 1443 (2021), official model answer", "Exams/Midterm/2021/Midterm2_2021_Answers.pdf  (student copy: Exams/Midterm/2021/Midterm2_2021.pdf)")
mcq("M21c-1-1", 6, 4, "Security dimensions",
    "The three main dimensions of security engineering are:",
    ["Confidentiality, Integrity, and Availability", "Competence, Integrity, and Availability", "Confidentiality, Integrity and Reliability", "None of the above"], "a",
    "Security slide 4: <b>Confidentiality, Integrity, Availability</b>. Official key: a.",
    S, "Q1.1", 2)
mcq("M21c-1-2", 7, "14, 16", "Fault tolerant",
    "A software system is fault tolerant if:",
    ["It traps mistakes before they introduce system faults", "It detects errors before the system goes into service",
     "It ensures that system errors do not lead to system failures", "It minimises the possibility of mistakes"], "c",
    "Dependability slide 14: errors do not necessarily lead to failures — they can be corrected by built-in error detection and recovery; slide 16: fault tolerance = continue in operation in spite of faults. Official key: c.",
    S, "Q1.2", 2)
mcq("M21c-1-3", 6, 12, "Asset",
    "Something of value which has to be protected. The ___ may be the software system itself or data used by that system:",
    ["Asset", "Attack", "Control", "Threat"], "a",
    "Security slide 12: <b>Asset</b>. Official key: a.",
    S, "Q1.3", 2)
also("F24b-1-1", S, "Q1.4", 2)
mcq("M21c-1-5", 9, "", "Codeline",
    "In version management systems, which definition best describes a codeline?",
    ["An instance of a configuration item", "A collection of component versions that make up a system",
     "A version of a software system that is distributed to customers", "A sequence of versions of source code with later versions in the sequence derived from earlier versions"], "d",
    "A <b>codeline</b> is a sequence of versions of source code, each derived from the previous. (b = baseline, c = release.) Official key: d.",
    S, "Q1.5", 2)
mcq("M21c-1-6", 7, 6, "Dependability = trust",
    "\"The dependability of a system reflects the user's degree of trust in that system.\"",
    ["True", "False, it is the availability that reflects the user's degree of trust", "False, it is the reliability that reflects the user's degree of trust", "False, it is the security that reflects the user's degree of trust"], "a",
    "Dependability slide 6: \"The dependability of a system reflects the user's degree of trust in that system.\" Official key: a.",
    S, "Q1.6", 2)
short("M21c-2-1", 9, "", "Centralized vs distributed VCS",
      "Provide two differences between distributed and centralized version control systems.",
      table(["Centralized", "Distributed"],
            [["Developers check out components from a single project repository", "Each developer creates a <b>clone</b> of the whole repository"],
             ["Programmers commit their changes to the central copy", "Allows <b>off-line</b> working; commits are local, then pushed"],
             ["The central server is a single point of failure", "Every clone is a backup of the repository"],
             ["Example: Subversion", "Example: Git — essential for open-source development"]]),
      "Official model answer. (Configuration management — not in your slides.)",
      S, "Q2.1", 3)
SYS = [
    ("a", "A protection system monitors a chemical reactor and shuts down the reaction if it is overheating.", 3,
     "Overheating could cause an explosion and harm people → <b>safety</b>. Official key: Safety."),
    ("b", "A university system that keeps track of student records such as transcripts. It handles a large number of transactions regularly throughout the day. You are willing to accept around 10 failures a day.", 2,
     "Failures are tolerated (≈10 a day), but transcripts are confidential records that must not be changed → <b>security</b>. Official key: Security (reliability is also accepted)."),
    ("c", "A system to control a refrigeration unit for home owners' use.", 0,
     "It must keep running to keep food cold; it is not safety-critical → <b>availability</b>. Official key: Availability."),
]
for n, desc, a, e in SYS:
    mcq("M21c-2-2%s" % n, 7, 8, "Most critical dependability attribute",
        "Choose the dependability attribute that is likely to be most critical for this system:<br>" + desc,
        ["Availability", "Reliability", "Security", "Safety"], a, e + " \"Any meaningful justification is accepted; reliability can be chosen for any of the systems.\"", S, "Q2.2" + n, 3)
short("M21c-3-1", 7, 23, "Seatbelt POFOD",
      "POFOD ranges from 0 to 1, and Dependability + POFOD = 1. An automobile manufacturer sets a goal of only 1 failed seatbelt in any of its cars during a 1-million-unit product run, assuming every car were to crash.<br>1) What is the POFOD if there are four seatbelts per car?<br>2) What is the necessary dependability of the seatbelts?",
      "1) 1 million cars × 4 seatbelts = 4,000,000 seatbelts → POFOD = <b>1 / 4,000,000 = 0.00000025</b><br>"
      "2) Dependability = 1 − POFOD = 1 − 1/4,000,000 = <b>0.99999975</b> (99.999975%)",
      "Official model answer. Dependability slide 23: POFOD = failures / demands.",
      S, "Q3.1", 4)
short("M21c-3-2", 7, 26, "Copier availability",
      "A copier is expected to operate for 200 hours after repair, and the mean repair time is expected to be two hours. Determine the availability of the copier.",
      "MTBF = 200 h, MTTR = 2 h → Availability = MTBF / (MTBF + MTTR) = 200 / 202 = <b>0.99</b>",
      "Official model answer. Dependability slide 26: availability = uptime / total time, taking repair time into account.",
      S, "Q3.2", 4)
