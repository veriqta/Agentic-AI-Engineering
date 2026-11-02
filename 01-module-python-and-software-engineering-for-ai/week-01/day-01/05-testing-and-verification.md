# 05. Testing and Verification

## 1. Start from requirements

You need evidence that the scripts execute and produce the specified behavior. The welcome script should print one exact welcome message. The briefing should print six specified lines, including its explicit verification limitation. Both should finish successfully without unexpected diagnostics.

You also need to understand location dependence. Running a file by relative path requires the right current directory. Once Python receives the correct absolute script path, this application should not require a particular working directory because it opens no additional application files.

The three reference tests check these requirements through real subprocess execution. They do not invent name, payment or user-input cases for an application that accepts no such runtime inputs yet.

## 2. Prepare the test file

Continue in your practice day directory from the lab, containing 09-source and 10-tests. If you use the repository reference instead, start in this day-01 directory. In either case, the source and tests must keep the same sibling-folder layout.

vi opens the test file. Enter insertion mode with i, save the complete implementation, then use Esc and :wq followed by Enter. Inspect an existing file before replacing it.

```bash
vi 10-tests/test_day01.py
```

The complete test implementation follows. Read its [walkthrough](03-code-walkthrough.md) to understand the process calls, paths and assertions. You may use the supplied implementation while learning how it works. You do not need to invent a testing framework or memorize class syntax on Day 01.

```python
"""Check the public Day 01 scripts through their process interface."""

from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

DAY = Path(__file__).resolve().parents[1]
SOURCE = DAY / "09-source"
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

## 3. Understand the discovery command

python3 selects the interpreter. -m asks Python to run a module, here the built-in unittest runner. discover searches for test files. -s supplies the starting directory, 10-tests. -v requests individual test names and outcomes. The file test_day01.py matches the conventional discovery pattern.

Run this from the day directory. The -s argument is a relative path, so it depends on this starting location. The tests themselves resolve the application paths from the test file's location.

```bash
python3 -m unittest discover -s 10-tests -v
```

Expected summary:

```text
Ran 3 tests in <variable duration>

OK
```

The duration, line wrapping and some diagnostic wording depend on your environment. Expect three named methods. A zero-test run is not proof that the application passed. An import error, assertion failure or process timeout needs investigation.

## 4. Interpret the result

| Observation | What it means | Your next action |
|---|---|---|
| Three methods and OK | The checked requirements passed in this run | Record the actual command and summary |
| Ran 0 tests | No matching tests were discovered | Inspect the directory, filename and test_ method names |
| Assertion failure | Actual behavior differed from an expectation | Compare the expected contract with the actual source/result |
| Error or traceback | Execution or test setup could not complete normally | Read the final exception and inspect its boundary |
| Timeout | A bounded subprocess did not finish in time | Investigate the command and environment before increasing limits |

The runner normally reports progress on stderr. That does not mean each application produced an error. The tests capture their child processes' streams and assert that successful application stderr is empty.

## 5. Test a controlled regression

A suite is more convincing when it detects an actual defect. The optional reference evidence tool performs this investigation in a temporary copy: run the working scripts, run the tests, introduce an undefined student variable, observe failure, restore source and rerun the suite.

Inspect [reproduce_reference.py](15-evidence/reproduce_reference.py) before executing it. Run this optional section from the repository's day-01 directory, where the tool and its sibling source/test folders exist. If you only created the practice source and tests manually, you can instead perform the isolated debugging exercise in the practical assessment.

python3 starts the tool. --output names a new result directory. The tool refuses an existing destination so that earlier evidence is preserved. Its internal commands run with bounded timeouts.

```bash
python3 15-evidence/reproduce_reference.py --output veriqta-day01-evidence
```

Expect a success message only after the tool has checked the normal contract, detected the deliberate regression and verified recovery. Inspect its JSON records for the actual streams and exit codes. The source in your reference day folder is not edited by the regression step.

## 6. Explain what passing does not establish

The checks do not prove input validation, model accuracy, payment truth, authentication, network reliability or production readiness. The program has no external-system boundary yet. They also do not demonstrate your own understanding.

The suite checks a presentation contract intentionally. If requirements later change, review both the implementation and the contract. Do not change the expected fields simply to make a misspelled variable or missing output line appear correct.

## 7. Record your own verification

Keep your actual Python version, source revision or saved files, exact command, test count and outcome. Save any failure and its correction. Use screenshots only from genuine execution, remove sensitive context and retain text output when possible. Reference output panels show what actually ran in the reference environment; they are not your assessment evidence.
