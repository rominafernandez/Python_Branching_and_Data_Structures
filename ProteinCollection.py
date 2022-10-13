## Exercise 18 - Protein collection

# Write a program that creates a complex dictionary in form of a protein collection
# Each entry of the dictionary „proteins“ should contain another dictionary in which the name,
# the length of the protein, the function and the location are collected
# The final dictionary should contain information of at least four proteins
# Print out the final dictionary at the end (in the next exercise)
import json

Proteins = {}
Proteins["PRDM1"] = {"Name":"PR domain zinc finger protein 1", "Length":825, "Function":"Transcription regulation", "Location": "Chromosome 6"}
Proteins["IRF1"] = {"Name":"Interferon regulatory factor 1", "Length":325, "Function":"Antiviral defense", "Location":"Chromosome 5"}
Proteins["STAT1"] = {"Name":"Signal transducer and activator of transcription 1" , "Length":750, "Function":"Antiviral defense", "Location":"Chromosome 2"}
Proteins["MCM5"] = {"Name":"Minichromosome maintenance complex component 5", "Length":734, "Function":"DNA replication", "Location": "Chromosome 22"}
Proteins["ORC2"] = {"Name":"Origin recognition complex subunit 2", "Length":577, "Function":"DNA replication", "Location":"Chromosome 2"}
Proteins["CDC6"] = {"Name":"Cell division control protein 6 homolog", "Length":560, "Function": "Cell division", "Location":"Chromosome 17"}
Proteins["PSKH1"] = {"Name":"Serine/threonine-protein kinase H1", "Length":424, "Function":"Kinase", "Location":"Chromosome 16"}
Proteins["MAPK2"] = {"Name":"Mitogen-activated protein kinase 2", "Length":400, "Function":"Kinase", "Location":"Chromosome 1"}


## Exercise 19 - Adjusting the Collection

# Take your dictionary from exercise 18 and write a program that allows the user to make some changes
# Ask the user if he wants to add an entry, delete an entry or change an entry
# If the user wants to delete an entry ask for the entry which should be removed and remove it
# If the user wants to change an entry ask which part should be
# changed and what the new content should be
# If the user wants to add an entry ask for the information necessary to create a new entry
# Print the dictionary at the start and end of the program

print("Here is the Protein dictionary:")
tmp = json.dumps(Proteins, indent=4)
print(tmp)

user_op = input("\nWhat action would you like to perform for the dictionary? \nChoose either search, add, delete or change.\n")
# Adding to the dictionary. Either a whole new protein or add a new key-value pair to an existing protein
if user_op == "add":
    user_input = input("Do you want to add a whole new protein (new) or add information to an existing protein (add)?\n")
    if user_input == "new":
        print("Please provide the information of the protein you want to add.")
        prot_abbr = input("Abbreviation: ")
        if prot_abbr in Proteins:
            print(f"{prot_abbr} already exists in the dictionary! It will not be added to avoid errors.")
        else:
            prot_name = input("Full name: ")
            prot_length = int(input("Length (Amino acids): "))
            prot_function = input("Function: ")
            prot_location = input("Location (Chromosome): ")
            Proteins[prot_abbr] = {"Name":prot_name, "Length":prot_length, "Function":prot_function, "Location":prot_location}

            tmp = json.dumps(Proteins, indent=4)
            print(f"This is the new dictionary: \n{tmp}")
    elif user_input == "add":
        print("Please provide the information you want to add.")
        prot_abbr = input("Abbreviation: ")
        if prot_abbr in Proteins:
            prot_key = input("Key: ")
            prot_value = input("Value: ")
            if prot_value.isdigit():
                prot_value = int(prot_value)
            Proteins[prot_abbr][prot_key] = prot_value

            tmp = json.dumps(Proteins, indent=4)
            print(f"This is the new dictionary: \n{tmp}")
        else:
            print(f"{prot_abbr} was not found in the dictionary!")
    else:
        print("Invalid Input")
# Deleting an entry. Asks the user for the abbreviation of the protein, which should be deleted.
elif user_op == "delete":
    prot_abbr= input("Which protein do you want to delete? \nAbbreviation: ")
    if prot_abbr in Proteins:
        del Proteins[prot_abbr]

        tmp = json.dumps(Proteins, indent=4)
        print(f"This is the new dictionary: \n{tmp}")
    else:
        print(f"{prot_abbr} was not found in the dictionary!")
# Changing entries. Can only change values and not keys.
elif user_op == "change":
    prot_abbr = input("Of which protein do you want to change the information?\nAbbreviation: ")
    if prot_abbr in Proteins:
        print("Choose from the following list, which part you want to change:")
        # prints a changing list depending on the existing keys
        print(*list(Proteins[prot_abbr].keys()), sep=', ')
        prot_key = input()
        if prot_key in list(Proteins[prot_abbr].keys()):
            prot_value = input("New information:")
            if prot_value.isdigit():
                prot_value = int(prot_value)
            Proteins[prot_abbr][prot_key] = prot_value

            tmp = json.dumps(Proteins, indent=4)
            print(f"This is the new dictionary: \n{tmp}")
        else:
            print(f"{prot_key} is no available key in {prot_abbr}.")
    else:
        print(f"{prot_abbr} was not found in the dictionary!")
# Search for a protein
elif user_op == "search":
    prot_abbr = input("Which protein are you looking for? \nAbbreviation: ")
    if prot_abbr in Proteins:
        tmp = json.dumps(Proteins[prot_abbr], indent=4)
        print(f"Here is the entry for {prot_abbr}: \n{tmp}")
    else:
        print(f"{prot_abbr} was not found in the dictionary!")
# Invalid input if none of the above are true
else:
    print("Invalid Input")
