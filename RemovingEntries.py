## Exercise 14 - Removing entries

# Write a program that generates at least three different lists.
# Print these lists out.
# Ask the user for one entry from each list he wants to have removed.
# Let the program remove the entry.
# Print out the new lists.

Ls1 = list(range(10))
Ls2 = ["Monkey", "Donkey", "Lion", "Cat", "Dog"]
Ls3 = ["Hello", 1, 5, "World", 20, 30]

print(f"\nHere are three lists: \nList 1: {Ls1} \nList2: {Ls2} \nList 3: {Ls3}\n \nNow you can decide which element should be removed from each list.")
input1 = int(input("List 1: "))
input2 = input("List 2: ")
input3 = input("List 3: ")

Ls1.remove(input1)
print(f"\nList 1 without element {input1}: {Ls1}")

Ls2.remove(input2)
print(f"List 2 without element {input2}: {Ls2}")


if input3.isdigit():
    input3 = int(input3)
    Ls3.remove(input3)
else:
    Ls3.remove(input3)
print(f"List 3 without element {input3}: {Ls3}")
