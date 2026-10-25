# 13. Shortest Word
# Find the shortest word in a sentence

sentence = input("Enter a sentence: ")
words = sentence.split()
shortest =""

for word in words:
    if len(word) < len(shortest):
        shortest = word

print("Shortest word:", shortest)
