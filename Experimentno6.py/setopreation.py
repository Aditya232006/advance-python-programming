
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)

a.add(7)
print("After Adding:", a)

a.remove(2)
print("After Removing:", a)

print("Multiplication:", a & b) 
print("Division:", a - b)
print("Transpose:", b | a)