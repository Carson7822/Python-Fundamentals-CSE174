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

if __name__ == "__main__":
    main()