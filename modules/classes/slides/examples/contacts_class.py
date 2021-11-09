"""En enkel telefonbok"""

import person

def main():
    """Huvudprogram"""
    phonebook = {
            "adam": person.Person("Adam", "Adamsson", "1985-01-01",
                                  "Gatan 1, Orten", "0701234567"),
            "bertil": person.Person("Bertil", "Bertilsson", "1990-01-01",
                                    "Gatan 2, Orten", "okänt"),
            "cesar": person.Person("Cesar", "Cesarsson", "1995-01-01",
                                   "okänt", "0731234567")
            }

    for name in phonebook:
        print(name, end=" ")

    print()

    name = input("Who's contacts? ")
    while name != "":
        phone = phonebook[name].get_phone()
        address = phonebook[name].get_address()
        print(f"{name} has phone number {phone} and lives at {address}.")
        name = input("Who's contacts? ")

if __name__ == "__main__":
    main()
