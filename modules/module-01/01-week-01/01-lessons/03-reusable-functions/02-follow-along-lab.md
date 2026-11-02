# 02. Guided Follow-Along Lab

## 1. Understand what you are about to run

You will pass values through functions and distinguish return from print. The input and output are simulated, so you can investigate safely without credentials or a payment provider.

## 2. Prepare your location

Continue in your veriqta-week-01 practice folder. Run pwd if you are unsure where the shell is located. The source path in the run command is interpreted from that location. Preserve earlier milestone files rather than replacing them.

## 3. Open the file

Use vi to open the named Python source file in your current practice folder. Check the filename before editing and preserve earlier milestones.

```bash
vi student_support_baseline.py
```

vi opens the named text file. Press i for insertion mode, enter the complete code below, press Esc, then type :wq and Enter to save and exit. If the parent directory does not exist, create or select it first. Do not put editor commands inside Python source. Use :q! only when you intentionally want to abandon unsaved edits.

## 4. Read and enter the complete implementation

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

Before running it, follow [the walkthrough](03-code-walkthrough.md). Identify the line that starts processing, the selected branch or function, and the line that produces output. Defining a function does not execute its body immediately.

## 5. Execute and observe

Start the Python interpreter with the saved script path below. The application runs its top-level entry point. Review the expected result and argument explanation before executing.

```bash
python3 student_support_baseline.py
```

python3 starts the interpreter. The next path selects the file you saved. No extra arguments are needed for this milestone because the example values are in the source. The command runs locally and does not change real course access.

Expected output:

```text
Hello Sarah, your course access is approved.
```



## 6. Verify the milestone

Compare your actual result with the expected behavior. If it differs, record the command and first relevant error rather than pasting expected text into an evidence file. Trace the name and payment status through both functions and identify what each returns.

## 7. Keep the result and continue

Keep the saved source and actual output. Attempt the knowledge check and practical assessment. The weekly project will integrate these milestones and add automated verification. A successful run is evidence about execution, not a substitute for understanding.
