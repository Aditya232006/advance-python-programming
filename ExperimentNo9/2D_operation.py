import numpy as np

A = np.array([
    [10, 20],
    [30, 40]
])

B = np.array([
    [2, 4],
    [5, 8]
])

print("Array A:")
print(A)

print("Array B:")
print(B)

print("Addition:")
print(A + B)

print("Subtraction:")
print(A - B)

print("Multiplication:")
print(A * B)

print("Division:")
print(A / B)

print("Transpose of A:")
print(A.T)

print("Exponential of A:")
print(np.exp(A))