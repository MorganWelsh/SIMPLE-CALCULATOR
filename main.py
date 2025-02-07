# gui_calculator.py
import tkinter as tk
from tkinter import messagebox
from calculator import add, multiply, divide

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("300x200")

        # Create input fields
        self.num1_label = tk.Label(root, text="Enter first number:")
        self.num1_label.pack()
        self.num1_entry = tk.Entry(root)
        self.num1_entry.pack()

        self.num2_label = tk.Label(root, text="Enter second number:")
        self.num2_label.pack()
        self.num2_entry = tk.Entry(root)
        self.num2_entry.pack()

        # Create operation buttons
        self.add_button = tk.Button(root, text="Add", command=self.perform_add)
        self.add_button.pack()

        self.multiply_button = tk.Button(root, text="Multiply", command=self.perform_multiply)
        self.multiply_button.pack()

        self.divide_button = tk.Button(root, text="Divide", command=self.perform_divide)
        self.divide_button.pack()

        # Create result label
        self.result_label = tk.Label(root, text="Result: ")
        self.result_label.pack()

    def perform_add(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            result = add(num1, num2)
            self.result_label.config(text=f"Result: {result}")
        except ValueError:
            messagebox.showerror("Error", "Invalid input! Please enter numeric values.")

    def perform_multiply(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            result = multiply(num1, num2)
            self.result_label.config(text=f"Result: {result}")
        except ValueError:
            messagebox.showerror("Error", "Invalid input! Please enter numeric values.")

    def perform_divide(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            result = divide(num1, num2)
            self.result_label.config(text=f"Result: {result}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero!")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()