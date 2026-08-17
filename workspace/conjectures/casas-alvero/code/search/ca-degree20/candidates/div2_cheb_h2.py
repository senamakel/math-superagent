from sympy import symbols, chebyshevt
x = symbols('x')
# CONSTRUCTION div2 (e): CHEBYSHEV-derived, SHIFTED. T_20(x-1)/2^19 : monic
# degree-20 Chebyshev shifted by +1 (roots moved off their symmetric set).
# All 20 roots simple -> generically low sharing; tests the shift effect.
f = chebyshevt(20, x - 1) / 2**19
