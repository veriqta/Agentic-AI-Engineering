# 02. Your First Guided Python Lab

## Start with the words

A file is a saved item of information. A folder, also called a directory, groups files. A Python source file contains instructions written as text. The Python interpreter executes those instructions. Your terminal lets you enter commands; its shell reads those commands and starts programs.

There are two places to distinguish. The repository organizes teaching material for visitors. Your own practice folder is where you build an application. A folder number in this repository is not Python syntax and is not a required project structure.

## 1. Prepare Python and the editor

If you have not installed Python, follow [the complete Ubuntu setup](00-ubuntu-python-setup.md). It gives the exact current-version download, checksum, build, installation and verification commands. Do not guess how to install it. That guide targets Ubuntu 24.04 LTS and Python 3.15.2 as checked on November 2, 2026.

python3 starts the interpreter selected by this shell. --version asks it to identify itself instead of running a script.

```bash
python3 --version
```

Expected result after following the current-version setup:

```text
Python 3.15.2
```

If you see a different version, check the setup guide's PATH selection step. If the command is missing, installation has not been verified. Do not copy a reference version into your own execution record.

## 2. Create one folder

You will use an ordinary practice folder named veriqta-day-01. You will place the Python files directly inside it. No separate source or test directory is needed.

mkdir creates the folder. -p permits an existing folder. ~ expands to your home directory in this shell. It does not delete existing contents.

```bash
mkdir -p ~/veriqta-day-01
```

Expected result. Normally no text and a return to the prompt. Quiet success is normal.

cd enters the folder. It changes where subsequent filenames are interpreted.

```bash
cd ~/veriqta-day-01
```

Expected result. Normally no text. If the shell reports that the directory does not exist, inspect the preceding command rather than proceeding with a guessed location.

pwd prints your current folder's absolute path.

```bash
pwd
```

Expected shape. A path ending in /veriqta-day-01. Your username and home-directory prefix may differ from another reader's.

ls lists the visible filenames in that folder. Inspect existing work before editing.

```bash
ls
```

Expected result. A new folder is normally empty and prints no filenames. If files exist, retain or inspect them before deciding what to change.

## 3. Understand the next command before typing it

vi first_agent.py opens the editor for a file named first_agent.py in this folder. The .py suffix identifies Python source to readers and tools. It does not execute the file.

```bash
vi first_agent.py
```

Expected result. The screen changes to vi, displaying the file or a new editing buffer. Press i to enter insertion mode. Enter these complete instructions:

```python
# Introductory Python execution example. No model or agent loop is used.
print("Welcome to Agentic AI Engineering")
```

The comment states the scope. print is a built-in output function. Parentheses call it and contain its argument. Quotes delimit the string; the quote characters are not part of the displayed welcome. The filename is an introductory label, not proof that this script has an AI agent loop.

Press Esc to leave insertion mode. Type :wq and press Enter to save and quit. Expect to return to the shell. These keystrokes belong to the editor, not inside the Python file.

## 4. Inspect before running

cat displays the saved source. It does not execute Python.

```bash
cat first_agent.py
```

Expected result. The two source lines above. If you see missing text or editor instructions such as :wq in the file, correct it before execution.

Now the shell starts Python, and Python opens the named file from the current folder.

```bash
python3 first_agent.py
```

Expected result:

```text
Welcome to Agentic AI Engineering
```

After printing, the program finishes. It does not remain running as a background assistant.

## 5. Explain each part of a run command

| Part | Meaning |
|---|---|
| python3 | The program that reads and executes Python instructions |
| first_agent.py | The saved source file to execute |
| Current folder | The place where that relative filename is looked up |
| print statement | The application instruction producing the welcome |

You do not type a repository folder number into the command unless the file actually lives in that child folder and you are running from its parent. In this lab, the file lives beside you in your current folder, so the simple filename is correct.

## 6. Build the complete project

Continue with [the complete follow-along project](04-project.md). It starts from the same empty-folder assumption and supplies every command, every Python file, editor action, expected result, test and debugging step. If you have already completed its welcome-program steps here, inspect them and continue to its support-briefing stage.

The project does not merely list requirements and send you away to invent an implementation. You will build it in order, compare outputs and complete the practical review.

## 7. Keep real evidence

Record your actual version, command and output. If execution fails, retain the diagnostic and investigate its cause. Use the [walkthrough](03-code-walkthrough.md) and [troubleshooting](12-troubleshooting.md) when needed. An expected-output example is a prediction, not proof that your machine executed it.
