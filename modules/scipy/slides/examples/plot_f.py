"""Plot a function graph"""

import matplotlib.pyplot as plt

def main():
    f = lambda x: (x-1)*(x+2)

    x_vals = range(-10, 10)
    y_vals = list(map(f, x_vals))

    plt.plot(x_vals, y_vals)
    plt.grid(True)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("y(x) = (x-1)(y+2)")
    plt.show()


if __name__ == "__main__":
    main()
