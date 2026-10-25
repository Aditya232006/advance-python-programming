import re

text = input("Enter word or phrase: ").lower()
text = re.sub(r'[^a-z0-9]', '', text)

print(text == text[::-1])