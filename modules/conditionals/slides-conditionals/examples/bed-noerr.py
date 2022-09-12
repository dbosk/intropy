import sys

def hardness():
    """Fråga om vikt och returnera en rekommendation."""
    weight = float(input("Hur mycket väger du (kg)? "))

    if weight < 50:
        return "mjuk"
    elif weight < 80:
        return "mellan"
    elif weight < 120:
        return "hård"
    else:
        return "special"

def main():
    """Huvudprogrammet"""
    length = int(input("Hur lång är du? "))

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
