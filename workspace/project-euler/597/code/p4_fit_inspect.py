#!/usr/bin/env python3
"""Analyze / factor the p4 cubic rational fit and the p3 quadratic fit,
check their large-L limits, and evaluate the p4 fit at many m values."""
from fractions import Fraction as F
from sympy import symbols, factor, simplify, Rational, limit, oo

m = symbols('m')

# p4 fit:  N/D, N deg3, D deg3
N3 = -Rational(9,2) + Rational(61,9)*m - Rational(119,36)*m**2 + Rational(19,36)*m**3
D3 = -Rational(15,2) + Rational(47,4)*m - 6*m**2 + m**3
print("p4 N:", factor(N3))
print("p4 D:", factor(D3))
print("p4 limit m->inf:", limit(N3/D3, m, oo))

# p3 fit: (7m^2-17m+12)/(18m^2-45m+27)
N2 = 7*m**2 - 17*m + 12
D2 = 18*m**2 - 45*m + 27
print("\np3 N:", factor(N2))
print("p3 D:", factor(D2))
print("p3 limit m->inf:", limit(N2/D2, m, oo))

# p2: L/(2L-40) = m/(2m-1), m=L/40.  factor it in m form.
print("\np2 (m=L/40):", factor(m/(2*m-1)))

# evaluate p4 fit at m = L/40 for several L to give predictions
import json
# known values to spot-check
KNOWN = {
    160:"7/15",240:"187/378",320:"1951/3861",400:"521/1020",480:"3077/5985",
    560:"16033/31050",640:"2839/5481",800:"54559/104895",900:"143561/275520",
    1000:"25382/48645",1100:"2493559/4773600",1200:"68843/131670",
    1300:"474941/907680",1400:"677228/1293435",1500:"2249593/4294080",
    1600:"57511/109725",1800:"166802/317985",2000:"1044769/1990440",
    2500:"3723481/7085760",3000:"2454796/4667985",4000:"990791/1882335",
    5000:"35280338/66990105",
}
# HELD-OUT predictions at L values NOT in the fit data
HOLDOUT_L = [600, 700, 750, 850, 950, 1050, 1150, 1250, 1350, 1450, 1550,
             1650, 1750, 1850, 1950, 2200, 2600, 3200, 3500, 4500, 1800]
for L in HOLDOUT_L:
    mm = F(L, 40)
    pred = (N3/D3).subs(m, mm)
    print(f"L={L:5d} (m={mm})  pred p4 = {pred} = {float(pred):.10f}")
