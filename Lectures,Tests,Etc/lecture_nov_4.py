#It is my birthday today yay :)
import copy # for getting a deep copy
import random # for generating random values
import sys # to get max smallest or largest value in python

if __name__ == "__main__":
    num1 = 10
    num2 = num1 # num2 is a copy of num1
    print('The origin num: %d' % (num1))
    print('The copy num: %d' % (num2))
    print()
    
    num1 = 20
    print('The origin num: %d' % (num1))
    print('The copy num: %d' % (num2))
    print()

    list1  = [1,2,3,-4,-5]
    list_copy = list1

    print('The orgin of list: %s' % (list1))
    print('The copy num: %s' % (list_copy))
    print()

    list1[-2] = -900

    print('The orgin of list: %s' % (list1))
    print('The copy num: %s' % (list_copy))
    print()

#When we deal with normal values like numbers and string and boolean, the vars
#are holding the actual value directory

#However when the var is holding the list, it is actualy not holding the actual
#list for example list1 is not holding the actual list directly. Instead, it is
#holding the memory location of the list instead of the actual values. Which
#Means it is pointing to the list or it is refrencing the actual list.


#To prevent shallow copy and do the actualy copy or what is known as deep copy,
#We need to manually go through the first list, and get a copy of all elements,
#and then add to the second list

    list_copy = []

    #Manually copying list1 into list_copy
    for elem in list1:
        list_copy.append(elem)

    list1[0] = -900

    print('The orgin of list: %s' % (list1))
    print('The copy num: %s' % (list_copy))
    print()



    #Does same thing as manually copying it
    #list2 = copy.deepcopy(list1)
    

    list1 = []
    #Because list1 is holding the memory location
    #When we pass list1 to another function\method
    #The same memory location that list1 is holding, now is being passed
    #to the parameter of that method\function 
    #This means, both of them are pointing to the same list
    #Which means if we change the value of the list inside of that function
    #It actually effects the values of the origninal list1

    def fill_in_with_random(lst : list) -> None:
        for i in range(10):
            lst.append(random.randint(1, 100))

    print('--- looking at the list after adding values to it inside another'
          ' function ---')

    fill_in_with_random(list1)

    print(list1)



    #--- 2D list---
    '''
    [
    [1,2,3], 
    [4,5,6], 
    [7,8,9]
    ]

    Can have multiple elements and lengths in each list
    [
    [1,2,3, 3, 54, 'hello', 'hi'], 
    [4,5,6], 
    [7,8,9]
    ]

    [1, 1] --> 5

    9 Changes to 4444
    list[2,2] = 4444

    '''

    print()
    print()

    list2 = [[1,2,3],[4,5,6],[7,8,9]]

    #looping through 2d list 
    def display(lst : list) -> None:
        for row in range(len(lst)): # len(list2) tells us how many rows we have inside of the 2d array
            for col in range(len(list2[row])): #Tells us how many colums we have inside of the 2d array
                print(list2[row][col], end = '\t')


            print()
        
    display(list2)
    print()


    def get_max(lst: list) -> int:

        max = -sys.maxsize # This gives me the minimum possible int value that is in python

        for row in range(len(lst)):
            for col in range(len(lst[row])):
                if (lst[row][col]) > max:
                    max = lst[row][col]
        return max
    
    print('The max value in our 2D list is: %d' % (get_max(list2)))
