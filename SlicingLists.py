## Exercise 12 - Slicing of lists

# Write a program that generates two different lists with contents of your choice
# Let the user input four numbers
# If the numbers entered are bigger than the length of the lists ask a second time for smaller numbers
# Slice your lists with the numbers from the user
# If the new numbers are still too big generate slices until the last entry of the lists

Ls1 = list(range(5, 50, 5))
Ls2 = list(range(2, 40, 4))

print(f"\nHere are the two Lists you can slice: \nList 1 = {Ls1} \nList 2 = {Ls2}")
user_input = input("\nType in four numbers by which you want to slice the lists. \nThe first two numbers indicate the starting and endpoint for the first list and the second two numbers for the second list. \nSeparate them by spaces.\n").split()

# Security check to see, if the lists can be sliced by those numbers. If not, ask once for new input
if int(user_input[0]) > len(Ls1)-1 or  int(user_input[1]) > len(Ls1)-1 or int(user_input[2]) > len(Ls2)-1 or int(user_input[3]) > len(Ls2)-1:
    print(f"Your input number pairs exceed the length of the lists. \nKeep in mind that the first list has {len(Ls1)} elements and the second list has {len(Ls2)} elements.")
    user_input = input("Type in a new set of numbers.\n").split()

# Generating the slices for the first list
    if int(user_input[0]) < len(Ls1)-1 and  int(user_input[1]) < len(Ls1)-1:
        res1 = Ls1[int(user_input[0]):int(user_input[1])]
        print(f"List 1 = {res1}")
    elif int(user_input[0]) < len(Ls1)-1 and  int(user_input[1]) > len(Ls1)-1:
        res1 = Ls1[int(user_input[0]):len(Ls1)]
        print(f"Your second number still exceeds the length of List 1 so the slicing ends at the end of the list. \nList 1 = {res1}")
    else:
        print(f"Can not slice the first list by those numbers. Here is the whole list again: \nList 1 = {Ls1}")

# Generating the slices for the second list
    if int(user_input[2]) < len(Ls2)-1 and int(user_input[3]) < len(Ls2)-1:
        res2 = Ls2[int(user_input[2]):int(user_input[3])]
        print(f"List 2 = {res2}")
    elif int(user_input[2]) < len(Ls2)-1 and int(user_input[3]) > len(Ls2)-1:
        res2 = Ls2[int(user_input[2]):len(Ls2)]
        print(f"Your second number still exceeds the length of List 2 so the slicing ends at the end of the list. \nList 2 = {res2}")
    else:
        print(f"Can not slice the second list by those numbers. Here is the whole list again: \nList 2 = {Ls2}")
else:
    res1 = Ls1[int(user_input[0]):int(user_input[1])]
    res2 = Ls2[int(user_input[2]):int(user_input[3])]
    print(f"List 1 = {res1}")
    print(f"List 2 = {res2}")
