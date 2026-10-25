import re
from collections import Counter

text = input("Enter text: ").lower()
words = re.findall(r'\b[a-z]+\b', text)

stopwords = {"the", "is", "a", "an", "and", "of", "to", "in", "for", "on"}
words = [w for w in words if w not in stopwords]

print("Top 5 Keywords:", Counter(words).most_common(5))