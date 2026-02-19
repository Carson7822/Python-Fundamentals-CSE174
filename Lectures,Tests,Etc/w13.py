'''
Task for students:
1- Break the code into small tasks:
    Identify the different tasks being performed in the code, 
    such as reading data from a file, 
    creating a deep copy of the list, 
    sorting the list, 
    displaying the data, 
    and handling the menu.
	Then, define a Separate Method for Each Task:
    For every distinct task, create a separate method. For example:
    •	A method to read data from the file.
    •	A method to create a deep copy of the original list.
    •	A method to sort the list using an improved bubble sort.
    •	A method to display data with 10 items at a time, pausing between batches.

2- When displaying the list (either original or sorted), show only 10 items at a time.
    After printing 10 items, pause and ask the user:
    - "Press any key to continue, or 's' to stop: "
    If the user presses 's', stop displaying the list and return to the menu.
    Otherwise, continue displaying the next 10 items until the list is fully displayed.

'''
if __name__ == "__main__":

    filename = "data.txt"
    data_list = []
    
    file = open(filename, 'r')
    for line in file:
        data_list.append(line.strip())
    file.close()
   
    # Create a deep copy of the original list
    copy_list = []
    for item in data_list:
        copy_list.append(item)

    # Sort the copied list using an improved bubble sort algorithm
    n = len(copy_list)

    swapped = True
    while (swapped):
        swapped = False
        for j in range(n - 1):
            if copy_list[j] > copy_list[j + 1]:
                # swapping values
                copy_list[j], copy_list[j + 1] = copy_list[j + 1], copy_list[j]
                swapped = True

    # Menu-driven program
    while True:
        print("\nMenu:")
        print("1. Print original list")
        print("2. Print sorted list")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("Displaying the original list: ")
            # implement the display function as explain at the top


        elif choice == "2":
            print("Displaying the sorted list: ")
            # implement the display function as explain at the top

        elif choice == "3":
            # Exit the program
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")