---
title: Fördjupande övning om upprepningar
authors:
  - Daniel Bosk <dbosk@kth.se>
---
# Fördjupande övning: upprepningar och moduler

Målet med övningen är att du ska få en djupare förståelse för för hur du ska

  - tillämpa olika former av upprepningar: rekursion, for- och
    while-iterationer,
  - konstruera interaktiva program,
  - dela upp problem i mindre problem,
  - minimera kodupprepning,
  - leta i Pythons dokumentation.


## Önskemål från gruppen

Var det något särskilt från veckans föreläsning och/eller OLI-material som gruppen vill gå in djupare på?

## Övningsuppgifter

### Fibonacci sekvenser

Skriv ett program som räknar ut en Fibonacci-sekvens rekursivt.

För att komma igång:
- Vad är rekursion?
- Hur kan vi skriva en funktion som anropas rekursivt?

[Lösningsförslag](https://github.com/dbosk/intropy/blob/master/modules/iterations/tutorial/fib.py)

Finns det några brister i lösningsförslaget?

### Multiplikationshjälpmedel

**Multiplikationstabellen** Låt användaren ange vilken multiplikationstabell
hen vill se och skriv ut den. Exempelvis 7:ans multiplikationstabell:
```
Vilken multiplikationstabell vill du se? 7

  7 |   7  14  21  28  35  42  49  56  63  70
```

**Multiplikationstabeller** Låt användaren ange vilket maxtal som ska anges i
multiplikationstabellerna. Skriv sedan ut dem. Exempelvis alla
multiplikationstabeller upp till 7:
```
Vilket är det högsta tal du vill multiplicera? 7

 * |  1  2  3  4  5  6  7
---+---------------------
 1 |  1  2  3  4  5  6  7
 2 |  2  4  6  8 10 12 14
 3 |  3  6  9 12 15 18 21
 4 |  4  8 12 16 20 24 28
 5 |  5 10 15 20 25 30 35
 6 |  6 12 18 24 30 36 42
 7 |  7 14 21 28 35 42 49
```

Ett lösningsförslag (för båda) finns i [multtable.py][multtable].

[multtable]: https://github.com/dbosk/intropy/blob/master/modules/iterations/tutorial/multtable.py


### Primtalsfaktorisering

Ett [primtal][primtal] är ett tal som endast är delbart med 1 och sig självt,
exempelvis 2, 3, 5, 7, 11 och 13. [Aritmetikens fundamentalsats][aritfund]
säger att "varje heltal större än 1 kan skrivas som en produkt av primtal på
ett och endast ett sätt" (primtalsfaktorerna är sorterade, $2\cdot 3$ och
$3\cdot 2$ räknas som samma).

Skriv en funktion som tar ett heltal och returnerar en sträng med dess
primtalsfaktorer. Exempelvis: $15 = 3\cdot 5$, $8 = 2\cdot 2\cdot 2$. (Denna
funktion är sannolikt enklast att skriva som en rekursiv funktion.)

[Lösningsförslag för primtalsfaktorisering, primes.py][primes].

[primtal]: https://sv.wikipedia.org/wiki/Primtal
[aritfund]: https://sv.wikipedia.org/wiki/Aritmetikens_fundamentalsats
[primes]: https://github.com/dbosk/intropy/blob/master/modules/iterations/tutorial/primes.py


### Cowsay

I terminalen finns alla möjliga intressanta kommandond. Ett av de lite roligare
är `cowsay`. Det funkar såhär:
```
$ cowsay "Smaka på den här utmaningen!"
 ______________________________
< Smaka på den här utmaningen! >
 ------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```
Skriv en funktion som åstadkommer samma sak som `cowsay`. [Lösningsförslag cowsay.py][cowsay].

[cowsay]: https://github.com/dbosk/intropy/blob/master/modules/iterations/tutorial/cowsay.py
