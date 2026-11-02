# 06. Automated Testing Follow-Along Laboratory

## 1. Why test instead of changing tiny values manually?

Manual exploration helps reveal behavior, but repeated editing is slow and easy to forget. Tests record requirements as executable checks. This suite groups related variations and tests the actual CLI boundary as well as individual functions.

Function tests answer whether a helper behaves as required. Command-line tests answer whether the whole program accepts arguments, formats output and reports status correctly. Neither is a substitute for reasoning about real payment authority.

## 2. Numbered source and test files

The lesson source is `16-source/01_student_support.py`; tests are `17-tests/01_test_student_support.py`. File prefixes help readers follow the classroom order. A normal Python import statement cannot name a module starting with digits. This reference therefore uses the standard-library runpy loader and explains it explicitly.

`APP = Path(__file__).resolve().parents[1] / "16-source" / "01_student_support.py"` identifies the source relative to the test file. `runpy.run_path(str(APP))` executes its definitions with a non-main name and returns a dictionary. Looking up check_payment and generate_response retrieves the function objects. The execution guard prevents CLI argument parsing during this load. Do not use runpy to load untrusted arbitrary code: loading executes top-level code.

## 3. Create the test file

```bash
vi veriqta-practice/17-tests/01_test_student_support.py
```

vi opens the test file in the practice layout. Enter the full reference below, save and exit. The reference is complete; read its groups and explanations before treating it as learned.

```python
"""Tests for VERIQTA Academy student support automation."""

import json
from pathlib import Path
import subprocess
import sys
import runpy
import unittest

APP = Path(__file__).resolve().parents[1] / "16-source" / "01_student_support.py"
module = runpy.run_path(str(APP))
check_payment = module["check_payment"]
generate_response = module["generate_response"]


class PaymentTests(unittest.TestCase):
    def test_paid_variations(self):
        for status in ("paid", "Paid", "PAID", "  paid  "):
            with self.subTest(status=status):
                self.assertTrue(check_payment(status))

    def test_non_paid_statuses(self):
        for status in ("unpaid", "pending", "refunded"):
            with self.subTest(status=status):
                self.assertFalse(check_payment(status))

    def test_invalid_statuses(self):
        for status in ("", "   ", "unknown", None, 123):
            with self.subTest(status=status):
                with self.assertRaises(ValueError):
                    check_payment(status)


class ResponseTests(unittest.TestCase):
    def test_approved_response_and_name_cleanup(self):
        self.assertEqual(
            generate_response("  Sarah  ", " Paid "),
            "Hello Sarah, your course access is approved.",
        )

    def test_unpaid_response(self):
        self.assertEqual(
            generate_response("Sarah", "unpaid"),
            "Hello Sarah, please verify your payment.",
        )

    def test_invalid_names(self):
        for name in ("", "   ", None, 123):
            with self.subTest(name=name):
                with self.assertRaises(ValueError):
                    generate_response(name, "paid")


class CommandLineTests(unittest.TestCase):
    def run_app(self, status):
        return subprocess.run(
            [
                sys.executable,
                str(APP),
                "--name", "Sarah",
                "--payment-status", status,
            ],
            capture_output=True,
            text=True,
            check=False,
        )

    def test_successful_json_output(self):
        result = self.run_app("paid")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(
            json.loads(result.stdout),
            {"message": "Hello Sarah, your course access is approved."},
        )

    def test_unpaid_request_returns_valid_json(self):
        result = self.run_app("unpaid")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(
            json.loads(result.stdout),
            {"message": "Hello Sarah, please verify your payment."},
        )

    def test_invalid_request_has_no_success_output(self):
        result = self.run_app("unknown")
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, "")
        self.assertIn("Unsupported payment status.", result.stderr)


if __name__ == "__main__":
    unittest.main()
```

## 4. Understand the imports

json parses actual output. Path locates the source. subprocess starts the CLI in a separate process. sys.executable chooses the interpreter running the tests. unittest provides the runner and assertions. runpy loads the numbered source without invoking its guarded main. No network or package installation is used.

## 5. Understand test classes and self

Each class inherits unittest.TestCase, which supplies assertion methods. Test methods start with test_ so the runner can discover them. self refers to the particular test instance; using self.assertEqual calls its comparison helper. Object-oriented application design is not a prerequisite for understanding this test pattern.

PaymentTests checks policy decisions. ResponseTests checks composed messages and name validation. CommandLineTests checks the external program behavior. run_app is a helper, not a test, because its name does not begin with test_.

## 6. Understand grouped cases

A for loop supplies each related value in turn. with self.subTest(status=status) identifies the active case in failures without turning each variation into a separate test method. The paid examples cover case and outside spaces. The non-paid examples cover recognized negative results. Invalid examples cover empty, spaces-only, unknown, None and integer input.

A context manager such as with self.assertRaises(ValueError) sets an expectation for the enclosed call. The assertion passes when the expected exception occurs and fails when invalid input silently succeeds. It is not suppressing errors arbitrarily; it checks a deliberate contract.

## 7. Understand subprocess capture

The list passed to subprocess.run keeps executable, script, flags and values separate. Python does not request shell=True. This prevents the shell from interpreting supplied arguments as commands. capture_output collects streams, text requests string results, and check=False allows explicit assertions about failure codes.

result.returncode is the process status. result.stdout is application data. result.stderr is diagnostics. json.loads checks whether stdout is parseable JSON, and assertEqual compares the resulting dictionary with the expected structure. The unknown-input test also asserts empty stdout, preventing invalid requests from producing misleading success output.

## 8. Run the practice suite

```bash
python3 veriqta-practice/17-tests/01_test_student_support.py -v
```

python3 starts the interpreter and executes the numbered test file directly. The final unittest.main guard starts its test runner. -v requests method names and outcomes. Direct execution avoids discovery rules that skip Python filenames beginning with digits. Quoting a wildcard would not fix that module-name restriction. This layout honors numbered classroom files while making the invocation explicit.

Expected result: nine methods, all successful, ending with OK. Runtime varies. Compare the [reference execution capture](19-images/02-test-suite.svg). A failed or missing discovery run does not count as a passing suite.

For the repository reference layout, use:

```bash
python3 17-tests/01_test_student_support.py -v
```

No PYTHONPATH setting is needed because runpy loads the source by its explicit path. This differs from the earlier unnumbered classroom layout and is tested separately.

## 9. What each method establishes

| Test | Acceptance criterion |
|---|---|
| test_paid_variations | Paid case/space variations return True |
| test_non_paid_statuses | Recognized non-paid labels return False |
| test_invalid_statuses | Malformed or unsupported values raise ValueError |
| test_approved_response_and_name_cleanup | Correct message contains trimmed Sarah |
| test_unpaid_response | Correct verification message is returned |
| test_invalid_names | Invalid names raise ValueError |
| test_successful_json_output | Paid CLI exits 0 and emits expected JSON |
| test_unpaid_request_returns_valid_json | Unpaid CLI exits 0 and emits expected JSON |
| test_invalid_request_has_no_success_output | Unknown CLI exits 2, emits no JSON and explains failure |

## 10. Interpret failure instead of hiding it

A syntax error means Python could not parse source. An import/loading error means the test module could not be prepared. An assertion failure means execution reached a check but observed behavior differed. Each requires a different investigation. Do not edit the expected result just to make a faulty application appear correct.

## 11. Coverage limits

These nine methods cover defined examples. They do not test every parser error, all Unicode behavior, external payments, network timeouts, permissions, persistence, deployment or full security. No percentage coverage or production readiness is claimed. Extra tests should correspond to meaningful requirements.

## 12. Meaningful assessment checkpoint

Explain why unpaid succeeds as a process while unknown fails as input. Identify which assertion would detect JSON polluted with logs. Then proceed to the weekly project and bounded debugging exercise. Evidence of nine tests alone does not complete the lesson.
