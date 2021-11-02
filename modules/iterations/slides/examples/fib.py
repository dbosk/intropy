"""Program som skriver ut Fibonacci-serien"""

def fib(n):
    """Returnerar n:te talet i Fibonacci-serien"""
    print(f"fib({n})")

    if n <= 0:
        return 0
    elif n == 1:
        return 1

    return fib(n-1) + fib(n-2)

print(f"fib(5) = {fib(5)}")
