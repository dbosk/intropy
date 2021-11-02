"""Program som visar hur särfall funkar"""

try:
    int("a")
except ValueError as err:
    print(f"We caught this: {err}")

