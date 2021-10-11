"""Räknar på sparkapital och ränteutveckling åt användaren"""

import lastal as lt

sparkapital = lt.läs_decimaltal(
        "Hur mycket sparkapital har du (ange i kr)?",
        "Sparkapital")
antal_månader = lt.läs_heltal(
        "Hur många månader avser du spara?",
        "Antal månder")

# Läs in räntan för varje månad
räntor = []
for månad in range(antal_månader):
    räntor.append(lt.läs_decimaltal(
        f"Ange ränta för månad {månad+1} (i procent):",
        "Räntan"))

# Skriv ut resultatet
print("             Total     Ökning")
ökning = 0
for månad in range(antal_månader):
    print(f"Månad {månad:2d}: {sparkapital:8.2f} kr {ökning:6.2f} kr")
    ökning = sparkapital * räntor[månad] / 100
    sparkapital += ökning

# Vi behöver skriva ut ytterligare denna för att få med sista månaden
print(f"Månad {månad+1:2d}: {sparkapital:8.2f} kr {ökning:6.2f} kr")
