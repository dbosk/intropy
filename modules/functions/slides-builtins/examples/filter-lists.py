"""Filtering experiments"""

def gt_two(s):
    """Return true if length > 2"""
    return len(s) > 2

def own_filter(f, lst):
    result = []
    for i in lst:
        if f(i):
            result.append(i)
    return result

ns = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [0]]
ms = own_filter(gt_two, ns)

for i in ms:
    print(i, end=" ")
print("\n")
