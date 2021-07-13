# Laboration: Listor, for-slingor och uppslagslistor

I denna laboration ska vi utöka programmet vi skrev i föregående laboration.

I vårt förra program lät vi användaren mata in värdena för variablerna $a_1, d, 
g_1, q$ och $n$, därefter beräknade vi den aritmetiska och den geometriska 
summan och, slutligen, skrev vi ut vilken av dem som var störst.


## Uppgift

Som vi nämnt tidigare kan geometriska följder användas för att räkna på räntor. 
Räntor kan variera över tid. Det ska vi ta hänsyn till i denna laboration.

Vi kan nu lämna den aritmetiska delen (den som använder $d$) och fokusera på 
den geometriska följden, den som använder $q$.

Låt nu $q$ variera över tid. Tidigare hade vi endast ett värde i $q$ och 
använde samma värde alla $n$ gånger. Låt $q$ innehålla en lista med $n$ värden 
istället.

Observera att nu kan vi inte längre använda formeln, då de förutsätter att $q$ 
är konstant. (Rent terminologiskt betyder detta också att talföljden inte 
längre är en geometrisk talföljd, då definitionen förutsätter ett konstant 
$q$.) Vi måste då iterera igenom alla $q$:n.

**Test**: Vi kan testa koden med korta exempel som vi kan beräkna för hand. Vi 
kan även testa koden genom att mata in samma värde för $q$ hela tiden, d.v.s. 
att $q_1 = q_2 = \cdots = q_n$, för då kan vi använda formeln för att beräkna 
summan.

**Exempeltillämpning**: Säg att vi har ett sparkonto där räntan varierar och vi 
vill uppskatta inkomsten från räntan för ett år framåt. Då låter vi $g_1$ vara 
vårt ursprungliga sparkapital, medan $q_1, \ldots, q_{12}$ är räntan för varje 
månad.  Då ger räntan en avkastning på
$g_1\cdot q_1\cdot q_2\cdots q_{12} - g_1$.

**Inlämning**: Låt ditt program fråga användaren efter antalet månader ($n$) 
och det ursprungliga sparkapitalet ($g_1$). Skriv ut sparkapitalets totala 
värde och värdeökning månad för månad. Exempelvis:
```
Hur mycket sparkapital har du (ange i kr)? 1000
Hur många månader avser du spara? 2
Ange ränta för månad 1: 1.02
Ange ränta för månad 2: 1.01

         Total       Ökning
Månad 0: 1000.00 kr   0.00 kr
Månad 1: 1020.00 kr  20.00 kr
Månad 2: 1030.20 kr  30.20 kr
```

