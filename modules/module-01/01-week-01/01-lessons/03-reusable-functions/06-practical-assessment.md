# 06. Practical Assessment: Diagnose a missing return

## Your task

In a separate baseline copy, replace the True return inside check_payment with print(True). Predict the returned value and the final response before executing. Observe the result, explain how the implicit None reaches generate_response, restore the return and verify the original output. Keep all other logic unchanged so the cause remains identifiable.

## Evidence and review

Keep the exact source revision, commands, actual output and your explanation of the responsible statements. Label expected results separately from actual execution. If the result differs from your prediction, investigate the difference and verify a correction. Do not copy a reference result into your own evidence.

## Criteria

You identify that a displayed True is not a returned True. You trace the nested calls and the Falsey None condition. Your corrected program returns the decision and prints the response only at the outer boundary. You retain a before-and-after explanation.

Record meets criteria, needs revision or not yet assessed for each requirement. You are not expected to memorize the script. You must be able to locate the relevant code and explain its behavior. The reference assigns no individual grade.

## Progression

Use the knowledge check and practical result together before the next major dependency. This assessment verifies one lesson milestone. It does not by itself complete Week 01 or Module 01.
