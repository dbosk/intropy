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

def input_full_name(prompt="Ange fullständigt namn."):
    """Ber användaren mata in namn, returnerar (förnamn, efternamn)."""
    print(prompt)

    firstname = input("Ange förnamn: ")
    while not firstname:
        firstname = input("Ange förnamn: ")

    lastname = input(f"Ange efternamn för {firstname}: ")

    capitalize = input("Stavar personen med inledande stor bokstav? [ja/nej] ")
    if capitalize.casefold() == "ja":
        firstname = firstname.capitalize()
        lastname = lastname.capitalize()

    return firstname, lastname

def input_contact(prompt=""):
    """
    Låter användaren mata in kontaktinfo om en kontakt,
    returnerar en dictionary med nycklarna:
        - first_name
        - last_name
        - nickname
        - phone_number
        - email
    """
    contact_info = {}

    first, last = input_full_name()
    contact_info["first_name"] = first
    contact_info["last_name"] = last

    nickname = input(f"Smeknamn för {first}: ")
    contact_info["nickname"] = nickname

    if nickname:
        phonenum = input_phonenum(f"Ange telefonnummer för {nickname}: ")
    else:
        phonenum = input_phonenum(f"Ange telefonnummer för {first}: ")

    contact_info["phone_number"] = phonenum

    return contact_info

def print_contact_info(contact_info):
    """
    Tar en dictionary med kontaktinfo och skriver ut på skärmen,
    har nycklarna:
        - first_name
        - last_name
        - nickname
        - phone_number
        - email
    """
    print(f"{contact_info['nickname']} "
          f"({contact_info['first_name']} {contact_info['last_name']}):")
    print(f"Phone: {contact_info['phone_number']}")
    print(f"Email: {contact_info['email']}")

def fill_phonbook():
    """
    Ber användaren att fylla telefonboken.
    Returnerar en uppslagslista som innehåller telefonboken.
    """
    phonebook = {}

    name = input_name("Ange namn för en ny kontakt: ")
    while name:
        phonebook[name] = input_contact(
            f"Ange kontaktinformation för {name.capitalize()}: ")

        print()
        name = input_name("Ange namn för en ny kontakt: ")

    return phonebook

def search_phonebook(phonebook):
    """Låter användaren söka i phonebook"""
    name = input_name()
    while name:
        try:
            print_contact_info(phonebook[name])
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
