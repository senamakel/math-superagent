"""Euler characteristics of the clique complex (flag complex) of the controls,
and exact beta_1 via modular rank of the triangle-edge boundary map.

For the clique complex of a connected graph G=(V,E) with triangles T:
  chi = |V| - |E| + |T| = 99-693+231 = -363 at (99,14,1,2);
  beta_0 = 1;  beta_2 - beta_1 = chi - 1.
H_1(Cl(G);Q) rank = (|E|-|V|+1) - rk_Q(delta_2)  where delta_2: C_2 -> C_1
maps each triangle {a,b,c} to the 1-chain ab+bc+ca.

We compute rk_Fp(delta_2) for the controls at two primes (1009, 65537) by
sparse modular elimination; agreement of the two primes is the evidence the
rank is generic (i.e. equals the rational rank). Exact integer arithmetic,
mod-p only.

Inventor's files claim "rook: 6 triangles chi=1" — the triangle count 6 is
right; we recompute chi exactly here.
"""
import itertools
import numpy as np
from lib.srg import rook, bvls_graph


def triangles(A, v):
    A = np.asarray(A, dtype=np.int64)
    tris = []
    for a in range(v):
        for b in range(a + 1, v):
            if not A[a, b]:
                continue
            for c in range(b + 1, v):
                if A[a, c] and A[b, c]:
                    tris.append((a, b, c))
    return tris


def boundary_rank_modp(edge_idx, tri_list, p):
    """Rank over F_p of delta_2: triangle {a,b,c} -> ab+bc+ca.
    edge_idx: dict (min,max) -> column index.  Returns rank."""
    # columns = triangles; rows = edges; sparse elimination with pivot map
    # col_sets[c] = set of row indices currently nonzero in column c
    rows = {}   # row r -> dict col->value (nonzero)
    for c, (a, b, c3) in enumerate(tri_list):
        rows.setdefault(edge_idx[(min(a, b), max(a, b))], {})[c] = 1
        rows.setdefault(edge_idx[(min(b, c3), max(b, c3))], {})[c] = 1
        rows.setdefault(edge_idx[(min(a, c3), max(a, c3))], {})[c] = 1
    # Gaussian elimination on columns (c = 0..ntri-1), pivot per column
    piv = {}  # pivot row -> column
    rank = 0
    for c in range(len(tri_list)):
        # find a row with nonzero at column c
        cand = [r for r in rows if c in rows[r] and rows[r][c] % p != 0]
        while cand:
            r = cand[0]
            val = rows[r][c] % p
            inv = pow(val, p - 2, p)
            # normalize row r
            rows[r] = {cc: (v * inv) % p for cc, v in rows[r].items()}
            # eliminate c from all other rows
            others = [rr for rr in rows if rr != r and c in rows[rr]]
            for rr in others:
                f = rows[rr].pop(c, 0) % p
                if f:
                    for cc, vv in rows[r].items():
                        rows[rr][cc] = (rows[rr].get(cc, 0) - f * vv) % p
                    if not rows[rr]:
                        del rows[rr]
            piv[r] = c
            rank += 1
            break
        else:
            continue
    return rank


def report(name, A, v):
    A = np.asarray(A, dtype=np.int64)
    e = int(A.sum() // 2)
    tris = triangles(A, v)
    t = len(tris)
    chi = v - e + t
    edge_idx = {}
    for a in range(v):
        for b in range(a + 1, v):
            if A[a, b]:
                edge_idx[(a, b)] = len(edge_idx)
    print(f"--- {name}: v={v}, e={e}, triangles={t}, chi={v}-{e}+{t} = {chi}")
    # cycle space dim = e - v + 1
    for p in (1009, 65537):
        r = boundary_rank_modp(edge_idx, tris, p)
        beta1 = (e - v + 1) - r
        print(f"    mod {p}: rk(delta_2) = {r},  beta_1 = {e-v+1} - {r} = {beta1}, "
              f"beta_2 = beta_1 + (chi-1) = {beta1 + chi - 1}")


if __name__ == "__main__":
    report("rook(3)", rook(3), 9)
    report("bvls(243)", bvls_graph(), 243)