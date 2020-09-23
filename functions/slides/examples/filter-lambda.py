"""Filtering experiments"""

ns = range(-10, 10)
ms = filter(lambda x: x > 2, ns)

for i in ms:
    print(i, end=" ")
print()
