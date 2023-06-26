#Dynamic password Generator
# 1st: import random and string
import random
import string # for grab all lower and uppercase letter + special characters +  ? numbers ?

#the function below needs 3 parameters, min_lenght is number, others are optional parameters
#min_lenght = how many length user wants he's password include
#number=True : means the password includs numbers ( user chooses )
#special_characters=True : means the password includs characters( user chooses )
def generate_password( min_lenght , numbers=True, special_characters=True):
    print(numbers, special_characters)
    #here we call letters,numbers and punctuations, then put them in differente variable (like: abcdefgABCDEFG)
    letter = string.ascii_letters # all lower and uppercase letters (like: abcdefgABCDEFG)
    digits = string.digits # all numbers (1234567890)
    special = string.punctuation # all punctuations (like: !"#$%&'()*+,-./ )

    password_ = letter # ouser password atleast will include letters
    if numbers == True: # if user needs number in the password 
        password_ += digits
    if special_characters == True: # if user needs characters in the password 
        password_ += special

    pwd = "" # the generated password will keap in PWD 
    meets_criteria = False # for checking that password includs number and special
    has_number = False
    has_special = False
    
    while not meets_criteria  or  len(pwd) < min_lenght: # to be sure that the generated passwor is correct
        new_char = random.choice(password_) # here we use random to choose a char from password_
        pwd += new_char # after choosing, then put it in pwd

        if new_char in digits: # then we check that the chosen char is digit or special
            has_number = True
        elif new_char in special:
            has_special = True
            
        meets_criteria = True
        if numbers: # number == True
            meets_criteria = has_number
        if special_characters: # special_character == True
            meets_criteria = meets_criteria and has_special
            
    return pwd

min_lenght = int(input("enter the minimum lenght: "))
has_number = input("Do you want to have numbers (y/n) ? ").lower() == "y"
has_special = input("Do you want to have special character (y/n) ? ").lower() == "y"

pwd = generate_password(min_lenght, has_number, has_special)
print("your password is: ", pwd)
