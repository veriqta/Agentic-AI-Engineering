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
