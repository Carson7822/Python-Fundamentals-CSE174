'''
Carson Gooch
CSE 174 
lab 2:Income Tax
'''
#This program calculates the total tax over the past three years for each
#of the two employees in the Initech Company 


def IncomeOne():
    #income of Employee One
    Employee_one_income = 38000
    print('Computing the tax for employee #1:')
    #Multiplys the income by all 3 years percentages combined
    Employee_one_income = Employee_one_income * .0198
    print('Net income: 38000')
    print('Total tax:',round(Employee_one_income,1))

def spacer():
    print ('')

def IncomeTwo():
    Employee_two_income = 96000
    print('Computing the tax for employee #2:')
    Employee_two_income = Employee_two_income * 0.0234
    print('Net income: 96000')
    print('Total tax:',round(Employee_two_income,3))


if __name__ == "__main__":
    #run
    IncomeOne()
    spacer()
    IncomeTwo()
