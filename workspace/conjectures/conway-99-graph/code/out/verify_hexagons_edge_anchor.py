"""Independent induced-C6 count for BvLS via the fixed-directed-edge anchor.

Second, genuinely different route from lib/hexagons.py (which anchors at an
induced P4's first four vertices). Here we anchor each oriented hexagon
(a,b,c,d,e,f) at its directed edge (a,b) -- the cycle is traversed
a->b->c->d->e->f->a. Summing over ordered directed edges (a,b) counts each
undirected induced hexagon 12 times (6 edges x 2 directions).

Constraints for an induced hexagon (consecutive edges ab,bc,cd,de,ef,fa; all
other pairs non-adjacent). Non-consecutive pairs to forbid:
  a.c a.d a.e   b.d b.e b.f   c.e c.f   d.f
Using the matvec completion trick over (c,d,e) -> (f) candidates:
  for fixed (a,b,c,d,e):
    cand_f = N[e] & N[a] & ~N[b] & ~N[c] & ~N[d]   (f adj a and e, not b/c/d)
    subtract f in {a,b,c,d,e} automatically excluded (a in ~N[a] frame,
      and b,c,d,e handled: f==b excluded by ~N[b], f==c by ~N[c], f==d by
      ~N[d]; f==e excluded because N[e] diagonal is 0; f==a excluded by ~N[a]).
  count += |cand_f|
"""
import time
import numpy as np
from lib.srg import bvls_graph, rook, is_srg
from lib.hexagons import hexagon_formula


def count_induced_C6_edge_anchor(A):
    A = np.asarray(A, dtype=np.int64)
    n = A.shape[0]
    N = A.astype(bool)
    directed = 0
    for a in range(n):
        Na = N[a]
        for b in np.flatnonzero(Na):
            Nb = N[b]
            # c: adj b, not a, chord a.c forbidden -> c not in N[a]
            cand_c = Nb & ~Na
            cand_c[a] = False
            for c in np.flatnonzero(cand_c):
                Nc = N[c]
                # d: adj c, not {a,b}, not N[a] (a.d), not N[b] (b.d)
                cand_d = Nc & ~Na & ~Nb
                cand_d[a] = cand_d[b] = False
                for d in np.flatnonzero(cand_d):
                    Nd = N[d]
                    # e: adj d, not {a,b,c}, not N[a] (a.e), not N[b] (b.e),
                    #    not N[c] (c.e)
                    cand_e = Nd & ~Na & ~Nb & ~Nc
                    cand_e[a] = cand_e[b] = cand_e[c] = False
                    # f candidates via matvec (handled directly here fine)
                    for e in np.flatnonzero(cand_e):
                        Ne = N[e]
                        cand_f = Ne & Na & ~Nb & ~Nc & ~Nd
                        directed += int(cand_f.sum())
    return directed


if __name__ == "__main__":
    # entry guard on rook(3): should give directed = 12 * 6 = 72
    r = count_induced_C6_edge_anchor(rook(3))
    print("rook(3) directed =", r, "(expect 72), /12 =", r // 12)

    B = bvls_graph()
    t0 = time.time()
    d = count_induced_C6_edge_anchor(B)
    dt = time.time() - t0
    print(f"BvLS directed = {d}, divisible by 12: {d % 12 == 0}")
    print(f"BvLS induced C6 (directed/12) = {d // 12}")
    print("closed form =", hexagon_formula(243, 22), " equal:", d // 12 == hexagon_formula(243, 22))
    print("wall-clock seconds:", round(dt, 2))
