#September 16th lecture about if and else statements 



if __name__ == "__main__":
    print('Enter your age:', end = '')
    age = float(input())

    if age >= 18:
        print('Do you have your learner\'s permit, yes or no:', end = '')
        learner = input()
        if learner.lower() == 'yes':
            print('You are eligable for a drivers liscense!')
        else:
            print('You are not eligable for a drivers liscense. \n'
            + 'Please obtain a learner\'s permit first.')
    elif age >= 15.5:
        print('You must obtain and have a learner\'s permit for 6 months')
    else:
        print('You are not old enough for a drivers liscense.')

    

