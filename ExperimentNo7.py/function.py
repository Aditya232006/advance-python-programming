class Calculator:
    def add(self, a, b):
        result = a + b
        print("Addition:", result)
    def multiply(self, a, b):
            result = a * b
            print("Multiplication:", result)
    def divide(self, a, b):
        if b != 0:
            result = a / b
            print("Division:", result)
        else:
            print("Division by zero is not allowed.")
c1 = Calculator()

c1.add(10, 20)
c1.multiply(10, 20)
c1.divide(20, 10)