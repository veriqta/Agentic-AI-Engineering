# 05. Test Your Completed Project

## Where the files must be

Continue inside your own veriqta-day-01 practice folder. first_agent.py, support_briefing.py and test_day01.py must be directly beside one another. You do not need a numbered source folder, a separate test folder or a PYTHONPATH setting.

If you are reading the repository reference, its project folder contains the same three files. Open that folder only when running the reference copy. Your practice folder and the repository folder are separate locations with the same application layout.

## What the checks do

The welcome test checks the exact greeting, empty stderr and exit 0. The briefing test checks all six required output lines, empty stderr and exit 0. The third test starts the briefing by absolute path from a different temporary working directory and checks the same contract. These are three execution tests, not a claim of production readiness.

## Create the test file

vi opens a text file in your current folder. Press i, enter the complete code below, then save with Esc, :wq and Enter.

```bash
vi test_day01.py
```

Expected result. The editor opens for test_day01.py. After saving and quitting, the shell returns. The file must sit beside the two application scripts.

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

The [walkthrough](03-code-walkthrough.md) explains the paths, subprocess calls and assertions. The supported implementation lets you start verifying behavior while the course introduces deeper Python structure progressively.

## Run the checks

python3 is the interpreter. -m runs a module. unittest is the built-in test runner, not a package you must download. -v shows individual method results. test_day01 names the test file as a module, without its .py ending.

```bash
python3 -m unittest -v test_day01
```

Expected result. Three named methods should appear and the summary should report Ran 3 tests followed by OK. Duration varies. If any test reports FAIL or ERROR, keep the actual message and investigate it. A test-runner result on stderr is not automatically an application error; the tests separately inspect their child processes' streams.

## Interpret a problem

If the runner cannot import test_day01, inspect pwd and ls to confirm that you are in the folder containing that file. If it cannot open an application script, inspect whether all three files sit together. If an assertion fails, compare actual behavior with the requirement. Do not change expected values merely to accept incorrect source.

If you get a zero-test report, check the test method names and complete saved file. The reference has three methods beginning with test_. A zero-test success does not verify the application.

## Verify recovery from a real defect

The [practical assessment](11-practical-assessment.md) teaches a safe manual debugging copy. The optional [reference evidence tool](15-evidence/README.md) performs a similar investigation in an isolated temporary project, captures the failure and verifies recovery. The complete follow-along project supplies every core command, so this optional reference utility is not required just to build the application.

## Keep your own evidence

Record your actual Python version, source, exact command, complete test summary and any diagnosed failure. Expected output is a prediction; actual output comes from execution. A reference pass is not your personal assessment. These checks do not establish payment verification, enrollment authority, dynamic-input validation or deployment security.
