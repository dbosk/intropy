"""Plot a function graph"""

import math
import matplotlib.pyplot as plt
import numpy

def main():
    f = math.sin

    # using pi/4 gives an unsmooth result,
    # pi/8 or pi/12 yields a smoother curve
    x_vals = numpy.arange(-2*math.pi, 2*math.pi, math.pi / 4)
    y_vals = list(map(f, x_vals))

    plt.plot(x_vals, y_vals)
    plt.grid(True)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("y(x) = sin(x)")
    plt.show()


if __name__ == "__main__":
    main()
