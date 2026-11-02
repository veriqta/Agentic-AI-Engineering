# 11. Knowledge Answers and Instructor Explanations

1. python3 is the interpreter, the next path is the script, and --name supplies a value. The required payment-status option is absent, so argparse reports usage rather than processing a request.
2. Relative paths start from the shell's current directory. pwd reveals that location. The existence of a file elsewhere does not make every relative path to it valid.
3. The value stored in student_name enters value. The literal label student_name enters field_name. The returned cleaned string is assigned to name in the calling function.
4. Assignment binds a name to a value. Equality compares values and returns True or False. Confusing them changes whether code stores information or asks a question.
5. None is not a string and has no string strip method. The deliberate type check raises a controlled ValueError first.
6. strip removes leading and trailing whitespace. Internal spaces and letter capitalization remain. It returns a result rather than editing an existing string in place.
7. Empty and spaces-only strings are still strings. After cleaning, they contain no usable text, so the second check rejects them.
8. The payment contract intentionally treats case variants as equivalent. Name presentation should preserve capitalization. Normalization should follow the field contract, not be applied blindly.
9. Membership means a label is recognized by this component. It does not prove payment, identity, authorization or correctness of the source.
10. False is a normal result and lets the caller continue down the negative branch. ValueError interrupts normal flow and travels to a matching handler.
11. The first return ends that call. The later return is reached only when the first branch was not selected.
12. Return sends data to a caller. `print(json.dumps({"message": message}))` serializes and writes the success document.
13. A dictionary is Python data in memory. JSON is a text representation that another program or language can parse. dumps serializes; loads parses.
14. Extra log lines can make stdout invalid JSON. stderr gives diagnostics a separate channel, even when both streams appear in the same terminal window.
15. Process success means valid input was handled as designed. It does not imply business approval. Unknown is outside the contract, so it reports invalid input.
16. The source is loaded with a non-main name, so its guard does not call main. Functions become available without required CLI argument processing.
17. Discovery skips filenames that cannot be normal Python identifiers, including digit-prefixed module names. Running the numbered script directly invokes unittest.main without discovery. A wildcard alone does not fix this restriction.
18. Subtests identify which related input failed inside a loop. Nine methods therefore cover more than nine individual values, but not all possible values.
19. A correct message alone cannot establish correct process behavior. Tests also check status and that invalid requests produce diagnostics without success data.
20. Keep access pending. Treat the authenticated provider record as the payment authority, reconcile the correct transaction and course, communicate that verification is pending and use a bounded follow-up or human review for a continuing conflict. A model interpretation cannot override trusted transaction evidence.
21. The suite establishes its assertions for supplied cases and environments. It does not establish full coverage, production readiness, trusted payments, complete understanding or module completion.
22. Record environment, source revision or hashes, exact commands, actual streams and exit status, test scope, failure investigation, correction and known limitations. Label rendered reference captures and distinguish publisher execution from a reader's own work.
