# 27. Email Validator
# Validate whether a given email address follows a valid format

email = input("Enter an email address: ")

if '@' in email and '.' in email.split('@')[-1]:
    username, domain = email.split('@', 1)
    if username and '.' in domain:
        print("Valid email address.")
    else:
        print("Invalid email address.")
else:
    print("Invalid email address.")
