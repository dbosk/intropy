"""Program som skriver ut Fibonacci-serien"""

def fib(n):
    """Returnerar n:te talet i Fibonacci-serien"""
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    return fib(n-1) + fib(n-2)

print(f"fib(1) = {fib(1)}")
print(f"fib(2) = {fib(2)}")
print(f"fib(3) = {fib(3)}")
print(f"fib(4) = {fib(4)}")
print(f"fib(5) = {fib(5)}")
