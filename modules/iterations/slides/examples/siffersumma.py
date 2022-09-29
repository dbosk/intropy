"""Program som beräknar siffersumman för användarens tal"""

def siffersumma(heltal):
    """Returnerar siffersumman för heltalet heltal (int)"""
    if heltal <= 0:
        return 0

    sista_siffran = heltal % 10

    return sista_siffran + siffersumma(heltal // 10)

def siffersumma_while(heltal):
    """Returnerar siffersumman för heltalet heltal (int)"""
    summan = 0

    while heltal > 0:
        sista_siffran = heltal % 10
        summan += sista_siffran
        heltal = heltal // 10

    return summan

def siffersumma_for(heltal):
    """Returnerar siffersumman för heltal (int)"""
    summan = 0
    siffror = str(heltal)

    for siffra in siffror:
        summan += int(siffra)

    return summan


heltalet = int(input("Postivt heltal: "))
print(f"Siffersumman för {heltalet} är {siffersumma(heltalet)}!")
