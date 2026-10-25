# 16. Create another file containing the text in uppercase
file = open("student.txt", "r")

content = file.read()

file.close()

output = open("uppercase.txt", "w")

output.write(content.upper())

output.close()

print("Uppercase file created successfully.")