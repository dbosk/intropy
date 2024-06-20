"""Our own sum function."""

def summera(lst):
    """Sum numbers in lst"""
    result = 0

    for i in lst:
        result += i

    return result


ns = [1, 2, 3, 4, 5]
print(f"{summera(ns)}")
