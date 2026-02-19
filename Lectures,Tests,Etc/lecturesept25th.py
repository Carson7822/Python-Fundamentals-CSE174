def main():
    print('Enter a sentence to count the instances of the word \"the\":'\
          , end = ' ')
    sentence = input().strip().split()
    count = 0
    word_sep = 0
    previous_word = ''
    for c in sentence:
        if(word_sep == 1):
            print(c)
            print(previous_word)
            word_sep = 0
        word = c.lower()
        if (word == 'the'):
            count = count + 1
            word_sep = word_sep + 1
        else:
            previous_word = c

        

    count = str(count)
    print('The number of \"The\" instances in the sentence are: ' + count)

'''
    print('') 
    print('Please enter a non-negative interger to calculate the factorial:', end = ' ')
    factorial = int(input())
    answer = 0
    if (factorial < 0):
        while(factorial < 0):
            print('Please enter a non-negative integer:', end = ' ')
            factorial = int(input())
            factorial1 = factorial
        while(factorial != 0):
            multiplier = factorial - 1
            print(multiplier)
            print(factorial)
            loop_answer = factorial * multiplier
            factorial = factorial - 1
            answer = answer + loop_answer
        answer = answer + factorial1
        print(answer)
'''





if __name__ == "__main__":
    main()
