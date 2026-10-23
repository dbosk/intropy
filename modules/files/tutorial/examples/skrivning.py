"""Skriver en rad till en fil och räknar tecknen i den två gånger"""

FILNAMN = "ronja.txt"


def antal_tecken(filnamn):
    """Returnerar antalet tecken i filen filnamn"""
    with open(filnamn, "r") as fil:
        return len(fil.read())


def main():
    """Skriver en rad och räknar tecknen i filen två gånger"""
    fil = open(FILNAMN, "w")
    fil.write("Ronja\n")
    print("Första räkningen:", antal_tecken(FILNAMN))
    fil.close()
    print("Andra räkningen:", antal_tecken(FILNAMN))


if __name__ == "__main__":
    main()
