from sympy import symbols, solve, Eq, oo, sqrt

x = symbols("x")
y = symbols("y")

equation = solve(Eq(x + x ** 2 + y + y ** 2 * 69, 666), x)

print(f"{equation=}")

