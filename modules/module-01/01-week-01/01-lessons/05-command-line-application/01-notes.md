# 01. Teaching Notes: Build a Command-Line Support Application

You will connect reusable functions to terminal arguments, JSON output and diagnostics.

## The VERIQTA Academy setting

Think of a support desk receiving information, making a decision and returning an answer. You will implement only the responsibility introduced in this lesson. The terminal supplies the input; there is no hidden web form or real payment connection.

## Command-line interfaces and argparse

A command-line interface accepts arguments through the terminal. argparse defines their names, reads them and produces useful usage errors. Both name and payment-status are required. Missing a required option is rejected before the main validation try block.

The terminal flag uses `--payment-status` while Python accesses `args.payment_status`. argparse translates the hyphen to an underscore for the attribute name. `--help` describes the interface and exits without processing a support request.

Quotes preserve multiple words or outside spaces as one argument. They are shell syntax and are not part of the final string supplied to the application. Avoid using real secrets as command-line arguments, because shell history or process inspection may expose them.

## Dictionaries and JSON

A dictionary maps keys to values. `{"message": message}` uses the literal string message as the key and the variable message as its value. The quotes distinguish the fixed field name from the variable holding the response.

JSON is a text interchange format understood by many languages. `json.dumps` converts the dictionary into JSON text. `json.loads` parses JSON text back into Python data. Dumping and loading are opposite directions; neither verifies that a payment is real.

The response currently contains only a message. A later interface may add a structured decision code, but its meaning and tests must be defined before implementation. Do not parse approval by searching for reassuring words in model-generated language.

## Logs, stdout, stderr and exit status

A process normally has separate standard output and standard error streams. Successful application data goes to stdout. Diagnostics go to stderr. Both appear in an interactive terminal, but callers can capture them separately. Mixing log lines into a JSON document can break another program's parser.

The logger is obtained with logging.getLogger(__name__). main configures INFO-level reporting with a level and message. The log avoids student names and raw input. This reduces unnecessary data exposure while recording that a request succeeded or failed validation.

An exit status is a number reported when a process finishes. This application uses 0 for successful processing and 2 for invalid requests. Unpaid can legitimately exit 0 because the request was valid and processed correctly. Business approval and software execution success answer different questions.

`raise SystemExit(main())` converts main's returned integer into process exit status. Merely writing return 2 in a helper would not necessarily cause an operating-system exit unless the caller uses it appropriately.

## Imports and the execution guard

Imports load reusable functionality. argparse, json, logging, unittest, subprocess, pathlib and sys are standard-library modules. No pip package is required. The standard library is included with a normal Python installation, although distribution packaging can vary for some optional components.

When Python runs a script directly, its __name__ is __main__. When a tool loads it under another name, the value differs. The final guard starts main only in direct script execution. That allows tests to load functions without requesting terminal arguments or printing a support message.



## Connect this milestone to agent engineering

A future agent needs reliable ordinary code to call. You are learning to state what a component accepts, returns and rejects. You will add a model only after you can explain the tool behavior and its trust boundaries. A simulated payment flag never establishes real payment authority.

## Before you execute

Read the full code, identify its inputs and outputs, and predict the normal result. If a name, operation or branch is unclear, revisit the relevant paragraph before running it. You do not need to memorize the script.

## Trace the complete successful request

Suppose the shell supplies --name Sarah and --payment-status " Paid ". The shell removes its grouping quotes but preserves the inside spaces. argparse reads both options. args.name is Sarah and args.payment_status contains the spaced label. The namespace produced by parse_args is a container of named argument values, not a student database.

main configures diagnostics and calls generate_response. The helper validates the name and passes the status to check_payment. After normalization and membership validation, check_payment returns True. generate_response formats and returns the approval string. Back in main, the logger writes an INFO diagnostic to stderr. json.dumps converts the response dictionary to JSON text and print writes it to stdout. main returns 0, and SystemExit transfers that result to the shell.

For unknown, the helper raises before the message assignment completes. The except handler logs a rejection and returns 2. Control never reaches the success log or JSON print. This is why the error-path test checks both the exit code and an empty stdout. A nonzero code alone would not prove that misleading success output was suppressed.

## The interface contract

| Situation | Application data on stdout | Diagnostic channel | Exit status |
|---|---|---|---|
| Recognized paid status | Approval JSON | INFO on stderr | 0 |
| Recognized unpaid status | Verification-request JSON | INFO on stderr | 0 |
| Unsupported status | No success JSON | ERROR on stderr | 2 |
| Missing required flag | No success JSON | argparse usage and error on stderr | 2 |
| --help | Usage/help text | Normally no application diagnostic | 0 |

Help output is a separate mode of the interface, so stdout is not promised to contain JSON when --help is requested. Successful request processing and successful access approval are different outcomes: unpaid is a valid completed request with a negative business decision.

## Understand the important library calls

logging.basicConfig configures a default handler when normal default conditions apply. level=logging.INFO permits INFO and more severe diagnostics. The format string uses logging's percent-style field placeholders to include severity and message. logger.error uses a %s placeholder and a separate error argument, allowing logging to format the message. The exception messages use fixed field labels or fixed text rather than printing the student's name or raw input.

json.dumps receives a Python dictionary. Its fixed key "message" is different from the variable message used as its value. JSON formatting correctly escapes characters when necessary; you should not build JSON by manually joining quotes around arbitrary input. In tests, parse the output with json.loads and compare data structures so that irrelevant formatting does not become the acceptance criterion.

The execution guard compares __name__ with "__main__". Direct execution satisfies that condition. Importing student_support into a test does not, so parsing and output do not run merely because the helpers are imported. Keeping CLI setup inside main makes the ordinary functions reusable by another interface later.

## Inspect the boundary before adding features

The final source is still small enough to keep helpers and CLI in one file. Splitting it into many modules immediately would add navigation before you understand the responsibilities. Week 02 introduces project organization as the application grows. You should still identify which functions are reusable policy and which code interacts with the process. That distinction will later support an API endpoint or agent tool without rewriting the payment rule.
