# 01. Teaching Notes: Separate Work into Reusable Functions

You will pass values through functions and distinguish return from print.

## The VERIQTA Academy setting

Think of a support desk receiving information, making a decision and returning an answer. You will implement only the responsibility introduced in this lesson. The terminal supplies the input; there is no hidden web form or real payment connection.

## Functions, parameters and arguments

A function defines reusable work. `def normalize_text(value, field_name):` defines its name and parameter names. The colon introduces an indented body. Four spaces are used consistently in this classroom. Indentation changes program structure; it is not decorative alignment.

Parameters are local names for incoming values. Arguments are the values supplied by a call. In `normalize_text("  Sarah  ", "student_name")`, value receives the spaced name and field_name receives the ordinary string label student_name. The label helps format an error; it does not refer indirectly to another variable.

The caller and function can use different variable names. `name = normalize_text(student_name, "student_name")` passes the value stored in student_name, receives the function result and stores it as name. Inside the helper, the same incoming information is called value and its cleaned result is called cleaned.

Each function call has its own local context. A cleaned variable in normalize_text is not automatically a global variable in main. Data crosses these boundaries through arguments and returned values. This is why tracing values is more useful than memorizing every name.

## Return versus print

`return cleaned` ends the current function call and gives a value to the caller. It does not print anything. The caller can store it, compare it, serialize it or pass it onward. Once a return executes, later lines in that same call do not run.

`print(message)` writes output, usually to stdout. A function that only prints is harder for another program to reuse because the caller receives no meaningful message value unless it captures output. Keeping core functions return-based lets tests directly compare results and lets a later API adapter reuse the logic.

Returning a result is like a receptionist handing a checked record to the next desk. Printing is like displaying it on a notice board. Both can be useful, but they solve different problems. This application prints only at the outer command-line boundary.

## Connect this milestone to agent engineering

A future agent needs reliable ordinary code to call. You are learning to state what a component accepts, returns and rejects. You will add a model only after you can explain the tool behavior and its trust boundaries. A simulated payment flag never establishes real payment authority.

## Before you execute

Read the full code, identify its inputs and outputs, and predict the normal result. If a name, operation or branch is unclear, revisit the relevant paragraph before running it. You do not need to memorize the script.

## Walk through the call stack

Imagine VERIQTA Academy has two responsibilities at its support desk. One helper checks the payment label. Another composes the response. The second helper asks the first for a Boolean rather than duplicating its rule. This separation lets you test the decision independently from the wording.

Python reads each def statement and creates a callable function. It does not yet know which student will be processed. The top-level assignments then supply Sarah and paid. The call to generate_response passes those two values into its parameters in order. Inside that function, student_name refers to Sarah and payment_status refers to paid for this call.

The next call invokes check_payment using the status value. Its comparison is true, so it returns True. Python resumes generate_response at the point where check_payment was called and stores that result as payment_verified. The if selects the approval return. That string travels back to the top-level call and becomes response. Finally print displays response. The name parameter is not an input form; it is a local name for an argument supplied by the caller.

| Step | Active location | Important value |
|---|---|---|
| 1 | Top-level assignments | student_name is Sarah; payment_status is paid |
| 2 | generate_response starts | Parameters receive both values |
| 3 | check_payment starts | Its payment_status receives paid |
| 4 | check_payment returns | Boolean True |
| 5 | generate_response returns | Approval string including Sarah |
| 6 | Top-level print | Displays the returned response |

## Compare a returned value with visible output

A return transfers a value to the caller and ends the current function call. It does not display that value by itself in a script. print performs an output operation. If check_payment printed True but returned nothing, its caller would receive None. A later condition could then select the wrong branch even though the terminal displayed reassuring text.

The f prefix marks a formatted string literal. Braces inside it evaluate expressions and place their values into the string. The braces around student_name insert the name; they are not printed literally. Keep the f prefix when formatting. Without it, the braces and variable name would become plain text, which is a behavior defect a response test should detect.

The current baseline explicitly returns True or False inside if/else. A later implementation uses return status == "paid" to return the comparison result directly. Both approaches can express the same simple rule. The more compact version is appropriate only when its meaning is clear to you. Refactoring should preserve observable behavior and be checked by tests.

## Identify what still needs engineering work

This baseline accepts an exact lowercase paid label and does not validate the name. Paid with a capital P is not equal to paid. An empty name can create an unhelpful response. A mistyped label is treated like a recognized negative outcome. These are related input-contract problems, which the next lesson addresses together through normalization and validation. You will test their variations together rather than completing a separate manual exercise for every spelling.
