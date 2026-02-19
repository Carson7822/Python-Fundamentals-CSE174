'''
Name: Carson Gooch
Section: F
Date:September 18th, 2024
This program encrypts the digits of a phone number.
'''

'''
My previous attempt on this project used str and int function which was not
allowed to be used so I created a new project that does not use those functions

This project works by having for loops that seperate the phone number and then
rounding the number by using the math.floor function and then combining those
numbers inside of a variable to be used later on

This program also uses a while loop to reverse the order of the numbers since
the numbers are grabbed from right to left

Then the last 4 digits are encrypted using the chr function and addition
while the first 6 digits are encrypted through subtraction
then the final output is printed onto the screen with the fully encrypted
phone number. 
'''



import math

def main():
    '''
    Solving Homework #1
    '''
    # Prompting the user with a message
    print('Enter a 10 digit phone number (e.g. 5131234567): ', \
          end = '')

    # Saving the given number inside a constant variable
    PHONE_NUM = int(input())
    #Establishes a variable to store the last 4 numbers of the phone number
    phone_store = 0
    #This variable is used to store the number for encryption later on
    #A for loop that extracts the last 4 digits of the phone number and stores
    #Them inside of a variable 
    for i in range(4):
        phone_sep = PHONE_NUM % 10
        #Rounds the number down
        phone_sep = math.floor(phone_sep)
        PHONE_NUM /= 10
        #Multiplys this var by 10 and then adds the next number to it
        #This combines the number without the use of strings
        phone_store = phone_store * 10
        phone_store = phone_store + phone_sep

    #Establshes var to reverse the phone_store var
    reverse_num = 0

    #This while loop manipulates the numbers into reverse order without the 
    #use of string manipulation
    while phone_store != 0:
        digit = phone_store % 10
        reverse_num = reverse_num * 10 + digit
        phone_store //= 10

    #Does the same thing as the first for loop did but this one seperates
    #The middle 3 numbers of the phone number
    for i in range(3):
        phone_sep = PHONE_NUM % 10
        phone_sep = math.floor(phone_sep)
        PHONE_NUM /= 10
        phone_store = phone_store * 10
        phone_store = phone_store + phone_sep

    #Saves the last 4 digits in a var
    last4digits = reverse_num
    #Sets the reverse_num var back to zero
    reverse_num = 0
    #Does the same thing as the first while loop but this one reverses
    #The middle 3 numbers without string manipulation
    while phone_store != 0:
        digit = phone_store % 10
        reverse_num = reverse_num * 10 + digit 
        phone_store //= 10

    #Does the same thing as the first 3 for loops but this one extracts
    #The last 3 numbers of the phone number
    for i in range(3):
        phone_sep = PHONE_NUM % 10
        phone_sep = math.floor(phone_sep)
        PHONE_NUM /= 10
        phone_store = phone_store * 10
        phone_store = phone_store + phone_sep
    
    #Saves the middle 3 digits in a var
    middle3digits = reverse_num
    #Sets reverse_num back to zero 
    reverse_num = 0

    #Reverses the first 3 numbers 
    while phone_store != 0:
        digit = phone_store % 10
        reverse_num = reverse_num * 10 + digit
        phone_store //= 10
    
    #Saves the first 3 digits in a var
    first3digits = reverse_num

    #Creates symbols used in the output of the phone number
    parentheses1 = '('
    parentheses2 = ')'
    dash = '-'

    #Prints the fully seperated phone number
    print('%s%d%s %d %s %d' % (parentheses1, first3digits, parentheses2, \
                               middle3digits,dash, last4digits))
    
    #Now that the phone number has been seperated and formmated the correct
    #way, the remaining code will encrypt the phone number

    #Clear the phone store var to be used in a similar for loop
    #that seperates the last 4 digits of the number into 2 seperate
    #numbers
    phone_store = 0
    for i in range(2):
        phone_sep = last4digits % 10
        phone_sep = math.floor(phone_sep)
        last4digits /= 10
        phone_store = phone_store * 10
        phone_store = phone_store + phone_sep
    #Rounds the last 4 digits down so that it is a number without
    #decimal places
    last4digits = math.floor(last4digits)
    #The var phone_store is currently holding the last 2 digits of the phone
    #Number, however, they are in reverse order so the next section of code
    #Will put this code back in the correct order so that encryption can
    #take place

    #Clears previous value out of reverse_num var
    reverse_num = 0
    
    #Reverses the order of the last 2 digits
    while phone_store != 0:
        digit = phone_store % 10
        reverse_num = reverse_num * 10 + digit
        phone_store //= 10
    #Saves reverse_num var into a different var
    last2digits = reverse_num
    #Encryption process for the last 4 digits of the phone number
    last2digits = last2digits + 33
    last4digits = last4digits + 33

    #Converts both sseperate numbers into char types for encryption
    last2digits = chr(last2digits)
    last4digits = chr(last4digits)

    #Prints out the full phone number with the last 4 digits encrypted
    print('%s%d%s %d %s %s%s' % (parentheses1, first3digits, parentheses2, \
                               middle3digits,dash, last2digits,last4digits))
    
    #Finally the first 6 digits of the phone number will now be encrypted
    #These next 2 lines of code combine the first 3 digits and middle 3 digits
    #without the use of string manipulation
    first3digits = first3digits * 1000
    first6digits_encrypt = first3digits + middle3digits

    #This line of code subtracts 99756473822 from the first 6 digits of the
    #phone number so that it can be encrypted
    first6digits_encrypt = first6digits_encrypt - 99756473822
    #This multiplys the number by -1 so that the number is not negative
    first6digits_encrypt = first6digits_encrypt * -1

    print(first6digits_encrypt)

    #Finally the fully encrypted phone number is printed
    print('%s%d%s' % (last2digits, first6digits_encrypt, last4digits))



# Using the variable __name__ 
if __name__=="__main__":
    main()
