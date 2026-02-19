'''
Tail Recursive Example:
Write a recursive function named add_odd_digits() which takes an int as the only
parameter and does not return anything. This function will recursively sum the odd digits
from x (the starting value of the parameter) to 0. Furthermore, you should make this a tail
recursive function.
'''

def add_odd_digits(val: int) -> int:
    return add_odd_digits_helper(val, 0)

def add_odd_digits_helper(val: int, result: int) -> int:
    if(val == 0):
        return result
    
    if(((val % 10) % 2) == 1):
        return add_odd_digits_helper(val // 10, result + (val % 10))
    else:
        return add_odd_digits_helper(val // 10, result)
    
'''
String manupulation Example:
Write a function called reverse_zero() which accepts a String as a parameter. This function
returns a String that is the input String, but in reverse order with the 0th index missing. So,
if the input String was “Hello World”, then the result of the function would be “dlroW
olle”
'''
def reverse_zero(word: str) -> str:
    result = ''

    for i in range(len(word) - 1, 0, -1):
        result += word[i]

    return result



'''
String Problem:
When given two Strings
entered by the same user. If the length of String1 is the same as the length of String2 and
if they both start with the same letter, then print the sum of the two string’s lengths. If they
start with the same letter but have different lengths, print the result of subtracting String1’s
length by String2's length. In all other cases, print Error.
'''

def functionthing():
    print('Enter in string 1:', end = '')
    str1 = str(input())

    print('Enter in String 2:', end = '')
    str2 = str(input())

    if (len(str1) == len(str2) and str1[0] == str2[0]):
        print(len(str1) + len(str2))
    elif(str1[0] == str2[0]):
        print(len(str1)- len(str2))
    else:
        print('Error')



'''
Simple Prob
For this problem, write an entire program that will ask for use input for an int. If the user
enters anything that is not an int, i.e., a String, float, etc., then deal with the corresponding
ValueError, and loop to continue asking the user for input until an int is entered. Once it is
entered, print out to the console “The number entered is x.” where “x” is the number the
user entered
'''


def functionthing2():
    is_correct = True
    
    while(is_correct):
        try:
            print('Please enter an int: ', end = '')
            val = int(input())
            is_correct = False
        except ValueError:
            print('Error, you did not enter an int!')
        
    print('The number entered is %d.' % (val))
    

'''
Remove Vowels
Write a recursive function called remove_vowels() which accepts a non-empty 
string and returns a string with all vowels removed from the given string. 
For example: if the given string is 'Beautiful day', the result should be 
'Btfl dy', removing all vowels from the input.
'''

def remove_vowels(word : str ) -> str:
    if len(word) == 0:
        return ''
    if word[0].lower() == 'a' or word[0].lower() == 'u' \
        or word[0].lower() == 'e' or word[0].lower() == 'i' \
            or word[0].lower() == 'o':
        return remove_vowels(word[1:])
    else:
        return word[0] + remove_vowels(word[1:])


'''
Extract Chars
Write a recursive function called extract_chars() which accepts a non-empty 
String and returns a string with only characters in it. This function extracts 
the characters (not digits) inside the given String and returns them all 
as a string.
'''

def extract_chars(word: str) -> str:
    if len(word) == 0:
        return ''
    
    elif word[0].isdigit():
        return extract_chars(word[1:])
    
    else:
        return word[0] + extract_chars(word[1:])

def find_gcd(num1: int, num2: int) -> int:
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1

#Least Common Multiple
def find_lcm(num1: int, num2: int) -> int:
    gcd = find_gcd(num1, num2)
    return abs(num1 * num2) // gcd
    

if __name__ == "__main__":
    #Tail Recursion
    #print(add_odd_digits(125110))
    
    #String cutting 
    #print(reverse_zero('Hello World'))

    #String Problem
    #functionthing()

    #Simple Prob
    #functionthing2()

    #Remove Vowels
    #result = remove_vowels('PENISAeiosu')
    #print(result)

    #Extracting Chars 
    #print(extract_chars('a1a1a1a1a12'))

    print(find_lcm(5, 3))