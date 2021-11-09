---
title: Övning om filer
authors:
  - Daniel Bosk <dbosk@kth.se>
  - Olle Bälter <ob1@kth.se>
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


## Laborationen

Hur har olika grupper löst samma labb? Oftast väldigt olika. Vi går igenom 
några lösningar. Hur löser man extrauppgiften?


## Fortune cookies

Under förra övningen skrev vi ett program som heter `fortune.py`. Det skriver 
ut en slumpvis vald humoristisk "fortune cookie" relaterad till era studier. 
Exempelvis:
```
$ python3 fortune.py
Alla kommer att få A på matematiktentan!
$ python3 fortune.py
Det är en lovande dag för dig!
```
I den förra versionen hårdkodade vi databasen med fortunes i programmet. Nu ska 
vi lagra dem på fil. Ändra programmet så att det läser alla fortunes från en 
fil.

### Extra utmaning med fortune och cowsay

Hantera fortunes som innehåller flera rader. Anpassa även `cowsay.py` så att 
den kan hantera flerradiga inmatningar utan problem.
```
 ---------------------------------
| Vi vill även ha fortunes som    |
| kan vara flera rader.           |
|                                 |
| Och till och med flera stycken. |
 ---------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\ 
                ||----w |
                ||     ||
```

Hint: dela först upp i stycken, därefter meningar med ord.

Filer i lösningsförslaget:

- [Ett förbättrat fortune-program, fortune_better.py][fortune_better.py],
- [En fortunesdatabas, fortunes.txt][fortunes.txt]
- [En förbättrad cowsay-funktion, cowsay_better.py][cowsay_better.py],

[fortune_better.py]: https://github.com/dbosk/intropy/blob/master/modules/files/tutorial/fortune_better.py
[cowsay_better.py]: https://github.com/dbosk/intropy/blob/master/modules/files/tutorial/cowsay_better.py
[fortunes.txt]: https://github.com/dbosk/intropy/blob/master/modules/files/tutorial/fortunes.txt


## Räkna ord och bokstäver

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


## Översättare till och från rövarspråket

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


## Rövarspråket eller inte?

Skriv ett program som använder `wc`- och `rövare`-modulerna ovan för att 
undersöka hur bokstavsförekomsterna förändras när en text översätts till 
rövarspråket.

Lösningsförslag:
- [Analysprogram som jämför text med översättning till rövarspråket, 
  analys.py][analys.py]

[analys.py]: https://github.com/dbosk/intropy/blob/master/modules/files/tutorial/analys.py


## Önskemål från gruppen

Vad vill gruppen gå igenom igen från veckan som var?
