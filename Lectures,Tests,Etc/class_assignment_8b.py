'''
Carson Gooch
CSE 174 
Section F

This program does a number of things. This program mainly demenstrates 
chained functions. This program has 2 parts:
The first part takes 3 different functions and these functions calculate the 
radius for different shapes such as a circle, rectangle, and triangle. 
The functions mainly work by setting up a parameter variable that is then used
in the calculation for that shape and is returned in the function.
Then the main function prints out the result of that function.
The first time these functions are printed is when the functions are using
their set variable. The second time it is printed is when one or more variables
are changed in the parameter. 

The second part of this program sets up 2 functions one being withdraw and the
other being deposit. These functions simulate a bank account that has money
being deposited and withdrawn. These functions only have one parameter variable
and that is the number that is being withdrawn or deposited. A global variable
named checking is used to keep track of how much money is in the bank. 
'''
import math
#Global Var
checking = 0.0




def circle_area(radius = 1.75) -> float:
    '''
    This function calculates the area of a circle using set parameter values
    and returns it so that it can be printed

    Args:
        (radius): the number that is multipled in the formula

    Returns:
        The sum of the formula 
    '''
    return (radius ** 2) * math.pi

def rectangle_area(num1=2.22, num2=2.22) -> float:
    '''
    This function calculates the area of a rectangle

    Args:
        (num1): The length of the rectangle, is multipled with the other number
        (num2):The width of the rectangle, is multipled with the other number

    Returns:
        The sum of num1 multipled by num2
    '''
    return num1 * num2

def triangle_area(num3 = 5, num4 = 5) -> float:
    '''
    This function calculates the area of a triangle.

    Args:
        (num3): The number that is multiplied by other number
        (num4): The number that is multiplied by other number 

    Returns:
        The sum of the formula
    
    '''
    return 1/2 * num3 * num4
    

def deposit(number) -> None:
    '''
    This function takes a number and adds it to the checking variable. Then
    it checks if the checking variable is below 0 and prints out a statement
    if it is below zero.

    Args:
        (number): Number that is added to checking
    
    Returns:
        Nothing

    '''
    global checking
    checking += number
    print('Checking balance after depositing $%.2f: $%.2f' % (number, checking))
    if (checking < 0):
        print('You still have a negative balance after your deposit!')

    

def withdraw(num) -> None:
    '''
    This function takes a number and subtracts it from the global checking 
    variable. It then checks if checking is below zero and prints out a 
    statement if it is.

    Args:
        (num):The number that is subtracted from the global checking variable.
    
    Returns:
        Nothing 

    '''
    global checking
    checking -= num
    print('Checking balance after withdrawing $%.2f: $%.2f.' % (num, checking))
    if (checking < 0):
        print('You have a negative balance after your withdraw!')
    


def main():
    '''
    This function is what puts all of these other functions together. This 
    function is used to print out the results of all of the other functions
    and sets the argument variables to different numbers if needed.

    Args:
        None
    
    Returns:
        Nothing

    '''
    print('The area of a circle given the radius 22.5 = %.2f.' \
          % (circle_area(22.5)))
    
    print('The area of a rectanlge given the length' \
           ' and width of 15.5 and 17.7 = %.2f.' % (rectangle_area(15.5, 17.7)))
    
    print('The area of a triangle given the base and height of 5 and 6 '\
          '= %.2f.' % (triangle_area(5, 6)))
    
    print('The cirlce\'s area with no arugment is %.2f.' % (circle_area()))

    print('The rectangle\'s area using positional arguments is %.2f.' % (rectangle_area(13.37)))

    print('The triangle\'s area using keyword arguments is %.2f.' % (triangle_area(21, 17)))


    print('')

    deposit(300)
    withdraw(3000)
    deposit(3001)
    withdraw(30)
    withdraw(40)
    deposit(100)
    withdraw(100000)
    deposit(1)
    

if __name__ == "__main__":
    main()
