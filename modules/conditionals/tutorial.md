---
title: Övning om inmatning och villkorssatser
authors:
  - Daniel Bosk <dbosk@kth.se>
---
# Övning: inmatning och villkorssatser

Målet med övningen är att du ska blir bättre på att

  - tillämpa styrstrukturer,
  - konstruera interaktiva program,
  - dela upp problem i mindre problem,
  - minimera kodupprepning,
  - bekanta dig med rekursion.


## Laborationen

Hur har olika grupper löst samma labb? Oftast väldigt olika. Vi går igenom 
några lösningar. Hur löser man extrauppgiften?


## Att göra saker

Vi ska nu fokusera på att skriva funktioner som fokuserar på att dela upp 
algoritmer i deras beståndsdelar. Den här gången kommer algoritmerna att kunna 
bli lite mer avancerade, de ska kunna göra olika saker beroende på olika 
villkor.

Vi börjar med [ett exempel för att gå][walk]:
```python
"""Ett program som illustrerar funktionsuppdelningen i att gå, dock med en 
tämligen udda gångstil."""

def take_step_first(the_leg):
    """En funktion som anropar funktionerna som behövs för att ta ett steg"""
    lift_leg(the_leg)
    lean_body("framåt")

def take_step_second(the_leg):
    """En funktion som anropar funktionerna för att ta det kompletterande steget"""
    lift_leg(the_leg)
    lean_body("bakåt")
    put_leg(the_leg)

def lift_leg(the_leg):
    """Lyfter ett ben, the_leg anger höger eller vänster"""
    print(f"lyft {the_leg} ben")

def put_leg(the_leg):
    """Sätter ner ett ben som är i luften"""
    print(f"sätt ned {the_leg} ben")

def lean_body(direction):
    """Luta kroppen, direction anger riktning"""
    print(f"luta kroppen {direction}")

def walk_1m_fwd():
    """En funktion som går en meter framåt"""
    take_step_first("höger")
    take_step_second("vänster")

def walk_fwd(meters):
    """En funktion som går meters antal meter framåt"""
    if meters > 0:
        walk_1m_fwd()
        walk_fwd(meters-1)

walk_fwd(2)
```
Givetvis kan vi dela upp funktionen `lift_leg` ytterligare.

[walk]: https://github.com/dbosk/intropy/blob/master/modules/conditionals/walk.py

Skriv program som, på samma sätt som ovan, skriver ut instruktioner för att 
dansa (valfri dans) $n$ takter, vilka steg ska tas med vilka fötter vid de 
olika tillfällena i musiken?

Vi går igenom olika lösningar.

En användbar byggsten för att få lite variation i dansen är slump. Följande kod 
illustrerar hur vi kan slumpa tal.
```python
"""Ett program som illustrerar hur man skapar slumptal i Python"""

import random

slumptal = random.randint(1, 10)

print(f"Slumptalet är {slumptal}.")
```
Vi kan även gå igenom [ett exempel som använder denna och skapar en slumpmässig 
dans][random-dance].

[random-dance]: https://github.com/dbosk/intropy/blob/master/modules/conditionals/dance.py


## Frågesport

Ett klassiskt program för att experimentera med villkor är frågesport. Skriv 
ett frågeprogram med kluriga frågor. För att mäta hur lång tid en användare tar 
på sig kan man använda följande konstruktion:
```python
"""
Exempelprogram för tidsmätning

Vi sparar klockslaget vid start och klockslaget vid slut, sedan tar vi 
skillnaden.
"""

import datetime as dt

start_time = dt.datetime.now()

svar = input("Vad är svaret på frågan? ")

end_time = dt.datetime.now()

print(f"Tidsåtgång: {end_time-start_time}")
```

Tips: använd funktioner för att åstadkomma straffrundor vid fel svar.


## Önskemål från gruppen

Vad vill gruppen gå igenom igen från veckan som var?
