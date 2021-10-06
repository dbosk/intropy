"""Program som räknar ord och bokstäver"""

def räkna_ord(filnamn):
    """Returnerar en dictionary med orden i filen filnamn som nycklar och 
    antalet gånger de förekommer som värden"""

    ord_antal = {}

    with open(filnamn, "r") as infil:
        for rad in infil:
            rad = rad.strip()
            for ett_ord in rad.split(" "):
                # ett väldigt pythoniskt sätt att göra detta på (try-except)
                try:
                    ord_antal[ett_ord] += 1
                except KeyError:
                    ord_antal[ett_ord] = 1

    return ord_antal

def räkna_bokstäver(filnamn):
    """Returnerar en dictionary med bokstäverna i filen filnamn som nycklar
    och antalet gånger de förekommer som värden"""

    bokstäver_antal = {}

    with open(filnamn, "r") as infil:
        for rad in infil:
            rad = rad.strip()
            for bokstav in rad:
                # mindre pythoniskt sätt, men funkar också.
                if not bokstav in ord_antal:
                    ord_antal[bokstav] = 1
                else:
                    ord_antal[bokstav] += 1

    return bokstäver_antal

def fil_finns(filnamn):
    """Returnerar sant om filen finns, falskt annars"""
    try:
        with open(filnamn, "r") as fil:
            pass
        return True
    except FileNotFoundError:
        return False

def läs_infilnamn(prompt=""):
    """Låter användaren mata in ett filnamn, returnerar filnamnet när 
    användaren matat in ett namn för vilket filen finns"""
    infilnamn = input(prompt)

    while not fil_finns(infilnamn):
        print(f"Finns ingen fil som heter {infilnamn}, försök igen.")
        infilnamn = input(prompt)

    return infilnamn

def läs_utfilnamn(prompt=""):
    """Låter användaren mata in ett filnamn, returnerar filnamnet när 
    användaren matat in ett namn för vilket det inte finns någon fil."""
    utfilnamn = input(prompt)

    while fil_finns(utfilnamn):
        print(f"Det finns redan en fil som heter {utfilnamn}, försök igen.")
        utfilnamn = input(prompt)

    return utfilnamn

def läs_alternativ(prompt, alternativ):
    """Presenterar användaren med alternativen i listan alternativ,
    returnerar vilket alternativ användaren väljer"""
    print(prompt)

    valet = input(f"Ange ett av alternativen {alternativ}: ")
    while valet not in alternativ:
        print(f"Tyvärr är {valet} inte ett av alternativen.")
        valet = input(f"Ange ett av alternativen {alternativ}: ")

    return valet

def skriv_CSV(filnamn, uppslagslista):
    """Skriver uppslagslistan till en fil. Använder CSV-format: nyckel;värde"""
    with open(filnamn, "w") as utfil:
        for nyckel, värde in uppslagslista.items():
            # vi använder tab (\t) som separator då komma och semikolon
            # används i texten
            utfil.write(f"{nyckel}\t{värde}\n")

def main():
    """Huvudprogrammet"""
    infilnamn = läs_infilnamn("Vilken fil ska vi analysera? ")

    att_analysera = läs_alternativ(
            "Vill du analysera antalet ord eller bokstäver?",
            ["ord", "bokstäver"])

    utfilnamn = läs_utfilnamn("Till vilken fil ska vi skriva "
            "resultatet (CSV-format)? ")

    if att_analysera == "ord":
        skriv_CSV(utfilnamn, räkna_ord(infilnamn))
    else:
        skriv_CSV(utfilnamn, räkna_bokstäver(infilnamn))

if __name__ == "__main__":
    main()
