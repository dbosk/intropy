import random

class Bankkonto:
    def __init__(self, kontoinnehavare, pin):
        self.kontoinnehavare = kontoinnehavare
        self.__balans = 0
        self.genereraKontoNr()
        self.pin = pin

    def kontrolleraPin(self):
    	försök = int(input("Ange din pinkkod"))
    	if försök != self.pin:
    		print("Felaktig pinkod")
    		return False
    	else: 
    		return True
        
    def __getBalans(self):
    	return self.__balans

    def __setBalans(self, balans):
    	self.__balans = balans

    def genereraKontoNr(self):
        kontoNr = ""
        for i in range(10):
        	kontoNr += str(random.randint(0,9))
        self.kontoNr = kontoNr

    def uttag(self, belopp):
    	if not self.kontrolleraPin():
    		return
    	if self.__getBalans() > belopp: 
    		print("Tar ut", belopp, "kr")
    		gammalBalans = self.__getBalans()
    		nyBalans = gammalBalans - belopp
    		self.__setBalans(nyBalans)
    		print("Återstående balans: ", self.__getBalans())
    	else: 
    		print("du har inte sådär mycket pengar på kontot pucko!")

    def insättning(self, belopp):
    	if not self.kontrolleraPin():
    		return
    	print ("sätter in ", belopp, "på ditt konto")
    	gammalBalans = self.__getBalans()
    	nyBalans = gammalBalans - belopp
    	self.__setBalans(nyBalans)

    	print ("nuvarande belopp på ditt konto är: ", self.__getBalans()) 
	       

konto = Bankkonto("Aleks", 1234)
konto.insättning(1000)
konto.uttag(100)
