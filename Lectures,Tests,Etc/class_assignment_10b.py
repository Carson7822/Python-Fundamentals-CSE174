'''
Author:Carson Gooch
Date:October 30th, 2024
Class:CSE 174
Section F

This program goes over the basics of lists and how to use them.
'''


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lst1 = []

lst2 = ['I am a String', 22, True, 97.5]
def display(lst : list):
    #Prints lst
    for i in range(len(lst)):
        print(lst[i])

    #Prints lst1
    count = 0
    for i in range(len(lst2)):
        print(lst2[count])
        count += 1


def sum_even_lengths(lst3 : list) -> int:
    def helper(index):
        if index == len(lst3):
            return 0
        length = len(lst3[index])
        if length % 2 == 0:
            return length + helper(index + 1)
        else:
            return helper(index + 1)
    
    return helper(0)



if __name__ == "__main__":
    display(lst)
    lst3 = ['Hello', 'Hi', 'CSE 174!']

    print('Enter the first index to update between 0 and 9: ', end = '')
    index = int(input())

    #First index

    print('Enter the value to change index %d to:' % (index), end = ' ')
    changed_val = int(input())

    lst[index] = changed_val


    print('Enter the second index to update between 0 and 9: ', end = '')
    index1 = int(input())

    #Second index

    print('Enter the value to change index %d to:' % (index1), end = ' ')
    changed_val1 = int(input())

    lst[index1] = changed_val

    #Third index

    print('Enter the third index to update between 0 and 9: ', end = '')
    index2 = int(input())

    print('Enter the value to change index %d to:' % (index2), end = ' ')
    changed_val2 = int(input())

    #Print statement for all

    lst[index2] = changed_val
    print('Indicies %d, %d, and %d have been change with the values of %d, %d,'
        ' and %d, respectectivly.' % 
            (index, index1, index2, changed_val, changed_val1, changed_val2))


    #Even or Odd
    print('Enter a index value to see if the index is even or odd:', end = ' ')
    even_or_odd = int(input())

    if lst[even_or_odd] % 2:
        print('The value %d at at index %d is odd.' % (even_or_odd, lst[even_or_odd]))
    else:
        print('The value %d at at index %d is even' % (even_or_odd, lst[even_or_odd]))
    

    #Range of index printed

    print('Enter two values between zero and nine to form a range to'
          ' display values in the list:')
    

    range1 = int(input())
    range2 = int(input())

    print(lst[range1:range2])
    print()
    print('With the list:')
    print(lst3)
    print('The sum of the even lengths of all Strings in the list is %d.' % (sum_even_lengths(lst3)))
