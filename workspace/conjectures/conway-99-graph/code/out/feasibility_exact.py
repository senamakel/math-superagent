"""Exact integrality feasibility for srg(v,k,1,2) — corrected general formula.

For general (v,k,lambda,mu): eigenvalues k, r, s with
    delta = (lambda-mu)^2 + 4*(k-mu)
    r,s   = (lambda-mu +- sqrt(delta))/2
    mult_s = g = 1/2 [ (v-1) - (2k + (v-1)(lambda-mu)) / sqrt(delta) ]
    mult_r = f = (v-1) - g
with v = 1 + k + k(k-2)/2 from counting (mu=2 case).

The earlier note code/out/feasibility-candidates.md used the r=3,s=-4 formula
f = (-k+4(v-1))/7, which is ONLY valid when delta=49 (k=14). For other k the
eigenvalues differ, so that note's claim that k=32 "passes integrality" is wrong.
Correct it here with the general formula, exact integer arithmetic.
"""
from sympy import integer_nthroot

lam, mu = 1, 2

def feas(k):
    v = 1 + k + k*(k-2)//2
    delta = (lam-mu)**2 + 4*(k-mu)          # 4k - 7
    root, perfect = integer_nthroot(delta, 2)
    if not perfect:
        return v, None, None, None, None, False, "4k-7 not a perfect square"
    # eigenvalues
    num_r = (lam-mu) + root
    num_s = (lam-mu) - root
    if num_r % 2 != 0 or num_s % 2 != 0:
        return v, None, None, None, None, False, "eigenvalues not integers"
    r, s = num_r//2, num_s//2
    # multiplicity of s
    term = 2*k + (v-1)*(lam-mu)
    if term % root != 0:
        return v, r, s, None, None, False, f"multiplicity numerator {term} not divisible by {root}"
    q = term // root
    gnum = (v-1) - q
    if gnum % 2 != 0:
        return v, r, s, None, None, False, "multiplicity not integer (odd)"
    g = gnum // 2
    f = (v-1) - g
    if f < 0 or g < 0:
        return v, r, s, f, g, False, "negative multiplicity"
    return v, r, s, f, g, True, "feasible"

print("  k     v   r     s   f(r)  g(s)  feasible  note")
for k in [4, 8, 14, 22, 32, 44, 112, 994]:
    v, r, s, f, g, ok, note = feas(k)
    print(f"{k:>4} {v:>5} {str(r):>4} {str(s):>5} {str(f):>6} {str(g):>6}  {str(ok):>8}  {note}")
