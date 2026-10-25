import re

html = input("Enter HTML: ")
text = re.sub(r'<[^>]*>', '', html)
print("Cleaned Text:", text)