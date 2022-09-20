## Exercise 61 – Checking for values

# Write a program that generates a list with contents of your choice.
# Now let the user input at least three different things.
# Check whether these inputs are part of your list or not.
# Print out an appropriate answer.

Ls1 = ["Hello", 1, 5, "World", 20, 30, "Monkey", "Donkey", 6, 100, "Duck"]
user_input = input("\nType in three different numbers or words to check, whether they are in the secret list. \nSeparate the entries by space. \n").split()

# checking the first input
if user_input[0].isdigit():
    tmp = int(user_input[0])
    if tmp in Ls1:
        print(f"\n{tmp} is found in the list.")
    else:
        print(f"\n{tmp} is not found in the list.")
else:
    tmp = user_input[0]
    if tmp in Ls1:
        print(f"\n{tmp} is found in the list.")
    else:
        print(f"\n{tmp} is not found in the list.")

# checking the second input
if user_input[1].isdigit():
    tmp = int(user_input[1])
    if tmp in Ls1:
        print(f"{tmp} is found in the list.")
    else:
        print(f"{tmp} is not found in the list.")
else:
    tmp = user_input[1]
    if tmp in Ls1:
        print(f"{tmp} is found in the list.")
    else:
        print(f"{tmp} is not found in the list.")

# checking the third input
if user_input[2].isdigit():
    tmp = int(user_input[2])
    if tmp in Ls1:
        print(f"{tmp} is found in the list.")
    else:
        print(f"{tmp} is not found in the list.")
else:
    tmp = user_input[2]
    if tmp in Ls1:
        print(f"{tmp} is found in the list.")
    else:
        print(f"{tmp} is not found in the list.")
