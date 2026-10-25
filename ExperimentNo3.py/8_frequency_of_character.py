# 8. Frequency of a Character
# Count how many times a specified character appears in a string

s = input("Enter a string: ")
ch = input("Enter the character to count: ")
count = 0

for c in s:
    if c == ch:
        count += 1

print("Frequency of", ch, "=", count)
