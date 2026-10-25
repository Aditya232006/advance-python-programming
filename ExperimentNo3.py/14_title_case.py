# 14. Title Case
# Convert the first letter of every word to uppercase



sentence = input("Enter a sentence: ")

words = sentence.split()
result = ""

for word in words:
    result = result + word.capitalize() + " "

print("Title case:", result)
