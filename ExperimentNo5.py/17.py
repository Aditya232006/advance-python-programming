file = open("students.txt", "r")

lines = file.readlines()

file.close()

students = []

for line in lines[1:]:
    roll, name, marks = line.strip().split(",")
    
    students.append({
        "roll": roll,
        "name": name,
        "marks": int(marks)
    })

print("All Student Records:")

for student in students:
    print(student["roll"], student["name"], student["marks"])

highest = max(students, key=lambda x: x["marks"])

print("\nStudent with highest marks:")
print(highest["name"], "-", highest["marks"])

total = sum(student["marks"] for student in students)
average = total / len(students)

print("\nAverage Marks:", average)

print("\nStudents scoring more than 80:")

for student in students:
    if student["marks"] > 80:
        print(student["name"], "-", student["marks"])