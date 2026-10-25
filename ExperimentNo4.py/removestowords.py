text = input("Enter paragraph: ")

stopwords = {"is", "and", "the", "a", "an", "are", "of", "in", "to"}

words = text.split()
result = [word for word in words if word.lower().strip(".,!?") not in stopwords]

print("Cleaned Text:", " ".join(result))