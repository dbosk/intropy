# Laboration: Filer och filhantering

Tidigare har vi låtit användaren ange ett följd av $q$-värden som har använts i 
beräkningarna av en talföljd. Ibland kan det bli långa följder, exempelvis om 
vi har månadsräntorna för flera år. Då kan det vara bekvämt att lagra värdena 
på fil och läsa dem därifrån.


## Uppgift

För en längre följd av värden för $q$ blir det jobbigt för användaren att mata 
in dessa för hand. Vanligtvis finns dessa värden att tillgå i en fil.

I denna laboration ska du låta användaren mata in namnet på en fil som 
innehåller värdena för $q$. Därefter läser du in värdena och använder dem i 
ditt program.

Du kan låta användaren mata in $g_1$, värdet för $n$ får du genom antalet 
värden för $q$ som finns i filen. Ett exempel på inmatning:
```
Hur mycket sparkapital har du (ange i kr)? 1000
Ange fil med förväntad ränteutveckling: räntor.txt

         Total       Ökning
Månad 0: 1000.00 kr   0.00 kr
Månad 1: 1020.00 kr  20.00 kr
Månad 2: 1030.20 kr  30.20 kr
```
Samma krav på felhantering som tidigare gäller.


## Extrauppgift

Använd Pythons inbyggda [`csv`-modul][csv] för att läsa in en fil på 
CSV-format. Då kan filen med räntor skapas i ett kalkylarksprogram som Google 
Sheets, LibreOffice Calc eller Microsoft Excel.

[csv]: https://docs.python.org/3/library/csv.html

Om resultaten även skrivs till fil i CSV-format (med hjälp av `csv`-modulen), 
då kan även resultatet importeras tillbaka i kalkylarksprogrammet.

