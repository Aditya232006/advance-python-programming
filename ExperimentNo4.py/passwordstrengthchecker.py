import re

def check_password(p):
    return (len(p) >= 8 and
            re.search(r'[A-Z]', p) and
            re.search(r'[a-z]', p) and
            re.search(r'\d', p) and
            re.search(r'[!@#$%^&*()_-]', p)) != False

p = input("Enter password: ")
print(bool(check_password(p)))