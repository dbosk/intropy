"""Ett program som läser in data från användaren och beräknar en aritmetisk och 
en geometrisk summa"""

def aritmetisk(a1, d, n):
    """Returnerar a_1 + ... + a_n, där a_{i+1} = a_i + d"""
    return a1 + d*(n-1)

def geometrisk(g1, q, n):
    """Returnerar g_1 + ... + g_n, där g_{i+1} = g_i g"""
    return g1*(q**n-1)/(q-1)

def läs_data(info, p1, p2):
    """Skriver ut info och läser därefter två flyttal från användaren, 
    namngivna p1 och p2 som prompt"""
    print(info)
    t1 = float(input(str(p1)+": "))
    t2 = float(input(str(p2)+": "))
    return t1, t2


# Huvudprogrammet

a1, d = läs_data("Data för den aritmetiska summan:", "a1", "d")
g1, q = läs_data("Data för den geometriska summan:", "g1", "q")
n = int(input("Antal termer i summorna: "))
aritmetisk_summa = aritmetisk(a1, d, n)
geometrisk_summa = geometrisk(g1, q, n)

if aritmetisk_summa > geometrisk_summa:
    print("Den aritmetiska summan är störst.")
elif aritmetisk_summa < geometrisk_summa:
    print("Den geometriska summan är störst.")
else:
    print("Summorna är lika.")
