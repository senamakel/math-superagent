"""Verify the closed form of the coclique bound alpha = v(-s)/(k-s) for the
family srg(v,k,1,2), k = u^2+u+2, over many u (exact integers).
Eigenvalues: r = u, s = -(u+1)  (negative root; disc = 4k-7 = (2u+1)^2).
Conjecture alpha = (u*k+2)/2 identically.
Also test: is alpha always an integer? and find first term that would falsify."""
import sympy as sp

u = sp.symbols('u')
k = u**2 + u + 2
v = 1 + k**2/2
s = -(u+1)
alpha_sym = sp.simplify(sp.expand(v*(-s)/(k - s)))
print("symbolic alpha =", sp.simplify(alpha_sym))
print("(u*k+2)/2      =", sp.expand((u*k+2)/2))
print("equal:", sp.simplify(alpha_sym - (u*k+2)/2) == 0)

# exact integer check over u=1..200 for a wide non-family-sparse range
mismatch = []
for uu in range(1, 201):
    kk = uu*uu + uu + 2
    vv = 1 + kk*kk//2
    ss = -(uu+1)
    alpha = sp.Integer(vv*(-ss)) // sp.Integer(kk - ss)
    assert alpha * (kk - ss) == vv * (-ss), (uu, "not integer bound / mismatch")
    pred = (uu*kk + 2)//2
    if alpha != pred:
        mismatch.append((uu, alpha, pred))
print("mismatches over u in [1,200]:", mismatch[:5], "count", len(mismatch))
print("first falsifying term would be u=1, k=4, alpha=3 if pred!=3:", (1*4+2)//2 == 3)

# integrality: show u*k always even => alpha integer for all u
print("u*k parity check over [1,1000]:",
      all((uu*(uu*uu+uu+2)) % 2 == 0 for uu in range(1,1001)))
