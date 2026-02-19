'''
Author:Carson Gooch
Date:November 15th, 2024
Class:CSE 174
Section F
'''

def main():
    count = 0
    list = []
    fileopen = open('customer_list.txt', 'r')
    for line in fileopen:
        count += 1
        line = line.strip().split()

        list.append(line)
    '''
    print('[0]: %s' % (list[0]))
    print('[10]: %s' % (list[10]))
    print('[1500]: %s' % (list[1500]))
    print('[Last index:] %s' % (list[count - 1]))
    '''

    key = ['Delilah', '4350600189']
    index = linear_search(list, key)
    print('The customer %s is located at index: %d.' % 
                  (key, index))
    print()
    index = binary_search(list, key)
    print('The customer %s is located at index: %d.' % 
                  (key, index))
    
    print()
    
    key = ['Zola', '2074980639']
    index = linear_search(list, key)
    print('The customer %s is located at index: %d.' % 
                  (key, index))
    print()

    index = binary_search(list, key)
    print('The customer %s is located at index: %d.' % 
                  (key, index))
    print()

    key = ['Reinaldo', '9988586038']

    index = linear_search(list, key)
    print('The customer %s is located at index: %d.' % 
                  (key, index))
    print()

    index = binary_search(list, key)
    print('The customer %s is located at index: %d.' % 
                  (key, index))
    print()

    key = ['CSE174', '1111111111']

    index = linear_search(list, key)
    print('The customer %s is located at index: %d.' % 
                  (key, index))
    print()

    index = binary_search(list, key)
    print('The customer %s is located at index: %d.' % 
                  (key, index))



def linear_search(lst: list, key: list) -> int:
    num_compare = 0

    for i in range(len(lst)):
        num_compare += 1
        if (lst[i][0] == key[0] and lst[i][1] == key[1]):
            print('Linear Search: the key is found after %d comparisons.' 
                  % (num_compare))
            return i

    print('Linear Search: the key is found after %d comparisons.' 
                  % (num_compare))
    return -1



def binary_search(lst: list, key: list) -> int:
    low = 0
    high = len(lst) - 1
    num_compare = 0

    while(low <= high):
        mid = (low + high) // 2
        

        num_compare += 1 
        if (lst[mid][0] == key[0] and lst[mid][1] == key[1]):
            print('Binary Search: the key is found after %d comparisons.'
                    % (num_compare))

            return mid
        elif(key[1] < lst[mid][1]):
            high = mid - 1
        else:
            low = mid + 1
            
    print('Binary Search: the key is found after %d comparisons.'
        % (num_compare))
    return -1
        


if __name__ == "__main__":
    main()
