# Fråga användaren om hur många rader och hur många kolumner de vill att deras rektangel ska vara
# Använd en funktion för att skriva ut en rektangel i stjärnform

# Exempel: rader = 5, kolumner = 3

# ***
# ***
# ***
# ***
# ***



def rektangel(rad, kolumn):
   for i in range(rad):
   		s = ""
   		for j in range(kolumn):
   			s = s + "*"
   		print(s)

svar = input("hur många rader? ")
rad = int(svar)

svar = input("hur många kolumner? ")
kolumn = int(svar)

rektangel(rad, kolumn)