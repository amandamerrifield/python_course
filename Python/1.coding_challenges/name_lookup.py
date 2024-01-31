names = [
    "Dudley",
    "Matt",
    "Jane",
    "Sarah",
    "Jack",
    "Ted"
]

name_to_search = input("Enter the name to search: ")
name_found = False


for name in names:
    #this block will be executed 6 times because there are 6 names
    if name_to_search == name:
        print(name_to_search, " is registered to the course.")
        name_found = True
        break

if not name_found:
    print(name_to_search, " is not in the list.")
