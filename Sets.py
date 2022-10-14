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


## Exercise 22 - Adding and removing

# Take your sets from exercise 21
# Remove some elements from them
# Try to remove two elements directly one after the other
# Check which elements were removed with the print command
# Add the elements again to the set
# Print out the new sets
# What changes can you see?
print("")
print(set1)

set1.remove(1)
print(set1)

set1.remove(3)
set1.remove(0)
print(set1)

set1.add(1)
set1.add(3)
set1.add(0)
print(set1)
