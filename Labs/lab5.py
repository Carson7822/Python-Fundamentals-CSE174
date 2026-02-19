'''
Name:Carson Gooch
Date:Sept 27th, 2024
CSE 174
Section F

This program asks the user for an input and output file name
it then reads the data from the input file and converts the numbers
into grades and then calculates the class average and the number of students
in the class. All of this data is then printed to the output file and the class 
average and number of students is also printed to the terminal.

'''


def main():
    #Gathers inputs from the user
    print('Enter an input file name:', end = ' ')
    filein = input()
    print('Enter an output file name:', end = ' ')
    fileout = input()
    out = open(fileout, 'w')


    #opens the input file
    fileinput = open(filein, 'r')
    count = 0
    total = 0
    #For loop that goes through and reads each line
    for line in fileinput:
        line = line.strip().split()
        #Establishes the count var to count the number of students
        count += 1
        
        #Calculates the grades and what letter grade they should be
        for ele in line:
            if ele.isdigit():
                grade = int(ele)
                total = total + grade
                if (grade >= 90):
                    gpa = 'A'
                elif (grade >= 80):
                    gpa = 'B'
                   
                elif (grade > 69.5):
                    gpa = 'C'
                  
                elif (grade > 59.5):
                    gpa = 'D'
                  
                else:
                    gpa = 'F'
                #Writes out the letter grade into the output file and creates a
                #New line
                out.write(gpa)
                out.write('\n')             
    
    #Prints the num of students and class average to the file and terminal
    print('Number of students: %d' %(count))
    out.write('Number of students: %d \n' %(count))
    total = total / count
    print('Class average: %.2f' % total)
    out.write('Class average: %.2f' % total)

    #Closes the file
    fileinput.close()
    out.close()



        


    




if __name__ == "__main__":
    main()