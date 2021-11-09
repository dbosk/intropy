"""Ett program som analyserar bokstavsfrekvenser i en text och samma text i 
rövarspråket"""

import wc
import rövare

def skriv_CSV(filnamn, frekvens1, frekvens2):
    """Skriver ut två frekvenstabeller (frekvens1, frekvens2; dictionaries) 
    tillsammans till filen filnamn (sträng)"""
    with open(filnamn, "w") as utfil:
        for nyckel in frekvens1:
            utfil.write(f"{nyckel};")

            utfil.write(str(frekvens1[nyckel]))
            # Vi använder tabb ('\t') som separator då den inte förekommer i 
            # texten.
            utfil.write("\t")

            # vi behöver try då nyckel kanske inte finns i frekvens2
            try:
                utfil.write(str(frekvens2[nyckel]))
            except KeyError:
                # om nyckeln inte finns, finns det 0 av den.
                utfil.write("0")

            utfil.write("\n")

def main():
    """Huvudprogrammet"""
    textfilnamn = wc.läs_infilnamn("Ange fil att analysera: ")
    resultatfilnamn = wc.läs_utfilnamn("Ange fil för resultat (CSV-format): ")

    innehåll = wc.läs_fil(textfilnamn)
    innehåll_rövare = rövare.till_rövarspråket(innehåll)

    frekvenser = wc.räkna_bokstäver(innehåll)
    frekvenser_rövare = wc.räkna_bokstäver(innehåll_rövare)

    skriv_CSV(resultatfilnamn, frekvenser, frekvenser_rövare)

if __name__ == "__main__":
    main()
