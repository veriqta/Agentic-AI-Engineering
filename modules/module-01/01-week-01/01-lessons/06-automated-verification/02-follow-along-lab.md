# 02. Guided Automated Testing Lab

## 1. Select the project layout

Open the [weekly project](../../02-weekly-project/README.md). Its 03-source directory contains student_support.py and 04-tests contains test_student_support.py. Conventional Python filenames allow normal imports and test discovery. Folder numbering supplies your reading order without changing Python module rules.

## 2. Read and save the tests

Use vi to create 04-tests/test_student_support.py in your project copy. Read the notes and walkthrough before executing it. The full reference follows.

```python
"""Tests for VERIQTA Academy student support automation."""

import json
from pathlib import Path
import subprocess
import sys
import unittest

from student_support import check_payment, generate_response

APP = Path(__file__).resolve().parents[1] / "03-source" / "student_support.py"


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

## 3. Run the suite

From the weekly project directory:

```bash
PYTHONPATH=03-source python3 -m unittest discover -s 04-tests -v
```

PYTHONPATH=03-source adds the source directory to the import path for this command only. python3 -m unittest runs the built-in runner. discover finds test files, -s selects 04-tests, and -v lists method names. The conventional test_ filename matches discovery without special loaders or filename patterns.

Expected summary:

```text
Ran 9 tests in ...
OK
```

Timing varies. The suite groups related variations in subtests, so nine methods check more than nine individual values.

## 4. Interpret before accepting

Find a function assertion, an expected exception and a subprocess assertion. Explain what each would catch. A loading error differs from an assertion failure. Do not change an expected value only to make defective code pass. Use the weekly project's controlled regression to investigate a real failure and recovery.
