'''
Author:Carson Gooch
Date:November 5th, 2024
Class:CSE 174
Section:F

This program involves grabbing and sorting data sets.

The program gives the user a variety of options. Option one is to load a set
of data from a file. Option 2 is to print the unsorted list of data that has
been obtained from the file. Option 3 is to sort the list based on shipment IDs
Option 4 is to sort the list based off of tracking numbers. Option 5 is to
print the sorted list. Finally option 6 is to exit the loop.
'''



#Checks if the file has been read or not yet
file_check = False
#Checks if the file has been sorted yet
sort = False
#Checks if the file has been loaded yet
load_file_check = False
#Variable that keeps all lines in the file
file_lines = '' 
#Variable that has the file information
file_read = ''
#Varibale that keeps all data of the file 
file_data = ''
#Second variable of file_read but just used for sorting
file_read_sort = ''
#Second variable of file_lines but just used for sorting
file_lines_sort = ''

def menu():
    exit_var = False
    while (not exit_var):
        print("1. Load from a file")
        print("2. Print from the loaded list")
        print("3. Sort the list based on shipment IDs")
        print("4. Sort the list based on the tracking numbers")
        print("5. Print the sorted list")
        print("6. Exit")
        print("Enter a number[1-6]:", end = '')
        selection = input()

        if selection == '1':
            load_file()
        elif selection == '2':
            loaded_list()
        elif selection  == '3':
            sort_list()
        elif selection == '4':
            tracking_num()
        elif selection == '5':
            print_list()
        elif selection == '6':
            print('End!')
            exit_var = True
        else:
            print('Invalid Option Selected!')
    

def load_file():
    global file_check
    global load_file_check
    global file_lines
    global file_read
    global file_data
    global sort
    print('Enter the name of the file: ', end = '')
    file_data = input()
    file_read = open(file_data, 'r')
    for file_lines in file_read:
        file_lines = file_lines.strip().split()
    print('Loading from the file is done!')
    print('')
    file_check = True
    load_file_check = True
    sort = False
    return file_lines


def loaded_list():
    global file_lines
    global file_read
    if not file_check:
        print("No data has been loaded yet!")
        print('')
    else:
        print('**** Printing the list ****')
        line_count = 0
        file_read = open(file_data, 'r')
        for file_lines in file_read:
            file_lines = file_lines.strip().split()
            print(file_lines)
            line_count += 1
            if (line_count > 10):
                line_count = 0
                print('Enter something to continue/enter s to stop: ', end = '')
                cont = input()
                if cont == 's':
                    print('')
                    return
        print('')


def sort_list():
    if not file_check:
        print("No data has been loaded yet!")
        print('')
    else:
        sort1()

def tracking_num():
    if not file_check:
        print("No data has been loaded yet!")
        print('')
    else:
        sort2()
        print('')


def print_list():
    global sort
    if not file_check:
        print("No data has been loaded yet!")
        print('')
    elif not sort:
        print('Nothing sorted yet!')
        print('')
    else:
        print('**** Printing the list ****')
        line_count = 0
        for line in file_lines_sort:
            print(line)
            line_count += 1
            if (line_count > 10):
                line_count = 0
                print('Enter something to continue/enter s to stop: ')
                cont = input()
                if cont == 's':
                    return
        print('')
    


def sort1():
    '''
    This function uses bubble sort to sort the data set based off of shipment
    IDs. This function uses 2 global variables and transfers those variables to
    two different variables so that the unsorted list remains unchanged.
    Args:
        None
    Returns:
        None
    '''
    global file_lines
    global file_read
    global file_lines_sort
    global file_read_sort
    global sort
    file_lines_sort = file_lines
    file_read_sort = file_read
    file_read_sort = open(file_data, 'r')

    file_lines_sort = []
    for line in file_read_sort:
        colums = line.strip().split()
        if len(colums) >= 4:
            file_lines_sort.append(colums)
    swap = True
    while(swap):
        swap = False
        for i in range(0, len(file_lines_sort) - 1):
            if int(file_lines_sort[i][1]) > int(file_lines_sort[i + 1][1]):
                temp = file_lines_sort[i]
                file_lines_sort[i] = file_lines_sort[i + 1]
                file_lines_sort[i + 1] = temp
                swap = True
    print('Sorting is done!')
    print('')
    sort = True
def sort2():
    '''
    This function uses selection sort the sort the tracking numbers. This
    function works very similarly to the previous sorting function. It has the
    same method of using sorting global variables to not change the unsorted
    list. 

    Args:
        None:
    Returns
        None:
    '''
    global file_lines
    global file_read
    global file_lines_sort
    global file_read_sort
    global sort
    file_read_sort = open(file_data, 'r')
    file_lines_sort = []
    for line in file_read_sort:
        colums = line.strip().split()
        if len(colums) >= 4:
            file_lines_sort.append(colums)
    for i in range(len(file_lines_sort) - 1):
        min = i
        for j in range(i + 1, len(file_lines_sort)):
            if file_lines_sort[j][3] < file_lines_sort[min][3]:
                min = j
        if(min != i):
            temp = file_lines_sort[i]
            file_lines_sort[i] = file_lines_sort[min]
            file_lines_sort[min] = temp
    print('Sorting is done!')
    sort = True
if __name__ == "__main__":
    menu()