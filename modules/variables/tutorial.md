---
title: Övning om variabler och funktioner
authors:
  - Daniel Bosk <dbosk@kth.se>
  - Celina Soori <celinah@kth.se>
---
# Övning: funktioner och variabler

Målet med övningen är att du ska bli bättre på att

  - dela upp problem in mindre problem,
  - minimera kodupprepning,
  - skapa funktioner med parametrar och returvärden.

## Genomgång av veckans svårigheter

Vi går igenom det vi upptäckt i OLI är extra svårt den här veckan.

Zoomlänk: 

## Önskemål från gruppen

Har alla kommit igång med kursens material? Är det några frågetecken om kursuppläget?

Var det något särskilt från veckans föreläsning och/eller OLI-material som gruppen vill gå igenom igen?

## Övningsuppgifter

### Kakelfabriken

En kakelfabrik behöver räkna ut hur mycket färg som går åt för olika 
kakelmönster och olika storlekar.

Skriv funktioner som beräknar mängden färg givet relevanta inparametrar.

![Kakel: cirkel](https://github.com/dbosk/intropy/raw/master/modules/variables/fig/kakel1.png)
![Kakel: kvadrat](https://github.com/dbosk/intropy/raw/master/modules/variables/fig/kakel2.png)
![Kakel: hexagon](https://github.com/dbosk/intropy/raw/master/modules/variables/fig/kakel3.png)

### Finn fem fel

Dela upp er i par och låt en av er ladda ner [ett program för att göra hushållssysslor](https://github.com/dbosk/intropy/blob/revision_of_exercises/modules/variables/easy_house_chores.py)

Läs igenom koden och få ett hum om vad den är tänkt att göra. Testa att köra koden.

Hitta nu tillsammans minst fem fel/utvecklingsområden i koden (tänk på vad ni lärt er under veckan).

Förbättra nu koden efter det ni hittat. Blev koden mer lättläst, användbar och/eller användarvänlig? Varför?

### Att göra saker

Vi ska nu fokusera på att skriva funktioner som fokuserar på att dela upp
algoritmer i deras beståndsdelar.

Vi börjar med [ett exempel för att gå][walk]:
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
    """En funktion som tar två steg framåt"""
    take_step_fwd()
    take_step_fwd()

walk_two_steps()
```
Givetvis kan vi dela upp funktionen `lift_leg` ytterligare.

[walk]: https://github.com/dbosk/intropy/blob/master/modules/variables/walk.py

Skriv program som, på samma sätt som ovan, skriver ut instruktioner för att:

  1. dansa (valfri dans), vilka steg ska tas med vilka fötter?
  2. diska (handdisk, då diskmaskinen inte är så utmanande, vi såg en algoritm
     på föreläsningen).

Vi går igenom olika lösningar och det här [lösningsförslaget](https://github.com/dbosk/intropy/blob/master/modules/variables/diska.py)
