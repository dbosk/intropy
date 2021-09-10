---
title: Övning om variabler och funktioner
---
# Övning: funktioner och variabler

Målet med övningen är att du ska blir bättre på att

  - dela upp problem in mindre problem,
  - minimera kodupprepning,
  - skapa funktioner med parametrar och returvärden.


## Laborationen

Hur har olika grupper löst samma labb? Oftast väldigt olika. Vi går igenom 
några lösningar.


## Kakelfabriken

En kakelfabrik behöver räkna ut hur mycket färg som går åt för olika 
kakelmönster och olika storlekar.

Skriv funktioner som beräknar mängden färg givet relevanta inparametrar.

![Kakel: cirkel](https://github.com/dbosk/intropy/raw/functions-first/modules/variables/fig/kakel1.png)
![Kakel: kvadrat](https://github.com/dbosk/intropy/raw/functions-first/modules/variables/fig/kakel2.png)
![Kakel: hexagon](https://github.com/dbosk/intropy/raw/functions-first/modules/variables/fig/kakel3.png)


## Att göra saker

Vi ska nu fokusera på att skriva funktioner som fokuserar på att dela upp 
algoritmer i deras beståndsdelar.

Vi börjar med ett exempel för att gå.
```python
"""Ett program som illustrerar funktionsuppdelningen i att gå"""

def take_step_fwd():
    """En funktion som anropar funktionerna som behövs för att ta ett steg"""
    lift_leg("vänster")
    lean_body("framåt")
    lift_leg("höger")
    lean_body("bakåt")

def lift_leg(the_leg):
    """Lyfter ett ben, the_leg anger höger eller vänster"""
    print(f"lyft {the_leg} ben")

def lean_body(direction):
    """Luta kroppen, direction anger riktning"""
    print(f"luta kroppen {direction}")

def walk_two_steps():
    """En funktion som tar fem steg framåt"""
    take_step_fwd()
    take_step_fwd()

walk_two_steps()
```
Givetvis kan vi dela upp funktionen `lift_leg` ytterligare.

Skriv program som, på samma sätt som ovan, skriver ut instruktioner för att:

  1. dansa (valfri dans), vilka steg ska tas med vilka fötter?
  2. diska (handdisk, då diskmaskinen inte är så utmanande, vi såg en algoritm 
     på föreläsningen).

Vi går igenom olika lösningar samt

  - ett [alternativ för vad som händer när man diskar](https://github.com/dbosk/intropy/blob/functions-first/modules/variables/diska.py)
    och
  - hur man kan [konstruera e-postadresser utifrån namn](https://github.com/dbosk/intropy/blob/master/resources/funktioner/adress.py).


## Önskemål från gruppen

Vad vill gruppen gå igenom igen från veckan som var?
