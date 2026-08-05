# Program to create a simple calculator

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y


def main():
    print("Simple Calculator")
    print("Operations: +, -, *, /")

    while True:
        operator = input("Enter operator (+, -, *, /) or 'q' to quit: ")
        if operator.lower() == 'q':
            print("Goodbye!")
            break

        if operator not in ['+', '-', '*', '/']:
            print("Invalid operator")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if operator == '+':
            print("Result:", add(num1, num2))
        elif operator == '-':
            print("Result:", subtract(num1, num2))
        elif operator == '*':
            print("Result:", multiply(num1, num2))
        elif operator == '/':
            print("Result:", divide(num1, num2))


if __name__ == "__main__":
    main()

