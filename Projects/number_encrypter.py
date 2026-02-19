'''
Name: Carson Gooch
Section: F
Date: Sept 18th
This program encrypts the digits of a phone number.
'''
#General overview of the program
'''
The encryption process of this program largerly relies on the use of
for loops. These for loops seperate the numbers of the phone number.
The way they work is that they use the % to seperate a part of the 
phone number and then that number gets stored into a variable that is
then converted into a int so that there are no decimals and then converted
into a string so that it can be reversed as the way the numbers are seperated
grab the numbers from right to left, not left to right. There is also another 
variable stored in these for loops that stores the number and uses that stored
number for encryption later on.

The first part of the encryption process works based off of the way the 
phone number is orginally seperated. This is because instead of seperating
the entire phone number, only the last 4 digits need to be seperated so that
they can both be encrpted differently. After the numbers are seperated
they are converted into a char then the rest of the phone number is encrypted
by combining the first 3 digits and middle 3 digits and then subtracting
99756473822 from that value. This final encrypted phone number is printed
by rearranging the first value that was converted into a char and moving
that value to the begining of the encrypted phone number and then printing
the value that was subtracted by 99756473822 in the middle and finally
printing the other number that was converted into a char last. 
'''



def main():
    '''
    Solving Homework #1
    '''
    # Prompting the user with a message
    print('Enter a 10 digit phone number (e.g. 5131234567): ', \
          end = '')

    # Saving the given number inside a constant variable
    PHONE_NUM = int(input())
    #This variable stores the last 4 digits of the phone numebr
    phone_store1 = ''
    #Creates a variable that will be used for encrypting later on
    encrypt1 = ''
    #This for loop seperates the phone number, converts it into an int so
    #that the numbers are ronuded, then converts it into a string
    #So that it can be stored in a variable that will be used for reversing
    #the string 
    for i in range(4):
        phone_sep = PHONE_NUM % 10
        phone_sep = int(phone_sep)
        phone_sep = str(phone_sep)
        encrypt1 = encrypt1 + phone_sep
        phone_store1 = phone_store1 + phone_sep
        PHONE_NUM /= 10
    encrypt1 = str(encrypt1)
    #This adds the proper symbols and spaces
    phone_store1 = phone_store1 + ' -'
    #This reverses the string because the for loop above grabbed the last
    #numbers from right to left
    phone_reverse = phone_store1[::-1]


    #Makes phone_sep var back into a int type and creates phone_store2
    #That will store the middle 3 numbers of the number
    phone_sep = int(phone_sep)
    phone_store2 = ' '
    #Creates another variable that will be used for encryption
    encrypt2 = ''
    #This for loop is similar to the one above expect it takes the 3 middle
    #numbers and stores them in a different variable
    for i in range(3):
        phone_sep = PHONE_NUM % 10
        phone_sep = int(phone_sep)
        phone_sep = str(phone_sep)
        encrypt2 = encrypt2 + phone_sep
        phone_store2 = phone_store2 + phone_sep
        PHONE_NUM /= 10
    #Reverses the string
    phone_reverse1 = phone_store2[::-1]


    #Gets phone_sep var back into a int string and establishes the third 
    #variable that will store the first 3 digits of the number
    phone_sep = int(phone_sep)
    phone_store3 = ''
    #Creates another variable that will be used for encryption
    encrypt3 = ''
    #This final loop grabs the first 3 numbers of the phone number and 
    #stores them in one final variable
    for i in range(3):
        phone_sep = PHONE_NUM % 10
        phone_sep = int(phone_sep)
        phone_sep = str(phone_sep)
        encrypt3 = encrypt3 + phone_sep
        phone_store3 = phone_store3 + phone_sep
        PHONE_NUM /= 10
    #adds the proper symbols
    phone_store3 = phone_store3 + '('
    phone_reverse2 = phone_store3[::-1]
    #Adds the proper symbols to the end of the string
    phone_reverse2 = phone_reverse2 + ') '
    #Adds up all stored variables to create the seperated phone number
    final_number = (phone_reverse2 + phone_reverse1 + phone_reverse)
    print(final_number)

    #Converts the last 4 digits into a int 
    encrypt1 = encrypt1[::-1]
    encrypt1 = int(encrypt1)
    #Estables a new variable that will grab the last 2 numbers of the last
    #4 digits of the phone number and store them for encrpytion
    store_encrypt1 = ''
    #Very similar to the loops used throughout this code seperates the last
    # 4 digits into 2 seperate numbers so that they can be encrypted 
    for i in range(2):
        encrypt_sep = encrypt1 % 10
        encrypt_sep = int(encrypt_sep)
        encrypt_sep = str(encrypt_sep)
        store_encrypt1 = store_encrypt1 + encrypt_sep
        encrypt1 /= 10
    
    #Reverses the last 2 digits of the last 4 digits of the phone number
    store_encrypt1 = store_encrypt1[::-1]

    #Estables new var to store the first 2 numbers of the last 4 digits
    #of the phone number 
    store_encrypt2 = ''
    #Cleans up the previous var to be used again on this for loop
    encrypt_sep = ''

    for i in range(2):
        encrypt_sep = encrypt1 % 10
        encrypt_sep = int(encrypt_sep)
        encrypt_sep = str(encrypt_sep)
        store_encrypt2 = store_encrypt2 + encrypt_sep
        encrypt1 /= 10
    
    #Converts the vars storing the 2 seperate numbers from the last 4 digits 
    #into int's so that 33 can be added then it converts these new numbers
    #into char types 
    store_encrypt2 = store_encrypt2[::-1]
    store_encrypt2 = int(store_encrypt2)
    store_encrypt1 = int(store_encrypt1)
    print(store_encrypt1)
    print(store_encrypt2)
    store_encrypt1 = store_encrypt1 + 33
    store_encrypt2 = store_encrypt2 + 33
    store_encrypt2 = chr(store_encrypt2)
    store_encrypt1 = chr(store_encrypt1)
    lastdigit_encryption = '- '
    lastdigit_encryption = lastdigit_encryption + (store_encrypt1 + store_encrypt2)
    print(phone_reverse2 + phone_reverse1 + lastdigit_encryption)
    
    encrypt2 = encrypt2[::-1]

    encrypt3 = encrypt3[::-1]

    #These lines of code combine the 2 numbers stored inside of encrypt2 and
    #encrypt using only addition and subtraction
    #The formula used for this is encrypt2 * 1000 + encrypt3
    #First the numbers are converted into int's
    encrypt2 = int(encrypt2)
    encrypt3 = int(encrypt3)
    encrypt_combined = encrypt3 * 1000
    encrypt_combined = encrypt_combined + encrypt2

    #Now to encrypt this number it is subtracted from 99756473822
    encrypt_combined = encrypt_combined - 99756473822
    #Multiply this by -1 so that the number is not negative
    encrypt_combined = encrypt_combined * -1
    encrypt_combined = str(encrypt_combined)
    print(encrypt_combined)
    #Combines the 2 stored encrypted parts of the last 4 digits of the 
    #phone number and combines it with the rest of it that was also encrypted
    finaloutput = (store_encrypt1 + encrypt_combined + store_encrypt2)
    print(finaloutput)


        

# Using the variable __name__ 
if __name__=="__main__":
    main()
