# Laboration: Filer och felhantering

Tidigare har vi låtit användaren ange all information om studenterna. Detta
känns dock inte helt rimligt för administrativ personal på en stor skola att göra,
därför ska vi nu istället låta programmet läsa in den informationen från en fil. 

## Innan du börjar koda

Läs på om [filhantering][filhantering] i Python.

Ladda ner filen [students.csv](https://github.com/dbosk/intropy/files/9403241/students.csv)
och spara den på ett bra ställe på datorn. 

[filhantering]: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

## Uppgift

I denna laboration ska du låta användaren mata in namnet på en fil som 
innehåller alla studenters uppgifter. Därefter läser du in uppgifterna på filen och 
använder dem i ditt program som du skrev i förra laborationen. Om filen inte 
finns ska användaren mata in ett nytt filnamn.

## Exempelutskrift

```
Vad heter filen med alla studenter? students.cs
Den filen fanns inte! Skriv in en ny fil: students.csv

Dessa studenter är skrivna på KTH:
Johan Tierney 8411285597
Erik Bolin 9910247016
Per Edenström 8410024155
...
```

## Krav
* Användaren ska få mata in ett nytt filnamn om filen inte hittas
* Din kod ska uppfylla kraven i rättningsmatrisen
* Din kod ska lämnas in på Canvas som en .py fil

## Extrauppgift 1

Ge användaren möjlighet att lägga till, ändra eller ta bort objekt. 
I slutet av programmet ska alla objekt läsas tillbaka till en fil som 
användaren får skriva in namnet på.

### Exempelutskrift


```
Vad heter filen med alla studenter? students.cs
Den filen fanns inte! Skriv in en ny fil: students.csv

Dessa studenter är skrivna på KTH:
Johan Tierney 8411285597
Erik Bolin 9910247016
Per Edenström 8410024155
...

Vill du lägga till (l), ändra (a) eller ta bort (t) ett objekt? a

Skriv in personnumret på objektet du vill ändra: 0101010000
Vill du ändra namn på Emma Löv (j/n)? j
Skriv in det nya namnet: Ebba Löv

Nu är namnet för 0101010000 ändrat till Ebba Löv!

Ange namn på den fil som uppgifterna ska sparas på: students.csv

Nu är alla uppgifter sparade på filen students.csv
```

## Extrauppgift 2

Lägg till felhantering när programmet läser in en fil. Om det
är något som är fel i filen ska programmet varna användaren för det
och hoppa vidare till nästa rad.

### Exempelutskrift

```
Vad heter filen med alla studenter? students.cs
Den filen fanns inte! Skriv in en ny fil: students.csv

Det är fel på rad 21 i filen students.csv. Hoppar över raden. 

Dessa studenter är skrivna på KTH:
Johan Tierney 8411285597
Erik Bolin 9910247016
Per Edenström 8410024155
...

```

## Extrauppgift 3

Använd Pythons inbyggda [`csv`-modul][csv] för att läsa in en fil på 
CSV-format. Då kan filen med räntor skapas i ett kalkylarksprogram som Google 
Sheets, LibreOffice Calc eller Microsoft Excel.

[csv]: https://docs.python.org/3/library/csv.html

Om resultaten även skrivs till fil i CSV-format (med hjälp av `csv`-modulen), 
då kan även resultatet importeras tillbaka i kalkylarksprogrammet.

