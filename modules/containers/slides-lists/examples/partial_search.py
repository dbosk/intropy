"""Program om sökning i lista"""

def input_name():
    """Läser in ett namn från användaren och returnerar det i sökbar form."""
    return input("Ange namn: ").casefold()

def partial_search(substring, strings):
    """Söker efter substring i strängarna i strings."""
    result = []
    for string in strings:
        if substring in string:
            result.append(string)

    return result

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
        result = partial_search(name, names)

        if result:
            print(f"Hittade '{name}' i namndatabasen: ")
            for name in result:
                print(name.capitalize())
        else:
            print(f"Hittade INTE '{name}' i namndatabasen")

        name = input_name()

if __name__ == "__main__":
    main()
