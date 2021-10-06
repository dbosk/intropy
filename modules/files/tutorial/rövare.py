"""Ett program som översätter till och från rövarspråket"""

import wc

VOKALER = "aouåeiyäö"
KONSONANTER = "bcdfghjklmnpqrstvwxz"

def till_rövarspråket(text):
    """Läser texten text (sträng) och returnerar den översatt till 
    rövarspråket"""
    rövartext = ""

    for bokstav in text:
        if bokstav.lower() in KONSONANTER:
            rövartext += f"{bokstav}o{bokstav.lower()}"
        else:
            rövartext += bokstav

    return rövartext

def från_rövarspråket(rövartext):
    """Läser texten text (sträng) och översätter den från rövarspråk till 
    vanligt språk"""
    vanlig_text = ""

    # vänd för att använda pop för första bokstaven
    rövarlista = list(rövartext)
    rövarlista.reverse()

    while rövarlista:
        bokstav = rövarlista.pop()
        if bokstav.lower() in KONSONANTER:
            if rövarlista and rövarlista.pop() != "o":
                raise ValueError(
                    f"{bokstav} måste följas av 'o{bokstav.lower()}'")
            if rövarlista and rövarlista.pop() != bokstav.lower():
                raise ValueError(
                    f"{bokstav} måste följas av 'o{bokstav.lower()}'")

        vanlig_text += bokstav

    return vanlig_text

def skriv_fil(filnamn, text):
    """Skriver text till filen med namn filnamn"""
    with open(filnamn, "w") as utfil:
        utfil.write(text)

def main():
    """Huvudprogrammet"""
    till_eller_från = wc.läs_alternativ(
        "Vill du översätta till eller från rövarspråket?",
        ["till", "från"])
    filnamn = wc.läs_infilnamn("Ange fil att översätta: ")

    # Nu har vi filens innehåll i minnet och filen är stängd,
    # då kan vi skriva över den senare.
    innehåll = läs_fil(filnamn)

    try:
        if till_eller_från == "till":
            nytt_innehåll = till_rövarspråket(innehåll)
        else:
            nytt_innehåll = från_rövarspråket(innehåll)

        # Om något går fel skriver vi inte över filen.
        skriv_fil(filnamn, nytt_innehåll)
    except ValueError as err:
        print(f"Tyvärr, filen går inte att översätta: {err}.")


if __name__ == "__main__":
    main()
