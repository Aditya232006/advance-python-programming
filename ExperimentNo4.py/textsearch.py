import re

text = input("Enter text: ")
query = input("Enter search word: ")

count = len(re.findall(re.escape(query), text, re.I))
result = re.sub(re.escape(query), lambda m: "**" + m.group() + "**", text, flags=re.I)

print("Occurrences:", count)
print("Highlighted Text:", result)