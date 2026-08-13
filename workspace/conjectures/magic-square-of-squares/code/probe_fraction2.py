from sage.all import *
# mimic prepared constants
X0q = _sage_const_139129
y0q = _sage_const_373  * _sage_const_23  * _sage_const_527
C = 138600
from fractions import Fraction
print("X0q:", type(X0q), X0q)
print("C:", type(C), C)
num = (X0q * X0q + C * C)**_sage_const_2
den = _sage_const_4  * y0q * y0q
print("num:", type(num), num)
print("den:", type(den), den)
try:
    xf = Fraction(num, den)
    print("xf:", xf)
except Exception as e:
    print("FAIL:", type(e).__name__, e)
# try int() coercion path
try:
    xf2 = Fraction(int(num), int(den))
    print("xf2:", xf2)
except Exception as e:
    print("FAIL2:", type(e).__name__, e)