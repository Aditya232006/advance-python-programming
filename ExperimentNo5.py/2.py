# 2. Open a text file and display its complete contents
file = open("student.txt", "r")

content = file.read()

print(content)

file.close()