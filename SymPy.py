from sympy import symbols, solve, Eq, oo, sqrt

x = symbols("x")
y = symbols("y")

equation = solve(Eq(x, sqrt(16 ** 2 / 4 ** 2)))

print(f"{equation=}")

