"""Compute family sequences exactly for the feasible srg(v,k,1,2) members
u in {1,3,4,10,31}: k=u^2+u+2, v=1+k^2/2.
Eigenvalue s = negative root of x^2 + (mu-lambda)x + (mu-k) = x^2 + x + (2-k).
Coclique (independence) bound alpha <= v*(-s)/(k-s).
Also re-emit the derived-design sequences and the Reimbayev hexagon bound.
Exact integers only."""
from fractions import Fraction

feas_k = [k for u in (1,3,4,10,31) for k in [u*u+u+2]]
# dedupe keep order
seen=set(); feas_k=[k for k in feas_k if not (k in seen or seen.add(k))]

def f2(n):
    # floor of sqrt? we keep exact. Compute s exactly via discriminant.
    pass

import math
print("k      v        coclique_bound(v*(-s)/(k-s))   alpha_integer_floor")
for k in feas_k:
    v = 1 + k*k//2
    # x^2 + x + (2-k) = 0 ; disc = 1 - 4(2-k) = 4k -7
    disc = 4*k - 7
    s = ( -1 - math.isqrt(disc) ) / 2   # negative root; disc=d^2 perfect? 
    d = math.isqrt(disc)
    assert d*d == disc, (k, disc)
    # s = (-1 - d)/2 (exact integer since d odd, -1-d even? d odd (4k-7 odd), -1-d even yes)
    s_int = (-1 - d)//2
    r_int = (-1 + d)//2
    bound = Fraction(v * (-s_int), k - s_int)
    print(f"{k:>4} {v:>7}   {float(bound):.6f}  = {bound.numerator}/{bound.denominator}   floor {bound.numerator//bound.denominator}   (r,s)=({r_int},{s_int})")

print()
print("coclique bounds as integers (floor or exact?)")
for k in feas_k:
    v = 1 + k*k//2
    d = math.isqrt(4*k-7)
    s_int = (-1 - d)//2
    b = Fraction(v*(-s_int), k-s_int)
    print(k, b, "=", float(b))
