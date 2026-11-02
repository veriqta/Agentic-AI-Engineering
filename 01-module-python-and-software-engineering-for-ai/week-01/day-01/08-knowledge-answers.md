# 08. Knowledge Answers and Explanations

Use these explanations after attempting the knowledge check. If an answer surprises you, revisit the relevant source or command and verify its behavior.

## 1. Executable and file

python3 selects the executable. support_briefing.py is an argument telling that interpreter which source file to open. The latter is a relative path interpreted from the shell's current directory. A correct interpreter name does not compensate for an incorrect script path.

## 2. Saving and publishing

vi saves source to a file in the current working environment. GitHub changes require a separate version-control and review workflow. Saving is not a commit, push or merge. If your shell is remote, the saved file belongs to that remote filesystem rather than automatically appearing on your laptop.

## 3. Path investigation

Use pwd to inspect the current directory and ls with the relevant directory to inspect actual filenames. Compare the selected path with the file's location and spelling. If Python cannot open the file, the failure occurs before that source is executed. Editing a valid print statement will not correct the caller's wrong location.

## 4. Assignment

The statement binds student_name to the string Sarah during this program's execution. It does not print, prompt for input or query a database. A later print call reads the value through its name. The value comes from the source assignment.

## 5. Formatted text

The f prefix enables expression substitution. The quotes delimit the string, and the literal Student: label describes the field. The expression student_name inside braces supplies the value Sarah. print receives the resulting string and writes it to stdout with a newline.

## 6. Missing f and correctness

Without f, a regular string displays the braces and variable name literally. That can be valid Python, so the process can finish with exit 0 while producing an incorrect field. Output-contract tests inspect behavior beyond process completion. This is one reason to define expected results before accepting generated code.

## 7. Misspelled variable

Expect NameError when Python evaluates an undefined name. Read the final exception line and inspect the referenced source line. Compare the name's use with its earlier assignment. Correct the spelling, save and rerun. Do not replace the traceback with expected output or change tests merely to hide the defect.

## 8. Dependencies and permissions

The scripts use built-in language features and the standard library for their tests. No third-party package is required. python3 reads the source as data, so executing the source file itself through operating-system executable permissions is unnecessary. You need ordinary permission to read the file and execute the interpreter. sudo is not required for the lab and would add unnecessary privilege.

## 9. Previous exit status

In Bash, $? expands to the status of the immediately previous command, and echo displays it. Another command replaces that remembered status. A successful local run should normally report 0; a nonzero status needs interpretation. The value is process evidence, not evidence of payment truth or business approval.

## 10. Test scope

The three methods check the welcome program's defined output, the briefing's six-line process contract and the briefing's execution by absolute path from another working directory. They inspect actual output, diagnostics and status. They do not establish payment verification, enrollment authority, model accuracy, input validation, deployment security or your own understanding. Only the specific checked behavior in the recorded environment is supported.

## 11. Review state and authority

Awaiting review is assigned to request_status in the source. It is sample information. It does not come from an authenticated support system. Displaying a course or review label cannot authorize an enrollment change. A future integration needs a trusted source and an explicitly permitted action boundary.

## 12. Reviewing the AI explanation

Trace the assignments and every operation in the source. There is no payment-provider call, credential handling, enrollment lookup or verification function. The final line explicitly states that no checks occurred. Reject the unsupported explanation and describe the actual capability: a deterministic report of supplied example data. AI-generated prose must be checked against implementation just as generated code must be checked against requirements.
