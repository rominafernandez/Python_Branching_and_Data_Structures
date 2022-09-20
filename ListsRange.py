## Exercise 10 – Skipping parts with range

# Write a Program that generates different lists with the help of the range function
# The program should generate a list that doesn‘t start at 0
# The program should generate two other lists that skip some numbers (three arguments for range)
# Don‘t forget to print out all three lists at the end

print("At which number should your lists start and end? \nWhich steps do you want those numbers to have inbetween?\nType in those three numbers separated by space.\n")
len1 = input("First list: ")
len1 = len1.split()
len2 = input("Second list: ")
len2 = len2.split()
len3 = input("Third list: ")
len3 = len3.split()

List1 = list(range(int(len1[0]), int(len1[1]), int(len1[2])))
List2 = list(range(int(len2[0]), int(len2[1]), int(len2[2])))
List3 = list(range(int(len3[0]), int(len3[1]), int(len3[2])))

print(f"\nYour first list looks like this: {List1} and has {len(List1)} elements")
print(f"Your second list looks like this: {List2} and has {len(List2)} elements")
print(f"Your third list looks like this: {List3} and has {len(List3)} elements")
