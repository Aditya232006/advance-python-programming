import math

x = float(input("Enter value of x (in radians): "))
n = int(input("Enter number of terms: "))
cos_val = 0
for i in range(n):
  sign = (-1) ** i
  power = 2 * i
  cos_val += sign * (x**power) / math.factorial(power)
print("Cosine value:", cos_val)