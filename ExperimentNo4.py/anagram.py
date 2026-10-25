import re

def anagram(s1, s2):
    s1 = sorted(re.sub(r'[^a-zA-Z0-9]', '', s1.lower()))
    s2 = sorted(re.sub(r'[^a-zA-Z0-9]', '', s2.lower()))
    return s1 == s2

a = input("Enter first string: ")
b = input("Enter second string: ")

if anagram(a, b):
    print("Anagrams")
else:
    print("Not Anagrams")