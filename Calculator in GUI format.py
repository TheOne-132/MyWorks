import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            result = num1 / num2
        elif operation == "Exponential":
            result = num1 ** num2
        elif operation == "Floor Modulus":
            result = num1 // num2
        elif operation == "Modulus":
            result = num1 % num2
        else:
            messagebox.showerror("Error", "Please select a valid operation")
            return

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero.")
    except OverflowError:
        messagebox.showerror("Error", "Result is too large.")

# GUI setup
root = tk.Tk()
root.title("Simple GUI Calculator")
root.geometry("350x300")
root.resizable(False, False)

# Widgets
tk.Label(root, text="Enter first number:").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter second number:").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack()

tk.Label(root, text="Choose operation:").pack(pady=5)
operation_var = tk.StringVar()
operation_dropdown = ttk.Combobox(root, textvariable=operation_var)
operation_dropdown['values'] = ("Addition", "Subtraction", "Multiplication", "Division", "Modulus", "Exponential", "Floor Modulus")
operation_dropdown.pack()

tk.Button(root, text="Calculate", command=calculate).pack(pady=10)

result_label = tk.Label(root, text="Result: ", font=("ALGERIAN", 12, "bold"))
result_label.pack(pady=10)

tk.Button(root, text="Exit", command=root.quit).pack(pady=5)

# Run the GUI loop
root.mainloop()