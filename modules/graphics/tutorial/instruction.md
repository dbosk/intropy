---
title: Övning om grafiska användargränssnitt
authors:
  - Daniel Bosk <dbosk@kth.se>
---
# Övning: grafiska användargränssnitt

Målet med övningen är att du ska blir bättre på att

  - konstruera grafiska användargränssnitt,
  - använda och konstruera sammansatta datatyper (klasser),
  - programmera med hjälp av händelseprogrammering och callbackfunktioner,
  - leta i dokumentationen för programbibliotek.


## En klocka

Börja med att skriva ett klockprogram för terminalen. Det ska skriva ut tiden 
(hh:mm:ss) i terminalen, sedan gå tillbaka och uppdatera texten. Ett tips är 
att skriva ut `\b`-tecken, dessa backar var utskriften sker och kan då användas 
för att skriva över. Exempelvis
```python
print("hej\b\b\bHEJ")
```
kommer att skriva ut "hej" sedan backa tre steg och skriva över "hej" med "HEJ" 
istället.
Python uppdaterar dock inte terminalen förrän tillräckligt mycket har skrivits 
ut.
Då kan man tvinga fram det, se följande experiment som illustrerar konceptet:
```python
import sys
import time

print("test", end="")
time.sleep(1)
sys.stdout.flush()
time.sleep(1)
```

För att få tillgång till tiden (och för att vänta mellan utskrifterna) används 
[Pythons `time`-modul][timedoc] (se länken eller kör `pydoc3 time`).

[timedoc]: https://docs.python.org/3/library/time.html#functions

![En bild på grafiskt gränssnitt som visar tiden i digitalt fortmat][clock]

[clock]: https://github.com/dbosk/intropy/blob/master/modules/graphics/tutorial/clock.png

Nu kan du gå vidare med att skriva ett grafiskt gränssnitt som visar tiden. Nu 
kan vi inte längre använda `time.sleep` för att vänta mellan uppdateringarna. 
Då GUI:n är händelsebaserade måste vi sätta upp en händelse att vi ska bli 
notifierade när en sekund har gått. `Tk`-klassen har en metod som heter `after` 
som är användbar, du kan läsa om den om du kör `pydoc3 tkinter.Tk` och sedan 
söker efter `after` (tryck `/` och skriv `after` medan du läser 
dokumentationen).

Lösningsförslag:
- [Lösningsförslag för klockan i terminalen][term_clock.py].
- [Lösningsförslag för GUI-klockan][clock.py].

[term_clock.py]: https://github.com/dbosk/intropy/blob/master/modules/graphics/tutorial/term_clock.py
[clock.py]: https://github.com/dbosk/intropy/blob/master/modules/graphics/tutorial/clock.py


## En timer

Nu vill vi istället skriva en timer. Konceptet är detsamma. Men nu ska vi kunna 
ställa in timern och sedan ska den räkna ner. Exempelvis kan det se ut såhär:

![En bild på grafiskt gränssnitt som visar en timer som räknar ned][timer]

[timer]: https://github.com/dbosk/intropy/blob/master/modules/graphics/tutorial/timer.png

I exemplet ovan skriver vi in tiden i rutorna och sedan räknar programmet ned i 
samma rutor. Men man kan ha rutor där man ställer in, en OK-knapp och sedan 
räkna ner i en label också.

[Lösningsförslag för en GUI-timer][timer.py].

[timer.py]: https://github.com/dbosk/intropy/blob/master/modules/graphics/tutorial/timer.py


# Ett ritprogram

Under föreläsningen skrev vi ihop [ett enkelt ritprogram][draw_debug.py]. Nu 
ska du utöka det programmet:

- Lägg till knappar för att byta färg. Du kan använda `create_line(x1, y1, x2, 
  y2, fill="yellow")` för att rita en linje med en viss färg, gult i exemplet.

- Lägg till en knapp för att rita rektanglar istället för att dra linjer. Det 
  finns en metod `create_rectangle` som fungerar likt `create_line`.

- Se `pydoc3 tkinter.Canvas` för fler metoder som kan användas.

Det kan se ut såhär:

![Ritprogram med knappar för att byta färg och mellan rektangel och linje][draw.png]

Lösningsförslag:
- [Ritprogram där man kan byta färger][draw_colors.py]
- [Ritprogram där man kan rita rektanglar][draw_rect.py]

[draw.png]: https://github.com/dbosk/intropy/blob/master/modules/graphics/tutorial/draw.png

[draw_debug.py]: https://github.com/dbosk/intropy/blob/master/modules/graphics/tutorial/draw_debug.py

[draw_colors.py]: https://github.com/dbosk/intropy/blob/master/modules/graphics/tutorial/draw_colors.py
[draw_rect.py]: https://github.com/dbosk/intropy/blob/master/modules/graphics/tutorial/draw_rect.py


## Önskemål från gruppen

Vad vill gruppen gå igenom igen från veckan som var?

