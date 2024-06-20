"""Program som skriver ut Fibonacci-serien"""

import snoop

snoop.install(columns="")

def fib(n):
    """Returnerar n:te talet i Fibonacci-serien"""
    if n <= 0:
        return 0
    if n == 1:
        return 1

    return fib(n-1) + fib(n-2)

with snoop(depth=10):
    print(f"fib(3) = {fib(3)}")
