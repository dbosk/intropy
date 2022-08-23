# Laboration: Upprepningar och felhantering

Hittills har vi antagit att användaren matat in korrekta data, men det är inte 
alltid fallet. I den här laborationen ska vi felsäkra det program vi skrev i 
föregående laboration med hjälp av egna felhanteringsfunktioner. De funktioner 
vi skriver i denna laboration kommer vara bra verktyg att ha för kommande 
laborationer! 

## Innan du börjar koda

Läs på om [felhantering][felhantering] samt om [moduler][moduler]. 

[felhantering]: https://docs.python.org/3/tutorial/errors.html
[moduler]: https://docs.python.org/3/tutorial/modules.html#:~:text=A%20module%20is%20a%20file,global%20variable%20__name__%20.


## Uppgift

I denna laboration kommer vi använda oss av en egenskriven modul som vi 
importerar in i vårt huvudprogram. Denna modul ska innehålla två funktioner, 
en som kontrollerar att input är en int och en som kontrollerar om input är en float. 
De två funktionerna ska ta inmatning från användaren och inte returnera förrän 
användaren har matat in korrekt data. 

Ert huvudprogram kommer efteråt likna programmet nedan (med bättre variabelnamn):

```python
import check_input_library as check_input

def sum_arithmetic(a1, d, n):
  # Here goes your code from earlier labs

def sum_geometric(g1, q, n):
  # Here goes your code from earlier labs

def main():
  a1 = check_input.is_float("Skriv in värdet på a1: ")
  d = check_input.is_float("Skriv in värdet på d: ")
  n = check_input.is_int("Skriv in värdet på n: ")
  
  arithmetic = sum_arithmetic(a1, d, n)
  
  g1 = check_input.is_float("Skriv in värdet på a1: ")
  q = check_input.is_float("Skriv in värdet på d: ")
  
  geometric = sum_geometric(g1, q, n)
  
  # and then your code to compare the two sums
  
```
## Exempelutskrift
```
Data för den aritmetiska summan:
a_1: a
a_1 måste vara ett flyttal, prova igen.
a_1: 1
d: 2
Data för den geometriska summan:
g_1: 1.01
q: b
q måste vara ett flyttal, prova igen.
q: 1.10
Antal termer i summorna:
n: 0
n måste vara större än noll.
n: 10.2
n måste vara ett heltal.
n: 10
Den aritmetiska summan är störst.
```

## Krav

* Felhanteringsfunktionerna ska vara i en separat modul som importeras in i huvudprogrammet
* All inmatning ska felhanteras med hjälp av passande hjälpfunktion
* Användaren ska ha oändligt antal försök på sig att mata in rätt värden 
* Ditt program ska kunna hantera alla testfall som visas i exempelutskriften
* Din kod ska uppfylla kraven i rättningsmatrisen
* Din kod ska lämnas in på Canvas som en .py fil

## Redovisning

Denna laboration ska redovisas för en lärarassistent på ett laborationstillfälle. Information 
om bokning av redovisningstillfälle kommer komma upp på Canvas. På redovisningen ska du kunna
köra ditt program och beskriva din kod detaljerat. 

## Frivillig extrauppgift

Läs om [paketering][packaging] i Python och gör din modul installerbar 
genom `pip`. Då kan andra enkelt installera din modul på sina system.

[packaging]: https://packaging.python.org/tutorials/packaging-projects/
