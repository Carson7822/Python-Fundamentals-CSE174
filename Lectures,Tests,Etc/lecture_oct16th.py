#This program provides a set of examples for both chaining together
#function calls as well as catch errors thrown in other functions
#Also, it shows how to do a more formal program header comment

def get_user_input()-> str:
    print('Enter 2 numbers: ', end = '')
    return input()

def extract_number(number: str) -> int:
    return int(number)



def do_math() -> float:
    input = get_user_input().replace(' ', '')
    result = 1
    for item in input:
        result *= extract_number(item)
    return result


def print_output() -> None:
    print('The result of multiplying the 2 entered numbers is ' + str(do_math()))

def break_program(num: int) -> None:
    if(num > 0):
        raise RuntimeError('The number is greater than zero')
    else:
        print('The number is less than or equal to zero')
    

def main():
    print_output()
    try:
        break_program(5)
    except RuntimeError as e:
        print(e)





if __name__ == "__main__":
    main()