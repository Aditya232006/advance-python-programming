# 14. Replace a word with another word
old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")

file = open("student.txt", "r")

content = file.read()

file.close()

content = content.replace(old_word, new_word)

file = open("student.txt", "w")
file.write(content)
file.close()

print("Word replaced successfully.")