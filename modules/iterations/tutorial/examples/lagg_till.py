"""Lägger till ett element i en lista, inne i en funktion."""


def lägg_till1(lista, element):
    """Lägger element sist i lista."""
    lista.append(element)


def lägg_till2(lista, element):
    """Lägger element sist i lista."""
    lista = lista + [element]


def main():
    """Lägger till ett tal i två lika listor och skriver ut dem."""
    första = [1, 2]
    lägg_till1(första, 3)
    print(första)

    andra = [1, 2]
    lägg_till2(andra, 3)
    print(andra)


if __name__ == "__main__":
    main()
