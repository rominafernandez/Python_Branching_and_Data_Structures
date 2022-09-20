## Exercise 4 - Names

# Write a program that asks the user their name, if they enter
# your name say "That is a nice name", if they enter "John
# Cleese" or "Michael Palin", tell them how you feel about
# them ;), otherwise tell them "You have a nice name."

name = input("Please type in your name: ")

if name == "Romina":
    print("That is a nice name")
elif name == "John Cleese" or name == "Michael Palin":
    print("Wow, you're famous!")
else:
    print(f"{name} is a very nice name.")
