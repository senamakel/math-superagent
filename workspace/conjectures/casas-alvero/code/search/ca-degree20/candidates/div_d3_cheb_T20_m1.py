from sympy import symbols, chebyshevt
x = symbols('x')
# CONSTRUCTION div-d3: CHEBYSHEV-derived. (T_20(x) - 1)/2^19 : monic degree-20.
# Roots are the 20 (double) points where T_20 = 1, i.e. cos(2k*pi/20), k=0..19,
# each to multiplicity 2. Multiplicity-2 roots force the first derivative to
# share them (a start, unlike the all-simple T_20).
f = (chebyshevt(20, x) - 1) / 2**19
