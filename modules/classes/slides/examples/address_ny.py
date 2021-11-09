"""Module med en klass för att hantera adresser"""

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
        if self.__land == "Sverige":
            return f"{self.__gata} {self.__nummer}, " + \
                f"{self.__postnummer} {self.__postort}"

        return f"{self.__gata} {self.__nummer}, " + \
               f"{self.__postnummer} {self.__postort}, " + \
               f"{self.__land}"

    def gatan(self):
        """Returnerar gatan i adressen"""
        return self.__gata

def main():
    """Testprogram"""
    daniels_kontor = Adress("Lindstedtsvägen", "5", "11428", "Stockholm")
    print(f"Daniel har sitt arbtesrum på adressen {daniels_kontor}.")
    print(f"Gatan är {daniels_kontor.gatan()}.")

if __name__ == "__main__":
    main()
