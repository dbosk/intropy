# Laboration: Iterationer

Hittills har vi antagit att användaren matat in korrekta data, men det är inte 
alltid fallet. I den här laborationen ska vi felsäkra det program vi skrev i 
föregående laboration.


## Uppgift

Skriv en funktion som tar inmatning från användaren och inte returnerar förrän 
användaren har matat in korrekt data. Ersätt all inmatning i förra programmet 
med din nya funktion. Föregående program tog följande inmatning:
```
n: 3
q_1: 1.02
q_2: 1.05
q_3: 1.04
g_1: 1000
Summan blir: 1113.84
```
Men nu ska vi kunna hantera att användaren matar in fel, exempelvis:
```
n: 0
n måste vara större än 0, prova igen.
n: 3
q_1: 1.02
q_2: 1.05
q_3: a
q_3 måste vara ett flyttal, prova igen.
q_3: 1.04
g_1: 1000
Summan blir: 1113.84
```

