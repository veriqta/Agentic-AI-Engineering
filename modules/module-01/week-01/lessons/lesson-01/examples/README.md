# Introductory Examples and Baseline

These examples preserve the verified introductory learning sequence. They use no LLM or agent loop despite the historical filenames.

| File | Purpose | Evidence scope |
|---|---|---|
| first_agent.py | Execute Python and print a welcome message | Source command and welcome output were visible in supplied execution evidence |
| decision_agent.py | Simulate a payment Boolean and select a branch | Source and approved-path execution were visible; unpaid branch execution was not established |
| student_support_baseline.py | Separate payment decision and message generation | Original source and paid/unpaid outputs were visible; Sarah is the public example name |

These are instructional transcriptions from reviewed screenshots, not byte-for-byte exports from the learner's machine. Comments and public example naming are editorial additions. No missing test or assessment evidence is invented.

## Follow the progression

In first_agent.py, print sends a literal message to stdout. Run `python3 examples/first_agent.py` from the lesson directory; expect `Welcome to Agentic AI Engineering`.

In decision_agent.py, `payment_confirmed = True` stores a Boolean. The if statement selects the approval message when it is true; else supplies the alternative. Run `python3 examples/decision_agent.py`; expect `Access granted to VERIQTA Academy`. This is a local simulated rule, not verified financial information.

In student_support_baseline.py, check_payment returns a Boolean, generate_response uses it to return a message, and print displays the result. Run `python3 examples/student_support_baseline.py`; expect `Hello Sarah, your course access is approved.`. The baseline compares exact text and accepts unsupported labels as False. The improved implementation adds deliberate validation, normalization and a reusable CLI.

Keep baselines for comparison rather than repeatedly editing trivial input values. The [main lesson](../README.md) develops the application and tests together.
