## Exercise 21 - Working with Sets

# Write a program that creates four sets of different lengths
# The lengths should be dictated by the user
# Print out the sets

user_input = input("Type in four numbers separated by space which determine the length of four different sets. \n").split()

set1 = set(range(int(user_input[0])))
set2 = set(range(int(user_input[1])))
set3 = set(range(int(user_input[2])))
set4 = set(range(int(user_input[3])))

print(f"Set 1: {set1}")
print(f"Set 2: {set2}")
print(f"Set 3: {set3}")
print(f"Set 4: {set4}")
