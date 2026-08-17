"""Independent exact check of the n=5 traceless-slice 0-dimensionality.

The claim "a2,a3 not nilpotent -> slice not 0-dim" contradicts CA_5 (settled
true), so it must be a computation artifact.  Cross-check by reducing the
whole computation mod p (exact arithmetic, no huge-coefficient issues):
  - compute grevlex GB of (R_1..R_4) over GF(p) for good p
  - count standard monomials (finite iff 0-dim)
  - check whether a3^e becomes a leading monomial for some e
If mod-p slice is 0-dim but QQ slice is not, the QQ grevlex GB (huge integer
coefficients) is the suspect.
"""
from sympy import symbols, Poly, expand, resultant, groebner, QQ, GF, binomial
import itertools

x = symbols("x")


def hasse(f, i):
    p = Poly(expand(f), x)
    c = {j: p.coeff_monomial(x ** j) for j in range(p.degree() + 1)}
    return sum(binomial(j, i) * cc * x ** (j - i)
               for j, cc in c.items() if j >= i)


def slice_dim(n, p):
    a = symbols(f"a_1:{n+1}")
    f = x ** n + sum(a[i] * x ** (n - 1 - i) for i in range(n))
    sl = list(a[1:])
    R = [expand(resultant(f, hasse(f, i), x).subs(a[0], 0)) for i in range(1, n)]
    D = GF(p) if p else QQ
    Rp = [Poly(r, *sl, domain=D).as_expr() for r in R]
    gb = groebner(Rp, *sl, order="grevlex", domain=D)
    LMs = []
    for g in gb.polys:
        gg = g if isinstance(g, Poly) else g.as_poly(*sl, domain=D)
        lp = Poly(gg.LM().as_expr(), *sl, domain=D)
        LMs.append(tuple(lp.degree(v) for v in sl))
    LMs = sorted(set(LMs))
    # standard monomials
    def is_std(ev):
        return not any(all(le <= ee for le, ee in zip(lev, ev)) for lev in LMs)
    cap = {3: 40, 5: 40}
    std = [ev for ev in itertools.product(range(cap[n]), repeat=n - 1) if is_std(ev)]
    maxe = [max(e[i] for e in std) for i in range(n - 1)] if std else None
    # check for pure a3-type LM (last-but... variable index 1 in 0-based a2,a3..)
    pure_a3 = any(e[1] > 0 and all(e[k] == 0 for k in (0, 2, 3)) for e in LMs)
    return len(LMs), len(std), maxe, pure_a3


for p in (101, 10007):
    nl, nstd, maxe, pure_a3 = slice_dim(5, p)
    print(f"n=5 mod p={p}: #LM={nl}, #standard={nstd}, max std exp={maxe}, pure-a3 LM={pure_a3}")
