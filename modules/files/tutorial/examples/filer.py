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


def test_fil_finns():
    """Frågar om en fil som finns och en som inte gör det"""
    print("madicken.txt finns:", fil_finns("madicken.txt"))
    print("finns-inte.txt finns:", fil_finns("finns-inte.txt"))


def test_fragorna():
    """Frågar efter en fil att läsa och en att skriva till"""
    infilnamn = läs_infilnamn("Vilken fil ska vi läsa? ")
    utfilnamn = läs_utfilnamn("Vilken fil ska vi skriva till? ")
    print(f"Läser {infilnamn} och skriver {utfilnamn}.")


def test_alternativ():
    """Låter användaren välja mellan ord och bokstäver"""
    vad = läs_alternativ(
        "Vill du räkna ord eller bokstäver?",
        ["ord", "bokstäver"],
    )
    print(f"Valet blev {vad}.")


def test_fil():
    """Skriver en fil med två rader och läser tillbaka den"""
    skriv_fil("filprov.txt", "Ronja\nPippi\n")
    print(läs_fil("filprov.txt"), end="")


def tests():
    """Provkör filmodulens funktioner"""
    test_fil_finns()
    test_fragorna()
    test_alternativ()
    test_fil()


if __name__ == "__main__":
    tests()
