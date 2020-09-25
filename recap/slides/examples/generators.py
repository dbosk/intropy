"""Experiment: advantage of generators"""

def map_nogen(func, lst):
    """ Computes map function without generator """
    result = []
    for i in lst:
        print(f"nogen {i} -> {func(i)}")
        result.append(func(i))
    return result

def map_gen(func, lst):
    """ Computes map function as generator """
    for i in lst:
        print(f"gen {i} -> {func(i)}")
        yield func(i)

def main():
    """ Experiment to test the difference between nogen and gen """
    lst = [1, 2, 3, 4, 5]
    func = lambda x: 2*x
    for item in map_nogen(func, lst):
        print(item)
    for item in map_gen(func, lst):
        print(item)

if __name__ == "__main__":
    main()
