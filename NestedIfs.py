## Exercise 72 - Nested ifs

# Rework your program from Exercise 07 with the use of nested if statements instead of the logical operators:
# and
# or

nr1 = int(input("Please type in a number: "))
nr2 = int(input("Please type in another number: "))
nr3 = int(input("Please type in another number: "))
nr4 = int(input("Please type in another number: "))

if nr1 == nr2 == nr3 == nr4 :
    print("All your numbers are identical.")
elif nr1 == nr2:
    if nr3 == nr4:
        print("You tiped in two pairs of numbers.")
    else:
        print("Your first two numbers are identical but your last two are not.")
elif nr1 == nr3:
    if nr2 == nr4:
        print("You tiped in two pairs of numbers.")
    else:
        print("Your first and third number are identical but the others are not.")
elif nr1 == nr4:
    if nr2 == nr3:
        print("You tiped in two pairs of numbers.")
    else:
        print("Your first and last number are identical but the others are not.")
elif nr2 == nr3:
    if nr1 == nr4:
        print("You tiped in two pairs of numbers.")
    else:
        print("Your second and third number are identical but the others are not.")
elif nr2 == nr4:
    if nr1 == nr3:
        print("You tiped in two pairs of numbers.")
    else:
        print("Your second and last number are identical but the others are not.")
elif nr3 == nr4:
    if nr1 == nr2:
        print("You tiped in two pairs of numbers.")
    else:
        print("Your third and last number are identical but the others are not.")
else:
    print("You didn't repeat any numbers.")
