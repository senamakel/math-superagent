"""Definitive verification of the canonical srg oracle, lib/srg.py.

Every rejection reason is checked to exercise the *discriminating* logic, not
just the cheap shape/degree guards:

  - C9(1,2) is 4-regular on 9 vertices but is NOT the rook's graph: it must
    fail (9,4,1,2) citing a common-neighbour (lambda/mu) mismatch, not shape
    or degree.  [count-path negative at 9]
  - random_regular_14_99(seed=1) is the circulant C99 (1..7): 14-regular on
    99 vertices but must fail (99,14,1,2) citing a count mismatch. [count-path
    negative at 99]

This is the file that produced code/out/oracle_verification.captured.txt, the
artifact that promotes the oracle rows from "asserted" to "checked".
"""
import numpy as np
from lib.srg import is_srg, rook, bvls_graph, random_regular_14_99


def circulant(n, conn):
    A = np.zeros((n, n), dtype=np.int64)
    for i in range(n):
        for s in conn:
            A[i, (i + s) % n] = 1
            A[i, (i - s) % n] = 1
    np.fill_diagonal(A, 0)
    return A


def petersen():
    A = np.zeros((10, 10), dtype=np.int64)
    for i in range(5):
        A[i, (i + 1) % 5] = 1            # outer 5-cycle
        A[i, 5 + i] = 1                  # spokes
        A[5 + i, 5 + ((i + 2) % 5)] = 1  # inner pentagram
    A |= A.T
    np.fill_diagonal(A, 0)
    return A


def fmt(res):
    ok, why = res
    return "PASS" if ok else "FAIL"


if __name__ == "__main__":
    print("Ran: python code/out/verify_oracle.py (from /workspace); oracle imported from lib/srg.py")
    print("Oracle function: is_srg(A, v, k, lam, mu) from code/lib/srg.py, "
          "exact integer common-neighbour counts via A@A")
    print("Inputs: rook(3) on (9,4,1,2); bvls_graph() on (243,22,1,2); "
          "random_regular_14_99(seed=1) on (99,14,1,2); C9(1,2) circulant on (9,4,1,2); "
          "rook(4) on (9,4,1,2); Petersen on (9,4,1,2) and (10,3,0,1)")
    print("=" * 74)
    print("ORACLE VERIFICATION — lib/srg.is_srg, exact integer common-neighbour counts")
    print("=" * 74)

    print("\n[1] Positive controls")
    print("  rook(3)        srg(9,4,1,2):     %s  %s" % (fmt(is_srg(rook(3), 9, 4, 1, 2)),
          is_srg(rook(3), 9, 4, 1, 2)[1]))
    B = bvls_graph()
    print("  bvls shape %s  edges %d (expect 2673=243*22/2)"
          % (B.shape, int(B.sum() // 2)))
    print("  bvls_graph()   srg(243,22,1,2):  %s  %s"
          % (fmt(is_srg(B, 243, 22, 1, 2)), is_srg(B, 243, 22, 1, 2)[1]))

    print("\n[2] Negative controls that pass shape + regularity, fail only on counts")
    C9 = circulant(9, [1, 2])
    print("  C9(1,2) 4-regular on 9v:", bool(np.all(C9.sum(axis=1) == 4)))
    print("  C9(1,2)        srg(9,4,1,2):     %s  %s"
          % (fmt(is_srg(C9, 9, 4, 1, 2)), is_srg(C9, 9, 4, 1, 2)[1]))
    R = random_regular_14_99(seed=1)
    print("  rand14-99 14-regular on 99v:", bool(np.all(R.sum(axis=1) == 14)))
    print("  rand14-99      srg(99,14,1,2):   %s  %s"
          % (fmt(is_srg(R, 99, 14, 1, 2)), is_srg(R, 99, 14, 1, 2)[1]))

    print("\n[3] Other negatives (may fail on shape/degree)")
    print("  rook(4)        srg(9,4,1,2):     %s  %s"
          % (fmt(is_srg(rook(4), 9, 4, 1, 2)), is_srg(rook(4), 9, 4, 1, 2)[1]))
    P = petersen()
    print("  Petersen srg(10,3,0,1) sanity:  %s" % fmt(is_srg(P, 10, 3, 0, 1)))
    print("  Petersen       srg(9,4,1,2):     %s  %s"
          % (fmt(is_srg(P, 9, 4, 1, 2)), is_srg(P, 9, 4, 1, 2)[1]))

    print("\n[4] Independent BvLS spectrum cross-check (suggestive, not decisive)")
    ev = np.round(np.linalg.eigvalsh(B.astype(float)), 6)
    vals, cnts = np.unique(ev, return_counts=True)
    for vv, cc in zip(vals, cnts):
        print("    eigenvalue %s  multiplicity %s" % (vv, cc))
    print("    expected 22^1, 4^132, -5^110")
