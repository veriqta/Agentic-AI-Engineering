# Test Design and Interpretation

The suite has nine test methods. Loops group related examples into subtests rather than separate manual exercises.

| Test | Behavior checked |
|---|---|
| test_paid_variations | Paid capitalization and outside whitespace return True |
| test_non_paid_statuses | Unpaid, pending and refunded return False |
| test_invalid_statuses | Empty, spaces-only, unknown, None and integer values raise ValueError |
| test_approved_response_and_name_cleanup | Trimmed name appears in the correct approval message |
| test_unpaid_response | Valid negative decision returns the expected message |
| test_invalid_names | Missing or non-text names raise ValueError |
| test_successful_json_output | Paid CLI request exits 0 and emits the expected JSON |
| test_unpaid_request_returns_valid_json | Unpaid CLI request exits 0 and emits the expected JSON |
| test_invalid_request_has_no_success_output | Unknown status exits 2 with empty stdout and an error diagnostic |

From the lesson directory run:

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -v
```

The local source path makes student_support importable without installing it. Discovery selects tests under tests. Verbose output lists each method. Compare the summary with [actual verification](verification.md), not with fabricated passing output.

The original interactive lab kept source and tests beside each other. Publication separates them into src and tests. Only the test application path and import command change; application behavior is preserved. The packaged version is tested separately from learner EC2 evidence.

## What is not covered

The nine methods do not exercise every parser error, non-paid status through the CLI, exact logging format, real payment data, timeouts, permissions, network failures or deployment. There is no coverage percentage claim. External API and security assessments belong to later milestones.

## Debugging exercise

Work in a scratch copy or feature branch. Temporarily remove `.lower()` from check_payment. Predict the failing subtests, run the suite and explain why mixed-case inputs fail. Restore the code and rerun all tests. The expected failure is a teaching scenario, not a claim that it has already been executed. This exercise is pending unless actual evidence is reviewed.
