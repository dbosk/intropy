"""Program som frågar användaren efter saker och skriver ut dem snyggt"""

import aligncinek2 as align

items = []

while True:
    item = input("Mata in en sak: ")
    if item == "":
        break
    items.append(item)

align.print_list(items, 20)
