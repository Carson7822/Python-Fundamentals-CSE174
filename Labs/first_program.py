#Name:Carson Gooch
#CSE 174, Section C or something idk 
#Date:8/30/2024
#Description: Practicing with writing, saving
#           and compiling code. Play a game of 
#           Guess my number with the user


import random
def welcome(name):
    print('Welcome, ' + name + '.')
    print('This is my first CSE 174 programming assignement')
    print("Let's play " + '"Guess My Number".')

def game_rules(name):
    print('Are you ready to play a game, ' + name + '?')
    print('I will think of a number between 1 and 100.')
    print('Try to guess it in 7 or fewer tries.')



def draw_border(length):
    for i in range(length):
        print('*', end = '')
    print('')
    
def main():
    #Get user's first and last name
    print('What is your first and last name?')
    first = input()
    last = input()

    #Display border and greeting
    draw_border(50)
    welcome(first + ' ' + last)
    draw_border(50)

    #Explain the rules
    game_rules(first)

    #Start the game with a random number
    correct_number = random.randint(1,100)
    guess_count = 0

    #Get first guess
    guess_count += 1
    print('Enter guess #' + str(guess_count) + ': ', end = '')
    guess = int(input())

    #Loop until the guess is correct

    cheat = ("Cheat")
    while(guess != correct_number):
        #High or Lower?
        if(guess < correct_number):
            print('Guess Higher')
        elif(guess == 782):
            print("Thats my lucky number! ")
        elif(guess == 4200):
            print("Oh no! Thats my unlucky number :(")
        elif(guess > 5000):
            print("What are you doing that number is way over 100!")
        else:
            print('Guess lower')
    
        #Get next guess
        guess_count += 1
        print('Enter guess #' + str(guess_count) + ': ', end = '')
        guess = int(input())

    #By the time we get here, the user has guessed the correct number.
    #Print the results

    print('Congratulations, ' + first + '.')
    print('You got it in ' +str(guess_count) + ' guesses.')

    if(guess_count <= 7):
        print('You are an excellent guesser. :)')
    

    else:
        print('Try harder next time. :(')
    

    
    #Display some art
    print('')
    print('And now, some stars to make you happy!')

    triangle_size = 7
    for length in range(0, triangle_size, 1):
        draw_border(length)
    
    print('Goodbye!')

        
# Using the "special" variable __name__

if __name__ =="__main__":
    main()