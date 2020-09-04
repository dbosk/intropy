# Aleks Durowicz, grupp 1 
# Rumprogram - extra övning

# Uppgiftern går ut på att skriva ett program med byggnadsobejkt som E och D osv
# samt klassrumsobjekt som E35, D42 osv

# 1. Skapa en byggnadklass som kan beskriva namnet på byggnaden, adress våningar och dess klassrum (fler klassrum)
# 2. Skapa en klassrumklass som kan beskriva namnet på klassrummet, våningen den ligger på och antal sittplatser
# 3. Skapa byggnadsobjekt och klassrumsobjekt
# 4. Skriv ut en byggnad och dess klassrum, alltså ska man på nått sätt se till att en byggnad har en lista av klassrumsobjekt
# 5. Exempel på utskrift av en klar labb:

# Byggnaden heter E och ligger på Lindstedtvägen 24 och har 6 våningar
# Har klassrummen: 
# E35 på plan 3 med 45 platser
# E53 på plan 5 med 40 platser
# Byggnaden heter D och ligger på Lindstedtvägen 28 och har 6 våningar
# Har klassrummen: 
# D35 på plan 3 med 37 platser
# D36 på plan 4 med 32 platser

# attributen ska vara inkapslade
# använd dig av en __str__ metod
# programmet ska ha en skapaobjekt() funktion där objekt skapas och läggs in i en byggnadslista och en klassrumslista
# programmet ska ha en main() funktion

class Byggnad:

    def __init__(self, namn, adress, våningar):
        self.__namn = namn
        self.__adress = adress
        self.__våningar = våningar
        self.__klassrum = []

    #metoder som returnerar de inkapslade attributen
    def namnmetod(self):
        return self.__namn
    
    def adressmetod(self):
        return self.__adress

    def väningarmetod(self):
        return self.__våningar

    def klassrummetod(self):
        return self.__klassrum

    # metod där klassrum läggs till till en byggnad
    def klassrumlista(self, ettrum):
        self.__klassrum.append(ettrum)

    #metod för lättare utskrift av objket
    def __str__(self):
        return "Byggnaden heter " + self.__namn + " och ligger på " + self.__adress + " och har " + str(self.__våningar) + " våningar"
    
class Klassrum:

    def __init__(self, våning, namn, antalplatser):
        self.__våning = våning
        self.__namn = namn
        self.__antalplatser = antalplatser

    #metoder som returnerar de inkapslade attributen
    def våningmetod(self):
        return self.__våning

    def namnmetod(self):
        return self.__namn

    def platsermetod(self):
        return self.__antalplatser

    #metod för lättare utskrift av objket
    def __str__(self):
        return self.__namn + " på plan " + str(self.__våning) + " med " + str(self.__antalplatser) + " platser"


# funktion som skapar och printar ut objekt
def skapa():
    
    # skapar byggnader
    b1 = Byggnad("E", "Lindstedtvägen 24", 6)
    b2 = Byggnad("D", "Lindstedtvägen 28", 6)

    # lägger in byggnaderna i en lista
    byggnaderlista =  [b1, b2]

    # skapar klassrum
    k1 = Klassrum(3, "E35", 45)
    k2 = Klassrum(5, "E53", 40)
    k3 = Klassrum(3, "D35", 37)
    k4 = Klassrum(4, "D36", 32)

    # lägger till klassrummen i en lista
    klassrumlista = [k1, k2, k3, k4]

    return byggnaderlista, klassrumlista


def main():

    byggnaderlista, klassrumlista = skapa()

    for k in klassrumlista:
        bokstavslista = list(k.namnmetod())

        if (bokstavslista[0] == "E"):
            for b in byggnaderlista:
                if (b.namnmetod() == "E"):
                    b.klassrumlista(k)
                    
        elif (bokstavslista[0] == "D"):
            for b in byggnaderlista:
                if (b.namnmetod() == "D"):
                    b.klassrumlista(k)

    # skriver ut bygnaderna med dess klassrum
    for b in byggnaderlista:
        print(b)
        print ("Har klassrummen: ")
        for klassrum in b.klassrummetod(): 
            print(klassrum)

main()
    









