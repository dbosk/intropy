def integer_division(a, b):
    """Skriver ut info om a heltalsdividerat med b"""
    print(f"{a} = {a // b} * {b} + {a % b}")
    print(f"{a} // {b} == {a // b}")
    print(f"{a} % {b} == {a % b}")

integer_division(10, 4)
print()
integer_division(10, 3)
print()
integer_division(9, 3)
