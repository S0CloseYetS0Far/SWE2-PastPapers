from qb import *

S = "F23b"
src(S, "Final — 2nd Semester 2023", "Exams/Final/2023/Final_2nd_CS392_2023.pdf  (also pages 1–6 of Exams/Final/2023/_Final_2nd_CS392_2023.pdf)")

mcq("F23b-1-1", 4, 10, "Clean code principles",
    "Which of the following is <b>not</b> one of the clean code principles?",
    ["Rule of thumb", "Boy Scout rule", "Don't Repeat Yourself", "Single Responsibility Principle"], "a",
    "Source Code Quality slide 10 lists the clean code principles: <b>Boy Scout rule</b>, <b>DRY</b> and <b>SRP</b>. \"Rule of thumb\" is not one of them.",
    S, "Q1.1", 1)
mcq("F23b-1-2", 6, 28, "Security requirement classification",
    "When requirements set out how the system should be designed so that it can recover from and restore system assets after some loss has occurred, it is called:",
    ["Risk avoidance", "Risk mitigation", "Risk detection", "Risk prevention"], "b",
    "Security slide 28: \"<b>Risk mitigation</b> requirements set out how the system should be designed so that it can recover from and restore system assets after some loss has occurred.\" Avoidance = risks cannot arise; detection = identify and neutralise the risk before losses occur.",
    S, "Q1.2", 1)
also("M24c-1-3", S, "Q1.3", 1)
mcq("F23b-1-4", 6, 12, "Vulnerability",
    "__________ is a weakness in a computer-based system that may be exploited to cause loss or harm.",
    ["Asset", "Attack", "Control", "Vulnerability"], "d",
    "Security slide 12: \"<b>Vulnerability</b> — a weakness in a computer-based system that may be exploited to cause loss or harm.\"",
    S, "Q1.4", 1)
mcq("F23b-1-5", 5, "26, 27", "Broker pattern / middleware",
    "The __________ is an architectural pattern used to structure distributed software systems with components that interact by remote method calls.",
    ["Strategy pattern", "Broker pattern", "Repository pattern", "Publisher-Subscriber pattern"], "b",
    "The <b>Broker</b> pattern puts a middleware broker between distributed components that coordinates remote method calls (e.g. CORBA, Java RMI). OOAD slide 27: middleware offers services related to object communication so that extraneous functionality is offloaded to it.",
    S, "Q1.5", 1)
mcq("F23b-1-6", 4, 15, "Coherent identifiers",
    "To use coherent identifiers in an attempt to clean up your code means:",
    ["Choosing one variable style for one language, such as CamelCase identifiers", "Choosing meaningful variables", "Choosing proper data structure", "Choosing proper indentation"], "a",
    "Source Code Quality slide 15 (Use coherent identifiers): choose one language and <b>one variable style</b> — either CamelCase or underscores, but not both.",
    S, "Q1.6", 3)
mcq("F23b-1-7", 7, "7, 8", "Principal dependability properties",
    "Principal dependability properties are:",
    ["Usability, Portability, Reliability and Resilience", "Safety, Security, Complexity and Reliability",
     "Availability, Safety, Security and Reliability", "Availability, Reliability, Usability and Complexity"], "c",
    "Dependability slide 8 (principal properties): <b>Availability, Reliability, Safety, Security</b> (resilience is the fifth on slide 7).",
    S, "Q1.7", 3)
mcq("F23b-1-8", 5, 7, "Supporting actor",
    "The actor that passively participates in the use case is called a(n):",
    ["Onstage actor", "Offstage actor", "Supporting actor", "Initiating actor"], "c",
    "A <b>supporting</b> (participating/secondary) actor takes part in a use case started by someone else — e.g. a payment service. The initiating (primary) actor starts it. OOAD slide 7 defines actors as external entities that interact with the system.",
    S, "Q1.8", 3)

short("F23b-2-1", 5, "20–25", "Match pattern to situation",
      "Match the design pattern to the situation where you should apply it (a pattern can be used for more than one system; each system has one pattern).<br><b>Patterns:</b> 1 Singleton · 2 Façade · 3 Observer · 4 Adapter · 5 Strategy"
      + ol(["Sending an SMS message requires lots of big ugly code, involving connection, message and other objects.",
            "An app developed in the USA returns the top speed of luxury cars in miles per hour (MPH). Now we need to use the same app for clients in Saudi Arabia who want the same results but in kilometres per hour (km/h).",
            "A shared single washing machine among all the residents in a hotel.",
            "Each YouTuber has many subscribers on their channel. Each subscriber wants to watch their subscribed channel's videos."]),
      ol(["<b>Façade</b> — one simple <code>sendSMS()</code> interface hides the complex connection/message subsystem.",
          "<b>Adapter</b> — converts the MPH interface into the km/h interface the Saudi clients expect.",
          "<b>Singleton</b> — only one instance exists and everyone shares it.",
          "<b>Observer</b> — subscribers are notified when the channel publishes a new video."]),
      "OOAD slide 25: Singleton — a class of which only a single instance can exist; Adapter — match interfaces of different classes; Façade — a single class that represents an entire subsystem. Observer (publish/subscribe) is not in your deck.",
      S, "Q2.1", 2)
short("F23b-2-2", 5, 15, "Law of Demeter — installDoor",
      "Consider the method installDoor() from the Contractor class:<pre>class Contractor {\n  installDoor() {\n    subcontractor  = YellowPages.getSubcontractor();\n    carpenter      = subcontractor.getCarpenter();\n    doorHandle     = carpenter.getDoorHandle();\n    doorBody       = carpenter.getDoorBody();\n    screws         = carpenter.getScrews();\n    door           = carpenter.assemble(doorHandle, doorBody, screws);\n    securityExpert = subcontractor.getSecurityExpert();\n    securityExpert.installDoorSensors(door);\n  }\n}</pre>"
      "1) Evaluate the quality of the code (write two problems).<br>2) What major design flaw is evident? Which design principle(s) are violated? Specify one design issue and suggest a solution.",
      "1) Problems: <b>no documentation</b> of what the method does; variables are never declared/typed; the method <b>does too much</b> (finds the subcontractor, gathers parts, assembles, installs sensors); it depends on a global <code>YellowPages</code> class.<br>"
      "2) <b>Violates the Law of Demeter</b> (\"speak only to your friends; treat your friends' friends as strangers\"): Contractor reaches through the subcontractor to the carpenter and security expert and manipulates their parts — <b>long communication chains and high coupling</b>. It also violates <b>SRP</b> and <b>Injection of Dependency</b> (it looks up its own subcontractor).<br>"
      "<b>Solution:</b> tell, don't ask — delegate the work: <code>subcontractor.installDoor()</code>, where the subcontractor asks its carpenter to <code>buildDoor()</code> and its security expert to install sensors. Inject the subcontractor into Contractor instead of fetching it from YellowPages.",
      "OOAD slide 15: Demeter principle, SRP and Injection of Dependency; Source Code Quality slides 26–27 (documentation).",
      S, "Q2.2", 2)

SYS = [
    ("i", "A digital calculator", ["Security", "Safety", "Reliability"], 2,
     "A calculator must give <b>correct results</b> — it holds no secrets and cannot harm anyone → reliability (slide 8)."),
    ("ii", "An Internet-based personal finance management system", ["Availability", "Security", "Safety"], 1,
     "It stores sensitive financial data and is exposed on the Internet → <b>security</b> (slide 8; Security slide 10: networked systems need security)."),
    ("iii", "A system to control a refrigeration unit for home owners' use", ["Security", "Safety", "Availability"], 2,
     "It must keep running to keep the food cold; it is not safety-critical → <b>availability</b> (the Midterm 2 2021 model answer gives the same: refrigeration unit → availability)."),
    ("iv", "A roller-coaster at a theme park", ["Availability", "Security", "Safety"], 2,
     "A failure could injure or kill riders → <b>safety</b> (slide 8: how likely the system will cause damage to people)."),
]
for n, desc, opts, a, e in SYS:
    mcq("F23b-3a-%s" % n, 7, 8, "Most critical dependability attribute",
        "Which dependability attribute is the most critical for this system?<br>" + desc, opts, a, e, S, "Q3 a.%s" % n, 4)
short("F23b-3b", 7, "13, 16, 17", "Match term to example",
      "Match each term with the most appropriate example."
      + table(["Term", "Example"],
              [["1. Human error", "You got an oil temperature warning in your car."],
               ["2. System failure", "A train protection system automatically applies the brakes of a train if the speed limit for a segment of track is exceeded."],
               ["3. Fault detection", "Loss of service in your system."],
               ["4. Fault tolerance", "A car driver forgetting to set the park brake in his car."]]),
      table(["Term", "Example"],
            [["Human error", "<b>A car driver forgetting to set the park brake</b>"],
             ["System failure", "<b>Loss of service in your system</b>"],
             ["Fault detection", "<b>Oil temperature warning in your car</b>"],
             ["Fault tolerance", "<b>Train protection system automatically applies the brakes</b> (the system protects itself and keeps operating safely when a dangerous condition occurs)"]]),
      "Dependability slide 13: human error = human behaviour that introduces faults; slide 15: loss of service is a type of system failure; slides 16–17: fault detection discovers problems, fault tolerance keeps the system operating in spite of faults.",
      S, "Q3 b", 5)
short("F23b-3c", 7, "23–26", "MTBF, availability, POFOD, ROCOF",
      "An operating system (OS) was tested for 30 days. 4165 requests were made and it crashed on average once in 30 days and had 91 wrong results in total. When a system crash occurs, the Mean Time To Repair (MTTR) is 12 hours. Calculate MTBF, availability, POFOD and ROCOF.",
      "30 days = 720 hours; failures = 1 crash + 91 wrong results = 92.<br>"
      "<b>MTBF</b> = 720 / 1 crash = <b>720 hours</b> (time between crashes)<br>"
      "<b>Availability</b> = MTBF / (MTBF + MTTR) = 720 / 732 = <b>0.984</b> (or (720 − 12) / 720 = 0.983)<br>"
      "<b>POFOD</b> = 92 / 4165 = <b>0.022 failures/request</b><br>"
      "<b>ROCOF</b> = 92 / 720 = <b>0.128 failures/hour</b>",
      "Slide 23: POFOD = failures / requests; slide 24: ROCOF = failures / time; slide 25: MTBF = time between failures; slide 26: availability = uptime / total time (MTBF / (MTBF + MTTR), as in the Midterm 2 2021 model answer). Only the crash makes the system unavailable.",
      S, "Q3 c", 5)
short("F23b-4-1", 6, 26, "Security vs safety specification",
      "Security specification has something in common with safety requirements specification — in both cases your concern is to avoid something bad happening — but they are not the same. Provide two major differences.",
      "Any two:<ol><li>Safety problems are <b>accidental</b> — the software is not in a hostile environment. In security you must assume <b>attackers know the system's weaknesses</b>.</li>"
      "<li>After a safety failure you can look for the root cause; after a deliberate attack <b>the attacker may conceal the cause</b>.</li>"
      "<li><b>Shutting down</b> a system can avoid a safety-related failure, but causing a shutdown may be <b>the aim of an attack</b>.</li>"
      "<li>Safety events are not generated by an intelligent adversary; an <b>attacker can probe defences over time</b> to discover weaknesses.</li></ol>",
      "Security slide 26 (Security specification — four major differences).",
      S, "Q4 i", 6)
short("F23b-4-2", 6, "14, 15", "Misuse case threat types",
      "In the misuse case diagram (Customer and Operator use cases; misuser <b>Crook</b> with misuse cases <i>Flood system</i>, <i>Steal card info</i>, <i>Tap communication</i>, <i>Obtain password</i>), specify the type of threat of two of the misuse cases.",
      "<b>Flood system</b> → <b>Interruption</b> (denial of service makes the system unavailable)<br>"
      "<b>Steal card info</b> → <b>Interception</b> (gains access to an asset)<br>"
      "<b>Tap communication</b> → <b>Interception</b><br>"
      "<b>Obtain password</b> → <b>Interception</b> (which can then lead to modification or fabrication)",
      "Security slides 14–15: interception = gain access to an asset; interruption = make part of the system unavailable; modification = tamper with an asset; fabrication = insert false information.",
      S, "Q4 ii", 6, img="F23b_misuse.jpg")
