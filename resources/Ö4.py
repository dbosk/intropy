## öva p åklasser och objekt

class Pjas:

    def __init__(self, color, agare):
        self.color = color
        self.position = 0
        self.agare = agare
        

    def move(self, step):
        self.position = self.position + step

    def pushed(self):
        self.position = 0

    def supermove(self, step):
        self.position = self.position + (2*step)

def utskrift(lista):
    for i in range(len(lista)):
        print(lista[i].color + ": ", lista[i].position, lista[i].agare)
    print()


##p1 = Pjas("röd")
##p2 = Pjas("blå")

##print(p1.color + ": ", p1.position)
##print(p2.color + ": ", p2.position)
##print()
##
##p1.move(4)
##p2.move(5)
##
##print(p1.color + ": ", p1.position)
##print(p2.color + ": ", p2.position)
##print()

pjaser = list()

for i in range(4):
    pjaser.append(Pjas("röd", "Aleks"))
    pjaser.append(Pjas("blå", "Fred"))

utskrift(pjaser)

pjaser[2].move(4)
pjaser[6].move(6)

utskrift(pjaser)

pjaser[2].pushed()

utskrift(pjaser)

pjaser[6].supermove(4)

utskrift(pjaser)




    
