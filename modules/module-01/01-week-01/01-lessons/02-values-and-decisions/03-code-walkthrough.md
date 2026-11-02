# 03. Code Walkthrough: Represent Data and Make a Decision

Read the complete implementation in the guided lab beside this explanation. Follow the values and selected branches before changing code.

## Assignment comes before the decision

payment_confirmed = True binds a variable name to a Boolean. True has no quotes because it is a Boolean literal; "True" would be text. The program reaches if payment_confirmed and evaluates that value. With True, it executes the indented approval print. Otherwise it executes the indented else branch.

The colon introduces the block and indentation identifies its statements. Four spaces are used consistently. Moving a statement outside its block changes the logic. The two messages are alternative outcomes, not sequential output.

## Simulation versus truth

This value is supplied in the program. It is not a payment-provider response. A real access system cannot approve a student merely because a local variable or a model says True. This example teaches how a deterministic decision is represented; later integration will establish where trustworthy facts come from.

## Assignment versus comparison

One equals sign assigns. Double equals compares values. This example already has a Boolean, so the if can use it directly. In the next milestone, the status label will be compared to paid to produce that Boolean.
