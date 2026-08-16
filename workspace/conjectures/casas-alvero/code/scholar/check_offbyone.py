"""Verify the recorded off-by-one bug in the as-is esym_from_diffs helper.

The as-is verify_rootdiff_identity.py defines:
    esym_from_diffs(betas, x, y, k) = Poly(expand(prod((x-b)+y for b in betas)), y).nth(k)
and then checks H_i(f) == esym_from_diffs(betas, n-i).

Claim on record: nth(k) returns e_{n-k}(x-beta_*), NOT e_k, so the as-is
check compares H_i against e_i instead of e_{n-i}.

Test: comparing the two candidate meanings against the true H_i for n=4.
"""
import sympy as sp
from sympy import symbols, prod, expand, Poly

x, t, y = symbols("x t y")

for n in (3, 4, 5):
    betas = symbols("b1:%d" % (n + 1))
    fexpr = prod(x - b for b in betas)

    # true H_i
    ft = expand(fexpr.subs(x, x + t))
    Hs = {i: Poly(ft, t).nth(i) for i in range(n + 1)}

    # as-is helper meaning
    e = expand(prod((x - b) + y for b in betas))
    Pe = Poly(e, y)
    def asis(k):
        return Pe.nth(k)
    # correct e_k meaning via combinations
    from itertools import combinations
    def corr(k):
        tot = 0
        for S in combinations(betas, k):
            p = 1
            for b in S:
                p *= (x - b)
            tot += expand(p)
        return expand(tot)

    print(f"n={n}")
    for i in range(n + 1):
        hi = expand(Hs[i].as_expr())
        gi = expand(asis(n - i))   # what the as-is script compares H_i to
        ci = expand(corr(n - i))   # the correct e_{n-i}
        match_asis = sp.simplify(expand(hi - gi)) == 0
        match_corr = sp.simplify(expand(hi - ci)) == 0
        # Also: does asis(n-i) equal e_i?  (the recorded claim)
        equals_ei = sp.simplify(expand(asis(n - i) - corr(i))) == 0
        print(f"  i={i}: asis(n-i) matches H_i? {match_asis}; "
              f"corr(n-i) matches H_i? {match_corr}; "
              f"asis(n-i) == e_i? {equals_ei}")
