## Exercise 13 - Slicing with a :

# Write a program that generates a list with the help of the range function
# The user should input the length of the wanted list and than input four other different numbers that
# can be used for slicing the list
# The first number should be an endpoint of a new list, the second number a starting point
# and the other two numbers should represent skips you can do with slicing
# Print out the new lists

list_length = int(input("Type in a number to generate a list of this length: "))
user_list = list(range(list_length))

print(f"This is your list: {user_list}")

user_input = int(input("Define a new end point for the list: "))
print(f"The new list is: {user_list[:user_input]}")

user_input = int(input("Define a new starting point for the list: "))
print(f"The new list is: {user_list[user_input:]}")

user_input = int(input("Define a skipping number: "))
print(f"The new list is: {user_list[::user_input]}")

user_input = int(input("Define another skipping number: "))
print(f"The new list is: {user_list[::user_input]}")
