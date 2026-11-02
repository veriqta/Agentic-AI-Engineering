# 03. Code Walkthrough: Separate Work into Reusable Functions

Read the complete implementation in the guided lab beside this explanation. Follow the values and selected branches before changing code.

## Define work before calling it

The two def statements create functions. Their bodies do not run at definition time. check_payment has one parameter called payment_status. The expression payment_status == "paid" compares the supplied value to the recognized paid label and returns True or False.

The generate_response function accepts a student name and status. It calls check_payment with that status. A True result selects the approval return. Returning ends that call immediately. A False result reaches the other return. The f before each string enables substitution: {student_name} becomes the supplied name.

## Trace the call chain

The bottom assignments supply Sarah and paid. The call to generate_response passes those values into its parameters. The nested call obtains the payment decision. The message is returned and assigned to response. Only the final print writes output.

A returned value can be stored, tested or passed to another function. Printed text appears on a stream. These are different responsibilities. Keeping the functions return-based will let a later API reuse them without capturing terminal output.

## Known gap

This baseline treats every non-paid string as False and does not reject malformed information. It also compares exact case. You will address the input contract in Lesson 04 rather than manually editing every possible variation here.
