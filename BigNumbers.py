## Exercise 5 - Big numbers

# Write a program that asks for two numbers
# If the sum of the numbers is greater than 100, print "That is a big number.“
# If the sum is greater than 10, print “That is a mediocre number.”
# If the sum is greater than 5, print “That is a small number”
# In all other cases print “This is a very small number”
# Combine all predicates in one if, elif, else statement

nr1 = int(input("Tell me a number: "))
nr2 = int(input("Tell me a second number: "))

if nr1 + nr2 > 100:
    print("That is a big number.")
elif nr1 + nr2 > 10:
    print("That is a mediocre number.")
elif nr1 + nr2 > 5:
    print("That is a small number.")
else:
    print("That is a very small number.")
