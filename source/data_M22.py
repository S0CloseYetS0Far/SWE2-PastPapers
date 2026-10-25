from qb import *

# ---------------- Midterm 1, 2nd semester 2022 (also = Midterm 1 Dec 2021 model answer) ----------------
S = "M22b1"
src(S, "Midterm 1 — 2nd Semester 2022", "Exams/Midterm/2022/CS 392 - 2022 - mid 1 - second semester.pdf")

mcq("M22b1-1-1", 5, 27, "Middleware",
    "A __________ is software used to make diverse applications work together smoothly.",
    ["Middleware", "Traceability Matrix", "JUnit Assertion", "ISO 9001"], "a",
    "OOAD slide 27: \"In general, <b>middleware</b> is software used to make diverse applications work together smoothly.\"",
    S, "Q1.1", 1)
mcq("M22b1-1-2", 10, "", "Serialization",
    "The process of converting an object into a stream of bytes to store the object or transmit it to memory, a database, or a file is called:",
    ["Serialization", "Code Refactoring", "Dependency Injection", "Iteration"], "a",
    "<b>Serialization</b> turns an object into bytes so it can be stored or sent (and deserialization rebuilds it). Official 2021 key: a. (Not on your slides.)",
    S, "Q1.2", 1)
mcq("M22b1-1-3", 4, 15, "Coherent identifiers",
    "To maintain code quality, we should use coherent identifiers, which means:",
    ["We should use camel case identifiers", "We should use one language and one variable style",
     "We should use a unified vertical alignment", "We should use meaningful variable names"], "b",
    "Source Code Quality slide 15: \"Use coherent identifiers — choose <b>one language</b> … use <b>one variable style</b>, either CamelCase or underscores, but not both.\" (d is 'meaningful names', a different rule on slide 14.)",
    S, "Q1.3", 1)
mcq("M22b1-1-4", 4, 10, "Boy Scout rule",
    "The Boy Scout rule says:",
    ["Don't Repeat Yourself", "Leave the campground cleaner than you found it",
     "Functions should do one thing. They should do it well.", "Speak only to your friends. Treat friends' friends as your enemies."], "b",
    "Source Code Quality slide 10: Boy Scout rule — \"Leave the campground cleaner than you found it.\"",
    S, "Q1.4", 1)
mcq("M22b1-1-5", 3, 20, "Pair programming downside",
    "A downside of pair programming that could jeopardize the quality of software development is the possibility of having:",
    ["Code is unlikely being reviewed by the pair", "Mutual misunderstanding of the requirements",
     "The depth of knowledge of the program by the pair is shallow", "None of the above. Pair programming guarantees to produce software with the best qualities."], "b",
    "Quality slide 20: \"Mutual misunderstandings — both members of a pair may make the same mistake in understanding the system requirements.\"",
    S, "Q1.5", 1)
short("M22b1-2a", 5, "13, 15", "Compare sequence diagrams",
      "This is a module sequence diagram of an online clothing store: after a customer places an order, this use case calculates the discount value of the total order.<br>"
      "<b>(a)</b> <i>Order</i> does everything itself: getQuantity and getProduct from Order Line, getPricingDetails from Product, calculateBasePrice and calculateDiscounts itself, getDiscountInfo from Customer.<br>"
      "<b>(b)</b> <i>Order</i> asks each Order Line to calculatePrice (which asks its Product getPrice(quantity)), then asks the Customer getDiscountedValue(order), which calls back getBaseValue.<br>"
      "Compare the two sequence diagrams in terms of OO design. Which provides a better design and why?",
      "<b>(b) is the better design.</b> Responsibility is distributed: each object does the work on the data it owns (Order Line computes its own price, Customer computes its own discount). "
      "This gives <b>shorter communication chains</b>, <b>lower coupling</b> and higher cohesion — Order no longer has to know the internals of Order Line, Product and Customer. "
      "In (a) Order is a \"hub\" that micromanages everyone (centralized control). <i>Official 2021 model answer: \"(b) has shorter communication chain than (a) and less responsibilities on an order, which means b has lower coupling.\"</i>",
      "OOAD slide 13 (sequence diagrams: messages, activations) and slide 15 (SRP, Demeter — speak only to your friends).",
      S, "Q2 a", 2, img="M22_seq.jpg")
mcq("M22b1-2b", 10, "", "Doing responsibility",
    "What type of object responsibility is data processing?",
    ["Doing responsibility", "Knowing responsibility", "Delegation responsibility", "Initiation responsibility"], "a",
    "<b>Doing</b> responsibilities are actions an object performs: creating objects, doing calculations/data processing, initiating actions in other objects. Knowing = data it holds and references to other objects. (Not on your slides.)",
    S, "Q2 b", 3)
mcq("M22b1-2c", 5, 7, "Primary actor",
    "If the system has an actor who initiates the use case to achieve a goal, then this actor is called a(n):",
    ["Primary actor", "Participating actor", "Supporting actor", "Offstage actor"], "a",
    "The <b>primary</b> actor initiates the use case to achieve a goal (OOAD slide 7: a use case is initiated by an actor). Supporting/participating actors help; offstage actors have an interest but don't interact.",
    S, "Q2 c", 3)
short("M22b1-3-1", 5, "20–25", "Match pattern to situation",
      "Match the design pattern to the situation (each system has one pattern).<br><b>Patterns:</b> 1 Singleton · 2 Façade · 3 Observer · 4 Adapter · 5 Strategy"
      + ol(["Sending an SMS message requires lots of big ugly code, involving connection, message and other objects.",
            "Your program must support switching among several different email libraries, but each one has a slightly different interface.",
            "Your video game needs to listen for presses of the arrow keys to update the position of the character in the game.",
            "The office of the President of the United States has at most one active president at any given time. Regardless of the identity of the active president, the title \"The President of the United States\" is a global point of access that identifies the person in the office."]),
      ol(["<b>Façade</b> (2)", "<b>Adapter</b> (4)", "<b>Observer</b> (3)", "<b>Singleton</b> (1)"]),
      "Official 2021 model answer. OOAD slide 25: Façade = one class representing a whole subsystem; Adapter = match interfaces of different classes; Singleton = only one instance with a global access point. Observer (listeners) is not in your deck.",
      S, "Q3.1", 4)
short("M22b1-3-2", 5, "21, 22", "RoboChef — Adapter design",
      "You created an \"intelligent\" kitchen system, RoboChef, that controls kitchen appliances. Initially RoboChef uses only Electrolux gas ovens: <code>RoboChef —controls→ ElectroluxGasOven { +heat(howHot: Temperature, howLong: Time) }</code>. "
      "Now you want to support other ovens: <code>MaytagMicrowave { +cook(seconds: Integer, power: Integer) }</code> and <code>WhirlpoolElectricRange { +bake(degrees: Integer, time: Time) }</code>. Update the design to allow easy switching between oven-control systems.<br>"
      "1) What design pattern(s) should you use and why? 2) Draw a class diagram. 3) What effect did the new design have on the coupling between RoboChef and ElectroluxGasOven?",
      "1) <b>Adapter</b> — each vendor already provides an interface that <i>almost</i> does what RoboChef needs but with a different signature; an adapter converts it into the interface RoboChef expects, so new ovens are added without changing RoboChef (Open/Closed).<br>"
      "2) Class diagram:<pre>RoboChef ──controls──▶ «interface» Oven\n                        + heat(howHot: Temperature, howLong: Time)\n                              ▲ (implements)\n        ┌─────────────────────┼──────────────────────┐\nElectroluxAdapter       MaytagAdapter          WhirlpoolAdapter\n   │ adaptee                │ adaptee                │ adaptee\n   ▼                        ▼                        ▼\nElectroluxGasOven      MaytagMicrowave      WhirlpoolElectricRange\n+heat(...)             +cook(seconds, power) +bake(degrees, time)</pre>"
      "Each adapter's <code>heat()</code> translates the call (e.g. MaytagAdapter converts temperature/time to seconds/power and calls <code>cook()</code>).<br>"
      "3) <b>Reduced their coupling</b> — RoboChef now depends only on the Oven interface, not on ElectroluxGasOven.",
      "OOAD slide 21: Adapter converts the interface of a class into another interface clients expect; slide 22: Open/Closed — introduce new adapters without breaking client code.",
      S, "Q3.2", 5)

# ---------------- Midterm, 1st semester 1444 (Oct 2022) — official model answer ----------------
S = "M22a"
src(S, "Midterm — 1st Semester 1444 (Oct 2022), official model answer", "Exams/Midterm/2022/CS 392 Mid 1 2022 MA.docx")

mcq("M22a-1-1", 3, 7, "Quality plan structure",
    "A quality plan structure contains:",
    ["Quality goals", "Risks management", "Process descriptions", "All of the above"], "d",
    "Quality slide 7 (quality plan structure): product introduction, product plans, <b>process descriptions</b>, <b>quality goals</b>, <b>risks and risk management</b>. Official key: d.",
    S, "Q1.1")
mcq("M22a-1-2", 3, 4, "Quality management activities",
    "Which is <b>not</b> one of the quality management activities?",
    ["Provides an independent check on the software development process", "The quality management should be done by the development team",
     "Ensure that the project is consistent with organizational standards and goals"], "b",
    "Quality slide 4: QM provides an independent check and checks deliverables against organizational standards; the quality team should be <b>independent from</b> the development team. Official key: b.",
    S, "Q1.2")
also("M22b1-1-1", S, "Q1.3")
mcq("M22a-1-5", 10, "", "Design pattern classifications",
    "Which of the following is the correct list of classifications of design patterns?",
    ["Creational, Structural and Behavioral patterns", "Executional, Structural and Behavioral patterns",
     "Creational, Executional and Behavioral patterns", "None of the above"], "a",
    "The Gang-of-Four groups patterns as <b>creational</b> (e.g. Singleton), <b>structural</b> (e.g. Adapter, Façade) and <b>behavioral</b> (e.g. Observer, Strategy). Official key: a.",
    S, "Q1.5")
mcq("M22a-1-6", 3, 2, "Benefit of standards",
    "A benefit of following software standards is:",
    ["Standards might be irrelevant", "Standards encapsulate best practices", "Standards are always up-to-date", "None of the above"], "b",
    "Standards capture (encapsulate) best practice and knowledge that was learned through trial and error. 'Might be irrelevant' and 'not up-to-date' are problems of standards. Official key: b.",
    S, "Q1.6")
mcq("M22a-1-7", 4, 10, "Not a clean code principle",
    "Which is <b>not</b> a clean code principle?",
    ["A problem in code must be fixed by the original developer", "Avoid code duplications", "Functions should do one thing"], "a",
    "Avoid duplication (DRY) and one-thing functions (SRP) are on Source Code Quality slide 10. Quality slide 17 says the opposite of (a): \"Fix problems when you see them\" — you can fix others' code directly. Official key: a.",
    S, "Q1.7")
mcq("M22a-1-8", 5, 15, "SRP violation",
    "A block of code such as a class or method serving multiple different functionalities tends to violate which of the following?",
    ["Single responsibility principle", "Liskov substitution principle", "Open/closed principle"], "a",
    "OOAD slide 15: SRP — a class should have one and only one reason to change. Official key: a.",
    S, "Q1.8")
short("M22a-2-1", 4, "12–16, 26–29", "Evaluate and fix string-reverse code",
      "Evaluate the quality of the following code and fix the issues (the code reverses a string; find at least 3 issues):"
      "<pre>public class string\n{static String string1(String x1)\n{String x2=\"\";\nfor(int i=x1.length();i&gt;0;--i)  {  x2=x2+(x1.charAt(i-1));  }\nreturn x2; }\npublic static void main(String[] arg) {\nstring  x3=new string ();\nScanner x4=new Scanner(System.in);\nSystem.out.print(\"Enter a string: \");\nString  x5=x4.nextLine();\nSystem.out.println(\"Reverse of a String  is : \"+x3.string1(X5));  }}</pre>",
      "<b>Issues:</b><ul><li>Meaningless identifiers (<code>string</code>, <code>string1</code>, <code>x1</code>…<code>x5</code>) — slide 14; the class name <code>string</code> is lowercase and clashes with <code>String</code>.</li>"
      "<li>Inconsistent identifier: <code>X5</code> vs <code>x5</code> (Java is case-sensitive — it won't compile).</li>"
      "<li>No indentation / poor layout — slides 17–18.</li><li>No documentation — slides 26–29.</li><li>A static method is called through an unnecessary object instance.</li></ul>"
      "<b>Fixed:</b><pre>/** Reverses strings. */\npublic class StringReverser {\n    /**\n     * Reverses the given text.\n     * @param text  the string to reverse (not null)\n     * @return      the reversed string\n     */\n    static String reverse(String text) {\n        String reversed = \"\";\n        for (int i = text.length(); i &gt; 0; i--) {\n            reversed = reversed + text.charAt(i - 1);\n        }\n        return reversed;\n    }\n\n    public static void main(String[] args) {\n        Scanner input = new Scanner(System.in);\n        System.out.print(\"Enter a string: \");\n        String userText = input.nextLine();\n        System.out.println(\"Reverse of the string is: \" + reverse(userText));\n    }\n}</pre>",
      "Source Code Quality slides 12–16 (meaningful, coherent identifiers), 17–18 (indentation and structure), 26–29 (documentation, JavaDoc).",
      S, "Q2.1")
also("F23b-2-2", S, "Q2.2")
short("M22a-3-1", 5, "20–25", "Match pattern to situation",
      "Match the design pattern to the situation (each system has one pattern).<br><b>Patterns:</b> 1 Singleton · 2 Façade · 3 Observer · 4 Adapter · 5 Strategy"
      + ol(["You are building a system that relies on a complex algorithm, and that algorithm may be changed often due to marketing pressures.",
            "Your company already implemented a component that almost implements the interface that you need, but not quite.",
            "A cricket app notifies viewers about the current score, run rate etc. CricketData has all the data; whenever data changes, the display elements (CurrentScoreDisplay, AverageScoreDisplay) are notified with new data and display it.",
            "<code>public class PrintSpooler { private static final PrintSpooler instance = new PrintSpooler(); private PrintSpooler() {} public static PrintSpooler getInstance() { return instance; } }</code>",
            "Clients need a simplified interface to the overall functionality of a complex subsystem."]),
      ol(["<b>Strategy</b> (5)", "<b>Adapter</b> (4)", "<b>Observer</b> (3)", "<b>Singleton</b> (1) — private constructor + static getInstance()", "<b>Façade</b> (2)"]),
      "Official model answer. OOAD slides 20–25 (Singleton, Adapter, Façade). Strategy and Observer are not in your deck.",
      S, "Q3.1")
short("M22a-3-2", 10, "", "Observer — bank interest rate",
      "A Bank-client system issues loans based on an interest rate. Currently all clients keep checking the interest rate by requesting the Bank server every 5 seconds, which is inefficient. Refine the design so clients are informed when the interest rate changes.<br>"
      "<b>Which?</b> pattern and its intent · <b>Why?</b> how it addresses the problem · <b>How?</b> implementation and a class diagram for this specific case.",
      "<b>Which:</b> <b>Observer</b> — defines a one-to-many dependency so that when one object changes state, all its dependents are notified and updated automatically.<br>"
      "<b>Why:</b> instead of clients polling every 5 seconds (active approach), the Bank pushes a notification only when the interest rate actually changes — no wasted requests, and Bank and clients stay loosely coupled.<br>"
      "<b>How:</b><pre>«interface» Subject                 «interface» Observer\n+attach(o: Observer)                 +update(rate: double)\n+detach(o: Observer)                          ▲\n+notifyObservers()                            │ implements\n        ▲ implements                          │\n      Bank ─────────── observers 0..* ──────▶ Client\n  -interestRate: double                 -currentRate: double\n  +setInterestRate(r)  → notifyObservers()   +update(rate)\n  +getInterestRate()</pre>"
      "Clients call <code>bank.attach(this)</code> once; when <code>setInterestRate()</code> changes the rate, Bank calls <code>update(rate)</code> on every registered client.",
      "Official model answer: Observer pattern. (Observer is not one of the three patterns in your OOAD deck.)",
      S, "Q3.2")

# ---------------- Midterm 2, 2nd semester 2022 ----------------
S = "M22b2"
src(S, "Midterm 2 — 2nd Semester 2022", "Exams/Midterm/2022/CS 392 Mid 2 2022 - second semester.pdf  (same Q1 as page 14 of Exams/Final/2023/_Final_2nd_CS392_2023.pdf)")

mcq("M22b2-1-1", 9, "", "Change management",
    "The CM (configuration management) activity for keeping track of requests for changes to the software from customers and developers is:",
    ["Version management", "Change management", "Release management", "System building"], "b",
    "<b>Change management</b> keeps track of change requests, works out their costs and impact, and decides if/when to implement them. (Configuration management — not in your slides.)",
    S, "Q1.1", 1)
mcq("M22b2-1-2", 9, "", "Checksums",
    "__________ are signatures on the source code file that are calculated from data in the file.",
    ["Deltas", "Mitigations", "Source code checksums", "Modification timestamp"], "c",
    "A <b>checksum</b> is computed from the file's contents, so it changes whenever the content changes (used by build systems to detect modified files). Deltas are differences between versions.",
    S, "Q1.2", 1)
mcq("M22b2-1-3", 6, 24, "Operational risk assessment",
    "The risk assessment process that focuses on the possible risks that can arise from human behaviour is:",
    ["Operational risk assessment", "Life cycle risk assessment", "Preliminary risk assessment", "Baseline risk assessment"], "a",
    "Security slide 24: \"<b>Operational risk assessment</b>: possible risks that can arise from human behavior.\"",
    S, "Q1.3", 1)
mcq("M22b2-1-4", 9, "", "Baseline",
    "A __________ is the set of component versions that are included in the system.",
    ["Mainline", "Codeline", "Baseline", "Workspace"], "c",
    "A <b>baseline</b> is a definition of a specific system: the component versions included in it. A codeline is a sequence of versions of one component.",
    S, "Q1.4", 1)
mcq("M22b2-1-5", 9, "", "Distributed version control",
    "Which of the following is <b>not</b> true for a distributed version control system?",
    ["It is essential for open source development", "It provides a backup mechanism for the repository",
     "Developers can compile and test the entire system on their local machines", "Developers check out components from the project repository into their private workspace"], "d",
    "Checking out components from a central project repository is how a <b>centralized</b> system works. In a distributed system developers <b>clone</b> the whole repository.",
    S, "Q1.5", 1)
also("F23b-4-1", S, "Q2.1", 2)
short("M22b2-2-2", 6, "14, 15", "Add a misuse case",
      "Complete the <b>Online Shopping System</b> use case diagram (Customer; use cases View items, Make purchase, Complete checkout, Log in; external services Authentication, Identity Provider, Credit Payment Service, PayPal) to include one misuse case, then specify the type of threat of that misuse case.",
      "Example: add an <b>Attacker</b> actor with misuse case <b>Steal login info</b> linked to <i>Log in</i> by <code>&lt;&lt;threaten&gt;&gt;</code> → threat type <b>Interception</b> (unauthorized access to an asset).<br>"
      "Other valid examples: <i>Flood the system with requests</i> → Interruption; <i>Change order/payment details</i> → Modification; <i>Create fake orders/accounts</i> → Fabrication.",
      "Security slides 14–15 (the four threat types). Any misuse case is accepted if its threat type matches.",
      S, "Q2.2", 3)
also("F21a-5-2", S, "Q3.2", 2)
also("F21a-5-3", S, "Q3.3", 2)
also("F21a-5-4", S, "Q3.4", 2)
mcq("M22b2-3-1", 7, "16, 17", "Train protection — fault tolerance",
    "A train protection system automatically applies the brakes of a train if the speed limit for a segment of track is exceeded, or if the train enters a track segment that is currently signalled with a red light. This operation is called:",
    ["Fault detection", "Fault removal", "Fault avoidance", "Fault tolerance"], "d",
    "The system keeps the train operating safely <b>in spite of</b> a fault (the driver speeding or passing a red signal) — fault tolerance (Dependability slide 16). Official Final 2021 key: d.",
    S, "Q3.1", 2)
