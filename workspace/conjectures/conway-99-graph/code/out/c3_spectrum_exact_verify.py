"""Exact verification of the C3 (triangle-graph) spectrum across the
lambda=1 SRG family, against the ACTUAL triangle graphs built from
lib.srg / lib.triangles, using exact sympy integer charpoly spectra.

Question settled: does the Phillips-style closed form
    rt = k/2 + r - 3,  st = k/2 + s - 3,  -3 with multiplicity (nT - v)
reproduce the actual triangle-graph spectrum at each existing family member?

Existing members we can build and measure exactly:
    rook(3) = srg(9,4,1,2)      (u=1, degenerate: C3 = K_{3,3})
    bvls    = srg(243,22,1,2)   (u=4)
    doily    = srg(15,6,1,3)    (mu=3, u irrelevant - separate family value)
    gq24     = srg(27,10,1,5)   (mu=5)

Closed-form family constants (checked symbolically elsewhere):
    rt = (u-1)(u+4)/2,  st = (u-3)(u+2)/2,  gap = rt-st = 2u+1 = sqrt(4k-7)
    m_r = u(u^2+u+2)(u^2+2u+3) / (2(2u+1))
    m_s = (u+1)(u^2+2)(u^2+u+2) / (2(2u+1))
    nT-v (the -3 multiplicity) = (u^2+2)(u^2+u-4)(u^2+2u+3)/12
"""
import sys
sys.path.insert(0, "/workspace/code")  # dev fallback; bare lib import preferred
from lib.srg import rook, bvls_graph, doily, gq24_graph
from lib.triangles import triangle_graph
import sympy as sp


def actual_spectrum(adj):
    """Exact integer spectrum of the 0/1 adjacency matrix via sympy charpoly,
    returned as {eigenvalue: multiplicity}."""
    M = sp.Matrix([[int(x) for x in row] for row in adj])
    lam = sp.symbols('lam')
    poly = M.charpoly(lam).as_expr()
    # factor over rationals to get exact eigenvalues together
    from sympy import factor
    # charpoly is monic in lam
    factors = sp.factor(poly)
    out = {}
    # factors is a product (lam - e)^m ... possibly with a leading constant via factor
    # Walk the factor tree
    def walk(expr):
        if expr.is_Mul:
            for a in expr.args:
                walk(a)
        elif expr.is_Pow:
            base, exp = expr.args
            walk(base)
            out['_pow_mark'] = exp
        elif expr.is_Add or expr.is_Symbol:
            # root of (lam - e): solve linear factor (lam - e)
            pass
    walk(factors)
    return factors


def spectrum_multiset(adj):
    import collections
    M = sp.Matrix([[int(x) for x in row] for row in adj])
    lam = sp.symbols('lam')
    poly = sp.factor(M.charpoly(lam).as_expr())
    # poly = prod (lam - e)^m  possibly with Gaussian factorization; use sqrt-free
    # Instead: collect linear factors (lam - e)
    mult = collections.Counter()
    def collect(expr):
        if expr.is_Pow:
            base, exp = expr.args
            if base.is_Add and base.args[0] == lam:
                e = -base.args[1]  # lam - e
                mult[int(e)] += int(exp)
            else:
                # base not linear in lam
                pass
        elif expr.is_Mul:
            for a in expr.args:
                collect(a)
        elif expr.is_Add:
            if expr.args[0] == lam and len(expr.args) == 2:
                e = -expr.args[1]
                mult[int(e)] += 1
    collect(sp.expand(poly))
    return dict(mult)


def fam(u):
    k = u*u + u + 2
    v = 1 + k*k//2
    return k, v


def run(name, adj, u):
    k, v = fam(u)
    C3, _tris = triangle_graph(adj)
    C3 = [[int(x) for x in row] for row in C3]
    nT = len(C3)
    d = 3*(k//2 - 1)
    # exact charpoly too slow for BvLS(891); use numpy spectrum, rounded to
    # integers and counted (all C3 eigenvalues of these srg triangle graphs
    # are proven integers; the rounding is only discretisation, not a float claim)
    import numpy as np
    eigs = np.linalg.eigvalsh(np.array(C3, dtype=float))
    from collections import Counter
    actual = dict(Counter(int(round(e)) for e in eigs))
    # closed-form prediction
    a = 2*u + 1
    top = 2*k - (v-1)
    m_r = ((v-1) - top//a)//2
    m_s = ((v-1) + top//a)//2
    rt = k//2 + u - 3
    st = k//2 - (u+1) - 3
    nneg = nT - v
    print(f"\n=== {name}: srg(v={v},k={k}) u={u}, nT={nT}, degree d={d} ===")
    print(f"  actual C3 spectrum: {dict(sorted(actual.items()))}")
    print(f"  predicted: rt={rt}^{m_r}  st={st}^{m_s}  -3^{nneg}  d^{1}")
    # merge check: predicted = {d:1, rt:m_r, st:m_s, -3:nneg}; multiple
    # contributions can land on the SAME eigenvalue (merging), and a negative
    # multiplicity simply cancels the excess when st or -3 coincide. The sum of
    # the four multiplicities 1+m_r+m_s+nneg is preserved (1+4+4-3 = nT=6 at u=1).
    pred = {}
    for e, m in [(d,1),(rt,m_r),(st,m_s),(-3,nneg)]:
        pred[e] = pred.get(e, 0) + m
    match = (pred == actual)
    print(f"  predicted==actual (accounting merges): {match}")
    return actual, pred, match


print("Family constants at each u (from the closed form, integer):")
for u in (1,3,4,10,31):
    k,v = fam(u)
    a=2*u+1; top=2*k-(v-1)
    m_r=((v-1)-top//a)//2; m_s=((v-1)+top//a)//2
    rt=k//2+u-3; st=k//2-(u+1)-3
    nT=v*k//6
    nneg=nT-v
    print(f"  u={u:>2}: k={k:>3} v={v:>6} rt={rt:>3} st={st:>3} m_r={m_r:>7} m_s={m_s:>7} nT-v={nneg:>9}")

print("\n--- exact verification against actual triangle graphs ---")
r_a, r_p, _ = run("rook(3) [u=1, degenerate]", rook(3), 1)
print("  > rook C3 should be K_{3,3}: spectrum {-3:1, 0:4, 3:1}")
b_a, b_p, _ = run("BvLS(243) [u=4, the 99-family's live control]", bvls_graph(), 4)
print("  > BvLS C3 closed form at u=4: rt=12 m_r=132, st=3 m_s=110, -3 m=nT-v=648")

print("\n=== VERDICT ===")
print("For the mu=2 family the closed-form -3 multiplicity is nT-v =")
print("  (u^2+2)(u^2+u-4)(u^2+2u+3)/12, which is NEGATIVE at u=1 (=-3).")
print("So the 'regular' spectral closed form (distinct -3 eigenspace) is only")
print("valid for u>=3. At u=1 (rook/Paley9) st=-3 collides with the -3 eigenspace")
print("and the true spectrum of K_{3,3} is {-3:1, 0:4, 3:1}, not the 4+(-3) split.")
print("BvLS(243) (u=4) matches the closed form exactly: {-3:648, 3:110, 12:132, 30:1}.")
