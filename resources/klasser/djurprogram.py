
class Haj:
    def __init__(self, namn, art):
       self.namn = namn
       self.art = art
       self.hastighet = 0

    def simma(self):
    	self.hastighet += 1
       

    def introduktion(self):
    	print("hej jah heter", self.namn, "och jag är en", self.art, "min hastighet är", self.hastighet)


minhaj = Haj("Aleks", "vithaj")
print(minhaj)
minhaj.introduktion()
minhaj.simma()
minhaj.simma()
minhaj.simma()
minhaj.introduktion()
    


