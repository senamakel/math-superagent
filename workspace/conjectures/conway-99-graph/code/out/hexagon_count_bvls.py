"""Exact induced-C6 count on the BvLS srg(243,22,1,2), captured.

Runs lib.hexagons.count_induced_C6 on lib.srg.bvls_graph() and compares with
the Reimbayev-style closed form (1/12) n k (k-2) (2k^2-21k+53). Prints the
guard oracle check (rook(3) gives 6) at entry.
"""
import time
import numpy as np
from lib.srg import bvls_graph, rook
from lib.hexagons import count_induced_C6, hexagon_formula

if __name__ == "__main__":
    # Entry guard: the method must reproduce the small oracle before we trust
    # it at full size.
    r = count_induced_C6(rook(3))
    assert r == 6, f"rook(3) guard failed: {r}"
    print("entry guard: rook(3) induced C6 =", r, "(== formula 6)")

    B = bvls_graph()
    t0 = time.time()
    c = count_induced_C6(B, workers=1)
    dt = time.time() - t0

    f = hexagon_formula(243, 22)
    print(f"BvLS (243,22,1,2) induced C6 = {c}")
    print(f"closed-form value (1/12)*243*22*20*559 = {f}")
    print("equal:", c == f)
    print("wall-clock seconds:", round(dt, 3))
    print("guard: rook and BvLS both srg via lib.srg.is_srg:")
    from lib.srg import is_srg
    print("  rook   ", is_srg(rook(3), 9, 4, 1, 2))
    print("  bvls   ", is_srg(B, 243, 22, 1, 2))
