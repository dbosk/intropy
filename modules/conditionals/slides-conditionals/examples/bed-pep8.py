"""Ett program för att beräkna sängegenskaper"""
import sys

def hardness():
    """Fråga om vikt och returnera en rekommendation."""
    try:
        weight = float(input("Hur mycket väger du (kg)? "))
    except ValueError as err:
        print(f"Din vikt måste anges med siffror: {err}")
        sys.exit()

    mattress = "special"

    if weight < 50:
        mattress = "mjuk"
    elif weight < 80:
        mattress = "mellan"
    elif weight < 120:
        mattress = "hård"

    return mattress

def main():
    """Huvudprogrammet"""
    try:
        length = int(input("Hur lång är du? "))
    except ValueError as err:
        print(f"Du måste ange din längd i hela centimeter med siffror: {err}")
        sys.exit()

    mattress = "mjuk"

    if length < 10:
        print("Ange längden i cm.")
        sys.exit()
    elif length < 130:
        print("Du kan använda en barnsäng.")
    elif length < 200:
        print("Du kan använda en vanlig vuxensäng, 200 cm.")
        mattress = hardness()
    elif length < 220:
        print("Du kan använda vår längre vuxensäng, 220 cm.")
        mattress = hardness()
    else:
        print("Tyvärr har vi inga sängar i lager för dig, "
            "du måste specialbeställa en.")
        sys.exit()

    if mattress == "special":
        print("Vi har ingen lämplig madrass för dig, "
              "men det går att specialbeställa.")
    else:
        print(f"Du trivs nog bäst på en {mattress} madrass.")

main()
