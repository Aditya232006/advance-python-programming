##3. Write python program to demonstrate multilevel inheritance. 
# You need to define three classes: 
# 1. Person: This class will represent a person with basic attributes like name and age. 
# 2. Employee: This class will inherit from Person and add additional attributes related to an employee, 
# such as employee ID and salary. 
# 3. Manager: This class will inherit from Employee and add additional functionality related to a manager, 
# such as department and team size. Class Details:
# 1. Person class should have the following attributes:o name: The name of the person. o age: The age of the person.
#  Method: 
# o display_person_info(): Displays the persons name and age.
# 2. Employee class should inherit from Person and add the following attributes: 
#  o employee_id: The unique employee ID.
#  o salary: The salary of the employee. Method: o display_employee_info(): 
# Displays the employees ID and salary, as well as the name and age using the Person class& s method. 
# 3. Manager class should inherit from Employee and add the following attributes: 
# o department: The department managed by the manager. o team_size: The size of the managers team. Method: 
# o display_manager_info(): Displays the manager and  department, team size, and all information related to the employee and the person. 

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Display person information
    def display_person_info(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Child class of Person
class Employee(Person):

    def __init__(self, name, age, employee_id, salary):
        # Initialize Person attributes
        super().__init__(name, age)

        # Employee-specific attributes
        self.employee_id = employee_id
        self.salary = salary

    # Display employee information
    def display_employee_info(self):
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)

        # Call Person class method
        self.display_person_info()

class Manager(Employee):

    def __init__(self, name, age, employee_id, salary, department, team_size):
        # Initialize Employee attributes
        super().__init__(name, age, employee_id, salary)

        # Manager-specific attributes
        self.department = department
        self.team_size = team_size

    # Display manager information
    def display_manager_info(self):
        print("Department:", self.department)
        print("Team Size:", self.team_size)

        # Call Employee method
        self.display_employee_info()


# Create Manager object
manager1 = Manager(
    "Madhuri",
    20,
    101,
    60000,
    "Computer Science",
    10
)

# Display all information
manager1.display_manager_info()