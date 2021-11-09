"""Ett program som immiterar `cowsay`"""

def dela_upp(text, bredd=30):
    """Delar upp text i rader, returnerar en lista med ett element per rad"""
    words = text.split(" ")
    words.reverse()

    rader = []
    rad = ""

    while words:
        if len(rad) > bredd or len(rad) + len(words[0]) > bredd:
            rader.append(rad)
            rad = ""

        rad += " " + words.pop()

    if rad:
        rader.append(rad)

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
    rader = dela_upp(text)
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
