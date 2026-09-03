"""Inköpslista med klasser"""

class ShoppingList:
    def __init__(self, name):
        self.name = name
        self.items = []
    
    def add_item(self, item):
        self.items.append({"name": item, "checked": False})
    
    def list_items(self):
        for i, item in enumerate(self.items, 1):
            status = "[X]" if item["checked"] else "[ ]"
            print(f"{i}. {status} {item['name']}")
    
    def check_item(self, index):
        if 0 <= index < len(self.items):
            self.items[index]["checked"] = True
    
    def remove_checked(self):
        self.items = [item for item in self.items 
                      if not item["checked"]]

def main():
    """Exempel på användning"""
    # Skapa en inköpslista för mat
    mat_lista = ShoppingList("Mat")
    mat_lista.add_item("Mjölk")
    mat_lista.add_item("Bröd")
    mat_lista.add_item("Ägg")
    
    mat_lista.list_items()
    mat_lista.check_item(0)  # Bocka av mjölk
    mat_lista.remove_checked()
    
    # Hantera flera listor
    listor = []
    listor.append(ShoppingList("Mat"))
    listor.append(ShoppingList("Diverse"))
    
    # Lägg till varor
    listor[0].add_item("Mjölk")
    listor[0].add_item("Bröd")
    listor[1].add_item("Tandkräm")
    
    # Visa alla listor
    for lista in listor:
        print(f"\n{lista.name}:")
        lista.list_items()

if __name__ == "__main__":
    main()
