'''
Carson Gooch
CSE 174
Section F
Date:October 23, 2024

'''
def sub_digits(n: int) -> int:
    '''
    This function 
    
    '''


    if(n == 0):
        return 0
    return (n % 10) - sub_digits(n // 10)


def add_div3_digits(num: int) -> int:
    '''
    This function takes a string of numbers and see's if they are able to be
    divided by 3 if they are it adds that number to the result.

    Args:
        num: The string of numbers that was plugged into the function

        returns: The result of numbers that are divisble by 3 added together
    '''
    if len(num) == 0:
        return 0
    
    first_digit = int(num[0])

    if first_digit % 3 == 0:
        return first_digit + add_div3_digits(num[1:])
    else:
        return add_div3_digits(num[1:])

def count_hi(s: str) -> int:
    '''
    This function counts the number of times hi is in a string

    Args:
        s: The string that is plugged into the function
    Returns:
        The amount of times hi is in the string 
    '''
    if len(s) == 0:
        return 0

    if (s[:2] == 'hi'):
        return 1 + count_hi(s[2:])
    else:
        return count_hi(s[1:])
    







if __name__ == "__main__":
    print('Testing sub_digits():')
    result = sub_digits(45224)
    print(result)
    print()
    '''
    The sub_digits() function works with recursion. The first thing the

    function does is establish a parameter variable named n. Then it checks

    if this variable is equal to zero. If it is then it will return zero. 

    If the varibale is not equal to zero it will see how many times 10 can go
    
    into the variable. Then it returns that result. It will then take this
    
    result and plug it back into this same line over and over until n == 0.

    Then it will return 0 and then it will run line 4 of the function 3 times

    making n back into its orginal value. and the output is equal to how many
    
    times line 4 of the function ran. 
    
    
    '''
    print('Testing add_div3_digits():')
    result = add_div3_digits(str(337546192))
    print(result)
    result = add_div3_digits(str(36))
    print(result)
    result = add_div3_digits(str(22587))
    print(result)
    print()


    print('testing count_hi():')
    result = count_hi('hi')
    print(result)
    result = count_hi('hello')
    print(result)
    result = count_hi('hihellohi')
    print(result)