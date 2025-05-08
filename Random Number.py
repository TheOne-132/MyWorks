def guess_number():
    import random
    number_to_guess = random.randint(1, 10)
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == number_to_guess:
        print("Congratulations, you guessed it!")
    else:
        print(f"Sorry, the number was; {number_to_guess}")

    loop = input("Do you want to play the guessing game again? (yes/no): ").strip().lower()
    while loop == "yes":
        return True
    else:
        print("Thank you for playing!")
        print("Created by TheOne")

while guess_number():
    pass
