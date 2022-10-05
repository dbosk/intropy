"""Program om sökning i lista"""

def input_name():
    """Läser in ett namn från användaren och returnerar det i sökbar form."""
    return input("Ange namn: ").casefold()

def main():
    """Huvudprogrammet"""
    names = []

    print("Nu bygger vi upp namndatabasen. Ange namn. "
          "Ange tom sträng för att gå vidare.")

    name = input_name()
    while name:
        names.append(name)
        name = input_name()

    print("Nu ska vi söka bland namnen. Skriv namn för att söka. "
          "Skriv blankrad för att avsluta.")

    name = input_name()
    while name:
        if name in names:
            print(f"Hittade {name.capitalize()} i namndatabasen.")
        else:
            print(f"Hittade INTE {name.capitalize()} i namndatabasen")

        name = input_name()

if __name__ == "__main__":
    main()
