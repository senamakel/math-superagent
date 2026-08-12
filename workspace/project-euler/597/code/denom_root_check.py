#!/usr/bin/env python3
"""Test the denominator-root conjecture against ALL exact p(4,L) data points.
Conjecture: for p(n,L)=N(m)/D(m), m=L/40 reduced, D (as a polynomial in m,
before reduction with N) has simple roots at m = (n-1)/2, n/2, ..., (2n-3)/2.
For n=4: roots at m=3/2, 2, 5/2 i.e. D = c*(2m-3)(m-2)(2m-5);
the reduced p4 formula is (19m^3-119m^2+244m-162)/(9(m-2)(2m-5)(2m-3)).
Check every exact p(4,L) matches the formula (already done in verify_p4_cubic)
and additionally that the required half-integer roots appear (i.e. the
denominator's vanishing there is NOT cancelled by numerator zero / a removable
singularity that would make p finite at those m)."""
from fractions import Fraction as F

def p4(m):
    m = F(m)
    num = 19*m**3 - 119*m**2 + 244*m - 162
    den = 9*(m-2)*(2*m-5)*(2*m-3)
    return num/den

# The half-integer roots claimed for n=4: m = 3/2, 2, 5/2 (k=3,4,5)
roots = [F(3,2), F(2), F(5,2)]
print("n=4 denominator roots (conjecture): m =", [str(r) for r in roots])
print("p4 numerator at each root (should be NONZERO for a true pole; if zero it's removable):")
num = lambda m: 19*m**3 - 119*m**2 + 244*m - 162
for r in roots:
    nv = num(r)
    # den factor that vanishes
    zero_factor = (r-F(2))*(2*r-F(5))*(2*r-F(3))
    print(f"  m={str(r):>6}: num={nv}  (num nonzero -> genuine pole / |p|->inf)")

# p(n,inf) leading numerator sequence: 1/2, 7/18, 19/36 -> numerators 1,7,19
# denominators of the limits: 2,18,36 -> factor: 2, 2*9, 2*18...
print("\nn=2,3,4 large-L limits (exact): 1/2, 7/18, 19/36")
print("numerator sequence: 1, 7, 19  -- differences 6, 12 (level2 = 6 constant)")
print("denominator sequence: 2, 18, 36 -- differences 16, 18; +2 = 9, consistent with 1/2 C(n,2)+...")
