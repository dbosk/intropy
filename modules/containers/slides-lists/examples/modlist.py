"""En modul med en funktion som ber användaren att ändra värden i en lista"""

import input_type as it
import input_list as il

def input_index(lst, prompt=""):
    """
    Låter användaren välja ett index för listan lst,
    returnerar endast giltigt index.
    """
    print(prompt)

    while (index := it.input_type(int, f"Välj 0-{len(lst)-1}: ")) >= len(lst):
        pass

    return index

def change_items(lst, prompt=""):
    """
    Skriver ut prompt till användaren och låter hen ändra värden i listan 
    lst.
    """
    print(prompt)

    for index in range(len(lst)):
        print(f"{index}: {lst[index]}")

    index = input_index(lst, "Välj index att ändra: ")

    lst[index] = input("Nytt värde: ")

    return lst

def main():
    """Huvudprogram för testning"""
    names = il.input_list("Ange dina favoritnamn: ")
    print(f"Dina favoritnamn är {names}")
    names = change_items(names, "Vilket namn vill du ändra?")
    print(f"Dina favoritnamn är {names}")

if __name__ == "__main__":
    main()
