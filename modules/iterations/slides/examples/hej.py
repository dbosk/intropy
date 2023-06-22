"""Program som skriver ut hej 50 gånger"""

def hej_for():
    """Skriver ut hej 50 gånger med en for-loop"""
    for gång in range(50):
        print(f"hej {gång}!")

def hej_while():
    """Skriver ut hej 50 gånger med en while-loop"""
    antal = 50
    while antal > 0:
        print(f"hej {antal}!")
        # antal = antal - 1
        antal -= 1

def hej_while_alt():
    """En alternativ version av hej_while"""
    antal = 0
    while antal < 50:
        print(f"hej {antal}!")
        antal += 1


if __name__ == "__main__":
    hej_for()
