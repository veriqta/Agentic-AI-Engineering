# 15. Portfolio Presentation and Evidence Guide

## Present engineering, not only output

A useful portfolio entry helps another reader understand the problem, design, behavior and evidence. This first project is a deterministic support-response component. Do not call it an autonomous payment agent or production-ready access system. Its place in the broader agentic program is a tested tool foundation.

## Suggested portfolio structure

1. State the VERIQTA Academy support problem and why validated input matters.
2. Explain the architecture: CLI adapter, validation helper, payment rule and response function.
3. Link complete source, tests and the follow-along guide.
4. Show a valid JSON response with the command that produced it.
5. Show the suite summary and explain what the nine methods cover.
6. Show one intentional invalid request, including empty stdout and exit 2.
7. Explain a controlled regression, the observed failures and successful recovery.
8. Record interpreter version, source revision/hash and output provenance.
9. State unimplemented capabilities and assessment status clearly.

## Reference visuals

The [image index](19-images/00-README.md) links four 1080 by 1350 SVG output panels displaying actual publisher execution results. They are not AI-generated terminal screenshots or evidence of a learner's host. The source records remain available as JSON, including streams and exit codes. Presentation styles do not alter the captured values.

Readers should compare behavior, not exact timing or temporary paths. A passing summary alone does not establish a full project. The failure and recovery capture demonstrates how a regression was detected and corrected in an isolated copy.

## Create personal evidence safely

Run the project runner to a new directory. Review every output before sharing. Avoid hostnames, IP addresses, tokens, account identifiers, private student data and unrelated personal surroundings. Use Sarah and simulated values. If a terminal screenshot includes identifiers, capture a safe view of reviewed output rather than publish the raw host view.

Do not create a terminal image containing expected output and label it actual execution. If output is rendered into a presentation panel, label the rendering and link its original record, as this classroom does. A conceptual architecture diagram is not execution evidence and must be labeled separately.

## Example caption

Reference execution, Python version recorded in the environment file. The normalized paid input produced valid JSON and exit 0. This is a simulated response decision; no payment source or access grant was involved. Raw command output and source hash are linked for inspection.

## Review before publication

Check that each claim has supporting evidence, that all links work, and that final source agrees with the evidence version. Publish changes only on a feature branch and open a PR. The owner reviews and merges. Do not create releases, packages or external deployments as part of this classroom workflow.
