# Laboration: Listor, for-slingor och uppslagslistor

I denna laboration ska vi utöka programmet vi skrev i föregående laboration.

I vårt förra program lät vi användaren mata in värdena för variablerna $a_1, d, 
g_1, q$ och $n$, därefter beräknade vi den aritmetiska och den geometriska 
summan och, slutligen, skrev vi ut vilken av dem som var störst.


## Uppgift

Som vi nämnt tidigare kan geometriska följder användas för att räkna på räntor. 
Räntor kan variera över tid. Det ska vi ta hänsyn till i denna laboration.

Låt $d$ och $q$ variera över tid. Tidigare hade vi endast ett värde i $d$ och 
$q$ och använde samma värde alla $n$ gånger. Låt $d$ och $q$ innehålla listor 
med $n$ värden istället.

Observera att nu kan vi inte längre använda formlerna, då de förutsätter att 
$d$ och $q$ är konstanta. (Rent terminologiskt betyder detta också att dessa 
inte längre är aritmetiska eller geometriska talföljder, då definitionen av 
dessa förutsätter konstanta $d$ och $q$.) Vi måste då iterera igenom alla 
termer i summan.

**Inlämning**: Låt användaren mata in $n$ först, sedan läser du in $n$ värden 
för $d$ och $q$ från användaren. Slutligen måste du även läsa in $a_1$ och 
$g_1$ för att kunna beräkna talföljderna. Skriv ut talföljderna och deras 
summor.

**Test**: Vi kan testa koden med korta exempel som vi kan beräkna för hand. Vi 
kan även testa koden genom att mata in samma värden för $q$ och $d$, d.v.s. att 
$q_1 = q_2 = \cdots = q_n$ och $d_1 = d_2 = \cdots = d_n$, för då kan vi 
använda formlerna för att beräkna summan.

**Exempeltillämpning**: Säg att vi har ett sparkonto där räntan varierar och vi 
vill uppskatta inkomsten från räntan för ett år framåt. Då låter vi $g_1$ vara 
vårt ursprungliga sparkapital, medan $q_1, \ldots, q_{12}$ är räntan för varje 
månad.  Då ger räntan en avkastning på $g_1\cdot q_1\cdot q_2\cdots q_{12} 
- g_1$.

