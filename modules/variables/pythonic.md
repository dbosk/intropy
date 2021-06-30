I de flesta fall kommer andra att behöva läsa och modifiera din kod. Då 
underlättar det att följa en gemensam programmeringsstil. Pythonprogrammerare 
följer generellt en standard som kallas för [PEP-8][pep8]. PEP är en 
förkortning för Python Enhancement Proposal. Lyckligtvis behöver vi inte läsa 
hela PEP-8, för det finns verktyg som kan hjälpa oss att detektera när vi 
avviker i stil.

[pep8]: https://www.python.org/dev/peps/pep-0008/

Programmet `pylint` läser igenom ett pythonprogram och talar om var källkoden 
avviker från god pythonprogrammeringssed (PEP-8). Vi kan köra `pylint` i 
terminalen. Om vi har sparat ett program i filen `test.py`, då kan vi köra 
`pylint test.py`.
