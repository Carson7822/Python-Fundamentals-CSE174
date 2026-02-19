
def run():
    print(0 == 0)
    print (0 > 1)
    print(0 < 1)
    x = 0
    print(x)
    print(x == 5)
    print (x != 9)
    print(x >= 0)
    print(0.1 + 0.1 +0.1)
    print(0.1+0.1+0.1 == 0.3)
    eps = 0.0000001
    print((0.1+0.1+0.1) - 0.3 < eps)
    print('0' == '0')
    word = ('hello')
    print(word == 'hello')
    fruit1 = 'apple'
    fruit2 = 'orange'
    print(fruit1 < fruit2)
    print('\n\n\n')
    #in order for this statement true both of these expressions must be true
    print(x < 10 and x > -5)
    print(x > 0 or x < 0)
    print(not not True)
    print(not True)
    print(3 > 0 or (3 / 0 < 10))
    



if __name__ == '__main__':
    run()
