"""Ett kort biblioteksexempel"""

import csv

class Bok:
    """En klass som representerar en bok"""
    def __init__(self, titel, författare, år, isbn):
        """Skapar ett bokobjekt"""
        self.titel = titel
        self.författare = författare
        self.år = år
        self.isbn = isbn
        self.utlånad = False

    def __str__(self):
        return f"{self.titel} av {self.författare}"

    def __repr__(self):
        return f"{self.titel} av {self.författare} utgiven {self.år}"

    def låna(self):
        """Markerar boken som lånad"""
        if self.utlånad:
            raise Exception("Boken är redan utlånad!")
        self.utlånad = True

    def lämna_tillbaka(self):
        """Markerar boken som återlämnad"""
        if not self.utlånad:
            raise Exception("Boken är inte lånad, kan inte lämna tillbaka då")
        self.utlånad = False

def skriv_boktabell(lista_med_böcker):
    """Skriver ut lista_med_böcker som tabell"""
    # {'text':25s} gör att strängen 'text' skrivs ut som sträng (s) med minst 
    # 25 tecken i bredd.
    print(f"{'Titel':25s}{'Författare':20s}{'År':5s}{'ISBN':15s}")
    for bok in lista_med_böcker:
        print(f"{bok.titel:25s}{bok.författare:20s}{bok.år:5s}{bok.isbn:15s}")

def main():
    """Testprogram"""
    # Testa att skapa böcker
    sor = Bok("Sagan om ringen", "JRR Tolkien", 1920, "973-xxxxxxxxx")
    sodtt = Bok("Sagan om de två tornen", "JRR Tolkien", 1925, "973-xxxxx")
    sokå = Bok("Sagan om konungens återkomst", "JRR Tolkien", 1930, "973-X")

    # Skriv ut info om dem (testar __str__)
    print(f"{sor.titel} av {sor.författare}")
    print(sodtt)
    print(sokå)

    # Lägg i lista och skriv ut (testar __repr__)
    boklista = [sor, sodtt, sokå]
    print(boklista)

    # Krångligt med dict istället för klass
    bokdict = {"Sagan om ringen": ("JRR Tolkien", 1920, "973-xxxxx")}
    print(bokdict["Sagan om ringen"][0])
    print(sor.författare)

    # Testa utlåning
    print(f"{sor} är utlånad: {sor.utlånad}")
    sor.låna()
    print(f"{sor} är utlånad: {sor.utlånad}")
    try:
        sor.låna()
    except Exception as err:
        print(err)

    sor.lämna_tillbaka()
    print(f"{sor} är utlånad: {sor.utlånad}")

    # Läs in böcker från filer
    print("Eget filformat")
    ny_boklista = []
    with open("böcker.txt", "r") as bokfil:
        peek = bokfil.readline()
        while peek != "":
            titel = peek
            författare = bokfil.readline()
            år = bokfil.readline()
            isbn = bokfil.readline()
            ny_boklista.append(Bok(titel, författare, år, isbn))

            peek = bokfil.readline()

    print(ny_boklista)

    print("CSV som filformat")
    en_till_boklista = []
    with open("böcker.csv", "r") as bokcsv:
        böcker = csv.reader(bokcsv)
        for bok in böcker:
            en_till_boklista.append(Bok(bok[0], bok[1], bok[2], bok[3]))

    print(en_till_boklista)

    # Sortera listan och skriv ut den
    sorterade_böcker_titel = sorted(en_till_boklista,
            key=lambda x: x.titel)
    skriv_boktabell(sorterade_böcker_titel)

    sorterade_böcker_år = sorted(en_till_boklista,
            key=lambda x: x.år)
    skriv_boktabell(sorterade_böcker_år)

    # samma sak som lambda x: x.författare
    def hämta_författare(x):
        return x.författare

    sorterade_böcker_författare = sorted(en_till_boklista,
            key=hämta_författare)
    skriv_boktabell(sorterade_böcker_författare)


if __name__ == "__main__":
    main()
