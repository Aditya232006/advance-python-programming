import re
from collections import Counter

with open("text.txt", "r") as f:
    text = f.read().lower()

words = re.findall(r'\b\w+\b', text)
freq = Counter(words)

print("Total Words:", len(words))
print("Top 10 Words:", freq.most_common(10))