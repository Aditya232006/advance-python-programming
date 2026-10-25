# 5. Count and display the total number of lines
file = open("student.txt", "r")

lines = file.readlines()

print("Total number of lines:", len(lines))

file.close()