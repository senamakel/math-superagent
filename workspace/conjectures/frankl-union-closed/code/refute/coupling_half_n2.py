r"""Run the n=2 exhaustive search (script form for actual execution).

Attacks G-coupling-half.  mu uniform over a subset of the 4 masks {00,01,10,11}
on n=2, max marginal < 1/2, H>0.  For each, we compute sup over ALL symmetric
couplings of H(A∨B).  If that sup <= H(mu), then a fortiori no conditionally-iid
coupling achieves H(A∨B) > H(mu): refutation.  This is a documented numeric
check (SLSQP), and any refutation found is then hand-verified.
"""
import itertools
import numpy as np
from scipy.optimize import minimize

def test_mu_uniform(support):
    k = len(support)
    n = 2
    masks = list(range(1 << n))
    m1 = sum(((m >> 1) & 1) for m in support) / k
    m2 = sum((m & 1) for m in support) / k
    if max(m1, m2) >= 0.5 - 1e-9:
        return None
    Hmu = np.log2(k)
    if Hmu <= 0:
        return None
    mu_vec = np.array([1 / k if m in support else 0.0 for m in masks])
    idx = [(i, j) for i in range(4) for j in range(i, 4)]
    free = len(idx)

    def joint(par):
        J = np.zeros((4, 4))
        for t, (i, j) in enumerate(idx):
            J[i][j] = J[j][i] = par[t]
        return J

    def orp(J):
        o = np.zeros(4)
        for a in range(4):
            for b in range(4):
                o[a | b] += J[a][b]
        return o

    def ent(p):
        p = np.clip(p, 1e-15, 1)
        return -(p * np.log2(p)).sum()

    def obj(par):
        return -ent(orp(joint(par)))

    cons = [{'type': 'eq', 'fun': lambda x: joint(x).sum(axis=1) - mu_vec}]
    bounds = [(0, 1 + 1e-6)] * free
    best = 1e9
    rng = np.random.default_rng(7)
    ind0 = np.outer(mu_vec, mu_vec)
    par0 = [ind0[i][j] for (i, j) in idx]
    starts = [par0]
    for _ in range(800):
        starts.append(rng.dirichlet(np.ones(4)))
    for sp in starts:
        r = minimize(obj, np.array(sp, float), method='SLSQP', bounds=bounds,
                     constraints=cons, options={'maxiter': 900, 'ftol': 1e-14})
        if r.fun < best:
            J = joint(r.x)
            if (J >= -1e-7).all() and np.allclose(J.sum(axis=1), mu_vec, atol=1e-6):
                best = r.fun
    if best > 1e8:
        return None
    return (support, Hmu, -best, -best > Hmu + 1e-9)

results = []
for r in range(1, 5):
    for support in itertools.combinations(range(4), r):
        res = test_mu_uniform(support)
        if res is not None:
            results.append(res)

print("n=2 uniform supports, max marginal<1/2 (refutation = maxH<=Hmu):")
print(f"{'support':<16}{'H(mu)':>8}{'maxH':>10}{'refuted?':>10}")
refs = [r for r in results if r[3]]
for support, Hmu, maxH, ref in sorted(results, key=lambda x: -x[3]):
    print(f"{str(support):<16}{Hmu:8.4f}{maxH:10.4f}{str(ref):>10}")
print("\n# refuted:", len(refs))
for r in refs[:5]:
    print("  e.g.", r[0], "H(mu)=", r[1], "maxH=", r[2])
