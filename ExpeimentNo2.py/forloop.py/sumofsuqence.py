import math

n = int(input("Enter n: "))
total_sum = 0
for i in range(n + 1):
  total_sum += 1 / math.factorial(i)
print("Sum of sequence:", total_sum)