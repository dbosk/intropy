"""Filtering experiments"""

def print_all(lst):
    for i in lst:
        print(i)

def check(lst):
    gt_two = lambda x: x > 2

    if any(map(gt_two, lst)):
        print("There are elements larger than two.")
    if all(map(gt_two, lst)):
        print("All elements are larger than two.")


ns = range(-10, 10)
print_all(ns)
check(ns)

print("-"*10)

ms = list(filter(lambda x: x > 2, ns))
print_all(ms)
check(ms)

