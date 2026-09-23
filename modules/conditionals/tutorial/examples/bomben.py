"""Ett spel: svarar du fel på en fråga detonerar bomben."""


def detonera():
    """Skriver ut att bomben detonerar, och ger True."""
    print("BOM!")
    return True


def forsta_fragan():
    """Ställer den första frågan och ger True om bomben detonerade."""
    tal = float(input("Hur mycket är 1 + 1? "))
    if tal == 2:
        return detonera()

    return False


def andra_fragan():
    """Ställer den andra frågan och ger True om bomben detonerade."""
    tal = float(input("Säg ett tal mellan 0 och 1: "))
    if not (0 < tal and tal < 1):
        return detonera()

    return False


def tredje_fragan():
    """Ställer den tredje frågan och ger True om bomben detonerade."""
    tal = float(input("Säg ett tal mellan 1 och 2: "))
    if tal <= 1 or tal >= 2:
        return detonera()

    return False


def fjarde_fragan():
    """Ställer den fjärde frågan och ger True om bomben detonerade."""
    svar = input("9 < 10 or 1 < 2 and 2 < 1, sant eller falskt? ")
    if svar == "falskt":
        return detonera()

    return False


def femte_fragan():
    """Ställer den femte frågan och ger True om bomben detonerade."""
    alder = int(input("Nämn en bra ålder. [Ange ett tal] "))
    trad = "blå"
    if alder < 30:
        trad = "röd"
    elif alder > 20 and alder < 40:
        trad = "grön"
    elif not (alder < 65):
        trad = "röd"

    print(f"Du klipper den {trad} tråden.")
    if trad == "röd":
        return detonera()

    return False


def main():
    """Ställer frågorna i tur och ordning och säger hur det gick."""
    forsta = forsta_fragan()
    andra = andra_fragan()
    tredje = tredje_fragan()
    fjarde = fjarde_fragan()
    femte = femte_fragan()

    if not (forsta or andra or tredje or fjarde or femte):
        print("Du tog dig igenom utan att detonera bomben!")


main()
