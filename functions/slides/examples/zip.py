"""Enumerate objects"""

l = ["a", "b", "c"]
L = ["A", "B", "C"]

for v, g in zip(L, l):
    print(f"{v}: {g}")

