# 05. Detailed Application Code Walkthrough

Read the [complete source](16-source/01_student_support.py) beside this guide. No edits are needed during the walkthrough.

## Imports and shared definitions

`import argparse` loads Python's command-line parser. `import json` provides JSON serialization. `import logging` provides application diagnostics. These are standard-library modules, so there is no dependency installation step.

`logger = logging.getLogger(__name__)` obtains a logger named for this module. Importing the module does not configure the whole application's logging; configuration belongs in main.

`VALID_STATUSES = {"paid", "unpaid", "pending", "refunded"}` creates a set of recognized labels. Uppercase naming communicates a constant by convention; Python does not make it immutable.

## normalize_text

`def normalize_text(value, field_name):` defines a function with two parameters. A call passes the input and a descriptive field label.

`if not isinstance(value, str):` asks whether the input is not text. It runs before any text method. `raise ValueError(...)` rejects invalid data. The f-string substitutes `field_name` into the diagnostic.

`cleaned = value.strip()` assigns the trimmed string result. For `"  Sarah  "`, cleaned becomes `"Sarah"`. Internal whitespace and name capitalization are preserved.

`if not cleaned:` checks for an empty string after trimming. Nonempty strings are truthy; the empty string is falsey. Spaces-only input becomes empty and is rejected.

`return cleaned` ends the function and sends the string back. It prints nothing.

## check_payment

`def check_payment(payment_status):` accepts a supplied status. It does not retrieve payment records.

`status = normalize_text(payment_status, "payment_status").lower()` first calls normalization, then lowercases the returned string, then stores the final result. If normalization raises, the later operations do not execute.

`if status not in VALID_STATUSES:` checks membership in the recognized set. Unsupported values raise ValueError. The final `return status == "paid"` returns the Boolean result of equality directly.

| Input | Normalized value | Result |
|---|---|---|
| `" Paid "` | `"paid"` | True |
| `"unpaid"` | `"unpaid"` | False |
| `"pending"` | `"pending"` | False |
| `"unknown"` | `"unknown"` | ValueError |
| `None` | No string result | ValueError |

## generate_response

The two parameters are student_name and payment_status. `name = normalize_text(...)` stores the validated name. `payment_verified = check_payment(...)` stores a Boolean if status validation succeeds. Despite its variable name, this is a decision about simulated input, not independently verified payment evidence.

`if payment_verified:` selects the approval branch. `return f"Hello {name}, ..."` substitutes the cleaned name and immediately ends the function. The final return is reached only when the Boolean is False. No `else` is necessary because the earlier return already exits the approved path.

## main and the command-line adapter

`argparse.ArgumentParser(description=...)` creates the parser and help text. `add_argument(..., required=True)` requires both named inputs. `parse_args()` reads the terminal arguments. The flag `--payment-status` is exposed as `args.payment_status` because argparse translates its hyphen to an underscore for attribute access.

`logging.basicConfig(...)` enables INFO-level messages and formats them with a level and message. It is called in main to avoid configuring logging when another program imports the module.

Inside `try`, generate_response may return a message or raise ValueError. `except ValueError as error:` catches that expected failure and gives it the local name error. `logger.error("Request rejected: %s", error)` formats a controlled diagnostic, then `return 2` prevents success output.

After successful generation, `logger.info(...)` writes a diagnostic. `{"message": message}` constructs a dictionary. `json.dumps(...)` serializes it into JSON text, and print writes that text to stdout. `return 0` reports successful processing.

## Direct execution versus import

When executed as a script, Python sets `__name__` to `"__main__"`. The guard then calls main. `raise SystemExit(main())` uses its return value as the process exit status. During import, the guard is false, so tests can use the functions without starting the CLI.


## Complete worked trace: successful input

Start at main with args.name equal to Sarah and args.payment_status equal to the spaced mixed-case label. The parser has already checked that both arguments were supplied. It has not verified their business truth.

The try block calls generate_response. That calls normalize_text for the name and stores its returned string. Then it calls check_payment. check_payment calls normalize_text again, with a different value and label. Each call has independent local variables. A successful normalized status becomes paid after lower, passes membership and compares equal to paid.

True returns to generate_response, which selects the first return. That string returns to main and is stored as message. Main logs a diagnostic, builds a dictionary, serializes it and prints. Returning 0 reaches SystemExit, which finishes the process successfully. At no point does return print a message by itself.

## Complete worked trace: invalid input

An unknown status is valid text, so normalize_text returns it. The membership condition rejects it. ValueError interrupts check_payment and generate_response. Neither function produces a normal result. Main's except handler receives the exception, logs its explanation and returns 2. The successful JSON print is skipped.

A missing name differs: argparse notices the absent required flag before entering the try block. A whitespace-only name differs again: the flag exists, but normalize_text rejects its cleaned empty value. Errors can arise at different layers, and diagnosis requires locating the responsible layer.

## Complete worked trace: unpaid input

Unpaid passes text validation, lowercasing and membership. Comparing it to paid returns False. The approval branch is skipped and generate_response returns the verification message. Main produces valid JSON and exits 0 because the request was processed correctly. A business refusal is not necessarily a software failure.

## Why functions have these boundaries

normalize_text owns generic text requirements. check_payment owns the supported payment-label contract and approval comparison. generate_response owns message wording. main owns terminal interaction. This means message wording can change without rewriting CLI parsing, and an API can reuse the core functions without launching a terminal process.

These are separation-of-responsibility choices, not a requirement to make every function as short as possible. Splitting every line into its own function would make this beginner application harder to follow. Keep boundaries aligned with responsibilities and tests.

## Imports and side effects

The guard protects importing or runpy-loading from starting main. Defining a function creates the callable; it does not run its body immediately. Loading the module still executes imports and shared assignments. Therefore, even guarded code should be inspected for top-level side effects. This source only sets up definitions and a logger.

## What the application does not validate

A nonempty string name can still be inaccurate. A supplied paid label can still be false. There is no trusted provider lookup, authentication, actual authorization change, persistence, rate limit or audit store. The program validates representation and policy inputs; it does not establish their external truth. Keep those distinctions in any future agent-tool schema and documentation.

## Test-code walkthrough

The numbered filename is loaded with runpy rather than a normal import statement. See the full [testing lab](06-testing-lab.md) for each import, path expression, dictionary lookup, test class, subtest, assertion and subprocess option. This is a navigation-driven classroom layout, not a claim that dynamic loading is necessary in every Python application.

## Trace exercise before editing

Choose one existing test and point to the exact application branch it exercises. Follow the supplied input to the returned value or exception. Identify what the test would fail to detect. This checks engineering reading without requiring script memorization.
