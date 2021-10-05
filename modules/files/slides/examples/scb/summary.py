"""Summerar statistik"""

import operator
import scb

#   lambda x: x[1]
#
# är en namnlös funktion som gör detsamma som
#
#   def plocka_ut_andra_elementet(x):
#       return x[1]
#
# Vilket i sin tur är detsamma som
#
#   operator.itemgetter(1)

def sortera_efter_antal(namn_antal_lista):
    """Tar en dictionary namn_antal_lista och
    returnerar en lista med (namn, antal)-tupler sorterade efter antal"""
    return sorted(namn_antal_lista.items(),
            key=lambda x: x[1], reverse=True)

# lista = [1, 2, 3, 4, 5]
# lista[0] == 1: plockar ut element 0.
# lista[0:2] == [1, 2]: skapar en lista med alla elementen 0, 1 (inte inkl 2)

def better_topp_10(namn_antal_lista):
    """Tar dictionary namn_antal_list och returnerar lista med de 10 vanligast 
    förekommande namnen"""
    sorterad = sortera_efter_antal(namn_antal_lista)
    return sorterad[0:10]

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
    # vi skapar en kopia, annars förstör vi originallistan
    kopia = namn_antal_lista.copy()
    topplista = []
    for topp in range(10):
        namn, antal = max_antal(kopia)
        topplista.append((namn, antal))
        kopia.pop(namn)

    return topplista

def skriv_ut_topplista(namntyp, lista):
    """Skriver ut en topp N-lista för namn av typen namntyp (str) och listan 
    lista med topplistan, längden på lista används för N"""

    print(f"Topp {len(lista)} kvinnliga tilltalsnamn:")
    for nummer, (namn, antal) in enumerate(lista):
        print(f"{nummer+1}: {namn}, {antal} personer")

def main():
    """Huvudprogram"""
    förnamn_män = scb.läs_in_namn_antal("förnamn-män-2020.csv")
    efternamn = scb.läs_in_namn_antal("efternamn-2020.csv")
    tilltalsnamn_kvinnor = scb.läs_in_namn_antal("tilltalsnamn-kvinnor-2020.csv")
    förnamn_kvinnor = scb.läs_in_namn_antal("förnamn-kvinnor-2020.csv")
    tilltalsnamn_män = scb.läs_in_namn_antal("tilltalsnamn-män-2020.csv")

    skriv_ut_topplista("kvinnliga tilltalsnamn",
        topp_10(tilltalsnamn_kvinnor))
    skriv_ut_topplista("Topp 10 kvinnliga tilltalsnamn:",
        better_topp_10(tilltalsnamn_kvinnor))

if __name__ == "__main__":
    main()
