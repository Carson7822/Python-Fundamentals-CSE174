
"""
Author:Carson Gooch
Date:October 27th, 2024
Class:CSE 174 
Section:F


This program consists of many different functions that solve various things
involving strings, numbers, floats, etc. 
"""

def not_descending(a: int, b: int, c: int) -> bool:
    """
    This function determines if a set of numbers is descending and returns
    either true or false depending on if it is or not

    Args:
        (a, b, c) all numbers that are inputted and used for the function

    Returns:
        True or False



    """
    if(a > b and b > c):
        return True
    else:
        return False

def check_nums(n: int, start: int, end: int, check: bool) -> bool:
    """
    This function checks if a number is in between 2 different numbers. If it
    is it will return True, if not False

    Args:
        (n) the number that is being checked for being inbetween 2 different
        numbers
        (start) The first number that dictates what the value n has to be
        inbetween
        (end) The last number that dictates what the value n has to be 
        inbetween
    Returns:
        True or False
    """
    if(start <= n and end >= n):
        return True
    else:
        return False

def get_substring(inp: str, start: int, end: int, check: bool) -> str:
    """
    This function takes a string and 2 numbers and returns only what the 2
    numbers cut out of the string 

    Args:
        (inp) the string of the function that is being cropped out
        (start) the first number that is used to determine how many values are 
        being cropped
        (end) The second number that determines how many values are being 
        cropped from the string 
    """
    if check:
        return inp[start:end]
    else:
        return inp
        




def switch_xo(inp: str) -> str:
    """
    This function takes a string of X's and O's and takes the X's and swaps 
    them with the O's

    Args:
        (inp) the string with the X's and O's
    Returns:
        (new_string) The swapped string 
    """
    if not inp:
        return ''

    new_string = ''
    count = len(inp)

    while(count != 0):
        if inp[0] == 'O':
            new_string += 'X'
            inp = inp[1:]
        else:
            new_string += 'O'
            inp = inp[1:]
        count -= 1
    return new_string

def next_div7(num: int) -> int:
    """
    This function determines if a number can be divisble by 7. If it can't be
    divisble then it will increase the number until the function finds a number
    that is divisble by 7. 

    Args:
        (num) the number that is entered into the function
    Returns:
        The number that is divisble by 7
    """
    if (num % 7 == 0):
        return num
    else:
        return next_div7(num + 1)


def change_odd_chars(inp: str, odd: bool) -> str:
    """
    This function takes a string and changes each even letter in the string to
    a uppercase letter.

    Args:
        (inp) the string that is entered into the function
        (odd) the variable that determines if it should change odd letters or 
        not
    Returns:
        The new string that is upper case and lower case 
    """
    if len(inp) == 0:
        return ''
    if len(inp) == 1:
        return inp[0].lower()
    
    first_char = inp[0].lower()


    if odd and len(inp) > 1:
        return first_char[0] + inp[1].upper() + change_odd_chars(inp[2:], odd)
    else:
        return first_char + change_odd_chars(inp[1:], odd)


def what_missing(inp: str) -> str:
    """
    This function takes a string and prints out the first letter of the 
    alphabet that the string skips over 
    Args:
        (inp) the string that is plugged into the function 
    Returns:
        The letter of the alphabet that the string is missing
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    input_s = ''.join(sorted(inp.lower()))

    for i in range(len(input_s) - 1):
        if ord(input_s[i]) + 1 != ord(input_s[i + 1]):
            return chr(ord(input_s[i]) + 1)
    return ''


def get_similars(s1: str, s2: str, s3: str) -> str:
    """
    This function takes 3 different strings and returns the characters that are
    the same in each string.

    Args:
        (s1, s2, s3) 3 different strings that are plugged into the function
    Returns:
        The character that is inside of each string 
    """
    if len(s1) == 0:
        return ''

    if(s1 == s2 and s1 == s3):
        return s1
    loop_count = len(s1)

    for i in range(loop_count):
        if(s1[0] == s2[0] and s3[0]):
            return s1[0]
        get_similars(s1[1:])




def add_digits(inp: str) -> int:
    """
    This function takes a string, tests each character to determine if it is a
    digit. If it is it is added the overall value and returned
    
    Args:
        (str) The string that is plugged into the function
    Returns:
        The final number of all the numbers added up from inside the string
    """
    if not inp:
        return 0
    try:
        digit = int(inp[0])
        return digit + add_digits(inp[1:])
    except ValueError:
        return add_digits(inp[1:])


def add_divisibles(num: int) -> int:
    """
    This function takes a number, finds all of the other numbers that it can be
    divided by, and adds all of those numbers up for a final value

    Args:
        (num) the number that is entered into the function
    Returns:
        (final_answer) all of the numbers added up
    """
    if num <= 1:
        return 0
    final_answer = 0

    for num_check in range(1, num):
        if num % num_check == 0 and num_check % 2 == 0:
            final_answer += num_check
    return final_answer


def fix_sentence(inp: str) -> str:
    """
    This function takes a sentence and makes the first character in every word
    uppercase.

    Args:
        (inp) The string that is plugged into the function.
    Returns:
        (fixed_sent) The scentence with each word having an uppercase letter
    """
    fixed_sent = inp[0].upper()

    for i in range(1, len(inp)):
        if inp[i - 1] == ' ':
            fixed_sent += inp[i].upper()
        else:
            fixed_sent += inp[i]

    return fixed_sent

def switch_signs(inp: str) -> str:
    """
    This function takes a string of numbers and switches the sign on that
    number. So negative -> positive positive -> negative

    Args:
        (inp) the string that is plugged into the function.
    Returns:
        (switched_signs) The string with the signs of each number switched. 
    """
    if not inp:
        return ''
    
    number = inp.split()

    switched_signs = [str(-int(num)) for num in number]

    return ' '.join(switched_signs)



def double_hi(inp: str) -> bool:
    """
    This function takes a string and determines if the word 'hi' is in the
    string. If it is True is returned

    Args:
        (inp) The string that is plugged into the function
    Returns:
        True or False
    """
    if len(inp) < 2:
        return False
    if inp[0].lower() == 'h' and 'i':
        return True
    else:
        return double_hi(inp[1:])


def put_together(inp: str) -> str:
    """
    This function takes a string of letters and numbers and puts them all
    of the same letters and numbers together.

    Args:
        (inp) The string that is plugged into the function
    Returns:
        (new_string) The new string with all of the letters and numbers
        together
    """
    new_string = ''
    string_check = inp

    if not inp:
        return ''
    
    
    loop_length = len(inp)

    for i in range(loop_length):
        if string_check[0] == '1':
            new_string += string_check[0]
        string_check = string_check[1:]

    string_check = inp
    for i in range(loop_length):
        if string_check[0] == 'a':
            new_string += string_check[0]
        string_check = string_check[1:]
    
    string_check = inp
    for i in range(loop_length):
        if string_check[0] == 'c':
            new_string += string_check[0]
        string_check = string_check[1:]

    string_check = inp
    for i in range(loop_length):
        if string_check[0] == 'w':
            new_string += string_check[0]
        string_check = string_check[1:]

    string_check = inp
    for i in range(loop_length):
        if string_check[0] == '2':
            new_string += string_check[0]
        string_check = string_check[1:]

    string_check = inp
    for i in range(loop_length):
        if string_check[0] == 'g':
            new_string += string_check[0]
        string_check = string_check[1:]

    string_check = inp
    for i in range(loop_length):
        if string_check[0] == 'd':
            new_string += string_check[0]
        string_check = string_check[1:]

    string_check = inp
    for i in range(loop_length):
        if string_check[0] == 'm':
            new_string += string_check[0]
        string_check = string_check[1:]

    return new_string
def get_sec_max(inp: str) -> float:
    """
    This function takes a string of numbers and determines the second highest
    number in that string.

    Args:
        (inp) The string that is plugged into the function
    Returns:
        (sort_num) The second highest number in the string 
    """

    if not inp:
        return 0.0
    numb = inp.split()

    diff_num = set(float(num) for num in numb)

    sort_num = sorted(diff_num, reverse=True)

    if len(sort_num) < 2:
        return 0.0
    
    return sort_num[1]
    



def main():
    print('***Testing not_descending***')
    print('False == ' + str(not_descending(1, 2, 3)))
    print('True == ' + str(not_descending(3, 2, 1)))
    print('True == ' + str(not_descending(-2, -3, -4)))
    print('')

    print('***Testing check_nums***')
    print('True == ' + str(check_nums(2, 1, 10, True)))
    print('False == ' + str(check_nums(0, 1, 10, True)))
    print('True == ' + str(check_nums(10, 9, 10, True)))
    print('')

    print('***Testing get_substring***')
    print('a == ' + str(get_substring('abc', 0, 1, True)))
    print('000111222 == ' + str(get_substring('000111222', 0, 3, False)))
    print('Hell == ' + str(get_substring('Hello', 0, 4, True)))
    print('')

    print('***Testing switch_xo***')
    print('O == ' + str(switch_xo('X')))
    print(' == ' + str(switch_xo('')))
    print('XO == ' + str(switch_xo('OX')))
    print('')

    print('***Testing next_div7***')
    print('7 == ' + str(next_div7(1)))
    print('14 == ' + str(next_div7(8)))
    print('14 == ' + str(next_div7(9)))
    print('')

    print('***Testing change_odd_chars***')
    print('aB == ' + str(change_odd_chars('ab', True)))
    print('aAaAa == ' + str(change_odd_chars('aaaaa', True)))
    print('aBcSdE == ' + str(change_odd_chars('ABcsde', True)))
    print('')

    print('***Testing what_missing***')
    print('b == ' + str(what_missing('ac')))
    print(' == ' + str(what_missing('ab')))
    print('f == ' + str(what_missing('abcdeg')))
    print('')

    print('***Testing get_similars***')
    print('ab == ' + str(get_similars('ab', 'ab', 'ab')))
    print('a == ' + str(get_similars('ab', 'ac', 'ad')))
    print('a == ' + str(get_similars('a', 'ab', 'abc')))
    print('')

    print('***Testing add_digits***')
    print('0 == ' + str(add_digits('')))
    print('0 == ' + str(add_digits('a0')))
    print('3 == ' + str(add_digits('1fr2')))
    print('')

    print('***Testing add_divisibles***')
    print('12 == ' + str(add_divisibles(12)))
    print('0 == ' + str(add_divisibles(1)))
    print('0 == ' + str(add_divisibles(5)))
    print('')

    print('***Testing fix_sentence***')
    print('Hi == ' + str(fix_sentence('hi')))
    print('Good Morning == ' + str(fix_sentence('Good morning')))
    print('Nice Job! == ' + str(fix_sentence('nice job!')))
    print('')

    print('***Testing switch_signs***')
    print(' == ' + str(switch_signs('')))
    print('-1 == ' + str(switch_signs('1')))
    print('2 -3 == ' + str(switch_signs('-2 3')))
    print('')

    print('***Testing double_hi***')
    print('True == ' + str(double_hi('HiHi')))
    print('False == ' + str(double_hi('')))
    print('True == ' + str(double_hi('Hkji3Hi')))
    print('')

    print('***Testing put_together***')
    print(' == ' + str(put_together('')))
    print('aacd == ' + str(put_together('acda')))
    print('11ww222gddm == ' + str(put_together('1w2g1dw2md2')))
    print('')

    print('***Testing get_sec_max***')
    print('1.2 == ' + str(get_sec_max('2 1.2')))
    print('4.1 == ' + str(get_sec_max('1.3 4.1 5')))
    print('0.0 == ' + str(get_sec_max('')))

if __name__=="__main__":
    main()