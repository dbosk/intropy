---
title: Övning om filer
authors:
  - Daniel Bosk <dbosk@kth.se>
  - Olle Bälter <ob1@kth.se>
  - Celina Soori <celinah@kth.se>
---
# Övning: filer

Målet med övningen är att du ska blir bättre på att

  - överföra data mellan fil och program, d.v.s.
    - läsa data från filer,
    - lagra data i filer;
  - tillämpa behållare för att lagra mängder med data,
  - se textsträngar som en lista med bokstäver,
  - tillämpa olika former av upprepningar för att arbeta med data,
  - dela upp problem i mindre problem,
  - minimera kodupprepning,
  - konstruera interaktiva program,
  - leta i Pythons dokumentation.


## Önskemål från gruppen

Var det något särskilt från veckans föreläsning och/eller OLI-material som gruppen vill gå igenom igen?

Gick förra veckans laboration bra? Finns det något ni skulle vilja gå igenom från laborationen?

## Övningsuppgifter

### Finn fem fel

Den här övningen ska ni kvalitet-checka en kurskamrats kod.

Förra veckans övning skrev ni ett program för att skapa bankkonton. Byt kod med en annan person i gruppen.
Om du inte var med eller inte hann skriva programmet på förra övningen, byt istället med en annan kod 
du skrivit under en övning!

Läs igenom koden och få ett hum om vad den är tänkt att göra. Testa att köra koden.

Hitta nu minst fem fel/utvecklingsområden i koden (tänk på vad ni lärt er under kursen).

Förbättra nu koden efter det du hittat. Blev koden mer lättläst, användbar och/eller användarvänlig? Varför?

Finns det en gräns till hur mycket man kan komprimera en kod utan att påverka kodens läsbarhet?

### Räkna ord och bokstäver

Skriv ett program som frågar användaren om ett filnamn, läser in filen och 
räknar förekomsten av varje ord i filen.

Låt programmet även fråga användaren om ett filnamn och skriv sedan ut 
resultatet i CSV-format till filen.
```
Vilken fil ska vi analysera? något
Finns ingen fil som heter något, försök igen.
Vilken fil ska vi analysera? madicken.txt
Vill du analysera antalet ord eller bokstäver?
Ange ett av alternativen ['ord', 'bokstäver']: något
Tyvärr är något inte ett av alternativen.
Ange ett av alternativen ['ord', 'bokstäver']: ord
Till vilken fil ska vi skriva resultatet (CSV-format)? madicken.txt
Det finns redan en fil som heter madicken.txt, försök igen.
Till vilken fil ska vi skriva resultatet (CSV-format)? madicken.csv
```
(Ni kan antingen använda Pythons CSV-modul, d.v.s. `import csv`, eller skriva 
ut på egen hand.) Sedan kan ni prova att öppna filen i ett kalkylbladsprogram 
(exempelvis LibreOffice Calc, Microsoft Excel eller Google Sheets).

Exempelfiler att arbeta med:
- [Textfil att räkna ord och bokstäver i, madicken.txt][madicken.txt], [utdrag 
  ur wikipediauppslaget "Madicken (bok)"][madicken-wiki].
- [Resultat av ordräkning, madicken.csv][madicken.csv].

[madicken.txt]: https://github.com/dbosk/intropy/blob/master/modules/files/tutorial/madicken.txt
[madicken-wiki]: https://sv.wikipedia.org/wiki/Madicken_(bok)
[madicken.csv]: https://github.com/dbosk/intropy/blob/master/modules/files/tutorial/madicken.csv

Lösningsförslag:
- [Ett ord- och bokstavsräkningsprogram, wc.py][wc.py],

[wc.py]: https://github.com/dbosk/intropy/blob/master/modules/files/tutorial/wc.py


### Översättare till och från rövarspråket

Skriv ett program som frågar efter ett filnamn, frågar om översättning till 
eller från rövarspråket, läser filen och översätter all text. Översättningen 
ska sedan skriva över originalfilen.

När du har en översättar från rövarspråket tillbaka till vanligt språk kan du 
läsa [filen rövare.txt][rövare.txt].

[rövare.txt]: https://github.com/dbosk/intropy/blob/master/modules/files/tutorial/rövare.txt

Lösningsförslag:
- [Översättare till och från rövarspråket, rövare.py][rövare.py]
- [Ett ord- och bokstavsräkningsprogram, wc.py][wc.py],

[rövare.py]: https://github.com/dbosk/intropy/blob/master/modules/files/tutorial/rövare.py
