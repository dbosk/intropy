"""A module with phonebook related functions"""

def print_sorted(phonebook):
    """Prints the names in phonebook in alphabetical order"""
    for i, name in enumerate(sorted(phonebook)):
        print(f"{name:10s}", end="")
        if (i+1) % 5 == 0:
            print()
    print()

def interactive_search(phonebook):
    """Lets the user search in the phonebook by name"""
    name = input("Who's phone number? ")
    while name != "":
        print(f"{name} has phone number {phonebook[name]}.")
        name = input("Who's phone number? ")

