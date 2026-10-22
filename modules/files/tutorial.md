---
title: 'Övning: Filhantering'
regex: '^Övning: Filhantering$'
published: true
front_page: false
editing_roles: teachers
modules:
  - module: '^Filhantering$'
    position: 4
---
Övningen är frivillig och ges för hela klassen, i D37 och på
[Zoom][zoom-room]; tider och plats står i veckoöversikten överst i
modulen. På det första tillfället löser vi uppgifter tillsammans, och på
det andra fortsätter vi med veckans innehåll. Samtidigt leder en
assistent, oftast Emelie, en repetition i ett eget grupprum på Zoom, så
långt tillbaka i kursen som behövs. Uppgifterna och deras
lösningsförslag finns i det interaktiva dokumentet (FeedbackFruits) här
i modulen, *Övning: Filhantering (övningsanteckningar)*: pröva varje
uppgift innan du läser lösningen.

[zoom-room]: https://kth-se.zoom.us/j/61952197407

<!-- TODO: FBF-dokumentet skapas av författaren -->

## Vad vi går igenom på övningen

Vi hinner bara ett urval av övningens uppgifter under passet. De här tar
vi tillsammans, i den här ordningen:

1. **Uppgift 1: Innan filen stängs.** Förutsäga vad ett litet program
   skriver ut när det skriver en rad till en fil och räknar tecknen i
   filen två gånger. Kör sedan programmet, [skrivning.py][skrivning], och
   jämför med din förutsägelse.
2. **Uppgift 2: Frågan om filnamnet.** Skriva en modul med
   hjälpfunktioner som frågar efter en fil att läsa eller skriva till,
   tills svaret duger.
3. **Uppgift 4: Räkna ord och bokstäver.** Räkna ord eller bokstäver i en
   textfil och skriva frekvenstabellen till en ny fil i CSV-format.
   Texten att räkna på finns i [madicken.txt][madicken]. Frågorna
   ställer du med modulen från Uppgift 2; har du ingen egen, hämta
   lösningsförslagets [filer.py][filer].
4. **Uppgift 5: Rövarspråket.** Översätta en fil till eller från
   rövarspråket och skriva översättningen över originalfilen på ett
   säkert sätt. Filen [rövare.txt][rovare] är skriven på rövarspråket.

[skrivning]: https://github.com/dbosk/intropy/blob/master/modules/files/tutorial/examples/skrivning.py
[filer]: https://github.com/dbosk/intropy/blob/master/modules/files/tutorial/examples/filer.py
[madicken]: https://github.com/dbosk/intropy/blob/master/modules/files/tutorial/examples/madicken.txt
[rovare]: https://github.com/dbosk/intropy/blob/master/modules/files/tutorial/examples/r%C3%B6vare.txt

## På egen hand

Resten av uppgifterna finns kvar att göra på egen tid; lösningsförslagen
i dokumentet låter dig kontrollera dina egna svar.

1. **Uppgift 3: Är det en JPEG-bild?** Läsa en fil i binärt läge och
   kontrollera de första byten mot JPEG-formatets signatur. Pröva på
   bilden [bild.jpg][bild] och på en textfil, till exempel
   [madicken.txt][madicken]. Filnamnet frågar du efter med modulen från
   Uppgift 2, eller med lösningsförslagets [filer.py][filer].
2. **Fördjupning: Uppgift 6: Lyckokakor ur en fil.** Läsa och skriva en
   radbaserad databas med slumpvis valda lyckokakor.
3. **Fördjupning: Uppgift 7: Kakor på flera rader.** Utforma ett eget
   filformat som klarar poster på flera rader.
4. **Fördjupning: Uppgift 8: Rövarspråket eller inte?** Sätta ihop
   ordräkningen och översättaren till en analys av vilka bokstäver som
   ändras av översättningen. Har du ingen egen ordräkning eller
   översättare, hämta lösningsförslagets [wc.py][wc] och
   [rövare.py][rovare-py].

[bild]: https://github.com/dbosk/intropy/blob/master/modules/files/tutorial/examples/bild.jpg
[wc]: https://github.com/dbosk/intropy/blob/master/modules/files/tutorial/examples/wc.py
[rovare-py]: https://github.com/dbosk/intropy/blob/master/modules/files/tutorial/examples/r%C3%B6vare.py

## Förberedelser

Innan övningen bör du ha tagit del av föreläsningen *Föreläsning:
Filhantering* här i modulen.

## Efter övningen

Fortsätt enligt veckoöversikten: arbeta i par med *Laboration (6)
filhantering (obligatorisk)*, den sista obligatoriska laborationen före
datorprovet.
