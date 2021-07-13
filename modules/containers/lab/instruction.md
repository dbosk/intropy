# Laboration: Listor, for-slingor och uppslagslistor

Hittills har vi arbetat med aritmetiska och geometriska talföljder, d.v.s. att 
$d$ och $q$ har varit konstanta. Nu ska de variera över tid. Som vi nämnt 
tidigare kan geometriska talföljder användas för att räkna på räntor. Räntor 
kan dock variera över tid. Det ska vi ta hänsyn till i denna laboration.

När vi arbetar med räntor, då är det dock de olika talen i följden som är 
intressant, inte summan. Vi påminner oss om definitionen för en geometrisk 
talföljd från tidigare: Låt oss säga att det första elementet i följden är 
$g_1$ (det ursprungliga beloppet) och kvoten är $q$ (den konstanta räntan per 
månad). Då kan vi beräkna $g_n = g_1 q^{n-1}$, d.v.s. beloppet $n$ månader 
senare.


## Uppgift

Skriv en funktion som returnerar $g_n$ givet en lista
$$q = (q_1, \ldots, q_{n-1})$$
(d.v.s. $q$ som varierar över tid). Tidigare hade vi endast ett värde i $q$ och 
använde samma värde alla $n$ gånger. Låt $q$ innehålla en lista med $n$ värden 
istället. (Rent terminologiskt betyder detta också att vi inte längre arbetar 
med en geometrisk talföljd, då definitionen förutsätter att $q$ är konstant.) 
Vi måste alltså iterera då $q$ inte är konstant, då formeln inte längre 
fungerar.

**Inlämning**: Låt användaren mata in $n$ först, sedan läser du in $n$ värden 
för $q$ från användaren. Slutligen måste du även läsa in $g_1$ för att kunna 
beräkna talföljden. Skriv ut det sista talet i följden.
```
n: 3
q_1: 1.02
q_2: 1.05
q_3: 1.04
g_1: 1000
Summan blir: 1113.84
```

**Test**: Vi kan testa koden med korta exempel som vi kan beräkna för hand (som 
ovan). Vi kan även testa koden genom att mata in samma värden för $q$, d.v.s. 
att $q_1 = q_2 = \cdots = q_n$, för då kan vi använda formlerna för att beräkna 
det sista talet i följden.

**Exempeltillämpning**: Säg att vi har ett sparkonto där räntan varierar och vi 
vill uppskatta inkomsten från räntan för ett år framåt. Då låter vi $g_1$ vara 
vårt ursprungliga sparkapital, medan $q_1, \ldots, q_{12}$ är räntan för varje 
månad.  Då kommer vi att ha $g_1\cdot q_1\cdot q_2\cdots q_{12}$ kronor på 
sparkontot när alla månader passerat.

