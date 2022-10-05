Laboration 2 - Vanliga Fel
===========================

Vi har kollat igenom många av era Laboration 2 inlämningar och sett att det finns flera vanliga fel som görs. Nedan finns en lista på sådana fel. Om ni ser att ni har gjort ett eller flera av dessa misstag, se då till att rätta dem innan redovisningen av Laboration 3!

Funktionskommentarer & Docstrings
-----------------------
Varje funktion måste ha en funktionskommentar enligt PEP-8, mer detaljer finns här: [PEP-257](https://peps.python.org/pep-0257/). Från PEP-257: _"The “Specification” text comes mostly verbatim from PEP 8 by Guido van Rossum."_. Det vill säga PEP-8 och PEP-257 är relaterade till varandra. PEP-8 hänvisar också tillbaks till PEP-257.

Kortfattat, skriv funktionskommentarer på följande vis:

```python
def factorial(n):
    """Beräknar fakulteten av n, d.v.s. n!.
    n är ett positivt heltal eller 0.
    """
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1
```

Notera att funktionskommentaren:
- Ska vara under funktionssignaturen `def namn(...):`.
- Ska använda """ """.
- Ska beskriva vad funktionen gör, parametrar, returvärden, möjliga exceptions som kan uppstå och eventuella sidoeffekter.

För mycket global kod
-----------------------
En tumregel är att en moduls innehåll bör vara strukturerad i följande ordning:
1. Eventuell kommentar som beskriver modulen.
2. Imports
3. Globala konstanter
4. Definitioner av funktioner (och klasser om du har det)
5. Global kod

**Mindre bra:**
```python
def f():
    """Beskrivande kommentar"""
    ...

first_value = f()

def g(value):
    """Beskrivande kommentar"""
    ...

second_value = g(first_value)
print(first_value, second_value)
```

**Bättre:**
```python
def f():
    """Beskrivande kommentar"""
    ...

def g(value):
    """Beskrivande kommentar"""
    ...

first_value = f()
second_value = g(first_value)
print(first_value, second_value)
```

Om ni ser att den globala delen av koden har blivit väldigt lång, se då till att dela upp den i flera funktioner. Funktioner har åtminstone två fördelar här: 1. att de namnger och beskriver delar av koden och 2. att de möjliggör återanvändning av kod. 

**Ser vi att mycket kod finns globalt och inte har delats upp i funktioner så kan det leda till ett påpekande.**

Inkonsekvent typografi
--------------------------

Om du väljer att använda snake_case för funktionsnamn, då bör alla funktioner vara skrivna på samma sätt. Samma princip gäller för variabelnamn också.

**Fel:**
```python
def min_första_funktion(ettArgument):
    ...

def minAndraFunktion(ettArgument):
    ...
```

**Rätt:**
```python
def min_första_funktion(ett_argument):
    ...

def min_andra_funktion(ett_argument):
    ...
```
