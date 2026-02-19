'''
Author:Carson Gooch
Date:November 1st 2024
Class:CSE 174
Section:F

This program reads a file, extracts that file in the form of a list, and then 
the program uses count variable and cut variables to cut certain parts ot the
list out to print the total profit, the average, and the amount for each profit
order.
'''



def get_total_profit(total_list: list) -> None:
    '''
    This function calculates the total profit
    Args:
        (total_list) This variable is the cut list that is in the function
        get_order_profits
    Returns:
        None

    '''
    loop_check = len(total_list)
    sum = 0
    count = 0
    for i in range(loop_check):
        total = total_list[count]
        sum += total
        count += 1
    print('The total profit is %.2f.' % (sum))


def get_average_profits(average_list : list) -> float:
    '''
    This function calculates the average profit
    Args:
        (average_list) This variable is the cut list that is in the function
        get_order_profits
    Returns:
        None
    '''
    divider = len(average_list)
    count = 0
    average = 0
    for i in range(divider):
        sum1 = average_list[count]
        count += 1
        average += sum1
    total = average
    average /= divider
    print('The average profit is %.2f.' % average)



def get_order_profits(list_lines: list)-> list:
    '''
    This function takes the entire list and cuts it into a smaller list
    only compiled of the profits
    Args:
        (list_lines) The list obtained in the read_file function
    Retrns:
        (list) This returns a list filled with all of the profits

    '''
    lst_profits = []
    for line in list_lines:
        # ["123", "pen", "10", "23.3"]

        amount = int(line[2])
        price = float(line[3])
        profit = amount * price
        lst_profits.append(profit)
   
    return lst_profits

def read_file(file: list ) -> list:
    '''
    This function reads the orginal file and makes one huge list of that file.
    Args:
        (file) This is the file name the user enters
    Retrns:
        (list) The big list compiled of everything

    '''
    lst = []
    
    try:
        fileopen = open(filename, 'r')
        for line in fileopen:
            line = line.strip().split()
            # ["123", "pen", "10", "23.3"]

            lst.append(line)

    except FileNotFoundError:
        print('Error, File not Found')

    return lst

def display(list_profits: list) -> None:
    '''
    This function prints out each order profit, and calls the other functions
    to print the average and total.
    Args:
        (list_profits) This is the list compiled with just the profits
    Retrns:
        None
    '''
    count = 1
    cut = 0
    loop_count = len(list_profits)

    for i in range(loop_count):
        print('Order #%d profit is $%.2f.' % (count, list_profits[cut]))
        count += 1
        cut += 1

    get_average_profits(list_profits)
    get_total_profit(list_profits)



if __name__ == "__main__":
    print('Enter a file name: ', end = '')
    filename = input()
    read_file(filename)
    list_lines = read_file(filename)
    list_profits = get_order_profits(list_lines)

    display(list_profits)
    