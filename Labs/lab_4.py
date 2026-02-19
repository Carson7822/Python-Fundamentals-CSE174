import math
'''
Name:Carson Gooch
Date:9/20/23
Class:CSE 174 
Section:F

This program asks the user for a set of number (1-3) and depending on the 
number the user enters it will do a specific task for the user 
the 3 different tasks this program can do is:
calculate grades, find out if numbers are perfect squares, and performs 
summations.
'''



def main():
    #Asks the user for numbers 1-3
    print('Welcome to the problem solver!')
    print('Please choose one of the 3 available options and follow all given\
 prompts.')
    print('1. Determining a Student\'s Final Grade')
    print('2. Getting Candy for Math')
    print('3. Solving a Summation Problem')
    print('Enter a number [1-3]:', end = ' ')
    num = int(input())

    #This chunk of code is the grade calculator 
    if (num == 1):
        print('Enter the final grade value:', end = ' ')
        grade = float(input())
        if (grade >= 90):
            print('The final grade is an A.')
        elif (grade < 90 and grade >= 80):
            print('The final grade is an B.')
        elif (grade < 80 and grade >= 70):
            print('The final grade is an C.')
        elif (grade < 70 and grade >= 60):
            print('The final grade is an D.')
        else: 
            print('The final grade is an F.')
    
    #This chunk of code is the perfect square calculator
    if (num == 2):
        print('Enter the number to see if it\'s a perfect square:', end = ' ')
        square_num = float(input())
        square_num = math.sqrt(square_num)
        if (square_num.is_integer()):
            print('True')
        else:
            print('False')
    
    #This chunk of code does the summations.
    if (num == 3):
        print('Enter the summation starting point:', end = ' ')
        sum_start = int(input())
        print('Enter the summation ending point:', end = ' ')
        sum_end = int(input())
        #This is the starting number that will be addded to the sum_start value
        sum_add = sum_start + 1 
        #This will check the number of loops and end the while loop
        loop_check = sum_start
        #This var is the number loop check checks to determine if the loop 
        # can end
        loop_check1 = sum_end
        #Establishes a var that prints the final answer
        final_result = 0
        #This var subtracts 4 multiplied by the amount of loops done.
        #This is because the starting value messes up the summation
        #And this subtractor var corrects it
        subtract = sum_start
        #This is the var that multiples the subtract var
        #It is at -1 because if it was set to 0 the number would be 
        #multiplied one extra time
        amount_of_loops = -1
        while(loop_check != loop_check1):
            result = sum_start + sum_add
            final_result = final_result + result
            sum_add = sum_add + 1
            loop_check = loop_check + 1
            amount_of_loops = amount_of_loops + 1
        subtract = subtract * amount_of_loops
        final_result = final_result - subtract
        print('The result of the summation is: %d' % (final_result))

#Starts the program
if __name__ == "__main__":
    main()