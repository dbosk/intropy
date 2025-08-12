"""
Denna modul innehåller funktioner som gör det
enkelt att översätta till och från rövarspråket.
"""

KONSONANTER = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
VOKALER = "aeiouyåäöAEIOUYÅÄÖ"
MENYVAL = "Vill du översätta till eller från rövarspråket " "eller avsluta? (t/f/a) "


def till_rövarspråket(text):
    """
    Översätt `text` till rövarspråket.
    Returnera översättningen.
    """
    översättning = ""
    for tecken in text:
        if tecken in KONSONANTER:
            översättning += tecken + "o" + tecken.lower()
        else:
            översättning += tecken

    return översättning


def från_rövarspråket(rövartext):
    """
    Översätt `rövartext` från rövarspråket.
    Returnera översättningen.
    """
    översättning = ""
    index = 0
    while index < len(rövartext):
        tecken = rövartext[index]
        if tecken in KONSONANTER:
            if (
                index + 2 < len(rövartext)
                and rövartext[index + 1] == "o"
                and rövartext[index + 2] == tecken.lower()
            ):
                översättning += tecken
                index += 2
            else:
                översättning += tecken
        else:
            översättning += tecken
        index += 1
    return översättning


def huvudfunktion():
    """
    Huvudprogrammet läser in en sträng från användaren
    och översätter den till rövarspråket.
    """
    while (val := input(MENYVAL)) != "a":
        if val == "t":
            text = input("Skriv in texten du vill översätta: ")
            print("Översättning:", till_rövarspråket(text))
        elif val == "f":
            text = input("Skriv in texten du vill översätta: ")
            print("Översättning:", från_rövarspråket(text))
        else:
            print("Felaktigt val, försök igen.")


if __name__ == "__main__":
    huvudfunktion()
