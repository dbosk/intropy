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


heltal = int(input("Postivt heltal: "))
print(f"Siffersumman för {heltal} är {siffersumma_while(heltal)}!")
