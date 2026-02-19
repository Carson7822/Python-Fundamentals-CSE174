'''
Write a function called count_list() that takes a list of Strings and a String as the two
parameters and returns an int. This function will count the number of occurrences of the
second String parameter that appears in the list of Strings and return the result as an int
'''

'''
def count_list(strings: list[str], target: str) -> int:
    """
    Counts the number of occurrences of the target string in the list of strings.

    Parameters:
    strings (list[str]): A list of strings to search through.
    target (str): The string to count occurrences of.

    Returns:
    int: The number of times the target string appears in the list.
    """
    return strings.count(target)

strings = ["apple", "banana", "apple", "orange", "apple"]
target = "apple"
result = count_list(strings, target)
print(result)  # Output: 3
'''

####################################################


'''
Write a function called contains_product(). This function should take in a list of int values
and an int product value. This function should return a True/False value of whether the
given list contains at least two numbers which, when multiplied together, results in the
given product value
'''

'''
def contains_product(nums: list[int], product: int) -> bool:
    """
    Checks if the list contains at least two numbers whose product equals the given value.

    Parameters:
    nums (list[int]): A list of integer values.
    product (int): The target product value.

    Returns:
    bool: True if there are at least two numbers whose product equals the target value, False otherwise.
    """
    # Use a set to keep track of potential divisors
    seen = set()

    for num in nums:
        if num == 0:
            # Special case: Check if product is 0 and there are at least two zeros
            if product == 0 and 0 in seen:
                return True
            seen.add(0)
        else:
            # Check if the current number's complement (product / num) exists in the set
            if product % num == 0 and (product // num) in seen:
                return True
            seen.add(num)

    return False

nums = [2, 4, 1, 6, 5]
product = 8
print(contains_product(nums, product))  # Output: True (2 * 4 = 8)


nums = [3, 7, 9]
product = 20
print(contains_product(nums, product))  # Output: False

nums = [0, 0, 5]
product = 0
print(contains_product(nums, product))  # Output: True
'''




################################################################

'''
Write a function called sum_list(). This function should take in a list of float values as the
only parameter and return an int. This function should return the sum of each element of
this list. Note, this problem must be solved recursively. You may create helper functions
to solve this problem
'''

'''
def sum_list(values: list[float]) -> int:
    """
    Recursively calculates the sum of a list of float values and returns it as an integer.

    Parameters:
    values (list[float]): A list of float values.

    Returns:
    int: The sum of the elements in the list, converted to an integer.
    """
    # Base case: If the list is empty, the sum is 0
    if not values:
        return 0
    
    # Recursive step: Add the first element to the sum of the rest of the list
    return int(values[0] + sum_list(values[1:]))


values = [1.2, 2.8, 3.4]
result = sum_list(values)
print(result)  # Output: 7 (since 1.2 + 2.8 + 3.4 = 7.4, which is cast to 7)
'''

##########################################################################
'''
Write a function called is_palindrome(). This function should take in a String as the only
parameter and return a Boolean. This function should return True if the given String is a
palindrome (the same characters forward and backwards) or False, otherwise. Note, this
problem must be solved recursively. You may create helper functions to solve this
problem
'''




'''
def is_palindrome(s: str) -> bool:
    """
    Recursively checks if a given string is a palindrome.

    Parameters:
    s (str): The string to check.

    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    # Base case: A string with 0 or 1 characters is a palindrome
    if len(s) <= 1:
        return True
    
    # Recursive case: Check if the first and last characters are the same
    if s[0] != s[-1]:
        return False
    
    # Recur on the substring excluding the first and last characters
    return is_palindrome(s[1:-1])



print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))    # Output: False
print(is_palindrome("a"))        # Output: True
print(is_palindrome(""))         # Output: True
'''



###############################################
'''
Write a function named sum_evens() that takes a 2-dimensional list of ints and 
returns the total number of even values in the list.
'''


'''
def sum_evens(matrix: list[list[int]]) -> int:
    """
    Counts the total number of even values in a 2-dimensional list.

    Parameters:
    matrix (list[list[int]]): A 2-dimensional list of integers.

    Returns:
    int: The total number of even values in the list.
    """
    count = 0
    for row in matrix:
        for value in row:
            if value % 2 == 0:
                count += 1
    return count


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
result = sum_evens(matrix)
print(result)  # Output: 4 (even numbers: 2, 4, 6, 8)
'''

##########################################################
'''
Write a function named data_match() that takes as its parameters 2 lists of 
ints, and returns True if the two collections contain exactly the same values 
in the same order, and False otherwise. Your solution should not create any 
additional lists and should not modify the given lists.
'''



'''
def data_match(list1: list[int], list2: list[int]) -> bool:
    """
    Checks if two lists contain exactly the same values in the same order.

    Parameters:
    list1 (list[int]): The first list of integers.
    list2 (list[int]): The second list of integers.

    Returns:
    bool: True if the lists are identical, False otherwise.
    """
    # Check if the lists are of the same length
    if len(list1) != len(list2):
        return False

    # Compare each element at the same index in both lists
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False

    return True


list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [1, 2, 4]

print(data_match(list1, list2))  # Output: True
print(data_match(list1, list3))  # Output: False
print(data_match(list1, [1, 2]))  # Output: False
'''


###########################################################
'''
Write a function (including the header) named count_cat() that takes as its 
only parameter a list of Strings, where one or more of the Strings is the
word "cat". The function will recursively count the occurrences of the word 
"cat" from within the list. Note, you must solve this problem recursively 
for credit. You are allowed to make helper functions.
'''



def count_cat(words: list[str]) -> int:
    """
    Recursively counts the occurrences of the word "cat" in a list of strings.

    Parameters:
    words (list[str]): A list of strings to check for occurrences of "cat".

    Returns:
    int: The number of times "cat" appears in the list.
    """
    # Base case: If the list is empty, return 0
    if not words:
        return 0

    # Recursive case: Check the first element
    if words[0] == "cat":
        return 1 + count_cat(words[1:])  # If "cat", add 1 and recurse on the rest
    else:
        return count_cat(words[1:])  # Otherwise, just recurse on the rest


words1 = ["dog", "cat", "fish", "cat", "bird"]
words2 = ["dog", "fish", "bird"]
words3 = ["cat", "cat", "cat"]

print(count_cat(words1))  # Output: 2
print(count_cat(words2))  # Output: 0
print(count_cat(words3))  # Output: 3
'''

########################################################

'''
Write a function named order_ends() (including the header) that takes a list 
of floats as its only parameter and returns the list it received. This 
function checks if the first element is larger than the last element and if it 
is, swaps those two elements in the list. Otherwise, the function makes no
changes to the list. Your solution should not create any additional lists.
'''

'''
def order_ends(nums: list[float]) -> list[float]:
    """
    Checks if the first element is larger than the last element in the list.
    If true, swaps the first and last elements. Otherwise, makes no changes.

    Parameters:
    nums (list[float]): A list of float values.

    Returns:
    list[float]: The modified list (or the original list if no change was made).
    """
    # Check if the list has at least two elements and the first is larger than the last
    if len(nums) > 1 and nums[0] > nums[-1]:
        # Swap the first and last elements
        nums[0], nums[-1] = nums[-1], nums[0]
    
    return nums




nums1 = [5.5, 2.3, 4.4]
nums2 = [2.1, 3.2, 4.5]
nums3 = [3.0, 1.2]

print(order_ends(nums1))  # Output: [4.4, 2.3, 5.5]
print(order_ends(nums2))  # Output: [2.1, 3.2, 4.5] (no change)
print(order_ends(nums3))  # Output: [1.2, 3.0] (swap)
'''


