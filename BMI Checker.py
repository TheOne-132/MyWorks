#This is a BMI Calculator
#Ever since I learnt the way dramatic_print works, I have been using it in all my projects.
import time

def bmi_calculator():
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

    weight = float(input("Please enter your weight in kilograms(kg): "))
    height = float(input("Please enter your height in metres(m): "))

    bmi = weight / (height ** 2)

    if bmi < 18.5:
        print()
        dramatic_print(f"Your BMI is {bmi:.2f}")
        dramatic_print("Your BMI Category is underweight, please eat balanced diet and consult a healthcare personnel.")
    elif bmi >= 18.5 and bmi <= 24.9:
        print()
        dramatic_print(f"Your BMI is {bmi:.2f}") 
        dramatic_print("Your BMI Category is normal, kindly keep up the good work.")
    elif bmi > 24.9:
        print()
        dramatic_print(f"Your BMI is {bmi:.2f}")
        dramatic_print(f"Your BMI Category is overweight, please exercise more often and consult a healthcare personnel.")

    print()
    loop = input("Do you want to check your BMI again? (yes/no): ").strip().lower()
    while loop == "yes":
        return True
    else:
        print()
        dramatic_print("Thank you for using the BMI Checker!")
        dramatic_print("TheOne made it.")

while bmi_calculator():
    pass