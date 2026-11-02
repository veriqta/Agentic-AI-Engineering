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
