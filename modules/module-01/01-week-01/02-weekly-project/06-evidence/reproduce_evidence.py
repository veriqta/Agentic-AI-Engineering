"""Capture real execution results without publishing host identifiers."""

import argparse
import hashlib
import json
from pathlib import Path
import platform
import os
import shutil
import subprocess
import sys
import tempfile

LESSON = Path(__file__).resolve().parents[1]
APP = LESSON / "03-source" / "student_support.py"
TESTS = LESSON / "04-tests" / "test_student_support.py"


def execute(arguments, directory):
    result = subprocess.run(
        arguments, cwd=directory, capture_output=True,
        text=True, check=False, timeout=30,
        env={**os.environ, "PYTHONPATH": "03-source"},
    )
    return {
        "arguments": arguments,
        "environment": {"PYTHONPATH": "03-source"},
        "exit_code": result.returncode,
        "stdout": result.stdout,
        "stderr": result.stderr,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    output = Path(args.output).resolve()
    if output.exists():
        parser.error("Choose a new output directory to preserve prior evidence.")
    output.mkdir(parents=True)

    def save(name, value):
        (output / name).write_text(json.dumps(value, indent=2) + "\n")

    save("02-environment.json", {
        "python": platform.python_version(),
        "system": platform.system(),
        "source_sha256": hashlib.sha256(APP.read_bytes()).hexdigest(),
        "tests_sha256": hashlib.sha256(TESTS.read_bytes()).hexdigest(),
    })
    with tempfile.TemporaryDirectory() as temporary:
        root = Path(temporary)
        shutil.copytree(LESSON / "03-source", root / "03-source")
        shutil.copytree(LESSON / "04-tests", root / "04-tests")
        cli = [sys.executable, "03-source/student_support.py", "--name", "Sarah"]
        suite = [sys.executable, "-m", "unittest", "discover", "-s", "04-tests", "-v"]

        success = execute(cli + ["--payment-status", " Paid "], root)
        save("03-success.json", success)
        if success["exit_code"] != 0 or json.loads(success["stdout"]) != {"message": "Hello Sarah, your course access is approved."}:
            raise RuntimeError("Successful request did not meet its contract.")

        tests = execute(suite, root)
        save("04-tests.json", tests)
        if tests["exit_code"] != 0 or "Ran 9 tests" not in tests["stderr"]:
            raise RuntimeError("Reference test suite failed.")

        invalid = execute(cli + ["--payment-status", "unknown"], root)
        save("05-invalid.json", invalid)
        if invalid["exit_code"] != 2 or invalid["stdout"] or "Unsupported payment status." not in invalid["stderr"]:
            raise RuntimeError("Invalid request did not meet its contract.")

        copy = root / "03-source" / "student_support.py"
        original = copy.read_text()
        copy.write_text(original.replace(".lower()", ""))
        regression = execute(suite, root)
        save("06-regression.json", regression)
        if regression["exit_code"] == 0:
            raise RuntimeError("The controlled regression was not detected.")
        copy.write_text(original)
        shutil.rmtree(root / "03-source" / "__pycache__", ignore_errors=True)
        recovery = execute(suite, root)
        save("07-recovery.json", recovery)
        if recovery["exit_code"] != 0 or "Ran 9 tests" not in recovery["stderr"]:
            raise RuntimeError("Restored implementation failed.")

    save("08-manifest.json", {
        "reference_tests_passed": True,
        "controlled_regression_detected": True,
        "recovery_tests_passed": True,
        "scope": "Local reference application only; no payment provider or deployment.",
    })
    print("Evidence captured. Reference passed; regression detected; recovery passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
