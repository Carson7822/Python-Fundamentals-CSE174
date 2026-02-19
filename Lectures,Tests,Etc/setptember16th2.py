if __name__ == "__main__":
    print('Enter the First number:', end = '')
    number1 = float(input())

    print('Enter the Second number', end = '')
    number2 = float(input())
    print('Select an operation: \n1. Addition\n2. Subtraction'
          + '\n3. Multiplication\n4. Divison')
    print('Enter either 1, 2, 3, 4 for your choice, ', end = '')
    choice = int(input())

    result = 0.0

    match(choice):
        case 1:
            result = number1 + number2
        case 2:
            result = number1 - number2
        case 3:
            result = number1 * number2
        case 4:
            result = number1 / number2
        case _:
            print('Error invalid choice')
    print('result %.2f' % result)
'''
    if choice == 1:
        result = number1 + number2
    elif choice == 2:
        result = number1 - number2
    elif choice == 3:
        result = number1 * number2
    elif choice == 4:
        result = number1 / number2
    else:
        print('Error invalid choice')
    print('result %.2f' % result)
'''