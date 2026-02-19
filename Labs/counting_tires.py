'''
Carson Gooch
CSE 174 
lab 2:Counting Tires
'''
#This program takes the pairs of tires ordered for cars and calculates
#How many cars can be produced with all of the tires and count
#all of the tires left over.

def tire_calc():
    #Declares the amount of tire pairs
    Tire_pairs = 19873123
    #Multiplys the pair of tires to get the amount of individual tires
    Tire_pairs = Tire_pairs * 2
    print('The number of:',str(Tire_pairs),\
          'tires are added to the production line!')
    cars = Tire_pairs // 4
    print(cars,'cars are produced.')
    tires_left = Tire_pairs % cars
    print(tires_left,'tires are left.')


if __name__ == "__main__":
    tire_calc()
