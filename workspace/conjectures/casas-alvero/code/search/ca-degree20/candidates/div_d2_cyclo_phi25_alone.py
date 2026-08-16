from sympy import symbols, cyclotomic_poly
x = symbols('x')
# CONSTRUCTION div-d2: CYCLOTOMIC-derived. (x-1)^12 * phi_25(x). phi_25 has
# degree 20 -> the whole polynomial is just phi_25 (all simple). Demonstrates
# an all-simple cyclotomic of degree exactly 20.
f = (x - 1)**0 * cyclotomic_poly(25, x)
