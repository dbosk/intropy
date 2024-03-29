---
title: Övning om klasser och behållare
authors:
  - Daniel Bosk <dbosk@kth.se>
  - Celina Soori <celinah@kth.se>
---
# Övning: Fler behållare och mer klasser

Målet med övningen är att du ska bli bättre på att

  - tillämpa olika behållare för att lagra mängder med data,
  - se textsträngar som en lista med bokstäver,
  - tillämpa olika former av upprepningar för att arbeta med behållarna,
  - skapa enkla klasser för att skapa nya datatyper,
  - dela upp problem i mindre problem,
  - minimera kodupprepning,
  - konstruera interaktiva program,
  - leta i Pythons dokumentation.

## Genomgång av veckans svårigheter

Vi går igenom det vi upptäckt i OLI är extra svårt den här veckan.

Zoomlänk: 

## Önskemål från gruppen

Var det något särskilt från veckans föreläsning och/eller OLI-material som gruppen vill gå igenom igen?

Gick förra veckans laboration bra? Finns det något ni skulle vilja gå igenom från laborationen?

## Övningsuppgifter

### Finn fem fel

[Gissningsspelet](https://github.com/dbosk/intropy/blob/master/modules/containers/tutorial/guess.py) låter användaren gissa.

Läs igenom koden och få ett hum om vad den är tänkt att göra. Testa att köra koden.

Hitta nu tillsammans minst fem fel/utvecklingsområden i koden (tänk på vad ni lärt er under veckan).

Förbättra nu koden efter det ni hittat. Blev koden mer lättläst, användbar och/eller användarvänlig? Varför?

[Lösningsförslag](https://github.com/dbosk/intropy/blob/master/modules/containers/tutorial/guess-good.py)

### Avgöra om en e-postadress är giltig

Skriv ett program som läser in en e-postadress från användaren och avgör om det är en giltig adress.

Fundera på:
- Vad avgör om en e-postadress är giltig
- Vad är gemensamt med alla e-postadresser? Hur kan vi använda det för att skapa ett flexibelt program?

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
    
Testa att lagra objekten i en lista och i en uppslagslista. Vad fungerar bäst i det här fallet?

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
