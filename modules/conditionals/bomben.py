"""Detta är ett litet spel där man ska undvika att få bomben att explodera

Användaren får frågor att besvara. Men då vi tycker om att smälla av bomben kan 
vi även smälla av den vid rätt svar. Därför måste användaren läsa källkoden för 
att undvika att detonera bomben."""

import bomb
import random

def välkommen():
    """Skriv ut en välkomstskärm för spelet"""
    print("""
            Hej och välkommen till spelet Bomben!

Du kommer att få frågor. Om du svarar "fel" kommer bomben att explodera. "Fel" 
är inte alltid samma som fel. Du måste läsa källkoden för att de vad rätt svar 
blir, exempelvis kan du få frågan "vad är 1+1?" och då kanske du måste svara 3 
för att undvika att detonera bomben.

            Ha så kul!
        """)

def krångliga_if():
    """Några frågor med nästlade if-satser"""
    flyttal = float(input("Säg ett tal mellan 0 och 1: "))
    if not(0 < flyttal and flyttal < 1):
        bomb.detonera()

    flyttal = float(input("Säg ett tal mellan 1 och 2: "))
    if 1 > flyttal or flyttal > 2:
        bomb.detonera()

    print("1 < 2 and 2 < 1 or 9 < 10, sant eller falskt?", end=" ")
    sant_eller_falskt = input()
    if sant_eller_falskt == "falskt":
        bomb.detonera()

    ålder = int(input("Nämn en bra ålder? [Ange ett tal] "))
    if ålder < 30:
        bomb.detonera()
    elif ålder > 20 and ålder < 40:
        bomb.detonera()
    elif not(ålder < 65):
        bomb.detonera()

def rekursion(n):
    """Några frågor som använder rekursion"""
    if n < 0:
        bomb.detonera()
    elif n == 0:
        return

    slumptal = random.randint(-5, 5)
    tal = int(input(f"Jag säger {slumptal}, vilket tal säger du? "))

    rekursion(n-1 + slumptal - tal)

def main():
    """Kör igång bombenspelet"""
    välkommen()

    if 2 == int(input("Hur mycket är 1+1? ")):
        bomb.detonera()

    krångliga_if()

    print("""
Grattis, du tog dig igenom de krångliga if-satserna! Nu ska jag finta bort dig 
med lite rekursion!
        """)

    rekursion(5)

    print("""

    Stort grattis, du tog dig igenom utan att detonera bomben!

Ditt pris blir att du får välja om du vill smälla av bomben på säkert avsåtnd.
""")
    detonera = input("Detonera, ja eller nej? ")
    if detonera == "ja":
        bomb.detonera()
    else:
        print("Så tråkigt ...")

main()
