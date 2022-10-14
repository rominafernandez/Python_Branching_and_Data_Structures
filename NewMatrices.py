## Exercise 15 - New matrices

# Write a program that creates at least three different matrices with different sizes
# For this exercise rows stands for the numbers of sublists and columns for the number of entries in the sublists
# One of them should be quadratic
# One should have more columns than rows
# One should have more rows than columns

M1 = [[0,1,2],[3,4,5],[6,7,8]]
M2 = [[5,6],[3,9],[2,7]]
M3 = [[3,5,6],[2,9,5]]


## Exercise 60

# Take your lists from exercise 15 and remove at least two different entries from each of these lists with the help of indices
# Let the user choose which entries he wants to have removed after he declared the dimensions of the lists
# Run at least on security check (if statement) to see if the given indices are part of the lists (len operator)
print(M1)
M1[1].remove(M1[1][0])
M1[0].remove(M1[0][2])
print(M1)

print(M2)
M2[2].remove(M2[2][0])
M2[2].remove(M2[2][0])
print(M2)

print(M3)
M3[0].remove(M3[0][1])
M3[1].remove(M3[1][2])
print(M3)

# Create a matrix with user input
user_input = input("Type in the dimensions for a list separated by space.\n").split()
user_col = int(user_input[0])
user_row = int(user_input[1])
ls1 = list(range(user_col))
user_matrix = user_row*[ls1]
print(f"Here is your matrix: {user_matrix}")

# Delete user specified entry
user_input = input("Type in the dimensions of an entry you want to delete.\n").split()
user_col = int(user_input[0])
user_row = int(user_input[1])

if user_row < len(user_matrix) and user_col < len(user_matrix[user_row]):
    user_matrix[user_row].remove(user_matrix[user_row][user_col])
    print(f"Here is your new matrix: {user_matrix}")
else:
    print("Error: Index out of range")
