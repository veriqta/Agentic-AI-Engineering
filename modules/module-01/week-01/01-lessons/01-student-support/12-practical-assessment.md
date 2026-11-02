# 12. Practical Assessment and Review Rubric

## Purpose

Assess whether a reader can operate, explain, test and troubleshoot the application. Memorizing source is not required. Reference material may be used; reasoning and evidence must still be the reader's own.

## Task A. Reproduce the implementation

Build the practice source and tests using the guided labs. Run a valid request and the full suite. Preserve the exact command, environment, source and results. Explain one input from argument parsing through JSON. Acceptance: the application follows the documented contract, nine reference methods pass, and the data flow explanation identifies each responsibility.

## Task B. Verify a valid negative outcome

The completed reference includes test_unpaid_request_returns_valid_json. Independently explain and, in the practice copy, implement or review its assertions: unpaid exits 0 and produces the verification message as parsed JSON. Acceptance: correct code, a real passing run and an explanation that execution success differs from approval. Earlier learner execution evidence establishes the named ninth method passed, not an automatic understanding grade.

## Task C. Diagnose and recover

Run the weekly evidence workflow or perform its controlled edit in an isolated copy. Predict affected tests, inspect actual failures, explain why the supported-status membership check rejects mixed-case labels after lower is removed, restore the implementation and verify all tests pass again. Acceptance: a cause supported by output and a complete recovery run. Publisher reference evidence does not establish a learner completed this task.

## Task D. Make a security decision

A receipt-reading AI says Sarah has paid, but the provider record says pending. State the access decision, authoritative evidence, follow-up action and student-facing communication. Acceptance: no approval based solely on model output; verify the correct transaction and entitlement using an authorized source. The original interactive response to this scenario remains pending.

## Task E. Review generated code

Explain why replacing payment comparison with bool(payment_status) is wrong. Point to existing tests that would detect recognized non-paid strings being treated as approved. Acceptance: reasoning follows actual Python truthiness and stated policy rather than vague criticism.

## Rubric

| Area | Meets criteria | Needs further work |
|---|---|---|
| Reproduction | Commands and complete files reproduce expected behavior | Missing source, unexplained steps or invented output |
| Architecture | Inputs, helpers, decisions, adapter and outputs are traced | Running code is treated as sufficient explanation |
| Validation | Type, empty and unsupported cases are distinguished | Invalid data is silently converted into an approved result |
| Testing | Assertions cover requirements and failures are interpreted | Tests merely echo implementation or expected data is altered to hide defects |
| Debugging | Cause, focused fix and recovery evidence agree | Success asserted without a corrected run |
| Security | Trusted evidence controls real access | Model confidence or a supplied flag is treated as authority |
| Documentation | Another beginner can follow the work | Only final code or unexplained screenshots are supplied |

Use assessed, needs revision or not assessed. No numerical grade is invented. Lesson completion requires essential knowledge checks and required practical criteria. Week and module completion require separate objectives and integrated work. Current learner implementation execution is verified; final understanding and debugging assessments remain unfinished.
