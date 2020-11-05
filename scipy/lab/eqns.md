# Laboration: Ekvationslösning

Vi ska nu använda datorn för att lösa ekvationer åt oss.


## Linjära ekvationssystem

Vi har följande ekvationssystem:
$$
\begin{cases}
2x + 1y + 3z = 13 \\
5x + 1z = 8 \\
-x - 1y - 3z = 12
\end{cases}
$$
Skriv ett program som finner $x, y, z$ med hjälp av [gaussisk 
elimination][gauss-elim].

[gauss-elim]: https://en.wikipedia.org/wiki/Gaussian_elimination


## Hitta nollställen

Vi har funktionerna $$
\begin{align}
p(x) &= x^6 - 21 x^5 + 175 x^4 - 735 x^3 + 1624 x^2 - 1764 x + 720 \\
q(x) &= x^6 + 21 x^5 + 175 x^4 + 735 x^3 + 1624 x^2 + 1764 x + 720 \\
s(x) &= x^6 + 3 x^5 - 41 x^4 - 87 x^3 + 400 x^2 + 444 x - 720 \\
t(x) &= x^6 - 3 x^5 - 41 x^4 + 87 x^3 + 400 x^2 - 444 x - 720
\end{align}.
$$

Skriv en funktion som finner nollställen för en given funktion. Använd 
[Newton-Raphsons metod][nr-method]. Använd den för att finna ett nollställe för 
respektive funktion ($p, q, s, t$, en åt gången, inte alla som ett 
ekvationssystem).

[nr-method]: https://en.wikipedia.org/wiki/Newton%27s_method

Newton-Raphsons metod kräver dock en gissning för $x_0$. Skriv en funktion som 
tar $n$ som argument gissar $x_0$ för att få ut $n$ unika nollställen för en 
given funktion. Funktionen ska sedan returnera de $n$ unika nollställena.

