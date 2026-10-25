# 3. Append additional student information without deleting previous contents
file = open("student.txt", "a")

file.write("\nEmail: madhurifarakate399@gmail.com\n")
file.write("College: D. Y. Patil College of Engineering and Technology\n")

file.close()

print("Additional information added successfully.")