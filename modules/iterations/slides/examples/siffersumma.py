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

def input_int(prompt):
    """Returnerar ett heltal, låter användaren försöka igen tills att det är 
    ett heltal."""
    while True:
        try:
            heltal = int(input(prompt))
            return heltal
        except ValueError:
            print("Det måste vara ett heltal.")


heltalet = input_int("Postivt heltal: ")
print(f"Siffersumman för {heltalet} är {siffersumma(heltalet)}!")
