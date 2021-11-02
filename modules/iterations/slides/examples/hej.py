"""Program som skriver ut hej 50 gånger"""

print("for")
for gång in range(50):
    print(f"hej {gång}!")
    if gång > 2:
        break

print("while")
antal = 50
while antal > 0:
    print(f"hej {antal}!")
    # antal = antal - 1
    antal -= 1
    if antal < 48:
        break

print("while alternativ")
antal = 0
while antal < 50:
    print(f"hej {antal}!")
    antal += 1
    if antal > 2:
        break
