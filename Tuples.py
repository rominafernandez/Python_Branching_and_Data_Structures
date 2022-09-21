## Exercise 20 - Working with Tuples

# Write a program that creates four tuple of different lengths.
# The lengths should be dictated by the user.
# Print out the tuples.
# Afterwards let the user chose one entry from each tuple to be displayed.
# Try to generate a tuple with duplicate values.

user_input = input("Type in four numbers separated by space which determine the length of four different tuples. \n").split()

tuple1 = ("bla",) * (int(user_input[0]))
tuple2 = tuple(range(int(user_input[1])))
tuple3 = tuple(range(int(user_input[2])))
tuple4 = tuple(range(int(user_input[3])))

print(f"Tuple 1: {tuple1}")
print(f"Tuple 2: {tuple2}")
print(f"Tuple 3: {tuple3}")
print(f"Tuple 4: {tuple4}")

# Tuple 1
user_input = int(input("\nWhich entry do you want to see from tuple 1?\n"))
if user_input < len(tuple1):
    print(f"The entry with the index {user_input} from tuple 1 is {tuple1[user_input]}.")
else:
    print(f"This index exceeds the length of tuple 1. Here is the last entry instead: {tuple1[-1]} with the index {len(tuple1)-1}")

# Tuple 2
user_input = int(input("\nWhich entry do you want to see from tuple 2?\n"))
if user_input < len(tuple2):
    print(f"The entry with the index {user_input} from tuple 2 is {tuple2[user_input]}.")
else:
    print(f"This index exceeds the length of tuple 2. Here is the last entry instead: {tuple2[-1]} with the index {len(tuple2)-1}")

# Tuple 3
user_input = int(input("\nWhich entry do you want to see from tuple 3?\n"))
if user_input < len(tuple3):
    print(f"The entry with the index {user_input} from tuple 3 is {tuple3[user_input]}.")
else:
    print(f"This index exceeds the length of tuple 3. Here is the last entry instead: {tuple3[-1]} with the index {len(tuple3)-1}")

# Tuple 4
user_input = int(input("\nWhich entry do you want to see from tuple 4?\n"))
if user_input < len(tuple4):
    print(f"The entry with the index {user_input} from tuple 4 is {tuple4[user_input]}.")
else:
    print(f"This index exceeds the length of the tuple. Here is the last entry instead: {tuple4[-1]} with the index {len(tuple4)-1}")
