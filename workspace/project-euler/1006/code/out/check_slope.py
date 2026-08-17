"""Decisive slope check for the mechanical-word modelling of PE1006.

The problem's Fibonacci word S is the characteristic Sturmian word of slope
alpha = (3-sqrt(5))/2 = 1/phi^2 ~ 0.38197 (Perrin-Restivo: s = characteristic
word of slope 2/(3+sqrt5); also Wikipedia: model with slope 1/phi).

Directive 2 says to use "slope a = F(n-1)/F(n)" (-> ~0.618 = density of ZEROS,
i.e. the complement word's ones-slope). This script settles which slope
reproduces the problem's actual factor set under the mechanical-word digit rule
  digit_j(x) = floor(x + (j+1)a) - floor(x + j a)
over the k+1 arc-midpoint intercepts x_m, m = 0..k.

Reference (truth): the problem's infinite word S_oo = 0100101001001...
Built directly by concatenation; its distinct length-k factors are the oracle.
"""
from fractions import Fraction
from math import floor

PHI2INV = (3.0 - 5 ** 0.5) / 2.0   # 1/phi^2

def fib_word(n):
    a, b = '0', '01'
    for _ in range(n):
        a, b = b, b + a
    return b

def oracle_factors(k, length=200):
    w = fib_word(length)
    return {w[i:i + k] for i in range(len(w) - k + 1)}

def mech_factors(k, a):
    """Mechanical-word factor set of slope a (FLOAT version, directive literal)."""
    pts = [(-m * a) % 1.0 for m in range(k + 1)]   # frac(-m*a)
    pts.sort()
    factors = set()
    for idx in range(len(pts)):
        x1, x2 = pts[idx], pts[(idx + 1) % len(pts)]
        # arc from x1 to x2 wrapping; midpoint
        if x2 >= x1:
            xm = (x1 + x2) / 2.0
        else:
            xm = (x1 + x2 + 1.0) / 2.0
            if xm >= 1.0:
                xm -= 1.0
        digs = [floor(xm + (j + 1) * a) - floor(xm + j * a) for j in range(k)]
        factors.add(''.join(str(d) for d in digs))
    return factors

def mech_factors_rat(k, num, den):
    """Rational slope num/den (exact), to avoid float edge cases at boundaries."""
    a = Fraction(num, den)
    pts = sorted([(-m * a) % 1 for m in range(k + 1)])
    factors = set()
    for idx in range(len(pts)):
        x1, x2 = pts[idx], pts[(idx + 1) % len(pts)]
        if x2 >= x1:
            xm = (x1 + x2) / 2
        else:
            xm = (x1 + x2 + 1) / 2 - 1
        digs = [floor(xm + (j + 1) * a) - floor(xm + j * a) for j in range(k)]
        factors.add(''.join(str(d) for d in digs))
    return factors

for k in range(1, 9):
    truth = oracle_factors(k)
    m382 = mech_factors(k, PHI2INV)          # 1/phi^2 float
    m618 = mech_factors(k, 1.0 / ((1 + 5 ** 0.5) / 2))  # 1/phi ~ 0.618 (directive literal)
    # rational approximants: F(n-2)/F(n) ~ 1/phi^2,  F(n-1)/F(n) ~ 1/phi
    f = [1, 1]
    while f[-1] < 100:
        f.append(f[-1] + f[-2])
    for fn in f:
        pass
    # pick F(n) = 89: F(n-2)=34 F(n-1)=55 ; F(n-1)=55
    rat382 = mech_factors_rat(k, f[-3], f[-1])   # F(n-2)/F(n) = 34/89 ~ .382
    rat618 = mech_factors_rat(k, f[-2], f[-1])   # F(n-1)/F(n) = 55/89 ~ .618 (directive)
    print(f"k={k} truth={len(truth)}")
    print(f"   slope 1/phi^2 (~.382) float match={m382==truth}  rational 34/89 match={rat382==truth}")
    print(f"   slope 1/phi  (~.618) float match={m618==truth}  rational 55/89 match={rat618==truth}")
    if k == 3:
        print("   problem's length-3 factors:", sorted(truth))
        print("     slope .382 set:", sorted(m382))
        print("     slope .618 set:", sorted(m618))
