def aritmetisk_talsumma(a1, d, n):
    return n * (a1 + (a1 + d * (n - 1))) / 2


def geometriska_talsumma(g1, q, n):
    return (g1 * ((q ** n) - 1) / (q - 1))

a1 = 1; d = 2; n = 3

print("Summan av den aritmetiska talföljden är", aritmetisk_talsumma(a1, d, n))

g1 = 2; q = 2; n = 4

print("Summan av den geometriska talföljden är ", geometriska_talsumma(g1, q, n))





















