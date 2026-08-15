from fractions import Fraction
from math import comb

# Moser spindle chromatic counts P(k) at k=4..14 (exact, from captured artifact)
P = {4:384, 5:5040, 6:31680, 7:134400, 8:443520, 9:1227744, 10:2983680,
     11:6557760, 12:13305600, 13:25293840, 14:45549504}

# Claim: P is a degree-7 polynomial in k.  A degree-d sequence satisfies the
# (d+1)-th finite-difference zero, i.e. the order-8 binomial recurrence:
#   sum_{i=0}^{8} (-1)^i C(8,i) P(k-i) = 0   for all k.
# Equivalent: P(k) = sum_{i=1}^{8} (-1)^{i+1} C(8,i) P(k-i).
coef = [(i, (-1)**(i+1) * comb(8, i)) for i in range(1, 9)]
print("order-8 binomial coefficients c_i for P(k)=sum c_i P(k-i):", coef)

ok = True
for k in range(12, 15):          # terms in range that allow 8 predecessors
    rhs = sum(c * P[k-i] for i, c in coef)
    if rhs != P[k]:
        ok = False
        print(f"MISMATCH at k={k}: P(k)={P[k]} vs sum={rhs}")
print("order-8 binomial recurrence over available k=12..14:", "HOLDS" if ok else "FAILS")

# Higher-order: any degree-d polynomial also satisfies order-(d+1) recurrence
# (x-1)^{d+1}.  Since degree is 7, order 8 with char poly (x-1)^8.
# Why did find_linear_recurrence(m<=9) report none? Test: does order 9 with
# general coefficients also fit?  Any extension also fits trivially; the tool's
# "no order<=9" likely reflects that the shortest (minimal) recurrence is
# exactly order 8, whose characteristic polynomial may not be (x-1)^8 if the
# tool seeks the *shortest* and the polynomial's finite support breaks it.
# Cross-check: verify the constant 8th difference is 0 and 7th is 5040.

def diffs(seq):
    out = [seq]
    while True:
        nxt = [out[-1][i+1]-out[-1][i] for i in range(len(out[-1])-1)]
        out.append(nxt)
        if len(nxt) == 1:
            return out

vals = [P[k] for k in range(4, 15)]
D = diffs(vals)
print("\n7th differences:", D[7])
print("8th differences:", D[8])
print("constant 7th diff =", D[7][0], "(degree 7, leading coeff = this/7!)")

# divisibility structure from factored form P=k(k-1)(k-2)^2(k-3)(k^2-3k+4)
import sympy as sp
k = sp.symbols('k')
poly = k*(k-1)*(k-2)**2*(k-3)*(k**2-3*k+4)
poly = sp.expand(poly)
print("\nexpanded:", sp.factor(poly))
print("P mod 48 for k=4..14:", [sp.nsimplify(poly.subs(k, kv)) % 48 for kv in range(4, 15)])
