"""Ett testprogram för personklasser"""

import address_ny
import person

class PersonSmeknamn(person.Person):
    """Bygger ut Person-klassen med smeknamn"""

    def __init__(self, förnamn, efternamn, födelsedag, adress, telefon, 
            smeknamn=""):
        """Skapar en person med attributen förnamn, efternamn, födelsedag, 
        adress, telefon"""
        super().__init__(förnamn, efternamn, födelsedag, adress, telefon)
        if smeknamn:
            self.__smeknamn = smeknamn
        else:
            self.__smeknamn = förnamn + "is"

    def get_smeknamn(self):
        """Returnerar smeknamnet"""
        return self.__smeknamn

def main():
    """Huvudprogram"""
    p1 = PersonSmeknamn("Kim", "Samson", "1995-01-01",
            address_ny.Adress("Lindstedtsvägen", "5", "11428", "Stockholm"),
            "okänt")
    p2 = PersonSmeknamn("Sam", "Kimson", "2000-01-01", "Malmö", "0701234567")

    print(f"p1 = {p1} har smeknamnet {p1.get_smeknamn()}")
    print(f"{p1} bor på {p1.get_address()}.")
    print(f"p2 = {p2} har smeknamnet {p2.get_smeknamn()}")

if __name__ == "__main__":
    main()
