"""Ett program för att imitera fortune-kommandot"""

import cowsay_better
import random

def läs_fortune(databas):
    """Läser en fortune från filobjektet databas,
    returnerar den i strängformat"""
    fortune = ""
    rad = databas.readline()

    while rad != "*** nästa fortune ***\n" and rad != "":
        fortune += rad
        rad = databas.readline()

    return fortune.rstrip()

def ladda_databas(filnamn="fortunes.txt"):
    """Läser in fortunes från filnamn, default fortunes.txt;
    returnerar en lista med alla fortunes"""
    fortunes = []

    with open(filnamn, "r") as databas:
        fortune = läs_fortune(databas)
        while fortune != "":
            fortunes.append(fortune)
            fortune = läs_fortune(databas)

    return fortunes

def fortune():
    """Returnerar en slumpad fortune cookie"""
    fortunes = ladda_databas()
    return random.choice(fortunes)

def main():
    """Huvudprogram"""
    cowsay_better.cowsay(fortune())

if __name__ == "__main__":
    main()
