#I_don't_know_what_I_want_to_do_yet
#I am not so good with creating my own custom functions yet, so, I'm trying out alternatives.
#trying to define username.
def userdata():
    user_name1 = str(input("Enter a name: "))
    def user_name():
        if type(user_name1) != str and len(user_name1) < 2:
            print("Invalid name, please try again.")
        elif type(user_name1) == str and len(user_name1) >= 2:
            print(f" Hello {user_name1}, welcome to the website")
            return True
        
     #trying to define email.
    user_email1 = str(input(f" {user_name1}, provide an email:"))
    def user_email():
        if type(user_email1) != str and len(user_email1) <= 4:
            print(f" {user_name1}, please check your email and try again")
        elif not any(char.isdigit() for char in user_email1):
                print(f" {user_name1}, please check your email and try again")
        elif "@" not in user_email1:
                print(f" {user_name1}, please check your email and try again")
        elif "." not in user_email1:
                print(f" {user_name1}, please check your email and try again")
        else: 
            print(f" {user_name1}, your email has been verified successfully!")
            print(f" {user_name1}, your email is {user_email1}")
            return True

    #trying to define password.
    user_password1 = str(input(f" {user_name1}, create a password:"))
    def user_password():
        if type(user_password1) != str and len(user_password1) <= 4:
            print(f" {user_name1}, please check your password length and try again")
        elif not any(char.isdigit() for char in user_password1):
                    print(f" {user_name1}, your password must include at least a number")
        elif not any(char.isupper() for char in user_password1):
                    print(f" {user_name1}, your password must include an uppercase")
        else: 
            print(f" {user_name1}, your password has been created successfully")
            print(f" {user_name1}, your password is {user_password1}")
            print("Please remember to keep your password safe and secure.")
            print("You can now log in to your account.")
            return True

    # Creating a dictionary to store user information
    user_dict = {
        "name": user_name1,
        "email": user_email1,
        "password": user_password1
    }

    if user_name() == True and user_password() == True and user_email() == True:
        print("You have successfully created your profile.")
        print(f" {user_name1}, these are your credentials; {user_dict}")
    else:
        print("Please check your inputs and try again.")
        print("User, please start over or quit")
        userdata()

userdata()

