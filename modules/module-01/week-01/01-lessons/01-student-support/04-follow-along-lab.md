# 04. Guided Follow-Along Laboratory

## Stage 1. Understand the outcome before editing

The application should accept a name and simulated status, return a predictable response for recognized statuses, and reject malformed requests. The first working milestone is a valid CLI response. The second is an automated suite covering good and bad inputs. The weekly project then captures reproducible evidence.

Read the [environment guide](03-environment-and-commands.md) first. Work from the lesson directory and create the practice source/test folders as explained there. Use Sarah for example people and VERIQTA for the organization.

## Stage 2. Read the introductory progression

Open the [baseline guide](18-baselines/00-README.md). first_agent demonstrates Python execution and print. decision_agent adds a Boolean and a branch. The baseline support script separates the decision and message. Readers who already understand those steps should inspect the code without repeating every execution.

These examples establish the starting point. They are not artificial completion of an entire week. The improved application introduces validation, a reusable boundary and tests because the support workflow needs them.

## Stage 3. Build the complete source

Open the practice file:

```bash
vi veriqta-practice/16-source/01_student_support.py
```

vi selects the file, not a Python interpreter session. Press i before entering text. Work through these logical sections: imports/shared status contract, normalize_text, check_payment, generate_response, main, and the execution guard. Read each corresponding explanation in the [walkthrough](05-code-walkthrough.md) before entering that section.

The full runnable reference follows. It is complete so a learner can compare the saved file against a known implementation, rather than assemble unexplained fragments.

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

Save with Esc, :wq and Enter. Before execution, confirm the following by reading the saved source: core helpers return values, only main prints JSON, unknown statuses raise ValueError, and the execution guard calls main only for direct script execution. These are reading checkpoints, not claims of a completed assessment.

## Stage 4. Trace a request

With name `"  Sarah  "` and status `" Paid "`, generate_response first calls normalize_text for the name. The value passes the string check, becomes Sarah after strip, and is returned. check_payment separately normalizes the status, lowercases it, confirms membership and returns True. generate_response returns the message, and main serializes it.

An unsupported status follows a different path. ValueError stops generation and reaches main's handler. The handler logs and returns 2. The success print is never reached. The word unpaid is supported, so it follows an ordinary False decision and still exits successfully.

## Stage 5. Execute one valid request

```bash
python3 veriqta-practice/16-source/01_student_support.py --name Sarah --payment-status " Paid "
```

The command selects the practice file. The two flags supply the values. Quotes preserve the outside spaces so normalization is exercised. The command does not contact a payment provider or grant access.

Expected stdout:

```json
{"message": "Hello Sarah, your course access is approved."}
```

Expected stderr:

```text
INFO Support response generated.
```

Compare with the [publisher execution capture](19-images/01-success-output.svg). That image displays real captured reference output, not a learner's remote host. If output differs, inspect the first error and use troubleshooting before advancing.

## Stage 6. Inspect the interface

```bash
python3 veriqta-practice/16-source/01_student_support.py --help
```

argparse handles --help and displays usage and the two required options. This does not generate a support response. Read the options to confirm how the CLI contract is exposed. A help option is useful documentation, but the public guide must still explain the engineering purpose and code.

## Stage 7. Exercise one controlled failure

```bash
python3 veriqta-practice/16-source/01_student_support.py --name Sarah --payment-status unknown
```

Expected stderr contains `ERROR Request rejected: Unsupported payment status.`. Expect no stdout JSON. Immediately run:

```bash
echo $?
```

Expected result is 2. echo displays text, and $? expands to the previous command's process status. Do not run another command between the application and echo. Compare with the [captured failure](19-images/03-invalid-input.svg). This is a known invalid request, not a crash to hide.

## Stage 8. Add tests together

Continue to the [testing lab](06-testing-lab.md). It supplies the full test implementation, explains its import/loading arrangement, and groups capitalization, whitespace and status variations into subtests. Do not spend a separate session manually changing each input.

## Stage 9. Produce a project artifact

The [weekly project](07-weekly-project.md) teaches how to capture raw results, exit statuses, environment and a manifest. Each command has a purpose. Keep reference evidence separate from personal practice evidence. Present the application, test outcome, one failure investigation and known limitations in a portfolio.

## Stage 10. Assess before completion

Answer the [knowledge check](10-knowledge-check.md), perform the [practical assessment](12-practical-assessment.md), then use its rubric to determine what needs more study. Record real outputs. No reader is marked completed merely by seeing the expected output or copying the reference implementation.
