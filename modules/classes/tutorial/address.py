import input_type as it


class Address:
    """En address."""

    DEFAULT_COUNTRY = "Sweden"
    """Om inget land specificeras under konstruktion av Address-objekt så blir 
    `DEFAULT_COUNTRY` det land som gäller.
    """

    def __init__(self, street_name, street_number, postal_code, town,
                 country=DEFAULT_COUNTRY):
        """`street_name` är gatunamnet, t.ex. "Sveavägen" (sträng).
        `street_number` är gatunumret, t.ex. "58" eller "2B" (sträng).
        `postal_code` är postnumret (sträng).
        `town` är orten (sträng).
        `country` är landets namn (sträng).
        """
        self.__street_name = street_name
        self.__street_number = street_number
        self.__postal_code = postal_code
        self.__town = town
        self.__country = country

    def __str__(self):
        address_str = f"{self.street_name} {self.street_number}, " \
                      f"{self.postal_code} {self.town}"

        if self.__country != self.DEFAULT_COUNTRY:
            address_str += " " + self.country

        return address_str

    @property
    def street_name(self):
        """Gatunamnet."""
        return self.__street_name

    @property
    def street_number(self):
        """Gatunumret."""
        return self.__street_number

    @property
    def postal_code(self):
        """Postnumret."""
        return self.__postal_code

    @property
    def town(self):
        """Orten."""
        return self.__town

    @property
    def country(self):
        """Landets namn."""
        return self.__country


def input_address(prompt=""):
    """Låter användaren mata in data för en adress,
    returnerar ett Address-objekt."""
    if prompt:
        print(prompt)

    gata = input("Gatans namn: ")
    nummer = input("Gatunummer: ")
    postnummer = it.input_type(int, "Postnummer: ")
    postort = input("Postort: ")
    land = input(f"Land [blankt för {Address.DEFAULT_COUNTRY}]: ")
    if not land:
        land = Address.DEFAULT_COUNTRY

    return Address(gata, nummer, postnummer, postort, land)


def main():
    """Testprogram"""
    daniels_kontor = Address("Lindstedtsvägen", "5", "11428", "Stockholm")
    print(f"Daniel har sitt arbetsrum på adressen {daniels_kontor}.")
    print(f"Gatan är {daniels_kontor.street_name}.")

    olles_kontor = Address("Lindstedtsvägen", "3", "11428", "Stockholm")
    if daniels_kontor == olles_kontor:
        print("Daniel och Olle har arbetsrum på samma adress.")
    else:
        print("Daniel och Olle har inte arbetsrum på samma adress.")


if __name__ == "__main__":
    main()
