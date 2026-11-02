# 01. Teaching Notes: Validate Input and Explain Failure

You will normalize allowed variations, reject malformed data and follow an exception.

## The VERIQTA Academy setting

Think of a support desk receiving information, making a decision and returning an answer. You will implement only the responsibility introduced in this lesson. The terminal supplies the input; there is no hidden web form or real payment connection.

## Strings, methods and normalization

A string is a sequence of text characters. A method is an operation available on an object. In `value.strip()`, the dot accesses the string's strip method and parentheses call it. With no argument, strip removes whitespace from both ends. It does not remove internal spaces or all punctuation.

Strings are immutable. strip returns a string result; it does not edit the existing string in place. `cleaned = value.strip()` stores that result under cleaned. `lower()` returns lowercase text. The application chains them by calling normalization first and lower afterward.

Normalization is an explicit interpretation rule, not a universal cleanup step. Outside spaces and capitalization are harmless variations for these payment labels. Passwords, identifiers or provider signatures may require exact matching; automatically lowercasing them could break security. Names preserve capitalization to avoid changing their presentation unnecessarily.

Validation checks whether input meets a contract. Normalization creates a standard representation where the contract permits it. These responsibilities are related but different. Removing spaces does not make a false payment statement trustworthy.

## Sets and an explicit status contract

`VALID_STATUSES = {"paid", "unpaid", "pending", "refunded"}` creates a set. A set stores distinct members and supports membership tests. The uppercase variable name signals a shared constant by convention; Python does not prevent a programmer from changing it.

`status not in VALID_STATUSES` asks whether the status is outside the recognized set. The application does not guess a meaning for unknown labels. Accepted labels are a contract between the source and this component. Provider-specific labels would need an explicit mapping during integration.

Paid produces True. Unpaid, pending and refunded produce False. Unknown raises ValueError. A valid negative decision is not the same as invalid information. Confusing them can conceal upstream data defects or accidentally authorize actions.

## Exceptions and controlled failure

An exception signals that normal processing cannot continue in the usual way. `raise ValueError(...)` deliberately reports an invalid input. This is preferable to allowing a non-string to fail accidentally when strip is called, because the caller gets a predictable failure category.

If normalize_text raises, Python stops that call. It also stops the enclosing check_payment or generate_response call unless a handler catches the exception. The exception travels back through callers to the try/except in main. Returning False would not do this; False is an ordinary result.

Main catches only ValueError because this is the expected invalid-input contract. A broad catch-all could hide programming errors, making an apparently calm application silently wrong. Unexpected failures should remain diagnosable. Future network integration will add separate timeout and provider-error handling rather than pretending all failures are invalid student data.

## Connect this milestone to agent engineering

A future agent needs reliable ordinary code to call. You are learning to state what a component accepts, returns and rejects. You will add a model only after you can explain the tool behavior and its trust boundaries. A simulated payment flag never establishes real payment authority.

## Before you execute

Read the full code, identify its inputs and outputs, and predict the normal result. If a name, operation or branch is unclear, revisit the relevant paragraph before running it. You do not need to memorize the script.

## Define a contract before choosing cleanup rules

At a physical support desk, a form may arrive with outside spaces or a differently capitalized status label. A receptionist can recognize those as harmless formatting differences. A missing value or an unfamiliar status needs clarification instead. Your input boundary implements the same distinction explicitly rather than guessing.

normalize_text accepts two parameters. value is the candidate data. field_name is a fixed descriptive label used in error messages. The type check runs first because strip is a string method. None and integer values cannot safely be treated as text merely because a later operation expects strings. After checking type, strip returns cleaned text. The empty check then rejects both an originally empty string and one made empty by trimming.

check_payment composes these operations. It calls normalize_text with payment_status and the fixed field label, lowercases the returned string, checks membership and finally compares with paid. Order matters: if you lowercase before checking type, unexpected non-text input can cause an accidental AttributeError instead of the deliberate ValueError contract.

| Input | After text cleanup | Policy result |
|---|---|---|
| " Paid " | paid after lowercase conversion | True |
| "unpaid" | unpaid | False |
| "pending" | pending | False |
| "refunded" | refunded | False |
| "unknown" | unknown | ValueError for unsupported status |
| Spaces only | Empty text | ValueError for empty input |
| None or 123 | No cleanup occurs | ValueError for non-text input |

This table is a specification for the later automated tests. It states how variations should behave without requiring you to edit the program repeatedly. The application does not infer paid from a misspelling or from a model-generated claim.

## Follow the failure path

The demonstration first calls check_payment with a harmless spaced label and prints True. It then calls check_payment with unknown. Text validation succeeds, but membership validation fails. raise interrupts normal processing and creates a ValueError. The except clause catches that expected category and prints a diagnostic. There is no Boolean return for that rejected call.

In the final application, main will handle this same exception and convert it into a logged error and a nonzero process exit. The small demonstration isolates the validation mechanism before adding that terminal boundary. The standalone example prints its diagnostic on normal stdout; Lesson 05 deliberately introduces stderr separation for a machine-readable CLI.

## Do not confuse validity with authority

A recognized label is well-formed input for this educational contract. It is not independently verified truth. A production workflow must obtain payment state from an authorized system and account for time, refunds and reconciliation. Keep that security boundary visible as you review AI-generated code: normalizing an untrusted claim cannot make it authoritative.
