## Group Exercise 2 - Options Menu

# Write a program that takes at least 6 different numbers as input from the user.
# Then ask the user which of the four standard mathematical operations the program should run over these numbers.
# Use Print commands to show the user what options he has.
# Create an if-statement that checks what option the user chose (use if elif else).
# don’t forget to include a security check.
# Run your mathematical operations inside this statement.
# Print out the results by using f-strings or commas.

tmp = True

print("\n****Welcome to Calculator1000**** \n \nGet 5 \"random\" calculations with your numbers and operator of choice!")
while tmp == True:
    print("Please type in 6 numbers (only numbers greater or equal 1):")
    nr1 = int(input("Nr1: "))
    nr2 = int(input("Nr2: "))
    nr3 = int(input("Nr3: "))
    nr4 = int(input("Nr4: "))
    nr5 = int(input("Nr5: "))
    nr6 = int(input("Nr6: "))

    if nr1 <= 0 or nr2 <= 0 or nr3 <= 0 or nr4 <= 0 or nr5 <= 0 or nr6 <= 0:
        print("\nI said no numbers below 1!")
    else:
        tmp = False


tmp = True
print("\nWhich mathematical operation do you want to perform with those numbers? \nChoose between Addition (+), Subtraction (-), Multiplication (*) or Division (/)")
while tmp == True:
    mo = input("Chosen operator: ")

    if mo == "+" or mo == "Addition":
        print(f"All six numbers added up equals to {nr1 + nr2 + nr3 + nr4 + nr5 + nr6}")
        print(f"{nr1} + {nr2} = {nr1 + nr2}")
        print(f"{nr6} + {nr5} = {nr6 + nr5}")
        print(f"{nr3} + {nr4} = {nr3 + nr4}")
        print(f"{nr6} + {nr1} = {nr6 + nr1}")
        print(f"{nr2} + {nr3} = {nr2 + nr3}")
        tmp = False
    elif mo == "-" or mo == "Subtraction":
        print(f"All six numbers subtracted equals to {nr1 - nr2 - nr3 - nr4 - nr5 - nr6}")
        print(f"{nr1} - {nr2} = {nr1 - nr2}")
        print(f"{nr6} - {nr5} = {nr6 - nr5}")
        print(f"{nr3} - {nr4} = {nr3 - nr4}")
        print(f"{nr6} - {nr1} = {nr6 - nr1}")
        print(f"{nr2} - {nr3} = {nr2 - nr3}")
        tmp = False
    elif mo == "*" or mo == "Multiplication":
        print(f"All six numbers multiplied equals to {nr1 * nr2 * nr3 * nr4 * nr5 * nr6}")
        print(f"{nr1} * {nr2} = {nr1 * nr2}")
        print(f"{nr6} * {nr5} = {nr6 * nr5}")
        print(f"{nr3} * {nr4} = {nr3 * nr4}")
        print(f"{nr6} * {nr1} = {nr6 * nr1}")
        print(f"{nr2} * {nr3} = {nr2 * nr3}")
        tmp = False
    elif mo == "/" or mo == "Division":
        print(f"All six numbers divided by each other equals to {nr1 / nr2 / nr3 / nr4 / nr5 / nr6}")
        print(f"{nr1} / {nr2} = {nr1 / nr2}")
        print(f"{nr6} / {nr5} = {nr6 / nr5}")
        print(f"{nr3} / {nr4} = {nr3 / nr4}")
        print(f"{nr6} / {nr1} = {nr6 / nr1}")
        print(f"{nr2} / {nr3} = {nr2 / nr3}")
        tmp = False
    else:
        print("\nSorry, that is not a valid operator! \nTry either Addition (+), Subtraction (-), Multiplication (*) or Division (/)")
