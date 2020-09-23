# Du ska skapa ett program där användaren anger tal till hen är nöjd. Dessa tal lägger du till en lista. När användaren är klar ska den största och minsta talet skrivas ut samt summan av alla tal i listan. 
# Tips: googla hur man får största, minsta värde och summa av en lista
# 
# Funktioner att använda: 
# AngeTal()
# 	Så länge användaren vill köra så ska hen kunna lägga till siffror i listan
# 	Return tallistan
# summanTalen(tallistan)
# störstaTalet(tallistan)
# minstaTalet(tallistan)


def störstaTalet(tallistan):
	return max(tallistan)

def minstaTalet(tallistan):
	return min(tallistan)

def summanTalen(tallistan): 
	return sum(tallistan)

def angeTal():
	köra = "ja"
	tallistan = []
	while köra != "nej":
		tal = int(input("Ange ett tal till listan: "))
		tallistan.append(tal)
		köra = input("vill du ange ett till tal (ja/nej): ")
	return tallistan

tallistan = angeTal()
print (störstaTalet(tallistan))
print (minstaTalet(tallistan))
print (summanTalen(tallistan))






