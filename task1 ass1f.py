# Task 1: Perform Basic Mathematical Operations

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("\nAddition:", num1 + num2)
    print("Subtraction:", num1 - num2)
    print("Multiplication:", num1 * num2)

    if num2 != 0:
        print("Division:", num1 / num2)
    else:
        print("Division: Cannot divide by zero.")

except ValueError:
    print("Invalid input! Please enter valid numbers.")