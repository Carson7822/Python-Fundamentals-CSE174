'''
Author:Carson Gooch
Date:November 18th, 2024
Class:CSE 174
Section:F
'''



import random


def insertion_sort(nums: list) -> None:
    '''
    This function Takes a list and compares each value to determine where they
    need to be in order to make a sorted list. It does this by taking the first
    number, seeing if it is bigger than the second number of the list, and then
    moving that number inside the list accordingly. So basically the function
    takes a number, and compares it to see if it is bigger or smaller than the
    numbers previously compared, and places that number in the list 
    accordingly.

    (Args):
        nums:The list that is being sorted
    Returns:
        None
    '''
    print('Insertion Sort:')
    print(nums)
    if(len(nums) < 2):
        return
    for i in range(1, len(nums)):
        temp = nums[i]
        j = i
        while(j > 0 and nums[j - 1] > temp):
            nums[j] = nums[j - 1]
            j -= 1
        nums[j] = temp


def selection_sort(nums: list) -> None:
    '''
    This function uses the selection sort algorthm. This function grabs the 
    largest number in a list, and the smallest number in a list. Then the
    function will place the smallest function at the begining and the largest
    at the end. Then the function will grab the second largest and smallest 
    numbers and places those at the second part of the list and the second to
    last part of the list. The function does this over and over until the list
    is fully sorted. 
    Args:
        (nums):The list that is being sorted
    Returns:
        None
    '''
    print('Selection Sort:')
    print(nums)
    if(len(nums) < 2):
        return
    for i in range(0, len(nums) - 1):
        min = i
        for j in range(i + 1, len(nums)):
            if(nums[j] < nums[min]):
                min = j
        if(min != i):
            temp = nums[min]
            nums[min] = nums[i]
            nums[i] = temp


def bubble_sort(nums: list) -> None:
    '''
    This function uses the bubble sort algorthm. The way this works is that
    2 numbers in a list are compared to each other. If the first number is
    bigger than the second number, the first number and the second number 
    switch places. Then the function moves on to the next number and compares
    that number with the second number that was compared. It moves through the
    list and does this until the list is fully sorted.

    Args:
        (nums):The list that is being sorted
    Returns:
        None
    '''
    print('Bubble Sort:')
    print(nums)
    if(len(nums) < 2):
        return
    swap = True
    while(swap):
        swap = False
        for i in range(0, len(nums) - 1):
            if(nums[i] > nums[i + 1]):
                temp = nums[i]
                nums[i] = nums[i + 1]
                nums[i + 1] = temp
                swap = True




def display(input_list: list) -> None:
    for i in input_list:
        print(str(i) + ' ', end = '')

if __name__ == "__main__":
    nums = []
    for i in range(15):
        random_num = round(random.uniform(1, 100), 1)
        nums.append(random_num)
    print('')
    bubble_sort(nums)
    display(nums)

    nums = []
    for i in range(15):
        random_num = round(random.uniform(1, 100), 1)
        nums.append(random_num)

    print('')
    print('')


    selection_sort(nums)
    display(nums)

    nums = []
    for i in range(15):
        random_num = round(random.uniform(1, 100), 1)
        nums.append(random_num)

    print('')
    print('')

    insertion_sort(nums)
    display(nums)