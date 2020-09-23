#1. Generering av epost-adresser för studenter
# Målet är att skapa en email-adress med hjälp av en funktion
# Emailen ska innehålla: 
# 	Ditt programs bokstav
# 	Din årgång
# 	Förnamn (3 första bokstäverna)
# 	efternamn (3 första bokstäverna)
# 	Avsluta med @kth.se
# 	Resultat: i16-aledur@kth.se
# Skapa en funktion som returnerar email adressen
# Använd lämplig in- och utdata

def skapaAdress(program, år, fnamn, enamn):
	adress = ""
	adress += program.lower()
	adress += str(år)
	adress += "-"
	adress += fnamn[0:3].lower()
	adress += enamn[0:3].lower()
	adress += "@kth.se"
	return adress

adress = skapaAdress("I", 16, "Aleks", "Durowicz")
print(adress)

adress = skapaAdress("O", 20, "Pelle", "Svanslös")
print(adress)

