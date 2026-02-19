

def year_check() -> None:
    '''
    This loop asks the user for how many college credit hours they have
    completed. If it is less than 30 then they are a freshmen, if it is more than
    30 they are a sophmore, more than 64 is junior, more than 96 is senior. 

    Args:
        None
    Returns:
        None

    '''
    loop = 0
    while(loop != 1):
        print('Enter how many credit hours you have completed: ', end = '')
        try:
            credits = int(input())
            result = 'Freshmen'

            if(credits >= 96):
                result = 'Senior'
            elif(credits >= 64):
                result = 'Junior'
            elif(credits >= 30):
                result = 'Sophmore'
            print('With %d credit hours completed, you have %s standing' % (credits, result))
            loop += 1
        except ValueError:
            print('Error, you did not enter a integer!')


def division_table() -> None:
    '''
    This program uses nested loops and formatted prints to print out a divison
    table from numbers 1 through 6.

    Args:
        None
    Returns:
        None
    '''
    length = 6
    print('Divison Table:')
    print('%6s' % (''), end = ' ')
    for col in range(1, length + 1):
        print('%6d' % col, end = '')
    print()

    for row in range(1, length + 1):
        print('%6d' % row, end ='')
        
        for col in range(1, length + 1):
            print('%6.0f' % (row // col), end = '')
        print()




if __name__ == "__main__":
    year_check()
    division_table()
