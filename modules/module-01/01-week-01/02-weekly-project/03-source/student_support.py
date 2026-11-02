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
