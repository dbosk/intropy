---
title: Övning om klasser och objekt
authors:
  - Daniel Bosk <dbosk@kth.se>
  - Celina Soori <celinah@kth.se>
  - Mazen Mardini <mazenm@kth.se>
---
# Fördjupande övning: klasser och objekt

Målet med övningen är att du ska få en djupare förståelse för hur du ska

  - använda och konstruera sammansatta datatyper (klasser),
  - tillämpa behållare för att lagra mängder med data,
  - tillämpa olika former av upprepningar för att arbeta med data,
  - dela upp problem i mindre problem,
  - minimera kodupprepning,
  - leta i Pythons dokumentation.


## Önskemål från gruppen

Var det något särskilt från veckans föreläsning och/eller OLI-material som gruppen vill gå in djupare på?

Är det någon som vill visa upp något särskilt från förra veckans laboration som kan ge inspiration till gruppen?

### Finn fem fel


[Gissningsspelet](https://github.com/dbosk/intropy/blob/master/modules/containers/tutorial/guess.py) låter användaren gissa.

Läs igenom koden och få ett hum om vad den är tänkt att göra. Testa att köra koden.

Hitta nu tillsammans minst fem fel/utvecklingsområden i koden (tänk på vad ni lärt er under veckan).

Förbättra nu koden efter det ni hittat. Blev koden mer lättläst, användbar och/eller användarvänlig? Varför?

[Lösningsförslag](https://github.com/dbosk/intropy/blob/master/modules/containers/tutorial/guess-good.py)

### Bankkontot

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
  - [Ett program med gränssnitt för en bank, bank_program.py][bank_program.py]
  - [En modul med en personklass, person.py][bank_program.py]
  - [En modul med en medborgarklass, citizen.py][citizen.py]
  - [En modul med en adressklass, address.py][address.py]
  - [En modul för inmatning av specifika typer, input_type.py][input_type.py]

[bank.py]: https://github.com/dbosk/intropy/blob/master/modules/classes/tutorial-advanced/bank.py
[bank_program.py]: https://github.com/dbosk/intropy/blob/master/modules/classes/tutorial-advanced/bank_program.py
[address.py]: https://github.com/dbosk/intropy/blob/master/modules/classes/tutorial-advanced/address.py
[citizen.py]: https://github.com/dbosk/intropy/blob/master/modules/classes/tutorial-advanced/citizen.py
[person.py]: https://github.com/dbosk/intropy/blob/master/modules/classes/tutorial-advanced/person.py
[input_type.py]: https://github.com/dbosk/intropy/blob/master/modules/classes/tutorial-advanced/input_type.py


### En bråkig klass

Vi vill ha en klass för att räkna med rationella tal, eller bråk. Vi ska kunna:

  - skapa bråk, exempelvis `a = Bråk(1, 3)` och `b = Bråk(2, 6)`;
  - jämföra bråk, exempelvis `a == b` eller `a < b`;
  - skriva ut bråk på läsbar form, exempelvis `print(f"{a} och {b}")` ger 
    utskriften `1/3 och 2/6`.
  - addera, subtrahera, multiplicera och dividera bråk.
  - typkonvertera bråket till ett flyttal (`float`).
  - förkorta bråk, exempelvis så att `b` (som är 2/6) kan förkortas till 1/3.

Detta kräver en del specialmetoder. Se [dokumentationen för Pythons 
specialmetoder för jämförelse][doc-cmp] och [dokumentationen för Pythons 
specialmetoder för att emulera numeriska typer][doc-numtypemethods].

[doc-cmp]: https://docs.python.org/3/reference/datamodel.html#object.__lt__
[doc-numtypemethods]: https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types

Lösningsförslag:

  - [Lösningsförslag: en modul med en klass för bråktal, frac.py][frac.py]

[frac.py]: https://github.com/dbosk/intropy/blob/master/modules/classes/tutorial/frac.py
