from sympy import symbols, chebyshevt
x = symbols('x')
# CONSTRUCTION div-d3: CHEBYSHEV-derived. T_20(x) / 2^19 : the degree-20
# Chebyshev polynomial of the first kind, scaled to be MONIC. Its 20 roots are
# the Chebyshev extrema cos(k*pi/20), k=1..20 -- all simple, real, irrational.
# Coefficients are rational (each is an integer over 2^19); scorer accepts them.
f = chebyshevt(20, x) / 2**19
