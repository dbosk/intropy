""" Experiment file format """

def main_write():
    """ Writes x, f(x) pairs to a file """
    x_list = range(100)
    y_list = apply_f(x_list)
    xy_pairs = zip(x_list, y_list)
    with open("xy.txt", "w") as file:
        for x_val, y_val in xy_pairs:
            file.write(f"{x_val} -> {y_val}\n")

def main_read():
    """ Reads a file of x, f(x) pairs """
    with open("xy.txt", "r") as file:
        lines = file.readlines()

    any_bad = False
    for line in lines:
        x_val, y_val = line.split(" -> ")
        if 2*int(x_val)+3 != int(y_val):
            print(f"{x_val} -/> {y_val}")
            any_bad = True

    if not any_bad:
        print("All values looked good!")

def apply_f(xs):
    """Takes a list of x-values, xs, returns the list 2x+3"""
    ys = []

    for x in xs:
        ys.append(2*x+3)

    return ys

if __name__ == "__main__":
    main_write()
    main_read()
