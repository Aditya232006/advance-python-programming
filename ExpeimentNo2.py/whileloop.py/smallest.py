count = int(input("How many numbers? "))
if count > 0:
  i = 1
  min_val = float("inf")
  while i <= count:
    num = float(input(f"Enter number {i}: "))
    if num < min_val:
      min_val = num
    i += 1
  print("Smallest number is:", min_val)