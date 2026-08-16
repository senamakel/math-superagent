from sympy import symbols
x = symbols('x')
# CONSTRUCTION div-d4: PRESCRIBED ROOT MULTISET, even-symmetric.
# f = x^12 (x^2-1)^4 = roots {0 mult 12, 1 mult 4, -1 mult 4}. An even
# polynomial: shares the common root 0 with every ODD derivative too, giving
# cross-sharing beyond the multiplicity (score 15 > the multiplicity-12 start).
f = x**12 * (x - 1)**4 * (x + 1)**4
