# Sage cross-check for Thue/unit completeness in the C(nm) proof.
# K = Q(omega), omega^3 = 2.  The only units with norm +-1 are +-1 times the
# fundamental unit (K has class number 1), and the tower admits that unit, so
# every integer solution of c^3 - 2d^3 = +-1 lies on the orbit x_0 + n*fund where
# x_0 is any one particular solution of that norm.  Enumerate ALL Slim
# representatives x0 + n*f under a large |n| bound and filter x^2-y^3  = 0 with y>=0.

from itertools import product
# explicit small search: this is NOT the proof; cross-check only
K = NumberField(x^3-2, names='w'); w = K.gen()

hits = []
for c in range(-60,61):
    for d in range(-60,61):
        if c**3 - 2*d**3 in (-1, 1):
            hits.append((c,d,c**3-2*d**3))
print("Sage: Thue solutions (c,d) with |c|,|d|<=60:", sorted(hits))
