'''
Name:Carson Gooch
Date:Sept 23 2024
Class:CSE 174 

This program asks for the user to enter a color that is either yellow red or
blue if the user does not enter this it prompts the user to try again and
has a variable that counts the amount of times it takes the user to enter
the correct color
'''



def main():
    #First part of program
    print('Please choose a color between, Blue, Red, or Yellow:', end = '')
    color = str(input())
    color = color.lower()
    color_count = 1

    while(color != 'red' and color != 'blue' and color != 'yellow'):
        print('Incorrect Color! Please try again:', end = '')
        color = str(input())
        color_count = color_count + 1

    print('That is the correct color!')
    print('You typed the correct color in %d tries!' % (color_count))


    #2nd part of program
    print('How many patients do you want to add to output.txt file?', end = ' ')
    patient_count = int(input())
    file = open('output.txt', 'w')
    for i in range(patient_count):
        print('Enter the patient\'s first name:', end = ' ')
        name = input()
        print('Enter the patient\'s last name:', end = ' ')
        last_name = input()
        print('Enter the patient\'s age:', end = ' ')
        age = int(input())
        print('Enter the patient\'s BMI:', end = ' ')
        bmi = int(input())
        print('Enter the patient\'s current temperature:', end = ' ')
        temp = int(input())
        file.write(name + '\n')
        file.write(last_name + '\n')
        file.write(str(age) + '\n')
        file.write(str(bmi) + '\n')
        file.write(str(temp) + '\n')
        file.write('--------------\n')
    file.close()


    print('How many numbers of Fibonacci: ', end  = '')

    sequence = int(input())

    first = 0
    second = 1

    for i in range(sequence):
        print(str(first) + ' ', end = '')
        next = first + second
        first = second
        second = next



if __name__ == "__main__":
    main()