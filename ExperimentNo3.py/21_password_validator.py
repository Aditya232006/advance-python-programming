# 21. Password Validator
# Validate a password based on required conditions

password = input("Enter a password: ")

if len(password) < 8:
    print("Password is invalid. Minimum 8 characters required.")
else:
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif not ch.isalnum():
            has_special = True

    if has_upper and has_lower and has_digit and has_special:
        print("Password is valid.")
    else:
        print("Password is invalid. Missing one or more required categories.")
