'''
Author:Carson Gooch
Date:November 11th, 2024
Class:CSE 174
Section F
'''


def linear_search(lst: list, key) -> int:
    '''
    This function takes a list and a key and determines if the key is in that
    list. This function searches for the key linearally. 

    Args:
        (lst) The list that the function is given
        (key) The variable that the function is trying to find in the list
    Returns:
        (int) Either -1 or the index value
    '''
    num_compare = -1

    for i in range(len(lst)):
        num_compare += 1

        if (lst[i] == key):
            print('Searching for %d in list with linear search, it is at '
                  'index %d.' % (key, num_compare))
            return i
    print('Searching for %d in list with linear search, it is at -1.' % (key))
    return -1


def binary_search(lst: list, key) -> int:
    '''
    This function takes a list and a key and determines if the key is in that
    list. This function searches for the key binarly. 

    Args:
        (lst) The list that the function is given
        (key) The variable that the function is trying to find in the list
    Returns:
        (int) Either -1 or the index value
    '''
    low = 0 
    high = len(lst) - 1 

    while(low <= high):
        mid = (low + high) // 2
        num_compare = 0
        
        num_compare += 1
        if (lst[mid] == key):
            print('Searching for %d in the list with binary search, it is at'
             ' index %d.' % (key, num_compare))

            return mid
        elif(key < lst[mid]):
            high = mid - 1
        else:
            low = mid + 1
    print('Searching for %d in the list with binary search, it is at'
    ' index -1.')                               
    return -1 



def linear_search_2d(lst: list, key) -> int:
    '''
    This function takes a list and a key and determines if the key is in that
    list. This function searches for the key linarly. The function is also 
    searching through a 2d list.

    Args:
        (lst) The list that the function is given
        (key) The variable that the function is trying to find in the list
    Returns:
        (int) Either -1 or the index value
    '''
    num_comparison = 0

    for row in range(len(lst)):
        for col in range(len(lst[row])):
            num_comparison += 1
            if (lst[row][col]) == key:
                print('Searching for %d in the 2d-list with linear search, it'
                       'is at index [%d] [%d].' % (key, row, col))
                return key
    
    print('Searching for %d in the 2d-list with linear search, it is at index'
          '[-1] [-1].' % (key))
    return -1






if __name__ == "__main__":
    lst1 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

    linear_search(lst1, 15)
    linear_search(lst1, 72)
    
    binary_search(lst1, 16)
    binary_search(lst1, 72)

    lst2 = [[1, 2, 6],[3, 4, 7, 8, 10],[100, 23]]

    linear_search_2d(lst2, 6)
    linear_search_2d(lst2, 20)