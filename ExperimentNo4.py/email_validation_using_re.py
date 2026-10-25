import re

def validate_email(email):
    pattern = r'^[A-Za-z0-9._-]+@[A-Za-z0-9]+(?:\.[A-Za-z0-9]+)*\.[A-Za-z]{2,6}$'
    return bool(re.match(pattern, email))

email = input("Enter email: ")

print(validate_email(email))