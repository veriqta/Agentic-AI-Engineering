# 18. Introductory Baselines

These short examples preserve the initial progression. Readers who have already demonstrated the concepts should inspect them without repeating them as separate long lessons. The numbered public versions are instructional transcriptions of reviewed source/output evidence. Comments and the Sarah example are editorial presentation choices, not byte-for-byte exports of private learner files.

## 01. Execute a Python statement

[01_first_agent.py](01_first_agent.py) contains a print call. The literal string inside quotes is the text displayed. Parentheses pass that value to print. The filename is historical; the code does not call a model or perform an agent loop.

```bash
python3 18-baselines/01_first_agent.py
```

Python executes the file. Expected stdout is `Welcome to Agentic AI Engineering`. A file-not-found error indicates the path or current directory is wrong. This verifies execution, not understanding of a complex application.

## 02. Make a deterministic decision

[02_decision_agent.py](02_decision_agent.py) assigns True to payment_confirmed. The if condition selects the approved branch, while else provides the alternative. Indentation determines which print belongs to each branch.

```bash
python3 18-baselines/02_decision_agent.py
```

Expected stdout is `Access granted to VERIQTA Academy`. This is a simulated label. The earlier execution evidence established the true branch; the false branch was visible in source but not established as executed in that original record.

## 03. Separate decision and message responsibilities

[03_student_support_baseline.py](03_student_support_baseline.py) defines check_payment and generate_response. The first returns a Boolean, the second returns a message, and the final print displays it. The name and status assignments are inputs to the example.

```bash
python3 18-baselines/03_student_support_baseline.py
```

Expected stdout is `Hello Sarah, your course access is approved.`. Earlier evidence showed paid and unpaid responses. The baseline has exact case matching and treats unsupported strings as False; the improved source deliberately adds normalization and validation.

## Complete code reference

### 01_first_agent.py

```python
# Introductory Python execution example. No model or agent loop is used.
print("Welcome to Agentic AI Engineering")
```

### 02_decision_agent.py

```python
# Introductory deterministic decision example. Payment is simulated.
payment_confirmed = True
if payment_confirmed:
    print("Access granted to VERIQTA Academy")
else:
    print("Please verify your payment")
```

### 03_student_support_baseline.py

```python
# VERIQTA Academy Student Support System


def check_payment(payment_status):
    if payment_status == "paid":
        return True
    else:
        return False


def generate_response(student_name, payment_status):
    payment_verified = check_payment(payment_status)
    if payment_verified:
        return f"Hello {student_name}, your course access is approved."
    else:
        return f"Hello {student_name}, please verify your payment."


student_name = "Sarah"
payment_status = "paid"
response = generate_response(student_name, payment_status)
print(response)
```

## What changes in the new application

The new core retains reusable functions but separates CLI execution, emits JSON, logs diagnostics, rejects invalid data and defines tests. Keep these baselines for comparison. Do not treat repeated tiny input edits as additional major lessons.
