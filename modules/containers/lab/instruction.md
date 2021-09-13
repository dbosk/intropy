# Laboration: Behållare och iterationer

Hittills har vi arbetat med aritmetiska och geometriska talföljder, d.v.s. att 
$d$ och $q$ har varit konstanta. Nu ska vi fokusera på den geometriska 
talföljden och vi ska dessutom låta värdet på $q$ variera över tid. Som vi 
nämnt tidigare kan geometriska talföljder användas för att räkna på räntor. 
Räntor kan dock variera över tid och det är därför vi vill låta $q$ variera. 

När vi arbetar med räntor, då är det dock de olika talen i följden som är 
intressanta, inte summan. Vi påminner oss om definitionen för en geometrisk 
talföljd från tidigare: Låt oss säga att det första elementet i följden är 
$g_1$ (det ursprungliga beloppet) och kvoten är $q$ (räntan som är densamma för 
alla månader). Då kan vi beräkna $g_n = g_1 q^{n-1}$, d.v.s. beloppet $n$ 
månader senare.


## Uppgift

Skriv en funktion som returnerar $g_n$ givet en lista
$$q = (q_1, \ldots, q_{n-1})$$
(d.v.s. $q$ som varierar över tid). Tidigare hade vi endast ett värde i $q$ och 
använde samma värde alla $n$ gånger. Låt $q$ innehålla en lista med $n$ värden 
istället. (Rent terminologiskt betyder detta också att vi inte längre arbetar 
med en geometrisk talföljd, då definitionen förutsätter att $q$ är konstant.) 
Vi måste alltså iterera över listan, då formeln inte längre fungerar.

**Test**: Vi kan testa koden med korta exempel som vi kan beräkna för hand (som 
ovan). Vi kan även testa koden genom att mata in samma värden för $q$, d.v.s. 
att $q_1 = q_2 = \cdots = q_n$, för då kan vi använda formlerna för att beräkna 
det sista talet i följden.

**Exempeltillämpning**: Säg att vi har ett sparkonto där räntan varierar och vi 
vill uppskatta inkomsten från räntan för ett år framåt. Då låter vi $g_1$ vara 
vårt ursprungliga sparkapital, medan $q_1, \ldots, q_{12}$ är räntan för varje 
månad.  Då kommer vi att ha $g_1\cdot q_1\cdot q_2\cdots q_{12}$ kronor på 
sparkontot när alla månader passerat.

**Inlämning**: Låt ditt program fråga användaren efter antalet månader ($n$) 
och det ursprungliga sparkapitalet ($g_1$). Skriv ut sparkapitalets totala 
värde och värdeökning månad för månad. Exempelvis:
```
Hur mycket sparkapital har du (ange i kr)? 1000
Hur många månader avser du spara? 2
Ange ränta för månad 1 (i procent): 2
Ange ränta för månad 2 (i procent): 1

         Total       Ökning
Månad 0: 1000.00 kr   0.00 kr
Månad 1: 1020.00 kr  20.00 kr
Månad 2: 1030.20 kr  30.20 kr
```
Använd din funktion för att beräkna värdena. (Inmatningarna ska givetvis 
repeteras tills att värdena är korrekta, återanvänd funktionerna från 
föregående laboration --- men du får givetvis skriva om dem om det behövs.)
