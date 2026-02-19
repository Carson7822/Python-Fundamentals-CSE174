'''
Author:Carson Gooch
Class:CSE 174
Section:F
Date:November 8th, 2024

My working code for midterm exam 2
'''




def sum_evens(start: int, end: int) -> None:
    '''
    This function takes 2 Variables. Start and end and takes all of the even
    numbers inbetween those 2 variables. It does this using a while loop and
    an if and else statement. Finally, the function prints out sum of all of 
    the even numbers inbetween the variables.

    Args:
        (start) The first number inputted into the function
        (end) The second number inputted into the function

    Returns:
        None
    '''



    total = 0
    while(start <= end):
        if(start % 2 == 0):
            total += start
            start += 1
        else:
            start += 1
    print(total)
#------------------------------------------------------------------------------



def subtract_digits(word: str) -> int:
    answer = 0
    num_list = []
    while(len(word) != 0):
        if word[0].isdigit():
            list_value = int(word[0])
            num_list.append(list_value)
            word = word[1:]
        else:
            word = word[1:]
    

    try:
        first_value = num_list[0]
        num_list = num_list[1:]

        for i in range(len(num_list)):
            first_value = first_value - num_list[0]
            num_list = num_list[1:]
        
        print(first_value)
    except IndexError:
        print(' 0')


#------------------------------------------------------------------------------

def remove_odds(word : str) -> str:
    if len(word) == 0:
        return ''
    if (word[0].isdigit()):
        odd_check = int(word[0])
        if (odd_check % 2 != 0):
            return remove_odds(word[1:])
        else:
            return word[0] + remove_odds(word[1:])
    else:
        return word[0] + remove_odds(word[1:])


#------------------------------------------------------------------------------


if __name__ == "__main__":
    sum_evens(-2, 2) # --> 0
    sum_evens(4, 4) # --> 4
    sum_evens(2, 8) # --> 20
    sum_evens(-1, 5) # --> 6

    print()
    print()

    subtract_digits('Okay!')  # --> 0
    subtract_digits('12')  # --> -1
    subtract_digits('h2i 34')  # --> -5
    subtract_digits('a1a1a1a2a0a3')  # --> -6

    print()
    print()

    print(remove_odds('h2e3l4l5o')) # --> 'h2el4lo'
    print(remove_odds('123456789')) # --> '2468'
    print(remove_odds('University')) # --> 'University'