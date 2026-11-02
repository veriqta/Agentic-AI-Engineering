# 03. Code Walkthrough: Validate Input and Explain Failure

Read the complete implementation in the guided lab beside this explanation. Follow the values and selected branches before changing code.

## normalize_text

The parameters accept a value and an error label. isinstance(value, str) checks whether the input is text before string methods are called. not reverses the result, so the first branch raises ValueError for non-text values. The f-string includes the label in its diagnostic.

cleaned = value.strip() removes outside whitespace and binds the result to cleaned. Strings are immutable; strip returns a result rather than editing value. An empty cleaned string is falsey. The next check therefore rejects empty and spaces-only input. return cleaned sends usable text to the caller.

## check_payment

The helper calls normalize_text and then lower on its returned string. The cleaned lowercase status is checked against the allowed set. Unknown is outside that set and raises. Recognized non-paid labels return False when compared with paid. False is a normal result; ValueError interrupts normal flow.

## Follow the controlled error

The try block first prints the successful result for the spaced mixed-case label. Its second call supplies unknown, so membership validation raises. The exception travels out of check_payment to the except block. The variable error receives the exception, and the handler prints a diagnostic. This demonstration puts both lines on stdout for visibility. Lesson 05 will move diagnostics to stderr at the CLI boundary.

## Why the order matters

Type checking must precede strip. Normalization must precede membership when the contract accepts case variations. The success message must not be produced after rejected input. These are engineering choices to trace and test, not arbitrary formatting preferences.
