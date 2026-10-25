p1 = set(input("Enter Project 1 employees: ").split())
p2 = set(input("Enter Project 2 employees: ").split())

print("Common Employees:", p1 & p2)
print("Only Project 1:", p1 - p2)
print("Only Project 2:", p2 - p1)
print("All Employees:", p1 | p2)
print("Total Employees:", len(p1 | p2))