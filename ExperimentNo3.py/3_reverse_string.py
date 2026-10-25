# 3. Reverse a String
# Reverse the given string without using built-in reverse functions

s = input("Enter a string: ")
reversed_string = ""

for ch in s:
    reversed_string = ch + reversed_string

print("Reversed string:", reversed_string)
