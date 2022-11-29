# Granskningsprotokoll

**Granskning av:** «Fyll i ditt namn»

**Utvecklare:** «Fyll i utvecklarens namn (den student som har
implementerat P-Uppgiften)»

**Datum:** «Fyll i datum»

Mer detaljerad information om kraven som ställs i granskningsprotokollet
finner du i slutet av dokumentet under rubriken [Information om
granskningen](#anchor) på sidan [4](#anchor).

Användarvänlighet
=================

1. Informativa utskrifter («"Ja" eller "Nej"»)
----------------------------------------------

«Fyll i din motivering till ditt svar här»

«Exempel (om "Ja"): Programmets gränssnitt är tillräckligt tydligt för
att en användare utan tidigare förkunskaper om P-uppgiften kan förstå
vad det handlar om och vad som händer i programmet.»

«Exempel (om "Nej"): Det första man ser när man startar programmet är
att det frågas om ett tal, det är otydligt vad programmet gör och vad
talet är till för.»

2. Enkel inmatning («"Ja" eller "Nej"»)
---------------------------------------

«Fyll i din motivering till ditt svar här»

«Exempel (om "Ja"): Det är enkelt att använda programmet p.g.a. att
frågorna som ställs till användaren alltid är tydliga. Vi vet att det är
ett Memory program utifrån tidigare utskrifter, och vi vet därför vad
frågan "Vilken storlek på spelet vill du ha \[t.ex. 5\]?" innebär.»

«Exempel (om "Nej"): Det är otydligt för användaren vad som ska matas
in. Speciellt på menyn där ingen numrering finns för alternativen.»

Programmerarvänlighet
=====================

3. Vettiga namn («"Ja" eller "Nej"»)
------------------------------------

«Fyll i din motivering till ditt svar här»

4. Kommentarer («"Ja" eller "Nej"»)
-----------------------------------

«Fyll i din motivering till ditt svar här»

5. Konsekvent språk («"Ja" eller "Nej"»)
----------------------------------------

«Fyll i din motivering till ditt svar här»

6. Konsekvent typografi («"Ja" eller "Nej"»)
--------------------------------------------

«Fyll i din motivering till ditt svar här»

Strukturering
=============

7. Lämplig uppdelning i funktioner («"Ja" eller "Nej"»)
-------------------------------------------------------

«Fyll i din motivering till ditt svar här»

8. Lämplig uppdelning i klasser/moduler («"Ja" eller "Nej"»)
------------------------------------------------------------

«Fyll i din motivering till ditt svar här»

9. Temporära variabler så lokalt som möjligt («"Ja" eller "Nej"»)
-----------------------------------------------------------------

«Fyll i din motivering till ditt svar här»

10. Återanvändbara funktioner/moduler/klasser («"Ja" eller "Nej"»)
------------------------------------------------------------------

«Fyll i din motivering till ditt svar här»

11. In- och utdata till funktioner («"Ja" eller "Nej"»)
-------------------------------------------------------

«Fyll i din motivering till ditt svar här»

12. Flexibelt/utbyggbart program («"Ja" eller "Nej"»)
-----------------------------------------------------

«Fyll i din motivering till ditt svar här»

13. Ingen kodupprepning («"Ja" eller "Nej"»)
--------------------------------------------

«Fyll i din motivering till ditt svar här»

14. Ingen hårdkodning («"Ja" eller "Nej"»)
------------------------------------------

«Fyll i din motivering till ditt svar här»

Obligatoriskt
=============

15. Uppfyller kraven i lydelsen («"Ja" eller "Nej"»)
----------------------------------------------------

«Fyll i din motivering till ditt svar här»

Omdöme
======

Projektet anses vara godkänt om alla krav under "Obligatoriskt" är
uppfyllda och att inte fler än *två* krav under "Användarvänlighet",
"Programmerarvänlighet" och "Strukturering" är ouppfyllda.

**Godkänt: «"Ja" eller "Nej"»**

[]{#anchor}Information om granskningen
======================================

Nedan finner du mer detaljerad information om kraven som ställs i
granskningsprotokollet.

1. Informativa utskrifter
-------------------------

Programmet ska tala om för användaren vad programmet gör i varje steg
och vilken inmatning som förväntas. Ett dåligt exempel kan se ut så här.

*Ge tal1 : *26*\
och tal2 : *54*\
29 31 37 41 43 47 53*

Man ska inte behöva titta i en manual eller ännu värre, i själva
programkoden för att förstå vad som händer. Programmet måste vara
självinstruerande.

*Hej och välkommen till primtalsprogrammet. Programmet\
skriver ut alla primtal i ett intervall du definierar.\
\
Ange undre gränsen i intervallet: *26*\
Ange högre gränsen i intervallet: *54*\
De primtal som finns mellan 26 och 54 är:\
29 31 37 41 43 47 53*

Den senare varianten är mycket lättare att förstå när man kör
programmet.

2. Enkel inmatning
------------------

Inmatningen ska inte vara onödigt krånglig.

*\...\
Vill du boka en biljett? *ja*\
Varifrån åker du? *Arlanda*\
Vart ska du åka? *Kastrup*\
Vilken månad ska du åka? *Mars*\
Vilken dag ska du åka? *25*\
Vill du boka returbiljett? *ja*\
Vilken månad ska du tillbaka? *April*\
Vilken dag ska du tillbaka? *5*\
Det går tyvärr inget flyg den 25 mars.\
Försök igen\
\
Vill du boka en biljett? *ja*\
Varifrån åker du? *Arlanda*\
Vart ska du åka? *Kastrup*\
Vilken månad ska du åka? *Mars*\
\...\
\
*Förutom att vara väldigt sen med att kläcka ur sig att det inte finns
något flyg den önskade resdagen så verkar det inte finnas något sätt att
boka en mängd biljetter. Att boka en klassresa med det systemet skulle
vara väldigt enerverande.

3. Vettiga namn
---------------

Programmet ska ha intuitiva namn på variablerna. För den som skrivit
programmet är allt självklart, men inte för andra.

Nedanstående programkod är ganska svår att tyda

namn = 0

kalle = 0

while kalle \< len(pelle):

if pelle\[kalle\] \> namn:

namn = pelle\[kalle\]

kalle = kalle + 1

Här följer samma kod med andra variabelnamn.

max = 0

i = 0

while i \< len(lista):

if lista\[i\] \> max:

max = lista\[i\]

i = i + 1

Man ser nu lättare vad koden gör, nämligen sparar undan det högsta
värdet i listan till variabeln max. Fortfarande är inte namnet på listan
optimalt. Vad för slags värden innehåller den? Är det löner,
skottstatistik eller vad?

När det gäller en funktion eller metod brukar ett bra namn oftast vara
ett verb som beskriver vad den gör eller vad den returnerar. Booleska
funktioner (som returnerar True/False) bör ha ett namn som talar om hur
läget är det fall den returnerar True, t ex *korrekt()* för en funktion
som kontrollerar om ett värde är korrekt.

Namnet på en klass kan vara ett substantiv som beskriver vad objektet
representerar. Variabler och attribut är också substantiv. Att komma på
bra namn kräver en del arbete!

4. Kommentarer
--------------

Alla klasser och funktioner måste kommenteras. Syftet med
klassen/funktionen ska framgå. Det ska räcka att läsa kommentaren för
att förstå hur en funktion ska användas (man ska inte behöva sätta sig
in i hela koden).

In- och utdata till funktioner måste kommenteras. Det gäller både
returvärden och parametrar. Om funktionen är en metod och den ändrar
något attribut ska detta också kommenteras.

Kommentarerna ska inte förklara hur Python fungerar. Förutsättningen är
att den som läser källkoden redan vet hur man programmerar. Kommentarer
som förklarar t ex att en if-sats gör ett val och att en slinga upprepar
något ska inte vara med vid redovisningen. Den som redovisar måste själv
veta sådant utan anteckningar.

5. Konsekvent språk
-------------------

Språkvalet ska vara konsekvent. Alla variabel-, klass- och funktionsnamn
på ett språk. Alla kommentarer på ett språk. Det är OK att ha engelska
variabel/metodnamn och kommentera på svenska. Undvik svengelska (sejva
svenska språket).

6. Konsekvent typografi
-----------------------

Programmet ska ha en genomgående typografi. Namn som är sammansatta av
flera ord kan t ex skrivas ihop genom att inleda varje nytt ord med stor
bokstav (t ex summeraVikter), eller genom att skilja orden åt med
understreck (t ex summera\_vikter), men använd samma variant genom hela
ditt program. Variabel- och metodnamn brukar inledas med med liten
bokstav och klasser med stor bokstav.

class EnBraKlass

def enMetodSomTarTreParametrar(x, y, z)

7. Lämplig uppdelning i funktioner/metoder
------------------------------------------

Bäst är det med specialiserade funktioner som bara gör en sak.

def läs\_från\_filen():

filnamn = input(\"Vad heter filen?\")

with open(filnamn, \"r\") as infil:

lista = infil.readlines()

lista2 = \[\]

for element in lista:

if type(element) == type(0):

lista2.add(element)

return lista2

Koden ovan gör flera saker; frågar efter en fil, läser in alla data från
filen, stoppar in heltalen i en heltalsvektor och returnerar denna. Det
vore bättre att dela upp dessa uppgifter på flera funktioner så att
funktionsanropen blir:

filnamn = fråga\_fil()

fildata = läs\_från\_filen(filnamn)

intresseanta\_tal = konvertera(fildata)

Programmet blir då mer flexibelt: Funktionen *fråga\_fil* kan skrivas om
till ett grafiskt GUI där man klickar på rätt fil. Funktionen
*läs\_från\_filen* kan användas i andra sammanhang då man vill läsa från
fil. Man kan skicka fildatan till en ny metod som kontrollerar data
innan man anropar konvertera.

8. Lämplig uppdelning i klasser/moduler
---------------------------------------

Data som hör ihop (t ex namn, födelsedata och adressuppgifter för en
person) kan samlas genom att dom får vara attribut i en klass.
Funktioner som hör ihop med dessa data får bli klassens metoder. Ett
program kan ha flera olika klasser!

Ett riktigt stort program kan man dela upp i flera moduler, där de
klasser som hör ihop samlas i en modul.

9. Temporära variabler så lokalt som möjligt
--------------------------------------------

Se till att tillfälliga variabler skapas så lokalt som möjligt. En
variabel som bara används inuti en slinga i en metod ska inte vara ett
attribut i klassen, utan en lokal variabel i metoden.

10. Återanvändbara funktioner/klasser
-------------------------------------

En del uppgifter kan delas upp i klasser som går att återanvända i andra
program. T ex kan en klass som representerar ett spelkort användas i
olika kortspelsprogram.

Funktioner ska om möjligt vara skrivna så att dom går att använda i
andra sammanhang. Ett knep är att se till att alla indata ges som
parametrar. Ett annat är att specialisera funktionerna, så att varje
funktion bara gör en liten del.

11. In- och utdata till funktioner
----------------------------------

Var noga med in och utdata till funktionerna. En del funktioner som
t.ex. bara skriver ut på skärmen kan vara parameterlösa och inte
returnera något. Övriga funktioner bör ha alla indata som parametrar och
utdata som returvärden.

12. Flexibelt/utbyggbart program
--------------------------------

Skriv ditt program så att det lätt att utöka och bygga ut. Några
exempel: I ett program som samlar data om Pokémon ska man kunna lägga
till fler Pokémon utan att gå in och ändra i programmet. Om ett program
läser in från fil ska det vara lätt att byta till en annan fil. Om man
vill lägga till en beräkning så ska det vara enkelt att stoppa in en
funktion för det, utan att behöva ändra på många ställen i programmet.

13. Ingen kodupprepning
-----------------------

Ett vanligt nybörjarfel när man programmerar är att använda taktiken
klippa och klistra när samma sak ska göras på flera ställen i
programmet. Detta leder dock till kod som är väldigt svår att
underhålla. Om man ändrar på ett ställe måste man göra samma ändring på
flera parallellställen. Det går i regel att skriva om den upprepade
koden till en funktion med parametrar och returvärde.

14. Ingen hårdkodning
---------------------

Förekommer talet 5 på flera ställen i programmet? Om man behöver använda
siffervärden kan dessa deklareras som konstanter.

ANTAL\_SPELARE = 5

PI = 3.14

15. Uppfyller kraven i lydelsen
-------------------------------

Programmet måste uppfylla kraven i P-uppgiftslydelsen. Det är inte
tillåtet att förenkla uppgiften. Den som vill göra några förändringar
måste förankra det med kursledaren först, och kunna visa en bekräftelse
(ett e-post t.ex.) på att kursledaren godkänt kravförändringar.

Versionsinformation
===================

Första versionen av denna granskningsmall skrevs av Mazen Mardini, med
tillägg av Celina Soori, den 28 och 29 november 2022.
