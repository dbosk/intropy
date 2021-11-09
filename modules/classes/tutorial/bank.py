"""En modul för bankrelaterade klasser"""

import adress

class Kund:
    """En klass för kunder"""

    def __init__(self, namn, personnummer, adress, telefon):
        """Skapar en bankkund: namn (sträng), personnummer (sträng), adress 
        (Adress-objekt), telefon (sträng)"""
        self.__namn = namn
        self.__personnummer = personnummer
        self.__adress = adress
        self.__telefon = telefon
        self.__konton = []

    # @property gör att vi inte behöver parenteserna:
    # `kund.namn` istället för `kund.namn()`
    @property
    def namn(self):
        """ Returnerar namnet"""
        return self.__namn

    def __str__(self):
        """Returnerar en strängrepresentation lämpligt för utskrift"""
        return self.namn

    @property
    def personnummer(self):
        """ Returnera personnummer """
        return self.__personnummer

    @property
    def adress(self):
        """ Returnera adress """
        return self.__adress

    def __repr__(self):
        """Returns unique representation"""
        return f"({self.namn}, {self.personnummer}"

    @property
    def telefon(self):
        """Returnerar telefonnumret"""
        return self.__telefon

    def lägg_till_konto(self, konto):
        """Lägger till konto till kundens konton"""
        self.__konton.append(konto)

    @property
    def konton(self):
        """Returnerar en lista med kundens konton"""
        return self.__konton.copy()

def input_kund(prompt=""):
    """Låter användaren mata in uppgifter för en kund,
    returnerar ett Kund-objekt"""
    if prompt:
        print(prompt)

    namn = input("Fullständigt namn: ")
    personnummer = input("Personnummer: ")
    adressen = adress.input_adress()
    telefon = input("Telefonnummer: ")

    return Kund(namn, personnummer, adressen, telefon)

class Konto:
    """Ett bankkonto"""

    def __init__(self, ägare, konto_id, saldo=0):
        """Skapar ett bankkonto:
            ägare är en Kund,
            konto_id är en textsträng,
            saldo är ett tal (int eller float, default 0)"""
        self.__owner = ägare
        self.__account_id = konto_id
        self.__amount = saldo
        self.__lösneord = ""

    @property
    def ägare(self):
        """Returnerar ägaren"""
        return self.__owner

    @property
    def kontonr(self):
        """Returnerar kontonumret"""
        return self.__account_id

    def __str__(self):
        return str(self.kontonr)

    def sätt_in(self, summa):
        """Sätter in en summa pengar på kontot"""
        self.__amount += summa

    @property
    def saldo(self):
        """Returnerar kontots saldo"""
        return self.__amount

    def ta_ut(self, summa):
        """Tar ut en summa pengar från kontot,
        kastar ett särfall ValueError vid för lite täckning på kontot"""
        if self.__amount - summa < 0:
            raise ValueError(f"kontot saknar täckning, "
                             f"saldot {self.__amount} är mindre än "
                             f"uttaget {summa}")

        self.__amount -= summa

    def sätt_lösenord(self, lösenord):
        """Sätter ett lösenord för kontot"""
        self.__lösenord = lösenord

    def korrekt_lösenord(self, lösenord):
        """Returnerar True om lösenordet matchar"""
        return self.__lösenord == lösenord

class Bank:
    """Klass för en bank"""

    def __init__(self, namn):
        """Skapa en bank med namnet namn"""
        self.__namn = namn
        self.__kunder = {}
        self.__konton = {}
        self.__nuvarande_kontonr = 0

    def __str__(self):
        """Returnerar en strängformaterat representation"""
        return self.__namn

    def registrera_kund(self, kund):
        """Registrera kunden kund (Kund-objekt) som kund i banken.
        kund får inte vara registrerad, då kastas ett KeyError."""
        if kund.personnummer in self.__kunder:
            raise KeyError(f"{kund} är redan registrerad som kund.")

        self.__kunder[kund.personnummer] = kund

    def hämta_kund(self, personnummer):
        """Returnerar kund med personnummer personnummer"""
        return self.__kunder[personnummer]

    def skapa_konto(self, personnummer):
        """Skapa ett nytt konto åt kunden med personnumret personnummer, 
        returnerar det nya kontot"""
        kund = self.hämta_kund(personnummer)
        konto = Konto(kund, self.__nuvarande_kontonr+1)
        self.__konton[konto.kontonr] = konto
        self.__nuvarande_kontonr += 1
        kund.lägg_till_konto(konto)
        return konto

    def hämta_konto(self, kontonr):
        """Returnerar Konto-objektet med kontonumret kontonr,
        kastar KeyError om kontonumret inte finns"""
        return self.__konton[int(kontonr)]


def main():
    """Testprogram"""
    kund = Kund("Ada Adamsdotter", "1999-01-01-xxxx",
                adress.Adress("Stora vägen", "1", "12345", "Orten"),
                "070-1234567")
    konto = Konto(kund, "123-456-789")

    print(f"{konto.ägare} har {konto.saldo} kr på {konto}")
    konto.sätt_in(500)
    print(f"{konto.ägare} har {konto.saldo} kr på {konto}")
    konto.ta_ut(200)
    print(f"{konto.ägare} har {konto.saldo} kr på {konto}")
    try:
        konto.ta_ut(500)
    except ValueError as err:
        print(err)
    print(f"{konto.ägare} har {konto.saldo} kr på {konto}")

if __name__ == "__main__":
    main()
