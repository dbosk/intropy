"""Funktioner som svarar på programmens frågor om filer"""


def läs_infilnamn(prompt):
    """Frågar tills filen finns, returnerar filnamnet"""
    while not fil_finns(filnamn := input(prompt)):
        print(f"Filen {filnamn} finns inte. Försök igen.")
    return filnamn


def läs_utfilnamn(prompt):
    """Frågar tills filen inte finns, returnerar filnamnet"""
    while fil_finns(filnamn := input(prompt)):
        print(f"Filen {filnamn} finns redan. Försök igen.")
    return filnamn


def fil_finns(filnamn):
    """Returnerar True om det finns en fil som heter filnamn"""
    try:
        with open(filnamn, "r"):
            pass
    except FileNotFoundError:
        return False
    return True


def läs_alternativ(prompt, alternativ):
    """Frågar tills svaret står i alternativ, returnerar svaret"""
    print(prompt)
    fråga = f"Ange ett av alternativen {alternativ}: "
    while (valet := input(fråga)) not in alternativ:
        print(f"Tyvärr är {valet} inte ett av alternativen.")
    return valet


def läs_fil(filnamn):
    """Returnerar hela innehållet i filen filnamn som en sträng"""
    with open(filnamn, "r") as fil:
        return fil.read()


def skriv_fil(filnamn, text):
    """Skriver text till filen filnamn, som töms först"""
    with open(filnamn, "w") as fil:
        fil.write(text)


def tests():
    """Provkör filmodulens funktioner"""
    print("madicken.txt finns:", fil_finns("madicken.txt"))
    print("finns-inte.txt finns:", fil_finns("finns-inte.txt"))
    infilnamn = läs_infilnamn("Vilken fil ska vi läsa? ")
    utfilnamn = läs_utfilnamn("Vilken fil ska vi skriva till? ")
    print(f"Läser {infilnamn} och skriver {utfilnamn}.")
    vad = läs_alternativ(
        "Vill du räkna ord eller bokstäver?",
        ["ord", "bokstäver"],
    )
    print(f"Valet blev {vad}.")
    skriv_fil("filprov.txt", "Ronja\nPippi\n")
    print(läs_fil("filprov.txt"), end="")


if __name__ == "__main__":
    tests()
