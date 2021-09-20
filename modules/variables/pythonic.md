I de flesta fall kommer andra att behöva läsa och modifiera vår kod, det är 
alltså inte bara i undervisningssammanhang som det händer. Då underlättar det 
att följa en gemensam programmeringsstil. Pythonprogrammerare följer en 
standard som kallas för [PEP-8][pep8]. PEP är en förkortning för Python 
Enhancement Proposal och är en serie med standardiseringsdokument. Lyckligtvis 
behöver vi inte lära oss hela PEP-8 utantill på en gång, för det finns verktyg 
som kan hjälpa oss att detektera när vi avviker i stil.

[pep8]: https://www.python.org/dev/peps/pep-0008/

Programmet `pylint` läser igenom ett pythonprogram och talar om var källkoden 
avviker från god pythonprogrammeringssed (PEP-8). Vi kan köra `pylint` i 
terminalen. Men vi måste först installera det. Det gör vi genom att köra 
`python -m pip install pylint` i terminalen. Vad är då terminalen?

Terminalen tillhandahåller ett kommandoradsgränssnitt. Där kan man skriva in 
kommandon som operativsystemet (Windows, MacOS eller GNU/Linux) sedan utför. 
Hur kan vi komma åt en terminal på olika system?

  - På Windows kan vi söka efter ett program som heter PowerShell (alternativt 
    Kommandotolken på äldre versioner). Se +@fig:windows.
  - På MacOS kan vi söka efter Terminalen. Se [dokumentationen][macos-doc], 
    fönstret ser ut som i Ubuntu (+@fig:ubuntu).
  - På GNU/Linux (exempelvis Ubuntu) söker vi också efter Terminalen. Se 
    +@fig:ubuntu.

[Kommandotolken och PowerShell för Windows.][wincmd]{#fig:windows}

[wincmd]: https://www.howtogeek.com/wp-content/uploads/2017/08/pcp_top.png?width=1198&trim=1,1&bg-color=000&pad=1,1

[macos-doc]: https://support.apple.com/en-gb/guide/terminal/apd5265185d-f365-44cb-8b09-71a064a42125/mac

[Terminalen på Ubuntu][ubuntu]{#fig:ubuntu}

[ubuntu]: https://www.howtogeek.com/wp-content/uploads/2013/03/linux-terminal-on-ubuntu.png?width=1198&trim=1,1&bg-color=000&pad=1,1

(Notera: du vill använda Python 3, på vissa system kan `python` köra Python 2 
istället och då måste du använda dig av `python3` istället för `python` 
överallt. Se även [denna][pip-windows] om du kör Windows.)

[pip-windows]: https://stackoverflow.com/a/29817514/1305099

Om vi har sparat ett program i filen `test.py`, då kan vi köra `pylint 
test.py`. Om `test.py` har följande innehåll:
```python
x = 5
y = 2
print(f"{x} + {y} = {x+y}")
```

Då ger `pylint test.py` följande:
```
************* Module test1
test1.py:1:0: C0114: Missing module docstring (missing-module-docstring)
test1.py:1:0: C0103: Constant name "x" doesn't conform to UPPER_CASE naming style (invalid-name)
test1.py:2:0: C0103: Constant name "y" doesn't conform to UPPER_CASE naming style (invalid-name)

------------------------------------------------------------------
Your code has been rated at 0.00/10 (previous run: 0.00/10, +0.00)
```

Men om vi ändrar koden i `test.py` till
```python
"""A short example program with variables"""

X = 5
Y = 2
print(f"{X} + {Y} = {X+Y}")
```
så får vi istället
```
--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
```
Det första problemet är att god programmeringsstil i Python (PEP-8) säger att 
vi ska lägga till beskrivande kommentarer till programfiler och funktioner, och 
de hade vi inte gjort i den första versionen (men är översta raden i den 
andra). Det andra problemet är att `x` och `y` inte används som variabler, de 
ändras inte i programmet, utan ses då som konstanter. Konstanter ska enligt 
PEP-8 skrivas med versaler.

Fördelen med `pylint` är att den även upptäcker vanliga misstag som orsakar 
svårfunna problem, som när programmeraren har blandat mellanslag och tabbar 
(som ser ut som likadana mellanrum för det mänskliga ögat, men som faktiskt är 
olika).
