import math

n = float(input("Enter a number: "))
sq_root = int(math.isqrt(int(n)))
print(f"Square root is: {sq_root}")

if sq_root <= 1:
  print("Not Prime")
else:
  is_prime = True
  for i in range(2, int(math.sqrt(sq_root)) + 1):
    if sq_root % i == 0:
      is_prime = False
      break
  if is_prime:
    print("Square root is Prime.")
  else:
    print("Square root is Not Prime.")