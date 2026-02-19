

def get_user_input():
    while True:
        print('Enter an integer to calculate the factorial of:', end = ' ')
        num = input()
        number = extract_int(num)
        if number is not None:
            result = factorial(number)
            print('The factorial is: %d' % (result))
            break

def factorial(number):
    result = 1
    for i in range(2, number + 1):
        result *= i
    return result



def extract_int(number):
    try:
        return int(number)
    except ValueError:
        print("Error, you entered a non-integer input!")






if __name__ == "__main__":
    get_user_input()
