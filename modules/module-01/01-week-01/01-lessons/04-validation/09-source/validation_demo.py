def normalize_text(value, field_name):
    if not isinstance(value, str):
        raise ValueError(f"{field_name} must be text.")
    cleaned = value.strip()
    if not cleaned:
        raise ValueError(f"{field_name} cannot be empty.")
    return cleaned


def check_payment(payment_status):
    status = normalize_text(payment_status, "payment_status").lower()
    if status not in {"paid", "unpaid", "pending", "refunded"}:
        raise ValueError("Unsupported payment status.")
    return status == "paid"


try:
    print(check_payment(" Paid "))
    print(check_payment("unknown"))
except ValueError as error:
    print(f"Request rejected: {error}")
