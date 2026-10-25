import re

html = input("Enter HTML: ")
pattern = r'(?:https?://|www\.)[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
print(re.findall(pattern, html))