"""En modul lämpad för hantering av shoppinglistor"""


class Item:
    """En klass för varor i en shoppinglista"""

    def __init__(self, name, amount=1):
        """Skapar ett inlägg i en shoppinglista:
        `name` (sträng),
        `amount` (heltal, default 1)"""
        self.__name = name
        if type(amount) in [int, float]:
            self.__amount = amount
        else:
            self.__amount = int(amount)
        self.__checked = False

    @property
    def name(self):
        """Returnerar namnet"""
        return self.__name

    @property
    def amount(self):
        """Returnerar antalet"""
        return self.__amount

    @property
    def checked(self):
        """Returnerar True om varan är avbockad, False annars"""
        return self.__checked

    def __str__(self):
        """Returnerar en representation lämplig för utskrift"""
        return f"[{'x' if self.checked else ' '}] {self.amount} st {self.name}"

    def check(self):
        """Bockar av"""
        self.__checked = True


def main():
    """Testprogram"""
    shopping_items = [Item("mjölk", 5), Item("tomater", 3), Item("yoghurt", 1)]

    print("Shoppinglista")
    for item in shopping_items:
        print(item)

    shopping_items[1].check()

    print("Shoppinglista")
    for item in shopping_items:
        print(item)


if __name__ == "__main__":
    main()
