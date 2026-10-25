
names = []
grades = []

def add_student():
    name = input("Enter student name: ")
    grade = float(input("Enter grade: "))
    names.append(name)
    grades.append(grade)
    print("Student added successfully!")

def update_grade():
    name = input("Enter student name: ")
    if name in names:
        i = names.index(name)
        grades[i] = float(input("Enter new grade: "))
        print("Grade updated successfully!")
    else:
        print("Student not found!")

def remove_student():
    name = input("Enter student name: ")
    if name in names:
        i = names.index(name)
        names.pop(i)
        grades.pop(i)
        print("Student removed successfully!")
    else:
        print("Student not found!")

def average_grade():
    if grades:
        print("Average Grade:", sum(grades) / len(grades))
    else:
        print("No grades available!")

def highest_lowest():
    if grades:
        print("Highest Grade:", max(grades))
        print("Lowest Grade:", min(grades))
    else:
        print("No grades available!")

def display_students():
    for i in range(len(names)):
        print(names[i], ":", grades[i])

while True:
    print("\n1. Add Student")
    print("2. Update Grade")
    print("3. Remove Student")
    print("4. Average Grade")
    print("5. Highest and Lowest Grade")
    print("6. Display Students")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        update_grade()
    elif choice == '3':
        remove_student()
    elif choice == '4':
        average_grade()
    elif choice == '5':
        highest_lowest()
    elif choice == '6':
        display_students()
    elif choice == '7':
        break
    else:
        print("Invalid choice!")

