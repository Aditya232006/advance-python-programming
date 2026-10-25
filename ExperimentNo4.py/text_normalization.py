import re

text = input("Enter text: ").lower()

contractions = {
    "don't": "do not",
    "can't": "cannot",
    "won't": "will not",
    "isn't": "is not"
}

for old, new in contractions.items():
    text = text.replace(old, new)

text = re.sub(r'\d+', '', text)
text = re.sub(r'[^a-z\s]', '', text)
text = re.sub(r'\s+', ' ', text).strip()

print("Cleaned Text:", text)