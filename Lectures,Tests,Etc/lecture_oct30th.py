

def sum2(lst : list) -> int:
    if len(lst) == 0:
        return 0 
    
    return lst[0] + sum2(lst[1: ])

def sum(lst : list) -> int:
    sum = 0 
    for elem in lst:
        sum += elem
    
    return sum

lst = ['hi', 'error', 'bye']

#Without recursion
def sum_len(lst : list):
    sum = 0
    for elem in lst:
        sum += len(elem)
    return sum


#Normal recurison
def sum_len2(lst : list):
    if (len(lst)) == 0:
        return 0
    else:
        return len(lst[0]) + sum_len2(lst[1:])

#Normal tail recursion

def sum_len3(lst : list) -> int:
        sum_len3_tail(lst, 0)

def sum_len3_tail(lst : list, sum : int) -> int:
    sum == len(lst[0])

    return sum_len3_tail(list[1:], sum)



def sum3(lst : list) -> int:
        
    def sum3_helper(lst : list, sum : int):
        if len(lst) == 0:
            return sum
        
        sum += lst[0]
        return sum3_helper(lst[1: ], sum)
    

# ---- tail recursion : Efficent way

def sum4(lst : list) -> int:

    
    return sum4_tail(lst, 0, 0)

def sum4_tail(lst : list, sum : int, index : int):
    if (index >= len(lst)):
        return sum4_tail(lst, 0, 0())

    sum == lst[index]

    return sum4_tail(lst, sum, index + 1)




if __name__ == "__main__":
    #Specifiy a list with brackets
    #Seperate values with a comma
    lst = [1, 2, 3, 4]
    print(lst)


    lst = ["hi, hello, bye"]
    print(lst)

    #We can have different type of values in the same list
    lst = [12, 24.3, 'Yes', True, 343, 'hi']
    print(lst)

    #Example list
    #   lst [12, 'test', 34.4, 'abc']
    #      0        1     2      3

    print(lst[2])
    # but when we don't know the length of the list or how many elements
    # we have inside the list
    print(len(lst))
    #print(lst[])
    #In python we can use a negative index

    print(lst[-1])
    print(lst[-2])

    lst = [34, 56, -10]
    #Looping through the list without using the index 
    print("[", end = '')
    for elem in lst:
        print(elem, end = ' ')
    print(']')

    #Looping through the list using index
    print('[', end = '')
    for i in range(len(lst)): #If the length if 3, range generates 0, 1, 2
        if i == len(lst) - 1:
            print(lst[i], end = ']\n')
        else:
            print(lst[i], end = ', ')





