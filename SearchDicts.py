## Exercise 17 - Searching in Dictionaries

# Create a dictionary with at least ten entries with biological or biochemical background
# Let the user search the dictionary for a specific entry
# If the entry is already present ask the user for an update of the contents for this entry,
# if the entry does not exist add it to the dictionary
# Run this option at least three times during one call of the program
# Print out the original dictionary and the modified dictionary at the end
import json

Proteins = {}
Proteins["PRDM1"] = "PR domain zinc finger protein 1"
Proteins["IRF1"] = "Interferon regulatory factor 1"
Proteins["STAT1"] = "Signal transducer and activator of transcription 1"
Proteins["MCM5"] = "Minichromosome maintenance complex component 5"
Proteins["ORC2"] = "Origin recognition complex subunit 2"
Proteins["CDC6"] = "Cell division control protein 6 homolog"
Proteins["PSKH1"] = "Serine/threonine-protein kinase H1"
Proteins["MAPK"] = "Mitogen-activated protein kinase"
Proteins["ASK1"] = "Apoptosis signal-regulating kinase 1"
Proteins["TRAF2"] = "TNF receptor-associated factor 2"
Proteins["IKK2"] = "Inhibitor of nuclear factor-kappa-B kinase subunit beta"
Proteins["HDAC9"] = "Histone deacetylase 9"
Proteins["SIN3A"] = "Paired amphipathic helix protein"

tmp = Proteins.copy()

# Round 1
user_abbr = input("Which Protein abbreviation are you looking for? \n")

if user_abbr in Proteins:
    print(f"{user_abbr} was found in the dictionary Proteins. \nThe abbreviation {user_abbr} stands for {Proteins[user_abbr]}")
    user_input = input("Do you want to update this entry? \n")
    if user_input == "yes":
        user_input = input(f"Type in the new value. \n{user_abbr} = ")
        tmp[user_abbr] = user_input
    else:
        pass
else:
    print(f"{user_abbr} was not found in the dictionary Proteins.")
    user_input = input("Do you want to add the entry? \n")
    if user_input == "yes":
        user_input = input(f"Type in the new value. \n{user_abbr} = ")
        tmp[user_abbr] = user_input
    else:
        pass
tmp2 = json.dumps(Proteins, indent=4)
print(f"The dictionary before any changes: \n{tmp2}")
tmp2 = json.dumps(tmp, indent=4)
print(f"The dictionary after your changes: \n{tmp2}")

# Round 2
user_abbr = input("Which Protein abbreviation are you looking for? \n")

if user_abbr in Proteins:
    print(f"{user_abbr} was found in the dictionary Proteins. \nThe abbreviation {user_abbr} stands for {Proteins[user_abbr]}")
    user_input = input("Do you want to update this entry? \n")
    if user_input == "yes":
        user_input = input(f"Type in the new value. \n{user_abbr} = ")
        tmp[user_abbr] = user_input
    else:
        pass
else:
    print(f"{user_abbr} was not found in the dictionary Proteins.")
    user_input = input("Do you want to add the entry? \n")
    if user_input == "yes":
        user_input = input(f"Type in the new value. \n{user_abbr} = ")
        tmp[user_abbr] = user_input
    else:
        pass
tmp2 = json.dumps(Proteins, indent=4)
print(f"The dictionary before any changes: \n{tmp2}")
tmp2 = json.dumps(tmp, indent=4)
print(f"The dictionary after your changes: \n{tmp2}")

# Round 3
user_abbr = input("Which Protein abbreviation are you looking for? \n")

if user_abbr in Proteins:
    print(f"{user_abbr} was found in the dictionary Proteins. \nThe abbreviation {user_abbr} stands for {Proteins[user_abbr]}")
    user_input = input("Do you want to update this entry? \n")
    if user_input == "yes":
        user_input = input(f"Type in the new value. \n{user_abbr} = ")
        tmp[user_abbr] = user_input
    else:
        pass
else:
    print(f"{user_abbr} was not found in the dictionary Proteins.")
    user_input = input("Do you want to add the entry? \n")
    if user_input == "yes":
        user_input = input(f"Type in the new value. \n{user_abbr} = ")
        tmp[user_abbr] = user_input
    else:
        pass
tmp2 = json.dumps(Proteins, indent=4)
print(f"The dictionary before any changes: \n{tmp2}")
tmp2 = json.dumps(tmp, indent=4)
print(f"The dictionary after your changes: \n{tmp2}")
