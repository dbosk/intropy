---
title: Övning om behållare
authors:
  - Daniel Bosk <dbosk@kth.se>
---
# Övning: upprepningar

Målet med övningen är att du ska blir bättre på att

  - tillämpa behållare för att lagra mängder med data,
  - se textsträngar som en lista med bokstäver,
  - tillämpa olika former av upprepningar för att arbeta med behållarna,
  - dela upp problem i mindre problem,
  - minimera kodupprepning,
  - konstruera interaktiva program,
  - leta i Pythons dokumentation.


## Laborationen

Hur har olika grupper löst samma labb? Oftast väldigt olika. Vi går igenom 
några lösningar. Hur löser man extrauppgiften?


## Förfina fulkoden!

Vi har lagt vantarna på lite fulkod. Fulkod är vi allergiska emot, så vi 
behöver omedelbart fixa den till finkod. Finkod uppfyller kriterierna:

- Informativa utskrifter
- Enkel inmatning
- Kommentarer
- Beskrivande namn
- Konsekvent språk och typografi
- Uppdelning i funktioner/metoder/moduler
- Parametrar och returvärden
- Ingen kodupprepning

Fulkoden som behöver fixas är följande:

- [Ett gissningsspel, guess.py][guess.py]
  ([lösningsförslag, guess-good.py][guess-good.py])
- [En multiplikationskolumn, multcol.py][multcol.py]
- [En multiplikationstabell, multtable.py][multtable.py]
  ([lösningsförslag, multtable-good.py][multtable-good.py])

[guess.py]: https://github.com/dbosk/intropy/blob/master/modules/containers/tutorial/guess.py
[guess-good.py]: https://github.com/dbosk/intropy/blob/master/modules/containers/tutorial/guess-good.py
[multcol.py]: https://github.com/dbosk/intropy/blob/master/modules/containers/tutorial/multcol.py
[multtable.py]: https://github.com/dbosk/intropy/blob/master/modules/containers/tutorial/multtable.py
[multtable-good.py]: https://github.com/dbosk/intropy/blob/master/modules/containers/tutorial/multtable-good.py


## Fortune cookies

Det finns många intressanta kommandon i den UNIX-lika terminalen. Förra 
övningen nämnde vi `cowsay`. Det finns även ett kommando `fortune` som ger 
lustiga korta utsagor och citat:
```
(0|13:23)dbosk@X1:tutorial (master)
$ fortune
Q:      What is printed on the bottom of beer bottles in Minnesota?
A:      Open other end.
(0|13:23)dbosk@X1:tutorial (master)
$ fortune
Go not to the elves for counsel, for they will say both yes and no.
                -- J.R.R. Tolkien
(0|13:24)dbosk@X1:tutorial (master)
$ fortune
You never hesitate to tackle the most difficult problems.
(0|13:24)dbosk@X1:tutorial (master)
$
```
Skriv ett program som skriver ut en slumpvis vald humoristisk "fortune cookie" 
relaterad till era studier. Exempelvis:
```
$ python3 fortune.py
Alla kommer att få A på matematiktentan!
$ python3 fortune.py
Det är en lovande dag för dig!
```


## Ett bättre `cowsay`

Förra övningen hade vi med en uppgift att implementera [en enkel version av 
kommandot `cowsay`][cowsay.py]. Resultatet när man körde programmet såg ut 
något i stil med följande:
```
 --------------------------------------------------------
| Smaka på den här utmaningen! Fast så svår är den inte. |
 --------------------------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\ 
                ||----w |
                ||     ||
```

Om texten blir för lång funkar inte programmet då skärmbredden tar slut. Nu 
vill vi kunna hantera längre texter genom att bryta dem till lagom långa rader,
exempelvis:
```
 -------------------------------
|  Smaka på den här utmaningen! |
|  Fast så svår är den inte.    |
 -------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\ 
                ||----w |
                ||     ||
```

[cowsay.py]: https://github.com/dbosk/intropy/blob/master/modules/containers/tutorial/cowsay.py


## `fortune` + `cowsay` = humor

Skriv dina fortune- och cowsay-program som moduler och kombinera dem:
```
 ---------------------------
|  Alla kommer att          |
|  få A på matematiktentan! |
 ---------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\ 
                ||----w |
                ||     ||
```
När ni känner er nöjda finns följande lösningsförslag:

- [fortune.py][fortune.py],
- [radbrytande cowsay_good.py][cowsay_good.py].

[fortune.py]: https://github.com/dbosk/intropy/blob/master/modules/containers/tutorial/fortune.py
[cowsay_good.py]: https://github.com/dbosk/intropy/blob/master/modules/containers/tutorial/cowsay_good.py


## Önskemål från gruppen

Vad vill gruppen gå igenom igen från veckan som var?
