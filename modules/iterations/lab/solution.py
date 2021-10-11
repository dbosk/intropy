"""Program som läser in data för och beräknar en aritmetisk och geometrisk 
summa."""

def aritmetisk(a1, d, n):
    """Returnerar a_1 + ... + a_n, där a_{i+1} = a_i + d"""
    return a1 + d*(n-1)

def geometrisk(g1, q, n):
    """Returnerar g_1 + ... + g_n, där g_{i+1} = g_i g"""
    return g1*(q**n-1)/(q-1)

def är_decimaltal(s):
    """Returnerar True on s är ett decimaltal"""
    try:
        float(s)
        return True
    except ValueError:
        return False

def är_heltal(s):
    """Returnerar True om s är ett heltal"""
    try:
        int(s)
        return True
    except ValueError:
        return False

def läs_decimaltal(prompt, variabelnamn):
    """Returnerar ett decimaltal från användaren, frågar om när användaren 
    matar in fel. Skriver ut prompt först och använder variabelnamn vid 
    inmatning."""
    print(prompt)
    s = input(variabelnamn+": ")
    while not är_decimaltal(s):
        print(variabelnamn, "måste vara ett decimaltal. Prova igen.")
        s = input(variabelnamn+": ")
    return float(s)

def läs_heltal(prompt, variabelnamn):
    """Returnerar ett heltal från användaren, frågar om när användaren matar in 
    fel. Skriver ut prompt först och använder variabelnamn vid inmatning."""
    print(prompt)
    s = input(variabelnamn+": ")
    talet_ok = False
    while not talet_ok:
        if är_heltal(s):
            if int(s)>0:
                return int(s)
        print(variabelnamn, "måste vara ett heltal större än noll. Prova igen.")
        s = input(variabelnamn+": ")

a1 = läs_decimaltal("Data för den aritmetiska summan:", "a1")
d = läs_decimaltal("Data för den aritmetiska summan:", "d")
g1 = läs_decimaltal("Data för den geometriska summan:", "g1")
q = läs_decimaltal("Data för den geometriska summan:", "q")
n = läs_heltal("Antal termer i summorna: ", "n")

aritmetisk_summa = aritmetisk(a1, d, n)
geometrisk_summa = geometrisk(g1, q, n)

if aritmetisk_summa > geometrisk_summa:
    print("Den aritmetiska summan är störst.")
elif aritmetisk_summa < geometrisk_summa:
    print("Den geometriska summan är störst.")
else:
    print("Summorna är lika.")
