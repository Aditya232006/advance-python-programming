import matplotlib.pyplot as plt

# Sample data
students = ["Asha", "Ravi", "Neha", "Amit", "Sara"]
marks = [78, 85, 92, 67, 88]

# 1. Line Graph
plt.figure()
plt.plot(students, marks, marker="o")
plt.title("Line Graph of Students' Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# 2. Bar Graph
plt.figure()
plt.bar(students, marks)
plt.title("Bar Graph of Students' Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# 3. Pie Chart
plt.figure()
plt.pie(marks, labels=students, autopct="%1.1f%%")
plt.title("Percentage of Students' Marks")
plt.show()

# 4. Histogram
plt.figure()
plt.hist(marks, bins=5, edgecolor="black")
plt.title("Histogram of Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

# 5. Scatter Plot
plt.figure()
plt.scatter(students, marks)
plt.title("Scatter Plot of Students' Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()