# 03. Code Walkthrough: Build a Command-Line Support Application

Read the complete implementation in the guided lab beside this explanation. Follow the values and selected branches before changing code.

## Standard-library imports and shared policy

argparse defines a terminal interface, json serializes output and logging provides diagnostics. getLogger(__name__) obtains a logger for the module without configuring all application logging during import. VALID_STATUSES is a set of recognized labels. Uppercase naming signals a constant by convention, not language-enforced immutability.

## Core helpers

normalize_text checks type, trims outside whitespace, rejects empty results and returns cleaned text. check_payment lowercases only status information, validates membership and returns the equality result. generate_response validates the name, obtains the Boolean and returns one message. Its payment_verified variable represents the simulated rule result, not an independent provider verification.

## Argument parsing

ArgumentParser creates help text and parsing behavior. add_argument declares required flags. parse_args reads the supplied values and stores them on args. The flag --payment-status becomes args.payment_status because argparse converts the hyphen for attribute access. Missing required arguments cause usage errors before the application validation try block.

## Logging and controlled failure

basicConfig configures INFO reporting inside main. The try calls generate_response. An expected ValueError is caught, logged on stderr and converted to return 2. This prevents the later success print from executing. Unexpected programming errors are not hidden by a broad catch-all.

## JSON and process exit

The dictionary maps the fixed key message to the returned string. json.dumps serializes that data to JSON text; print writes it to stdout. The success log goes to stderr so a caller can parse stdout independently. main returns 0 for successful processing, including recognized unpaid requests. The final guard calls main only when the file is executed directly. SystemExit converts the returned number into process exit status.

## Full data flow

For Sarah and a spaced Paid label: parse arguments, validate name, normalize and validate status, return True, return approval message, log, serialize and exit. For unknown: validation raises, the exception reaches main, the handler logs and returns 2 with no success JSON. No real payment lookup occurs in either path.
