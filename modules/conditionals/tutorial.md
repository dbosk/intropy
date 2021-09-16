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
Givetvis kan vi dela upp funktionen `lift_leg` ytterligare. Du kan även se en 
[interaktiv genomgång av exekveringen][walk-tutor].

[walk]: https://github.com/dbosk/intropy/blob/master/modules/conditionals/walk.py
[walk-tutor]: https://pythontutor.com/visualize.html#code=%22%22%22Ett%20program%20som%20illustrerar%20funktionsuppdelningen%20i%20att%20g%C3%A5,%20dock%20med%20en%20%0At%C3%A4mligen%20udda%20g%C3%A5ngstil.%22%22%22%0A%0Adef%20take_step_first%28the_leg%29%3A%0A%20%20%20%20%22%22%22En%20funktion%20som%20anropar%20funktionerna%20som%20beh%C3%B6vs%20f%C3%B6r%20att%20ta%20ett%20steg%22%22%22%0A%20%20%20%20lift_leg%28the_leg%29%0A%20%20%20%20lean_body%28%22fram%C3%A5t%22%29%0A%0Adef%20take_step_second%28the_leg%29%3A%0A%20%20%20%20%22%22%22En%20funktion%20som%20anropar%20funktionerna%20f%C3%B6r%20att%20ta%20det%20kompletterande%20steget%22%22%22%0A%20%20%20%20lift_leg%28the_leg%29%0A%20%20%20%20lean_body%28%22bak%C3%A5t%22%29%0A%20%20%20%20put_leg%28the_leg%29%0A%0Adef%20lift_leg%28the_leg%29%3A%0A%20%20%20%20%22%22%22Lyfter%20ett%20ben,%20the_leg%20anger%20h%C3%B6ger%20eller%20v%C3%A4nster%22%22%22%0A%20%20%20%20print%28f%22lyft%20%7Bthe_leg%7D%20ben%22%29%0A%0Adef%20put_leg%28the_leg%29%3A%0A%20%20%20%20%22%22%22S%C3%A4tter%20ner%20ett%20ben%20som%20%C3%A4r%20i%20luften%22%22%22%0A%20%20%20%20print%28f%22s%C3%A4tt%20ned%20%7Bthe_leg%7D%20ben%22%29%0A%0Adef%20lean_body%28direction%29%3A%0A%20%20%20%20%22%22%22Luta%20kroppen,%20direction%20anger%20riktning%22%22%22%0A%20%20%20%20print%28f%22luta%20kroppen%20%7Bdirection%7D%22%29%0A%0Adef%20walk_1m_fwd%28%29%3A%0A%20%20%20%20%22%22%22En%20funktion%20som%20g%C3%A5r%20en%20meter%20fram%C3%A5t%22%22%22%0A%20%20%20%20take_step_first%28%22h%C3%B6ger%22%29%0A%20%20%20%20take_step_second%28%22v%C3%A4nster%22%29%0A%0Adef%20walk_fwd%28meters%29%3A%0A%20%20%20%20%22%22%22En%20funktion%20som%20g%C3%A5r%20meters%20antal%20meter%20fram%C3%A5t%22%22%22%0A%20%20%20%20if%20meters%20%3E%200%3A%0A%20%20%20%20%20%20%20%20walk_1m_fwd%28%29%0A%20%20%20%20%20%20%20%20walk_fwd%28meters-1%29%0A%0Awalk_fwd%282%29%0A&cumulative=false&curInstr=24&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false

Skriv program som, på samma sätt som ovan, skriver ut instruktioner för

  - att gå till olika platser som användaren kan välja mellan.
  - gå en slumpmässig promenad (höger, vänster, framåt, bakåt) som är $n$ meter 
    lång.
  - att dansa (valfri dans) $n$ takter, vilka steg ska tas med vilka fötter vid 
    de olika tillfällena i musiken?

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
dans][random-dance] ([interaktiv genomgång av exemplets exekvering][dance-tutor]).

[random-dance]: https://github.com/dbosk/intropy/blob/master/modules/conditionals/dance.py
[dance-tutor]: https://pythontutor.com/visualize.html#code=%22%22%22Ett%20exempelprogram%20som%20%22dansar%22%20ett%20antal%20steg%0A%0AFunktionen%20dansa%28n%29%20dansar%20tills%20att%20n%20%3D%200.%20S%C3%A5%20dansa%285%29%20kommer%20att%20dansa%20fem%20%0Atakter%20i%20dansen,%20exempelvis%20ta%20fem%20steg,%20tills%20att%20%22takterna%20%C3%A4r%20slut%22.%0A%0ADet%20%C3%A4r%20som%20en%20automat%20eller%20Turingmaskin,%20om%20man%20s%C3%A5%20vill.%22%22%22%0A%0Aimport%20random%0A%0Adef%20flytta_fot%28n,%20fot,%20riktning%29%3A%0A%20%20%20%20%22%22%22Flyttar%20foten%20fot%20i%20riktningen%20riktning,%20returnerar%20n-1%20%28steg%20tar%20en%20%0A%20%20%20%20takt%29%22%22%22%0A%20%20%20%20print%28f%22%7Bfot%7D%20fot%20%7Briktning%7D%22%29%0A%20%20%20%20return%20n-1%0A%0Adef%20slumpa_fot%28%29%3A%0A%20%20%20%20%22%22%22Returnerar%20%22h%C3%B6ger%22%20eller%20%22v%C3%A4nter%22.%22%22%22%0A%20%20%20%20if%20random.randint%280,%201%29%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20return%20%22h%C3%B6ger%22%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20return%20%22v%C3%A4nster%22%0A%0Adef%20slumpa_riktning%28%29%3A%0A%20%20%20%20%22%22%22Returnerar%20en%20riktning%22%22%22%0A%20%20%20%20slumptal%20%3D%20random.randint%280,%204%29%0A%20%20%20%20if%20slumptal%20%3C%201%3A%0A%20%20%20%20%20%20%20%20return%20%22fram%C3%A5t%22%0A%20%20%20%20elif%20slumptal%20%3C%202%3A%0A%20%20%20%20%20%20%20%20return%20%22bak%C3%A5t%22%0A%20%20%20%20elif%20slumptal%20%3C%203%3A%0A%20%20%20%20%20%20%20%20return%20%22h%C3%B6ger%22%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20return%20%22v%C3%A4nster%22%0A%0Adef%20snurra%28n%29%3A%0A%20%20%20%20%22%22%22Snurrar%20i%20dansen,%20returnerar%20n-2%20%28snurr%20tar%20tv%C3%A5%20takter%29%22%22%22%0A%20%20%20%20print%28%22Snurra!%22%29%0A%20%20%20%20return%20n-2%0A%0Adef%20dansa%28n%29%3A%0A%20%20%20%20%22%22%22Tar%20stegen%20f%C3%B6r%20n%20takter%20i%20dansen%22%22%22%0A%20%20%20%20if%20n%20%3C%3D%200%3A%0A%20%20%20%20%20%20%20%20return%0A%0A%20%20%20%20slump%20%3D%20random.randint%280,%201%29%0A%0A%20%20%20%20if%20slump%20%3C%201%3A%0A%20%20%20%20%20%20%20%20n%20%3D%20flytta_fot%28n,%20slumpa_fot%28%29,%20slumpa_riktning%28%29%29%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20n%20%3D%20snurra%28n%29%0A%0A%20%20%20%20dansa%28n%29%0A%0Adansa%285%29%0A&cumulative=false&curInstr=17&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false


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
