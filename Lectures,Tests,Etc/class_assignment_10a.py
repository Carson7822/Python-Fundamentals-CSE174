'''
Author:Carson Gooch
Date:Oct 28th, 2024
Class:CSE 174
Section:F
'''



def multiply_greater4(num) -> int:
    def multiply_greater4_helper(num, count):
        if num == 0:
            return count
        else:
            digit = num % 10

            if digit > 4:
                return multiply_greater4_helper(num // 10, count * digit)
            else:
                return multiply_greater4_helper(num // 10, count)
    return multiply_greater4_helper(num, 1)


def remove_cse(s : str) -> str:
    def remove_cse_helper(s, result):
        if not s:
            return result
        elif s[:3] == 'cse':
            return remove_cse_helper(s[3:], result)
        else:
            return remove_cse_helper(s[1:], result + s[0])
    return remove_cse_helper(s, '')
        

            
        
    




if __name__ == "__main__":
    '''
    Recursion and Tail Recursion differ from each other in a variety of ways. 
    Generally tail recursion is seen as a more effiecent way of recursion. Normal
    recurison works by calling a function within its self over and over until a
    condition is met. Tail recursion works similar to this except that it handles
    the recursive call to make it the last call of the function, and allows you to 
    handle the recursive call directly. 

    The call stacks behave differently as well between normal and tail 
    recursion. The call stacks in normal recursion are saved as they are needed
    to return the final result, but in tail recursion, the call stacks are not
    saved because of the way the recursive call is handled. 
    '''
    print('Testing multiply_greater4()')
    print(multiply_greater4(337546192))
    print(multiply_greater4(36))
    print(multiply_greater4(44587))
    print('')
    print('Testing remove_cse()')
    print(remove_cse('hicsehello'))
    print(remove_cse('csecsecse'))
    print(remove_cse('i love cse 174'))