"""Program om sökning i lista"""

def input_name():
    """Läser in ett namn från användaren och returnerar det i sökbar form."""
    return input("Ange namn: ").casefold()

def is_phonenum(phonenum):
    """Returnerar True on phonenum ser ut som telefonnummer"""
    clean_phonenum = phonenum.replace("-", "").replace(" ", "")
    return clean_phonenum.isdigit()

def input_phonenum(prompt="Ange telefonnummer: "):
    """
    Läser in en telefonnummer från användaren, ber användaren om nytt försök om 
    det inte ser ut som ett telefonnummer.
    """
    phonenum = input(prompt)

    while not is_phonenum(phonenum):
        phonenum = input(prompt)

    return phonenum

def fill_phonbook():
    """
    Ber användaren att fylla telefonboken.
    Returnerar en uppslagslista som innehåller telefonboken.
    """
    phonebook = dict()

    name = input_name()
    while name:
        number = input_phonenum(
            f"Ange telefonnummer för {name.capitalize()}: ")
        phonebook[name] = number

        name = input_name()

    return phonebook

def search_phonebook(phonebook):
    """Låter användaren söka i phonebook"""
    name = input_name()
    while name:
        try:
            print(f"{name.capitalize()} har telefonnummer {phonebook[name]}.")
        except KeyError:
            print(f"Hittade INTE {name.capitalize()} i telefonboken.")

        name = input_name()


def main():
    """Huvudprogrammet"""
    print("Nu bygger vi upp telefonboken. Ange namn och nummer. "
          "Ange tom sträng för att gå vidare.")

    phonebook = fill_phonbook()

    print("Nu ska vi söka bland namnen. Skriv namn för att söka. "
          "Skriv blankrad för att avsluta.")

    search_phonebook(phonebook)


if __name__ == "__main__":
    main()
