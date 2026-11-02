# 03. Code Walkthrough: Verify the Application Automatically

Read the complete implementation in the guided lab beside this explanation. Follow the values and selected branches before changing code.

## Imports and application path

The test module imports json, Path, subprocess, sys and unittest from the standard library. It imports check_payment and generate_response normally from student_support. The command's temporary PYTHONPATH setting makes the project's 03-source directory discoverable. No dynamic loader is needed.

APP uses the test file's resolved path, selects its parent lesson-project directory through parents[1], then joins 03-source/student_support.py. This locates the application for subprocess tests regardless of the test runner's current path.

## Test organization

Each class inherits unittest.TestCase, which supplies assertions. self refers to the current test instance. Methods beginning with test_ are selected by the runner. PaymentTests groups decision cases, ResponseTests checks messages, and CommandLineTests checks the actual program. run_app is a helper because it does not start with test_.

## Assertions and subtests

assertTrue and assertFalse check Boolean outcomes. assertEqual compares actual and expected values. assertRaises(ValueError) expects the enclosed call to reject invalid input. A for loop groups related cases, and subTest identifies which value failed without making each variation a separate exercise.

## Command-line tests

subprocess.run receives an argument list with the current Python executable, application path and separate flags/values. No shell is requested. capture_output collects stdout/stderr separately, text makes them strings, and check=False allows assertions about deliberate nonzero exits. json.loads parses actual stdout before comparison. The unknown-input test requires exit 2, no stdout and the expected diagnostic.

## Runner and evidence

python3 -m unittest discover starts the built-in runner. -s selects 04-tests; -v lists method names. Conventional test_student_support.py matches default discovery. Nine methods contain multiple input cases, but they do not establish complete coverage, real payments or production readiness. The weekly project investigates a deliberate regression and records recovery separately.
