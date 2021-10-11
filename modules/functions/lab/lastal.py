"""Modul med funktioner för att läsa in och testa tal"""

def är_decimaltal(sträng):
    """Returnerar True om sträng är ett decimaltal"""
    try:
        float(sträng)
        return True
    except ValueError:
        return False

def är_heltal(sträng):
    """Returnerar True om sträng är ett heltal"""
    try:
        int(sträng)
        return True
    except ValueError:
        return False

def läs_decimaltal(prompt, variabelnamn=""):
    """Returnerar ett decimaltal från användaren, frågar om när användaren
    matar in fel. Skriver ut prompt först och använder variabelnamn vid
    inmatning."""
    print(prompt)
    sträng = input(variabelnamn+": ")
    while not är_decimaltal(sträng):
        print(variabelnamn, "måste vara ett decimaltal. Prova igen.")
        sträng = input(variabelnamn+": ")
    return float(sträng)

def läs_heltal(prompt, variabelnamn=""):
    """Returnerar ett heltal från användaren, frågar om när användaren matar
    in fel. Skriver ut prompt först och använder variabelnamn vid inmatning."""
    print(prompt)
    sträng = input(variabelnamn+": ")
    talet_ok = False
    while not talet_ok:
        if är_heltal(sträng):
            if int(sträng) > 0:
                return int(sträng)
        print(variabelnamn, "måste vara ett heltal större än noll. Prova igen.")
        sträng = input(variabelnamn+": ")
