barn_pris = 10
vuxen_pris = 20

antal_biljetter = input("Hur många biljetter vil du köpa? ")
antalBiljetter = int(antal_biljetter)

antal_vuxen = input("Hur många av de biljetterna är för en vuxen? ")
antalVuxen = int(antal_vuxen)

antal_barn = antalBiljetter - antalVuxen

total_pris = antal_barn*barn_pris + antalVuxen*vuxen_pris

print("Du ska betala:")
print(total_pris)
