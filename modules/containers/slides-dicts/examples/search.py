"""Program om sökning i lista"""

def input_name(prompt="Ange namn: "):
    """Läser in ett namn från användaren och returnerar det i sökbar form."""
    return input(prompt).casefold()

def is_phonenum(phonenum):
    """Returnerar True on phonenum ser ut som telefonnummer"""
    clean_phonenum = phonenum.replace("-", "").replace(" ", "")
    return clean_phonenum.isdigit()

def input_phonenum(prompt="Ange telefonnummer: ",
                   fail_prompt="Det ser inte ut some ett telefonnummer."):
    """
    Läser in en telefonnummer från användaren, ber användaren om 
    nytt försök om det inte ser ut som ett telefonnummer.
    """
    phonenum = input(prompt)

    while not is_phonenum(phonenum):
        print(fail_prompt)
        phonenum = input(prompt)

    return phonenum

def fill_phonbook():
    """
    Ber användaren att fylla telefonboken.
    Returnerar en uppslagslista som innehåller telefonboken.
    """
    phonebook = {}

    name = input_name("Ange namn för en ny kontakt: ")
    while name:
        number = input_phonenum(
            f"Ange telefonnummer för {name.capitalize()}: ")
        phonebook[name] = number

        print()
        name = input_name("Ange namn för en ny kontakt: ")

    return phonebook

def search_phonebook(phonebook):
    """Låter användaren söka i phonebook"""
    name = input_name()
    while name:
        try:
            print(f"{name.capitalize()} har telefonnummer {phonebook[name]}.")
        except KeyError:
            print(f"Hittade INTE {name.capitalize()} i telefonboken.")

        print()
        name = input_name()


def main():
    """Huvudprogrammet"""
    print("Nu bygger vi upp telefonboken. Ange namn och nummer. "
          "Ange tom sträng för att gå vidare.")
    print()

    phonebook = fill_phonbook()

    print()
    print("Nu ska vi söka bland namnen. Skriv namn för att söka. "
          "Skriv blankrad för att avsluta.")
    print()

    search_phonebook(phonebook)


if __name__ == "__main__":
    main()
