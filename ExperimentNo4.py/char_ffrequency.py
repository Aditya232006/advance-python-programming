from collections import Counter

text = input("Enter string: ")
choice = input("Ignore case? (yes/no): ")

if choice.lower() == "yes":
    text = text.lower()

freq = Counter(text)

for ch, count in sorted(freq.items(), key=lambda x: x[1], reverse=True):
    print(repr(ch), ":", count)