def beräkna_aritmetisk(a1, d, n):
    return n * (a1 + (a1 + d * (n - 1))) / 2


def beräkna_geometrisk(g1, q, n):
    return (g1 * ((q ** n) - 1) / (q - 1))

a1 = 1; d = 2; n = 3

print("Summan av den aritmetiska talföljden är", beräkna_aritmetisk(a1, d, n))

g1 = 2; q = 2; n = 4

print("Summan av den geometriska talföljden är ",beräkna_geometrisk(g1, q, n))
