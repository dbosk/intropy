"""Klass för en person"""

class Person:
    """En person"""

    def __init__(self, förnamn, efternamn, födelseår, adress, telefon):
        """Skapar en person utifrån argumenten ... allt är strängar"""
        self.__förnamn = förnamn
        self.__efternamn = efternamn
        self.__födelseår = födelseår
        self.__adress = adress
        self.__telefon = telefon

    def namn(self):
        """Returnerar namnet"""
        return self.__förnamn + " " + self.__efternamn

    def byt_namn(self, nytt_namn):
        """Byter för- och efternamn till nytt_namn"""
        namndelar = nytt_namn.split(" ")
        self.__efternamn = namndelar[-1]
        self.__förnamn = " ".join(namndelar[:-1])

    def födelseår(self):
        """Returnerar födelseåret"""
        return self.__födelseår

    def adress(self):
        """Returnerar adressen"""
        return self.__adress

    def telefon(self):
        """Returnerar telefonnumret"""
        return self.__telefon

    def __str__(self):
        """Returnerar objektet i strängformat"""
        return self.namn()

    def __repr__(self):
        """Returnerar en unik representation i strängform"""
        return f"({self.namn()}, {self.födelseår()}, {self.adress()}, {self.telefon()})"

    def __int__(self):
        return int(self.__födelseår)

    def __lt__(self, other):
        """Jämförelse <: returnerar True om self är yngre än other, False annars"""
        return int(self.födelseår()) > int(other.födelseår())

def main():
    """Testprogram"""
    telefonbok = {
            "ada": Person("Ada", "Bedasdotter", "1990",
                          "Kiruna", "070-1234567"),
            "beda": Person("Beda", "Bertilsdotter", "1970",
                           "Malmö", "071-1234567")
            }

    namn = input("Vem söker du? ")
    person = telefonbok[namn]

    print(f"person = {person}")
    print(f"person heter {person.namn()}")
    print(f"{person.namn()} har telefonnumret {person.telefon()} och "
          f"bor på adressen {person.adress()}.")

    print(telefonbok)

    person.byt_namn("Cesil Cesarsson")
    print(person)

    ada = telefonbok["ada"]
    beda = telefonbok["beda"]

    if ada > beda:
        print(f"{beda} är yngre än {ada}.")
    else:
        print(f"{ada} är yngre än {beda}.")

    lista = [beda, ada]
    print(lista)
    lista.sort()
    print(lista)

if __name__ == "__main__":
    main()
