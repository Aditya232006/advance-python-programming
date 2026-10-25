import re

password = input("Enter password: ")
if not re.search(r"[A-Z]", password):
    print("Error: Capital letter is missing.")

if not re.search(r"[a-z]", password):
    print("Error: Small letter is missing.")

if not re.search(r"[0-9]", password):
    print("Error: Number is missing.")

if not re.search(r"[^A-Za-z0-9]", password):
    print("Error: Special character is missing.")

if len(password) < 8:
    print("Error: Password must contain at least 8 characters.")

if (re.search(r"[A-Z]", password)
        and re.search(r"[a-z]", password)
        and re.search(r"[0-9]", password)
        and re.search(r"[^A-Za-z0-9]", password)
        and len(password) >= 8):

    print("Password is valid.")