"""En modul som läser in en lista"""

def input_list(prompt="", term_prompt="blankrad för avslut"):
    """Skriver prompt på skärmen och låter användaren mata in,
    term_prompt innehåller en påminnelse om hur man avslutar med blankrad."""
    print(prompt)

    index = 0
    items = []

    while (item := input(f"{index} ({term_prompt}): ")) != "":
        items.append(item)
        index += 1

    return items

def main():
    """Huvudprogram för testning"""
    names = input_list("Skriv in dina favoritnamn.")
    print(f"Du gillar namnen {names}")

if __name__ == "__main__":
    main()
