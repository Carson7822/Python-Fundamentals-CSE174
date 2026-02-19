def thing():
    print('Enter a number ', end = '')
    val = int(input())

    if (val == 0):
        print('The input is zero')
    elif(val < 0):
        print('The input is negative')
    else:
        print('The input is positive')
        





if __name__ == "__main__":
    thing()
