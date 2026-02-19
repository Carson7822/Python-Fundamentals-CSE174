

'''
Carson Gooch, CSE 174
This program collects information from the user to calculate the bmi of the
user and then asks the user to read information from another file and then
calculates the bmi from the information of that file and then asks the user
to write a filename were all of this information is stored 
'''



def get_input():
    #This block of code collects inputs from the user
    print('Enter your first and last name:', end = ' ')
    first_last = input()
    print('Enter your age:', end = ' ')
    age = input()
    print('Enter your weight(lb):', end = ' ')
    weight = float(input())
    print('Enter your height(feet):', end = ' ')
    height = float(input())
    height = height * 12
    height = height * height

    #This block of code calculates the BMI
    bmi = weight / height
    bmi = bmi * 703

    #This block of code prints the table and displays the results
    print(' --------------------------------------')
    print('|%-20s|%-8s|%-8s|' % ('Name', 'Age', 'BMI'))
    print('|......................................|')
    print('|%-20s|%-8s|%-8.1f|' % (first_last, age, bmi))
    print(' --------------------------------------')

    #This block of code gets a file from the user and reads it
    print('Enter an input filename:', end = ' ')
    filename = input()
    input_file = open(filename, 'r')

    #This block of code collects info from the file
    name_file = input_file.readline().strip()
    age_file = int(input_file.readline())
    weight_file = float(input_file.readline())
    height_file = float(input_file.readline())

    #Closes the file
    input_file.close()

    #Does the calculations for bmi with the new information
    height_file = height_file * 12
    height_file = height_file * height_file 
    bmi_file = weight_file / height_file
    bmi_file = bmi_file * 703


    #This block of code prints the same table but with the new values
    print(' --------------------------------------')
    print('|%-20s|%-8s|%-8s|' % ('Name', 'Age', 'BMI'))
    print('|......................................|')
    print('|%-20s|%-8s|%-8.1f|' % (name_file, age_file, bmi_file))
    print(' --------------------------------------')

    #This block of code asks the user to name a file to store all of the info
    #and then combines both of the tables and prints it to the new file
    print('Enter an output filename:', end = ' ')
    file_out = input()
    out = open(file_out, 'w')
    out.write(' --------------------------------------\n')
    out.write('|%-20s|%-8s|%-8s|\n' % ('Name', 'Age', 'BMI'))
    out.write('|......................................|\n')
    out.write('|%-20s|%-8s|%-8.1f|\n' % (first_last, age, bmi))
    out.write('|......................................|\n')
    out.write('|%-20s|%-8s|%-8.1f|\n' % (name_file, age_file, bmi_file))
    out.write(' --------------------------------------\n')

#Runs the program
if __name__ == "__main__":
    get_input()

