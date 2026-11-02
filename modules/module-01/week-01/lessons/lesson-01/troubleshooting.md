# Troubleshooting

| Symptom | Likely cause | Investigation and correction | Verify |
|---|---|---|---|
| python3: command not found | Interpreter unavailable | Check environment setup and approved Python installation | python3 --version |
| Cannot open application file | Wrong working directory or path | Use pwd and inspect the lesson's src directory; select the documented directory | Run the documented CLI command |
| No module named student_support | src not on import path | Run from the lesson directory with PYTHONPATH=src | Run full unittest discovery command |
| Ran 0 tests | Wrong discovery directory or test filename | Confirm tests/test_student_support.py exists and use -s tests | Nine test methods are listed |
| IndentationError or SyntaxError | Paste or edit changed indentation/punctuation | Inspect the indicated line in vi and compare against complete source; use consistent four-space blocks | Run full suite |
| Required argument usage error | Missing or misspelled flag | Read python3 src/student_support.py --help; supply --name and --payment-status | Valid invocation exits 0 |
| Field cannot be empty | Input is empty or whitespace-only | Inspect supplied value; replace it with valid text rather than suppressing validation | Relevant valid and invalid tests pass |
| Unsupported payment status | Label outside the contract | Check intended source and supported labels; do not silently reinterpret unknown values as paid | Unknown still fails; supported values work |
| JSON parsing error | Logs or other prints reached stdout | Inspect stdout separately from stderr; keep diagnostics in logging | CLI JSON tests pass |
| Mixed-case input rejected after editing | Normalization regression | Inspect .lower() and compare against paid-variation tests | Entire suite passes after correction |
| cp -n portability warning | Tool warns about option portability | This is not a test failure; inspect whether the intended backup exists. Use cp -i for an interactive future copy | Compare original and backup contents before replacing either |

## Debugging workflow

Read the first relevant error, identify the failing input and component, explain the suspected cause, make one focused correction and rerun the relevant test. Once it passes, rerun the whole suite. Do not change expected results solely to hide a bug. Record actual evidence and redact environment identifiers before publication.
