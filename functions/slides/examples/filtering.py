"""Filtering experiments"""

def gt_two(x):
    """Return true if x > 2"""
    return x > 2


ns = range(-10, 10)
ms = filter(gt_two, ns)

for i in ms:
    print(i, end=" ")
print()
