# 1. Write a Python program to create a file named student.txt 
# and write the student's name, roll number, branch, and semester into the file. 
# Create and write student details into student.txt

file = open("student.txt", "w")

file.write("Name: Madhuri Farakate\n")
file.write("Roll Number: 46\n")
file.write("Branch: Computer Science and Engineering\n")
file.write("Semester: IV\n")

file.close()

print("Student details written successfully.")