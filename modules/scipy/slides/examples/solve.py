"""Solve systems of linear equations"""

import numpy as np
import scipy.linalg as linalg

def print_eqns(A, b):
    """print a matrix as a system of equations"""
    for eqn, coeffs in enumerate(A):
        for index, coeff in enumerate(coeffs):
            if index < len(coeffs)-1:
                print(f"{coeff:2.2f}x_{index} +", end=" ")
            else:
                print(f"{coeff:2.2f}x_{index} = {b[eqn]:2.2f}")

def main():
    A = np.array([[1, 2], [3, 4]])
    b = np.array([1, 2])
    print_eqns(A, b)
    print()

    sols = linalg.solve(A, b)
    print_eqns(np.identity(len(A)), sols)

if __name__ == "__main__":
    main()
