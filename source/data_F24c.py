from qb import *

S = "F24c"
src(S, "Final — 3rd Semester 2024", "Exams/Final/2024/final_3nd_2024.pdf")

mcq("F24c-1-1", 7, 4, "Causes of failure",
    "When human operators make mistakes in using the software system, we consider this failure as:",
    ["Hardware failure", "Operational failure", "Software failure", "None of the above"], "b",
    "Dependability slide 4: \"<b>Operational failure</b> — human operators make mistakes. Now perhaps the largest single cause of system failures.\"",
    S, "Q1.1", 7)
mcq("F24c-1-2", 10, "", "Model checking limitation",
    "One major limitation of model checking is:",
    ["The verification occurs too late in the process", "It cannot guarantee the absence of bugs",
     "Difficult to scale when software grows", "Very weak debugging capabilities"], "c",
    "Model checking explores every reachable state, so the state space explodes as the software grows — it is hard to <b>scale</b>. It is used early (on models) and gives counter-examples that help debugging. (Not in your slide decks.)",
    S, "Q1.2", 7)
mcq("F24c-1-3", 10, "", "TDD cycle",
    "The Test-Driven Development cycle elements are:",
    ["Red, green, blue", "Red, green, refactor", "Write a test, make a test pass, refactor", "Both b and c"], "d",
    "TDD cycle: <b>Red</b> — write a failing test; <b>Green</b> — write code to make the test pass; <b>Refactor</b> — clean up the code. Options b and c describe the same cycle. (TDD is only referenced as a reading on Source Code Quality slide 35.)",
    S, "Q1.3", 7)
mcq("F24c-1-4", 6, 44, "Penetration testing",
    "Which of the following best describes the process of actively attempting to gain unauthorized access to a system or network in order to identify and exploit vulnerabilities?",
    ["Penetration testing", "Regression testing", "Load testing", "Structural testing"], "a",
    "Security slide 44: \"<b>Penetration testing</b> — a team is established whose goal is to breach the security of the system by simulating attacks on the system.\"",
    S, "Q1.4", 7)
mcq("F24c-1-5", 4, 33, "When to apply formal methods",
    "When should formal methods be applied in the development process?",
    ["Only at the end, after the system is fully implemented", "Throughout the development lifecycle, in parallel with testing",
     "During the early stages of design and specification", "When the system is released to the customers"], "c",
    "Source Code Quality slide 33: formal methods are applied to software requirements analysis (UML) and validation — they are most cost-effective in the <b>early stages of specification and design</b>, where they find errors before code is written.",
    S, "Q1.5", 7)
mcq("F24c-1-6", 7, 8, "Most important dependability factor",
    "A restaurant has a beeping device at each table that customers use to know when their orders are ready. Which dependability factor is most important?",
    ["Availability", "Safety", "Scalability", "Security"], "a",
    "The device just has to be up and able to deliver its service (beep) whenever an order is ready → <b>availability</b> (Dependability slide 8). It cannot harm people (safety) and holds no sensitive data (security); scalability is not a dependability property.",
    S, "Q1.6", 7)
mcq("F24c-1-7", 5, "20, 25", "Choosing a design pattern",
    "A web application needs to manage user login sessions across multiple devices. Users can stay logged in on one device. If a user logs in from a different device, they are automatically logged out from the previous device. Which design pattern would be most appropriate to implement this user session management functionality?",
    ["Singleton Pattern", "Factory Pattern", "Observer Pattern", "Adapter Pattern"], "a",
    "Only <b>one</b> active session may exist per user, managed by a single session manager — the Singleton pattern \"restricts creation of more than one object\" (OOAD slides 20, 25). Adapter only converts interfaces.",
    S, "Q1.7", 6)

short("F24c-2", 9, "", "Evolution & security fill-in",
      "Fill each blank with the most appropriate term (no duplication).<br><b>Terms:</b> Fail safe · Refactoring · Boy scout rule · Re-engineering · Application-level protection · Phase-out · Model checking · Servicing · Marshalling"
      + ol(["______ is a continuous process of improvement throughout the development and evolution process, while ______ takes place after a system has been maintained for some time and maintenance costs are increasing, especially for legacy systems.",
            "In software maintenance, ______ means the software remains useful but the only changes made are those required to keep it operational, while ______ means that the software may still be used but no further changes are made to it.",
            "______ is a specific protection mechanism built into the application itself, e.g. additional password protection.",
            "______ is a formal method for verifying an abstract representation of a system using a finite state machine."]),
      ol(["<b>Refactoring</b> … <b>Re-engineering</b>", "<b>Servicing</b> … <b>Phase-out</b>", "<b>Application-level protection</b>", "<b>Model checking</b>"]),
      "Refactoring vs re-engineering and servicing vs phase-out come from software evolution (Sommerville ch. 9 — no deck in your slides). Application-level protection: Security slide 6. Model checking uses a finite-state model of the system (formal verification).",
      S, "Q2", 6)

short("F24c-3-1", 8, "", "Cyclomatic complexity from a graph",
      "The following flow graph represents a program. Edges: 1→2, 1→6, 2→3, 2→4, 3→5, 4→5, 5→6, 6→7.<br>a) What is the cyclomatic complexity?<br>b) Write down the independent paths that should cover the test.",
      "a) E = 8, N = 7 → V(G) = 8 − 7 + 2 = <b>3</b> (2 decision nodes, 1 and 2, + 1)<br>"
      "b) <b>1-6-7</b> · <b>1-2-3-5-6-7</b> · <b>1-2-4-5-6-7</b>",
      "Software-testing question (no deck in your slides). V(G) = E − N + 2.",
      S, "Q3.1", 5, img="F24c_cfg.jpg")
short("F24c-3-2", 8, "", "Speeding fine — EP and BVA",
      "The system calculates the fine for speeding:<ul><li>1–10 km/h over the limit: 100 SAR</li><li>11–20 km/h over: 200 SAR</li><li>21–30 km/h over: 300 SAR</li><li>more than 30 km/h over: 400 SAR</li></ul>a) How many equivalence classes could be identified?<br>b) Write down all boundary values.",
      "a) <b>5 classes:</b> not speeding (≤ 0) · 1–10 · 11–20 · 21–30 · &gt; 30<br>"
      "b) <b>0, 1, 10, 11, 20, 21, 30, 31</b>",
      "Software-testing question (no deck in your slides). Each fine band is one valid class; values at or below the limit form the extra class. Boundary values sit at the edges of each class.",
      S, "Q3.2", 5)

TFQ = [
    (1, "The identifiers in the code are coherent.", False, "15",
     "The naming style is mixed: <code>isEven</code> uses CamelCase but <code>is_Odd</code> uses an underscore — slide 15: use one variable style, \"but not both!\" (main even calls <code>isOdd</code>, which does not match <code>is_Odd</code>)."),
    (2, "The code lacks proper documentation.", True, "26–29",
     "There are no comments or JavaDoc at all — slides 27–29: document what the code does, the parameters, return values, restrictions (e.g. <code>div</code> with b = 0) and exceptions."),
    (3, "The methods in the class violate the Single Responsibility Principle (SRP).", False, "10",
     "Each method does exactly one thing (add, subtract, check even, print…) — slide 10: \"Functions should do one thing.\""),
    (4, "There is high coupling between main() and class Util.", True, "",
     "main() calls every static method of Util directly, so it depends on Util's whole interface — any change to Util ripples into main (high fan-out, Quality slide 31). <i>This item is open to interpretation; justify your choice either way.</i>"),
]
CODE = ("<pre>public class Util {\n  public static int add(int a, int b) { return a + b; }\n  public static int sub(int a, int b) { return a - b; }\n  public static int mul(int a, int b) { return a * b; }\n  public static int div(int a, int b) { return a / b; }\n"
        "  public static boolean isEven(int num) { return num % 2 == 0; }\n  public static boolean is_Odd(int num) { return num % 2 != 0; }\n  public static void printMessage(String message) { System.out.println(message); }\n}\n"
        "public class Main {\n  public static void main(String[] args) {\n    int result = Util.add(5, 3);\n    Util.printMessage(\"The sum is: \" + result);\n    result = Util.sub(10, 4); …  result = Util.div(20, 4); …\n"
        "    boolean isEven = Util.isEven(12); …\n    boolean isOdd = Util.isOdd(11); …\n  }\n}</pre>")
for n, q, a, sl, e in TFQ:
    tf("F24c-4-1-%d" % n, 4, sl, "Code review of Util class", CODE + q, a, e, S, "Q4.1.%d" % n, 4)

ATT = [
    (1, "Sniffing the network traffic between the user's web browser and the bank's server to intercept user login credentials or sensitive financial information.", 1,
     "The attacker <b>gains access</b> to an asset (credentials/financial data) — interception (slide 14)."),
    (2, "Creating fake user accounts to gain access to the users' profile.", 2,
     "The attacker <b>inserts false information</b> (fake accounts) into the system — fabrication (slide 15)."),
    (3, "Denial of Service (DoS) attack, where the attacker disrupts the availability of the banking application's services by overwhelming the system with excessive login requests.", 0,
     "Making part of the system <b>unavailable</b> — interruption (slide 14 gives a denial of service attack as the example)."),
    (4, "Changing the permissions for their account so they can have access to more data.", 3,
     "The attacker <b>tampers with</b> a system asset (the permission settings) — modification (slide 15)."),
]
for n, desc, a, e in ATT:
    mcq("F24c-4-2a-%d" % n, 6, "14, 15", "Classify the attack",
        "A web-based banking application (use cases: Login, View Account, Transfer funds, Update profile) received this attack. Select its threat type:<br>" + desc,
        ["Interruption", "Interception", "Fabrication", "Modification"], a, e, S, "Q4.2a.%d" % n, 6)
short("F24c-4-2bc", 6, "14, 15, 24", "Misuse cases and mitigation",
      "For the banking system above (actor <i>user</i>; use cases Login, View Account, Transfer funds, Update profile):<br>b) Modify the use case diagram with the misuse cases from the four attacks. Draw a proper misuse case diagram.<br>c) Pick one attack, specify what asset it threatens and suggest a proper mitigation.",
      "b) Add an <b>Attacker</b> (misuser) actor outside the system and four <b>misuse cases</b> (usually drawn shaded/black), each linked to the use case it attacks with a <code>&lt;&lt;threaten&gt;&gt;</code> arrow:<ul>"
      "<li><i>Sniff network traffic</i> —threatens→ Login (and View Account)</li><li><i>Create fake account</i> —threatens→ Login / Update profile</li>"
      "<li><i>Flood with login requests (DoS)</i> —threatens→ Login</li><li><i>Change account permissions</i> —threatens→ Update profile / View Account</li></ul>"
      "Mitigations can be added as use cases that <code>&lt;&lt;mitigate&gt;&gt;</code> the misuse cases.<br>"
      "c) Example: <b>Sniffing</b> threatens the users' <b>login credentials and financial data</b> (confidentiality) → mitigate by encrypting all traffic (HTTPS/TLS) and using multi-factor authentication. "
      "Other examples: DoS → asset: service availability → rate limiting, CAPTCHA, traffic filtering; permission change → asset: account data → strict authorization checks and logging of user actions.",
      "Security slide 13 (asset/threat/control examples), slides 14–15 (threat types), slide 40 (log user actions) and slide 24 (risk assessment). The Final 2021 model answer used the same &lt;&lt;threaten&gt;&gt; notation.",
      S, "Q4.2 b–c", 3)

short("F24c-5-1", 7, "23, 24, 26, 30–32", "Is the product ready to ship?",
      "A company developed an application for managing customer orders. Customer requirements:<ol><li>Availability: at least 99%</li><li>POFOD: less than 0.1</li><li>ROCOF: less than 2 failures per 8-hour work period</li></ol>"
      "After testing for <b>10 days</b>: total requests 2,500; total failures 120 (80 software crashes, 40 data corruption issues); average restart time after a failure 5 minutes.<br>"
      "a) Calculate the availability, POFOD, and ROCOF.<br>b) Can the MTBF be calculated? If so, calculate it.<br>c) Is the product ready to ship? Explain.",
      "Total time = 10 × 24 = 240 h = 14,400 min.<br>"
      "a) <b>Availability:</b> downtime = 80 crashes × 5 min = 400 min → (14400 − 400) / 14400 = <b>0.972</b> (97.2%). <i>(If all 120 failures are counted: 600 min → 0.958.)</i><br>"
      "<b>POFOD</b> = 120 / 2500 = <b>0.048</b><br>"
      "<b>ROCOF</b> = 120 / 240 h = 0.5 per hour = <b>4 failures per 8-hour period</b><br>"
      "b) <b>No</b> — MTBF needs the timestamp of each failure and of when service resumed; we only know the average restart time, not when each failure happened.<br>"
      "c) <b>No.</b> POFOD (0.048 &lt; 0.1) is fine, but availability (97.2% &lt; 99%) and ROCOF (4 &gt; 2 per 8 h) do not meet the requirements.",
      "This mirrors the Dependability slides 30–32 activity exactly: compute ROCOF per work period, POFOD per request, availability from crash downtime; \"Can we calculate MTBF? No — need timestamps.\"",
      S, "Q5.1", 8)
FH = [
    (1, "The system has backup power sources, such as a battery backup, to keep critical devices running during power outages.", 0,
     "The system <b>keeps operating despite the failure</b> → fault tolerance (Dependability slide 16)."),
    (2, "Sensors throughout the house monitor for issues like water leaks, unusual temperature changes, or abnormal power consumption.", 2,
     "Monitoring to <b>discover</b> problems → fault detection (slide 17, reliability achievement)."),
    (3, "Software updates are automatically applied to fix known vulnerabilities and improve the system's reliability.", 1,
     "Fixing known weaknesses <b>before</b> they can cause errors or failures prevents faults from occurring in operation → fault avoidance (slide 17)."),
]
for n, desc, a, e in FH:
    mcq("F24c-5-2-%d" % n, 7, "16, 17", "Fault handling type",
        "A smart home system controls appliances and devices. It can leverage fault tolerance, fault avoidance and fault detection. Which type of fault handling is this action?<br>" + desc,
        ["Fault tolerance", "Fault avoidance", "Fault detection"], a, e, S, "Q5.2.%d" % n, 8)
