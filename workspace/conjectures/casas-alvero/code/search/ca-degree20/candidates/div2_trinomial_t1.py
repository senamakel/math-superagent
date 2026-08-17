from sympy import symbols
x = symbols('x')
# CONSTRUCTION div2 (a): TRINOMIAL (3-term support, degree 20).
# x^20 - 3x^7 - 2x^3 : exposed monomials at 7 and 3, both OFF zero so roots
# are not all at 0. Truly 3-term, not a binomial in disguise.
f = x**20 - 3*x**7 - 2*x**3
