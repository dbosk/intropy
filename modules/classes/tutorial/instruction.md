---
title: Övning om klasser och objekt
authors:
  - Daniel Bosk <dbosk@kth.se>
---
# Övning: klasser och objekt

Målet med övningen är att du ska blir bättre på att

  - använda och konstruera sammansatta datatyper (klasser),
  - tillämpa behållare för att lagra mängder med data,
  - tillämpa olika former av upprepningar för att arbeta med data,
  - dela upp problem i mindre problem,
  - minimera kodupprepning,
  - leta i Pythons dokumentation.


## Laborationen

Hur har olika grupper löst samma labb? Oftast väldigt olika. Vi går igenom 
några lösningar. Hur löser man extrauppgiften?


## Inköpslistan

Skriv ett program som hanterar en inköpslista. Du ska kunna ha flera olika 
inköpslistor (exempelvis en för mat, en för andra saker), men det räcker med 
att experimentera med en.

Det ska gå att lägga till saker, lista dem, bocka av enskilda saker och ta bort 
alla avbockade saker.

Lösningsförslag:

  - [En modul som illustrerar en enkel inköpslista, shopping.py][shopping.py]

[shopping.py]: https://github.com/dbosk/intropy/blob/master/modules/classes/tutorial/shopping.py


## Folkbokföringen

Under föreläsningen skrev vi en [modul med en klass för 
personer][person_old.py]. Vi ska nu bygga vidare på den och skriva en enkel 
version av Skatteverkets folkbokföringsdatabas.

[person_old.py]: https://github.com/dbosk/intropy/blob/master/modules/classes/slides/examples/person.py

Folkbokföringen håller koll på följande om varje person:

  - personens identitet (namn, personnummer och de olika delarna av dessa),
  - personens föräldrar och barn,
  - personens bostadsadress (delarna av den adressen) och alla historiska 
    bostadsadresser.

Lösningsförslag:

  - [En modul med en klass för personer, person.py][person.py],
  - [en modul med en klass för adresser, address.py][address.py],
  - [en modul med anpassningar för Skatteverket och testprogram, skatteverket.py][skatteverket.py]

[person.py]: https://github.com/dbosk/intropy/blob/master/modules/classes/tutorial/person.py
[address.py]: https://github.com/dbosk/intropy/blob/master/modules/classes/tutorial/address.py
[skatteverket.py]: https://github.com/dbosk/intropy/blob/master/modules/classes/tutorial/skatteverket.py


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
  - [Ett program med gränssnitt för en bank, banken.py][banken.py]
  - [En modul för inmatning av specifika typer, input_type.py][input_type.py]

[bank.py]: https://github.com/dbosk/intropy/blob/master/modules/classes/tutorial/bank.py
[banken.py]: https://github.com/dbosk/intropy/blob/master/modules/classes/tutorial/banken.py
[input_type.py]: https://github.com/dbosk/intropy/blob/master/modules/classes/tutorial/input_type.py


## En bråkig klass

Vi vill ha en klass för att räkna med rationella tal, eller bråk. Vi ska kunna:

  - skapa bråk, exempelvis `a = Bråk(1, 3)` och `b = Bråk(2, 6)`;
  - jämföra bråka, exempelvis `a == b` eller `a < b`;
  - skriva ut bråk på läsbar form, exempelvis `print(f"{a} och {b}")` ger 
    utskriften `1/3 och 2/6`.
  - förkorta bråk, exempelvis så att `b` (som är 2/6) kan förkortas till 1/3.
  - addera, subtrahera, multiplicera och dividera bråk.
  - typkonvertera bråket till ett flyttal (`float`).

Detta kräver en del specialmetoder. Se [dokumentationen för Pythons 
specialmetoder för jämförelse][doc-cmp] och [dokumentationen för Pythons 
specialmetoder för att emulera numeriska typer][doc-numtypemethods].

[doc-cmp]: https://docs.python.org/3/reference/datamodel.html#object.__lt__
[doc-numtypemethods]: https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types

Lösningsförslag:

  - [Lösningsförslag: en modul med en klass för bråktal, frac.py][frac.py]

[frac.py]: https://github.com/dbosk/intropy/blob/master/modules/classes/tutorial/frac.py


## Önskemål från gruppen

Vad vill gruppen gå igenom igen från veckan som var?
