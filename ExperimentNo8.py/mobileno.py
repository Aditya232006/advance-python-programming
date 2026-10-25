import re

mobile = input("Enter your mobile number: ")

mobile_pattern = r"^[6-9][0-9]{9}$"

if re.match(mobile_pattern, mobile):
    print("Valid 10-digit mobile number")
else:
    print("Invalid mobile number")