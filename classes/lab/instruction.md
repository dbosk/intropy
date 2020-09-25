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
import input_type as it # from the lectures examples

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

if __name__ == "__main__":
  main()
```

Ovan nämnda egenskap är sann för alla talföljder, vare sig de är aritmetiska, 
geometriska eller något annat. Då kan vi ha en generell klass för talföljder 
och sedan specialiserade klasser för aritmetiska och geometriska talföljder. Så 
vi skulle kunna byta ut `a = myseq.ArithmeticSequence(a1=1, d=2)` mot `a = 
myseq.MultiplicativeSequenceFromFile("file.txt")` (som läser in en sekvens från 
fil, likt föregående laboration) och resten av koden i exemplet ovan kommer att 
fortsätta att fungera.

**Inlämning**: Lämna in en modul (`my_sequence_library.py`) som fungerar med 
testprogrammet ovan. Den måste då innehålla klasserna `ArithmeticSequence`, 
`GeometricSequence` och `MultiplicativeSequenceFromFile`.

**Krav**: Du ska ha felhantering. Exempelvis hantera att filen inte finns, att 
talföljden (från fil) inte har tillräckligt många element. Exempelvis om den 
innehållet data för 12 månader, då finns inte `a[20]`.

