
def count_ch(s : str, ch : str) -> int:
    if not s:
        return 0
    
    '''
    if (s[0] == ch):
        return 1 + count_ch(s[1:], ch)
    else:
        return count_ch(s[1:], ch)
    '''

    #Compact if else statement 

    return (1 + count_ch(s[1:], ch) if (s[0] == ch) else count_ch(s[1:], ch))


#Tail Recursion
#1 - We need a helper method that has an extra parameter 
#2 - We pass the result to the extra parameter during each iteration 
def count_ch2(s : str, ch : str) -> int:
    return count_ch2_helper(s, ch, 0)

def count_ch2_helper(s : str, ch : str, count : int = 0) -> int:
    if not s:
        return count
    

    if (s[0] == ch):
        #Instead of doing this:
        #Return 1 + count2_ch(s,ch)
        return count_ch2_helper(s[1:], ch, count + 1)
    else:
        return count_ch2_helper(s[1:], ch, count)


def factorial(num : int) -> int:
    if (num == 1):
        return 1
    

    return num * factorial(num - 1)

#Tail Recurison

def factorial2(num : int) -> int:
    return factorial2_helper(num, 1)

def factorial2_helper(num : int, result : int = 1) -> int:
    if (num == 1):
        return result
    
    return factorial2_helper(num - 1, num * result)


if __name__ == "__main__":
    print(count_ch('Hello', 'l'))
    print(count_ch2('Hellolll', 'l'))
    print(factorial(4))
    print(factorial2(4))