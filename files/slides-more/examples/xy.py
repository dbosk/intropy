""" Read x, f(x) pairs from a CSV file """

import csv

def write_data(filename, pairs):
    """ Writes x, f(x) pairs to a file """
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        for pair in pairs:
            if len(pair) != 2:
                raise ValueError("must be pair: {pair}")
            writer.writerow(pair)

def write_linear_sample_file():
    """ Generates xy_pairs for f(x) = 2x+3 """
    x_list = range(100)
    y_list = map(lambda x: 2*x+3, x_list)
    write_data("xy-linear.csv", zip(x_list, y_list))

def xy_pairs(x_vals, func):
    """ Takes x-values and returns (x, y)-pairs """
    return zip(x_vals, map(func, x_vals))

def write_quadratic_sample_file():
    """ Generates xy_pairs for f(x) = x**2 """
    write_data("xy-quadratic.csv",
               xy_pairs(range(-10, 10), lambda x: x**2))


def read_data(filename):
    """ Reads a file of x, f(x) pairs """
    with open(filename, "r", newline="") as file:
        reader = csv.reader(file)
        for x_val, y_val in reader:
            yield (x_val, y_val)


def main():
    """ Tests module functionality """
    write_linear_sample_file()
    for pair in read_data("xy-linear.csv"):
        print(pair)

if __name__ == "__main__":
    main()
