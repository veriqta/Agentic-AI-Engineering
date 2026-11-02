# 01. Teaching Notes: Verify the Application Automatically

You will test functions and the actual CLI, interpret failures and describe test limits.

## The VERIQTA Academy setting

Think of a support desk receiving information, making a decision and returning an answer. You will implement only the responsibility introduced in this lesson. The terminal supplies the input; there is no hidden web form or real payment connection.

## Automated tests as engineering evidence

A test states an expected behavior and checks actual behavior. Function tests call helpers directly. CLI tests start a separate process, capture stdout/stderr and inspect exit status. These levels can catch different defects: a correct function can still be wired incorrectly at the terminal boundary.

Assertions express acceptance criteria. assertTrue checks a true result; assertFalse checks a false result; assertEqual compares values; assertRaises expects an exception. subTest identifies cases inside one loop, keeping capitalization and whitespace examples together rather than creating many repetitive manual exercises.

Passing tests prove only the checked behavior for those inputs and environments. They do not prove all possible inputs, security, scalability or understanding. Test quality matters: an expectation copied from an incorrect implementation can preserve a bug. Define the business requirement before accepting an AI-written test.

## Subprocesses and paths in tests

subprocess.run starts another program and waits for it. The argument list contains the Python executable, application path and separate flags/values. No shell is requested, so these arguments are not treated as shell commands. sys.executable selects the interpreter running the suite.

capture_output=True captures stdout and stderr separately. text=True returns strings. check=False permits the test to inspect nonzero exit codes intentionally. Otherwise, raising on every nonzero code could interrupt a test designed to prove a controlled failure.

Path(__file__) identifies the test file. resolve creates its absolute path; parents[1] selects the weekly project directory from a file within 04-tests. Joining the numbered source directory and filename locates the application without relying on the caller's current directory for that subprocess path.

## Reviewing AI-generated software

Read generated code before running it. Identify what it reads, writes, starts or contacts. Inspect dependencies, subprocess invocation, credentials, exception handling and approval boundaries. Ask where each input comes from and what happens when it is missing, wrong or malicious.

Then review tests against requirements. Do they distinguish unsupported input from a negative business result? Do they verify stdout remains machine-readable? Do they cover failure paths? Does a change add a dependency or network call without explanation?

AI can accelerate drafting, but the engineer owns the decision to accept the code. Reproduce failures, inspect diffs and test corrections. Do not rewrite expected test results merely because generated implementation disagrees with them.

## Connect this milestone to agent engineering

A future agent needs reliable ordinary code to call. You are learning to state what a component accepts, returns and rejects. You will add a model only after you can explain the tool behavior and its trust boundaries. A simulated payment flag never establishes real payment authority.

## Before you execute

Read the full code, identify its inputs and outputs, and predict the normal result. If a name, operation or branch is unclear, revisit the relevant paragraph before running it. You do not need to memorize the script.

## Read a test as a small engineering argument

Each test starts with a requirement, supplies input, observes a result and asserts the expected behavior. PaymentTests checks the policy function. ResponseTests checks the composition of name validation and payment response. CommandLineTests launches the actual application to verify that the process boundary agrees with those helpers. These layers overlap deliberately: a correct helper can be connected to the wrong flag or output channel.

A test class inherits from unittest.TestCase to receive the assertion helpers and test-runner behavior. self refers to the current test instance. Method names beginning with test_ are discovered as tests. A for loop iterates through related inputs. with self.subTest records which input failed while allowing related cases to be reported together. The runner counts nine test methods, even though loops check more than nine values.

with self.assertRaises(ValueError) describes an exception as the expected outcome. If no exception occurs, the test fails. If an unrelated exception occurs, the test reports an error. That difference helps distinguish a missing validation rule from an accidental programming defect.

## Why test a subprocess?

The CLI is a process with arguments, streams and an exit status. Calling generate_response directly cannot prove that argparse reads the right flags, stdout contains valid JSON or the main guard correctly exits. subprocess.run starts the application using a list of arguments. Each list item is one argument; a value containing spaces remains a single item without shell quoting. sys.executable selects the Python interpreter running the tests, reducing interpreter mismatch.

The test captures both streams as text. check=False lets it inspect an intentional exit 2 instead of raising immediately for that status. The reference helper does not set a subprocess timeout; this is acceptable for the bounded local example, but a production integration test should specify an appropriate timeout. The evidence runner supplies a 30-second outer timeout for its captured commands. No real payment service is contacted.

## Discovery and imports are different responsibilities

unittest discover finds the test_student_support.py file in 04-tests. The import inside that file must separately find student_support.py in 03-source. PYTHONPATH=03-source provides that location for the one command. Without it, discovery may locate the test file and still fail with ModuleNotFoundError. A failed import is not a business-rule assertion failure.

The APP path uses __file__ to begin at the test file's location. resolve produces an absolute path. parents[0] is the 04-tests folder and parents[1] is the weekly-project folder. The / operators then append 03-source and student_support.py. This application path stays correct when the subprocess is launched from the intended project context. You still run discovery from the project root so its relative start directory and PYTHONPATH resolve correctly.

## Diagnose a regression using evidence

The project evidence runner removes lower() from an isolated copy. Exact lowercase paid still succeeds. Mixed-case labels now fail the membership check, so the relevant subtests and response test expose the defect. Inspect the actual error and traced line rather than assuming every failure is a bad expected value. Restore the implementation and rerun the full suite to check recovery.

Tests establish only their defined scope. They do not cover every Unicode name, missing CLI flag, concurrency scenario or upstream provider failure. You will strengthen coverage and structure progressively. For this week, the important habit is linking requirements to assertions, reading failures and verifying a correction without manufacturing evidence.
