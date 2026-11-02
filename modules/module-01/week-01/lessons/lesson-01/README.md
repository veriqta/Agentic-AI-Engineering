# Lesson 01: Student Support Automation

Module 01, Week 01. Suggested duration: 60 minutes for the guided build; allow an additional review session when needed.

**Status:** Implementation and nine-test execution verified. Knowledge check and final understanding review remain pending. This lesson, week and module are not marked completed.

## Engineering problem

VERIQTA Academy needs consistent responses to student access requests. A support application must accept a name and a simulated payment status, reject malformed input, apply a clear rule, and return a machine-readable answer. It must be testable before a future API or agent calls it.

## Learning objectives

- Trace a request through parameters, local variables, function calls and return values.
- Validate types and empty input before applying a business rule.
- Separate a valid negative decision from an invalid request.
- Explain command-line arguments, JSON output, logging and process exit codes.
- Run and interpret function tests and command-line integration tests.
- Identify why supplied payment status is not proof of payment.

## Prerequisites and tools

Basic terminal navigation and editing a text file are helpful. Introductory scripts are preserved in [examples](examples/README.md); review them only if needed. Use Python 3.12 or later, a terminal and vi. The implementation uses only the Python standard library, requires no API keys and makes no network requests. Local publication checks use Python 3.12.14; learner execution evidence reports Python 3.14.4. See [evidence](verification.md) for the limits of those claims.

## Learning sequence

1. Read the [instructor notes](notes.md) for the scenario, concepts and decisions.
2. Build the application using the [guided laboratory](follow-along-lab.md).
3. Trace each component with the [code walkthrough](code-walkthrough.md).
4. Review [test design](testing.md), then answer the [knowledge check](knowledge-check.md).
5. Complete the [practical assessment](practical-assessment.md) and [improvement exercises](exercises.md).
6. Compare results with the [verification record](verification.md); consult [troubleshooting](troubleshooting.md) for failures.

## Expected practical outcome

A reusable Python application with a command-line interface, validated inputs, JSON output, logs and nine automated test methods. This is one milestone toward the [module portfolio project](../../../module-project/README.md), not a complete AI agent or production payment service.

## Files

| Path | Responsibility |
|---|---|
| `src/student_support.py` | Validation, payment decision, response and CLI |
| `tests/test_student_support.py` | Function and subprocess checks |
| `examples/` | Preserved introductory examples and baseline |
| `notes.md`, `code-walkthrough.md` | Instruction and architecture |
| `follow-along-lab.md`, `testing.md` | Reproducible build and verification |
| `knowledge-check.md`, `practical-assessment.md` | Understanding and application tasks |
| `verification.md` | Evidence, limitations and completion state |

## Next connection

The next milestone will develop professional Python structure and structured student data before introducing external APIs. Payment decisions remain deterministic; later LLMs may assist communication but must not invent authorization evidence.

[Week navigation](../../README.md) | [Module navigation](../../../README.md)
