"""Experiment: advantage of generators"""

def map_nogen(func, lst):
    result = []
    for i in lst:
        print(f"nogen {i} -> {func(i)}")
        result.append(func(i))
    return result

def map_gen(func, lst):
    for i in lst:
        print(f"gen {i} -> {func(i)}")
        yield func(i)

def main():
    l = [1, 2, 3, 4, 5]
    f = lambda x: 2*x
    for i in map_nogen(f, l):
        print(i)
        break
    for i in map_gen(f, l):
        print(i)
        break

if __name__ == "__main__":
    main()
