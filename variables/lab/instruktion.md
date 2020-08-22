# Laboration: Variabler och utskrifter

Vi ska nu börja med att använda datorn som den räknemaskin den är. Vi ska 
arbeta med [aritmetiska][aritmetiska] och [geometriska][geometriska] följder.

[aritmetiska]: https://sv.wikipedia.org/wiki/Aritmetisk_f%C3%B6ljd
[geometriska]: https://sv.wikipedia.org/wiki/Geometrisk_f%C3%B6ljd

Fördelen med att börja med denna typ av följder är att vi enkelt kan beräkna 
dem för hand. Detta betyder att vi enkelt kan kontrollera korrektheten i våra 
program.


## Aritmetiska följder

I en aritmetisk följd är differensen mellan två element konstant. Exempelvis, 
$$
  1, 2, 3, 4, \ldots
$$ är en aritmetisk följd där differensen är ett.

Låt oss säga att det första elementet i följden är $a_1$ och differensen är 
$d$. Då kan vi beräkna $a_n = a_1 + d\cdot (n-1)$.

Vi kan även beräkna summan $S^a_n = a_1 + \cdots + a_n =
n \frac{a_1 + a_n}{2}$.


## Geometriska följder

I en geometrisk följd är det istället kvoten mellan elementen som är konstant. 
Exempelvis, $$
  1, 2, 4, 8, 16, \ldots
$$ är en geometrisk följd där kvoten är två.

Låt oss säga att det första elementet i följden är $g_1$ och kvoten är $q$. 
Då kan vi beräkna $g_n = g_1 q^{n-1}$.

Vi kan även beräkna summan $S^g_n = g_1 + \cdots + g_n =
g_1 \frac{q^n-1}{q-1}$.


## Uppgift

Skriv ett program som använder variabler för $$
  a_1, d, g_1, q, n
$$ och beräknar summorna $S^a_n$ och $S^g_n$.

