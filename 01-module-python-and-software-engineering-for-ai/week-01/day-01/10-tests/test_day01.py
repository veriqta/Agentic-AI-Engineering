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
