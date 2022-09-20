## Group Exercise 03 – Manipulating lists

# The user should create three lists according to his specifications (1, 2 or 3 arguments for the range function)
# Let the user manipulate the lists by adding an element, removing an element, reversing the list, searching for the
# index of an entry in the list or checking if a specific element is in the list
# Skip over parts that don‘t work with the user inputs, but tell him what went wrong

print("\n***********Welcome to List Manipulator 1000***********")
print("Here you can create lists as you like and manipulate them in many different ways.")
print("To create a list, you need to provide some info.")
print("1. Possibility: Type in 1 number to create a list from 0 to your number.")
print("2. Possibility: Type in 2 numbers to decide the starting and end point of the list.")
print("3. Possibility: Type in a third number to specify the skipping steps.")
print("Separate the numbers by space.")
print("Type q to quit the program")

while True:
    tmp = True
    user_input = ""
    user_input = input("\nCreate a list: ").split()

# generating of the user_list and safety checks
    if user_input[0] == "q":
        exit()
    elif len(user_input) == 1 and user_input[0].isdigit():
        user_list = list(range(int(user_input[0])+1))
        print(f"\nThis is the list you created: {user_list}")
    elif len(user_input) == 2 and user_input[0].isdigit() and user_input[1].isdigit():
        user_list = list(range(int(user_input[0]), int(user_input[1])+1))
        print(f"\nThis is the list you created: {user_list}")
    elif len(user_input) == 3 and user_input[0].isdigit() and user_input[1].isdigit() and user_input[2].isdigit():
        user_list = list(range(int(user_input[0]), int(user_input[1])+1, int(user_input[2])))
        print(f"\nThis is the list you created: {user_list}")
    else:
        print("\nInvalid Input")
        break

# Asking the user for list manipulations
    print("\n***Now you can choose manipulations.***")
    while tmp == True:
        print("\nChoose from the following options: add, remove, reverse, index, check. \nType new, if you want to create a new list and q if you want to quit the program.")
        user_op = input("Type in the option: ")
# First manipulation: Adding elements
        if user_op == "add" or user_op == "Add":
            print("Type in the number you want to add and the position you want to add it in (separated by space).")
            print("If your index exceeds the length of your list, the element will be added to the end of the list.")
            user_input = input()

            if user_input != "":
                user_input = user_input.split()
                if len(user_input) == 2 and user_input[0].isdigit() and user_input[1].isdigit():
                    user_list.insert(int(user_input[1]), int(user_input[0]))
                    print(f"This is your new list: {user_list}")
                else:
                    print("Invalid Input")
            else:
                pass

#Second manipulation: removing an elements
        elif user_op == "remove" or user_op == "Remove":
            print("Type in the number you want to remove from your list.")
            print("The first element with this value will be removed.")
            user_input = input()

            if user_input != "":
                if int(user_input) in user_list:
                    user_list.remove(int(user_input))
                    print(f"This is your new list: {user_list}")
                else:
                    print("This element is not found in your list.")
            else:
                pass

# Third manipulation: Reversing the lists
        elif user_op == "reverse" or user_op == "Reverse":
                user_list.reverse()
                print(f"This is your new list: {user_list}")

# Fourth manipulation: Searching for the index of an entry in the lists
        elif user_op == "index" or user_op == "Index":
            print("Type in the number of which you want to now the index of.")
            user_input = input()

            if user_input != "":
                if int(user_input) in user_list:
                    print(f"The index of element {user_input} is {user_list.index(int(user_input))}")
                else:
                    print("This element is not found in your list.")
            else:
                pass

# Fifth manipulation: Check for a specific element in the list
        elif user_op == "check" or user_op == "Check":
            print("Type in the number you want to check.")
            user_input = input()

            if user_input != "":
                if int(user_input) in user_list:
                    print(f"{user_input} was found in your list")
                else:
                    print("This element is not found in your list.")
            else:
                pass

# exit the manipulation menu
        elif user_op == "new" or user_op == "New":
            tmp = False

        elif user_op == "q":
            exit()

        else:
            print("Invalid Input")
