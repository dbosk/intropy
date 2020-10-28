"""Find a root of a function"""

import scipy.optimize as opt

def newton_raphson(f, df, x, prec=0.01):
    """Return the root of f"""
    x_prev = x
    x_next = x_prev - f(x_prev)/df(x_prev)

    """Refine until we reach desired error"""
    while abs(x_next - x_prev) > prec:
        x_prev = x_next
        x_next = x_prev - f(x_prev)/df(x_prev)

    return x_next


def main():
    f = lambda x: (x-1)*(x+2) # x**2 + x -2
    df = lambda x: 2*x+1

    print(f"f(x) = x² + x -2 has root {newton_raphson(f, df, 0)}")
    print(f"f(x) = x² + x -2 has root {opt.newton(f, 0)}")


if __name__ == "__main__":
    main()
