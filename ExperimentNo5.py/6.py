# 6. Count the total number of words in a text file
file = open("student.txt", "r")

content = file.read()

words = content.split()

print("Total number of words:", len(words))

file.close()