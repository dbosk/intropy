# Laboration: Iterationer

Hittills har vi antagit att användaren matat in korrekta data, men det är inte 
alltid fallet. I den här laborationen ska vi felsäkra det program vi skrev i 
föregående laboration.


## Uppgift

Skriv en funktion som tar inmatning från användaren och inte returnerar förrän 
användaren har matat in korrekt data. Ersätt all inmatning i förra programmet 
med din nya funktion. Föregående program tog följande inmatning:
```
Data för den aritmetiska summan:
a_1: 1
d: 2
Data för den geometriska summan:
g_1: 1.01
q: 1.10
Antal termer i summorna:
n: 10
Den aritmetiska summan är störst.
```
Men nu ska vi kunna hantera att användaren matar in fel, exempelvis:
```
Data för den aritmetiska summan:
a_1: a
a_1 måste vara ett flyttal, prova igen.
a_1: 1
d: 2
Data för den geometriska summan:
g_1: 1.01
q: b
q måste vara ett flyttal, prova igen.
q: 1.10
Antal termer i summorna:
n: 0
n måste vara större än noll.
n: 10
Den aritmetiska summan är störst.
```

