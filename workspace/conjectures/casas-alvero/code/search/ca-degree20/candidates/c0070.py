from sympy import symbols, Rational
x = symbols('x')
# general: (x-a)^19 (x-b), r=a <=> a+19b=20. use a=3, b=(20-3)/19=17/19
f = (x-3)**19 * (x - Rational(17,19))
