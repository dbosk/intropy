---
title: Fördjupande övning om inmatning och villkorssatser
authors:
  - Daniel Bosk <dbosk@kth.se>
  - Celina Soori <celinah@kth.se>
---
# Fördjupande övning: inmatning, felhantering och villkorssatser

Målet med övningen är att du ska få en fördjupad förståelse för hur du ska

  - tillämpa styrstrukturer,
  - felhantera inmatning,
  - konstruera interaktiva program,
  - dela upp problem i mindre problem,
  - minimera kodupprepning

## Önskemål från gruppen

Var det något särskilt från veckans föreläsning och/eller OLI-material som gruppen vill gå in djupare på?

Är det någon som vill visa upp något särskilt från förra veckans laboration som kan ge inspiration till gruppen?

## Övningsuppgifter

### Finn fem fel

Dela upp er i par och låt en av er ladda ner ett program för [att köpa biobiljetter](https://github.com/dbosk/intropy/blob/revision_of_exercises/modules/containers/slides/examples/guess.py)

Läs igenom koden och få ett hum om vad den är tänkt att göra. Testa att köra koden.

Hitta nu tillsammans minst fem fel/utvecklingsområden i koden (tänk på vad ni lärt er under veckan).

Förbättra nu koden efter det ni hittat. Blev koden mer lättläst, användbar och/eller användarvänlig? Varför?

### Att göra saker

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
Givetvis kan vi dela upp funktionen `lift_leg` ytterligare. Du kan även se en
[interaktiv genomgång av exekveringen][walk-tutor].

[walk]: https://github.com/dbosk/intropy/blob/master/modules/conditionals/walk.py
[walk-tutor]: https://pythontutor.com/visualize.html#code=%22%22%22Ett%20program%20som%20illustrerar%20funktionsuppdelningen%20i%20att%20g%C3%A5,%20dock%20med%20en%20%0At%C3%A4mligen%20udda%20g%C3%A5ngstil.%22%22%22%0A%0Adef%20take_step_first%28the_leg%29%3A%0A%20%20%20%20%22%22%22En%20funktion%20som%20anropar%20funktionerna%20som%20beh%C3%B6vs%20f%C3%B6r%20att%20ta%20ett%20steg%22%22%22%0A%20%20%20%20lift_leg%28the_leg%29%0A%20%20%20%20lean_body%28%22fram%C3%A5t%22%29%0A%0Adef%20take_step_second%28the_leg%29%3A%0A%20%20%20%20%22%22%22En%20funktion%20som%20anropar%20funktionerna%20f%C3%B6r%20att%20ta%20det%20kompletterande%20steget%22%22%22%0A%20%20%20%20lift_leg%28the_leg%29%0A%20%20%20%20lean_body%28%22bak%C3%A5t%22%29%0A%20%20%20%20put_leg%28the_leg%29%0A%0Adef%20lift_leg%28the_leg%29%3A%0A%20%20%20%20%22%22%22Lyfter%20ett%20ben,%20the_leg%20anger%20h%C3%B6ger%20eller%20v%C3%A4nster%22%22%22%0A%20%20%20%20print%28f%22lyft%20%7Bthe_leg%7D%20ben%22%29%0A%0Adef%20put_leg%28the_leg%29%3A%0A%20%20%20%20%22%22%22S%C3%A4tter%20ner%20ett%20ben%20som%20%C3%A4r%20i%20luften%22%22%22%0A%20%20%20%20print%28f%22s%C3%A4tt%20ned%20%7Bthe_leg%7D%20ben%22%29%0A%0Adef%20lean_body%28direction%29%3A%0A%20%20%20%20%22%22%22Luta%20kroppen,%20direction%20anger%20riktning%22%22%22%0A%20%20%20%20print%28f%22luta%20kroppen%20%7Bdirection%7D%22%29%0A%0Adef%20walk_1m_fwd%28%29%3A%0A%20%20%20%20%22%22%22En%20funktion%20som%20g%C3%A5r%20en%20meter%20fram%C3%A5t%22%22%22%0A%20%20%20%20take_step_first%28%22h%C3%B6ger%22%29%0A%20%20%20%20take_step_second%28%22v%C3%A4nster%22%29%0A%0Adef%20walk_fwd%28meters%29%3A%0A%20%20%20%20%22%22%22En%20funktion%20som%20g%C3%A5r%20meters%20antal%20meter%20fram%C3%A5t%22%22%22%0A%20%20%20%20if%20meters%20%3E%200%3A%0A%20%20%20%20%20%20%20%20walk_1m_fwd%28%29%0A%20%20%20%20%20%20%20%20walk_fwd%28meters-1%29%0A%0Awalk_fwd%282%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false

Skriv program som, på samma sätt som ovan, skriver ut instruktioner för

  - att gå till olika platser som användaren kan välja mellan.
  - gå en slumpmässig promenad (höger, vänster, framåt, bakåt) som är $n$ meter
    lång.
  - att dansa (valfri dans) $n$ takter, vilka steg ska tas med vilka fötter vid
    de olika tillfällena i musiken?
  - reagerar om användaren går in i en vägg, ramlar ner i ett hål m.m.

Vi går igenom olika lösningar.

En användbar byggsten för promenaden och för att få lite variation i dansen är
slump. Följande kod illustrerar hur vi kan slumpa tal.
```python
"""Ett program som illustrerar hur man skapar slumptal i Python"""

import random

slumptal = random.randint(1, 10)

print(f"Slumptalet är {slumptal}.")
```
Vi kan även gå igenom [ett exempel som använder denna och skapar en slumpmässig
dans][random-dance].

[random-dance]: https://github.com/dbosk/intropy/blob/master/modules/conditionals/dance.py
