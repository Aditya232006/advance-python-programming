# 5. Uppercase and Lowercase Count
# Count uppercase and lowercase letters in a string
# 5. Count Uppercase and Lowercase Letters

s = input("Enter a string: ")

upper = 0
lower = 0

for ch in s:
    if 'A' <= ch <= 'Z':
        upper += 1
    elif 'a' <= ch <= 'z':
        lower += 1

print("Uppercase letters:", upper)
print("Lowercase letters:", lower)


# 5. Count Uppercase and Lowercase Letters using ASCII

s = input("Enter a string: ")

upper = 0
lower = 0

for ch in s:
    value = ord(ch)

    if value >= 65 and value <= 90:
        upper += 1
    elif value >= 97 and value <= 122:
        lower += 1

print("Uppercase letters:", upper)
print("Lowercase letters:", lower)