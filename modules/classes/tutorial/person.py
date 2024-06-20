from address import Address


class Person:
    """En person."""

    def __init__(self, first_name, last_name, address):
        """`first_name` är förnamnet (sträng).
        `last_name` är efternamnet (sträng).
        `address` är adressen (Address-objekt).
        """
        self.__first_name = first_name
        self.__last_name = last_name
        self.__address = address

    # Obs: __str__-metoden används för att ge en användarvänlig
    # sträng-representation av objektet.
    def __str__(self):
        """Personens fullständiga namn."""
        return self.full_name

    # Obs: __repr__-metoden används för att ge en sträng-representation
    # av objektet som är hjälpsam
    # för programmeraren.
    def __repr__(self):
        """En sträng som innehåller alla attribut."""
        return f"Person({self.__first_name}, {self.__last_name}, " \
               f"{repr(self.__address)})"

    # Obs: @property gör att vi inte behöver parenteserna:
    # `kund.namn` istället för `kund.namn()`
    @property
    def first_name(self):
        """Personens förnamn."""
        return self.__first_name.capitalize()

    @property
    def last_name(self):
        """Personens efternamn."""
        return self.__last_name.capitalize()

    @property
    def full_name(self):
        """Personens fullständiga namn."""
        return self.first_name + " " + self.last_name

    @property
    def address(self):
        """Personens adress."""
        return self.__address

    # Obs: "*" betyder att alla efterkommande parametrar måste explicit anges i
    # ett anrop om du väljer att tilldela dem värden. Till exempel är
    # "person.change_name('Olle', 'Ohlsson')" inte tillåtet, men
    # "person.change_name(first_name='Olle', last_name='Ohlsson')" är det.
    def change_name(self, *, first_name=None, last_name=None):
        """Byt personens för- och/eller efternamn.

        Om parametern `first_name` eller `last_name` är None så byts det
        inte ut.

        Exempel:
        >> person.change_name()  # Gör ingenting
        >> person.change_name(last_name="Stonkman")  # Byter efternamnet till
        "Stonkman"
        """
        if first_name:
            self.__first_name = first_name

        if last_name:
            self.__last_name = last_name

    def __lt__(self, other):
        """Gör så att operatorn < jämför personer baserat på deras namn."""
        return self.full_name < other.full_name


def main():
    """ Test program """

    # Skapa ett Person-objekt
    person = Person("Anne-Marie", "Ingeström", Address("Odengatan", "1",
                                                       11424, "Stockholm"))
    print(f"{person} bor på adressen {person.address}.")

    # Byt namn
    person.change_name(first_name="Margareta", last_name="Engström")
    print(f"{person} bor på adressen {person.address}")

    # Skapa ett annat Person-objekt
    person2 = Person("Ada", "Bedasdotter", Address("Uttervägen", "12",
                                                   98137, "Kiruna"))

    # Jämför objekten (använder __lt__-metoden implicit)
    if person < person2:
        print(f"{person} sorteras före {person2}.")
    else:
        print(f"{person2} sorteras före {person}.")

    people = [person, person2]

    # När man skriver ut en lista så används __repr__-metoden för alla element
    print(people)

    # Vi kan sortera listan eftersom < operatorn är definierad för Person-objekt
    people.sort()
    print(people)


if __name__ == "__main__":
    main()
