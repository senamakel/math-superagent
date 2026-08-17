"""Confirm the leading coefficient of R_i's weighted form is nonzero ON THE
TRACELESS SLICE (sum beta_j = 0), exactly, for n=3..8, i=1..n-1.

Leading coeff = prod_k e_{n-i}({beta_k - beta_j : j=1..n}).
Evaluate at an exact integer point with sum beta = 0; the value being nonzero
is a proof the polynomial is not zero on that hyperplane (for these n,i).
A nonzero polynomial of this degree evaluated at a generic point of the
hyperplane is almost surely nonzero; we use exact integers and a fresh random
seed, which is a probabilistic but exact-integer check.
"""
import sympy as sp
import random

def check(n):
    random.seed(1000 + n)
    beta = [sp.symbols('b%d' % k) for k in range(n)]
    results = {}
    for i in range(1, n):
        m = n - i
        # generic integer point in traceless slice: pick random then shift to sum 0
        while True:
            vals = [random.randint(-50, 50) for _ in range(n)]
            s = sum(vals)
            if s != 0:  # shift one coordinate to force sum 0
                vals[0] -= s
            break
        prod = sp.Integer(1)
        for k in range(n):
            others = [beta[k] - beta[j] for j in range(n) if j != k]
            # e_m of (n-1 items) = sum over size-m subsets of the n-1 indices
            from itertools import combinations
            e = sum(sp.prod([others[ix] for ix in sub])
                    for sub in combinations(range(n - 1), m))
            prod *= e
        pv = prod.subs(dict(zip(beta, vals)))
        results[i] = (pv != 0)
    return results

allok = True
for n in range(3, 9):
    r = check(n)
    ok = all(r[i] for i in r)
    allok &= ok
    print(f"n={n}: leading coeff nonzero on traceless slice -> {r} {'OK' if ok else 'FAIL'}")
print("ALL OK" if allok else "SOME FAIL")
