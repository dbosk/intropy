"""Olles inläsningsfunktion"""

def läs_in_talföljd(prompt):
    """Skriv ut prompt och låt användaren mata in ett tal,
    fortsätt tills att användaren matar in blankt."""
    tallista = []

    inläsning_klar = False
    while not inläsning_klar:
        tal = input(prompt)
        if tal == "":
            inläsning_klar=True
        else:
            tallista.append(int(tal))

    return tallista


