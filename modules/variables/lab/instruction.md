# Laboration: Variabler och utskrifter

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


## Uppgift

Skriv en funktion som beräknar summan för en aritmetisk talföljd (givet $a_1, 
d, n$ returnera $S^a_n$) och en funktion som beräknar summan för en geometrisk talföljd 
(givet $g_1, q, n$ returnera $S^g_n$).
Skriv ett program som använder funktionerna.
(Kontrollera att funktionerna ger korrekt resultat.)

## Krav

* De två summa-funktionerna ska returnera summan, som sedan ska skrivas ut från huvudprogrammet
* Programmet ska följa de riktlinjer kursen har:
  * Varje funktion ska vara dokumenterad med en docstring
  * Variabel och funktionsnamn ska vara beskrivande och skrivna med snake_case

## Exempelutskrift

```
Den aritmetiska summan är: 11
Den geometriska summan är: 26

```

## Extrauppgift

Lägg till så att användaren måste skriva in värdena för $a_1, d, n$ samt $g_1, q, n$ i början av körningen. 
Räkna därefter ut den aritmetiska och geometriska summan av de värdena användaren skrivit in.

### Exempelutskrift

```
Skriv in värdet på a1: 1
Skriv in värdet på d: 2
Skriv in värdet på n: 3
Den aritmetiska summan är: 5

Skriv in värdet på g1: 2
Skriv in värdet på q: 2
Skriv in värdet på n: 4
Den geometriska summan är: 16

```
