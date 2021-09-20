import random

class Bankkonto:
    def __init__(self, kontoinnehavare):
        self.kontoinnehavare = kontoinnehavare
        self.balans = 0
        self.genereraKontoNr()

    def genereraKontoNr(self):
        kontoNr = ""
        for i in range(10):
        	kontoNr += str(random.randint(0,9))
        self.kontoNr = kontoNr

    def uttag(self, belopp):
    	if self.balans > belopp: 
    		print("Tar ut", belopp, "kr")
    		self.balans -= belopp
    		print("Återstående balans: ", self.balans)
    	else: 
    		print("du har inte sådär mycket pengar på kontot pucko!")

    def insättning(self, belopp):
    	print ("sätter in ", belopp, "på ditt konto")
    	self.balans += belopp
    	print ("nuvarande belopp på ditt konto är: ", self.balans)        

konto = Bankkonto("Aleks Durowicz")
print(konto.kontoinnehavare, konto.balans, konto.kontoNr)
konto.insättning(1000)
konto.uttag(100)
