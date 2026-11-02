# 01. Instructor Notes

## 1. Understand the problem before the tool

Imagine the reception desk at VERIQTA Academy. Sarah asks about access to a course. Before anyone approves or rejects that request, the support team needs a clear briefing: who the request concerns, which course it concerns, what help is requested and whether the request has been reviewed.

At first, a receptionist might write these details on a card. Your first application is the software equivalent of that card. It displays explicitly supplied information in a consistent format. It does not inspect a payment system or modify an enrollment record.

This small outcome establishes several durable engineering habits. You identify the component's responsibility, separate information from verified facts, produce an observable result and check that the result matches the requirement. Those habits will remain useful when a future agent calls a tool, retrieves a document or coordinates a workflow.

Your first implementation uses fixed sample values. This makes the execution easy to trace. Interactive input, validation and external data will come later. Starting with an understandable fixed contract avoids hiding the execution model behind a web interface or framework.

## 2. The parts of your working environment

Your computer supplies processing, memory and storage. The operating system manages those resources and starts programs. Ubuntu is one operating system. A terminal provides a text interface to a session. A shell, such as Bash, reads commands from that interface and decides how to execute them.

Your editor changes source text. Your Python interpreter reads and executes Python source. These are separate responsibilities. Typing a command into a terminal is not the same operation as typing a Python statement into a source file.

| Component | Responsibility | Example in this class |
|---|---|---|
| Operating system | Manages files and processes | Linux starts Python and provides output streams |
| Terminal | Displays and accepts text interaction | You enter a command and see a result |
| Shell | Interprets command syntax | It selects python3 and passes a script path |
| Editor | Creates and saves source text | vi writes first_agent.py to disk |
| Interpreter | Executes Python source | Python runs the print statements |
| Source file | Stores the instructions | support_briefing.py contains assignments and output calls |

Think of a kitchen. The source file is a written recipe. The editor is where you write the recipe. The interpreter is the cook following it. The terminal is where you request the work and receive messages. Saving the recipe does not cook the meal. Running the interpreter asks for execution of the saved recipe.

### Local and remote sessions

An SSH terminal on your laptop may be connected to Ubuntu on a remote EC2 instance. Commands entered in that session run on the remote machine. A file created there is not automatically created on your laptop. A local terminal and a remote terminal can look similar while referring to different files and installed software.

Before debugging a missing file or package, establish which environment you are using. This class does not need a cloud connection, and a public reference run does not establish access to your own machine. Keep host addresses and account details out of public screenshots.

## 3. Understand a shell command

Consider this command:

```bash
python3 first_agent.py
```

The first word selects the executable. The next word is an argument identifying the script. The shell locates python3 through its configured command search path and starts it. Python then attempts to open the specified source file and execute it.

Do not type a displayed shell prompt as part of a command. A tutorial may show a dollar sign or a machine-specific prefix before the command, but this class's command blocks contain only what you should type.

If you enter Python source such as print directly into Bash, Bash does not become Python automatically. If you start python3 without a script, you may enter Python's interactive prompt, normally shown as >>>. That prompt accepts Python statements rather than ordinary shell commands. Use exit() there, or Ctrl+D on a typical Linux terminal, to return to the shell before continuing this lab.

## 4. Your current directory controls relative paths

A directory groups files. A path identifies a file or directory. An absolute path begins at the filesystem root, represented by /. A relative path is interpreted from the current working directory.

If your shell is in a folder containing first_agent.py, the relative filename first_agent.py is enough. If the file is in a child directory named 09-source, the relative path is 09-source/first_agent.py. If you run from another directory, the same text may point somewhere else or fail to find a file.

pwd prints your current working directory. cd changes that directory in the current shell. ls lists entries. You use these commands to establish context, not as a ritual before every program. When Python reports that it cannot open a file, check location and spelling before changing the source.

Linux filenames are normally case-sensitive. first_agent.py and First_Agent.py can refer to different files. Names containing spaces require shell quoting, so this course uses simple underscore-separated Python filenames and hyphenated navigation folders.

### Navigation folders and Python names

Numbered folders such as 09-source organize the reading order. Source filenames remain ordinary Python names such as first_agent.py. This keeps the classroom navigable without introducing unnecessary module-loading complexity. Later classes will explain imports and reusable modules in detail.

## 5. Check the environment you actually have

python3 --version asks the interpreter to report its version. The result depends on your installation. Record your actual output rather than copying a version from this page or a reference image.

This class targets Python 3.12 or later and uses basic standard-library features. The exact reference version is recorded with the execution evidence. Testing one reference environment does not prove behavior on every release, editor or operating system.

If python3 is missing, the class cannot execute yet. Use a supported interpreter installation for your operating system or seek environment-specific setup help. Do not replace Ubuntu's system interpreter or alter system symlinks just to imitate a screenshot. Installation and operating-system maintenance need instructions appropriate to the environment.

vi also needs to be available. The command vi --version commonly works with Vim-based installations, but traditional vi variants may not support it. This lesson uses the basic editing operations shared by common vi-compatible editors and does not require a particular plugin or configuration.

## 6. Source text, saving and execution

A Python script is a text file containing Python source. The .py extension communicates its intended language. It does not automatically execute the file, and it does not require making the file executable when you invoke it through python3.

When vi opens a file, your edits are held in its editing buffer. Saving writes the buffer to disk. Running Python reads the saved file. If you leave unsaved changes in an editor and run the script from another terminal, Python sees the previous disk contents.

Use i to enter insertion mode. Use Esc to leave insertion mode. From normal mode, type :wq and press Enter to write and quit. The editor command is not Python source. If you accidentally type :wq into the file while still in insertion mode, correct the text before saving.

Use :q! only when you intentionally want to discard unsaved edits. The exclamation mark is significant. Do not use it as a universal fix for an unfamiliar editor state.

## 7. Your first print statement

The first script contains a comment and one executable statement:

```python
# Introductory Python execution example. No model or agent loop is used.
print("Welcome to Agentic AI Engineering")
```

The comment begins with # and explains intent to a person reading the file. The interpreter does not execute it as an instruction. print is a built-in function. Parentheses call it, and the quoted text is its argument.

A string is a text value. The quotation marks delimit it in source and are not displayed as part of this message. print writes the text and normally appends a newline. That is why the next shell prompt appears on a new line.

The filename first_agent.py is retained as an introductory exercise name. The implementation does not call a model, choose tools, plan actions or run an agent loop. Naming a file agent does not make it an autonomous system. You should describe observable capability accurately.

## 8. Variables and assignment

The briefing stores information under descriptive names:

```python
student_name = "Sarah"
```

The left side is a variable name. The single equals sign performs assignment. The right side is a string value. After the statement runs, the name student_name refers to that value within this executing program.

Assignment does not ask a question and does not display output. A comparison uses different syntax, which a later class will introduce. Read the statement as assigning the value Sarah to the name student_name.

Names help explain intent. student_name is clearer than an unexplained x. Snake case uses lowercase words separated by underscores, a common Python naming convention. Python names are case-sensitive, so student_name and Student_Name are different names.

If later code refers to student_nam instead of student_name, Python does not guess the intended spelling. It raises a NameError when it reaches that undefined name. This is a useful signal: a clear failure is easier to investigate than silently substituting the wrong student's data.

Assignments in this script are held in the memory of its process. They do not create database records. When the program finishes, those in-memory bindings do not become persistent student storage. Saving source code and persisting business data are separate operations.

## 9. Formatted strings connect data to presentation

The briefing includes this line:

```python
print(f"Student: {student_name}")
```

The f immediately before the opening quote marks a formatted string literal. The expression inside braces is evaluated and its value is inserted into the text. With student_name bound to Sarah, the result is Student: Sarah.

The fixed label Student: is presentation text. The value comes from the variable. This separation helps you identify which part communicates structure and which part carries data. The label does not turn the output into a machine-readable JSON response; JSON will be taught later.

If the f prefix is removed, the braces are ordinary characters in a regular string, and Python displays Student: {student_name}. The program may still exit successfully even though the output is wrong. That difference explains why a successful process exit is only one part of correctness.

String interpolation is appropriate for this local text report. In later contexts, such as SQL queries or HTML, you will need context-appropriate parameterization or escaping. Do not assume an f-string alone makes arbitrary input safe for every external system.

## 10. Trace the complete briefing

Python executes this script's top-level statements in order. It first assigns the five sample values. It then evaluates and writes the formatted heading and detail lines. Finally, it writes a fixed limitation statement and reaches the end of the file.

| Stage | Data or operation | Result |
|---|---|---|
| Define the example | Academy, student, course, request topic and review state | Five in-memory string values |
| Build the heading | Insert academy_name into the heading | Identifies the example organization |
| Build the detail lines | Insert the corresponding value into each label | A consistent support briefing |
| State the boundary | Print a fixed limitation sentence | No implied external verification |
| Finish the process | Reach the end without an unhandled error | Successful process exit |

The application has no input form. The values come from assignments in the source. It has no authentication, network calls, database, model, conditional approval or loop. You can identify what it does by following its statements instead of inferring capabilities from its subject matter.

The application reads its own source through the interpreter and writes terminal output. Python or the test runner may create ordinary cache or temporary files as part of execution, but the briefing itself does not intentionally create business records or send data to a service.

## 11. Output streams and exit status

A process has standard output, commonly called stdout, for ordinary output. It also has standard error, stderr, for diagnostic information. Your terminal normally displays both. Seeing text on the screen does not by itself establish which stream carried it.

print writes to stdout by default. An unhandled Python error normally produces a diagnostic traceback on stderr and a nonzero exit status. A successful run normally exits 0. The briefing is not configuring a logging system yet; later lessons will add explicit logging and machine-readable output contracts.

In Bash, echo $? prints the exit status of the immediately previous command. The dollar sign introduces expansion of the shell's special status value. Run it immediately after the command you are investigating. Running ls first would replace the status you meant to inspect.

Zero means the process completed successfully at that level. It does not prove a payment was checked, a business policy was satisfied or every output field was correct. You need both execution observations and behavior checks.

## 12. Recognize the failure boundary

A command-not-found message means the shell could not locate the selected executable. A cannot-open-file message means Python started but could not read the requested script path. A SyntaxError means the source could not be parsed correctly. A NameError means execution reached a reference to an undefined name.

These are different problems with different corrections. If the path is wrong, editing a valid print statement will not help. If a string quote is missing, installing another package will not correct it. Investigate the first relevant error, identify the boundary and make the smallest justified correction.

A traceback provides locations and an exception category. Read the final error line, then inspect the referenced source line and its context. Error wording and suggestion text can differ by Python version. Match the failure category and cause rather than memorizing a screenshot character for character.

## 13. Your first automated checks

The reference tests start the scripts as separate processes and compare actual results with requirements. They check the welcome output, the complete briefing and its ability to run by absolute path from another working directory. The test runner's implementation is explained in the walkthrough as a supported reference, not as a requirement to master Python classes on your first day.

The tests use subprocesses so they check the same executable boundary you use at the terminal. They inspect stdout, stderr and returncode. They include timeouts so a stuck process does not wait indefinitely in these checks.

A passing suite establishes only the checked behavior. It does not prove general input validation, provider integration, security or personal understanding. The application has no dynamic input contract yet, so the suite does not invent a large collection of name or payment-status variants.

## 14. Work with AI as a reviewer

You can ask AI to draft a briefing script or explain a traceback. Before accepting the result, check its responsibility, dependencies, side effects and claims. For this class, extra network packages, a payment API or a database would exceed the defined scope.

Read each assignment and print call. Ask where the displayed information comes from. Compare a generated explanation with the actual source. If the explanation says the code checked enrollment but the code only assigned text, reject that explanation.

Then run the implementation, compare its output with the requirements and investigate differences. Keep expected output separate from actual output. Never ask AI to manufacture a screenshot as evidence that a command ran.

## 15. Security and engineering judgment

Sarah is sample data. Use sample values rather than real student information in this public project. Do not put secrets in code, command history, screenshots or evidence files. No API key is necessary for this class.

The phrase Awaiting review is a supplied demonstration label. It is not fetched from a support database. The limitation sentence makes that boundary explicit to a reader. A future support agent must rely on authorized systems for consequential facts rather than treating generated language as permission.

Your professional habit begins here: describe what a component demonstrably does, explain what it cannot establish and define the next verification needed before adding an external action.

## 16. Key ideas to retain

Your editor saves instructions. Your interpreter executes saved instructions. Your shell chooses how to start a process and where relative paths begin. Your variables hold values during execution. Your f-strings insert those values into text. Your observations and tests check the resulting behavior.

You are not expected to memorize every command or reproduce the source from memory. You should be able to find the important line, explain it, run the correct file and investigate a simple failure independently.

## Further reading

Use these official references to revisit specific concepts. They supplement the teaching above rather than replace the guided class.

- [Python interpreter usage](https://docs.python.org/3.12/tutorial/interpreter.html).
- [Python introduction, strings and assignment](https://docs.python.org/3.12/tutorial/introduction.html).
- [unittest reference](https://docs.python.org/3.12/library/unittest.html).
- [subprocess reference](https://docs.python.org/3.12/library/subprocess.html).
