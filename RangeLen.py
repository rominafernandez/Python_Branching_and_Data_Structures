## Exercise 9 – Working with range and len

# Write a program that generates four lists with different lengths by using the range() function.
# The user should be able to input which lengths he needs.
# Let the program print out the generated lists as well as the corresponding lengths.

len1 = input("How long should your lists be?\nType in four numbers separated by space.\n").split()

List1 = list(range(int(len1[0])))
List2 = list(range(int(len1[1])))
List3 = list(range(int(len1[2])))
List4 = list(range(int(len1[3])))

print(f"Your first list looks like this: {List1} and has {len(List1)} elements")
print(f"Your second list looks like this: {List2} and has {len(List2)} elements")
print(f"Your third list looks like this: {List3} and has {len(List3)} elements")
print(f"Your fourth list looks like this: {List4} and has {len(List4)} elements")
