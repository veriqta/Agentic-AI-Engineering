# Week 01, Lesson 01: Build and Understand a Student Support Application

**Program:** VERIQTA Agentic AI Engineering. **Module:** 01, Python and Software Engineering for AI. **Audience:** Beginners. **Format:** Instructor-led explanations followed by a reproducible self-study build.

This classroom teaches how a small Python application accepts information, checks it, applies a decision, returns structured output and proves defined behavior through automated tests. The business setting is VERIQTA Academy, where Sarah requests access to a course.

The application is a deterministic support-response simulator. It contains no model, payment connection or actual access grant. That boundary is part of the lesson: reliable agent tools begin with ordinary software whose inputs, behavior and failures can be understood and tested.

## Start here and read in this order

| Order | Material | Purpose |
|---|---|---|
| 01 | [Learning plan and objectives](01-learning-plan.md) | Understand the scope, schedule and assessment criteria |
| 02 | [Comprehensive teaching notes](02-comprehensive-notes.md) | Learn the concepts before executing code |
| 03 | [Environment and command foundations](03-environment-and-commands.md) | Understand Python, paths, files, terminal commands and vi |
| 04 | [Guided follow-along laboratory](04-follow-along-lab.md) | Build the application in explained stages |
| 05 | [Complete code walkthrough](05-code-walkthrough.md) | Trace every important statement and decision |
| 06 | [Automated testing laboratory](06-testing-lab.md) | Build, run and interpret the test suite |
| 07 | [Weekly project, guided implementation](07-weekly-project.md) | Produce a reproducible evidence bundle from the application |
| 08 | [Troubleshooting laboratory](08-troubleshooting.md) | Investigate errors and verify corrections |
| 09 | [Practical exercises](09-exercises.md) | Apply the concepts independently |
| 10 | [Knowledge check](10-knowledge-check.md) | Check reasoning before viewing answers |
| 11 | [Knowledge answers and explanations](11-knowledge-answers.md) | Compare reasoning and revisit gaps |
| 12 | [Practical assessment](12-practical-assessment.md) | Demonstrate implementation, diagnosis and judgment |
| 13 | [Actual verification and limitations](13-verification.md) | Separate recorded execution from expected behavior |
| 14 | [Command and concept reference](14-command-reference.md) | Find commands and vocabulary quickly |
| 15 | [Portfolio presentation guide](15-portfolio-guide.md) | Present results truthfully with useful visuals |

## Numbered implementation and evidence directories

| Directory | Contents |
|---|---|
| [16-source](16-source/01_student_support.py) | Complete runnable application |
| [17-tests](17-tests/01_test_student_support.py) | Complete nine-method test suite |
| [18-baselines](18-baselines/00-README.md) | Preserved introductory scripts and their explanations |
| [19-images](19-images/00-README.md) | Actual execution-output captures and exact diagrams |
| [20-evidence](20-evidence/00-README.md) | Raw publisher output, environment information and reproducibility script |

All lesson files and directories use numeric prefixes. Folder names continue the reading order. Python scripts also carry prefixes, so the testing guide explicitly explains loading the numbered application. GitHub's conventional repository and week README entry points remain in place to support automatic rendering.

## Expected finished behavior

From this lesson directory:

```bash
python3 16-source/01_student_support.py --name Sarah --payment-status " Paid "
```

Expected stdout:

```json
{"message": "Hello Sarah, your course access is approved."}
```

The guide explains this command before asking readers to run it. Logs travel through stderr. Invalid inputs return an error without a success document. Related capitalization, whitespace and status cases are tested together rather than turned into many separate manual exercises.

## Time and learning pace

The material is intentionally detailed. Use three approximately 60-minute sessions: foundations and guided implementation, application walkthrough and testing, then project evidence and assessment. Experienced readers can use the reference and knowledge check to find gaps; beginners should not attempt to absorb all sections in one hour. This is Week 01, Lesson 01, not a claim that the entire week is finished.

## Weekly project policy

Every week develops one substantial project increment. Lessons supply bounded milestones within that project. Week 01's project is the **VERIQTA Student Support Response Toolkit**, including a working CLI, tests, a failure investigation and a portfolio evidence bundle. Later weeks add professional packaging, structured data and external-system integration toward the module deliverable.

## Prerequisites, cost and safety

A Linux terminal, Python 3.12 or later, a text editor and permission to create a local working directory are sufficient. Ubuntu is the reference learner environment; no EC2 purchase is necessary for public readers. No third-party Python packages, API keys, payment credentials or cloud resources are required. Existing cloud compute may incur its usual cost. Do not paste secrets into commands, source files or public evidence.

## Current verification and completion state

The earlier application and nine-test milestone were verified in supplied learner execution evidence. This numbered classroom edition is separately executed and checked in the publisher environment. See the actual version and results in [verification](13-verification.md).

Understanding reviews, the payment-authority scenario and the learner debugging assessment remain unfinished. This lesson, Week 01 and Module 01 are not marked completed. Publisher captures demonstrate reference behavior; they do not certify a reader's work or replace individual assessment.

[Week 01](../../README.md) | [Module 01](../../../README.md) | [52-week roadmap](../../../../../ROADMAP.md)
