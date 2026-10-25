n = int(input("Enter n: "))
fact = 1
i = 1
while i <= n:
  fact *= i
  i += 1
print("Factorial:", fact)