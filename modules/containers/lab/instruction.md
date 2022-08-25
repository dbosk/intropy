# Laboration: Klasser, behållare och upprepningar

Hittills i kursen har vi jobbat med existerande datatyper i Python. 
I den här laborationen ska ni istället skapa er egen sammansatta datatyp genom att
skriva er första klass. Ni kommer öva på att skapa objekt av er typ och
att spara ner dessa i en behållare som ni sedan ska iterera igenom.

I laborationen ska ni öva på att representera ett objekt med en sträng. Fördelen med 
att representera objekt på ett bättre sätt är att det underlättar 
för den som ska programmera. Det kan göra koden mer intuitiv, mer läsbar. Detta 
minskar risken för fel (buggar).

## Innan du börjar koda

Läs på om [klasser][klasser], [listor][listor] och [upprepningar][upprepningar].

[klasser]: https://docs.python.org/3/tutorial/classes.html
[listor]: https://docs.python.org/3/library/stdtypes.html#lists
[upprepningar]: https://docs.python.org/3/reference/compound_stmts.html?highlight=while#the-while-statement

## Uppgift

Definiera en klass "Student" som har minst tre attribut, __förnamn__, __efternamn__ och __personnummer__.
Klassen ska ha minst två metoder, __\_init\___ och __\_str\___. 

Skapa minst tre objekt av typen "Student" genom att be användaren skriva in
information om studenter. Fundera på bästa sättet att spara ner de skapade objekten.

När alla objekt är skapade ska programmet skriva ut alla skapade objekt. 

### Exempelutskrift

```
Vad heter studenten? Jan Jansson
Vad är studentens personnummer? 0404040010

Objektet skapat!

Vad heter studenten? Per Persson
Vad är studentens personnummer? 0303030030

Objektet skapat!

Vad heter studenten? Emma Emilsson
Vad är studentens personnummer? 010101000a
Personnumret får bara innehålla siffror, försök igen!
Vad är studentens personnummer? 0101010000

Objektet skapat!

Här är alla sparade objekt:
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

I grunduppgiften kan vi endast lägga till objekt av typen Student. 
Lägg till så att användaren kan ändra och ta bort objekt från listan. 

### Exempelutskrift

```
Vill du lägga till (l), ändra (a) eller ta bort (t) ett objekt? a

Skriv in personnumret på objektet du vill ändra: 0101010000
Vill du ändra namn på Emma Löv (j/n)? j
Skriv in det nya namnet: Ebba Löv

Nu är namnet för 0101010000 ändrat till Ebba Löv!
``` 
