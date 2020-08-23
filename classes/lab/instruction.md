# Laboration: Klasser och objekt

I förra laborationen lär vi användaren mata in ett filnamn och programmet läste 
därefter $q$-värdena från filen och returnerade summan.

I den här laborationen ska vi förenkla hanteringen av olika geometriska summor.


## Uppgift

Skriv en klass som hanterar en talföljd. Den ska hantera den karakteristiska 
egenskapen för en talföljd: det ska gå att få ut det $n$:te elementet (använd 
[`__getitem__`][getitem]).

[getitem]: https://docs.python.org/3/reference/datamodel.html#object.__getitem__

Med den egenskapen och om du använder `__getitem__` kan vi skriva kod som 
följande:

```python
a = ArithmSeq(a1=1, d=2)

# Skriv ut de första 20 elementen
for i in range(20):
  print("a[{}] = {}".format(i, a[i]))

# Skriv ut summan av de första 20 elementen
print("sum(a) = {}".format(sum(a[:20])))
```

Ovan nämnda egenskap är sann för alla talföljder, vare sig de är aritmetiska, 
geometriska eller något annat. Då kan vi ha en generell klass för talföljder 
och sedan specialiserade klasser för aritmetiska och geometriska talföljder. Så 
vi skulle kunna byta ut `a = ArithmSeq(a1=1, d=2)` mot `a = 
SeqFromFile("file.txt")` och resten av koden i exemplet ovan kommer att 
fortsätta att fungera.

Skriv om programmet från förra laborationen att använda en klass istället för 
att representera talföljden.

