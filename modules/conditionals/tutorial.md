---
title: Övning om inmatning och villkorssatser
authors:
  - Daniel Bosk <dbosk@kth.se>
  - Celina Soori <celinah@kth.se>
---
# Övning: inmatning, felhantering och villkorssatser

Målet med övningen är att du ska bli bättre på att

  - tillämpa styrstrukturer,
  - felhantera inmatning,
  - konstruera interaktiva program,
  - dela upp problem i mindre problem,
  - minimera kodupprepning


## Önskemål från gruppen

Var det något särskilt från veckans föreläsning och/eller OLI-material som gruppen vill gå igenom igen?

Gick förra veckans laboration bra? Finns det något ni skulle vilja gå igenom från laborationen?

## Övningsuppgifter

### Finn fem fel

Dela upp er i par och låt en av er ladda ner ett program för [att köpa biobiljetter](https://github.com/dbosk/intropy/blob/revision_of_exercises/modules/conditionals/movietickets.py)

Läs igenom koden och få ett hum om vad den är tänkt att göra. Testa att köra koden.

Hitta nu tillsammans minst fem fel/utvecklingsområden i koden (tänk på vad ni lärt er under veckan).

Förbättra nu koden efter det ni hittat. Blev koden mer lättläst, användbar och/eller användarvänlig? Varför?

### Bombspelet

Vi har satt ihop ett frågespel. Svarar man fel detoneras bomben.

Det behövs två filer: [bomben.py][bomben] och [bomb.py][bomb]. Båda måste ligga 
i samma katalog. Därefter kör man bomben.py: `python3 bomben.py`.

[bomben]: https://github.com/dbosk/intropy/blob/master/modules/conditionals/bomben.py
[bomb]: https://github.com/dbosk/intropy/blob/master/modules/conditionals/bomb.py



### Frågesport

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
