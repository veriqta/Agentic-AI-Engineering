# 02. Guided Follow-Along Lab

## 1. Understand what you are about to run

You will connect reusable functions to terminal arguments, JSON output and diagnostics. The input and output are simulated, so you can investigate safely without credentials or a payment provider.

## 2. Prepare your location

Continue in your veriqta-week-01 practice folder. Run pwd if you are unsure where the shell is located. The source path in the run command is interpreted from that location. Preserve earlier milestone files rather than replacing them.

## 3. Open the file

Use vi to open the named Python source file in your current practice folder. Check the filename before editing and preserve earlier milestones.

```bash
vi student_support.py
```

vi opens the named text file. Press i for insertion mode, enter the complete code below, press Esc, then type :wq and Enter to save and exit. If the parent directory does not exist, create or select it first. Do not put editor commands inside Python source. Use :q! only when you intentionally want to abandon unsaved edits.

## 4. Read and enter the complete implementation

```python
"""VERIQTA Academy student support automation."""

import argparse
import json
import logging

logger = logging.getLogger(__name__)

VALID_STATUSES = {"paid", "unpaid", "pending", "refunded"}


def normalize_text(value, field_name):
    if not isinstance(value, str):
        raise ValueError(f"{field_name} must be text.")

    cleaned = value.strip()

    if not cleaned:
        raise ValueError(f"{field_name} cannot be empty.")

    return cleaned


def check_payment(payment_status):
    status = normalize_text(payment_status, "payment_status").lower()

    if status not in VALID_STATUSES:
        raise ValueError("Unsupported payment status.")

    return status == "paid"


def generate_response(student_name, payment_status):
    name = normalize_text(student_name, "student_name")
    payment_verified = check_payment(payment_status)

    if payment_verified:
        return f"Hello {name}, your course access is approved."

    return f"Hello {name}, please verify your payment."


def main():
    parser = argparse.ArgumentParser(
        description="Prepare a VERIQTA Academy support response."
    )
    parser.add_argument("--name", required=True)
    parser.add_argument("--payment-status", required=True)
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s %(message)s",
    )

    try:
        message = generate_response(args.name, args.payment_status)
    except ValueError as error:
        logger.error("Request rejected: %s", error)
        return 2

    logger.info("Support response generated.")
    print(json.dumps({"message": message}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

Before running it, follow [the walkthrough](03-code-walkthrough.md). Identify the line that starts processing, the selected branch or function, and the line that produces output. Defining a function does not execute its body immediately.

## 5. Execute and observe

Start the Python interpreter with the saved script path below. The application runs its top-level entry point. Review the expected result and argument explanation before executing.

```bash
python3 student_support.py --name Sarah --payment-status " Paid "
```

python3 starts the interpreter. The next path selects the file you saved. The named flags supply the student and simulated status. Quotes keep the spaced status together as one argument. The command runs locally and does not change real course access.

Expected output:

```text
{"message": "Hello Sarah, your course access is approved."}
```

An INFO log also appears on stderr. The JSON above belongs on stdout; the two channels are distinct even though the terminal displays both.

## 6. Verify the milestone

Compare your actual result with the expected behavior. If it differs, record the command and first relevant error rather than pasting expected text into an evidence file. Trace a request from argparse through the helpers to JSON, including a rejected input.

## 7. Keep the result and continue

Keep the saved source and actual output. Attempt the knowledge check and practical assessment. The weekly project will integrate these milestones and add automated verification. A successful run is evidence about execution, not a substitute for understanding.
