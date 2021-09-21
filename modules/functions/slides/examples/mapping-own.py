"""
Experimenting with maps
This is also a comment
"""
# comment
# comment

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

def own_map(f, lst):
    result = []
    for i in lst:
        result.append(f(i))
    return result


ns = range(10)
print_all(ns)
print("-"*10)

ms = own_map(square, ns)
print_all(ms)
print("-"*10)

ks = own_map(add_one, ms)
print_all(ks)
print("-"*10)
