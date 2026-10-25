import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')

text = "Python is a simple and powerful programming language."

words = word_tokenize(text)

stop_words = set(stopwords.words('english'))

filtered_words = []

for word in words:
    if word.lower() not in stop_words:
        filtered_words.append(word)

print("Original Text:")
print(text)

print("After Removing Stop Words:")
print(filtered_words)