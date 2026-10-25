from qb import *

S = "M24b"
src(S, "Midterm — 2nd Semester 2024", "Exams/Midterm/2024/Midterm2-2nd-2024.pdf")

mcq("M24b-1-1", 2, "8, 9", "Business risk",
    "Which of the following risks is the potential negative impact on the company's reputation and image due to company corruption rumors?",
    ["Product risk", "Project risk", "Business risk", "Programming risk"], "c",
    "PM slide 8: \"<b>Business risks</b> affect the organisation developing or procuring the software.\" Reputation damage hits the organisation, not the schedule (project) or the software quality (product).",
    S, "Q1.1", 1)
mcq("M24b-1-2", 1, 5, "Problems with software production",
    "One of the problems in software production is:",
    ["Software is very hard to visualize", "Software wears out very quickly", "Software is manufactured", "Software is not scalable"], "a",
    "Intro slide 5: problems are complexity, conformity, changeability and \"<b>Invisibility</b> — software is very hard to visualize\".",
    S, "Q1.2", 1)
mcq("M24b-1-3", 2, "25, 26", "Human needs hierarchy",
    "Recognition of achievements is considered a(n) ______ need according to Maslow's human hierarchy of needs.",
    ["Physiological", "Esteem", "Social", "Self-realization"], "b",
    "PM slide 26 (need satisfaction): \"<b>Esteem</b> — recognition of achievements; appropriate rewards.\" Self-realization = training and responsibility.",
    S, "Q1.3", 1)
mcq("M24b-1-4", 3, 20, "Pair programming weakness",
    "Which of the following is a true disadvantage of pair programming in XP?",
    ["The code is not being examined or reviewed", "Both members of a pair mutual understanding of the code",
     "Both members of a pair may make the same mistake in understanding the system requirements", "Working in pairs takes double the time to produce the code compared to single individuals"], "c",
    "Quality slide 20: \"Mutual misunderstandings — both members of a pair may make the same mistake in understanding the system requirements.\"",
    S, "Q1.4", 1)
mcq("M24b-1-5", 3, 2, "Benefit of standards",
    "The benefit of having and using software standards is:",
    ["They are always up-to-date", "They often involve bureaucratic form-filling and processes",
     "They are a framework for defining what quality means in a particular setting", "They take into account measuring quality as experienced by users of the software"], "c",
    "'Software standards' is a topic on Quality slide 2. Sommerville ch. 24: standards \"provide a framework for defining what quality means in a particular setting\" and capture best practice. Option b is a <i>problem</i> with standards.",
    S, "Q1.5", 1)
mcq("M24b-1-6", 3, 11, "Efficiency",
    "It refers to the ability of a system to maximize performance and productivity while minimizing resource usage:",
    ["Portability", "Reliability", "Resilience", "Efficiency"], "d",
    "<b>Efficiency</b> (a quality attribute on Quality slide 11) is about getting the most performance from the least resources (CPU, memory, time).",
    S, "Q1.6", 2)
mcq("M24b-1-7", 3, 31, "Size metrics",
    "In size-oriented metrics, to measure the size of the program we use:",
    ["Number of functions", "Number of user inputs", "Number of lines of code", "Amount of memory usage"], "c",
    "Quality slide 31: \"<b>Length of code</b> — this is a measure of the size of a program.\"",
    S, "Q1.7", 2)

RISK = [
    (1, "There is a sudden shift in consumer preferences towards a new social media app.", "Product competition"),
    (2, "The company decides to adopt a new software development methodology for all its projects.", "Technology change"),
    (3, "There is a change in the executive team, resulting in a new strategic direction for the organization.", "Management change"),
    (4, "The staff used an algorithm and estimated that it would take two weeks to complete; however, as they delved deeper into the technical details, they realized that the algorithm involved intricate calculations. As a result, the implementation took three months.", "Size underestimation"),
    (5, "Due to Covid-19-related disruptions, the staff faced delays in receiving a critical chip for their system, leading to uncertainty on when they will receive it.", "Hardware unavailability"),
]
OPTS = ["Hardware unavailability", "Technology change", "Size underestimation", "Product competition", "Management change"]
EXPL = {
    "Product competition": "Slide 9: \"Product competition (business) — a competitive product is marketed before the system is completed\"; consumers moving to a competing app is a competition risk.",
    "Technology change": "Slide 9: \"Technology change (business) — the underlying technology on which the system is built is superseded by new technology.\" A new development methodology replaces the existing way of working.",
    "Management change": "Slide 9: \"Management change (project) — there will be a change of organizational management with different priorities.\"",
    "Size underestimation": "Slide 9: \"Size underestimate (project and product) — the size of the system has been underestimated\" (2 weeks became 3 months).",
    "Hardware unavailability": "Slide 9: \"Hardware unavailability (project) — hardware that is essential for the project will not be delivered on schedule.\"",
}
for n, desc, ans in RISK:
    mcq("M24b-2-%d" % n, 2, 9, "Match risk to risk type",
        "Choose the most appropriate risk type for this possible risk (each type is used once in the exam):<br>" + desc,
        OPTS, OPTS.index(ans), EXPL[ans], S, "Q2.%d" % n, 2)

short("M24b-3", 5, 15, "SOLID violations in OrderProcessor",
      "The following Java code violates some design principles and SOLID rules. Identify two of the design issues and explain how they are violated.<pre>public class OrderProcessor {\n  private DatabaseConnector databaseConnector;\n  private EmailSender emailSender;\n\n  public OrderProcessor() {\n    databaseConnector = new DatabaseConnector();\n    emailSender = new EmailSender();\n  }\n  public void processOrder(Order order) {\n    databaseConnector.connect();\n    databaseConnector.saveOrder(order);\n    databaseConnector.disconnect();\n  }\n  public void sendEmail(String message) {\n    System.out.print(\"Order processed successfully.\");\n  }\n}\npublic class DatabaseConnector {\n  public void connect()  { /* connect */ }\n  public void saveOrder(Order order) { /* save */ }\n  public void disconnect() { /* disconnect */ }\n}</pre>"
      "Choices: a) short communication chains b) avoid \"hub\" modules c) high cohesion d) low coupling e) Single Responsibility f) Open/Closed g) Injection of Dependency h) Liskov Substitution i) Demeter",
      "<b>e) Single Responsibility Principle</b> — OrderProcessor both processes/saves orders <i>and</i> sends emails, so it has more than one reason to change.<br>"
      "<b>g) Injection of Dependency</b> — the constructor creates its collaborators itself with <code>new DatabaseConnector()</code> and <code>new EmailSender()</code>. They should be injected (passed in, ideally as interfaces) so implementations can vary at runtime.<br>"
      "<i>(Also acceptable: d) Low coupling — OrderProcessor is tied to concrete classes; f) Open/Closed — switching to another database or email service requires modifying OrderProcessor.)</i>",
      "OOAD slide 15 (SOLID): SRP — a class should have one and only one reason to change; Injection of Dependency — collaborating classes whose implementation may vary at runtime should depend on an intermediate injected dependency.",
      S, "Q3 A", 4)

short("M24b-4", 10, "", "Observer pattern — stock market",
      "<b>Stock Market Monitoring System:</b> design a system that tracks the prices of multiple stocks in real time and provides notifications to subscribed investors whenever there is a significant change in the stock prices. Investors should receive updates on their selected stocks without tightly coupling the notification system to the individual stocks.<br>"
      "a) What design pattern is most appropriate? Justify.<br>b) Draw a sequence diagram showing how the pattern operates between the stock market and two investors A and B.",
      "a) <b>Observer pattern</b> — defines a one-to-many dependency so that when one object (the subject: the stock) changes state, all its dependents (observers: investors) are notified automatically. The subject only knows observers through an <code>Observer</code> interface, so stocks and investors stay <b>loosely coupled</b>, and investors can subscribe/unsubscribe at runtime.<br>"
      "b) Lifelines: <code>:StockMarket</code> (subject), <code>A:Investor</code>, <code>B:Investor</code>.<ol>"
      "<li>A → StockMarket: <code>attach(A)</code> (subscribe)</li><li>B → StockMarket: <code>attach(B)</code></li>"
      "<li>StockMarket: <code>setPrice(newPrice)</code> → significant change → <code>notify()</code> (self-call)</li>"
      "<li>StockMarket → A: <code>update(stock, price)</code></li><li>StockMarket → B: <code>update(stock, price)</code></li>"
      "<li>(optional) A/B → StockMarket: <code>getPrice()</code> and a return message</li></ol>",
      "The Observer pattern is not one of the three patterns in your OOAD deck (Singleton, Adapter, Façade), so this sits under 'other topics'. Sequence-diagram notation (lifelines, synchronous messages, activations) is on OOAD slide 13.",
      S, "Q4", 4)
