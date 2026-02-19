def run():
    print('hi')
    i = 3 * 4
    print(i)
    run()
    '''
    Recursion is a technique of repeating a code by calling a function itself.

    Everytime we make a recursion call, all the information about the new 
    call gets loaded up inside the stack memory and evenutally it gets full
    and our program crashes.
    
    This is a big disadvantage over using normal loop.
    '''

def nums(i : int) -> None:
    '''
    Rules of recursion:
    - We need to come up with a condition that stops all the recursion calls
    This condition is called the base case. The base case is a condition that 
    stops the recursion calls at some point

    2-We need to write this code in a way that it reaches the base case, so it
    can be stopped at some point
    '''

    if(i == 0):
        return

    print('%d\t' % i, end = '')
    nums(i - 1)
    print('Coming back to %d call' % i)

'''
Calculate the sum of all numbers from 0 to num

num = 5
5 + sum(4)
    4 + sum(3)
        3 + sum(2)
            2 + sum(1)
                1 + sum(0)
                    0
'''
def sum(num: int) -> int:
    if(num == 0):
        return 0
    return num + sum(num-1)



'''
Go through all characters of a string and count how many "a" we have inside
that string
"meisama"
check(m) -> count_a("eisama")
            check(e) -> count_a(isama)
                check(i) -> count_a(sama)
                    check(s) -> count_a(ama)
                        check(s) -> 1 + count_a(ma)
                            check(s) -> + count_a(ma)
                                check(s) -> 1 + count(a)
                                    return 0 

'''

def count_a(s : str) -> int:
    if (len(s) == 0):
        return 0
    #" M e i s a m"
    #  0 1 2 3 4 5
    
    #(s[1:]) just cuts that part of the string and removes it
    if (s[0] == 'a'):
        return 1 + count_a(s[1:])
    else:
        return - + count_a(s[1:])


def add_even_digits(num : int) -> int:
    if (num == 0):
        return 0
    digit = num % 10
    if (digit % 2 == 0):
        return digit +  add_even_digits(num // 10)
    else:
        return add_even_digits(num // 10) 


    




if __name__ == "__main__":
    #run()
    #nums(5)
    #sum(3)
    #print(count_a('meisama'))
    add_even_digits()

