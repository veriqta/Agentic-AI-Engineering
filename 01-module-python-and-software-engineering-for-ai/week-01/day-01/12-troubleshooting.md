# 12. Troubleshooting

## Investigate the boundary before changing code

Keep the exact command and first useful error. Determine whether the problem is command selection, file location, source parsing, runtime behavior or test discovery. Make one justified correction and rerun the relevant command. Do not install packages or rewrite a valid program merely because the terminal displays an unfamiliar message.

## Python is not found

Observation. The shell reports that python3 is not found.

Likely cause. The interpreter is absent from this environment or is not available under that name on the shell's search path. You may also be using a different local or remote session than intended.

Investigation. Confirm the environment, then inspect command -v python3. If it identifies nothing, use an installation method supported by your operating system. This Day 01 lesson does not prescribe a universal installer or authorize replacement of system Python.

Correction and verification. Make the supported interpreter available, then rerun python3 --version. Do not continue with invented application output. Once the version is confirmed, retry the saved source command.

## You are at a Python prompt instead of a shell

Observation. The prompt shows >>>, and shell commands such as cd cause Python errors.

Likely cause. You started the interpreter without a script and entered interactive mode.

Correction. Enter exit() at that Python prompt, or use Ctrl+D on a typical Linux terminal. Then execute the documented shell command from the shell. Do not put cd or vi inside your Python source to solve a prompt-context problem.

Verification. Run pwd in the shell and confirm it displays a directory rather than a Python exception.

## Python cannot open the script

Observation. The interpreter reports that it cannot open the selected file, often including a no-such-file message.

Likely causes. Your current directory is wrong, the filename is misspelled, the file was saved somewhere else or its capitalization differs.

Investigation. Use pwd and ls from the expected day directory. Compare the exact filename with the argument supplied to Python. A valid relative path from one directory can be invalid from another.

Correction. Select the correct location or path. Preserve the source. Installing pip packages does not repair a wrong script path.

Verification. Rerun the correct file and compare actual output with the six-line contract.

## vi cannot save the file

Observation. vi reports that it cannot open the file for writing or indicates a permission problem.

Likely causes. A parent directory does not exist, the path is wrong or you do not have ordinary write permission there.

Investigation. Confirm the intended path and parent folders. Use a practice directory you own. The lab creates veriqta-day-01 and enters it before opening a file directly inside it.

Correction. Choose the correct writable practice directory and preserve any existing work. Do not use sudo as a routine editor fix. Do not discard unsaved text with :q! unless you deliberately intend to lose it.

Verification. Save successfully, exit the editor and use cat to inspect the actual file before running it.

## Editor commands appear inside the source

Observation. cat displays :wq or unexpected command text in the Python file.

Likely cause. You typed the editor instruction while still in insertion mode.

Correction. Reopen the file, remove accidental text, press Esc to return to normal mode, then issue :wq and Enter. Editor commands and application source have different roles.

Verification. Inspect the saved file, then execute it again. Do not assume the editor saved the intended text merely because its window closed.

## SyntaxError appears before the message

Observation. Python reports SyntaxError, possibly pointing at a quote, parenthesis or neighboring token.

Likely causes. A string delimiter or closing parenthesis is missing, smart quotation marks were pasted, or unintended text entered the file.

Investigation. Inspect the reported line and the preceding context. The caret shows where parsing encountered trouble, which may be after the original omission. Use plain source quotation marks, not decorative characters.

Correction. Restore the intended string and call syntax. Do not change unrelated lines or install dependencies.

Verification. Save and rerun. Confirm both successful execution and correct output. Error wording may differ between Python versions.

## NameError appears after some output

Observation. A heading may print, followed by a traceback referring to an undefined variable.

Likely cause. A formatted string references a misspelled or unassigned name, such as student_nam instead of student_name.

Investigation. Read the final exception category and the referenced line. Compare the name with its earlier assignment. Python can execute earlier statements before reaching this runtime defect, so partial output is expected.

Correction. Restore the correct name. Do not suppress the error or remove the field merely to make execution look quiet.

Verification. Run the corrected file, confirm the full output, then rerun the suite. The output contract should still be intact.

## Braces appear literally but the process exits 0

Observation. The output contains {student_name} instead of Sarah.

Likely cause. The string lacks its f prefix.

Investigation. Compare the print call with the walkthrough. Ordinary quoted strings do not substitute expressions in braces.

Correction. Restore formatted-string syntax where substitution is intended.

Verification. Check the complete report and the contract test. Exit 0 alone did not detect this behavioral defect.

## The terminal is quiet after redirection

Observation. The application command with > briefing-output.txt displays no report.

Likely cause. This is expected stdout redirection, not necessarily a failure.

Investigation. Inspect the exit status immediately and use cat briefing-output.txt to inspect saved stdout. Remember that > overwrites its destination.

Correction. If the source command failed, investigate its diagnostic. If it succeeded, compare the file contents. You do not need to rerun without redirection simply to make a result visible, although doing so is useful for comparison.

Verification. The saved file contains the real six-line result. Do not replace it by pasting expected text.

## The test runner discovers zero tests

Observation. unittest reports Ran 0 tests and may still show OK.

Likely causes. The start directory, test filename or test method names are wrong.

Investigation. Run the documented test command from veriqta-day-01. Check that test_day01.py, first_agent.py and support_briefing.py are directly beside one another and test methods begin with test_.

Correction. Restore the documented layout and discovery command. No PYTHONPATH setting is required because this test suite launches source files by path instead of importing them as application modules.

Verification. Exactly three reference methods should be discovered. A zero-test success must not be recorded as a passed application suite.

## A test fails or a subprocess times out

Observation. The runner reports FAIL, ERROR or TimeoutExpired.

Investigation. Read the failing method and assertion. Compare the actual stdout, stderr and returncode. Confirm that source files are present and the environment is intended. A timeout means a bounded execution did not finish; it does not automatically justify removing the limit.

Correction. Address the observed behavior or setup error. Keep requirements separate from implementation. Do not change expected values solely because the application is incorrect.

Verification. Rerun the affected check, then the full three-method suite. Record the correction and actual result.

## The evidence tool refuses its destination

Observation. The tool asks you to choose a new output directory.

Cause. The destination already exists. This is deliberate protection for earlier evidence.

Correction. Choose a new destination name. Do not delete a previous record just to force a success message. If a previous attempt failed, retain its partial records to investigate.

Verification. A successful new run contains environment, execution, regression, recovery and manifest records matching its actual source hashes.

## Debugging record

For a useful investigation, retain the command, observed result, suspected boundary, inspected evidence, justified correction and verified rerun. Remove credentials and unnecessary machine identifiers before sharing. If you cannot yet explain the cause, mark the investigation as unresolved instead of inventing a completion result.
