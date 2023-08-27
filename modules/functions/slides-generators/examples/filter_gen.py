"""Filtering experiments"""

def gt_two(s):
    """Return true if length > 2"""
    return len(s) > 2

def own_filter(f, lst):
    """filter elements of lst based on f"""
    for i in lst:
        if f(i):
            yield i


def main():
    """test module functionality"""
    ns = ["adam", "bertil", "ce", "ded"]
    ms = own_filter(gt_two, ns)

    for i in ms:
        print(i, end=" ")
    print("\n")

if __name__ == "__main__":
    main()
