# 04. Follow-Along Project. Support Request Briefing

## Your business problem

A support team needs to see the context of Sarah's course-access request before deciding what to investigate. You will build a small briefing component for VERIQTA Academy. It will present the available sample information consistently and state what has not been verified.

This is Day 01's project milestone. It contributes to the larger Student Support Automation Toolkit. You are not expected to build the entire module application today.

## Requirements

Your implementation must display the academy, student, course, request topic and supplied review state. It must use descriptive variable names and formatted strings. It must include the explicit sentence that no payment or enrollment checks were performed. It must run through python3 without third-party packages or external credentials.

The normal output must match the six-line contract in the guided lab. Do not add an approval message or pretend that sample assignments came from a database.

## Architecture and responsibilities

The source file defines sample data and formats a text report. The Python interpreter executes it as a process. The shell determines the initial working directory and can display or redirect the process's stdout. The separate test file starts the application and compares observed behavior with requirements.

| Component | Responsibility |
|---|---|
| 09-source/first_agent.py | Establish the first-program execution baseline |
| 09-source/support_briefing.py | Display the support briefing |
| 10-tests/test_day01.py | Check process output, status and location independence |
| 15-evidence/reproduce_reference.py | Optionally capture an isolated regression and recovery investigation |

You can trace all business data from source assignments to output. No model or network service participates. A future design will move authoritative data retrieval into a separate, explicitly controlled component.

## Build the milestone in order

1. Complete the environment and first-program stages in the [guided lab](02-follow-along-lab.md). Understand the interpreter and working directory before diagnosing application behavior.
2. Create 09-source/support_briefing.py using the full lab implementation. Read the corresponding [walkthrough](03-code-walkthrough.md) before running it.
3. Trace each variable to its output field. Predict the report without executing it.
4. Run the application and compare actual output with the requirements. Explain why the limitation sentence matters.
5. Follow the [testing instructions](05-testing-and-verification.md) to save and execute the complete test file.
6. Complete the controlled debugging exercise and explain the cause before accepting a correction.
7. Complete the practical assessment and prepare a concise project record.

These steps reuse the detailed commands and complete source provided in the lab instead of introducing a second competing implementation. Follow the linked instructions as part of the project.

## Expected result

The application should produce the six-line briefing, no successful-run diagnostic and exit 0. The reference suite should discover three methods and report OK. Compare with the [actual reference images](14-images/README.md) and [raw records](15-evidence/README.md). Exact durations and temporary paths are environment-specific.

## Security and reliability review

Use Sarah as sample data rather than a real student's details. No API key, cloud identifier or payment information belongs in the source or evidence. A report that merely displays a supplied review state cannot authorize enrollment. The tests establish a small local interface, not a secure production service.

## Portfolio record

Write a short record containing the problem, scope, file responsibilities, exact commands, actual results, one diagnosed failure and known limitations. Explain what you learned about execution and data flow. Include a genuine screenshot or retained text output when useful. If you use a provided output panel, identify it as reference evidence rather than presenting it as your own run.

A suitable project statement describes a deterministic Python support briefing with verified output behavior. It should not describe an autonomous agent, payment verifier or production access-control system.

## Milestone acceptance

You can reproduce the application, explain where every displayed value comes from, run the checks, diagnose a path or source failure and state the authorization boundary. Use the [assessment criteria](11-practical-assessment.md) to identify what still needs revision. Completing this milestone does not finish the week or module.
