---
title: Laboration om Mer klasser och behållare
authors:
  - Celina Soori <celinah@kth.se>
---
# Laboration: Mer klasser och behållare

I förra laborationen använde vi oss av en klass vars objekt vi sparade i en behållare i huvudprogrammet.
Nu ska vi istället använda oss av två klasser, därav den första
klassen har en behållare som ett attribut, där vi sparar objekt från
den andra klassen. 

Fördelen med att spara ner objekt på detta vis är att vi kan skapa en mer
strukturerad och användbar kod, vilket gör koden mer lättläst och flexibel.

## Innan du börjar koda

Läs på om [uppslagsverk][uppslagsverk].

[uppslagsverk]: https://docs.python.org/3/tutorial/datastructures.html#dictionaries

## Uppgift

Nu ska vi skriva en klass "School" som har minst ett attribut __students__. 

Skapa ett objekt av typen School. Låt igen användaren skriva in information om 
minst tre studenter och skapa objekt av typen Student. 

Spara nu objekten i skol-objektets attribut __students__. 

Fundera på vad som är den bästa typen av behållare för att spara objekten. 
Vilka nackdelar och fördelar finns det med olika behållare?

Avsluta programmet med att skriva ut objektet av typen School.

### Exempelutskrift

```
...
Vad heter studenten? Emma Emilsson
Vad är studentens personnummer? 010101000a
Personnumret får bara innehålla siffror, försök igen!
Vad är studentens personnummer? 0101010000

Studenten är tillagd!

Här är alla studenter på KTH:
Namn: Jan Jansson Personnr: 0404040010
Namn: Per Persson Personnr: 0303030030
Namn: Emma Emilsson Personnr: 0101010000

```

### Krav

* Programmet ska uppfylla alla krav nämnda i beskrivningen
* All inmatning ska felhanteras med hjälp av lämplig hjälpfunktion
* Din kod ska uppfylla kraven i rättningsmatrisen
* Din kod ska lämnas in på Canvas som en .py fil

### Kamraträttning

Denna laboration redovisas inte för en lärarassistent, utan kommer kamraträttas av en kurskamrat. När du lämnat in din kod på Canvas kommer du automatiskt bli tilldelad en annan persons kod, som du ska rätta utifrån den rättningsmatris som syns bredvid inlämningen. Ladda ner koden, provkör den på din dator och fyll sedan i rättningsmatrisen. Lämna gärna konstruktiva kommentarer för att hjälpa varandra att bli ännu bättre på att koda!

## Frivillig extrauppgift

Lägg till en klass Person som klassen Student ärver ifrån, se [arv][arv]. 
Skapa en till klass Teacher som också ärver från Person. Lägg till så att
klassen Skola har två attribut, en för studenter och en för lärare, alternativt
hitta på ett eget sätt att hålla isär elever och lärare i ditt program. 

[arv]: https://docs.python.org/3/tutorial/classes.html#inheritance

### Exempelutskrift

```
...
Vad för roll har personen? Lärare
Vad heter personen? Albert Einstein
Vad är personens personnummer? 7903140050

Personen tillagd!

Här är alla studenter på KTH:
Namn: Jan Jansson Personnr: 0404040010
Namn: Per Persson Personnr: 0303030030
Namn: Emma Emilsson Personnr: 0101010000

Här är alla lärare på KTH:
Namn: Albert Einsten Personnr: 7903140050

```
