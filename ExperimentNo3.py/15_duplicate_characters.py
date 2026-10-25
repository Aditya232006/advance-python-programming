# 15. Duplicate Characters
# Print all duplicate characters in a string

s = input("Enter a string: ")
seen = []
duplicates = []

for ch in s:
    if ch not in seen:
        seen.append(ch)
    elif ch not in duplicates:
        duplicates.append(ch)

print("Duplicate characters:", duplicates)
