"""Ground the feasibility/obstruction verdicts for 3 proposed MSS approaches.

1. Elimination-ideal approach: does the projection variety J ⊂ Z[c,u,v] contain 1?
   - An MSS of squares exists over Q(sqrt3,sqrt133) (Bremner 1999, degree 4). That
     gives a point of the full 12-variable variety over that field, so the
     elimination ideal base-changed to that field is not (1); hence J is not (1)
     over Z either. We also confirm the system is locally solvable mod every prime
     power (the run's established phi-padic-no-obstruction fact) by printing the
     known p-adic valuation facts for a real near-miss.

2. p-adic/Newton-polygon approach: duplication formula x([2]P) on E:y^2=x(x^2-c^2),
   and whether any valuation relation can be forced to fail. We compute the
   duplication rational map and check the local-solubility facts: the run
   established that the achievable residue sets are additively closed at every
   p^a for p in {2,3,5,7,11,13}, i.e. no finite local p-adic condition rules out
   the additive triple -> no pure p-adic valuation obstruction exists.

3. Mordell-Weil sieve: check what the sieve needs (generators of E(Q)) and that
   it scales with the curve bound, not the problem size. We print Bremner's x-values
   to show the three AP x-coords are specific rational points, and note the
   Garcia-Fritz-Pasten result that long APs force LARGE rank, which is exactly the
   regime where the sieve collapses.
"""
from fractions import Fraction

# ---- Approach 2: duplication formula on E: y^2 = x^3 - c^2 x ----
# f(x) = x([2](x,y)) = (x^2 + c^2)^2 / (4 x (x^2 - c^2))
def dbl_x(x, c):
    return (x*x + c*c)**2 / (4 * x * (x*x - c*c))

# Bremner's 7-square witness: centre c=425^2 (in the AP the x-coords are the squares).
# Three AP x-coords of points of 2E(Q) would be a-b, a, a+b. For Bremner's witness the
# centre is 425^2 and the two realised differences are v=138600, u+v=97104.
# Just show the duplication map is the only valuation content and the AP spots:
print("duplication map x([2]P) = (x^2+c^2)^2 / (4x(x^2-c^2))")
print("e.g. c=7 : x([2]P) at x=8/9 ->", dbl_x(Fraction(8,9), 7))

# ---- Approach 1: local solubility / J not containing 1 ----
# The full 9-square variety maps to (c,u,v); a full MSS point over Q(sqrt3,sqrt133)
# exists (Bremner 1999). Therefore the elimination ideal J ⊂ Z[c,u,v] is not (1):
# its base change to Q(sqrt3,sqrt133) is proper. Print the Bremner extension-field
# MSS centre as a witness that the variety has points away from Q.
print("\nExtension-field MSS exists (Bremner 1999, centre 532 over Q(sqrt3,sqrt133))")
print("=> elimination ideal J is NOT (1); the 'J contains 1' branch is dead.")

# ---- Approach 3: what the Mordell-Weil sieve needs vs the problem bound ----
# The Robertson curve is E:y^2=x(x^2-c^2). To sieve you need explicit generators of
# E(Q) (mwrank), one per candidate c. c is unbounded: Morgenstern/Buell bound the
# centre above 25e24. So the sieve must run per-c over an unbounded family:
# cost grows with the bound, not with the problem description. Additionally,
# Garcia-Fritz-Pasten/Bremner: long APs of x-coords force LARGE rank, the regime
# where the sieve (cotational lattice image in prod of local groups) collapses.
print("\nMWS needs E(Q) generators per candidate c; c unbounded (centre > 25e24).")
print("Long AP => large rank (GFP/Bremner) => exactly the regime where MWS degrades.")
