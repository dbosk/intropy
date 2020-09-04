## Övning 5 Aleks
class Ingrediens:

    def __init__(self, beskrivning, mängd):
        self.__beskrivning = beskrivning
        self.__mängd = mängd

    def beskrivning(self):
        return self.__beskrivning

    def mängd(self):
        return self.__mängd

    def __str__(self):
        return self.__beskrivning + " Mängd  " + str(self.__mängd) 

class Recept:
    def __init__(self,namn):
        self.__namn = namn
        self.__ingredienser = list()

    def namn(self):
        return self.__namn

    def ingredienser(self):
        return self.__ingredienser

    def addera(self, ingrediens):
        self.__ingredienser.append(ingrediens)      

    def __str__(self):
        s = "______________________\n" + str(self.__namn) + "\n"

        for p in self.__ingredienser:
            s += str(p)
        return s

def main():
    i1 = Ingrediens("Ägg", 4)
    i2 = Ingrediens("Mjölk (dl)", 6)
    i3 = Ingrediens("Mjöl (dl)", 5)
    ingredienserna = [i1, i2, i3]

    r1 = Recept("Pannkakor")
    r2 = Recept("Omlett")

    r1.addera(i1)
    r1.addera(i2)
    r1.addera(i3)

    r2.addera(i1)

    recepten = [r1,r2]

    for r in recepten:
        print("Beskrivning ") 
        print(r)


main()



        

    
