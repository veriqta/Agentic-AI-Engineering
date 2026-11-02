# 04. Complete Follow-Along Project. Your First Support Briefing

## What you will build

You will build this project from an empty practice folder to a working, tested application. No Python knowledge or existing source folder is assumed. Follow each command in order. Read its explanation first and compare the real result with the expected behavior after execution.

At VERIQTA Academy, Sarah asks for help with course access. A support worker needs a consistent briefing before investigating the request. Your program will display the academy, student, course, request and supplied review state. It will explicitly state that no payment or enrollment checks occurred.

## Requirements and architecture in ordinary language

A source file is a saved text file containing Python instructions. An interpreter is the program that executes those instructions. Your shell starts the interpreter. Your application prints a report. A separate test file starts the scripts and checks the report against requirements.

Your practice folder will contain first_agent.py, support_briefing.py and test_day01.py directly beside one another. It will later also contain your README.md and captured output. You will not create a folder named source, project, 09-source or 10-tests. Python does not require such a folder name.

The repository stores its reference copies in a folder named project so visitors can find them together. That repository label is not part of the command you type from your own practice folder.

## Before the commands

Complete the [Ubuntu Python setup guide](00-ubuntu-python-setup.md) if needed. It installs Python 3.15.2 separately from Ubuntu's system files and explains how to select it in your current shell. If your environment already meets that requirement, use it. Do not type a displayed shell prompt or expected-output block as a command.

## 1. Confirm Python

python3 selects the interpreter. --version requests its version, rather than executing a source file.

```bash
python3 --version
```

Expected result. The selected interpreter should print Python 3.15.2. If it does not, complete the setup guide or repeat its PATH selection step before continuing.

## 2. Create one ordinary project folder

mkdir means make directory. A directory is a folder. -p allows an existing folder and creates missing parents. ~ expands to your home directory. This command does not remove earlier files.

```bash
mkdir -p ~/veriqta-day-01
```

Expected result. Normally no text, followed by the shell prompt. Quiet success is normal. If the folder already holds work, inspect it and preserve it.

## 3. Enter that folder

cd means change directory. It changes where this terminal interprets relative filenames. It does not move or copy your files.

```bash
cd ~/veriqta-day-01
```

Expected result. Normally no text. Your shell is now working inside veriqta-day-01. A no-such-directory error means the preceding step or selected path needs investigation.

## 4. Confirm your location

pwd means print working directory. It displays the absolute location where you are now working.

```bash
pwd
```

Expected result. An absolute path ending in /veriqta-day-01. On a typical Ubuntu account it may look like /home/ubuntu/veriqta-day-01, but your account-specific prefix can differ.

## 5. Inspect existing files

ls lists visible filenames in the current folder. Check before opening a file so you do not overwrite previous work blindly.

```bash
ls
```

Expected result. A newly created empty folder normally produces no listed filenames. If files are already present, inspect them before editing. An empty listing does not mean mkdir failed.

## 6. Open your first Python file

vi opens a text editor for the named file. The .py ending indicates Python source. It is a filename, not an installation command.

```bash
vi first_agent.py
```

Expected result. The terminal switches into vi. A new or empty editing buffer is normal for a new file. It has not been saved or executed yet.

Press i to enter insertion mode, then enter the complete code below. # starts a human-readable comment. print calls Python's built-in output function. The quoted string is the text it will display.

```python
# Introductory Python execution example. No model or agent loop is used.
print("Welcome to Agentic AI Engineering")
```

Press Esc to leave insertion mode. Type :wq and press Enter to write the file and quit. Expect the terminal to return to the shell. These are editor actions, not text to put inside your Python file.

## 7. Read the saved file

cat displays a saved file as text. It does not run Python. This check confirms that the file on disk contains the intended instructions.

```bash
cat first_agent.py
```

Expected result. The comment and print statement above. If you see :wq or missing source, correct the file in vi before running it.

## 8. Execute the welcome script

The shell starts python3. Python opens first_agent.py from the folder you just entered. The print statement writes its message and the interpreter finishes.

```bash
python3 first_agent.py
```

Expected result. The following line, then a return to the shell.

```text
Welcome to Agentic AI Engineering
```

## 9. Create the actual briefing application

Open a separate file so the first exercise remains intact. This file will hold the project implementation.

```bash
vi support_briefing.py
```

Expected result. The editor opens a new file, or existing text if that name was already used. Inspect existing work before changing it.

Press i and enter the full implementation. The first line documents the file. Five assignments give descriptive names to sample text values. The f prefix on a string allows braces to insert a variable's value. The final print is fixed text stating the application's boundary. Read the [walkthrough](03-code-walkthrough.md) for a line-by-line explanation before execution.

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

Press Esc, then type :wq and press Enter. Expect a return to the shell after the file is saved. No support request has been processed merely by saving text.

## 10. Check the saved application

cat reads the file you just saved. Confirm the variable spellings, quotes and f prefixes.

```bash
cat support_briefing.py
```

Expected result. The complete source block above, including the explicit limitation sentence. It should show source code, not the generated briefing yet.

## 11. Run your project

python3 executes the saved application. The filename has no folder prefix because the file is directly inside your current folder.

```bash
python3 support_briefing.py
```

Expected result. Exactly this six-line report on stdout. There is no real payment or enrollment lookup.

```text
VERIQTA Academy | Student support briefing
Student: Sarah
Course: Agentic AI Engineering
Request: Course access
Status: Awaiting review
No payment or enrollment checks have been performed.
```

## 12. Check whether that process succeeded

echo displays its argument. $? expands to the exit status of the immediately preceding command. Run this immediately after the Python command.

```bash
echo $?
```

Expected result. 0 for the successful run. Zero means process success, not business authorization or proof that every conceivable behavior is correct.

## 13. Create the automated test file

The test file will sit beside the two scripts. You do not need a separate test directory. vi edits this new file.

```bash
vi test_day01.py
```

Expected result. An editor buffer for test_day01.py. You are creating a Python test script, not installing unittest.

Press i and enter the full tests below. They start your actual programs and compare stdout, stderr and exit status with requirements. Python includes unittest, so no package installation is required. The [walkthrough](03-code-walkthrough.md) explains the test helper and assertions; you do not need to invent a test framework or memorize class syntax today.

```python
"""Check the public Day 01 scripts through their process interface."""

from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SOURCE = Path(__file__).resolve().parent
EXPECTED_BRIEFING = [
    "VERIQTA Academy | Student support briefing",
    "Student: Sarah",
    "Course: Agentic AI Engineering",
    "Request: Course access",
    "Status: Awaiting review",
    "No payment or enrollment checks have been performed.",
]


class Day01ExecutionTests(unittest.TestCase):
    def run_program(self, filename, cwd=None):
        return subprocess.run(
            [sys.executable, str(SOURCE / filename)],
            cwd=cwd,
            capture_output=True,
            text=True,
            check=False,
            timeout=10,
        )

    def test_first_program_output(self):
        result = self.run_program("first_agent.py")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, "Welcome to Agentic AI Engineering\n")
        self.assertEqual(result.stderr, "")

    def test_briefing_contract(self):
        result = self.run_program("support_briefing.py")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.splitlines(), EXPECTED_BRIEFING)
        self.assertEqual(result.stderr, "")

    def test_briefing_from_another_working_directory(self):
        with tempfile.TemporaryDirectory() as temporary:
            result = self.run_program("support_briefing.py", cwd=temporary)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.splitlines(), EXPECTED_BRIEFING)
        self.assertEqual(result.stderr, "")


if __name__ == "__main__":
    unittest.main()
```

Use Esc, :wq and Enter to save and return to the shell.

## 14. Run the tests

-m asks Python to run a module. unittest is its built-in test runner. -v requests each test method name. test_day01 selects the test module from the current folder; omit the .py ending in this module argument.

```bash
python3 -m unittest -v test_day01
```

Expected result. Three named test methods, followed by Ran 3 tests in a varying duration and OK. Any FAIL, ERROR or zero-test result needs investigation. The summary normally appears on the test runner's stderr.

```text
Ran 3 tests in <variable duration>

OK
```

## 15. Capture your real application output

> redirects stdout into a file. It overwrites that filename if it already exists, so choose a fresh evidence filename if you need to keep an earlier record.

```bash
python3 support_briefing.py > briefing-output.txt
```

Expected result. Normally no report on screen because it went into briefing-output.txt. This is expected redirection, not proof of failure.

## 16. Inspect the capture

cat shows the actual text saved by the preceding application run. Do not type or paste the expected report into this file as if it were execution evidence.

```bash
cat briefing-output.txt
```

Expected result. The same six-line report shown in Step 11.

## 17. Observe an intentional missing-file error

This command selects a filename you have not created. It changes no source. The purpose is to recognize a path failure before trying to repair valid code.

```bash
python3 missing_briefing.py
```

Expected result. A diagnostic that Python cannot open missing_briefing.py because it does not exist. Exact paths and wording vary. This expected failure is part of the investigation, not a completed successful run.

## 18. Inspect the failed status immediately

Run this before another command replaces the shell's remembered status.

```bash
echo $?
```

Expected result. A nonzero status, normally 2 for this missing-script invocation. Record your actual result rather than fabricating a matching number.

## 19. Find the real filename

ls lists your current folder. Compare the names with the failed command.

```bash
ls
```

Expected result. The listing should include first_agent.py, support_briefing.py, test_day01.py and briefing-output.txt. Python may also have created __pycache__. The missing_briefing.py file should not be present unless you created it independently.

## 20. Verify the justified correction

Select the actual filename instead of editing correct application code.

```bash
python3 support_briefing.py
```

Expected result. The complete six-line report from Step 11. The correction was choosing the existing file, not changing a print statement or installing a package.

## 21. Document the project

A README is a text introduction for someone opening a project. vi creates your own project README beside the scripts.

```bash
vi README.md
```

Expected result. An editor buffer for README.md. Enter the following complete introduction, then save with Esc, :wq and Enter.

```markdown
# VERIQTA Academy Support Briefing

This educational Python project displays a simulated student-support request.
It does not check payment, query enrollment or grant course access.

## Files

- first_agent.py displays the introductory welcome.
- support_briefing.py displays the sample briefing.
- test_day01.py checks script behavior through real process execution.

## Run

From this project's directory, run python3 support_briefing.py.

## Test

Run python3 -m unittest -v test_day01.
The reference suite contains three test methods.

## Execution evidence

Record the actual Python version, exact commands, observed report,
test result and one diagnosed failure from your own run.
Keep expected output separate from actual evidence.

## Limits

All business data is assigned in source. There is no model, database,
payment provider, input form or external action.
```

## 22. Check the project introduction

cat displays the saved Markdown text. It does not publish to GitHub.

```bash
cat README.md
```

Expected result. The project introduction you entered. Fill your own execution record with actual observations before claiming a verified outcome. Saving a README is not a Git commit or push.

## Final project checkpoint

You now have a complete local Day 01 project: source, tests, documentation and an actual captured result. Explain where each displayed value comes from, why the missing-file command failed, and what your tests prove. Compare with the [reference output panels](14-images/README.md), which show genuine executions rather than invented terminal screenshots.

Complete the [knowledge check](07-knowledge-check.md) and [practical assessment](11-practical-assessment.md). Your project is verified only after you examine its real results; your understanding is assessed separately. This small first-day component contributes to the larger support toolkit. It is not yet an autonomous agent or production access-control system.
