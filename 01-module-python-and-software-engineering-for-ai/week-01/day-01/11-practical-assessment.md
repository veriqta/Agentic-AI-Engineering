# 11. Practical Assessment

## What you must demonstrate

You will reproduce the Day 01 briefing, explain its execution and diagnose one controlled defect. You can consult the notes and source. You are not expected to memorize complete scripts.

## Part A. Reproduce and inspect

From your day practice directory, identify the environment and Python version. Show the saved source for both scripts. Execute the welcome script and the support briefing using the correct paths. Compare the actual output with the contracts. Execute the test suite and confirm that three methods were discovered.

Evidence. Keep your actual version, exact commands, output and complete test summary. If a result differs, retain the failure and investigate before claiming verification. A screenshot of someone else's result is not your execution record.

## Part B. Explain the implementation

Trace student_name from its assignment to the Student output line. Identify the interpreter, script path, fixed labels, variable values and f-string evaluation. Explain what the script writes, what it does not store and why its review state is simulated.

Evidence. A short written explanation or annotated source is sufficient. The explanation should be specific to the implementation. A generic definition of Python does not establish this data flow.

## Part C. Diagnose a controlled source defect

Keep the working implementation intact. cp copies a file, and -i asks before replacing an existing destination. The first path is the source and the second is a separate debugging copy. If the destination exists and you want to preserve it, decline replacement and choose a fresh filename.

```bash
cp -i 09-source/support_briefing.py 09-source/support_briefing_debug.py
```

vi opens only the debugging copy. Use insertion mode to change the reference in the Student print line from student_name to student_nam. Leave the assignment unchanged. Save with Esc, then :wq and Enter.

```bash
vi 09-source/support_briefing_debug.py
```

Before executing, predict the failure category and the point where execution stops. Python will run the copied file selected below; your original source is unaffected.

```bash
python3 09-source/support_briefing_debug.py
```

Inspect the actual traceback. Explain why earlier output may appear before NameError and why a partially printed report is not a complete successful result. Inspect the exit status immediately using echo $?. Correct the misspelled name in the debugging copy, save and rerun that same command. Then run the original test suite to confirm the reference remains correct.

Evidence. Record the faulty line, actual exception, cause, correction and recovered output. Do not alter test expectations to accommodate the misspelling. The optional evidence runner demonstrates the same defect in an isolated temporary copy and proves the checks detect it.

## Part D. Apply engineering judgment

A support colleague says the report is enough to approve Sarah's access because it displays her name and course. Explain why that conclusion is unsupported. Identify the missing authoritative evidence and the boundary between displaying information and performing an authorized change.

Evidence. Your explanation must state that the current implementation makes no payment or enrollment lookup. It should describe the kind of trusted system a later implementation would need, without pretending that integration exists today.

## Review criteria

| Criterion | Meets the requirement when |
|---|---|
| Environment | You identify the actual interpreter version and correct working location |
| Reproduction | Both saved scripts produce their documented results |
| Data flow | You trace assigned data through formatted text to stdout |
| Verification | Three tests are discovered and their actual outcome is recorded |
| Diagnosis | You locate NameError, explain the mismatch and verify recovery |
| Security judgment | You do not treat sample fields as verification or authorization |
| Evidence quality | Your results are authentic, labeled and free of unnecessary sensitive details |

Record each criterion as meets criteria, needs revision or not yet assessed. Revise incomplete work and verify the correction before marking the day completed. This publication supplies no personal grade and does not claim you passed simply because the reference implementation passed.

## What completion means

Complete Day 01 when the core objectives, practical result and understanding are established. Completing this day does not complete Week 01, Module 01 or the larger support toolkit. Keep your source and evidence so later classes can build on them without unnecessary repetition.
