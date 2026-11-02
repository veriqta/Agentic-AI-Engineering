# 14. Command and Concept Reference

Read the teaching notes and labs before using this as a shortcut. Commands assume the stated working directory; placeholders are explanations, not literal strings to paste blindly.

| Command or part | Meaning | Expected effect |
|---|---|---|
| python3 --version | Ask the interpreter for its version | Version text, no application execution |
| git clone URL | Download a repository into a new directory | Local checkout; network needed |
| git -C DIRECTORY switch BRANCH | Operate in that repository and select a branch | Files reflect the chosen branch; local work must be preserved |
| cd DIRECTORY | Change shell location | Usually no output on success |
| pwd | Print current location | Absolute directory path |
| ls DIRECTORY | List directory contents | File and folder names |
| mkdir -p PATH | Create missing parent directories | Directory exists; existing parents retained |
| vi PATH | Open a text file | Editor command mode |
| i, Esc, :wq | Insert, return to command mode, save/exit | Saved file when :wq completes |
| :q! | Exit vi without saving changes | Unsaved edits abandoned intentionally |
| python3 SCRIPT --help | Ask argparse for usage | Interface description, no support response |
| --name Sarah | Supply a student-name argument | args.name receives Sarah |
| --payment-status " Paid " | Supply one quoted status value | args.payment_status receives spaces and text |
| python3 17-tests/01_test_student_support.py -v | Execute the numbered test file; its main guard starts unittest | Runs the suite without digit-prefixed discovery restrictions |
| -v | Verbose unittest output | Method names and outcomes |
| echo $? | Show previous command's exit status | 0 for success, here 2 for invalid input |
| > FILE | Shell stdout redirection | Replaces FILE with stdout |
| 2> FILE | Shell stderr redirection | Replaces FILE with stderr |
| cat FILE | Display a text file | Text content; no application logic executed |
| --output DIRECTORY | Evidence runner's destination option | Requires a new directory |

## Code vocabulary

| Concept | Meaning in this application |
|---|---|
| String | Text value such as Sarah or paid |
| Boolean | True or False decision |
| None | No value supplied in a direct Python call |
| Parameter | Local name accepting an argument |
| Argument | Particular supplied value |
| Assignment | Bind a variable name with = |
| Equality | Compare values using == |
| Return | End a call and send its value back |
| Exception | Interrupt normal flow for a condition requiring handling |
| Set membership | Check whether a status is recognized |
| Normalize | Produce a standard representation where permitted |
| Validate | Check whether a value satisfies its contract |
| Serialize | Convert data into a format such as JSON text |
| stdout | Program result stream |
| stderr | Diagnostic stream |
| Exit code | Process completion status, separate from business approval |
| Regression | A change breaks previously required behavior |
| Assertion | Executable acceptance check |
| Subtest | Labeled input case within one test method |
| PR | Proposed branch changes for review before merge |
