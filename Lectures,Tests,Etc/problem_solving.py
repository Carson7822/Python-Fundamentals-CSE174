'''
Author:Carson Gooch
Class:CSE 174
Section:F
Date:November 13th 2024
'''




'''
#1
Given an list of numbers, return true if the number of 1's is greater than the number of 4's

more14([1, 4, 1]) → true
more14([1, 4, 1, 4]) → false
more14([1, 1]) → true
'''
def more14(numbers : list) -> list:
    count4 = 0

    count1 = 0

    for i in range(len(numbers)):
        if numbers[i] == 4:
            count4 += 1
        else:
            count1 += 1
    
    if count1 > count4:
        return True
    else:
        return False

                 
            


'''
#2
Given an list of numbers, return true if the value 3 appears in the list exactly 3 times, 
and no 3's are next to each other.

haveThree([3, 1, 3, 1, 3]) → true
haveThree([3, 1, 3, 3]) → false
haveThree([3, 4, 3, 3, 4]) → false
'''
def haveThree(numbers : list) -> list:
    count3 = 0

    for i in range(len(numbers)):
        if numbers[i] == 3:
            count3 += 1
            if (i > 0 and numbers[i - 1] == 3):
                return False
    if count3 == 3:
        return True
    else:
        return False


'''
#3
Return a list that contains the exact same numbers as the given list, but rearranged so that 
all the even numbers come before all the odd numbers. 
Other than that, the numbers can be in any order. 
You may modify and return the given list, or make a new list.


evenOdd([1, 0, 1, 0, 0, 1, 1]) → [0, 0, 0, 1, 1, 1, 1]
evenOdd([3, 3, 2]) → [2, 3, 3]
evenOdd([2, 2, 2]) → [2, 2, 2]
'''
def evenOdd(numbers : list) -> list:
    lst = []
    lst2 = []

    for i in range(len(numbers)):
        if (numbers[i] % 2 == 0):
            lst.append(numbers[i])
        else:
            lst2.append(numbers[i])
    return lst + lst2


'''
#4
Given a non-empty list of numbers, return a new list containing the elements from the original array 
that come before the first 4 in the original list. 
The original list will contain at least one 4. 


pre4([1, 2, 4, 1]) → [1, 2]
pre4([3, 1, 4]) → [3, 1]
pre4([1, 4, 4]) → [1]
'''
def pre4(numbers : list) -> list:
    lst = []

    for i in range(len(numbers)):
        if numbers[i] == 4:
            return lst
        else:
            lst.append(numbers[i])
 
    return numbers  # Temporary return


'''
#5

For each multiple of 10 in the given list, change all the values following it to be that multiple of 10, 
until encountering another multiple of 10. So [2, 10, 3, 4, 20, 5] yields [2, 10, 10, 10, 20, 20].


tenRun([2, 10, 3, 4, 20, 5]) → [2, 10, 10, 10, 20, 20]
tenRun([10, 1, 20, 2]) → [10, 10, 20, 20]
tenRun([10, 1, 9, 20]) → [10, 10, 10, 20]
'''
def tenRun(numbers : list) -> list:
    count = 0

    for i in range(len(numbers)):
        if (numbers[i] % 10 == 0):
            count += 1
            if numbers[i] == 10:
                replacevar = 10
            else:
                replacevar = 20
        
        if (count > 0):
            numbers[i] = replacevar

    return numbers  # Temporary return



if __name__ == "__main__":
    # Sample calls for each function
    print(more14([1, 4, 1]))  # Expected: True
    print(more14([1, 4, 1, 4]))  # Expected: False
    print(more14([1, 1]))  # Expected: True

    print()
    
    print(haveThree([3, 1, 3, 1, 3]))  # Expected: True
    print(haveThree([3, 1, 3, 3]))  # Expected: False
    print(haveThree([3, 4, 3, 3, 4]))  # Expected: False

    print()
    
    print(evenOdd([1, 0, 1, 0, 0, 1, 1]))  # Expected: [0, 0, 0, 1, 1, 1, 1]
    print(evenOdd([3, 3, 2]))  # Expected: [2, 3, 3]
    print(evenOdd([2, 2, 2]))  # Expected: [2, 2, 2]

    print()
    
    print(pre4([1, 2, 4, 1]))  # Expected: [1, 2]
    print(pre4([3, 1, 4]))  # Expected: [3, 1]
    print(pre4([1, 4, 4]))  # Expected: [1]

    print()
    
    print(tenRun([2, 10, 3, 4, 20, 5]))  # Expected: [2, 10, 10, 10, 20, 20]
    print(tenRun([10, 1, 20, 2]))  # Expected: [10, 10, 20, 20]
    print(tenRun([10, 1, 9, 20]))  # Expected: [10, 10, 10, 20]
