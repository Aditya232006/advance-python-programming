# 7. Count the total number of characters, including spaces
file = open("student.txt", "r")

content = file.read()

print("Total number of characters:", len(content))

file.close()