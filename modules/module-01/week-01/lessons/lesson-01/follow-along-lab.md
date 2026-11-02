# Guided Follow-Along Laboratory

## 1. Inspect the environment

Run `python3 --version`. `python3` selects the interpreter and `--version` displays its version without running an application. Expect a Python 3 version; compare it with the tested versions in [verification](verification.md). A missing-command error means Python must be installed through the environment's approved setup process. Do not replace Ubuntu's system Python as part of this lab.

No packages, credentials, payment accounts or network services are needed by the application.

## 2. Obtain the classroom files

For a first checkout:

```bash
git clone https://github.com/veriqta/Agentic-AI-Engineering.git
cd Agentic-AI-Engineering
```

`git clone` downloads repository history and creates a local directory. `cd` changes the terminal's current directory; a successful cd usually prints nothing. If the directory already exists, inspect and use that checkout rather than cloning over it. When reviewing this PR before merge, select its feature branch in GitHub or use the branch checkout command provided by GitHub on the PR page.

From the repository root:

```bash
cd modules/module-01/week-01/lessons/lesson-01
```

This selects the lesson. All relative commands below assume this directory. Run `pwd` if unsure; it prints the current absolute directory, whose final component should be lesson-01.

## 3. Understand and preserve the baseline

Read [examples](examples/README.md). The simple scripts demonstrate interpreter execution, conditions and reusable functions. They are historical learning steps, not prerequisites to rerun if already understood.

If working with an existing student_support.py, preserve it before replacement. `cp -i student_support.py student_support_baseline.py` copies the source file and asks before overwriting an existing destination. Run it only in the directory containing that source. A missing-source error means the path is wrong; it is not a reason to create an empty replacement. The baseline included here uses Sarah as the public example name.

## 4. Build the application

The repository already includes complete runnable files. To follow the build actively, read [notes](notes.md) and [walkthrough](code-walkthrough.md), then open the implementation:

```bash
vi src/student_support.py
```

`vi` opens the source for inspection or editing. `src/` separates implementation from tests. Start with normalize_text, then check_payment, generate_response and main, in that order. Read each explanation before entering or changing that section. The imports and shared definitions appear at the top; the execution guard appears at the bottom.

The [full implementation](src/student_support.py) is the copyable reference. Do not overwrite an unreviewed existing file. For a blank file, press `i` to enter insertion mode, enter the complete reference, press Esc, then type `:wq` and Enter to save and exit. `:q!` exits without saving accidental edits.

Checkpoint: trace `"  Sarah  "` and `" Paid "` on paper. Name cleanup produces Sarah, status cleanup produces paid, and the payment comparison returns True. No actual payment provider is contacted.

## 5. Run a request

```bash
python3 src/student_support.py --name Sarah --payment-status " Paid "
```

Python executes the named file. `--name` supplies the student name; `--payment-status` supplies the simulated status. Quotes keep the spaces inside one argument so normalization can handle them. The parser passes these to the core functions.

Expected stdout:

```json
{"message": "Hello Sarah, your course access is approved."}
```

Expected stderr:

```text
INFO Support response generated.
```

Both streams appear in a terminal, but remain separate to calling programs. Record actual output before claiming verification. A usage error indicates missing or misspelled flags. A ValueError diagnostic indicates rejected input.

## 6. Build and run the tests

Open `vi tests/test_student_support.py`. Read [testing](testing.md), then implement the payment, response and subprocess tests using the [complete test source](tests/test_student_support.py). Each test has an acceptance criterion, not a requirement to memorize syntax.

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -v
```

`PYTHONPATH=src` adds the source directory to Python's import search path for this command only. `-m unittest` runs the built-in test runner. `discover` finds test files, `-s tests` selects their directory, and `-v` lists test names. No pip installation is required.

Expected summary:

```text
Ran 9 tests in ...
OK
```

Runtime varies. The nine methods include multiple subtest inputs. Failure output identifies the method and assertion; investigate rather than modifying expectations just to obtain green output.

## 7. Observe a failure without changing the code

```bash
python3 src/student_support.py --name Sarah --payment-status unknown
```

The input is text but outside the supported contract. Expect an ERROR diagnostic containing `Unsupported payment status.`, no stdout JSON and exit code 2. Immediately run `echo $?` to display the previous command's exit status. `$?` is a shell value, not application data; another intervening command would replace it.

These observations are examples to verify, not claims that a reader has already run them. Automated tests cover the input variations together.

## 8. Review, assess and document

Complete the [knowledge check](knowledge-check.md) before reading its separate answer guide. Follow the [assessment](practical-assessment.md), save genuine evidence and record actual environment and results. Do not publish terminal hostnames, cloud identifiers, credentials or unrelated personal content.

Prepare changes on a feature branch, run checks and open a PR. The owner reviews and merges. Lesson completion requires assessment evidence; a PR or successful run does not complete the module.
