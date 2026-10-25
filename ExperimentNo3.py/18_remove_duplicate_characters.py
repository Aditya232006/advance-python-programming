# 18. Remove Duplicate Characters
# Remove duplicate characters while maintaining the original order

s = input("Enter a string: ")
result = ""
seen = []

for ch in s:
    if ch not in seen:
        seen.append(ch)
        result += ch

print("String after removing duplicates:", result)
