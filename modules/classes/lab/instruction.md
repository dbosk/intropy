---
title: Laboration: Mer klasser och behållare
authors
  - Daniel Bosk <dbosk@kth.se>
  - Celina Soori <celinah@kth.se>
---
# Laboration: Mer klasser och behållare

I förra laborationen använde vi oss av en klass vars objekt vi sparade ner
i en lista. Nu ska vi istället använda oss av två klasser, därav den första
klassen har ett attribut som är en dictionary, där vi sparar ner objekt från
den andra klassen. 

Fördelen med att spara ner objekt på detta vis är att vi kan skapa en mer
strukturerad och användbar kod, vilket gör koden mer lättläst och flexibel.

## Innan du börjar koda

Läs på om [uppslagsverk][uppslagsverk].

[uppslagsverk]: https://docs.python.org/3/tutorial/datastructures.html#dictionaries

## Uppgift

Nu ska vi skriva en klass "School" som har minst ett attribut $students$. 
Attributet $students$ ska vara av typen uppslagsverk. 

Skapa ett objekt av typen School. Låt igen användaren skriva in information om 
minst tre studenter och skapa objekt av typen Student. 

Istället för att spara ner objekten i en lista som vi gjorde i förra laborationen, 
ska objekten nu sparas i skol-objektets attribut $students$. Tänk på vad som är 
rimligt att vi använder som nyckel för ett student-objekt och vad vi använder som värde. 

Avsluta programmet med att skriva ut objektet av typen School.

## Exempelutskrift

```
...
Vad heter studenten? Emma Löv
Vad är studentens personnummer? 010101000a
Personnumret får bara innehålla siffror, försök igen!
Vad är studentens personnummer? 0101010000

Studenten är tillagd!

Här är alla studenter på KTH:
Jan Jansson 0404040010
Per Persson 0303030030
Emma Löv 0101010000

```

## Krav

* Programmet ska uppfylla alla krav nämnda i beskrivningen
* All inmatning ska felhanteras med hjälp av lämplig hjälpfunktion
* Din kod ska uppfylla kraven i rättningsmatrisen
* Din kod ska lämnas in på Canvas som en .py fil

## Kamraträttning

Denna laboration redovisas inte för en lärarassistent, utan kommer kamraträttas av en kurskamrat. När du lämnat in din kod på Canvas kommer du automatiskt bli tilldelad en annan persons kod, som du ska rätta utifrån den rättningsmatris som syns bredvid inlämningen. Ladda ner koden, provkör den på din dator och fyll sedan i rättningsmatrisen. Lämna gärna konstruktiva kommentarer för att hjälpa varandra att bli ännu bättre på att koda!

## Frivillig extrauppgift

Lägg till en klass Person som klassen Student ärver ifrån, se [arv][arv]. 
Skapa en till klass Teacher som också ärver från Person. Lägg till så att
klassen Skola har två attribut, en för studenter och en för lärare, alternativt
hitta på ett eget sätt att hålla isär elever och lärare i ditt program. 

[arv]: https://docs.python.org/3/tutorial/classes.html#inheritance

## Exempelutskrift

```
...
Vad för roll har personen? Lärare
Vad heter personen? Albert Einstein
Vad är personens personnummer? 7903140050

Personen tillagd!

Här är alla studenter på KTH:
Jan Jansson 0404040010
Per Persson 0303030030
Emma Löv 0101010000

Här är alla lärare på KTH:
Albert Einsten 7903140050

```

