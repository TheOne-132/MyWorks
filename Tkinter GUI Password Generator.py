import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

custom_symbols = "@#$%&_-"

def generate_password(length, use_upper, use_digits, use_symbols):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_upper else ''
    digits = string.digits if use_digits else ''
    symbols = custom_symbols if use_symbols else ''
    all_chars = lower + upper + digits + symbols

    if not all_chars:
        return "Error: No character types selected."
    if length <= 0:
        return "Error: Password length must be greater than 0."

    first_char_options = lower + upper
    if not first_char_options:
        return "Error: At least one letter must be included to start the password."

    password_chars = [random.choice(first_char_options)]
    required_chars = []

    if use_upper:
        required_chars.append(random.choice(string.ascii_uppercase))

    digit_count = max(1, int(length * 0.2)) if use_digits else 0
    symbol_count = max(1, int(length * 0.15)) if use_symbols else 0

    if use_digits:
        for _ in range(digit_count):
            required_chars.append(random.choice(string.digits))
    if use_symbols:
        for _ in range(symbol_count):
            required_chars.append(random.choice(custom_symbols))

    while len(password_chars) + len(required_chars) < length:
        password_chars.append(random.choice(all_chars))

    password_chars.extend(required_chars)
    random.shuffle(password_chars[1:])
    return ''.join(password_chars)

def assess_strength(password):
    score = 0
    if len(password) >= 12:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in custom_symbols for c in password):
        score += 1

    if score <= 1:
        return "Weak 🔴", "red"
    elif score == 2:
        return "Fair 🟠", "orange"
    elif score == 3:
        return "Strong 🟢", "green"
    else:
        return "Very Strong 🌟", "teal"

class PasswordApp:
    def __init__(self, root):
        self.root = root
        root.title("TheOne Password Generator")
        root.geometry("500x400")

        self.length_label = tk.Label(root, text="Password Length:")
        self.length_label.pack()

        self.length_slider = tk.Scale(root, from_=5, to=100, orient="horizontal")
        self.length_slider.set(12)
        self.length_slider.pack()

        self.uppercase_var = tk.BooleanVar()
        self.digits_var = tk.BooleanVar()
        self.symbols_var = tk.BooleanVar()

        tk.Checkbutton(root, text="Include uppercase letters", variable=self.uppercase_var).pack()
        tk.Checkbutton(root, text="Include digits", variable=self.digits_var).pack()
        tk.Checkbutton(root, text="Include symbols", variable=self.symbols_var).pack()

        self.generate_btn = tk.Button(root, text="Generate Password", command=self.generate)
        self.generate_btn.pack(pady=5)

        self.password_display = tk.Label(root, text="", font=("Arial Black", 16), fg="blue")
        self.password_display.pack()

        self.strength_label = tk.Label(root, text="", font=("Calibri Heading", 10, "bold"))
        self.strength_label.pack(pady=5)

        self.copy_btn = tk.Button(root, text="Copy to Clipboard", command=self.copy, state="disabled")
        self.copy_btn.pack()

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        self.regen_btn = tk.Button(self.button_frame, text="Regenerate", command=self.generate, state="disabled")
        self.regen_btn.pack(side="left", padx=10)

        self.restart_btn = tk.Button(self.button_frame, text="Restart", command=self.reset, state="disabled")
        self.restart_btn.pack(side="right", padx=10)

        self.last_password = ""

    def generate(self):
        length = self.length_slider.get()
        upper = self.uppercase_var.get()
        digits = self.digits_var.get()
        symbols = self.symbols_var.get()

        password = generate_password(length, upper, digits, symbols)
        if password.startswith("Error"):
            messagebox.showerror("Error", password)
            return

        self.last_password = password
        self.password_display.config(text=password)

        label, color = assess_strength(password)
        self.strength_label.config(text=label, fg=color)

        self.copy_btn.config(state="normal")
        self.regen_btn.config(state="normal")
        self.restart_btn.config(state="normal")

    def copy(self):
        if self.last_password:
            pyperclip.copy(self.last_password)
            messagebox.showinfo("Copied", "Password copied to clipboard.")

    def reset(self):
        self.length_slider.set(12)
        self.uppercase_var.set(False)
        self.digits_var.set(False)
        self.symbols_var.set(False)
        self.password_display.config(text="")
        self.strength_label.config(text="")
        self.copy_btn.config(state="disabled")
        self.regen_btn.config(state="disabled")
        self.restart_btn.config(state="disabled")
        self.last_password = ""

root = tk.Tk()
app = PasswordApp(root)
root.mainloop()
