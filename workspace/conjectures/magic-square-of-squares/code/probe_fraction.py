from sage.all import *
from fractions import Fraction
import math

def isqrt(n):
    return math.isqrt(n)

C = 138600
X0q, y0q = 139129, 373 * 23 * 527
print("C:", C, type(C))
print("X0q:", X0q, type(X0q))
num = (X0q * X0q + C * C)**2
den = 4 * y0q * y0q
print("num:", num, type(num))
print("den:", den, type(den))
try:
    xf = Fraction(num, den)
    print("xf:", xf)
except Exception as e:
    print("FAIL:", e)
print("Fraction is", Fraction, getattr(Fraction, "__module__", "?"))
import fractions
print("fractions.Fraction is fractions.Fraction:", Fraction is fractions.Fraction)