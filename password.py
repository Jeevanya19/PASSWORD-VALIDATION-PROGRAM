import string

while True:
    password = input("Enter your password: ")

    has_upper = False
    has_lower = False
    has_number = False
    has_special = False

    for ch in password:
        if ch.isupper():
            has_upper = True
        if ch.islower():
            has_lower = True
        if ch.isdigit():
            has_number = True
        if ch in string.punctuation:
            has_special = True

    valid = True

    if len(password) < 8:
        print(" Password must have at least 8 characters.")
        valid = False

    if not has_upper:
        print(" Uppercase letter is missing.")
        valid = False

    if not has_lower:
        print(" Lowercase letter is missing.")
        valid = False

    if not has_number:
        print("Number is missing.")
        valid = False

    if not has_special:
        print(" Special character is missing.")
        valid = False

    if valid:
        print(" Password is valid and strong!")
        break

    print("Please try again.\n")
