'''
Carson Gooch
This is lecture 1 
this lecture is all about variables 
'''
'''
We always want to start a code with comments to add our name
as a author and to explain the purpose of the code
'''

def run():
    '''
    If we have a function in our code like run
    we must start the function with some comments
    explaining the purpose of the function 
    '''
    #This function will explain variables and run some variables
    #We want to keep the length of each line to less than 80 characters
    #VS code shows how many characters at the bottom
    
    #Why do we need variables?
    #In order to be able to solve problems we should be able to hold
    #On to values and results and result of calculations
    #We can use them later for more calculations thats why we have
    #Variables in almost all programming languages 

    #Names must be all in lowercase for variables 
    #Names should be meaningful depending on what value the var is holding
    #The same rule applies to function names as well

    #Some examples

    num = 10
    gpa = 3.87
    name = 'Carson'
    #This adds 10 to the value of num and saves result
    num = num + 10

    num += 1
    num = num + 1
    #This will print 22 because we have added 10 + 10 + 1 + 1
    print(num)

    print('num is',num)
    print('num is ' + str(num))

    result = 'Carson is'
    age = 18
    end = 'years old'

    #Can do this with commas
    print(result,age,end)
    #Or can use it with the str function
    print(result + ' ' + str(age) + ' ' + end)

    num_of_tires = 841

    num_of_cars = num_of_tires // 4

    print(num_of_cars)

    num_tires_left = num_of_tires % num_of_cars 
    print(num_tires_left)

    #More examples in videos 

def assignment():
    age = 19
    gpa = 2.75
    letter_grade = 'B'

    #the \n command takes the code to the next line of the terminal
    print("age =",age,"\ngpa =",gpa,"\n",letter_grade)
    first = 'm'
    last = 'b'

    temp = 42
    rate = 1.2

    print('my initals:', '\t', last)
    print('temp in celcius: ' + str(temp))
    print('rate of USD to something is:',rate)

    height_in_cm = 170
    weight_in_kilogram = 80

    bmi = weight_in_kilogram / (height_in_cm / 100) ** 2

    print(bmi)

if __name__ == "__main__":
    #run()
    assignment()



