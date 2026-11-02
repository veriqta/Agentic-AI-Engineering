# 01. Teaching Notes: Represent Data and Make a Decision

You will represent a business condition and trace which branch runs.

## The VERIQTA Academy setting

Think of a support desk receiving information, making a decision and returning an answer. You will implement only the responsibility introduced in this lesson. The terminal supplies the input; there is no hidden web form or real payment connection.

## Values, types and variables

A value is information the program works with. `"Sarah"` is a string, `123` is an integer, True and False are Booleans, and None represents absence of a value. Quotes make something a string. `"123"` and `123` have different types even though their written digits look alike.

A variable is a name bound to a value. In `student_name = "Sarah"`, the assignment operator `=` binds the name student_name to the string. It does not ask a question. In `status == "paid"`, the comparison operator `==` asks whether values are equal and produces a Boolean.

Descriptive names explain intent. student_name identifies incoming data, cleaned identifies a normalized string, and payment_verified identifies a Boolean decision. Naming is not evidence: despite that variable name, the current application verifies only a supplied status against a rule, not a real payment.

Python names are case-sensitive. True is the Boolean literal; true would be an ordinary name and usually fail if not defined. Strings are also case-sensitive until a program deliberately normalizes them.

## Conditions and truth values

An if statement selects work when its condition is true. `if not isinstance(value, str):` selects rejection for non-text input. isinstance asks whether the value has the expected type; not reverses that Boolean result.

After trimming, `if not cleaned:` checks emptiness. An empty string is falsey and a nonempty string is truthy. A spaces-only string is initially nonempty, but strip turns it into an empty string. That is why checking type alone is insufficient.

`if payment_verified:` uses a Boolean returned by check_payment. If True, generate_response returns the approval message. If False, execution reaches the later return. An else is unnecessary after an unconditional return because the first branch already ended the function.

## Connect this milestone to agent engineering

A future agent needs reliable ordinary code to call. You are learning to state what a component accepts, returns and rejects. You will add a model only after you can explain the tool behavior and its trust boundaries. A simulated payment flag never establishes real payment authority.

## Before you execute

Read the full code, identify its inputs and outputs, and predict the normal result. If a name, operation or branch is unclear, revisit the relevant paragraph before running it. You do not need to memorize the script.

## Trace a decision without guessing

At the reception desk, imagine a training card with a Boolean field named payment_confirmed. The card holds True for the demonstration. It is a simulation of an already-known decision, not evidence from a bank. The program reads that Boolean to select which instruction block runs.

Python first executes the assignment. It then reaches if and inspects the value bound to payment_confirmed. With True, Python enters the indented approval block. It skips the alternative else block. It does not print both messages. At the end of that block, processing continues after the complete if/else statement; here that is the end of the file.

| Source element | Meaning | Common mistake |
|---|---|---|
| `payment_confirmed` | A descriptive variable name | Treating the name as proof of payment |
| `=` | Assigns a value to a name | Reading it as an equality question |
| `True` | Boolean literal | Writing lowercase true or the text "False" |
| `if` | Selects the block when the condition is truthy | Expecting both branches to execute |
| `:` | Starts an indented suite of statements | Omitting it and causing SyntaxError |
| Four spaces | Place the print inside its branch | Mixing indentation or moving the print outside |
| `else` | Supplies the alternative branch | Giving else a separate unrelated condition |

A nonempty string such as "False" is truthy. That is why you should use the Boolean False when you mean a Boolean negative. Tests will later group such contract distinctions so that you do not spend a whole class changing one small value at a time.

## A branch is a policy decision

The code embeds a rule: when the confirmed flag is true, display the approval message; otherwise request payment verification. An AI might draft the branch correctly while using an untrustworthy source for the flag. Correct syntax and safe policy are separate reviews. You must ask both whether the code selects the intended branch and whether it is authorized to rely on the supplied information.

For this milestone you only print a message. You do not update enrollment, send email or call an external API. Keeping the first decision free of side effects makes its behavior easy to inspect. Later lessons will preserve a deterministic rule while placing input and output responsibilities at a clear boundary.

## Investigate indentation systematically

If you see IndentationError, inspect the first reported line and the block above it. A colon should be followed by a consistently indented body. Avoid replacing random whitespace throughout the whole program. In vi, open the file, inspect the affected lines, correct the indentation, save and run the same command again. If the code runs but prints both messages, inspect whether a print accidentally sits outside the if/else structure. The absence of an exception does not prove the business behavior is correct.
