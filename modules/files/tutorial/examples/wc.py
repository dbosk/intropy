"""Ett program som räknar ord och bokstäver i en fil"""

import csv

import filer


def räkna_ord(text):
    """Returnerar antalet förekomster av varje ord i text"""
    return räkna(text.split())


def räkna_bokstäver(text):
    """Returnerar antalet förekomster av varje tecken i text"""
    return räkna(text)


def räkna(delar):
    """Returnerar antalet förekomster av varje del i delar"""
    antal = {}
    for delen in delar:
        if delen in antal:
            antal[delen] += 1
        else:
            antal[delen] = 1
    return antal


def skriv_csv(filnamn, antal):
    """Skriver uppslagslistan antal som CSV till filnamn"""
    with open(filnamn, "w", newline="") as fil:
        skrivare = csv.writer(fil)
        for nyckel, värde in antal.items():
            skrivare.writerow([nyckel, värde])


def main():
    """Räknar ord eller bokstäver, skriver resultatet som CSV"""
    infilnamn = filer.läs_infilnamn(
        "Vilken fil ska vi analysera? ",
    )
    vad = filer.läs_alternativ(
        "Vill du räkna ord eller bokstäver?",
        ["ord", "bokstäver"],
    )
    utfilnamn = filer.läs_utfilnamn(
        "Till vilken fil ska vi skriva resultatet (CSV)? ",
    )
    text = filer.läs_fil(infilnamn)
    if vad == "ord":
        skriv_csv(utfilnamn, räkna_ord(text))
    else:
        skriv_csv(utfilnamn, räkna_bokstäver(text))
    print(f"Resultatet står nu i {utfilnamn}.")


if __name__ == "__main__":
    main()
