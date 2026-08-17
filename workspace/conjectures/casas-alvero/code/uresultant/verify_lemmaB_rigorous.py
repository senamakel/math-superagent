"""Rigorous spot-check of Lemma B on the traceless slice.

After fixing beta_n = -(beta_1+...+beta_{n-1}), each factor
A_{i,k} = e_{n-i}({beta_k - beta_j}_{j!=k}) becomes a polynomial in the n-1
free traceless params. Lemma B claims each A_{i,k} is a NONZERO polynomial and
hence (integral domain) the product is nonzero. To *stress-test* the claim we
check the polynomial is not the zero polynomial by expanding it symbolically in
the n-1 free variables and confirming at least one monomial has a nonzero
coefficient -- not just nonzero at one random point.
"""
import sympy as sp

def E(m, vars_):
    return sum(sp.prod([vars_[idx] for idx in sub]) for sub in sp.subsets(range(len(vars_)), m))

def check_factor_nonzero(n, i):
    free = sp.symbols('b0:%d' % (n-1))
    beta = list(free) + [-sum(free)]   # beta_n = -(sum of free)
    m = n - i
    for k in range(n):
        diffs = [beta[k] - beta[j] for j in range(n) if j != k]
        A = sp.expand(E(m, diffs))
        P = sp.Poly(A, *free)
        if P.degree() < 0 or all(c == 0 for _, c in P.terms()):
            return False, k, A
    return True, None, None

if __name__ == '__main__':
    allok = True
    for n in range(3, 8):
        for i in range(1, n):
            ok, k, A = check_factor_nonzero(n, i)
            if not ok:
                allok = False
                print(f"  n={n} i={i} k={k}: factor is ZERO POLY: {A}")
    print("LEMMA B: every factor is a nonzero polynomial on the traceless slice, n=3..7"
          if allok else "LEMMA B: FACTOR VANISHES IDENTICALLY (claim would be wrong)")
