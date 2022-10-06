## Exercise 6 - Comparing numbers

# Write a program that gets four numbers as input from the user.
# The program should print out a positive encouragement if one of these conditions are fullfilled and a negative
# encouragement if none of them are true
# Input 1 = Input 2 and Input 3 = Input 4
# Input 1 = Input 3 and Input 2 = Input 4
# Input 1 = Input 4 or Input 2 = Input 3

nr1 = int(input("Please type in a number: "))
nr2 = int(input("Please type in another number: "))
nr3 = int(input("Please type in another number: "))
nr4 = int(input("Please type in another number: "))

if nr1 == nr2 and nr3 == nr4:
    print("Good job, you typed in two pairs of numbers.")
elif nr1 == nr3 and nr2 == nr4:
    print("Good job, you typed in two pairs of numbers.")
elif nr1 == nr4 or nr2 == nr3:
    print("Good job, you typed in at least one pair of numbers.")
else:
    print("You don't like repeating yourself, don't you.")


## Exercise 7 - Other comparisons

# Take the program from Exercise 6 and add some more statements for printing out a positive encouragement
# Input 1 > Input 2 and Input 3 > Input 4
# Input 1 < Input 3 and Input 2 < Input 4
# Input 1 = Input 4 or Input 2 >= Input 3
# Input 1 <= Input 4 and Input2 = Input 3

if nr1 > nr2 and nr3 > nr4:
    print("Well done, your second number is bigger than the first and your last number is bigger than the third number.")
elif nr1 < nr3 and nr2 < nr4:
    print("Well done, Your third number is bigger than your first and your last number is bigger than your second number.")
elif nr1 == nr4 or nr2 >= nr3:
    print("Well done, Your first and last number are the same and your second number is bigger or equal to your third number.")
elif nr1 <= nr4 and nr2 == nr3:
    print("Well done.")
else:
    print("What have you done?")
