import nltk
from nltk.tokenize import sent_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')

text = "Python is easy to learn. NLTK is a Python library. It is used for NLP."

sentences = sent_tokenize(text)

print("Sentence Tokenization:")

for sentence in sentences:
    print(sentence)