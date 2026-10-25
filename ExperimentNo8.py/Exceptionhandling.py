try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

    numbers = [10, 20, 30]
    index = int(input("Enter index: "))
    print("Element =", numbers[index])

except ValueError:
    print("Error: Please enter numbers only.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except IndexError:
    print("Error: Index is out of range.")

except TypeError:
    print("Error: Invalid data type.")

except Exception as e:
    print("Some other error occurred:", e)

else:
    print("All operations completed successfully.")

finally:
    print("Program execution completed.")