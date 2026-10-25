def read_employees():
    file = open("employees.txt", "r")

    employees = []

    for line in file:
        emp_id, name, department, salary = line.strip().split(",")

        employees.append({
            "id": emp_id,
            "name": name,
            "department": department,
            "salary": float(salary)
        })

    file.close()

    return employees


def display_all(employees):
    print("\nAll Employees:")

    for emp in employees:
        print(emp["id"], emp["name"], emp["department"], emp["salary"])

def highest_paid(employees):
    employee = max(employees, key=lambda x: x["salary"])

    print("\nHighest-Paid Employee:")
    print(employee["name"], "-", employee["salary"])


# Calculate average salary
def average_salary(employees):
    total = sum(emp["salary"] for emp in employees)
    average = total / len(employees)

    print("\nAverage Salary:", average)



def above_salary(employees, amount):
    print("\nEmployees earning above", amount, ":")

    for emp in employees:
        if emp["salary"] > amount:
            print(emp["name"], "-", emp["salary"])


employees = read_employees()

display_all(employees)

highest_paid(employees)

average_salary(employees)

amount = float(input("\nEnter salary amount: "))

above_salary(employees, amount)