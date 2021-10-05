"""Program som söker efter namn och ger antalet"""

# lista: [element, element, element, ...]
# dictionary: {nyckel: värde, nyckel: värde, ...}

def städa_antal(antal):
    """Tar antal läst från fil och returnerar en städad variant"""
    antal = antal.strip()
    antal = antal.replace(",", "")
    return antal

def läs_in_namn_antal(filnamn):
    """Läser in namn och antal och returnerar som en dictionary"""
    namnsök = {}
    with open(filnamn, "r") as fil:
        for namnrad in fil:
            # namnrad = "Ida;5"
            namn, antal = namnrad.split(";")
            namnsök[namn.strip()] = int(städa_antal(antal))

    return namnsök

def main():
    """Huvudprogram"""
    eftersökt_namn = input("Vilket namn är du intresserad av? ")
    efternamn = läs_in_namn_antal("efternamn-2020.csv")

    print(f"{eftersökt_namn} heter {efternamn[eftersökt_namn]} personer i efternamn!")

if __name__ == "__main__":
    main()
