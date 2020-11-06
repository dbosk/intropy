# Laboration med Matlab

Vi ska nu använda datorn för att rita grafer och lösa ekvationer åt oss. Vi 
börjar med att rita grafer då vi kommer att behöva dessa för 
ekvationslösningen.


## Tvådimensionella grafer

Vi har funktionerna

$$p(x) = x^6 - 21 x^5 + 175 x^4 - 735 x^3 + 1624 x^2 - 1764 x + 720$$
$$q(x) = x^6 + 21 x^5 + 175 x^4 + 735 x^3 + 1624 x^2 + 1764 x + 720$$
$$s(x) = x^6 + 3 x^5 - 41 x^4 - 87 x^3 + 400 x^2 + 444 x - 720$$
$$t(x) = x^6 - 3 x^5 - 41 x^4 + 87 x^3 + 400 x^2 - 444 x - 720$$

Rita deras grafer, först var och en för sig och sedan alla i samma graf.


## Tredimensionella grafer (extrauppgift)

Utforska [Matlabs bibliotek][matlab-help] och testa att använda några olika 
funktioner för att skapa några snygga/coola/häftiga/fascinerande 3D-grafer.

[matlab-help]: https://se.mathworks.com/help/


## Linjära ekvationssystem

Vi ska nu börja lösa ekvationer. Matlab är bra på allt som rör matriser, så vi 
ska börja med linjära ekvationssystem.

Vi har följande ekvationssystem:

$$2x + 1y + 3z = 13$$
$$5x + 1z = 8$$
$$-x - 1y - 3z = -12$$

Skriv ett program som finner $x, y, z$. Skriv om ekvationsystemet på matrisform 
($Ax = b$) och beräkna $x = A^{-1} b$.


## Hitta nollställen

Vi har funktionerna

$$p(x) = x^6 - 21 x^5 + 175 x^4 - 735 x^3 + 1624 x^2 - 1764 x + 720$$
$$q(x) = x^6 + 21 x^5 + 175 x^4 + 735 x^3 + 1624 x^2 + 1764 x + 720$$
$$s(x) = x^6 + 3 x^5 - 41 x^4 - 87 x^3 + 400 x^2 + 444 x - 720$$
$$t(x) = x^6 - 3 x^5 - 41 x^4 + 87 x^3 + 400 x^2 - 444 x - 720$$

Skriv en funktion som finner nollställen för en given funktion. Använd 
[Newton-Raphsons metod][nr-method]. Använd den för att finna ett nollställe för 
respektive funktion ($p, q, s, t$, en åt gången, inte alla som ett 
ekvationssystem).

[nr-method]: https://en.wikipedia.org/wiki/Newton%27s_method

**Extrauppgift**: Newton-Raphsons metod kräver dock en gissning för $x_0$. 
Skriv en funktion som tar $n$ som argument och gissar $x_0$ och sedan använder 
funktionen ovan för att få ut ett nollställe, sedan gissar $x_0$ igen o.s.v. 
för att få ut $n$ unika nollställen för en given funktion. Funktionen ska sedan 
returnera de $n$ unika nollställena.

