"""Confirm leading coefficient nonzero on traceless slice with DISTINCT values.
For i=1 the leading coeff is proportional to the discriminant^2; we prove it
cannot vanish as a polynomial by evaluating at guaranteed-distinct betas.
"""
import sympy as sp
from itertools import combinations

def check(n):
    # use explicitly distinct exact values, sum to 0 by shifting one
    vals = [1, 2, 3, 4, 5, 6, 7, 8, 9][:n]
    s = sum(vals)
    vals[0] -= s   # now sum 0, all distinct (first becomes very negative)
    beta = [sp.symbols('b%d' % k) for k in range(n)]
    results = {}
    for i in range(1, n):
        m = n - i
        prod = sp.Integer(1)
        for k in range(n):
            others = [beta[k] - beta[j] for j in range(n) if j != k]
            e = sum(sp.prod([others[ix] for ix in sub])
                    for sub in combinations(range(n - 1), m))
            prod *= e
        pv = prod.subs(dict(zip(beta, vals)))
        results[i] = (pv != 0, pv)
    return results, vals

allok = True
for n in range(3, 9):
    r, vals = check(n)
    ok = all(r[i][0] for i in r)
    allok &= ok
    print(f"n={n}: values={vals} lead nonzero -> { {i: r[i][0] for i in r} } "
          f"{'OK' if ok else 'FAIL'}")
    # show the i=1 value for clarity
    print(f"   i=1 leading value (should be ~discriminant^2): {r[1][1]}")
print("ALL OK" if allok else "SOME FAIL")
