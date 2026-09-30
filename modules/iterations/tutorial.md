---
title: 'Övning: Upprepningar, listor och moduler'
regex: '^Övning: Upprepningar, listor och moduler$'
published: true
front_page: false
editing_roles: teachers
modules:
  - module: '^Upprepningar, listor och moduler$'
    position: 9
---
Övningen är frivillig och ges för hela klassen, i D37 och på
[Zoom][zoom-room]; tider och plats står i veckoöversikten överst i
modulen. På det första tillfället löser vi uppgifter tillsammans, och på
det andra fortsätter vi med veckans innehåll. Samtidigt leder en
assistent, oftast Emelie, en repetition i ett eget grupprum på Zoom, så
långt tillbaka i kursen som behövs. Uppgifterna och deras
lösningsförslag finns i det interaktiva dokumentet (FeedbackFruits) här
i modulen, *Övning: Upprepningar, listor och moduler
(övningsanteckningar)*: pröva varje uppgift innan du läser lösningen.

[zoom-room]: https://kth-se.zoom.us/j/61952197407

<!-- TODO: FBF-dokumentet skapas av författaren -->

## Vad vi går igenom på övningen

Vi börjar med att bygga ut programmet [lunch.py][lunch] från
föreläsningen, och det gör vi tillsammans: först diskuterar vi hur
utbyggnaden ska utformas, sedan implementerar ni delar av den, och till
sist jämför vi och diskuterar de olika lösningarna. Programmet importerar
modulen [bio.py][bio] från samma föreläsning, så hämta båda filerna och
lägg dem i samma katalog.

[lunch]: https://gits-15.sys.kth.se/dbosk/prgi26/blob/main/f%C3%B6rel%C3%A4sningar/lunch.py
[bio]: https://github.com/dbosk/intropy/blob/bc0b5604f4551e0c1da6ad85f493b093a81f520a/modules/iterations/tutorial/lunch/bio.py

Därefter tar vi ett urval av övningens uppgifter, i den här ordningen:

1. **Uppgift 1: Finn fem fel.** Läsa, köra och rätta ett färdigt
   (rekursivt) program som inte gör vad det ska, [fib.py][fib].
2. **Uppgift 2: Frågorna i en lista.** Lägga tre frågor i en lista och gå
   igenom den både med `for` och med `while`, där de senare programmen
   importerar det första programmets delar i stället för att skriva dem
   igen.
3. **Uppgift 3: Antalet försök.** Bygga ut frågesporten så att en lätt
   fråga ger ett begränsat antal försök och en svår fråga inte gör det.

[fib]: https://github.com/dbosk/intropy/blob/master/modules/iterations/tutorial/examples/fib.py

## På egen hand

Resten av uppgifterna finns kvar att göra på egen tid; lösningsförslagen
i dokumentet låter dig kontrollera dina egna svar.

1. **Uppgift 4: Menyn.** Lägga till en meny som upprepar sig, skriven
   både som en slinga och som ett rekursivt anrop, och avgöra vilken
   form som är bäst.
2. **Uppgift 5: Frågorna i blandad ordning.** Slumpa frågornas ordning
   med modulen `random`, genom att leta i dess dokumentation.
3. **Fördjupning: Uppgift 6: Antalet anrop.** Undersöka hur många anrop
   den rekursiva Fibonaccifunktionen gör, och hur det växer med `n`.
4. **Fördjupning: Uppgift 7: Multiplikationstabellen.** Skriva ut
   multiplikationstabeller med nästlade slingor.
5. **Fördjupning: Uppgift 8: Primtalsfaktorisering.** Skriva en funktion
   som primtalsfaktoriserar ett heltal.
6. **Fördjupning: Uppgift 9: Cowsay.** Skriva ett eget program som
   skriver text i en pratbubbla, som terminalkommandot `cowsay`.

## Förberedelser

Innan övningen bör du ha tagit del av föreläsningen *Föreläsning:
Upprepningar, listor och moduler* här i modulen.

## Efter övningen

Fortsätt enligt veckoöversikten: arbeta i par med *Laboration (3)
upprepningar, listor och moduler*.
