"""Lösning som skriver ut hej femtio gånger"""

def skriv_ut(meddelande, antal_gånger):
    """Skriver ut meddelande, antal_gånger gånger"""
    if antal_gånger <= 0:
        return

    print(meddelande)
    skriv_ut(meddelande, antal_gånger-1)

skriv_ut("hej", 2000)
