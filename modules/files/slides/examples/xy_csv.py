""" Experiment file format """

import csv

def main_write():
    """ Writes x, f(x) pairs to a file """
    x_list = range(100)
    y_list = map(f, x_list)
    xy_pairs = zip(x_list, y_list)
    with open("xy.csv", "w") as file:
        writer = csv.writer(file)
        for x_val, y_val in xy_pairs:
            writer.writerow([x_val, y_val])

def main_read():
    """ Reads a file of x, f(x) pairs """
    with open("xy.csv", "r") as file:
        reader = csv.reader(file)
        any_bad = False
        for x_val, y_val in reader:
            if f(int(x_val)) != int(y_val):
                print(f"{x_val} -/> {y_val}")
                any_bad = True

    if not any_bad:
        print("All values looked good!")

def f(x):
    return 2 * x + 3

if __name__ == "__main__":
    main_write()
    main_read()
