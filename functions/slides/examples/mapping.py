"""Experimenting with maps"""

def square(x):
    """return x squared"""
    return x**2

def add_one(x):
    """return successor of x"""
    return x+1

def print_all(lst):
    """print all elements in lst"""
    for i in lst:
        print(i)


ns = range(10)
print_all(ns)
print("-"*10)

ms = list(map(square, ns))
print_all(ms)
print("-"*10)

ks = map(add_one, ms)
print_all(ks)
print("-"*10)
