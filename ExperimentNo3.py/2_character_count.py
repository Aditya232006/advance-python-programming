# 2. Character Count
# Count vowels, consonants, digits, spaces, and special characters

# Character Count

s = input("Enter a string: ")

vowels = 0
consonants = 0
digits = 0
spaces = 0
special = 0

for ch in s:
    if ch in "aeiouAEIOU":
        vowels += 1
    elif ch >= '0' and ch <= '9':
        digits += 1
    elif ch == ' ':
        spaces += 1
    elif (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'):
        consonants += 1
    else:
        special += 1

print("\nCharacter Count:")
print("Vowels =", vowels)
print("Consonants =", consonants)
print("Digits =", digits)
print("Spaces =", spaces)
print("Special Characters =", special)
