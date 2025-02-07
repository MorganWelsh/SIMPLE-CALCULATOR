# main.py
from calculator import add, multiply, divide

def main():
    print("Welcome to the Simple Calculator!")
    print("This calculator can perform addition, multiplication, and division.")

    # Get user input
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    # Choose operation
    operation = input("Choose operation (add/multiply/divide): ").strip().lower()

    if operation == "add":
        result = add(num1, num2)
        print(f"The result of {num1} + {num2} is: {result}")
    elif operation == "multiply":
        result = multiply(num1, num2)
        print(f"The result of {num1} * {num2} is: {result}")
    elif operation == "divide":
        try:
            result = divide(num1, num2)
            print(f"The result of {num1} / {num2} is: {result}")
        except ValueError as e:
            print(e)
    else:
        print("Invalid operation! Please choose 'add', 'multiply', or 'divide'.")

if __name__ == "__main__":
    main()