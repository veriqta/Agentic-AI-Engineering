# 13. Command Reference

Use this as a review after the guided lab. Commands depend on context. Read the explanation before executing an unfamiliar command, and preserve existing files.

| Command | Important parts | Expected behavior or caution |
|---|---|---|
| pwd | Shell working-directory command | Prints the absolute current directory |
| python3 --version | Executable plus version option | Displays the actual installed Python version |
| command -v python3 | Shell command lookup with verbose-name result | Identifies which Python command this shell selects |
| mkdir -p PATH | Create directories; allow existing parents | Creates missing directories without clearing contents |
| cd PATH | Change this shell's directory | Alters the base used by subsequent relative paths |
| ls | List visible current-directory entries | Output depends on actual contents and shell configuration |
| ls 09-source | List a selected child directory | Confirms source filenames from the day directory |
| vi 09-source/first_agent.py | Open a named source file | Inspect an existing file before editing |
| i | vi insertion mode | Enables source text entry |
| Esc | Return to vi normal mode | Separates editing text from editor instructions |
| :wq, then Enter | Write and quit vi | Saves the buffer to disk before execution |
| :q!, then Enter | Quit without saving changes | Discards unsaved edits deliberately |
| cat FILE | Display saved text | Does not execute Python or validate business data |
| python3 09-source/first_agent.py | Interpreter plus relative script path | Displays the introductory welcome |
| python3 09-source/support_briefing.py | Interpreter plus project script path | Displays the six-line sample briefing |
| echo $? | Echo the immediately previous process status | Run immediately after the command being investigated |
| python3 09-source/support_briefing.py > briefing-output.txt | Redirect stdout to a file | Overwrites the destination; choose a fresh practice file |
| cp -i SOURCE DESTINATION | Copy, prompting before replacement | Keeps the original intact; decline an unwanted overwrite |
| python3 -m unittest discover -s 10-tests -v | Module execution, discovery, start folder, verbose results | Run from the day directory; expect three reference methods |
| python3 15-evidence/reproduce_reference.py --output veriqta-day01-evidence | Optional reference-evidence tool and new destination | Run from the repository day directory; destination must not exist |

## Context reminders

~ expands to your home directory in the shell contexts used in the lab. It is not a universal Python path expansion rule. Relative paths start at the current working directory. A displayed shell prompt is not part of a command. A >>> prompt indicates the interactive Python interpreter, where ordinary Bash commands do not belong.

This class does not require sudo, pip installation, chmod, cloud provisioning or a Git push. Publishing course changes is a separate feature-branch and pull-request process. Running the local project does not modify the public repository.
