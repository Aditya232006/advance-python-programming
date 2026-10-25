attendance = {}

for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    attendance[day] = set(input("Enter students for " + day + ": ").split())

all_students = set.intersection(*attendance.values())
all_attended = set.union(*attendance.values())

count = {}

for students in attendance.values():
    for student in students:
        count[student] = count.get(student, 0) + 1

print("Attended All Classes:", all_students)
print("Attended Only One Class:", {s for s in count if count[s] == 1})
print("Total Unique Students:", len(all_attended))