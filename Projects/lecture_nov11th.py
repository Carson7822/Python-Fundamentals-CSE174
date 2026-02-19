#Search Alg

def linear_search(nums: list, key) -> int:
    num_comparison = 0

    for i in range(len(nums)):

        num_comparison += 1
        if (nums[i] == key):
            print('The number of comparison in Linear search is: %d' % (num_comparison))

        if (nums[i] == key):
            return i 
        
    print('The number of comparison in Linear search is: %d' % (num_comparison))
    return -1 



#Binary Search 

def binary_search(nums: list, key) -> int:
    low = 0 # always starts with zero
    high = len(nums) - 1 #Always start with the index of the last element 

    num_comparison = 0
    while(low <= high):
        mid = (low + high) // 2
        
        num_comparison += 1
        if (nums[mid] == key):
            print('The number of comparison in Binary search is: %d' % (num_comparison))

            return mid
        elif(key < nums[mid]):
            high = mid - 1
        else:
            low = mid + 1
    print('The number of comparison in Binary search is: %d' % (num_comparison))                                  
    return -1 





if __name__ == "__main__":
    lst = [7, 7, 8, 10, 15, 26, 30, 47, 49]
    key = 7
    print('The result of linear search looking for %d is: %d ' % (key, linear_search(lst,key)))
    print('The result of linear search looking for %d is: %d ' % (key, binary_search(lst,key)))