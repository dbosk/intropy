"""Ett program som immiterar `cowsay`"""

def dela_upp_mening(mening, bredd=30):
    """Delar upp mening i rader, returnerar en lista med ett element per rad 
    som då är lagom långa"""

    words = mening.split()
    # omvänd ordning så att vi kan använda while och pop nedan
    words.reverse()

    rader = []
    rad = ""

    while words:
        if len(rad) > bredd or len(rad) + len(words[-1]) > bredd:
            rader.append(rad)
            rad = ""

        # Vi vill inte ha ett blanksteg i början av en ny rad
        if rad:
            rad += " " + words.pop().strip()
        else:
            rad = words.pop().strip()

    # vi vill alltid lägga till rad, utifall att det är en blankrad
    rader.append(rad)

    return rader

def dela_upp_stycken(text, bredd=30):
    """Delar upp en text i stycken, formaterar därefter enskilda meningar;
    returnerar en lista med lagom långa rader (inkl blankrader)"""

    meningar = text.split("\n")
    rader = []

    for mening in meningar:
        rader += dela_upp_mening(mening, bredd)

    return rader

def maxlängd(lista):
    """Returnerar längden för det längsta elementet i listan"""
    längd = 0
    for element in lista:
        ny_längd = len(element)
        if ny_längd > längd:
            längd = ny_längd

    return längd

def pratbubbla(text):
    """Skriver ut text i en pratbubbla"""
    rader = dela_upp_stycken(text)
    bredd = maxlängd(rader)

    print(" ", end="")
    for _ in range(bredd+2):
        print("-", end="")
    print()
    for rad in rader:
        print(f"| {rad:{bredd}s} |")
    print(" ", end="")
    for _ in range(bredd+2):
        print("-", end="")

def ko():
    """Skriver ut en ko"""
    print("""
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\ 
                ||----w |
                ||     ||""")

def cowsay(text):
    """Skriver ut text i en pratbubbla från en ko"""
    pratbubbla(text)
    ko()

def main():
    cowsay("Smaka på den här utmaningen! Fast så svår är den inte.")

if __name__ == "__main__":
    main()
