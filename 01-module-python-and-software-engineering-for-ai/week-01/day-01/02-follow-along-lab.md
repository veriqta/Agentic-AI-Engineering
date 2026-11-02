# 02. Guided Follow-Along Lab

## How to follow this lab

Read each explanation before executing its command. Run one command at a time and observe its actual result. The commands are intended for a Linux shell such as Bash. They are not Python statements and should not be pasted at a >>> prompt.

This lab creates a separate practice directory. It does not modify your public GitHub repository, create cloud resources or overwrite existing work intentionally. If a target file already exists, inspect it before editing. If you already have a verified first_agent.py, use that file to demonstrate the outcome and continue to the briefing rather than recreating it unnecessarily.

## 1. Identify your working environment

Confirm whether your terminal is local or connected to an authorized remote machine. Work in the environment where you intend to save and run the source. An SSH connection displays a remote shell, even though the terminal window is on your laptop.

pwd asks the shell to print its current working directory. Its output is an absolute path. Your exact path depends on the machine and account; there is no universal username or home-directory output to match.

```bash
pwd
```

Checkpoint. You can identify which machine owns this directory. Do not publish the prompt, host address or unnecessary account information when saving evidence.

## 2. Check Python before relying on it

python3 selects the Python executable available in this shell. --version requests its version and exits without running application source. You need a supported Python 3.12-or-later environment for the course reference.

```bash
python3 --version
```

Expected shape, with your actual version in place of the placeholder:

```text
Python <your installed version>
```

If the shell reports command not found, Python is not available under that command in this environment. Stop and resolve the environment using supported operating-system instructions. Installing unrelated Python packages will not fix a missing interpreter.

The shell command command -v reports which executable or command definition it will select. Here -v requests the located command. You use this when multiple Python installations might exist; a different installation path is not automatically a problem.

```bash
command -v python3
```

Expect a path or command definition appropriate to your shell. Record the version you actually used. You do not need to copy the reference environment's executable path.

## 3. Create a dedicated practice location

mkdir creates directories. -p creates missing parent directories and accepts ones that already exist. The leading ~ expands in this shell to your home directory. The nested path keeps the module, week and day together. This command does not remove existing contents.

```bash
mkdir -p ~/veriqta-agentic-ai/module-01/week-01/day-01
```

cd changes this shell's working directory. It does not copy files and does not change the location of a different open terminal session.

```bash
cd ~/veriqta-agentic-ai/module-01/week-01/day-01
```

Now use pwd to confirm where relative paths will begin. Expect a path ending in veriqta-agentic-ai/module-01/week-01/day-01.

```bash
pwd
```

Create the two implementation folders. They mirror the numbered source and test folders in the public lesson. Both arguments belong to the same mkdir command, which creates both locations.

```bash
mkdir -p 09-source 10-tests
```

ls lists the visible entries in the current directory. Expect 09-source and 10-tests, possibly alongside your existing files. Listing order or color may differ.

```bash
ls
```

Checkpoint. You can explain why the next source path begins with 09-source instead of starting at the filesystem root.

## 4. Save your first script with vi

Before creating a file, inspect the source folder. This avoids treating an existing exercise as if it were empty.

```bash
ls 09-source
```

vi opens the specified file for editing. If first_agent.py exists, inspect it. If it is new, vi creates an editing buffer, and saving will write the new file into the existing 09-source directory.

```bash
vi 09-source/first_agent.py
```

Press i to enter insertion mode. Enter the complete source below. The # line is a comment. The print call writes the quoted message. Read the first section of the [walkthrough](03-code-walkthrough.md) if any part is unfamiliar.

```python
# Introductory Python execution example. No model or agent loop is used.
print("Welcome to Agentic AI Engineering")
```

Press Esc to return to normal mode. Type :wq and press Enter to save and quit. The characters :wq are editor instructions; do not insert them into Python source. If you are unsure whether vi is in insertion mode, press Esc first.

cat displays the saved file as text. It does not execute the program. Use it to confirm that your source, not the editor command, was written to disk.

```bash
cat 09-source/first_agent.py
```

Expected result. The two source lines above are displayed. If the file is empty or contains editor commands, correct the saved source before executing it.

## 5. Execute the first script

python3 starts the interpreter. 09-source/first_agent.py tells it which saved file to read relative to your current directory. You do not need sudo, pip or chmod for this invocation.

```bash
python3 09-source/first_agent.py
```

Expected stdout:

```text
Welcome to Agentic AI Engineering
```

The interpreter should finish and return control to the shell. The program does not remain running as an assistant. Your shell prompt is not part of the program's output.

Immediately inspect the previous command's exit status. echo writes its argument; $? expands to the status of the preceding command. Do not run another command first.

```bash
echo $?
```

Expected result for a successful run:

```text
0
```

Checkpoint. You can identify the executable, the script path and the statement responsible for the message. You can also explain why exit 0 does not make the script an AI agent.

## 6. Build the support briefing

You will now use named values and formatted strings to display a support request consistently. Your example describes Sarah's request, not a real student record. No input form or external service is involved.

Open a separate file so that the first exercise remains intact. vi edits the path in the same source folder.

```bash
vi 09-source/support_briefing.py
```

Read the briefing section of the [walkthrough](03-code-walkthrough.md) before entering this code. The first string documents the module. The assignments define the sample information. Each formatted print call inserts one value into the report.

```python
"""Display a simulated VERIQTA Academy support request briefing."""

academy_name = "VERIQTA Academy"
student_name = "Sarah"
course_name = "Agentic AI Engineering"
request_topic = "Course access"
request_status = "Awaiting review"

print(f"{academy_name} | Student support briefing")
print(f"Student: {student_name}")
print(f"Course: {course_name}")
print(f"Request: {request_topic}")
print(f"Status: {request_status}")
print("No payment or enrollment checks have been performed.")
```

Use Esc, then :wq and Enter to save and leave vi. Review the saved source using cat. This catches unsaved or accidentally pasted editor text before execution.

```bash
cat 09-source/support_briefing.py
```

Predict the six output lines. Identify which lines use variable values and which line is a fixed limitation sentence.

## 7. Run the project milestone

Start Python with the new script's relative path. The program assigns the sample values and prints the report in source order. It does not ask for interactive input.

```bash
python3 09-source/support_briefing.py
```

Expected stdout:

```text
VERIQTA Academy | Student support briefing
Student: Sarah
Course: Agentic AI Engineering
Request: Course access
Status: Awaiting review
No payment or enrollment checks have been performed.
```

There should be no application diagnostic on stderr for this successful reference run. Inspect echo $? immediately if you need to confirm the process status. Compare meaning and exact text with the documented contract, rather than assuming any visible output is correct.

Checkpoint. Trace student_name from its assignment to the formatted Student line. Explain why the report's status is a supplied example value, not a database lookup.

## 8. Save a real output record

You can save stdout in a text file for comparison. In the shell, > redirects stdout and overwrites the destination if it exists. Choose a fresh practice filename so that you do not replace evidence you want to keep. The named source file is read; the named output file receives the displayed report.

```bash
python3 09-source/support_briefing.py > briefing-output.txt
```

A quiet terminal is expected because stdout went to the file. It does not mean the program failed. cat displays the saved result without rerunning the application.

```bash
cat briefing-output.txt
```

Expect the same six-line briefing. Do not paste the expected output into that file and describe it as an execution record. Save the command alongside the actual result in your own work notes.

## 9. Investigate a safe path failure

You will intentionally ask Python to open a filename that this lab never created. This changes no source file. The purpose is to identify a file-selection problem before trying to repair valid code.

```bash
python3 09-source/missing_briefing.py
```

Expected behavior. Python reports that it cannot open that file. Exact wording and paths vary. The result should be a nonzero exit status. Inspect it immediately with echo $? if needed.

Use pwd to confirm your location and ls 09-source to inspect actual filenames. The real script is support_briefing.py. Run that correct path again and verify the normal report. You did not need to alter print statements or install dependencies to correct the mistake.

Checkpoint. State which boundary failed and what evidence identified the cause. A failed path lookup is different from a SyntaxError or NameError inside an existing source file.

## 10. Prepare automated verification

Read [Testing and verification](05-testing-and-verification.md). It provides the complete test file, explains its execution command and shows how the checks observe real processes. Save the test file in 10-tests using the instructions there.

This supported verification step introduces test execution without requiring you to master classes or design a complete testing framework on your first day. You should still explain what the tests check and what they do not establish.

## 11. Finish with understanding and evidence

Complete the [project milestone](04-project.md), attempt the [knowledge check](07-knowledge-check.md) before its answers, then perform the [practical assessment](11-practical-assessment.md). Use the [troubleshooting guide](12-troubleshooting.md) for actual failures.

Your record should include the saved source, version, commands, actual report, test result and diagnosed problem. If a checkpoint is unclear, revisit the relevant note or walkthrough section before progressing. Source execution alone is not proof of understanding.
