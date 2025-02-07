# calculator.py

def add(x, y):
    """Function to add two numbers"""
    return x + y

def multiply(x, y):
    """Function to multiply two numbers"""
    return x * y

def divide(x, y):
    """Function to divide two numbers"""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y