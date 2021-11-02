"""Modul med en klass för att hantera adresser"""

class Adress:
    """Klass för att hantera adresser"""
    def __init__(self, gata, nummer, postnummer, postort,
            land="Sverige"):
        """Returnerar ett adressobjekt"""
        self.__gata = gata
        self.__nummer = nummer
        self.__postnummer = postnummer
        self.__postort = postort
        self.__land = land

    def __str__(self):
        """Returnerar sträng för utskrift"""
        adress = f"{self.__gata} {self.__nummer}, " + \
                 f"{self.__postnummer} {self.__postort}"

        if self.__land != "Sverige":
            adress += f", {self.__land}"

        return adress

    def gatan(self):
        """Returnerar gatan i adressen"""
        return self.__gata

    def orten(self):
        """Returnerar numret i adressen"""
        return self.__postort

    def __eq__(self, other):
        """Jämför två adresser, returnerar True om de är identiska"""
        return self.__gata == other.__gata and \
               self.__nummer == other.__nummer and \
               self.__postnummer == other.__postnummer and \
               self.__postort == other.__postort and \
               self.__land == other.__land

def input_adress(prompt=""):
    """Låter användaren mata in data för en adress,
    returnerar ett Adress-objekt"""
    if prompt:
        print(prompt)

    gata = input("Gatans namn: ")
    nummer = input("Gatunummer: ")
    postnummer = input("Postnummer: ")
    postort = input("Postort: ")
    land = input("Land [blankt för Sverige]: ")
    if not land:
        land = "Sverige"

    return Adress(gata, nummer, postnummer, postort, land)


def main():
    """Testprogram"""
    daniels_kontor = Adress("Lindstedtsvägen", "5", "11428", "Stockholm")
    print(f"Daniel har sitt arbtesrum på adressen {daniels_kontor}.")
    print(f"Gatan är {daniels_kontor.gatan()}.")

    olles_kontor = Adress("Lindstedtsvägen", "3", "11428", "Stockholm")
    if daniels_kontor == olles_kontor:
        print("Daniel och Olle har arbetsrum på samma adress.")
    else:
        print("Daniel och Olle har inte arbetsrum på samma adress.")

if __name__ == "__main__":
    main()
