# 8. Read a text file and display its lines in reverse order
file = open("student.txt", "r")

lines = file.readlines()

print("Lines in reverse order:")

for line in reversed(lines):
    print(line.strip())

file.close()