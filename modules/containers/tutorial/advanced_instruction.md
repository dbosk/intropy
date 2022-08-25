---
title: Övning om klasser och behållare
authors:
  - Daniel Bosk <dbosk@kth.se>
  - Celina Soori <celinah@kth.se>
---
# Fördjupande övning: Fler behållare och mer klasser

Målet med övningen är att du ska få en djupare förståelse för för hur du ska

  - tillämpa olika behållare för att lagra mängder med data,
  - se textsträngar som en lista med bokstäver,
  - tillämpa olika former av upprepningar för att arbeta med behållarna,
  - skapa enkla klasser för att skapa nya datatyper,
  - dela upp problem i mindre problem,
  - minimera kodupprepning,
  - konstruera interaktiva program,
  - leta i Pythons dokumentation.

## Önskemål från gruppen

Var det något särskilt från veckans föreläsning och/eller OLI-material som gruppen vill gå in djupare på?

Är det någon som vill visa upp något särskilt från förra veckans laboration som kan ge inspiration till gruppen?

## Övningsuppgifter

### Finn fem fel

Den här övningen ska ni kvalitet-checka en kurskamrats kod. 

Förra veckans övning skrev ni ett program för att skapa bankkonton. Byt kod med en annan person i gruppen.

Läs igenom koden och få ett hum om vad den är tänkt att göra. Testa att köra koden.

Hitta nu minst fem fel/utvecklingsområden i koden (tänk på vad ni lärt er under kursen).

Förbättra nu koden efter det du hittat. Blev koden mer lättläst, användbar och/eller användarvänlig? Varför?

Finns det en gräns till hur mycket man kan komprimera en kod utan att påverka kodens läsbarhet?

### Fortune cookies

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


### Ett bättre `cowsay`

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


### `fortune` + `cowsay` = humor

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
