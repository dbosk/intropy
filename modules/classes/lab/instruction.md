---
title: Laboration: Klasser och objekt
authors
  - Daniel Bosk <dbosk@kth.se>
---
# Laboration: Klasser och objekt

Hittils har vi använt funktioner för att beräkna $g_n$ på olika sätt (konstant 
$q$ och en lista med $q$-värden). Syftet med klasser (och objekt) är att de 
bättre liknar objekt i verkligheten. Exempelvis är en talföljd väldigt lik en 
lista, det är ju trots allt en (möjligtvis oändlig) lista med tal, men mindre 
lik en funktion för att beräkna talen i följden.

Fördelen med att representera objekt på ett bättre sätt är att det underlättar 
för den som ska programmera. Det kan göra koden mer intuitiv, mer läsbar. Detta 
minskar risken för fel (buggar).


## Uppgift

Nu ska vi skriva klasser som hanterar talföljder. Låt klasserna vara en del av 
din modul för talföljder. De ska hantera den karakteristiska egenskapen för en 
talföljd: det ska gå att få ut det $n$:te elementet (använd 
[`__getitem__`][getitem]).

[getitem]: https://docs.python.org/3/reference/datamodel.html#object.__getitem__

För att förbättra förståelsen efter att ha läst dokumentationen, experimentera 
med följande testkod:
```python
class Test:
  def __getitem__(self, key):
    return key

t = Test()
print(t[0])
```

Om du använder `__getitem__` på korrekt sätt kommer dina klasser att kunna köra 
igenom följande testprogram:
```python
import my_sequence_library as myseq
# Ladda hem modulen input_type från:
# https://github.com/dbosk/intropy/raw/master/modules/classes/lab/input_type.py
import input_type as it

def test_arithmetic_seq():
    """Function testing the arithmetic sequence"""
    a1 = myseq.ArithmeticSequence(1, 1)
    for i in range(20):
        print(f"a1[{i}] = {a1[i]}")
        if a1[i] != i:
            raise Exception(f"a1[{i}] = {a1[i]} != {i}")

    a2 = myseq.ArithmeticSequence(2, 2)
    for i in range(20):
        print(f"a2[{i}] = {a2[i]}")
        if a2[i] != 2*i:
            raise Exception(f"a1[{i}] = {a1[i]} != {2*i}")

    try:
        a2[-1]
    except IndexError as err:
        print(f"Förväntat IndexError fångat: {err}")
    else:
        raise Exception(f"a2[-1] = {a2[-1]}, förväntades IndexError")

def test_geometric_seq():
    """Function testing the arithmetic sequence"""
    g1 = myseq.GeometricSequence(1, 1)
    for i in range(20):
        print(f"g1[{i}] = {g1[i]}")
        if g1[i] != 1:
            raise Exception(f"g1[{i}] = {g1[i]} != 1")

    g2 = myseq.GeometricSequence(2, 2)
    for i in range(10):
        print(f"g2[{i}] = {g2[i]}")
        if g2[i] != 2**(i+1):
            raise Exception(f"g1[{i}] = {g1[i]} != {2**(i+1)}")

    try:
        g2[-1]
    except IndexError as err:
        print(f"Förväntat IndexError fångat: {err}")
    else:
        raise Exception(f"g2[-1] = {g2[-1]}, förväntades IndexError")

def test_file_seq():
    """Function testing the MultiplicativeSequenceFromFile class"""
    # använd sequence.csv som exempelinmatning:
    # https://github.com/dbosk/intropy/raw/master/modules/classes/lab/sequence.csv
    correct_filename = "sequence.csv"
    incorrect_filename = "this_file_does_not_exist.nonexisting_extension"
    # detta ska ge ett exception
    try:
      gf = myseq.MultiplicativeSequenceFromFile(incorrect_filename)
    except FileNotFoundError as err:
      print(f"Super, det verkar fungera: {err}")

    # detta ska funka om filen sequence.csv finns i samma mapp
    gf = myseq.MultiplicativeSequenceFromFile(correct_filename)

    print(f"gf[7] = {gf[7]}")
    if gf[7] != 1.217251414:
        # det här ska inte inträffa med sequence.csv ovan
        raise Exception(f"gf[7] = {gf[7]} != 1.217251414")

    # sequence.csv har färre än 1000 element, så detta ska generera ett
    # IndexError
    try:
        print(f"gf[1000] = {gf[1000]}")
    except IndexError:
        print("Förväntat IndexError fångat.")
    else:
        raise Exception(f"Förväntade ett IndexError: gf[1000] = {gf[1000]}")


def run_tests():
    """Function containing tests for the my_sequence_library module"""
    test_arithmetic_seq()
    test_geometric_seq()
    test_file_seq()

if __name__ == "__main__":
    run_tests()
```
(Du kan antingen klippa-och-klistra ovanstående kod eller ladda hem 
[testprogram.py][testprogram.py] som innehåller den.)

[testprogram.py]: https://github.com/dbosk/intropy/blob/master/modules/classes/lab/testprogram.py

Ovan nämnda egenskap (indexering, `__getitem___`) är sann för alla talföljder, 
vare sig de är aritmetiska, geometriska eller något annat. Då kan vi ha en 
klasser för olika typer av talföljder som beter sig lika. På så vis skulle vi 
kunna byta ut `a = myseq.ArithmeticSequence(a1=1, d=2)` mot `a = 
myseq.MultiplicativeSequenceFromFile("file.txt")` (som läser in en sekvens från 
fil, likt föregående laboration) och resten av koden i exemplet ovan kommer att 
fortsätta att fungera.

**Inlämning**: Lämna in en modul (`my_sequence_library.py`) som fungerar med 
testprogrammet ovan. Den måste då innehålla klasserna `ArithmeticSequence`, 
`GeometricSequence` och `MultiplicativeSequenceFromFile`.

**Krav**: Du ska ha felhantering. Exempelvis hantera att talföljden (från fil) 
inte har tillräckligt många element. Exempelvis om den innehållet data för 12 
månader, då finns inte `a[20]`. Testkoden ovan innehåller try-except-satser som 
fångar de särfall (exceptions) som er kod förväntas att kasta (`raise`).


## Extrauppgift

Hantera [slice-notation][slice-notation], exempelvis:
```
# Skriv ut summan av de första 20 elementen
print(f"sum(a) = {sum(a[:20])}")
```

För raden `sum(a[:20])` krävs att din kod hanterar [sliceobjekt][slice-docs]. 
Följande exempelkod är bra att experimentera med för att komma igång:
```python
class Test:
  def __getitem__(self, key):
    return key

t = Test()
print(t[0])
print(t[:10])
print(t[4:7])
slice_object = t[4:7]
print(slice_object.start)
print(slice_object.stop)
print(slice_object.step)
print(isinstance(t[4:8], slice))
print(isinstance(t[4], slice))
```

[slice-notation]: https://docs.python.org/3/tutorial/introduction.html#strings
[slice-docs]: https://docs.python.org/3/library/functions.html#slice


## Ytterligare extrauppgift

Implementera [`__setitem__`][setitem] för `MultiplicativeSequenceFromFile` för 
att sätta värden. När värdena sätts ska respektive $q$-värde beräknas från 
föregående värde. Lägg till en metod `.save(filename)` som sparar alla 
$q$-värden till en fil som kan läsas in med `MultiplicativeSequenceFromFile` 
nästa körning.

[setitem]: https://docs.python.org/3/reference/datamodel.html#object.__setitem__

