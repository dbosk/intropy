"""Inköpslista med Item-klass"""

class Item:
    """En vara på inköpslistan"""
    def __init__(self, name, checked=False):
        self.__name = name
        self.__checked = checked

    @property
    def name(self):
        return self.__name

    @property
    def checked(self):
        return self.__checked

    def check(self):
        """Bocka av varan"""
        self.__checked = True

    def uncheck(self):
        """Ta bort bockning"""
        self.__checked = False

    def __str__(self):
        status = "[X]" if self.__checked else "[ ]"
        return f"{status} {self.__name}"


class ShoppingList:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, item_name):
        """Lägg till en vara (skapar Item-objekt)"""
        item = Item(item_name)
        self.items.append(item)

    def list_items(self):
        """Visa alla varor"""
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item}")  # Använder Item.__str__()

    def check_item(self, index):
        """Bocka av en vara"""
        if 0 <= index < len(self.items):
            self.items[index].check()

    def remove_checked(self):
        """Ta bort alla avbockade varor"""
        self.items = [item for item in self.items
                      if not item.checked]


def main():
    """Exempel på användning"""
    # Skapa en inköpslista för mat
    mat_lista = ShoppingList("Mat")
    mat_lista.add_item("Mjölk")
    mat_lista.add_item("Bröd")
    mat_lista.add_item("Ägg")

    print("Inköpslista:")
    mat_lista.list_items()

    print("\nBockar av mjölk...")
    mat_lista.check_item(0)
    mat_lista.list_items()

    print("\nTar bort avbockade varor...")
    mat_lista.remove_checked()
    mat_lista.list_items()


if __name__ == "__main__":
    main()
