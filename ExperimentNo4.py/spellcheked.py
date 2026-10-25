import re
text = input("Enter text: ").lower()
dictionary = {"hello", "world", "python", "program", "computer", "student", "book"}

words = re.findall(r'\b[a-z]+\b', text)
wrong = [w for w in words if w not in dictionary]

print("Misspelled Words:", wrong)