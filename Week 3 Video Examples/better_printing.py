#Week 3 videos yay

import math

def standard_printing():
    print('Something')
    print('Your total is: ', end = '')
    print('782$')

def escape_characters():
    print('Hello\nWorld')
    print('Hello\tWorld')
    print('\\')

def formmated_printing():
    side_one = 3.2
    side_two = 4.2
    hypot = math.sqrt(side_one + side_one + side_two + side_two)
    #The .2f rounds that number off at the second decimal place. 
    print('With sides %.1f and %.3f, the hypotenuse is %.2f.' % (side_one, side_two, hypot))

    name = 'Carson'
    age = 18
    salary = 0

    print('My name is %s, I am %d years old, and I make $%.1f, dollars a year'\
          % (name, age, salary))
    print('My name is %s, I am %d years old, and I make $%15.1f, dollars a year'\
          % (name, age, salary))
    

if __name__ == '__main__':
    standard_printing()
    escape_characters()
    formmated_printing()


