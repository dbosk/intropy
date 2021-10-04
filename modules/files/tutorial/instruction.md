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

- [fortune_better.py][fortune_better.py],
- [fortunes.txt][fortunes.txt]
- [cowsay_better.py][cowsay_better.py],

[fortune_better.py]: https://github.com/dbosk/intropy/blob/master/modules/files/tutorial/fortune_better.py
[cowsay_better.py]: https://github.com/dbosk/intropy/blob/master/modules/files/tutorial/cowsay_better.py
[fortunes.txt]: https://github.com/dbosk/intropy/blob/master/modules/files/tutorial/fortunes.txt


## Önskemål från gruppen

Vad vill gruppen gå igenom igen från veckan som var?
