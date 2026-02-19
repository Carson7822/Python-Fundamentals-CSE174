'''
CSE 174
Section F
Carson Gooch

This program asks the user if they want to convert a letter with binary code
a word with binary code or if they want to exit the program. This program will
continue to loop through this and will allow the user to convert letters and
words until the user decides to exit the program. 
'''


# Practicing writing functions.

# TODO
# ADD get_letter() and get_word functions here

def menu() -> None:
    """
    Prints a menu with options on the display.

    Args: 
        None
    
    Returns: 
        None
    """
    print('**Binary Code Translator v 1.0**')
    print('1. Translate a binary code into a letter')
    print('2. Translate binary codes into a word')
    print('3. Exit\nEnter a number [1-3]: ', end = '')

def main():
    option = -1

    while(option != 3):
        menu()
        try:
            option = int(input())
        except ValueError as e:
            option = 0
        
        match(option):
            case 1:
                print('Enter a single binary code: ', end = '')
                letter = get_letter(input())
                print('The letter is: %s\n' % (letter))
            case 2:
                print('Enter binary codes: ', end = '')
                word = get_word(input())
                print('The word is: %s\n' % (word))
            case 3:
                print('End!')
            case _:
                print('Invalid input!')
            
def get_letter(number: str) -> str:

    '''
    This function takes in a 8 digit binary code and converts that code into a
    letter by running through a for loop 7 times and splitting the string into
    4 different parts and then it performs a binary to ASC conversion on each
    string that was split.

    Args:
        (number): the 8 digit number that was inputted by the user
    
    Returns:
        The answer variable that is converted using chr. Answer is all of the
        different strings added up after the conversion.
    '''

    answer = 0
    power = 0
    for i in range(7, -1, -1):
        if (number[i] == '1'):
            answer += 1 * (2 ** power)
        power  += 1
    return chr(answer)


def get_word(number: str) -> str:
    '''
    This function takes in a binary word and uses the get letter function
    to convert each 8 digits into a letter, and adds the letters to the word
    variable so that it can be printed.

    Args:
        (number): The binary code that the user inputs
    
        Returns:
            The word variable that is all of the letters added up into a single
            string. 
    '''
    word = ''
    for i in range(0, len(number), 8):
        letter_one = number[i: i + 8]
        word = word + get_letter(letter_one)
    return(word)
        
        
    




if __name__=="__main__":
    main()




