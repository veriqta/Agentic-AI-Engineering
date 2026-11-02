"""Capture genuine Day 01 execution, regression and recovery results."""

import argparse
import hashlib
import json
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import tempfile

DAY = Path(__file__).resolve().parents[1]
EXPECTED = [
    "VERIQTA Academy | Student support briefing",
    "Student: Sarah",
    "Course: Agentic AI Engineering",
    "Request: Course access",
    "Status: Awaiting review",
    "No payment or enrollment checks have been performed.",
]


def execute(arguments, directory):
    result = subprocess.run(
        arguments, cwd=directory, capture_output=True,
        text=True, check=False, timeout=30,
    )
    return {
        "arguments": arguments,
        "exit_code": result.returncode,
        "stdout": result.stdout,
        "stderr": result.stderr,
    }


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    output = Path(args.output).resolve()
    if output.exists():
        parser.error("Choose a new output directory to preserve earlier evidence.")
    output.mkdir(parents=True)

    def save(name, value):
        (output / name).write_text(json.dumps(value, indent=2) + "\n")

    files = [DAY / "09-source/first_agent.py",
             DAY / "09-source/support_briefing.py",
             DAY / "10-tests/test_day01.py"]
    save("01-environment.json", {
        "python": platform.python_version(),
        "system": platform.system(),
        "sha256": {str(p.relative_to(DAY)): hashlib.sha256(p.read_bytes()).hexdigest()
                   for p in files},
    })
    with tempfile.TemporaryDirectory() as temporary:
        root = Path(temporary)
        shutil.copytree(DAY / "09-source", root / "09-source")
        shutil.copytree(DAY / "10-tests", root / "10-tests")
        welcome = execute([sys.executable, "09-source/first_agent.py"], root)
        save("02-welcome.json", welcome)
        require(welcome["exit_code"] == 0 and welcome["stderr"] == "" and
                welcome["stdout"] == "Welcome to Agentic AI Engineering\n",
                "Welcome contract failed.")
        briefing = execute([sys.executable, "09-source/support_briefing.py"], root)
        save("03-briefing.json", briefing)
        require(briefing["exit_code"] == 0 and briefing["stderr"] == "" and
                briefing["stdout"].splitlines() == EXPECTED, "Briefing contract failed.")
        suite = [sys.executable, "-m", "unittest", "discover", "-s", "10-tests", "-v"]
        tests = execute(suite, root)
        save("04-tests.json", tests)
        require(tests["exit_code"] == 0 and "Ran 3 tests" in tests["stderr"],
                "Expected three passing test methods.")
        missing = execute([sys.executable, "09-source/missing_briefing.py"], root)
        save("05-missing-path.json", missing)
        require(missing["exit_code"] != 0 and missing["stdout"] == "" and
                "No such file" in missing["stderr"], "Expected missing-path failure.")
        source = root / "09-source/support_briefing.py"
        original = source.read_text()
        changed = original.replace('print(f"Student: {student_name}")',
                                   'print(f"Student: {student_nam}")', 1)
        require(changed != original, "Controlled mutation was not applied.")
        source.write_text(changed)
        regression = execute(suite, root)
        save("06-regression.json", regression)
        require(regression["exit_code"] != 0 and "NameError" in regression["stderr"] and
                "Ran 3 tests" in regression["stderr"], "Regression was not detected.")
        source.write_text(original)
        recovery = execute(suite, root)
        save("07-recovery.json", recovery)
        require(recovery["exit_code"] == 0 and "Ran 3 tests" in recovery["stderr"],
                "Restored source did not pass all three methods.")
    save("08-manifest.json", {
        "reference_tests_passed": 3,
        "controlled_name_error_detected": True,
        "recovery_tests_passed": 3,
        "scope": "Local sample briefing only; no model, payment or enrollment integration.",
    })
    print("Reference passed. NameError regression detected. Recovery passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
