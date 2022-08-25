---
title: Övning om upprepningar
authors:
  - Daniel Bosk <dbosk@kth.se>
  - Celina Soori <celinah@kth.se>
---
# Övning: upprepningar, listor och moduler

Målet med övningen är att du ska bli bättre på att

  - tillämpa olika former av upprepningar: rekursion, for- och
    while-iterationer,
  - konstruera interaktiva program,
  - dela upp problem i mindre problem,
  - minimera kodupprepning,
  - leta i Pythons dokumentation.


## Önskemål från gruppen

Var det något särskilt från veckans föreläsning och/eller OLI-material som gruppen vill gå igenom igen?

Gick förra veckans laboration bra? Finns det något ni skulle vilja gå igenom från laborationen?

## Övningsuppgifter

### Finn fem fel

Programmet [Fibonacci sekvenser](https://github.com/dbosk/intropy/blob/revision_of_exercises/modules/iterations/tutorial/fib.py)
skriver ut en [fibonacci sekvens](https://sv.wikipedia.org/wiki/Fibonaccital). 

Läs igenom koden och få ett hum om vad den är tänkt att göra. Testa att köra koden.

Hitta nu tillsammans minst fem fel/utvecklingsområden i koden (tänk på vad ni lärt er under veckan).

Förbättra nu koden efter det ni hittat. Blev koden mer lättläst, användbar och/eller användarvänlig? Varför?

### Frågesport

Utveckla ditt frågeprogram från förra veckans övning. Enklare frågor ska ha ett begränsat
antal försök, medan svårare frågor ska tillåta oändligt antal försök. Vi vill
också att användaren ska mata in korrekt, exempelvis om användaren skriver
"tre" istället för "3" ber vi användaren att skriva in igen. (Ska detta räknas
som ett försök? Kanske, det får ni avgöra själva.)

Lägg alla frågor i en lista och testa att använda while och for för att iterera genom listan. 
Vad fungerar bäst?

Lägg till en meny för frågesporten och låt användaren köra programmet oändligt många gånger.
Testa att använda for, while och rekursion för att upprepa programmet. Vad fungerar bäst?

Lägg till ett menyval där användaren får lägga till en fråga. 

### Bombspelet 2.0

Vi har förbättrat vårt frågespel Bomben till Bomben 2.0. Svarar man fel
detoneras fortfarande bomben, men klurigheterna är uppgraderade.

Det behövs fortfarande två filer: [bomben2.py][bomben2] och [bomb.py][bomb]
(samma som förra gången). Båda måste ligga i samma katalog. Därefter kör man
bomben2.py: `python3 bomben2.py`.

[bomben2]: https://github.com/dbosk/intropy/blob/master/modules/iterations/tutorial/bomben2.py
[bomb]: https://github.com/dbosk/intropy/blob/master/modules/conditionals/bomb.py
