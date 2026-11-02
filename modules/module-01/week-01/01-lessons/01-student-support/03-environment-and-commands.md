# 03. Environment Setup and Command Foundations

## 1. Choose where the work runs

Use a local Linux terminal or an existing Ubuntu EC2 shell. The terminal window may be on a different computer from the running application. This lab does not require creating cloud infrastructure. Avoid performing system upgrades or changing a production host for a learning exercise.

Commands shown in bash blocks are shell commands. Python blocks contain file contents or code explanations. Do not paste Python statements directly into an ordinary shell. Do not type a displayed prompt such as `$`; classroom command blocks omit it deliberately.

## 2. Check Python

```bash
python3 --version
```

python3 is the executable. --version asks it to display its version and exit. The result should begin with Python 3. The reference uses Python 3.12.14; previous learner evidence reports 3.14.4. Record the actual version rather than changing a version number in documentation to match an example.

If the command is unavailable, stop and use the operating system's approved Python installation process. Do not overwrite Ubuntu's system interpreter. A remote machine may differ from a laptop even if both have Python installed.

## 3. Obtain or inspect the repository

For a new checkout only:

```bash
git clone https://github.com/veriqta/Agentic-AI-Engineering.git
```

Git downloads the repository and creates Agentic-AI-Engineering in the current directory. It needs network access for this step. An existing-directory error means the destination already exists; inspect it rather than deleting work or forcing a clone over it.

During PR review, the revised material is on feat/module-01-student-support-classroom rather than main. In a newly cloned, clean checkout:

```bash
git -C Agentic-AI-Engineering switch feat/module-01-student-support-classroom
```

-C tells Git which repository directory to use. switch selects the feature branch. If Git reports local changes that would be overwritten, preserve and review them; do not discard them just to follow the lab. After merge, use the default main checkout. This classroom does not ask readers to push to the owner's repository.

## 4. Enter the lesson and verify location

```bash
cd Agentic-AI-Engineering/modules/module-01/week-01/01-lessons/01-student-support
pwd
ls
```

Run these in order. cd changes location. pwd prints it. ls lists lesson entries. Expect numbered learning documents and directories 16-source through 20-evidence. If cd fails, the following commands still operate in the previous directory, so investigate before continuing.

Relative commands in later guides assume this lesson directory. The shell does not infer a directory from the document being read in a browser.

## 5. Create a safe practice directory

```bash
mkdir -p veriqta-practice/16-source veriqta-practice/17-tests
```

mkdir creates directories. -p creates missing parents and accepts parents that already exist. The two paths create a small local workspace without changing reference files. These runtime practice paths are not additional curriculum folders. Use the same names as the reference layout so tests can locate the application.

## 6. Learn only the vi actions needed here

```bash
vi veriqta-practice/16-source/01_student_support.py
```

vi opens that path. If the file does not exist, saving creates it; the parent directory must already exist. vi starts in command mode. Press i to enter insertion mode, type or paste source, press Esc to return to command mode, type :wq and press Enter to save and exit. Use :q! only to abandon unsaved edits intentionally.

Do not type :wq into the Python file. If it appears as source, the editor was still in insertion mode. A syntax error at such text is an editor-mode mistake, not an application-design problem.

## 7. Why there is no package installation step

All application and test imports belong to the standard library. A virtual environment isolates third-party dependencies when a project needs them; this milestone has none. Installing packages without a reason adds opportunities for failure and hides the actual requirement. A later professional-development lesson will introduce dependency isolation with a concrete use case.

## 8. Understand command anatomy

```bash
python3 veriqta-practice/16-source/01_student_support.py --name Sarah --payment-status " Paid "
```

The shell starts python3. The script path tells Python which file to read. --name and --payment-status are application options. Sarah and the quoted spaced text are their values. Quotes make the spaced text one argument; the application receives the spaces inside them, not the quote characters.

Expect one JSON response on stdout and an INFO diagnostic on stderr. Read the implementation before running the command. A missing flag produces a usage error. Unknown status produces a controlled validation error. A missing file indicates a path problem.

## 9. Save output without changing its meaning

The shell operator `>` redirects stdout into a file, replacing any previous contents. `2>` redirects stderr. `>>` appends stdout. These operators are interpreted by the shell before the application runs. Always choose a deliberate output path; do not redirect into source code.

Immediately after a command, `echo $?` prints its exit status. Another command would replace that shell value. The project guide uses Python to capture status and streams together, reducing mistakes from manual recording.

## 10. Protect reference work

Use a practice copy or feature branch for experiments. An editor save changes local files; a Git commit records selected changes; a push updates a remote branch; a PR requests review. These are distinct operations. No classroom command authorizes direct changes to main or deployment. Keep credentials, host identifiers and unrelated personal information out of published evidence.
