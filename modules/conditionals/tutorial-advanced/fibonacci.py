from functools import lru_cache

# Det Fibonacci number som ska skrivas ut
FIBONACCI_NUMMER = 500


@lru_cache
def fibonacci(n: int) -> int:
    """Beräkna det n:te Fibonacci numret. Krav: n >= 0."""
    if n < 2:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)


if __name__ == "__main__":
    print(f"fibonacci({FIBONACCI_NUMMER}) = {fibonacci(FIBONACCI_NUMMER)}")
