# 13. Command Reference

Use this as a review after the guided lab. Application commands assume you are inside veriqta-day-01, where the Python files sit directly beside one another. The optional reference-evidence command has its separate starting location explained in its own guide. Commands depend on context. Read the explanation before executing an unfamiliar command, and preserve existing files.

| Command | Important parts | Expected behavior or caution |
|---|---|---|
| pwd | Shell working-directory command | Prints the absolute current directory |
| python3 --version | Executable plus version option | Displays the actual installed Python version |
| command -v python3 | Shell command lookup with verbose-name result | Identifies which Python command this shell selects |
| mkdir -p ~/veriqta-day-01 | Create directories; allow existing parents | Creates missing directories without clearing contents |
| cd ~/veriqta-day-01 | Change this shell's directory | Alters the base used by subsequent relative paths |
| ls | List visible current-directory entries | Output depends on actual contents and shell configuration |
| vi first_agent.py | Open a named source file | Inspect an existing file before editing |
| i | vi insertion mode | Enables source text entry |
| Esc | Return to vi normal mode | Separates editing text from editor instructions |
| :wq, then Enter | Write and quit vi | Saves the buffer to disk before execution |
| :q!, then Enter | Quit without saving changes | Discards unsaved edits deliberately |
| cat support_briefing.py | Display saved text | Does not execute Python or validate business data |
| python3 first_agent.py | Interpreter plus relative script path | Displays the introductory welcome |
| python3 support_briefing.py | Interpreter plus project script path | Displays the six-line sample briefing |
| echo $? | Echo the immediately previous process status | Run immediately after the command being investigated |
| python3 support_briefing.py > briefing-output.txt | Redirect stdout to a file | Overwrites the destination; choose a fresh practice file |
| cp -i support_briefing.py support_briefing_debug.py | Copy, prompting before replacement | Keeps the original intact; decline an unwanted overwrite |
| python3 -m unittest -v test_day01 | Module execution, discovery, start folder, verbose results | Run from your veriqta-day-01 practice folder; expect three reference methods |
| python3 15-evidence/reproduce_reference.py --output veriqta-day01-evidence | Optional reference-evidence tool and new destination | Run from the repository day directory; destination must not exist |

## Context reminders

~ expands to your home directory in the shell contexts used in the lab. It is not a universal Python path expansion rule. Relative paths start at the current working directory. A displayed shell prompt is not part of a command. A >>> prompt indicates the interactive Python interpreter, where ordinary Bash commands do not belong.

Installing the interpreter and editor can require the sudo package-installation commands in the setup guide. Running this completed project does not require sudo, third-party pip packages, chmod, cloud provisioning or a Git push. Publishing course changes is a separate feature-branch and pull-request process. Running the local project does not modify the public repository.
