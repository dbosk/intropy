"""
Denna modul innehåller funktioner som gör det
enkelt att bygga frågesportprogram.
"""


def ställ_fråga(fråga, rätt_svar):
    """
    Ställer en fråga och rättar användarens svar.
    Returnerar sant (True) om användaren svarade rätt,
    annars falskt (False).
    """
    print(fråga)
    användarens_svar = input("Svar: ")

    if användarens_svar == rätt_svar:
        print("Det var rätt svar!")
    else:
        print(f"Det var fel svar! Rätt svar är {rätt_svar}.")


def huvudfunktion():
    """
    Huvudprogrammet låter användaren spela ett
    frågesportspel som använder modulens funktioner.
    """
    ställ_fråga("Vad heter huvudstaden i Sverige?", "Stockholm")
    ställ_fråga("Vad heter huvudstaden i Norge?", "Oslo")
    ställ_fråga("Hur mycket är 1432 + 234?", "1666")


if __name__ == "__main__":
    huvudfunktion()
