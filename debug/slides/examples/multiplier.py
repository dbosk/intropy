""" This program performs multiplication by
repeated addition """

import input_type as it

def multiply(a, b):
    """ Computes a*b by repeated addition """
    result = 0
    for _ in range(b):
        result += b
    return result

def main():
    """ Test program """
    x = it.input_type(int, "x = ")
    y = it.input_type(int, "y = ")
    xy = multiply(x, y)
    print(f"{x} * {y} = {xy}")

if __name__ == "__main__":
    main()
