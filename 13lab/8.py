def is_valid_email(email):

    if len(email) > 256:
        return False

    if "@" not in email:
        return False

    if not email[0].isalnum():
        return False

    parts = email.split("@")

    if len(parts) != 2:
        return False

    if len(parts[0]) < 1 or len(parts[1]) < 1:
        return False

    if "." not in parts[1]:
        return False

    last_dot = parts[1].rfind(".")

    if len(parts[1]) - last_dot - 1 < 2:
        return False

    return True


email = input("Email: ")

if is_valid_email(email):
    print("Дійсна адреса")
else:
    print("Недійсна адреса")