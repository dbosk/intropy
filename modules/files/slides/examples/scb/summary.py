"""Summerar statistik"""

import scb

def max_antal(namn_antal_lista):
    """Returnerar det namn och antal som har störst antal"""
    max_antal = 0
    max_namn = ""

    for namn, antal in namn_antal_lista.items():
        if antal > max_antal:
            max_antal = antal
            max_namn = namn

    return max_namn, max_antal

def topp_10(namn_antal_lista):
    """Tar dictionary namn_antal_list och returnerar lista med de 10 vanligast förekommande namnen"""
    topplista = []
    for topp in range(10):
        namn, antal = max_antal(namn_antal_lista)
        topplista.append((namn, antal))
        namn_antal_lista.pop(namn)

    return topplista

def main():
    """Huvudprogram"""
    förnamn_män = scb.läs_in_namn_antal("förnamn-män-2020.csv")
    efternamn = scb.läs_in_namn_antal("efternamn-2020.csv")
    tilltalsnamn_kvinnor = scb.läs_in_namn_antal("tilltalsnamn-kvinnor-2020.csv")
    förnamn_kvinnor = scb.läs_in_namn_antal("förnamn-kvinnor-2020.csv")
    tilltalsnamn_män = scb.läs_in_namn_antal("tilltalsnamn-män-2020.csv")

    print("Topp 10 kvinnliga tilltalsnamn:")
    print(topp_10(tilltalsnamn_kvinnor))

if __name__ == "__main__":
    main()
