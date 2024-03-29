---
title: Laboration om Funktioner, variabler och utskrifter
authors:
  - Daniel Bosk <dbosk@kth.se>
  - Celina Soori <celinah@kth.se>
---
# Laboration: Funktioner, variabler och utskrifter

Vi ska nu börja med att använda datorn som den räknemaskin den är. Vi ska 
arbeta med [aritmetiska][aritmetiska] och [geometriska][geometriska] följder. 
Denna typ av följder är tämligen användbara, exempelvis kan geometriska följder 
användas för att räkna på ränteutveckling (bl.a. lån och sparande).

[aritmetiska]: https://sv.wikipedia.org/wiki/Aritmetisk_f%C3%B6ljd
[geometriska]: https://sv.wikipedia.org/wiki/Geometrisk_f%C3%B6ljd

Fördelen med att börja med denna typ av följder är att vi enkelt kan beräkna 
dem för hand. Detta betyder att vi enkelt kan kontrollera korrektheten i våra 
program.


## Aritmetiska följder

I en aritmetisk följd är differensen mellan två element konstant. Exempelvis, 
$$
  1, 2, 3, 4, \ldots
$$ är en aritmetisk följd där differensen är ett.

Låt oss säga att det första elementet i följden är $a_1$ och differensen är 
$d$. Då kan vi beräkna $a_n = a_1 + d\cdot (n-1)$.

Vi kan även beräkna summan $S^a_n = a_1 + \cdots + a_n =
n \frac{a_1 + a_n}{2}$.


## Geometriska följder

I en geometrisk följd är det istället kvoten mellan elementen som är konstant. 
Exempelvis, $$
  1, 2, 4, 8, 16, \ldots
$$ är en geometrisk följd där kvoten är två.

Låt oss säga att det första elementet i följden är $g_1$ och kvoten är $q$. Då 
kan vi beräkna $g_n = g_1 q^{n-1}$. (Operationen "upphöjt till" har en 
annorlunda notation i Python, $a^b$ skrivs `a**b` medan $a\cdot b$ skrivs som 
det förväntade `a*b`.)

Vi kan även beräkna summan $S^g_n = g_1 + \cdots + g_n =
g_1 \frac{q^n-1}{q-1}$.

## Innan du börjar koda

Se till att du har koll på hur [parametrar][parametrar], [argument][argument] och [funktioner][funktioner] fungerar i Python.
Kom även ihåg att använda [pylint][pylint] när du kodar. 

[parametrar]: https://docs.python.org/3/glossary.html#term-parameter
[argument]: https://docs.python.org/3/glossary.html#term-argument
[funktioner]: https://docs.python.org/3/reference/compound_stmts.html#function
[pylint]: https://pypi.org/project/pylint/

## Uppgift

Skriv en funktion som beräknar summan för en aritmetisk talföljd (givet $a_1, 
d, n$ returnera $S^a_n$) och en funktion som beräknar summan för en geometrisk 
talföljd (givet $g_1, q, n$ returnera $S^g_n$).
Skriv ett program som använder funktionerna.
(Kontrollera att funktionerna ger korrekt resultat.)

### Exempelutskrift

```
Den aritmetiska summan är: 11
Den geometriska summan är: 26
```

### Krav

* De två summa-funktionerna ska returnera summan, som sedan ska skrivas ut från 
  huvudprogrammet.
* Din kod ska uppfylla kraven i rättningsmatrisen.

### Kamraträttning

Denna laboration redovisas inte för en lärarassistent, utan kommer kamraträttas av en kurskamrat.
När du lämnat in din kod på Canvas kommer du automatiskt bli tilldelad en annan persons kod, som
du ska rätta utifrån den rättningsmatris som syns bredvid inlämningen. Ladda ner koden, provkör den
på din dator och fyll sedan i rättningsmatrisen. Lämna gärna konstruktiva kommentarer för att hjälpa
varandra att bli ännu bättre på att koda! 

## Frivillig extrauppgift

Lägg till så att användaren måste skriva in värdena för $a_1, d, n$ samt $g_1, q, n$. 
Räkna därefter ut den aritmetiska respektive geometriska summan av de värdena användaren skrivit in.

### Exempelutskrift

```
Skriv in startvärdet (a1): 1
Skriv in differensen (d): 2
Skriv in antal element i följden (n): 3
Den aritmetiska summan är: 9

Skriv in startvärdet (g1): 2
Skriv in kvoten (q): 2
Skriv in antal element i följden (n): 4
Den geometriska summan är: 30
```
