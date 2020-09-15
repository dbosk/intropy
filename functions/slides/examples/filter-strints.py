"""Filtering experiments"""

def gt_two(x):
    """Return true if length > 2"""
    if type(x) == int:
        return x > 2
    elif type(x) == str:
        return len(x) > 2

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
print("\n")
