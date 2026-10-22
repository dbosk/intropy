"""Ett program som översätter en fil till och från rövarspråket"""

import filer

KONSONANTER = "bcdfghjklmnpqrstvwxz"


def till_rövarspråket(text):
    """Returnerar text översatt till rövarspråket"""
    rövartext = ""
    for bokstav in text:
        rövartext += bokstav
        if bokstav.lower() in KONSONANTER:
            rövartext += "o" + bokstav.lower()
    return rövartext


def från_rövarspråket(rövartext):
    """Returnerar rövartext översatt till vanlig text"""
    text = ""
    i = 0
    while i < len(rövartext):
        bokstav = rövartext[i]
        text += bokstav
        if bokstav.lower() in KONSONANTER:
            väntat = "o" + bokstav.lower()
            if rövartext[i + 1 : i + 3] != väntat:
                fel = f"{bokstav} följs inte av {väntat}"
                raise ValueError(fel)
            i += 3
        else:
            i += 1
    return text


def main():
    """Översätter en fil till eller från rövarspråket"""
    riktning = filer.läs_alternativ(
        "Vill du översätta till eller från rövarspråket?",
        ["till", "från"],
    )
    filnamn = filer.läs_infilnamn("Vilken fil ska vi översätta? ")
    text = filer.läs_fil(filnamn)
    try:
        if riktning == "till":
            filer.skriv_fil(filnamn, till_rövarspråket(text))
        else:
            filer.skriv_fil(filnamn, från_rövarspråket(text))
    except ValueError as fel:
        print(f"Filen går inte att översätta: {fel}.")


if __name__ == "__main__":
    main()
