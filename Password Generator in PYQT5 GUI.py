import sys
import random
import string
import pyperclip
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QCheckBox, QVBoxLayout,
    QHBoxLayout, QMessageBox, QSlider
)
from PyQt5.QtCore import Qt

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
    strength_score = 0
    if len(password) >= 12:
        strength_score += 1
    if any(c.isupper() for c in password):
        strength_score += 1
    if any(c.isdigit() for c in password):
        strength_score += 1
    if any(c in custom_symbols for c in password):
        strength_score += 1

    if strength_score <= 1:
        return "Strength: Weak 🔴", "red"
    elif strength_score == 2:
        return "Strength: Fair 🟠", "orange"
    elif strength_score == 3:
        return "Strength: Strong 🟢", "green"
    else:
        return "Strength: Very Strong 🟢🌟", "teal"

class PasswordGeneratorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TheOne Password Generator")
        self.setGeometry(300, 200, 400, 250)

        self.length_display = QLabel("Password Length: 12")
        self.length_slider = QSlider(Qt.Horizontal)
        self.length_slider.setMinimum(5)
        self.length_slider.setMaximum(100)
        self.length_slider.setValue(12)
        self.length_slider.valueChanged.connect(self.update_slider_label)

        self.uppercase_cb = QCheckBox("Include uppercase letters")
        self.digits_cb = QCheckBox("Include digits")
        self.symbols_cb = QCheckBox("Include symbols")

        self.generate_btn = QPushButton("Generate Password")
        self.copy_btn = QPushButton("Copy to Clipboard")
        self.copy_btn.setEnabled(False)

        self.password_output = QLabel("")
        self.password_output.setStyleSheet("font-family: Calibri, Arial, sans-serif; font-size: 16pt; font-weight: bold; color: blue")
        self.password_output.setAlignment(Qt.AlignCenter)

        self.strength_label = QLabel("")
        self.strength_label.setStyleSheet("font-weight: bold; margin-top: 20px")

        self.regenerate_btn = QPushButton("Regenerate")
        self.regenerate_btn.setEnabled(False)
        self.restart_btn = QPushButton("Restart")
        self.restart_btn.setEnabled(False)

        layout = QVBoxLayout()
        layout.addWidget(self.length_display)
        layout.addWidget(self.length_slider)
        layout.addWidget(self.uppercase_cb)
        layout.addWidget(self.digits_cb)
        layout.addWidget(self.symbols_cb)
        layout.addWidget(self.generate_btn)
        layout.addWidget(self.password_output)
        layout.addWidget(self.strength_label)
        layout.addWidget(self.copy_btn)

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.regenerate_btn)
        btn_layout.addWidget(self.restart_btn)
        layout.addLayout(btn_layout)

        self.setLayout(layout)

        self.generate_btn.clicked.connect(self.handle_generate)
        self.copy_btn.clicked.connect(self.copy_password)
        self.regenerate_btn.clicked.connect(self.handle_generate)
        self.restart_btn.clicked.connect(self.reset_form)

        self.last_password = ""

    def update_slider_label(self):
        self.length_display.setText(f"Password Length: {self.length_slider.value()}")

    def handle_generate(self):
        length = self.length_slider.value()
        use_upper = self.uppercase_cb.isChecked()
        use_digits = self.digits_cb.isChecked()
        use_symbols = self.symbols_cb.isChecked()

        password = generate_password(length, use_upper, use_digits, use_symbols)
        if password.startswith("Error"):
            QMessageBox.warning(self, "Error", password)
            return

        self.last_password = password
        self.password_output.setText(f"{password}")

        label_text, color = assess_strength(password)
        self.strength_label.setText(label_text)
        self.strength_label.setStyleSheet(f"font-weight: bold; color: {color}; margin-top: 20px")

        self.copy_btn.setEnabled(True)
        self.regenerate_btn.setEnabled(True)
        self.restart_btn.setEnabled(True)

    def copy_password(self):
        if self.last_password:
            pyperclip.copy(self.last_password)
            QMessageBox.information(self, "Copied", "Password copied to clipboard.")

    def reset_form(self):
        self.length_slider.setValue(12)
        self.uppercase_cb.setChecked(False)
        self.digits_cb.setChecked(False)
        self.symbols_cb.setChecked(False)
        self.password_output.setText("")
        self.strength_label.setText("")
        self.copy_btn.setEnabled(False)
        self.regenerate_btn.setEnabled(False)
        self.restart_btn.setEnabled(False)
        self.last_password = ""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordGeneratorApp()
    window.show()
    sys.exit(app.exec_())
