from sympy import symbols, chebyshevt
x = symbols('x')
# CONSTRUCTION div2 (e): CHEBYSHEV-derived. (T_10(x))^2 / 2^18 : the degree-10
# Chebyshev polynomial squared, scaled monic -> degree 20. Each of T_10's 10
# (extrema) roots becomes a double root, so derivatives 1..? share them. Even
# polynomial -> shares root 0 with odd derivatives only because T_10 has no
# constant issue; crosses 0.
f = chebyshevt(10, x)**2 / 2**18
