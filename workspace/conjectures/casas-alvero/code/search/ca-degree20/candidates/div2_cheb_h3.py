from sympy import symbols, chebyshevt
x = symbols('x')
# CONSTRUCTION div2 (e): CHEBYSHEV-derived, SHIFTED SQUARED. (T_10(x-1))^2/2^18:
# degree-10 Chebyshev shifted +1, squared, scaled monic -> degree 20 with 10
# double roots moved off the symmetric set (cross-sharing test).
f = chebyshevt(10, x - 1)**2 / 2**18
