import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')

text = "Python is easy to learn."

words = word_tokenize(text)

print("Word Tokenization:")

for word in words:
    print(word)