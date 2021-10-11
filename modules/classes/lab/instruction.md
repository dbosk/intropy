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

Med den egenskapen och om du använder `__getitem__` kan vi skriva kod som 
följande:

```python
import my_sequence_library as myseq
# Ladda hem modulen input_type från:
# https://github.com/dbosk/intropy/raw/master/modules/classes/lab/input_type.py
import input_type as it

def run_tests():
  """Function containing tests for the my_sequence_library module"""
  a1 = it.input_type(int, "a1 = ")
  d = it.input_type(int, "d = ")

  # Skapa talföljdsobjekt
  a = myseq.ArithmeticSequence(a1, d)

  # Skriv ut de första 20 elementen
  for i in range(20):
    print(f"a[{i}] = {a[i]}")

  g1 = it.input_type(float, "g1 = ")
  q = it.input_type(float, "q = ")
  g = myseq.GeometricSequence(g1, q)
  print(f"g[12] = {g[12]}")
  
  try:
    print(f"g[-1] = {g[-1]}")
  except IndexError:
    print("Finns inget sista tal i en oändlig talföljd")

  filename = it.input_type(str, "filename = ")
  gf = myseq.MultiplicativeSequenceFromFile(filename)
  print(f"gf[12] = {gf[12]}")

  try:
    print(f"gf[1000] = {gf[1000]}")
  except IndexError:
    print("På tok för stort index.")

if __name__ == "__main__":
  run_tests()
```

Ovan nämnda egenskap (indexering, `__getitem___`) är sann för alla talföljder, 
vare sig de är aritmetiska, geometriska eller något annat. Då kan vi ha en 
generell klass för talföljder och sedan specialiserade klasser för aritmetiska 
och geometriska talföljder. Så vi skulle kunna byta ut `a = 
myseq.ArithmeticSequence(a1=1, d=2)` mot `a = 
myseq.MultiplicativeSequenceFromFile("file.txt")` (som läser in en sekvens från 
fil, likt föregående laboration) och resten av koden i exemplet ovan kommer att 
fortsätta att fungera.

**Inlämning**: Lämna in en modul (`my_sequence_library.py`) som fungerar med 
testprogrammet ovan. Den måste då innehålla klasserna `ArithmeticSequence`, 
`GeometricSequence` och `MultiplicativeSequenceFromFile`.

**Krav**: Du ska ha felhantering. Exempelvis hantera att talföljden (från fil) 
inte har tillräckligt många element. Exempelvis om den innehållet data för 12 
månader, då finns inte `a[20]`.


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

