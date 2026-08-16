from sympy import symbols
x = symbols('x')
# CONSTRUCTION div-d3: CHEBYSHEV-DERIVED via the shifted trinomial that mirrors
# the Chebyshev even-power shape at degree 20: x^20 with even powers only,
# giving an even polynomial. A purely-even monic degree-20 rational.
f = x**20 - 5 * x**18 + 10 * x**16 - 10 * x**14 + 5 * x**12 - x**10
