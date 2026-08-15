#!/usr/bin/env python3
"""Small brute-force oracle: for a GIVEN weight sequence w, is P non-increasing
across all rows up to a bound? Used to cross-check the LP result and to
verify the hand counterexample.

Checks the specific fatal transition from the hand probe:
   A = (1, 0, c)  ->  A' = (1, c),  d = (0,0,c-2) -> d' = (0, c-2)
   P' - P = (c-2)*(w2 - w1)... wait, need care: position numbering.
   d indices (0-based): parent d = [max(0,1-2), 0, max(0,c-2)] = [0,0,c-2]
   child d = [0, max(0, c-2)] = [0, c-2]
   P_parent = w3*(c-2)  [index2], P_child = w2*(c-2) [index1]
   P_child - P_parent = (c-2)(w2 - w3).  [positions 2 vs 3]
For the move to be non-increasing we need w2 <= w3. But a right-moving defect
gives the opposite. We show no consistent choice survives.
"""
def diff(row):
    return [abs(row[i]-row[i+1]) for i in range(len(row)-1)]
def defect(row):
    return [max(0, x-2) for x in row]

# Two transitions:
# (A) defect moves RIGHT (simpler, the one I want to confirm exactly):
#     A = (x, large) with x in {0,2} and large=c>2:
#        child=(c, ...) putting defect at position1.
# Let's instead directly test the LP-found infeasibility with a concrete scale.
print("ORACLE: brute force check that NO weight vector can cover these two rows:")
print()
rows_to_test = {
    "right-move A=(0,4,0)":  [0,4,0],
    "left-move  A=(1,0,4)":  [1,0,4],
}
for name, A in rows_to_test.items():
    Ap = diff(A)
    d, dp = defect(A), defect(Ap)
    print(name)
    print("   A  =", A, " d=", d)
    print("   A' =", Ap, " d'=", dp)
    # coefficient vector in terms of w1,w2,w3 (positions 1,2,3)
    coef = [0,0,0]
    for i in range(3):
        c = (dp[i] if i < len(dp) else 0) - (d[i] if i < len(d) else 0)
        coef[i] = c
    print("   P'-P =", " + ".join(f"({c})*w{i+1}" for c,i in zip(coef,range(3)) if c!=0))
    print()
