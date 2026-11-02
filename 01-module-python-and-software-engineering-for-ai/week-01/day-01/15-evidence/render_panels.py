"""Render captured Day 01 records into clearly labeled output panels."""

from pathlib import Path
import html
import json
import shlex
import textwrap

DAY = Path(__file__).resolve().parents[1]
RECORDS = DAY / "15-evidence/01-reference-run"
IMAGES = DAY / "14-images"


def read(name):
    return json.loads((RECORDS / name).read_text())


def command(record):
    return shlex.join(["python3"] + record["arguments"][1:])


def panel(filename, title, sections):
    elements = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1350" viewBox="0 0 1080 1350">',
        '<rect width="1080" height="1350" fill="#F2F7F3"/>',
        '<rect x="40" y="40" width="1000" height="1270" rx="18" fill="white" stroke="#B7CEC4"/>',
        '<g font-family="Arial, sans-serif" fill="#00382F">',
    ]

    def text(value, y, size=22, bold=False):
        weight = ' font-weight="700"' if bold else ''
        elements.append(f'<text x="70" y="{y}" font-size="{size}"{weight}>'
                        + html.escape(value) + '</text>')

    text("VERIQTA ACADEMY | AGENTIC AI ENGINEERING", 92, 22, True)
    y = 156
    for line in textwrap.wrap(title, 43):
        text(line, y, 36, True)
        y += 44
    text("Module 01, Week 01, Day 01", y + 10, 23)
    y += 53
    text("Actual execution, rendered output panel", y, 21)
    y += 37
    text("Python " + read("01-environment.json")["python"] + " | Linux reference run", y, 20)
    y += 49
    for label, value in sections:
        text(label, y, 22, True)
        y += 31
        for line in value.splitlines() or ["(empty stream)"]:
            for wrapped in textwrap.wrap(line, 86, replace_whitespace=False,
                                         drop_whitespace=False) or [" "]:
                text(wrapped, y, 19)
                y += 26
        y += 19
    if y >= 1220:
        raise RuntimeError(f"Panel content exceeds its readable area: {filename}")
    text("Captured subprocess output. This panel is not a terminal photograph.", 1250, 19)
    text("Raw commands, streams, status and hashes: 15-evidence/01-reference-run.", 1283, 18)
    elements.append('</g></svg>')
    IMAGES.mkdir(exist_ok=True)
    (IMAGES / filename).write_text("\n".join(elements) + "\n")


def main():
    briefing = read("03-briefing.json")
    panel("01-support-briefing.svg", "Your first support briefing", [
        ("Executed command, interpreter abbreviated", command(briefing)),
        ("Actual stdout", briefing["stdout"]),
        ("Actual stderr", briefing["stderr"] or "(empty stream)"),
        ("Actual exit status", str(briefing["exit_code"])),
        ("Scope", "Sample data only. No payment, enrollment or model service was contacted."),
    ])
    tests = read("04-tests.json")
    panel("02-three-tests.svg", "Verify three execution contracts", [
        ("Executed command, interpreter abbreviated", command(tests)),
        ("Actual test-runner output", tests["stdout"] + tests["stderr"]),
        ("Actual exit status", str(tests["exit_code"])),
    ])
    missing = read("05-missing-path.json")
    panel("03-path-error.svg", "Investigate a missing script path", [
        ("Executed command, interpreter abbreviated", command(missing)),
        ("Actual stdout", missing["stdout"] or "(empty stream)"),
        ("Actual stderr", missing["stderr"]),
        ("Actual exit status", str(missing["exit_code"])),
        ("Interpretation", "Python started but could not open the selected file. Inspect the location and filename before changing valid source."),
    ])
    broken = read("06-regression.json")
    recovered = read("07-recovery.json")
    error_lines = [line for line in broken["stderr"].splitlines() if "NameError:" in line]
    panel("04-regression-recovery.svg", "Detect a defect and verify recovery", [
        ("Controlled change in an isolated temporary copy", "The Student output referenced student_nam instead of student_name. The reference source was preserved."),
        ("Actual exception lines from the failing suite", "\n".join(error_lines)),
        ("Actual failing-run summary excerpt", "\n".join(broken["stderr"].splitlines()[-4:])),
        ("Actual failing exit status", str(broken["exit_code"])),
        ("Actual restored-run summary excerpt", "\n".join(recovered["stderr"].splitlines()[-4:])),
        ("Actual recovery exit status", str(recovered["exit_code"])),
    ])
    print("Rendered four panels from captured reference output.")


if __name__ == "__main__":
    main()
