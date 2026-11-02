# 02. Guided Weekly Project

## 1. Prepare a project copy

From your veriqta-week-01 practice folder, create a separate integration folder. mkdir -p creates both nested directories and accepts an existing directory; it does not clear existing files. Inspect any previous contents first.

```bash
mkdir -p veriqta-support/03-source veriqta-support/04-tests
```

Now enter the integration directory. cd changes your shell's location. All remaining paths in this project lab are relative to this directory. If you are running the repository reference instead, select its 02-weekly-project directory as explained in the environment setup guide.

```bash
cd veriqta-support
```


From this weekly-project directory, inspect the source and test files. If you are building your own copy, create the same 03-source and 04-tests folders with mkdir -p. The folder names organize your project; the Python filenames remain importable. Preserve prior work rather than overwriting it blindly.

Use vi 03-source/student_support.py to enter or inspect the complete implementation linked from the project README. Read Lesson 05's walkthrough first. Use vi 04-tests/test_student_support.py to build the full tests after reading Lesson 06. Press i to edit, Esc to leave insertion mode and :wq to save/exit.

## 2. Run a valid request

```bash
python3 03-source/student_support.py --name Sarah --payment-status " Paid "
```

python3 selects the interpreter; the path selects the application. The two flags supply values. Quotes preserve the spaced label as one argument. You should see JSON with the approval message on stdout and an INFO diagnostic on stderr. No real access changes.

## 3. Run the whole suite

```bash
PYTHONPATH=03-source python3 -m unittest discover -s 04-tests -v
```

PYTHONPATH changes the import search path for this command only. -m starts unittest as a module. discover selects test files, -s supplies their directory and -v lists methods. Expect nine methods and OK. Runtime varies. A loading error or zero-test run is not a passing result.

## 4. Observe rejected input

```bash
python3 03-source/student_support.py --name Sarah --payment-status unknown
```

You supplied text outside the supported contract. Expect an error diagnostic, no stdout JSON and exit 2. Immediately run echo $? to inspect that status. Any intervening command replaces the previous status. Explain why unpaid instead produces a valid response and exit 0.

## 5. Capture a controlled failure and recovery

The optional evidence tool is supplied in the repository reference project. Run this section from that reference project directory, or reproduce its 06-evidence folder in your integration copy before using the path below. It expects the same sibling 03-source and 04-tests layout.

After understanding the source and tests, inspect the optional evidence runner. It copies the project into a temporary directory, captures results, removes lower only in that copy, checks the resulting test failure, restores source and verifies recovery. It refuses an existing destination to protect previous evidence.

```bash
python3 06-evidence/reproduce_evidence.py --output veriqta-project-evidence
```

--output names a new directory for actual records. The script uses a bounded subprocess timeout, records stdout/stderr and exit codes, and writes a success manifest only after the expected conditions occur. A failed check is an investigation result, not a reason to fabricate a manifest.

Inspect the saved regression and recovery records. Explain the affected inputs, the exact rule that rejects them after normalization is removed, and how the restored suite establishes the correction. Compare with the labeled reference visuals. They display actual captured output rather than synthetic terminal evidence.

## 6. Assess and present

Complete the weekly assessment and portfolio guide. Include your environment, code revision, exact commands, actual outputs, failure investigation and limitations. Do not claim real payment verification or production readiness. Publish your own work only after reviewing it for private information and credentials.
