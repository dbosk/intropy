import sympy

x = sympy.symbols("x")

expr = x**2 - 4
print(f"expr = {expr}")

print(f"factorization: {expr} = {sympy.factor(expr)}")
print(f"solve: {expr} = 0 har rötterna {sympy.solve(expr, x)}")

print()
print(f"({expr})*{x} = {expr*x}")
expr *= x

print(f"factorization: {expr} = {sympy.factor(expr)}")
print(f"solve: {expr} = 0 har rötterna {sympy.solve(expr, x)}")
