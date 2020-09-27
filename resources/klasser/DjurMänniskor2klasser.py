class Djur:
    def __init__(self, art, ben, läte):
    	self.art = art
    	self.ben = ben
    	self.läte = läte

    def konversera(self):
       print(self.läte, self.läte)

    def __str__(self):
        return "Art: " + self.art + "Antal ben: " + str(self.ben)

class Människa(Djur):
    def __init__(self, art, ben, läte, namn):
    	super().__init__(art, ben, läte)
    	self.namn = namn

    def konversera(self, fras):
        print (fras + "!? Jahaja jag heter iaf" + self.namn)

    def programmera(self):
        print("jag programmerar nästa Apple produkt yeyeyeyeyy")

    def __str__(self):
    	sträng = super().__str__()
    	sträng += "Namn: " + self.namn
    	return sträng

def läsFil(filnamn):
	fil = open(filnamn, "r")
	rader = [i.strip() for i in fil.readlines()]
	return rader

def skapaDjur(djurInfo):
	djur = []
	for d in djurInfo:
		art, ben, läte = d.split()
		djur.append(Djur(art, ben, läte))
	return djur

def skapaMänniskor(människoInfo):
	människor = []
	for m in människoInfo:
		art, ben, läte, namn = m.split()
		människor.append(Människa(art, ben, läte, namn))
	return människor


mInfo = läsFil("människor.txt")
dInfo = läsFil("djur.txt")
människor = skapaMänniskor(mInfo)
djur = skapaDjur(dInfo)

# for m in människor: 
# 	print(m)
# 	m.konversera(m.läte)
# 	m.programmera()

for d in djur: 
	
	print(d)
	d.konversera()
