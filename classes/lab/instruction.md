# Laboration: Klasser och objekt

I förra laborationen lär vi användaren mata in ett filnamn och programmet läste 
därefter $q$-värdena från filen och returnerade summan.

I den här laborationen ska vi förenkla hanteringen av olika geometriska summor.


## Uppgift

Skriv en klass som hanterar en talföljd. Låt klassen vara en del av en modul 
för talföljder. Den ska hantera den karakteristiska egenskapen för en talföljd: 
det ska gå att få ut det $n$:te elementet (använd [`__getitem__`][getitem]).

[getitem]: https://docs.python.org/3/reference/datamodel.html#object.__getitem__

Med den egenskapen och om du använder `__getitem__` kan vi skriva kod som 
följande:

```python
import my_sequence_library as myseq
import input_type as it # https://github.com/dbosk/intropy/raw/master/classes/lab/input_type.py

def main():
  a1 = it.input_type(int, "a1 = ")
  d = it.input_type(int, "d = ")

  # Skapa talföljdsobjekt
  a = myseq.ArithmeticSequence(a1, d)

  # Skriv ut de första 20 elementen
  for i in range(20):
    print(f"a[{i}] = {a[i]}")

  # Skriv ut summan av de första 20 elementen
  print(f"sum(a) = {sum(a[:20])}")

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
  main()
```

Ovan nämnda egenskap (indexering, `__getitem___`) är sann för alla talföljder, 
vare sig de är aritmetiska, geometriska eller något annat. Då kan vi ha en 
generell klass för talföljder och sedan specialiserade klasser för aritmetiska 
och geometriska talföljder. Så vi skulle kunna byta ut `a = 
myseq.ArithmeticSequence(a1=1, d=2)` mot `a = 
myseq.MultiplicativeSequenceFromFile("file.txt")` (som läser in en sekvens från 
fil, likt föregående laboration) och resten av koden i exemplet ovan kommer att 
fortsätta att fungera.

För raden `sum(a[:20])` (se [här][slice-notation] för förklaring av notationen) 
krävs att din kod hanterar [sliceobjekt][slice-docs]. Följande exempelkod är 
bra att experimentera med:

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

**Inlämning**: Lämna in en modul (`my_sequence_library.py`) som fungerar med 
testprogrammet ovan. Den måste då innehålla klasserna `ArithmeticSequence`, 
`GeometricSequence` och `MultiplicativeSequenceFromFile`.

**Krav**: Du ska ha felhantering. Exempelvis hantera att filen inte finns, att 
talföljden (från fil) inte har tillräckligt många element. Exempelvis om den 
innehållet data för 12 månader, då finns inte `a[20]`.

