#Sept18th Lecture while loops and stuff and things

import random
if __name__ == "__main__":
    numr = 1
    numr = int(random.random() * 100) + 1
    numguess = 0
    print(numr)
    count = 0
    int(numguess)
    while (numguess != numr):
        print('Guess what number I am thinking of:', end = '')
        numguess = int(input())
        count = count + 1
        if (numguess != numr):
            if(numguess > numr):
                print('Guess smaller!')
            else:
                print('Guess higher!')
    if count == 1:
        print('You correctly guessed the number in ' + str(count) + ' try!')
    else:
        print('You correctly guessed the number in ' + str(count) + ' trys!')

    print('Now enter a series of words, one at a time, to count them. Enter \"Done\" to finish:', end = ' ')
    countw = 0
    word = ''
    checkword = 'Done'
    while (word.lower() != 'done'):
        word = input()
        countw = countw + 1
        if(word.lower() != 'done'):
            print('Enter another word:', end = ' ')
    if countw == 1:
        print('You entered ' + str(countw) + ' word!')
    else:
        print('You entered ' + str(countw) + ' words!')


    print('Genereate a number less than 10:', end = '')
    posnum = int(input())
    while(posnum != 20):
        posnum = posnum + 1
        print('%d, ' % (posnum))


    print('Please enter a 4 digit positive number:', end = '')
    fourdigit = int(input())
    for i in range(5):
        digit = fourdigit % 10
        print('%.0f' % (digit))
        fourdigit /= 10