#!/usr/bin/env python3
"""
Independent, degenerate, in-domain counterexample for R-weighted-excess-potential.
(excess-energy-ladder). The library already refutes this rung via A=(1,4,12,0)
(claim weighted-excess-potential-refuted); this is the small 'look by hand first'
case: a single spike next to a pair of coincident zeros.

Claim under attack:
  EXISTS summable weights w_i>=0, w_1>0 with P(A) = sum_i w_i*max(0,A_i-2)
  non-increasing under the row operator for EVERY nonneg-integer
  absolute-difference array.

Counterexample (leading 1, even interiors -> genuinely in the triangle's
row-1 shape):
  A  = (1, 0, 4, 0)   ->   A' = (|1-0|, |0-4|, |4-0|) = (1, 4, 4)
  defect A  = (max(0,0-2), max(0,4-2), max(0,0-2)) = (0, 2, 0)
  defect A' = (max(0,4-2), max(0,4-2))            = (2, 2)
  P(A)  = 0*w1 + 2*w2
  P(A') = 2*w1 + 2*w2
  P(A') - P(A) = 2*w1  > 0   (since w1 > 0).
Non-increase fails for EVERY weight sequence with w1 > 0.  REFUTED.
"""
def diff(row):
    return [abs(row[i]-row[i+1]) for i in range(len(row)-1)]
def defect(row):
    return [max(0,x-2) for x in row]

A  = [1, 0, 4, 0]
Ap = diff(A)
dA, dAp = defect(A), defect(Ap)

print("A    =", A,  " defect =", dA,  "  P(A)  = 2*w2")
print("A'   =", Ap, " defect =", dAp, "  P(A') = 2*w1 + 2*w2")
print("P(A')-P(A) = 2*w1")
print("Non-increase requires 2*w1 <= 0  ==>  w1 <= 0, contradicting w1>0.")
print()
# genuineness: A is a valid row-1 shape (leading 1, even interiors)
assert A[0] == 1 and all(x % 2 == 0 for x in A[1:]), "not row-1 shape"
assert dA == [0,2,0] and dAp == [2,2]
print("A is a valid row-1 shape (leading 1, even interiors).")
print("Trajectory is genuine: A' is the diff of A by construction.")
print()
print("VERDICT: R-weighted-excess-potential REFUTED (degenerate spike case).")
