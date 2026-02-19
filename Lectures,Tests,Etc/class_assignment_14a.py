'''
Author:Carson Gooch
Class:CSE 174
Section:F
Date December 2nd, 2024
'''


def check_length(p) -> bool:
    return len(password) >= 8

def check_lower(password : str) -> bool:
    for ch in password:
        if ch.islower():
            return True
    return False


def check_upper(password : str) -> bool:
    for ch in password:
        if ch.isupper():
            return True
    return False

def check_characters(password : str) -> bool:
    for ch in password:
        if ch == "!" or ch == "@" or ch ==  "^" or ch ==  "#":
            return True
    return False

def num_check(password : str) -> bool:
    for ch in password:
        if ch.isdigit():
            return True
    return False


def validate_password(password : str) -> bool:

    if not check_length(password):
        print("The length must be at least 8 characters")
        return False

    if not check_lower(password):
        print("There must be at least 1 lower case letter")
        return False

    if not check_upper(password):
        print("There must be at least 1 upper case letter")
        return False

    if not check_characters(password):
        print("One of these must be in the password !, #, @, ^")
        return False
    
    if not num_check(password):
        print("The password must have at least one number")
        return False

    return True 


if __name__ == "__main__":
    password = input("Enter a password: ")
    print(validate_password(password))