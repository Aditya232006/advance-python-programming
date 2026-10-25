# 4. Palindrome Check
# Check whether the entered string is a palindrome

# 4. Palindrome Check

s = input("Enter a string: ")

reverse = ""

for ch in s:
    reverse = ch + reverse

if s == reverse:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
