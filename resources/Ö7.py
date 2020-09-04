
import math

class Planet:

    def __init__ (self, namn, r, t):
        self.namn = namn
        self.r = r # radie
        self.t = t # omloppstid
        self.massa = planetmassa()

    def planetmassa(self):
        g = 6.67*math.pow(10,-11)
        return 4*math.pow(math.pi,2)*math.pow(self.r*1000000,3)/(G*math.pow(self.t*3600,2))


def lasfil():
    infil = open('infil.txt','r')
    rad = ""
    infil.readline() # slurpa slaskrad1
    infil.readline() # slurpa slaskrad2
    infil.readline() # slurpa slaskrad3
    infil.readline() # slurpa slaskrad4
    
    planetnamn = infil.readline().rstrip('\n')

    while ( planetnamn != ""):
        rad = infil.readline().rstrip('\n')
        delar = rad.split('/') # För att ta bort "/" tecknet
        r = float(delar[0])
        t = float(delar[1])
        p = planet(planetnamn,r,T)
        planeterna.append(p)
        planetnamn = infil.readline().rstrip('\n')
        
    return planeterna

def beräknaPlanetmassorna(planeterna):
    pass





        
