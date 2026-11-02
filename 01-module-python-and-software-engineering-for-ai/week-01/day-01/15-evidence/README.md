# 15. Reference Execution Evidence

This record establishes the local reference behavior for Day 01. It does not grade an individual learner or claim that a real support system was contacted.

## Actual captured checks

| Check | Actual reference result | Record |
|---|---|---|
| Environment and source identity | Recorded Python version, operating-system family and SHA-256 file hashes | [Environment](01-reference-run/01-environment.json) |
| First program | Expected welcome, empty stderr and exit 0 | [Welcome](01-reference-run/02-welcome.json) |
| Support briefing | Six-line contract, empty stderr and exit 0 | [Briefing](01-reference-run/03-briefing.json) |
| Automated verification | Three methods passed | [Tests](01-reference-run/04-tests.json) |
| Missing path | Nonzero exit, no stdout and a missing-file diagnostic | [Path failure](01-reference-run/05-missing-path.json) |
| Controlled source defect | NameError detected by the three-method suite | [Regression](01-reference-run/06-regression.json) |
| Restored source | All three methods passed again | [Recovery](01-reference-run/07-recovery.json) |
| Completed capture checks | Manifest written after the required conditions succeeded | [Manifest](01-reference-run/08-manifest.json) |

The actual version is in the environment record. This run does not demonstrate compatibility with every supported Python release or system. Temporary paths and execution durations will vary.

## Reproduce the investigation

Inspect [reproduce_reference.py](reproduce_reference.py). It copies source and tests into a temporary directory, runs bounded subprocesses and records arguments, stdout, stderr and exit status. It deliberately misspells the Student field's variable in that temporary copy, confirms NameError appears in a failing suite, restores the source and confirms three methods pass again. It does not edit the original application.

From the repository's day-01 directory, python3 selects the interpreter, the next path selects the evidence tool, and --output names a new destination. The tool refuses an existing destination to preserve prior records.

```bash
python3 15-evidence/reproduce_reference.py --output veriqta-day01-evidence
```

Expect a completion message only after the requirements are checked. Read the saved records instead of relying on the message alone. The tool checks the discovered method count as well as process status, so a zero-test success does not satisfy its reference-suite condition. Its outer subprocess timeout is 30 seconds; child application tests use 10 seconds.

The tool's hashes identify the application and test files used. Hashes establish identity, not safety or correctness. Review the corresponding source and results together.

## How the comparison panels are produced

[render_panels.py](render_panels.py) reads the bundled raw records and generates the four [output panels](../14-images/README.md) using Python's standard library. It does not invent stdout, diagnostics or test results. It abbreviates the command's interpreter label for display and labels any excerpt. The panels use Arial at 1080 by 1350 pixels.

If you rerender the bundled records, python3 starts the utility and the following path selects it. Run from the day directory. It overwrites the four generated SVG files, so retain any versions you intend to compare first.

```bash
python3 15-evidence/render_panels.py
```

This renderer reads the bundled 01-reference-run directory. It does not automatically select a new evidence directory you created. Inspect its path constants before adapting it to a different run. These utilities support reproducibility after the core class; understanding their complete implementation is not a prerequisite for your first print statement.

## Evidence boundaries

Expected results in the lab are instructional predictions. The JSON files here contain actual reference observations. Your own results need your own execution and review. A reference pass does not establish your understanding or practical-assessment completion.

The scripts use sample assignments and no model, payment provider, enrollment system, authentication or database. Nothing in this record establishes production readiness. Public evidence must omit secrets and unnecessary account or infrastructure details. No private learner screenshot is included.
