#!/usr/bin/env python3
"""Attack R-weighted-excess-potential.

Claim: there exist summable weights w_i >= 0, w_1 > 0, such that
  P_k = sum_i w_i * max(0, A_k(i) - 2)
is non-increasing under the absolute-difference row operator on EVERY
nonnegative-integer array.

Candidate counterexample (unhalved): A = (1, 0, 8, 0)  ->  A' = (1, 8, 8)
Halved:                    H = (0, 4, 0)            ->  H' = (4, 4)
Defect e = max(0, H-1):    (0, 3, 0)                ->  (3, 3)

Unhalved defect d = max(0, A-2):  (0,0,6,0)         ->  (0,6,6)

P_k = 6*w2 ;  P_{k+1} = 6*w1 + 6*w2.
Monotonicity forces 6*w1 + 6*w2 <= 6*w2, i.e. w1 <= 0,
contradicting w1 > 0 for ANY weight choice.
"""
def diff(row):
    return [abs(row[i]-row[i+1]) for i in range(len(row)-1)]

A = [1,0,8,0]
Ap = diff(A)
d  = [max(0,x-2) for x in A]
dp = [max(0,x-2) for x in Ap]
print("A   =", A)
print("A'  =", Ap)
print("d   =", d)
print("d'  =", dp)
print()
print("P_k   = sum w_i d_i  =", " + ".join(f"{v}*w{i}" for i,v in enumerate(d) if v))
print("P_k+1 = sum w_i d'_i =", " + ".join(f"{v}*w{i}" for i,v in enumerate(dp) if v))
print()
print("Monotonicity P_{k+1} <= P_k requires:")
print("  6*w1 + 6*w2 <= 6*w2  ==>  w1 <= 0.")
print("Claim requires w1 > 0. CONTRADICTION -> every weight sequence fails on this transition.")

# Also confirm the reduced form: any transition where a positive defect lands at
# the first position from a later position with equal total mass is fatal.
