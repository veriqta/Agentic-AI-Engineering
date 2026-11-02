# Day 01. Your Python Environment and First Support Program

Module 01. Python and Software Engineering for AI. Week 01. Python Foundations.

You will learn how a Python program moves from source text to an observable result. You will inspect your environment, create and run a first script, then build a small VERIQTA Academy support briefing. You will explain its data, verify its output and investigate a controlled failure.

## Your engineering problem

A support workflow needs clear, repeatable information before it can make a decision. Sarah has a course-access request. Your first component will display a consistent briefing showing the student, course, request topic and review state. It must not pretend that it checked a payment or granted access.

You will start with a local deterministic program. Later classes will build on these foundations with decisions, functions, validation and external systems. A script that prints a briefing is not yet an AI agent.

## Learning objectives

By the end of this class, you should be able to:

1. Distinguish your computer, operating system, terminal, shell, editor and Python interpreter.
2. Check the Python version in the environment where you are actually working.
3. Explain working directories, filenames, relative paths and absolute paths.
4. Create and save Python source using vi.
5. Explain comments, strings, assignment, variable names, formatted strings and print calls.
6. Trace the briefing from assigned values to terminal output.
7. Distinguish stdout, stderr and process exit status at an introductory level.
8. Run the reference checks, interpret their scope and troubleshoot a path or source error.
9. Explain why simulated request data is not authoritative evidence of payment or enrollment.

## What you need

Use a Linux shell, Python 3.12 or later, vi and permission to create a practice directory. Ubuntu is the reference platform. A local Linux machine is sufficient. If you use Ubuntu on EC2, use your existing authorized SSH session; this class does not create an instance or change cloud configuration.

The implementation uses only Python's standard library. You do not need pip packages, API keys, a model account or real student records. Check your actual installed version before proceeding. A version shown in a reference image does not establish your own environment.

## Study sequence

| Order | Material | What you will do |
|---|---|---|
| 01 | [Instructor notes](01-notes.md) | Understand the environment, problem and programming concepts |
| 02 | [Guided follow-along lab](02-follow-along-lab.md) | Build, save, execute and inspect both scripts |
| 03 | [Code walkthrough](03-code-walkthrough.md) | Explain every important application line and the reference checks |
| 04 | [Follow-along project](04-project.md) | Assemble your support briefing milestone and record evidence |
| 05 | [Testing and verification](05-testing-and-verification.md) | Run three automated execution tests and investigate a regression |
| 06 | [Exercises](06-exercises.md) | Apply path, data-flow and code-review skills |
| 07 | [Knowledge check](07-knowledge-check.md) | Test your understanding before opening the answers |
| 08 | [Knowledge answers](08-knowledge-answers.md) | Review explanations and correct misunderstandings |
| 09 | [Source](09-source/README.md) | Inspect the complete runnable reference files |
| 10 | [Tests](10-tests/README.md) | Inspect the complete automated checks |
| 11 | [Practical assessment](11-practical-assessment.md) | Demonstrate reproduction, diagnosis and engineering judgment |
| 12 | [Troubleshooting](12-troubleshooting.md) | Investigate errors by their actual failure boundary |
| 13 | [Command reference](13-command-reference.md) | Review commands, expected behavior and precautions |
| 14 | [Output images](14-images/README.md) | Compare with labeled output from genuine reference executions |
| 15 | [Reference evidence](15-evidence/README.md) | Inspect raw results and reproduce the reference investigation |

Read the notes first. During the lab, open the relevant walkthrough section before executing the code it explains. The numerical sequence helps navigation; the walkthrough and lab are designed to be used together.

## Suggested session plan

Allow approximately 60 minutes for the core class: 15 minutes for environment and concepts, 20 minutes for guided construction, 10 minutes for source review and verification, and 15 minutes for the knowledge check and assessment. The extended explanations, optional evidence tools and exercises can take additional time. Split the class when necessary rather than skipping a confusing concept.

If you already have a verified first program, inspect the reference and demonstrate the corresponding outcome without repeating every introductory command. Your next meaningful work is the briefing, its explanation and its practical review.

## Your deliverable

Keep your two saved scripts, actual Python version, exact run commands, observed output, one diagnosed failure and assessment responses. Use sample data only. Compare with the reference without copying its results into your own evidence.

Completion requires practical evidence and essential understanding. A reference test pass is not your assessment, and completing this day does not complete the week or module.

[Week 01](../README.md) | [Module 01](../../README.md) | [Course home](../../../README.md)
