---
title: Fördjupande övning om variabler och funktioner
authors:
  - Daniel Bosk <dbosk@kth.se>
  - Celina Soori <celinah@kth.se>
---
# Fördjupande övning: funktioner och variabler

Målet med övningen är att du ska få en fördjupad förståelse för hur man ska

  - dela upp problem in mindre problem,
  - minimera kodupprepning,
  - skapa funktioner med parametrar och returvärden.


## Önskemål från gruppen

Har alla kommit igång med kursens material? Är det några frågetecken om kursuppläget?

Var det något särskilt från veckans föreläsning och/eller OLI-material som gruppen vill gå in djupare på?

## Övningsuppgifter

### Finn fem fel

Dela upp er i par och låt en av er ladda ner [ett program för att göra hushållssysslor](https://github.com/dbosk/intropy/blob/master/modules/variables/tutorial-advanced/hard_house_chores.py)

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

[walk]: https://github.com/dbosk/intropy/blob/master/modules/variables/tutorial-advanced/walk.py

Skriv program som, på samma sätt som ovan, skriver ut instruktioner för att:

  1. dansa (valfri dans), vilka steg ska tas med vilka fötter?
  2. diska (handdisk, då diskmaskinen inte är så utmanande, vi såg en algoritm
     på föreläsningen).

Vi går igenom olika lösningar och det här [lösningsförslaget](https://github.com/dbosk/intropy/blob/master/modules/variables/tutorial-advanced/diska.py)

### Beräkna Body Mass Index (BMI)

Body Mass Index (BMI) kan användas för att se om man kanske är över- eller underviktigt, eller har en bra vikt.

Formula är: "BMI" = "vikt i kg" / ("längd i meter" ^ 2)

Skriv ett program bestående av en funktion som givet en persons vikt och längd beräknar hans/hennes BMI. 
Programmet ska använda funktionen för att skriva ut (åtminstone) ett BMI.

Vi går igenom olika lösningar och det här [lösningsförslaget](https://github.com/dbosk/intropy/blob/master/modules/variables/tutorial-advanced/bmi.py)

### Generera e-postadresser

Skriv ett program som generar en e-postadress utifrån parametrar som antingen är hårdkodade eller givna av användaren.

Vi går igenom olika lösningar och det här [lösningsförslaget](https://github.com/dbosk/intropy/blob/master/resources/funktioner/adress.py)

### Avgöra om en e-postadress är giltig

Skriv ett program som tar en e-postadress som input och sedan returnerar om
den givna e-postadressen är giltig eller inte. Går det att återanvända kod från
föregående uppgift?
