# Practical Assessment

## Task A: End-to-end unpaid behavior

Add a test inside CommandLineTests that calls run_app with unpaid. It must assert exit code 0 and parsed JSON equal to `{"message": "Hello Sarah, please verify your payment."}`. Keep the business functions unchanged. The reference implementation now includes this method; self-study readers should attempt it independently before consulting it.

Run the entire suite and review the added test. Acceptance requires a passing method named test_unpaid_request_returns_valid_json, correct assertions, and no regressions. Execution evidence for the interactive milestone shows nine passing methods. The final added method's exact saved source was not separately supplied after execution; the reference here is the instructed implementation, tested in the publication environment.

## Task B: Explain a trust conflict

Sarah supplies a receipt that an AI interprets as successful, while the payment provider reports pending. Explain the access decision, source of authority, next verification step and what to communicate. This is an understanding assessment, not another minor input-editing exercise.

## Task C: Diagnose a regression

Use the bounded debugging exercise in [testing](testing.md). Record the prediction, actual failure, cause, correction and successful rerun. It is available as an assessment exercise; its execution has not been verified in the current milestone.

## Evaluation criteria

| Area | Required evidence |
|---|---|
| Implementation | Review source and show the added unpaid CLI assertions |
| Execution | Actual suite output, command and environment |
| Data flow | Explain normalization, decision, returned message and JSON output |
| Failure handling | Distinguish invalid request from a valid non-approved response |
| Security judgment | Never treat model output or a supplied flag as payment authority |
| Troubleshooting | Identify a failing assertion and verify a correction |

Use meets criteria, needs revision or not assessed; do not invent numerical grades. Task A execution is verified as a milestone. The trust-conflict response and debugging exercise remain pending. Completion of this lesson requires essential understanding review; completion of Week 01 or Module 01 requires their separate objectives and assessments.
