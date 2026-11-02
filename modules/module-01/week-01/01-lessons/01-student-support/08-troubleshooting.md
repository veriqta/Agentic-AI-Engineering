# 08. Troubleshooting and Debugging Laboratory

## Diagnose by layer

First ask what failed: the shell locating a command, Python locating a file, Python parsing source, test discovery, input validation, a business decision or a test assertion. Read the earliest relevant message. Later messages may be consequences. Preserve the actual failure rather than replacing it with the expected output.

| Symptom | Meaning and investigation | Correction | Verification |
|---|---|---|---|
| python3: command not found | The shell cannot locate the interpreter; the application has not run | Use approved environment setup; check the remote host rather than assuming laptop software applies | python3 --version |
| No such file or directory | The named path is wrong from the current location | Run pwd and inspect ls; select the lesson directory | Run the original intended command |
| vi cannot save | Parent directory may not exist or permissions may prohibit writing | Check practice paths and ownership; do not run the whole lab as root to hide the cause | Save, reopen and inspect the intended file |
| SyntaxError | Python cannot parse a statement, quote or bracket | Inspect the reported line and preceding line against full reference | Run suite after correction |
| IndentationError | Block structure differs from valid Python indentation | Use consistent spaces and align function bodies, if branches and methods | Full suite passes |
| :wq appears as Python | Editor command was entered while still in insertion mode | Remove that source text; use Esc before editor commands | Script parses and tests run |
| Required argument usage error | argparse did not receive the required flags | Read --help and supply both options | Valid CLI emits expected JSON |
| payment_status must be text | A direct function call supplied a non-string | Inspect source of the value; do not coerce None into a convincing label | Invalid-input test remains rejected |
| Field cannot be empty | Empty or spaces-only text failed validation | Provide valid data or correct the upstream form; preserve validation | Valid request succeeds and empty input remains rejected |
| Unsupported payment status | Representation was text but outside supported labels | Check source contract and normalization; do not guess unknown means paid | Supported cases pass, unsupported still fail |
| Ran 0 tests | Discovery skips filenames starting with digits | Execute the numbered test script directly as documented | Nine method names appear |
| Test loading fails | Source path or function lookup is wrong | Inspect APP, the 16-source directory and runpy dictionary keys | Test suite starts and runs assertions |
| JSONDecodeError | stdout is not valid JSON | Look for extra print/log lines or empty output caused by failure | CLI JSON tests pass |
| A mixed-case test fails | Normalization may have been removed or applied after membership checking | Trace the failing input through strip, lower and membership | Restore intended order and rerun all tests |
| Evidence destination exists | Runner protects prior output | Select a new directory; inspect old records first | Fresh run writes a complete manifest |
| TimeoutExpired | Evidence subprocess exceeded its limit | Inspect the command, accidental loops or blocked code | Fix cause and rerun to a new destination |

## A complete controlled investigation

The weekly runner demonstrates a normalization regression in an isolated copy. Before running it, predict that mixed-case paid labels will be rejected. After execution, inspect 06-regression.json. Record the actual test names and why they failed. Compare 07-recovery.json after restoration. A test failure is useful evidence that a check detects the specified defect.

Do not report the expected failure as a surprise production incident. It is deliberately introduced for learning. Likewise, do not claim a reader performed the exercise merely because the reference bundle contains a publisher run.

## Debugging record template

Record the exact command, expected behavior, actual behavior, first relevant error, suspected cause, inspected code, focused correction and verification command. Include the result of the full suite after a focused test passes. Explain the connection between evidence and conclusion.

## When to stop

Stop before using credentials, changing system Python, deleting unreviewed directories or modifying a production host. This lab requires none of those actions. A command that seems to demand them probably signals an environment or path misunderstanding. Consult the setup and source instead of escalating privileges automatically.
