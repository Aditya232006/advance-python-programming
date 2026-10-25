import re

def extract_phone(text):
    pattern = r'(?<!\d)(?:\(\d{3}\)\s?\d{3}-\d{4}|\d{3}[-.]\d{3}[-.]\d{4}|\d{10})(?!\d)'
    return re.findall(pattern, text)

text = input("Enter text: ")

print("Phone Numbers:", extract_phone(text))