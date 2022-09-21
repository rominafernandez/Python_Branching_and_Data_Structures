## Exercise 16 - Simple Dictionary

# Write a program that generates a simple dictionary consisting of at least three pre-defined entries with
# biological or biochemical background
# Ask the user for a new entry and add this new one to the dictionary afterwards
# Then ask the user for an entry that should be removed and remove the entry from the dictionary
# Print out the remaining dictionary

Dict1 = {"DNA":"Desoxyribonucleic Acid", "RNA":"Ribonucleic Acid", "ATP":"Adenosine triphosphate"}
print(f"This is the dictionary: {Dict1}")
user_input = input("Type in a key-value pair you want to add to the dictionary. \nSeparate them with a :\n").split(":")

Dict1[user_input[0]] = user_input[1]
print(f"Here is the updated dictionary: {Dict1}")

user_input = input("\nType in a key you want to remove from the dictionary. \n")

if user_input in Dict1:
    del Dict1[user_input]
    print(f"Here is the updated dictionary: {Dict1}")
else:
    print("The key was not found in the dictionary")
