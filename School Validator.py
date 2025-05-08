#this is a code I'm trying out on this laptop.
def school():
    student_name = str(input("Dear User, enter your name: "))
    student_age = int(input(f" {student_name}, how old are you?: "))
    #i am trying to make something that can figure classes out, based on age.

    print(f' Dear {student_name}, you are {student_age} years old!')

    if 1 <= student_age < 11 :
        print(f' {student_name}, you should be in a primary school.')

    if 17 < student_age < 25 :
        print(f' {student_name}, you should be at the university')

    elif 11 <= student_age < 17 :
        print(f' {student_name}, you should be at a secondary school')

    elif student_age > 25 :
        print(f' {student_name}, you should not be at any school based on this age')

    elif student_age == 25: 
        print("You are in your university final year")

    while 17 <= student_age <= 25: 
        student_school = str(input(f" Dear {student_name}, enter your school's name: "))
        student_part = str(input(f" Dear {student_name}, what part are you in?"))
        student_department = str(input(f" Dear {student_name}, what is your department?"))
        student_school_1 = ("OAU", "Obafemi Awolowo University", "UI", "University of Ibadan", "Unilag", "Covenant University", "FUNAAB")
        if student_school in student_school_1: 
            print(f""" Dear {student_name}, you are a bonafide {student_part} student of {student_department} at {student_school}!
                Do try to graduate with a good result.""")
            
        else:
            print(f" Dear {student_name}, enter the name of a good university!")
        break

school()
while True:
    school()
    break
        
