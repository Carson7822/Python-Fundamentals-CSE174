'''
Author:Carson Gooch
Class:CSE 174
Section:F
Date:November 4th, 2024

This program establishes a 2d list with 3 rows and 5 colums, and fills that
list with random values. Then three functions will determine the mean of all
the numbers in the list, the max number in the list, and the smallest number
in the list.
'''



def max(lst: list) -> int:
    '''
    This function determines the max value of the 2D list.

    Args:
        (lst) The list that is plugged in to find the max value of
    
    Returns:
        (int) The max value of the list
    '''

    max_value = -sys.maxsize

    for row in range(len(lst)):
        for col in range(len(lst[row])):
            if (lst[row][col]) > max_value:
                max_value = lst[row][col]
    return max_value

def min(lst: list) -> int:
    '''
    This function determines the min value of the 2D list.

    Args:
        (lst) The list that is plugged in to find the min value of
    
    Returns:
        (int) The min value of the list
    '''

    min_value = -sys.maxsize
    count = 0

    for row in range(len(lst)):
        for col in range(len(lst[row])):
            if count == 0:
                if (lst[row][col]) > min_value:
                    min_value = lst[row][col]
                    count += 1
            else:
                if (lst[row][col]) < min_value:
                    min_value = lst[row][col]

    return min_value



def mean(lst: list) -> int:
    '''
    This function determines the mean of the 2D list.

    Args:
        (lst) The list that is plugged in to find the mean of
    
    Returns:
        (int) The mean of the list
    '''

    total = 0
    divider = 0

    for row in range(len(lst)):
        for col in range(len(lst[row])):
            total += lst[row][col]
            divider += 1
        
    average = total / divider
    return average 


def display(lst: list) -> None:
    '''
    This function takes a list, and fills that list with random numbers between
    1 and 100 and rounds those numbers by the second decimal place. Then the 
    list is printed. 
    
    Args:
        (lst) The list that is randomized and printed.
    
    Returns:
        None
    '''
    for row in range(len(lst)):
        for col in range(len(lst[row])):
            lst[row][col] = round(random.random() * 100, 2)
    print(lst[0])
    print(lst[1])
    print(lst[2])
    print()


if __name__ == "__main__":
    import random
    import sys
    nums = [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]

    display(nums)

    max(nums)
    print('The max value of the 2D list is: %.2f.' % (max(nums)))

    min(nums)
    print('The min value of the 2D list is: %.2f.' % (min(nums)))

    mean(nums)
    print('The mean of values in the the 2D list is: %.2f.' % (mean(nums)))