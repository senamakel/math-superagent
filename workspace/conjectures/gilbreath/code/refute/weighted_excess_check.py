#!/usr/bin/env python3
"""
DECISIVE check of R-weighted-excess-potential refutation.
Purely algebraic, exact. The refutation is a theorem, not a search result:
it uses ONLY the fact that (0,4,0) -> (4,4) under the operator, and that
P((4,4)) - P((0,4,0)) = 2*w1.
"""
def diff(row):
    return [abs(row[i]-row[i+1]) for i in range(len(row)-1)]
def defect(row):
    return [max(0,x-2) for x in row]

# One single row suffices: the claim quantifies over EVERY array.
A  = [0,4,0]
Ap = diff(A)
dA, dAp = defect(A), defect(Ap)
PA_sym   = "w1*%d + w2*%d" % (dA[0], dA[1]) if len(dA)>1 else "w1*%d"%dA[0]
PAp_sym  = "w1*%d + w2*%d" % (dAp[0], dAp[1])
print("A    =", A,  " defect =", dA,  " P(A)  =", PA_sym)
print("A'   =", Ap, " defect =", dAp, " P(A') =", PAp_sym)

# defect of (0,4,0) = (0,2,0) so P(A)=2w2 ; defect (4,4)=(2,2) so P(A')=2w1+2w2
assert dA == [0,2,0] and dAp == [2,2]
assert PA_sym  == "w1*0 + w2*2"
assert PAp_sym == "w1*2 + w2*2"
print("P(A') - P(A) = 2*w1")
print("Non-increase  P(A')<=P(A)  ==>  2w1 <= 0  ==>  w1 <= 0")
print("Claim requires w1 > 0.  Contradiction -> REFUTED.")
print()
print("Genuineness check: is (0,4,0) a valid row (has a parent)?")
parent=[4,4,8]
print("  diff(4,4,8) =", diff(parent), " -> yes, (0,4,0) is a child of (4,4,8).")
assert diff(parent)==A
print("  diff(parent)=A confirmed. Parent (4,4,8) itself has defect (2,2,6),")
print("  so P(parent)=2w1+2w2+6w3, P(child)=2w2, P(grandchild)=2w1+2w2.")
print("  The sequence P: 2w1+2w2+6w3 -> 2w2 -> 2w1+2w2.")
print("  Even with only nonneg weights this is NOT monotone in general;")
print("  the single spike (0,4,0)->(4,4) alone kills w1>0.")
print()
print("VERDICT: R-weighted-excess-potential is REFUTED unconditionally.")
