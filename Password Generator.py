import random
import string
import time
import pyperclip

def dramatic_print(message, letter_delay=0.03, word_delay=0.2, line_delay=1.0):
    for line in message.split('\n'):
        for word in line.split():
            for letter in word:
                print(letter, end='', flush=True)
                time.sleep(letter_delay)
            print(' ', end='', flush=True)
            time.sleep(word_delay)
        print()
        time.sleep(line_delay)

def generate_password(length, use_upper, use_digits, use_symbols):
    custom_symbols = "!@#$%&_~-"

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

    digit_count = int(length * 0.2) if use_digits else 0
    symbol_count = int(length * 0.15) if use_symbols else 0

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

def main():
    dramatic_print("Welcome to the Password Generator Tool!")

    while True:
        try:
            while True:
                length = int(input("Enter desired password length: "))
                if length <= 4:
                    print("Password length must be 5 or more.")
                else:
                    break

            use_upper = input("Do you want to include uppercase letters? (yes/no): ").lower() == 'yes'
            use_digits = input("Do you want to include digits? (yes/no): ").lower() == 'yes'
            use_symbols = input("Do you want to include symbols? (yes/no): ").lower() == 'yes'

            while True:
                password = generate_password(length, use_upper, use_digits, use_symbols)
                dramatic_print(f"\nYour generated password is; {password}")

                copy = input("Do you want to copy the password to clipboard? (yes/no): ").lower()
                if copy == 'yes':
                    pyperclip.copy(password)
                    dramatic_print("Password copied to clipboard.")

                try:
                    while True:
                        response = input("Are you satisfied with the password? (1: yes / 2: regenerate / 3: restart): ").strip()
                        if response == '1':
                            dramatic_print("""Password confirmed. Thank you for using the Password Generator Tool.
                            TheOne Made it!""")
                            return
                        elif response == '2':
                            break
                        elif response == '3':
                            raise Exception("restart")
                        else:
                            print("Invalid choice. Please type '1', '2', or '3'.")
                except Exception as e:
                    if str(e) == "restart":
                        break

        except ValueError:
            dramatic_print("Invalid input. Please enter a number for the password length.")

if __name__ == "__main__":
    main()