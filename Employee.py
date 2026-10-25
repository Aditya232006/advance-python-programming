#1. Creates an instance of the Employee class. 
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

emp1 = Employee("Madhuri", 50000)

print("Employee Name:", emp1.name)
print("Salary:", emp1.salary)

#2. Initializes all attributes for the employee, including inherited attributes. 
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):

    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)

        
        self.employee_id = employee_id
        self.salary = salary


emp1 = Employee("Madhuri", 20, 101, 50000)

print("Name:", emp1.name)
print("Age:", emp1.age)
print("Employee ID:", emp1.employee_id)
print("Salary:", emp1.salary)

#3. Calls the method to display both personal and employee-specific details.
#  Create two classes: 1. Person: This class will represent a person with basic details like name and age. 2. Employee: This class will inherit from the Person class and add additional functionality related to an employee, such as employee ID and salary. Class Details:
#  ● Person class should have the following attributes: 
# o name: The name of the person.
#  o age: The age of the person. It should also have a method: 
# o display_person_info(): Displays the name and age of the person. 
# ● Employee class should inherit from the Person class and add the following attributes: 
# o employee_id: A unique identifier for the employee. o salary: The salary of the employee. 
# It should also have a method: o display_employee_info():
#  Displays the employees ID, salary, name, and age (make use of the parent class method to display the name and age). 

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        print("Name:", self.name)
        print("Age:", self.age)

class Employee(Person):

    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)

        self.employee_id = employee_id
        self.salary = salary

    def display_employee_info(self):
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)

        self.display_person_info()

emp1 = Employee("Madhuri", 20, 101, 50000)

emp1.display_employee_info()

##########combine three operations in one class
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        print("Name:", self.name)
        print("Age:", self.age)

class Employee(Person):

    def __init__(self, name, age, employee_id, salary):
        # Initialize inherited attributes
        super().__init__(name, age)

        # Initialize employee-specific attributes
        self.employee_id = employee_id
        self.salary = salary

    # Display employee details
    def display_employee_info(self):
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)

        # Call parent class method
        self.display_person_info()


# 1. Create an instance of Employee
emp1 = Employee("Madhuri", 20, 101, 50000)

# 2 & 3. Display personal and employee-specific details
emp1.display_employee_info()
