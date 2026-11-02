# 06. Practical Assessment: Explain three different validation outcomes

## Your task

Use the validation demonstration and the contract table to compare one normalized paid input, one recognized pending input and one unknown label. Trace these together as a single investigation. Demonstrate that non-text and empty input raise the promised exception rather than silently becoming unpaid. Explain which step rejects each case and why lowercasing a payment label does not establish its truth.

## Evidence and review

Keep the exact source revision, commands, actual output and your explanation of the responsible statements. Label expected results separately from actual execution. If the result differs from your prediction, investigate the difference and verify a correction. Do not copy a reference result into your own evidence.

## Criteria

Your evidence separates True, False and ValueError. You explain why type checking precedes string methods, why stripping precedes the empty check and why membership precedes the paid comparison. You do not convert unknown into an approved result or a silent valid refusal.

Record meets criteria, needs revision or not yet assessed for each requirement. You are not expected to memorize the script. You must be able to locate the relevant code and explain its behavior. The reference assigns no individual grade.

## Progression

Use the knowledge check and practical result together before the next major dependency. This assessment verifies one lesson milestone. It does not by itself complete Week 01 or Module 01.
