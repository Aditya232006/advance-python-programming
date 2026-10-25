count = int(input("How many numbers? "))
if count > 0:
  i = 1
  max_val = float("-inf")
  while i <= count:
    num = float(input(f"Enter number {i}: "))
    if num > max_val:
      max_val = num
    i += 1
  print("Largest number is:", max_val)