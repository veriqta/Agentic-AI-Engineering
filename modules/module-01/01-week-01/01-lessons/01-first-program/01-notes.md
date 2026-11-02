# 01. Teaching Notes: Your First Python Program

You will execute a program and distinguish a shell command from Python source.

## The VERIQTA Academy setting

Think of a support desk receiving information, making a decision and returning an answer. You will implement only the responsibility introduced in this lesson. The terminal supplies the input; there is no hidden web form or real payment connection.

## Computer, operating system, terminal and shell

The computer provides processor, memory and storage. Ubuntu is an operating system that manages these resources and runs programs. A terminal displays text interaction. A shell reads commands typed into that terminal and starts programs.

When you type a Python command, the shell first separates its words and handles quoted arguments or redirection. It then starts the Python interpreter with the supplied arguments. Python reads the script and executes its top-level statements. In later lessons, a def statement will define a function without running its body. The operating system reports the process's final exit code to the shell.

An SSH application on a laptop may show a remote Ubuntu shell. That does not make the remote program run on the laptop. The program runs where the shell session points. You can work locally on Linux; a remote cloud machine is optional. Check which shell you are using before creating files.

## Files, directories and the current location

A directory groups files. A path tells software where a file lives. An absolute path starts from the filesystem root. A relative path is interpreted from the current working directory. `first_agent.py` means that file under the lesson directory only when the shell is currently in the lesson directory.

`pwd` prints the current working directory. `cd` changes it. `ls` lists entries. These commands help diagnose paths rather than serving as rituals to memorize. A file-not-found error often means the script exists but the caller selected the wrong directory.

The repository is the version-controlled classroom. Your working project is where practice happens. Keep experiments or evidence separate from the reference files when possible. Git records changes to tracked text; an editor saves a file to disk. Saving in vi does not itself create a Git commit or push a branch.

## Programs, scripts and the interpreter

A program is instructions and data that a computer executes. A Python script is a text file containing Python source. The interpreter reads and runs it. The `.py` extension identifies its intended language but does not make the file execute automatically.

In `python3 first_agent.py`, python3 is the executable and the following path identifies the script. Additional words are passed to the application. This is different from entering Python statements directly into a shell, which does not understand Python syntax.

A comment beginning with `#` explains code to humans. A module docstring, written as a string at the start of a file, documents the module. Neither verifies the application. Names such as first_agent.py are historical labels; a print statement is not an autonomous agent.

## Connect this milestone to agent engineering

A future agent needs reliable ordinary code to call. You are learning to state what a component accepts, returns and rejects. You will add a model only after you can explain the tool behavior and its trust boundaries. A simulated payment flag never establishes real payment authority.

## Before you execute

Read the full code, identify its inputs and outputs, and predict the normal result. If a name, operation or branch is unclear, revisit the relevant paragraph before running it. You do not need to memorize the script.

## Your first execution, explained from beginning to end

Imagine a VERIQTA Academy reception desk displaying a welcome notice. At this stage you are building the notice, not the complete support service. The business outcome is deliberately small: establish that you can create a source file, save it, select the correct interpreter and observe exactly the intended output. Later lessons add decisions, reusable work and a terminal interface to that foundation.

When you type `python3 first_agent.py`, the shell searches its configured executable locations for a program named python3. Python then opens first_agent.py relative to the shell's current directory. It reads the source and executes the print call. The text is written to the process's standard output, which the terminal normally displays. After the statement finishes, the interpreter reaches the end of the file and exits successfully. Python does not continue running as a background assistant.

If Python cannot be located, the shell reports a command-not-found error before any source runs. If Python is available but the script path is wrong, Python reports that it cannot open the file. If the file exists but its quotation marks are broken, the interpreter reports a SyntaxError. These failures happen at different boundaries. Learning to locate that boundary is more useful than repeatedly retyping a command.

## Read the only executable statement carefully

`print` is the name of a built-in function. You do not need an import to use it. Parentheses call the function and contain the information passed to it. The quoted characters form a string value. The quotation marks delimit the source string; they are not included in the displayed message. The closing parenthesis finishes the call. A newline is appended by print, which is why your next shell prompt normally begins on a new line.

The comment above the statement in the reference file begins with #. Python ignores the comment during execution. It explains that the historical filename first_agent.py is an introductory label. This program has no language model, tool-selection loop or autonomous planning. A dependable agent will eventually call ordinary software components; you are establishing the ability to run those components correctly first.

## Command reference for this class

| Command or key | What happens | What you should check |
|---|---|---|
| `python3 --version` | Starts Python's version-reporting option | A Python version is displayed; record your actual version |
| `pwd` | Prints the shell's working directory | You know where relative file paths begin |
| `mkdir -p veriqta-week-01` | Creates a directory, allowing an existing one | Existing contents are not cleared |
| `cd veriqta-week-01` | Changes this shell's current directory | Subsequent relative paths use this directory |
| `ls` | Lists visible entries in the current directory | Your saved file appears with the exact spelling |
| `vi first_agent.py` | Opens or starts editing a text file | You are editing the intended path |
| `i`, then Esc | Enters insertion mode, then returns to normal mode | Text entry and editor commands stay separate |
| `:wq`, then Enter | Writes the buffer and quits vi | The file is saved before execution |
| `python3 first_agent.py` | Runs the saved source | The welcome message appears once |

A command such as mkdir can succeed silently. No printed message does not automatically mean failure. Use a relevant observation, such as pwd after cd or ls after saving, instead of expecting every program to announce success.

## Save, run and publish are separate operations

An editor holds your current text in a buffer. Saving writes it to the file. Executing asks Python to read the saved file, not unsaved editor text. Git records selected changes in commits; pushing transfers commits to a remote repository. None of those later Git actions occurs merely because you save in vi or run Python. This distinction prevents a common beginner error: expecting the public repository to update when only a local file changed.

For this first lab, you only need to create, save, execute and explain. Keep an actual result in your own learning record. If you already have a verified first program, inspect this reference and complete its practical understanding check; you do not need to recreate it merely to progress through a numbered page.
