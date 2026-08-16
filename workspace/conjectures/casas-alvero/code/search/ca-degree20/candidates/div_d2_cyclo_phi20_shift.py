from sympy import symbols, cyclotomic_poly
x = symbols('x')
# CONSTRUCTION div-d2: CYCLOTOMIC-derived. phi_20(x) * (x-1)^12  ==  x^20-1.
# phi_20 has degree 8 (all primitive 20th roots, simple); multiply by (x-1)^12
# to reach degree 20, giving root 1 with multiplicity 12 + 8 simple unity roots.
f = (x - 1)**12 * cyclotomic_poly(20, x)
