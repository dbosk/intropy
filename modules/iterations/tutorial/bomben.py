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

def kommentera_fel():
    """Returnerar en slumpvis vald lagom elak kommentar"""
    slumptal = random.randint(0, 5)

    if slumptal == 0:
        return "Ajdå, det var fel!"
    elif slumptal == 1:
        return "Detta bådar inte gott!"
    elif slumptal == 2:
        return "Du är inte dum, du har bara lite otur när du tänker!"
    elif slumptal == 3:
        return "Hur tänkte du nu?"
    elif slumptal == 4:
        return "Men varför?"

    return "Suck."

def input_typ(typ, prompt=""):
    """Utökad version av input som har inbyggd typkonvertering,
    returnerar när korrekt typ typ har matats in."""
    while True:
        try:
            inmatning = typ(input(prompt))
            return inmatning
        except ValueError as err:
            print(kommentera_fel())

def ge_försök(antal, fråga, svar):
    """Ger användaren antal försök att besvara fråga med rätt svar,
    användarens svar typkonverteras till typ innan jämförelse;
    returnerar True om användaren svarar svar, False annars."""
    for försök in range(1, antal+1):
        if svar == input_typ(type(svar), fråga):
            return True
        print(kommentera_fel())

    print("Slut på försök, du var ju ingen höjdare på det här.")
    return False

def fråga_oändligt(fråga, svar):
    """Ställer frågan fråga till användaren och avslutar inte förrän användaren 
    ger korrekt svar"""
    inmatning = input_typ(type(svar), fråga)
    while svar != inmatning:
        print(kommentera_fel())
        inmatning = input_typ(type(svar), fråga)

def krångliga_if():
    """Några frågor med nästlade if-satser"""
    flyttal = input_typ(float, "Säg ett tal mellan 0 och 1: ")
    if not(0 < flyttal and flyttal < 1):
        bomb.detonera()

    flyttal = input_typ(float, "Säg ett tal mellan 1 och 2: ")
    if 1 > flyttal or flyttal > 2:
        bomb.detonera()

    print("1 < 2 and 2 < 1 or 9 < 10, ", end=" ")
    # den här är vansinnigt klurig, testa att typkonvertera strängar till bool
    if input_typ(bool, "True eller False? "):
        bomb.detonera()

    ålder = input_typ(int, "Nämn en bra ålder? [Ange ett tal] ")
    if ålder < 30:
        bomb.detonera()
    elif ålder > 20 and ålder < 40:
        bomb.detonera()
    elif not(ålder < 65):
        bomb.detonera()

def main():
    """Kör igång bombenspelet"""
    välkommen()

    if 2 == input_typ(int, "Hur mycket är 1+1? "):
        bomb.detonera()

    krångliga_if()

    print("""
Grattis, du tog dig igenom de krångliga if-satserna! Men nu blir det svårare.
        """)

    if ge_försök(3,
            "Gissa vilket tal jag tänker på: ",
            random.randint(1, 10)):
        print("Imponerande, du gissade rätt!")
    else:
        print("Du hade tre försök, "
              "som straff får du ta rundan med krångliga if igen.")
        krångliga_if()

    fråga_oändligt("Vem är bäst på att programmera? ", "Jag")
    print("Precis, det tar sig ;-)")

    detonera = input("Vill du detonera bomben, ja eller nej? ")
    if detonera == "ja":
        bomb.detonera()
    else:
        print("Så tråkigt ...")

main()
