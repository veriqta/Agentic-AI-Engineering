# 06. Reference Verification Record

You can compare your results with the actual reference run in [01-reference-run](01-reference-run/08-manifest.json). These records establish technical behavior in the recorded environment; they do not assign a learner grade or demonstrate a real payment integration.

## Actual checks

| Check | Recorded result |
|---|---|
| Normalized valid request | Exit 0 and expected approval JSON |
| Automated suite | Nine test methods passed |
| Unknown status | Exit 2, empty stdout and expected error diagnostic |
| Controlled regression | Removing lower() in a temporary copy made the suite fail |
| Restoration | All nine methods passed after source restoration |

Read the [environment and source hashes](01-reference-run/02-environment.json), [successful request](01-reference-run/03-success.json), [tests](01-reference-run/04-tests.json), [invalid request](01-reference-run/05-invalid.json), [regression](01-reference-run/06-regression.json) and [recovery](01-reference-run/07-recovery.json). Timings and temporary paths vary between runs.

## Reproduce the record

Inspect [reproduce_evidence.py](reproduce_evidence.py) before running it. From the weekly-project directory, python3 starts the interpreter, the path selects the evidence tool, and --output selects a new destination. The destination must not already exist. The runner copies source and tests to a temporary folder, captures separate output streams and exit codes, and applies the deliberate defect only to that copy. The reference source remains intact.

```bash
python3 06-evidence/reproduce_evidence.py --output veriqta-project-evidence
```

Expect a completion message only when the reference contract, regression detection and recovery checks succeed. Inspect the resulting JSON files rather than relying on the message alone. The runner checks that the suite reports nine methods, preventing a zero-test discovery run from being accepted as success. Its subprocess calls have a 30-second timeout.

[render_output_panels.py](render_output_panels.py) turns the bundled raw results into SVG panels. It requires only Python's standard library. Its paths target this bundled run; it does not select your new evidence directory automatically. The panels label their origin and retain exact output excerpts. They are rendered execution records, not terminal photographs.

## Limits

This run used the Python version recorded in the environment file. It does not establish compatibility with every Python release or machine. The code has no model, payment provider, persistent store, authentication or deployment. CLI missing-option coverage and broader security tests remain future improvements. Your understanding and practical assessment require your own work, even when reference tests pass.
