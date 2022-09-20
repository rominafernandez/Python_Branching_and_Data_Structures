## Exercise 9 – Working with range and len

# Write a program that generates four lists with different lengths by using the range() function.
# The user should be able to input which lengths he needs.
# Let the program print out the generated lists as well as the corresponding lengths.
'''
len1 = int(input("How long should your first list be?\n"))
len2 = int(input("How long should your second list be?\n"))
len3 = int(input("How long should your third list be?\n"))
len4 = int(input("How long should your fourth list be?\n"))
'''

len5 = input("How long should your lists be?\nType in four numbers separated by space.\n")
len5 = len5.split()

List1 = list(range(int(len5[0])))
List2 = list(range(int(len5[1])))
List3 = list(range(int(len5[2])))
List4 = list(range(int(len5[3])))

print(f"Your first list looks like this: {List1} and has {len(List1)} elements")
print(f"Your secondt list looks like this: {List2} and has {len(List2)} elements")
print(f"Your third list looks like this: {List3} and has {len(List3)} elements")
print(f"Your fourth list looks like this: {List4} and has {len(List4)} elements")
