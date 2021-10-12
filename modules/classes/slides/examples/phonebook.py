"""En enkel telefonbok"""

def main():
    """Huvudprogram"""
    phonebook = {"adam": "0701234567", "bertil": "0721234567"}
    phonebook["cesar"] = "0731234567"

    for name in phonebook:
        print(name, ", end=" ")

    name = input("Who's phone number? ")
    while name != "":
        print(f"{name} has phone number {phonebook[name]}.")
        name = input("Who's phone number? ")

if __name__ == "__main__":
    main()
