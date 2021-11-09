"""En modul lämpad för hantering av shoppinglistor"""

class Vara:
    """En klass för varor i en shoppinglista"""

    def __init__(self, namn, antal=1):
        """Skapar ett inlägg i en shoppinglista:
        namn (sträng),
        antal (int, default 1)"""
        self.__namn = namn
        if type(antal) in [int, float]:
            self.__antal = antal
        else:
            self.__antal = int(antal)
        self.__avbockad = False

    @property
    def namn(self):
        """Returnerar namnet"""
        return self.__namn

    @property
    def antal(self):
        """Returnerar antalet"""
        return self.__antal

    @property
    def avbockad(self):
        """Returnerar True om varan är avbockad, False annars"""
        return self.__avbockad

    def __str__(self):
        """Returnerar en representation lämplig för utskrift"""
        return f"[{'x' if self.avbockad else ' '}] {self.antal} st {self.namn}"

    def bocka_av(self):
        """Bockar av"""
        self.__avbockad = True


def main():
    """Testprogram"""
    lista = []
    lista.append(Vara("mjölk", 5))
    lista.append(Vara("tomater", 3))
    lista.append(Vara("yoghurt", 1))

    print("Shoppinglista")
    for vara in lista:
        print(vara)

    lista[1].bocka_av()

    print("Shoppinglista")
    for vara in lista:
        print(vara)

if __name__ == "__main__":
    main()
