def skriv_ut(meddelande, antal_gånger):
    """Skriver ut meddelande antal_gånger antal gånger"""
    if antal_gånger <= 0:
        return

    print(meddelande)
    skriv_ut(meddelande, antal_gånger-1)

skriv_ut("Hej", 2000)
