## Exercise 11 - Longer lists

# Write a Program that generates six different lists
# Append the third list to first one and the fourth list to the second one
# Extend the first list with the help of the fifth list and the second one with the help of the sixth list

ls1 = [1, 2, 3]
ls2 = [4, 5, 6]
ls3 = ["Hello", "World"]
ls4 = ["Monkey", "Donkey"]
ls5 = [1.1, 2.2, 3.3]
ls6 = [4.4, 5.5, 6.6]

ls1.append(ls3)
ls2.append(ls4)
print(ls1)
print(ls2)

ls1.extend(ls5)
ls2.extend(ls6)

print(ls1)
print(ls2)
