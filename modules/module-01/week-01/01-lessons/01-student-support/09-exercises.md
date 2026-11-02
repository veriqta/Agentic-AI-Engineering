# 09. Practical Exercises

These exercises test application and debugging rather than memorization. Work in the practice copy or a feature branch. Record actual results; no exercise is automatically completed by reading its answer.

## Exercise 1. Trace one full request

Use the existing spaced Sarah and mixed-case status example. Write down values at main, normalize_text, check_payment, generate_response and JSON output. Identify where the first return happens and which code prints. Acceptance: the trace separates arguments, local names, return values and output, without inventing a payment-provider call.

## Exercise 2. Add parser and empty-input coverage

Extend the CLI test helper or add focused subprocess calls to test a missing required flag and a whitespace-only name. Both should fail without success JSON. Explain that the parser handles the absent flag while normalize_text handles whitespace-only data. Acceptance: new checks pass and the original nine methods still pass; do not change business policy to accommodate invalid input.

## Exercise 3. Group response variations

Add one subtest-driven response test for pending and refunded, both producing the existing verification response. These are recognized non-approved states. Acceptance: two cases in a single method, unchanged original behavior and a clear explanation of valid negative decisions.

## Exercise 4. Investigate a defect

Use the weekly project's controlled removal of lower in an isolated copy. Predict affected tests, capture actual failures, explain membership failure and verify recovery. Acceptance: a readable cause-and-correction record plus a passing restored suite. Do not edit the reference source directly to produce portfolio drama.

## Exercise 5. Propose a structured decision contract

Design, without implementing yet, a result with a decision code and message. Define how approved, verification-required and invalid-input outcomes differ. Explain why downstream software should use a structured code rather than infer approval from natural language. Acceptance: explicit fields, meanings and test cases; no claim that changing JSON establishes real payment verification.

## Exercise 6. Review an AI-generated proposal

Consider a proposed simplification: replace check_payment with `return bool(payment_status)`. Explain why nonempty unpaid, pending or unknown strings would be treated as true. Identify existing tests that should detect the defect. Acceptance: reasoning tied to Boolean conversion and policy, not an unsupported statement that AI-generated code is always unsafe.

## Exercise 7. Portfolio review

Write a short report using the evidence bundle. Include a known limitation that materially affects real deployment, not just a generic disclaimer. Acceptance: exact commands, actual version, test scope, defect evidence and truthful boundaries. Ask another reader to reproduce from the guide and record any missing step.
