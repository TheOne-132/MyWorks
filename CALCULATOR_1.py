#This is me trying to create a simple calculator
#Putting it in a function so I can call and uncall

def calculator():
    num_1 = float(input("Enter the first number you want to perform a calculation on: "))
    num_2 = float(input("Enter the second number you want to perform a calculation on: "))

    addi = num_1 + num_2
    subtr = num_1 - num_2
    divi = num_1/num_2
    multi = num_1 * num_2
    expo = num_1 ** num_2
    floo = num_1//num_2
    modu = num_1 % num_2

    operations = ["addition", "subtraction", "division", "multiplication", "exponential", "floor division", "modulus"]
    print(f""" The available operations are; {operations}.
          Choose 1 for Addition, 2 for Subtraction, 3 for Division, 4 for Multiplication, 5 for Exponent, 6 for Floor Division and 7 for Modulus""")
    operation_1 = int(input("What operation do you want to perform amongst the above? "))

    if operation_1 == 1:
        print(f' Your result is; {addi}')
    elif operation_1 == 2:
        print(f' Your result is; {subtr}')
    elif operation_1 == 3:
        print(f' Your result is; {divi}')
    elif operation_1 == 4:
        print(f' Your result is; {multi}')
    elif operation_1 == 5:
        print(f' Your result is; {expo}')
    elif operation_1 == 6:
        print(f' Your result is; {floo}')
    elif operation_1 == 7:
        print(f' Your result is; {modu}')
    else:
        print("Please, enter a valid operation")

    loop = str(input("Do you want to continue calculating? Choose either 'yes' or 'no': "))
    if loop == "yes":
        return True
    else:
        print("Nice having you, dear user")
        print("Created by TheOne")
        return False

while calculator():
    pass
        