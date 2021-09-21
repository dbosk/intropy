---
title: Övning om upprepningar
authors:
  - Daniel Bosk <dbosk@kth.se>
---
# Övning: inmatning och villkorssatser

Målet med övningen är att du ska blir bättre på att

  - tillämpa olika former av upprepningar: rekursion, for- och 
    while-iterationer,
  - konstruera interaktiva program,
  - dela upp problem i mindre problem,
  - minimera kodupprepning,
  - leta i Pythons dokumentation.


## Laborationen

Hur har olika grupper löst samma labb? Oftast väldigt olika. Vi går igenom 
några lösningar. Hur löser man extrauppgiften?


## Frågesport

Skriv ett frågeprogram med kluriga frågor. Enklare frågor ska ha ett begränsat 
antal försök, medan svårare frågor ska tillåta oändligt antal försök. Vi vill 
också att användaren ska mata in korrekt, exempelvis om användaren skriver 
"tre" istället för "3" ber vi användaren att skriva in igen. (Ska detta räknas 
som ett försök? Kanske, det får ni avgöra själva.)


## Bombspelet 2.0

Vi har förbättrat vårt frågespel Bomben till Bomben 2.0. Svarar man fel 
detoneras fortfarande bomben, men klurigheterna är uppgraderade.

Det behövs fortfarande två filer: [bomben2.py][bomben2] och [bomb.py][bomb] 
(samma som förra gången). Båda måste ligga i samma katalog. Därefter kör man 
bomben2.py: `python3 bomben2.py`.

[bomben2]: https://github.com/dbosk/intropy/blob/master/modules/iterations/tutorial/bomben2.py
[bomb]: https://github.com/dbosk/intropy/blob/master/modules/conditionals/bomb.py


## Multiplikationshjälpmedel

**Multiplikationstabellen** Låt användaren ange vilken multiplikationstabell 
hen vill se och skriv ut den. Exempelvis 7:ans multiplikationstabell:
```
Vilken multiplikationstabell vill du se? 7

  7 |   7  14  21  28  35  42  49  56  63  70
```

**Multiplikationstabeller** Låt användaren ange vilket maxtal som ska anges i 
multiplikationstabellerna. Skriv sedan ut dem. Exempelvis alla 
multiplikationstabeller upp till 7:
```
Vilket är det högsta tal du vill multiplicera? 7

 * |  1  2  3  4  5  6  7
---+---------------------
 1 |  1  2  3  4  5  6  7
 2 |  2  4  6  8 10 12 14
 3 |  3  6  9 12 15 18 21
 4 |  4  8 12 16 20 24 28
 5 |  5 10 15 20 25 30 35
 6 |  6 12 18 24 30 36 42
 7 |  7 14 21 28 35 42 49
```

Ett lösningsförslag (för båda) finns i [multtable.py][multtable].

[multtable]: https://github.com/dbosk/intropy/blob/master/modules/iterations/tutorial/multtable.py


## Önskemål från gruppen

Vad vill gruppen gå igenom igen från veckan som var?