"""
Project #1 - CSE 174
Section:F
Author: Carson Gooch
""" 

'''
                    GENERAL PROGRAM OVERVIEW:
This program first asks the user for an input file. Then that input file

is put into a loop that runs for each line in the file. Then a nested loop runs

and takes each element of the file and trys to convert it into an integer.

If that conversion is sucsessful, the code then checks to see if the count is 

equal to one. If it is, then that value that was converted into an integer and

is saved into the variable value. If the count is not equal to one then the

number is saved into var valueone. If the try does not work at the start, then

the code will move to the except block. The code will then convert and save

the line of text in the file as a string and save it into the var mathcheck

after all of this is done. An if function is run to see if the count is equal

to two. This is done because this line of code under the if function should

only run once every time the code loops three times. 

This is because after three loops all the variables are account for. 

Count is only equal to two because the block of code that adds to count only 

runs twice out of the three loops.



I also took the function that was provided and modififed it a bit to work for 
this method which is why you don't see that function here.


Part 2:
This program works the same way however, there are some new if statements that
take in account for the <+, <*, etc. operators. There are also some try and
except blocks in these if statements to determine if there is a divison by zero
error. 

I have tried to introduce a line count var to try and figure out a way to
combine the long strings of numbers together and perform the operation on them
however, I have been unable to, and sent Meisam an email regarding that. 
'''

def run():
    #Sets up all starting vars
    mathcheck = ''
    count = 0
    value = 0
    valueone = 0
    answer = 0
    linecount = 0

    #Asks the user for a file input
    print('Enter input file name: ', end = '')
    #Opens the file and reads it
    filename = input() 
    fileopen = open(filename, 'r')
    #Runs a loop for each line in the file
    for line in fileopen:
        line = line.strip().split()
        linelength = len(line)
        if(linelength == 3 or 2):
            #Runs the nested loop for each element in the file
            if(linelength <= 3):
                for ele in line:
                    #Checks to see if the characters can be converted into a string
                    try:
                        int(ele)
                        ele = int(ele)
                        count += 1
                        if(linelength == 2):
                            count = 2
                            valueone = ele
                            value = 0
                        #Count determines where the text is saved and in what var
                        if(count == 1):
                            value = ele
                        else:
                            valueone = ele

                    #This block of code is ran only if the text could not be converted
                    #into an integer. This block of code saves the math operator
                    except ValueError:
                        #Converts ele into a string
                        ele = str(ele)
                        #Saves the string into a var
                        mathcheck = ele
                    #This only runs if count is equal to two because if it is equal to
                    #two then all values were accounted for
                    if(count == 2):
                        #Resets the count var for the next line in the file
                        count = 0

                        #All of these if and elif conditions check to see what math
                        #operator to use in the calculations and then performs the
                        #calculation
                        if(mathcheck == '+'):
                            answer = value + valueone

                        elif(mathcheck == '-'):
                            answer = value - valueone

                        elif(mathcheck == '*'):
                            answer = value * valueone
                        elif(mathcheck == '/'):
                            try:
                                answer = value / valueone
                            except ZeroDivisionError:
                                linecount += 1 
                                print('Result of line %d: Error: / by zero' % (linecount))

                        elif(mathcheck ==  '<+'):
                            if(linelength == 2):
                                answer = answer + valueone
                            else:
                                answer = answer + valueone + value

                        elif(mathcheck == '<-'):
                            if(linelength == 2):
                                answer = answer - valueone
                            else:
                                answer = value - valueone

                        elif(mathcheck == '<*'):
                            if(linelength == 2):
                                answer = answer * valueone
                            else:
                                answer = answer * valueone * value

                        elif(mathcheck == '</'):
                            if(linelength == 2):
                                try:
                                    answer = answer /valueone 
                                except ZeroDivisionError:
                                    linecount += 1 
                                    print('Result of line %d: Error: / by zero' % (linecount))   
                            else:
                                try:
                                    answer = answer / value / valueone
                                except ZeroDivisionError:
                                    linecount += 1 
                                    print('Result of line %d: Error: / by zero' % (linecount))
                        else:
                            try:
                                answer = value / valueone
                            except ZeroDivisionError:
                                linecount += 1 
                                print('Result of line %d: Error: / by zero' % (linecount))
                        #Linecount gets added one and keeps track of what line we are 
                        #on in the file
                        linecount += 1

                        #Finally, prints the full result and goes back through the loop
                        print('Result of Line %d: %d' % (linecount, answer))
if __name__=="__main__":
    run()

