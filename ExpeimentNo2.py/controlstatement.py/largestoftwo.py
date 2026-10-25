a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
if a > b:
  print(f"{a} is the largest.")
elif b > a:
  print(f"{b} is the largest.")
else:
  print("Both numbers are equal.")