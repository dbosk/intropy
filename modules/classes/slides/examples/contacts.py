"""En enkel telefonbok"""

def main():
    """Huvudprogram"""
    phonebook = {
            "adam": {
                "phone": "0701234567",
                "address": "Gatan 1, Orten"
                },
            "bertil": {
                "address": "Gatan 2, Orten"
                },
            "cesar": {
                "phone": "0731234567"
                }
            }

    for name in phonebook:
        print(name, end=" ")

    print()

    name = input("Who's contacts? ")
    while name != "":
        try:
            phone = phonebook[name]["phone"]
        except KeyError:
            phone = "no phone number"

        try:
            address = phonebook[name]["address"]
        except KeyError:
            address = "no address"

        print(f"{name} has phone number {phone} and lives at {address}.")
        name = input("Who's contacts? ")

if __name__ == "__main__":
    main()
