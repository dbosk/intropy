---
title: Övning om klasser och objekt
authors:
  - Daniel Bosk <dbosk@kth.se>
  - Celina Soori <celinah@kth.se>
---
# Övning: klasser och objekt

Målet med övningen är att du ska bli bättre på att

  - använda och konstruera sammansatta datatyper (klasser),
  - tillämpa behållare för att lagra mängder med data,
  - tillämpa olika former av upprepningar för att arbeta med data,
  - dela upp problem i mindre problem,
  - minimera kodupprepning,
  - leta i Pythons dokumentation.


## Önskemål från gruppen

Var det något särskilt från veckans föreläsning och/eller OLI-material som gruppen vill gå igenom igen?

Gick förra veckans laboration bra? Finns det något ni skulle vilja gå igenom från laborationen?

### Finn fem fel

Programmet [En multiplikationstabell](https://github.com/dbosk/intropy/blob/master/modules/containers/tutorial/multtable.py) skriver ut en multiplikationstabell.

Läs igenom koden och få ett hum om vad den är tänkt att göra. Testa att köra koden.

Hitta nu tillsammans minst fem fel/utvecklingsområden i koden (tänk på vad ni lärt er under veckan).

Förbättra nu koden efter det ni hittat. Blev koden mer lättläst, användbar och/eller användarvänlig? Varför?

([Lösningsförslag]([multtable-good.py](https://github.com/dbosk/intropy/blob/master/modules/containers/tutorial/multtable-good.py)

### Inköpslistan

Skriv ett program som hanterar en inköpslista. Du ska kunna ha flera olika 
inköpslistor (exempelvis en för mat, en för andra saker), men det räcker med 
att experimentera med en.

Det ska gå att lägga till saker, lista dem, bocka av enskilda saker och ta bort 
alla avbockade saker.

Lösningsförslag:

  - [En modul som illustrerar en enkel inköpslista, shopping.py][shopping.py]

[shopping.py]: https://github.com/dbosk/intropy/blob/master/modules/classes/tutorial/shopping.py


## Bankkontot

Vi ska skriva ett enkelt program som hanterar konton åt en bank. Vi behöver en 
sammansatt datatyp (klass) som kan representera ett bankkonto:

  - Det ska lagra ägarens uppgifter. Ägaren är en person. (Hm, kanske vi har en 
    klass lämplig för att spara en persons data? Hint: se folkbokföringen 
    ovan.)
  - Det ska lagra nuvarande saldo.
  - Det ska gå att sätta in pengar.
  - Det ska gå att ta ut pengar, men bara om det finns tillräckligt med pengar 
    på kontot. Inga negativa saldon!

Lösningsförslag:

  - [En modul med klasser för en bank, bank.py][bank.py]
  - [En modul med klasser för en bank (använder arv), bank_arv.py][bank_arv.py]
  - [Ett program med gränssnitt för en bank, banken.py][banken.py]
  - [Ett program med gränssnitt för en bank (arv), banken_arv.py][banken_arv.py]
  - [En modul för inmatning av specifika typer, input_type.py][input_type.py]

[bank.py]: https://github.com/dbosk/intropy/blob/master/modules/classes/tutorial/bank.py
[bank_arv.py]: https://github.com/dbosk/intropy/blob/master/modules/classes/tutorial/bank_arv.py
[banken.py]: https://github.com/dbosk/intropy/blob/master/modules/classes/tutorial/banken.py
[banken_arv.py]: https://github.com/dbosk/intropy/blob/master/modules/classes/tutorial/banken_arv.py
[input_type.py]: https://github.com/dbosk/intropy/blob/master/modules/classes/tutorial/input_type.py
