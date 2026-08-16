"""Confirm the eigen-recurrence for each fixed-type column, cleanly.

S(n,k) = (1/k!)*sum_{j=0..k} (-1)^(k-j) binom(k,j) j^n  (Stirling closed form).
For a FIXED type t (so fixed k = t+1), the count S(d-1, t+1) as a function of
d is a PLUS combination of the exponentials 1^n, 2^n, ..., k^n, hence obeys the
constant-coefficient recurrence whose characteristic polynomial is
prod_{j=1}^{k}(x - j)  =  x^k - e_1 x^{k-1} + e_2 x^{k-2} - ... (-1)^k e_k,
i.e.  a(n) = e_1 a(n-1) - e_2 a(n-2) + ... + (-1)^(k-1) e_k a(n-k),
where e_r is the elementary symmetric sum of {1,...,k}.
"""
from sympy import binomial, factorial

def closed_S(n, k):
    return sum((-1)**(k-j) * binomial(k, j) * j**n for j in range(k+1)) // factorial(k)

def elem_sym(k, r):
    # sum of products of r distinct elements chosen from {1..k}
    from itertools import combinations
    return sum(prod(c) for c in combinations(range(1, k+1), r))

def prod(seq):
    from functools import reduce
    from operator import mul
    p = 1
    for x in seq:
        p *= x
    return p

D = 30
all_ok = True
for t in range(0, 13):
    k = t + 1
    n_start = k          # need d-1 = n >= k, i.e. d >= k+1, but take d from t+2
    seq = [closed_S(d-1, k) for d in range(k+1, D+1)]
    # recurrence coefficients: c[r] multiplies a(n-r)
    cs = [ (-1)**(r-1) * elem_sym(k, r) for r in range(1, k+1) ]
    ok = all(seq[n] == sum(cs[r]*seq[n-1-r] for r in range(k))
             for n in range(k, len(seq)))
    all_ok &= ok
    cs_str = ", ".join(str(c) for c in cs)
    print(f"type {t:2d} (k={k:2d}): terms={len(seq):3d}  eigen-recurrence holds over ALL terms: {ok}")
    if not ok:
        # find first failure
        for n in range(k, len(seq)):
            if seq[n] != sum(cs[r]*seq[n-1-r] for r in range(k)):
                print(f"       FIRST FAIL at index n={n}: a[n]={seq[n]} vs "
                      f"recurrence={sum(cs[r]*seq[n-1-r] for r in range(k))}")
                break
print("\nALL columns satisfy their order-(t+1) eigen-recurrence:", all_ok)
