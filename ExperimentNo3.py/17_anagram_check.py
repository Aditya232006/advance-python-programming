# 17. Anagram Check
# Check whether two strings are anagrams

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if len(s1) != len(s2):
    print("Not anagrams.")
else:
    s1_sorted = sorted(s1.lower())
    s2_sorted = sorted(s2.lower())
    if s1_sorted == s2_sorted:
        print("Anagrams.")
    else:
        print("Not anagrams.")
