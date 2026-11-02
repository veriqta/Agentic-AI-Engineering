# 06. Practical Assessment: Verify the CLI boundary

## Your task

Run a valid and an invalid request while capturing stdout and stderr separately. From your practice folder use: python3 student_support.py --name Sarah --payment-status unknown > response.json 2> diagnostic.log. The > operator sends stdout to a file; 2> sends stderr to a different file. Both overwrite their destinations, so choose new disposable files. Immediately inspect echo $? for the application exit status, then use cat response.json and cat diagnostic.log to inspect the streams. cat displays saved text and does not parse JSON. Repeat with paid using separate output filenames. Explain why unpaid also exits 0.

## Evidence and review

Keep the exact source revision, commands, actual output and your explanation of the responsible statements. Label expected results separately from actual execution. If the result differs from your prediction, investigate the difference and verify a correction. Do not copy a reference result into your own evidence.

## Criteria

The invalid request has exit 2, no success JSON and a diagnostic. The paid request has parseable JSON on stdout and INFO on stderr. You distinguish process success from business approval, account for overwritten files and explain that echo $? must run before another command replaces the status.

Record meets criteria, needs revision or not yet assessed for each requirement. You are not expected to memorize the script. You must be able to locate the relevant code and explain its behavior. The reference assigns no individual grade.

## Progression

Use the knowledge check and practical result together before the next major dependency. This assessment verifies one lesson milestone. It does not by itself complete Week 01 or Module 01.
