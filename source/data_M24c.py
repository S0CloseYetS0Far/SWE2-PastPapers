from qb import *

S = "M24c"
src(S, "Midterm — 3rd Semester 2024", "Exams/Midterm/2024/Midterm-3rd-2024.pdf")

mcq("M24c-1-1", 1, 15, "SQA focus",
    "SQA (Software Quality Assurance) focuses on:",
    ["Ensuring the software meets specific functional requirements", "Evaluating the software's usability and user experience",
     "Ensuring that quality standards and processes are followed", "Managing the software development team and project timelines"], "c",
    "Intro slide 15: \"Quality Assurance: <b>processes/standards</b> to produce product and to improve quality over time.\" Quality slide 4: QM checks deliverables are consistent with organizational standards.",
    S, "Q1.1", 8)
mcq("M24c-1-2", 2, 27, "Interaction-oriented motivation",
    "Which of the following scenarios best represents \"interaction-oriented\" motivation for work?",
    ["Sarah enjoys her job as a software developer because she finds programming tasks intellectually stimulating and fulfilling.",
     "Ali works as an accountant primarily to earn a high salary and achieve financial security.",
     "Eman works as a customer service representative because she enjoys interacting with customers and helping them solve problems.",
     "Mahmoud works as a chef because he is passionate about cooking and wants to create delicious dishes."], "c",
    "PM slide 27: \"<b>Interaction-oriented</b> — the principal motivation is the presence and actions of co-workers.\" Sarah and Mahmoud are task-oriented (the work itself); Ali is self-oriented (personal goals).",
    S, "Q1.2", 8)
mcq("M24c-1-3", 10, "", "Traceability matrix",
    "To check that all requirements are covered by the use cases, we use:",
    ["Use case diagrams", "Sequence diagrams", "Design patterns", "Traceability matrix"], "d",
    "A <b>traceability matrix</b> maps each requirement to the use cases (or tests) that cover it, so gaps are visible. (PM slide 18 mentions deriving traceability information for requirements changes; the matrix itself is not on your slides.)",
    S, "Q1.3", 8)
mcq("M24c-1-4", 10, "", "SaaS",
    "SaaS is a software delivery model where:",
    ["Software is developed using agile methodologies", "Users access software applications over the Internet",
     "Software is installed and maintained on individual computers", "Software is hosted and managed by a third-party provider"], "b",
    "Software as a Service: the application runs on the provider's servers and users <b>access it over the Internet</b> (usually through a browser) instead of installing it. (Option d describes hosting in general and is part of SaaS, but b is the defining feature.) Not on your slides.",
    S, "Q1.4", 8)
mcq("M24c-1-5", 3, 16, "ISO 9001",
    "ISO 9001 certification for software quality indicates that:",
    ["The software is completely free of defects or bugs", "The software meets specific industry functional requirements",
     "The software meets specific industry functional and non-functional requirements", "The organization has established and follows a robust quality management system"], "d",
    "ISO 9001 is a standard for <b>quality management processes</b> (Quality slide 16 mentions \"quality processes as embodied in ISO 9001\"). It certifies the organization's process, not that a product is defect-free.",
    S, "Q1.5", 1)
mcq("M24c-1-6", 4, 10, "DRY",
    "In design quality, we follow the DRY rule, which means:",
    ["Defer Redundant Yellowpages", "Duplicate Reduction Yields", "Different Reports Yearly", "Don't Repeat Yourself"], "d",
    "Source Code Quality slide 10: \"DRY: <b>Don't Repeat Yourself</b> — to avoid code duplications.\"",
    S, "Q1.6", 1)
mcq("M24c-1-7", 5, "15, 24", "Characteristic of good design",
    "Which of the following is considered a characteristic of a good design?",
    ["Low degree of connectivity/associations among the objects", "Long communication chains between the objects", "High coupling", "Low cohesion"], "a",
    "Good OO design has <b>low coupling</b> (few connections between objects) and high cohesion. OOAD slide 24: Façade gives \"low coupling between the subsystem and its clients\"; slide 15 Demeter: speak only to your friends (short chains).",
    S, "Q1.7", 1)
mcq("M24c-1-8", 3, 30, "Dynamic metrics",
    "Dynamic metrics are closely related to software quality attributes such as:",
    ["Code coverage", "Lines of code", "Length of user manual", "Response time"], "d",
    "Quality slide 30: \"It is relatively easy to measure the <b>response time</b> of a system (performance attribute) or the number of failures (reliability attribute).\"",
    S, "Q1.8", 1)
mcq("M24c-1-9", 3, "3, 4", "Quality management responsibilities",
    "Quality management is responsible for:",
    ["Independent check on the software development process", "Checking the project deliverables to ensure that they are consistent with organizational standards and goals",
     "Establishing a quality plan for a project", "All of the above"], "d",
    "Quality slide 4: independent check; checks deliverables against organizational standards and goals. Slide 3: establishing a quality plan for a project. All three are listed.",
    S, "Q1.9", 1)
mcq("M24c-1-10", 2, 13, "People risks",
    "When staff are ill and unavailable at critical times in a project, the type of risk here is:",
    ["Technology risk", "People risk", "Estimation risk", "Tools risk"], "b",
    "PM slide 13: <b>People</b> — \"Key staff are ill and unavailable at critical times.\"",
    S, "Q1.10", 1)

short("M24c-2", 2, "10–21", "Risk process for a game launch",
      "A software development company is planning to launch a new mobile application in the competitive gaming industry. They want to ensure a successful launch while effectively managing potential risks. They recognize that the gaming market is highly competitive and subject to rapid technological advancements. "
      "The company has conducted market research, analysed the competitive landscape, developed a marketing strategy, and established a feedback collection mechanism. They plan to closely track user engagement metrics, app reviews and ratings, stay updated on industry trends and analyse competitor activities.<br>"
      "1) <b>Risk identification:</b> identify and explain one potential risk.<br>2) <b>Risk analysis:</b> assess its likelihood and consequences.<br>3) <b>Risk planning:</b> propose one strategy to mitigate it.<br>4) <b>Risk monitoring:</b> describe how the company plans to monitor the app's performance and user reception.",
      "1) <b>Product competition</b> (business risk): a competitor releases a similar or better game before or during the launch and takes the target audience. <i>(Also acceptable: technology change — new technology makes the app outdated.)</i><br>"
      "2) <b>Probability: high</b> (the market is \"highly competitive\" with rapid advances). <b>Effects: serious</b> — fewer downloads and revenue, the launch may fail.<br>"
      "3) <b>Minimisation strategy:</b> differentiate the game with unique features, release an early/beta version quickly, and use the marketing strategy to build awareness; <b>contingency plan:</b> adjust pricing/features quickly based on feedback.<br>"
      "4) <b>Monitoring:</b> regularly track user engagement metrics, app reviews and ratings, and competitor activity and industry trends; discuss these indicators at management meetings to see if the risk is becoming more or less likely and adapt strategies.",
      "PM slide 10 (risk management process), slide 9 (product competition / technology change are business risks), slide 14 (probability and effects scales), slide 17 (avoidance, minimisation, contingency), slides 20–21 (risk monitoring and indicators).",
      S, "Q2", 2)

short("M24c-3", 3, 11, "Quality attributes fill-in",
      "Fill the blank with the most appropriate term (no duplication).<br><b>Terms:</b> Understandability · Complexity · Robustness · Resilience · Usability · Reusability · Portability · Modularity · Maintainability · Learnability · Adaptability"
      + ol(["______ is a characteristic attributed to a computer program if it can run with minimal rework on operating systems other than the one for which it was created.",
            "______ is a measure of the depth and quantity of routines in a piece of code.",
            "______ refers to an organizing structure in which different components of a software system are divided into separate functional units.",
            "______ refers to how effectively users can interact with a software product."]),
      ol(["<b>Portability</b>", "<b>Complexity</b>", "<b>Modularity</b>", "<b>Usability</b>"]),
      "All four are software quality attributes on Quality slide 11.",
      S, "Q3", 5)

mcq("M24c-4A", 10, "", "Pattern for notifications",
    "You are developing a chat application where users can send messages to each other. The application needs to notify users whenever a new message is received, and it should support multiple notification mechanisms such as email, SMS, and push notifications. Additionally, the application should allow for easy addition of new notification mechanisms in the future. Select the most appropriate design pattern and justify your choice.",
    ["Singleton", "Facade", "Adapter", "Observer"], "d",
    "<b>Observer:</b> the chat (subject) notifies all registered notifiers/users (observers) automatically when a new message arrives. Email, SMS and push are each an observer implementing the same <code>update()</code> interface, so a new mechanism is added by registering a new observer without changing the chat code. Observer is not one of the three patterns in your OOAD deck (Singleton, Adapter, Façade).",
    S, "Q4 A", 7)
short("M24c-4B", 5, 7, "Initiating vs participating actor",
      "From the use case diagram of the <b>Online Shopping System</b> (actors: Customer, &lt;&lt;service&gt;&gt; Authentication, Identity Provider, Credit Payment Service, PayPal; use cases: View items, Make purchase, Complete checkout, Log in), give an example of:<br>- An initiating actor<br>- A participating actor",
      "<b>Initiating actor:</b> <b>Customer</b> — starts the use cases (view items, make purchase, log in).<br>"
      "<b>Participating actor:</b> e.g. <b>Credit Payment Service</b> or <b>PayPal</b> (take part in Complete checkout), or the Authentication / Identity Provider (take part in Log in) — they interact with the system but do not start the use case.",
      "OOAD slide 7: \"Use case — a complete sequence of related actions <b>initiated by an actor</b>; Actor — an external entity that interacts with the system.\"",
      S, "Q4 B", 7, img="M24c_usecase.jpg")
short("M24c-4C", 5, 15, "Shape code — pattern and violations",
      "Check the following Java code:<pre>public interface Shape { double calculateArea(); }\n\npublic class Square implements Shape {\n  private int sideLength;\n  public Square(int sideLength) { this.sideLength = sideLength; }\n  @Override public double calculateArea() { return sideLength * sideLength; }\n  public void printArea() {\n    double area = calculateArea();\n    System.out.println(\"Square area: \" + area);\n  }\n}\npublic class Circle implements Shape {\n  private int radius;\n  public Circle(int radius) { this.radius = radius; }\n  @Override public double calculateArea() { return Math.PI * radius * radius; }\n  public void draw() { /* draw a circle on screen */ }\n}\npublic class ShapeProcessor {\n  public double calculateArea(Shape shape) { return shape.calculateArea(); }\n}\npublic class Main {\n  public static void main(String[] args) {\n    Shape square = new Square(5);\n    double squareArea = new ShapeProcessor().calculateArea(square);\n    Circle circle = new Circle(3);\n    double circleArea = new ShapeProcessor().calculateArea(circle);\n    square.printArea();\n    circle.draw();\n  }\n}</pre>"
      "1) What is the design pattern used? Justify.<br>2) Provide two design principles that this code violates and explain how.",
      "1) <b>Strategy</b> — <code>Shape</code> is a common interface for a family of interchangeable area algorithms (Square, Circle); <code>ShapeProcessor</code> (the context) works with any Shape without knowing the concrete class.<br>"
      "2) <b>Single Responsibility Principle:</b> Square both computes its area and prints it (<code>printArea</code>), and Circle both computes and draws itself — presentation is mixed with geometry, so each class has more than one reason to change.<br>"
      "<b>Liskov Substitution Principle:</b> the subclasses are not interchangeable through the Shape type — Square adds <code>printArea()</code> and Circle adds <code>draw()</code>, which are not in the interface, so <code>square.printArea()</code> on a <code>Shape</code> reference does not even compile; clients must know the concrete type.<br>"
      "<i>(Also acceptable: Open/Closed — adding a new shape's display behaviour means changing client code.)</i>",
      "OOAD slide 15 (SOLID). The Strategy pattern is not one of the three patterns in your OOAD deck; the Final 2021 model answer defines it as \"defines a family of algorithms, encapsulates each one and makes them interchangeable\".",
      S, "Q4 C", 3)
