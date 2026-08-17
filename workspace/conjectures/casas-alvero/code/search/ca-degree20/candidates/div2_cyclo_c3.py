from sympy import symbols, cyclotomic_poly
x = symbols('x')
# CONSTRUCTION div2 (d): CYCLOTOMIC-derived, SHIFTED. phi_20(x-1)*(x-1)^12:
# degree 8 (primitive 20th roots) + degree 12 from the (x-1)^12 factor; root 1
# has multiplicity 1+12 = 13 in the shifted variable. Same total as x^20-1 but
# roots shifted by +1 so the support does not collapse.
f = (x - 1)**12 * cyclotomic_poly(20, x - 1)
