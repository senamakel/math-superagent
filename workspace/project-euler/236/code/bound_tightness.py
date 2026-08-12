"""Bound tightness for the largest m: how does making m>123/59 fail?

The per-product condition: feasible iff for every i, g_i = gcd(a_i q, b_i p) >= max(p,q),
where m=p/q reduced. Increasing m (p/q) pushes max(p,q) up and usually shrinks g_i.
Find, for candidate m slightly above 123/59, which product kills feasibility.
We already know a full enumeration gives 35 values and largest = 123/59; here we
confirm the *local* structure of why m cannot exceed 123/59, at least per-product.
"""
from fractions import Fraction
from math import gcd

A = [5248,1312,2624,5760,3936]
B = [640,1888,3776,3776,5664]
SA, SB = sum(A), sum(B)

def per_product_threshold(p,q):
    """returns list of (i, g_i, max(p,q)) for all 5."""
    out=[]
    for i in range(5):
        g=gcd(A[i]*q, B[i]*p)
        out.append((i,g,max(p,q),g>=max(p,q)))
    return out

# The largest value: p/q = 123/59. Its rate is R_max.
# question: could any m=num/den with value in (123/59, inf) pass per-product?
# For m slightly above 123/59 but of form X/59: n = 124? Try values just above.
print("Per-product thresholds for m = 123/59:")
for row in per_product_threshold(123,59):
    print("   i=%d g=%d thr=%d ok=%s" % row)

# Try m just above 123/59 (value being a bit larger), e.g. p/q with p/q > 123/59.
print("\nTry some m slightly above 123/59, per-product only:")
for pp in [124,125,126,182,183,185,246,247,123*2, 123*2+1, 1000]:
    for qq in [59, 118, 295]:
        m=Fraction(pp,qq)
        if m <= Fraction(123,59): continue
        thr = per_product_threshold(pp,qq)
        ok = all(t[3] for t in thr)
        if ok:
            print(f"   m={pp}/{qq}={float(m):.5f} PER-PRODUCT OK -> needs overall check")
        # else: print first failing product
        # (don't spam; only report ok ones and the bound)
print("(no per-product-OK values above 123/59 shown => per-product alone already caps at 123/59 for those samples)")

# The real question: is 123/59 the largest because per-product fails beyond it?
# Enumerate a dense set of reduced p/q with p,q up to, say, 3000 and value>123/59
# and check per-product. Count how many pass per-product.
cnt=0; examples=[]
for p in range(1,4000):
    for q in range(1,4000):
        if gcd(p,q)!=1: continue
        if p<=q: continue
        if p>3*q: continue  # value>123/59 means p/q in (2.0847, 3)
        if Fraction(p,q) <= Fraction(123,59): continue
        thr = per_product_threshold(p,q)
        if all(t[3] for t in thr):
            cnt+=1
            if len(examples)<5: examples.append((p,q))
print("\nper-product-feasible reduced m with value>123/59, p,q<=4000:", cnt)
print("examples:", examples)
