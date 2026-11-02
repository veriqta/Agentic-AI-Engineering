# 03. Application and Test Code Walkthrough

Open the complete source beside this page. Follow each value and operation. You are learning to review the implementation, not memorize it.

## 1. The welcome script

```python
# Introductory Python execution example. No model or agent loop is used.
print("Welcome to Agentic AI Engineering")
```

The comment documents the script's limited purpose. # begins a comment outside a string. It does not change the runtime result. print names a built-in function. The parentheses call it. The double quotes delimit one string argument. The function writes that string to stdout and adds a newline by default.

There is no assignment, branch, custom function, import or loop in this file. The application finishes after print returns. The filename does not add agent capabilities. If you omit a closing quote or parenthesis, the file can fail to parse before the print call executes.

## 2. The complete briefing

```python
"""Display a simulated VERIQTA Academy support request briefing."""

academy_name = "VERIQTA Academy"
student_name = "Sarah"
course_name = "Agentic AI Engineering"
request_topic = "Course access"
request_status = "Awaiting review"

print(f"{academy_name} | Student support briefing")
print(f"Student: {student_name}")
print(f"Course: {course_name}")
print(f"Request: {request_topic}")
print(f"Status: {request_status}")
print("No payment or enrollment checks have been performed.")
```

### The module description

The first line is a triple-quoted string at the start of the module. It is the module docstring, a description available to readers and documentation tools. Triple quotes delimit that string. The presence of a docstring does not automatically print it.

The word simulated is intentional. A person reviewing this code should not infer that the displayed fields came from an authorized support system.

### academy_name assignment

academy_name is a descriptive variable name. = binds it to the string VERIQTA Academy. The quoted organization name is data. This assignment produces no visible output. Later, the heading print uses this value.

### student_name assignment

student_name is bound to Sarah, a sample name. The variable is not a form field, database query or user account. No student is authenticated. Its value exists because the source explicitly assigned it.

### course_name assignment

course_name holds the course's display text. Keeping it under a descriptive name allows you to trace the source of the Course line. You are not yet creating a course object or checking enrollment in it.

### request_topic assignment

request_topic holds Course access. The topic describes the question. It does not encode an approval decision. Separating topic from state avoids treating the mere presence of an access request as permission to grant it.

### request_status assignment

request_status holds Awaiting review. This is also sample data. It describes a displayed review state but is not fetched from a queue or database. A future integration must define who can establish or change that state.

### Blank lines

Blank lines visually separate setup from presentation. They help a reader follow responsibilities. They do not instruct Python to wait, print spacing or end a process.

### Heading print

```python
print(f"{academy_name} | Student support briefing")
```

Python evaluates the formatted string before print receives it. The expression academy_name inside braces supplies the organization. The vertical bar and the remaining words are literal characters in the string. Because they are inside the source string, the bar is not a shell pipeline operator.

### Student print

```python
print(f"Student: {student_name}")
```

The fixed prefix identifies the field. The brace expression supplies Sarah. If you remove f, the braces and name are displayed literally. If you misspell the name inside the braces, Python raises NameError when evaluating that expression.

### Course, request and status prints

Each of the next three print calls follows the same pattern. Read them together as one concept. course_name supplies the Course line, request_topic supplies the Request line and request_status supplies the Status line. You do not need a separate exercise for every minor text substitution.

The order of the statements determines the order of these output lines. A consistent report is easier for a person to review, and the test contract checks that presentation order intentionally.

### Boundary statement

```python
print("No payment or enrollment checks have been performed.")
```

This line is an ordinary string, so it needs no f prefix. It states a real limitation of the code. The application contains no provider request or enrollment lookup. Keeping this sentence in the output helps prevent a briefing from being mistaken for an authorization result.

## 3. Follow the values through execution

| Name | Assigned value | Where you observe it |
|---|---|---|
| academy_name | VERIQTA Academy | Heading |
| student_name | Sarah | Student line |
| course_name | Agentic AI Engineering | Course line |
| request_topic | Course access | Request line |
| request_status | Awaiting review | Status line |

Python creates these name bindings when it executes the assignments. It then evaluates each print argument and writes the resulting string. There is no return value from a custom application function because you have not defined one here. print itself returns None, but this script does not store or use that result.

The operating system receives an exit status when Python finishes. That process status is separate from the text printed by the application. Echoing $? asks the shell for that status, not for a Python variable.

## 4. Inputs, outputs and side effects

| Boundary | This implementation |
|---|---|
| Business input | Fixed sample assignments in source |
| Runtime instruction | A script path passed to Python |
| Main output | A six-line text briefing on stdout |
| Normal stderr | Empty for the successful reference run |
| Business side effect | No enrollment, payment or messaging operation |
| Persistence | No database or intentional business-file storage |
| External dependencies | No third-party package or service |

Running through Python requires the interpreter to read the source. Redirecting stdout in your shell writes an output file, but that is the shell command's chosen output handling, not a database feature hidden in the briefing.

## 5. Why keep this implementation simple?

A web form, framework or model call would introduce extra boundaries before you understand ordinary execution. This script lets you account for every displayed value. Later classes will introduce functions when repeated responsibilities need names, validation when input can vary, and external systems when authoritative facts are required.

For now, top-level execution is deliberate. Importing support_briefing.py would run its print statements. The tests therefore execute it as a script instead of importing it as a reusable library. A later refactoring will introduce a main function and execution guard when import safety becomes a learning objective.

Do not describe this as production-ready. Its useful engineering outcome is a small, inspectable component with a defined output contract.

## 6. Understand the automated checks without memorizing their framework

The complete [test file](project/test_day01.py) uses Python's standard library. Its job is to execute the same files you run manually and compare the real result with requirements.

| Test-code element | Responsibility |
|---|---|
| pathlib.Path | Builds paths from the test file's location |
| subprocess | Starts Python as a child process |
| sys.executable | Selects the interpreter already running the tests |
| tempfile | Provides a disposable working directory for the portability check |
| unittest | Supplies discovery, assertions and result reporting |
| SOURCE | Refers to the folder containing the test and application files |
| EXPECTED_BRIEFING | States the required six output lines independently of the script |

Path(__file__) identifies the test file. resolve makes its path absolute. parent selects the folder holding that file. Because the application files sit beside the test file, SOURCE points to all three without a numbered directory or a guessed caller location. In your practice work, that folder is veriqta-day-01.

The class inherits unittest.TestCase to obtain assertion methods. A method is a function defined inside a class. self refers to the current test instance. You are not expected to design an object-oriented application today; these few constructs support the supplied checks and will be revisited as your Python skills develop.

### run_program helper

The helper receives a source filename and an optional working directory. It calls subprocess.run with a list whose first item is sys.executable and whose second is the script's absolute path. The list keeps arguments separate without invoking a shell. No shell=True setting is used.

capture_output=True records stdout and stderr separately. text=True asks for decoded text rather than bytes. check=False allows assertions to inspect an unsuccessful process instead of immediately raising for its status. timeout=10 limits the wait for this small local script. A timeout is an execution error to investigate, not a passing test.

### Welcome test

The first test executes first_agent.py. It checks exit 0, the exact welcome text including its newline, and empty stderr. This proves the defined welcome behavior in that run. It does not prove that a model or agent loop exists.

### Briefing test

The second test executes support_briefing.py. It checks exit 0 and empty stderr. It uses splitlines to compare the actual output with the six required lines. The expected list is written as a contract in the test rather than imported from the application. This helps detect a changed or missing field rather than letting the application define its own expected result.

The limitation statement is part of that contract because the report must not imply a verification it did not perform.

### Different-directory test

The third test creates a temporary directory and runs the briefing from there using its absolute source path. It checks the same successful contract. This exposes an accidental dependence on the shell's location if one is introduced later. The temporary directory is cleaned up by its context manager.

### Test runner guard

The final comparison checks whether the test file is being run directly. If so, unittest.main starts the runner. The documented unittest command loads the named test_day01 module and finds its test_ methods without that direct-execution branch running. Imports, classes and this guard are explained here only to make the verification reference readable; the core application remains ordinary assignments and output.

## 7. Review a proposed change

Before accepting an AI-generated revision, identify which requirement it serves. A request to display sample fields does not require a network client or a secret key. A variable named verified_payment is not evidence of an actual lookup. A successful print is not permission to grant access.

Review the code change, predict the output, run the checks and investigate any failure. Keep the contract unless the requirement itself has legitimately changed. Changing expected output merely to conceal a bug defeats the purpose of verification.
