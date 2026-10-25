# 6. Replace Characters
# Replace all occurrences of a character with another character

s = input("Enter a string: ")
old = input("Enter character to replace: ")
new = input("Enter replacement character: ")
result = ""

for ch in s:
    if ch == old:
        result += new
    else:
        result += ch

print("Updated string:", result)
