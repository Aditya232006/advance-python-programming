# 20. Count Occurrences of a Word
# Count how many times a specific word appears in a sentence

sentence = input("Enter a sentence: ")
word = input("Enter the word to search: ")

words = sentence.lower().split()
search_word = word.lower()
count = 0

for w in words:
    if w == search_word:
        count += 1

print("Occurrence count:", count)
