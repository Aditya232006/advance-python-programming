class Calculator:
    def add(self, a, b, c=0, d=0):
        return a + b + c + d

cal = Calculator()

print("Sum of 2 numbers:", cal.add(10, 20))
print("Sum of 3 numbers:", cal.add(10, 20, 30))
print("Sum of 4 numbers:", cal.add(10, 20, 30, 40))