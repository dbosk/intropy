"""Program som tar ålder som inmatning"""

year = int(input("När föddes du? "))

if year < 2000:
    print("Du är i hyfsad form ändå.")
elif year < 1990:
    print("Du är gammal och grå!")
else:
    print("Du är ung och fräsch! Än så länge!")
