"""Filtering experiments"""

def gt_two(x):
    """Return true if x > 2"""
    return x > 2

def own_filter(f, lst):
    result = []
    for i in lst:
        if f(i):
            result.append(i)
    return result

ns = ["adam", "bertil", "ce"]
ms = own_filter(gt_two, ns)

for i in ms:
    print(i, end=" ")
print()

ks = filter(gt_two, ns)

for i in ks:
    print(i, end=" ")
print()
