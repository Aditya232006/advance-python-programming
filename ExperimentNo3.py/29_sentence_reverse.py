sentence = input("Enter a sentence: ")

words = sentence.split()

words.reverse()

result = " ".join(words)

print("Output:", result)

# Reverse Words in a Sentence

sentence = input("Enter a sentence: ")

words = sentence.split()
result = ""

for word in words:
    result = word + " " + result

print("Output:", result.strip())