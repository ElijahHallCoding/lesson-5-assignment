# Task 1
def add(x, y):
    """Add two numbers."""
    return x + y

def subtract(x, y):
    """Subtract the second number from the first."""
    return x - y

def multiply(x, y):
    """Multiply two numbers."""
    return x * y

def divide(x, y):
    """Divide the first number by the second. Handle division by zero."""
    if y == 0:
        return "Error: Division by zero is not allowed." # Task 3
    else:
        return x / y

# Usage of the functions - Task 2
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

operation = input("Enter choice (1/2/3/4): ") # Task 2

if operation == '1':
    result = add(num1, num2)
    print(f"The result of {num1} + {num2} is {result}")

elif operation == '2':
    result = subtract(num1, num2)
    print(f"The result of {num1} - {num2} is {result}")

elif operation == '3':
    result = multiply(num1, num2)
    print(f"The result of {num1} * {num2} is {result}")

elif operation == '4':
    result = divide(num1, num2)
    print(f"The result of {num1} / {num2} is {result}")

else:
    print("Invalid input. Please select a valid operation.")