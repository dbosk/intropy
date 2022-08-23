# Laboration: Inmatning och styrstrukturer

I denna laboration ska vi utöka programmet vi skrev i föregående laboration.
I föregående laboration skrev vi två funktioner, en som beräknar en aritmetisk 
summa och en som beräknar en geometrisk summa.

## Innan du börjar koda

Läs på om [styrstrukturer][styrstrukturer] och hur [inmatning][inmatning] sker i Python.

[styrstrukturer]: https://docs.python.org/3/reference/compound_stmts.html#
[inmatning]: https://docs.python.org/3/library/functions.html#input

## Uppgift

Låt användaren mata in värdena för $a_1, d, g_1, q$ och $n$. Efter att summorna 
är beräknade, använd lämplig styrstruktur för att skriva ut enligt följande:

- "Den aritmetiska summan är störst" om den aritmetiska summan är (strikt) 
  större än den geometriska,
- "Den geometriska summan är störst" om den geometriska är (strikt) störst,  
  eller
- "Summorna är lika" om de är lika.

## Exempelutskrift
```
Data för den aritmetiska summan:
Skriv in startvärdet (a1): 1
Skriv in differensen (d): 2

Data för den geometriska summan:
Skriv in startvärdet (g1): 1.01
Skriv in kvoten (q): 1.10

Antal termer i summorna:
Skriv in antal element i följden (n): 10
Den aritmetiska summan är störst.
```

## Krav

* Den aritmetiska och geometriska summan ska använda sig av samma $n$
* Din kod ska uppfylla kraven i rättningsmatrisen
* Din kod ska lämnas in på Canvas som en .py fil
 
## Kamraträttning

Denna laboration redovisas inte för en lärarassistent, utan kommer kamraträttas av en kurskamrat. När du lämnat in din kod på Canvas kommer du automatiskt bli tilldelad en annan persons kod, som du ska rätta utifrån den rättningsmatris som syns bredvid inlämningen. Ladda ner koden, provkör den på din dator och fyll sedan i rättningsmatrisen. Lämna gärna konstruktiva kommentarer för att hjälpa varandra att bli ännu bättre på att koda!

## Frivillig extrauppgift

Låt programmet först fråga användaren om en summa är aritmetisk eller 
geometrisk. På så vis kan användaren jämföra en aritmetisk summa med en 
geometrisk eller två aritmetiska summor.

### Exempelutskrift
```
Är den första summan [a]rtimetisk eller [g]eometrisk? a
Skriv in startvärdet (a1): 1.02
Skriv in differensen (d): 0.1

Är den andra summan [a]ritmetisk eller [g]eometrisk? g
Skriv in startvärdet (g1): 1.02
Skriv in kvoten (q): 1.1

Hur många termer (n)? 10
Den andra summan är störst.
```
