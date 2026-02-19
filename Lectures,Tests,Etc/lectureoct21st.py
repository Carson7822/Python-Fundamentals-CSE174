def my_print() -> None:
    """
    This function demestrates formatted prints

    Args:
        None
    Returns:
        None
    """
    """
    |   1  2   3   4   5
    1   1   2   3   4   5
    2   2   4   6   8   10
    3   3   6   9   12  15
    4   4   8   12  16  20
    5   5   10  15  20  25
    """

    for i in range(1, 5):
        print('%6s' % (' '), end = '')

    for i in range(1, 6):
        print('%6s' % (str(i)), end = "")
    print()
    
    for row in range(1,6):
        print('%6s' % str(row), end = '')

        for col in range(1,6):
            print('%6s' % str((row == col)), end = '')
        
        

if __name__ == "__main__":
    #(90-100 print A)
    #(80-90 Print B)
    # (Anything below 70 print Q) 

    repeat = True
    while(repeat == True):
        print('Enter a grade between [0-100]:', end = ' ')
        try:
            grade = int(input())
            result = 'Q'
            if(grade >= 90):
                result = 'A'
            elif(grade >= 80):
                result = 'B'
            elif (grade >= 70):
                result = 'C'
            print(result)
            repeat = False
        except ValueError:
            print('Error input is not a number!')
        
    my_print()
