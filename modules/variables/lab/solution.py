def aritmetisk(a1, d, n):
    """Returnerar a_1 + ... + a_n, där a_i = a_{i-1} + d"""
    return a1 + d*(n-1)

def geometrisk(g1, q, n):
    """Returnerar g_1 + ... + g_n, där g_n = q g_{n-1}"""
    return g1*(q**n-1)/(q-1)

print(aritmetisk(3, 2, 7))
print(geometrisk(3, 2, 7))
