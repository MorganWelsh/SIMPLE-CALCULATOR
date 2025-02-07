# main.py
from calculator import add, multiply

def main():
    print("Welcome to the Simple Calculator!")
    print("This calculator can perform addition and multiplication.")

    # Get user input
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    # Choose operation
    operation = input("Choose operation (add/multiply): ").strip().lower()

    if operation == "add":
        result = add(num1, num2)
        print(f"The result of {num1} + {num2} is: {result}")
    elif operation == "multiply":
        result = multiply(num1, num2)
        print(f"The result of {num1} * {num2} is: {result}")
    else:
        print("Invalid operation! Please choose 'add' or 'multiply'.")

if __name__ == "__main__":
    main()