## Exercise 62 – Inserting values

# Write a program that generates three lists of different sizes and print them out
# Let the user choose where on these lists he wants to insert which number

Ls1 = list(range(10, 101, 10))
Ls2 = list(range(12))
Ls3 = list(range(2, 15, 2))

print(f"Here are three lists: \nList 1: {Ls1} \nList 2: {Ls2} \nList 3: {Ls3}\n")
print("You can decide which number you want to add where in those lists. \nWrite first the number and then the place separated by space.")
input1 = input("List 1: ").split()
input2 = input("List 2: ").split()
input3 = input("List 3: ").split()

if int(input1[1]) > len(Ls1)-1:
    print(f"Your index {input1[1]} exceeds the length of list 1 so your element {input1[0]} will be added to the end of the list.")
Ls1.insert(int(input1[1]), int(input1[0]))
print(f"List 1: {Ls1}")

if int(input2[1]) > len(Ls2)-1:
    print(f"Your index {input2[1]} exceeds the length of list 2 so your element {input2[0]} will be added to the end of the list.")
Ls2.insert(int(input2[1]), int(input2[0]))
print(f"List 2: {Ls2}")

if int(input3[1]) > len(Ls3)-1:
    print(f"Your index {input3[1]} exceeds the length of list 3 so your element {input3[0]} will be added to the end of the list.")
Ls3.insert(int(input3[1]), int(input3[0]))
print(f"List 3: {Ls3}")
