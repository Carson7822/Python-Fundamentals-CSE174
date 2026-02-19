
#Function 1
def neg_index(list1: list) -> str:
    index = ''
    index2 = ''
    index_check = 0
    for row in range(len(list1)):
        for col in range(len(list1[row])):
            if list1[row][col] < 0:
                if index_check == 0:
                    num1 = str(row)
                    num2 = str(col)
                    index = '(' + num1 +', ' + num2 + '),'
                    index_check += 1
                else:
                    num1 = str(row)
                    num2 = str(col)
                    index2 = ' (' + num1 +', ' + num2 + '),'
    index += index2
    return index


#Function 2 
def add_lists(list1: list, list2: list) -> list:
    count = 0
    sum_list = []
    for i in range(len(list1)):
        new_index = list1[count] + list2[count]
        sum_list.append(new_index)
        count += 1
    return sum_list


#Function 3

def rev_elements(list1: list) -> list:
    if not list1:
        return ''
    new_string = ''
    for i in range(len(list1)):
        new_string += list1[-1] + ' '
        list1 = list1[:-1]
    return new_string



    
#Function 4

def remove_negatives(nums: list) -> list:
    '''
    This function removes all of the negative numbers from a list by checking
    if a number is negative at a certain index by using a comparison operator.
    If the number is negative it is then excluded from the new list that gets
    returned.

    Args:
        (nums) The list that is inputted
    Returns:
        (new_list) The list that has all negative numbers excluded  
    '''
    new_list = []
    remover = -1
    count = 0
    remover_count = 0
    for i in range(len(nums)):
        if nums[count] < 0:
            new_list += nums[remover:count]
            count += 1
            remover += 1
            remover_count += 1
        else:
            count += 1
            remover += 1
    if remover_count == 0:
        return nums
    return new_list





if __name__ == "__main__":
    
    print('FUNCTION 4')
    nums = [4.0, -8.9, 7.2, -1.0]
    print(remove_negatives(nums))
    nums = []
    print(remove_negatives(nums))
    nums = [65.7]
    print(remove_negatives(nums))
    print('')

    
    print('FUNCTION 2')
    list1 = [4,1,9]
    list2 = [0,-1,1]
    print(add_lists(list1, list2))
    list1 = [-2,1,2,5,3]
    list2 = [2,2,2,2,99]
    print(add_lists(list1, list2))
    print('')

    print('FUNCTION 1')
    list1 = [[-99]]
    print(neg_index(list1))
    list1 = [[2,7], [1], [9,4,8]]
    print(neg_index(list1))
    list1 = [[], [-1,3], [5,4,0,-4]]
    print(neg_index(list1))
    list1 = [[]]
    print(neg_index(list1))
    print('')

    print('FUNCTION 3')
    list1 = ['house', 'cat', 'tree', 'house']
    print(rev_elements(list1))
    list1 = ['dog', 'mouse', 'cat']
    print(rev_elements(list1))

