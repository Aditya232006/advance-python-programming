from collections import Counter

text = input("Enter paragraph: ").lower()
words = text.split()

freq = Counter(words)

print("Total Words:", len(words))
print("Word Frequency:", dict(freq))
print("Top 3 Words:", freq.most_common(3))

vowels = sum(1 for ch in text if ch in "aeiou")
print("Total Vowels:", vowels)