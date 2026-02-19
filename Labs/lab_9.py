
"""
x= 2
n = 3

2 ^ 3
2 * power(2, 2)
    2 * power (2, 1)
        2 * power(2, 0)
            0 <- 1

"""
def power(x: int, n: int) -> int:
    """
    This function takes a base and a exponet and uses recursion to loop through
    the function and subtracts n over and over until it is equal to one.
    Then the function loops back through the code and prints out the final
    answer

    Args:
        (x) The base the user enters
        (n) The exponet the user enters
    Returns:
        The result of the exponet 
    """
    if n == 0:
        return 1
        
    else:
        return x * power(x, n - 1)

    

def sum_digits(n: int) -> int:
    """
    This function takes a number the user enters and strips through the it.
    Each time the number is stripped through it returns the digit and adds the
    digits together. It then strips the number

    Args:
        (n) The number the user entered
    Returns:
        (digit) The result of all the numbers added together 
    """
    
    if n == 0:
        return 0
    
    digit = n % 10 # 4567

    return digit  + sum_digits(n // 10)

    

def num_vowels(word: str) -> int:
    """
    Go through all of the characters in a string and counts how many vowels
    are in that string. Which are 'a e i o u and y'
    
    Args:
        (word) the string the user enters to be checked
    returns: 
        The amount of vowels that are in the string
    """
    if len(word) == 0:
        return 0

    if word[0].lower() in 'aeiouy':
        return 1 + num_vowels(word[1:])
    else:
        return + num_vowels(word[1:])
def print_backwards(word: str) -> None:
    """
    This function goes through a string and prints it backwards.

    Args:
        (word) The string the user enters
    Returns:
        None
    """

    if len(word) == 0:
        return
    else:
        print(word[-1], end = '')
        print_backwards(word[:-1])


def max_digit(n: int) -> int:

    """
    Goes through a number the user entered and grabs one number in the string
    and then strips that number. The max function is ran on this to determine
    what number is the largest value

    Args:
        (n) The number the user enters
    Returns:
        The final max digit 
    """
    if n < 10:
        return n
    return max(n % 10, max_digit(n // 10))





def menu() -> None:
    """
    Prints the menu

    Args:
         None
    Returns:
        None
    """

    print('Enter a choice for one of the following problems: ')
    print('1. Power')
    print('2. Sum digits')
    print('3. Count vowels')
    print('4. Print backwards')
    print('5. Max digit of an integer')
    print('6. Exit the program')

def main() -> None:
    """
    Handles the menu and inputs and running proper functions

    Args:
        None
    Returns:
        None
    """

    choice = -1
    while(choice != 6):
        menu()
        choice = int(input())

        match(choice):
            case 1:
                print('Enter the base: ', end = '')
                base = int(input())
                print('Enter the power: ', end = '')
                pow = int(input())
                print('The result of taking the power of %d of base %d is %d.' \
                      % (pow, base, power(base, pow)))
            case 2:
                print('Enter the integer to sum the digits of: ', end = '')
                num = int(input())
                print('The result of summing the digits of the integer %d is %d.' \
                      % (num, sum_digits(num)))
            case 3:
                print('Enter the String of characters you want ' \
                      + 'to count the vowels of: ', end = '')
                word = input()
                print('The number of vowels in the String %s is %d.' \
                      % (word, num_vowels(word)))
            case 4:
                print('Enter the String of characters you ' \
                      + 'want to print backwards: ', end = '')
                word = input()
                print('The String %s printed backwards is: ' % (word), end = '')
                print_backwards(word)
                print('')
            case 5:
                print('Enter a positive integer to find the max digit of: ', end ='')
                num = int(input())
                print('The max digit of the integer %d is %d.' % (num, max_digit(num)))
            case 6: 
                print('End!')
            case _:
                print('Invalid choice!')
        print('')

if __name__=="__main__":
    main()