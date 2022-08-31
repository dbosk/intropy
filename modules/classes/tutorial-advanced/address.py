from dataclasses import dataclass
from typing import ClassVar
import input_type as it


@dataclass(frozen=True)
class Address:
    """En address."""

    DEFAULT_COUNTRY: ClassVar[str] = "Sweden"
    """Om inget land specificeras under konstruktion av Address-objekt så blir 
    `DEFAULT_COUNTRY` det land som gäller.
    """

    street_name: str  # gatunamnet, t.ex. "Sveavägen"
    street_number: str  # gatunumret, t.ex. "58" eller "2B"
    postal_code: int  # postnumret
    town: str  # orten
    country: str = DEFAULT_COUNTRY  # landets namn

    def __str__(self):
        address_str = f"{self.street_name} {self.street_number}, " \
                      f"{self.postal_code} {self.town}"

        if self.country != self.DEFAULT_COUNTRY:
            address_str += " " + self.country

        return address_str


def input_address(prompt: str = "") -> Address:
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
    daniels_kontor = Address("Lindstedtsvägen", "5", 11428, "Stockholm")
    print(f"Daniel har sitt arbetsrum på adressen {daniels_kontor}.")
    print(f"Gatan är {daniels_kontor.street_name}.")

    olles_kontor = Address("Lindstedtsvägen", "3", 11428, "Stockholm")
    if daniels_kontor == olles_kontor:
        print("Daniel och Olle har arbetsrum på samma adress.")
    else:
        print("Daniel och Olle har inte arbetsrum på samma adress.")


if __name__ == "__main__":
    main()
