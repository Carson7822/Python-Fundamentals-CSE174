def main():
    validate = 'y'
    while(validate != 'n'):
        try:
            print('Enter an integer:', end = ' ')
            integer = int(input())


            print('you entered a valid input of %d.' % integer)
        except ValueError:
            print('Error, you tried to enter something'
                + ' besides an integer!')
        
        print('Would you like to validate another number '
            + '(y/n):', end = ' ')
        validate = input().lower()
    


    print('\nEnter an age between 18 and 99:', end = ' ')
    age = int(input())

    if (age < 18 or age > 99):
        raise ValueError('Error... Age must be between 18 and 99\n')
    print('\nEnter a grade between [0.0-100.0]:', end = ' ')
    grade = float(input())


    if (grade < 0 or grade > 100):
        raise ValueError('Error invalid grade value. Must be between 0.0 and '
                         + '100.0')
    





    



if __name__ == "__main__":
    main()
