"""Program som tar ålder som inmatning"""

år = int(input("När föddes du?"))

if år < 1995:
    print("Du är gammal och grå!")
elif år < 2000:
    print("Du är i hyfsad form ändå.")
else:
    print("Du är ung och fräsch! Än så länge!")
