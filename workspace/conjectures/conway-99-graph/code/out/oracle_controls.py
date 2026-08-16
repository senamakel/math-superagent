"""Run ALL oracle controls and capture them into oracle-controls.captured.txt.

Every decision goes through the single canonical oracle lib.srg.is_srg; no
script decides inline. This is the run's guard set:

  POSITIVES
    rook(3)                      -> srg(9,4,1,2)  PASS
    bvls_graph()                 -> srg(243,22,1,2) PASS, 2673 edges

  NEGATIVES that pass shape+degree but fail ONLY the common-neighbour
  (lambda/mu) counting path -- the gap this run closes:
    C9(1,2) circulant, conn {1,2} on 9 vertices, 4-regular, NOT rook(3)
        -> FAIL (9,4,1,2) citing LAMBDA or MU, not shape/degree
    circulant(99,{1..7}) 14-regular on 99 vertices
        -> FAIL (99,14,1,2) citing a count mismatch, not degree/shape

  NEGATIVES that fail on a cheaper guard (shape or degree):
    Petersen graph              -> FAIL (9,4,1,2) on degree (not 4-regular)
    edge-moved rook(3)          -> FAIL (9,4,1,2) (still 4-regular, wrong counts)
    rook(4)                     -> FAIL (9,4,1,2) on shape (16x16)
"""
import numpy as np
from lib.srg import (
    is_srg, rook, bvls_graph, circulant, random_regular_14_99,
)


def petersen():
    """Petersen graph, 3-regular on 10 vertices. Not srg(9,4,1,2) on shape+degree."""
    edges = [(0,1),(0,4),(0,5),(1,2),(1,6),(2,3),(2,7),(3,4),(3,8),(4,9),
             (5,7),(5,8),(6,8),(6,9),(7,9)]
    n = 10
    A = np.zeros((n, n), dtype=np.int64)
    for u, v in edges:
        A[u, v] = A[v, u] = 1
    return A


def edge_moved_rook():
    """rook(3) through a 2-edge switch that preserves 4-regularity.

    rook(3) cells: 0=(0,0) 1=(0,1) 2=(0,2) 3=(1,0) 4=(1,1) 5=(1,2)
                   6=(2,0) 7=(2,1) 8=(2,2); adjacent iff same row or col.
    Take the 4-cycle 0-1-4-3-0. Remove edges {0,1} and {3,4}; add edges
    {1,3} and {0,4}. Every vertex keeps degree 4 (asserted in main), but the
    graph is no longer the rook's graph, so it must fail the count path.
    """
    A = rook(3).copy()
    A[0, 1] = A[1, 0] = 0
    A[3, 4] = A[4, 3] = 0
    A[1, 3] = A[3, 1] = 1
    A[0, 4] = A[4, 0] = 1
    return A


def main():
    lines = []
    def emit(s):
        print(s)
        lines.append(s)

    emit("CAPTURE: what ran  : code/out/oracle_controls.py (this file)")
    emit("CAPTURE: oracle    : lib.srg.is_srg -- exact integer common-neighbour counts")
    emit("CAPTURE: inputs    : rook(3)/(9,4,1,2); bvls_graph()/(243,22,1,2);")
    emit("                        C9(1,2)=circulant(9,{1,2})/(9,4,1,2);")
    emit("                        circulant(99,{1..7})/(99,14,1,2);")
    emit("                        petersen()/(9,4,1,2); edge_moved_rook()/(9,4,1,2);")
    emit("                        rook(4)/(9,4,1,2)")
    emit("=" * 78)

    emit("[POSITIVE] rook(3)  -> srg(9,4,1,2)")
    ok, why = is_srg(rook(3), 9, 4, 1, 2)
    emit("   result: %s -- %s" % ("PASS" if ok else "FAIL", why))
    assert ok

    emit("[POSITIVE] bvls_graph() -> srg(243,22,1,2)")
    B = bvls_graph()
    edges = int(B.sum() // 2)
    emit("   shape=%s edges=%d" % (B.shape, edges))
    ok, why = is_srg(B, 243, 22, 1, 2)
    emit("   result: %s -- %s" % ("PASS" if ok else "FAIL", why))
    assert ok

    emit("[NEG, count-path] C9(1,2)=circulant(9,{1,2}) -> srg(9,4,1,2)")
    C9 = circulant(9, [1, 2])
    emit("   shape=%s degrees(all)=%s" % (C9.shape, set(C9.sum(axis=1).tolist())))
    ok, why = is_srg(C9, 9, 4, 1, 2)
    emit("   result: %s -- %s" % ("FAIL" if not ok else "PASS(unexpected)", why))
    assert not ok
    assert ("LAMBDA" in why or "MU" in why), "rejection must cite a count mismatch"
    assert "degree" not in why and "shape" not in why, "must not fail on a cheaper guard"

    emit("[NEG, count-path] circulant(99,{1..7}) -> srg(99,14,1,2)")
    R = circulant(99, list(range(1, 8)))
    emit("   shape=%s degrees(all)=%s" % (R.shape, set(R.sum(axis=1).tolist())))
    ok, why = is_srg(R, 99, 14, 1, 2)
    emit("   result: %s -- %s" % ("FAIL" if not ok else "PASS(unexpected)", why))
    assert not ok
    assert ("LAMBDA" in why or "MU" in why), "rejection must cite a count mismatch"
    assert "degree" not in why and "shape" not in why, "must not fail on a cheaper guard"

    emit("[NEG, degree-guard] petersen() -> srg(9,4,1,2)")
    P = petersen()
    ok, why = is_srg(P, 9, 4, 1, 2)
    emit("   result: %s -- %s" % ("FAIL" if not ok else "PASS(unexpected)", why))
    assert not ok

    emit("[NEG, count-path/edge-moved] edge_moved_rook() -> srg(9,4,1,2)")
    M = edge_moved_rook()
    emit("   degrees(all)=%s" % (set(M.sum(axis=1).tolist()),))
    assert set(M.sum(axis=1).tolist()) == {4}, "edge-moved rook must stay 4-regular"
    ok, why = is_srg(M, 9, 4, 1, 2)
    emit("   result: %s -- %s" % ("FAIL" if not ok else "PASS(unexpected)", why))
    assert not ok
    assert ("LAMBDA" in why or "MU" in why), "edge-moved rook must fail on the count path"

    emit("[NEG, shape-guard] rook(4) -> srg(9,4,1,2)")
    ok, why = is_srg(rook(4), 9, 4, 1, 2)
    emit("   result: %s -- %s" % ("FAIL" if not ok else "PASS(unexpected)", why))
    assert not ok

    emit("=" * 78)
    emit("ALL ORACLE CONTROLS PASSED (expected PASS/FAIL exactly as annotated).")
    with open("code/out/oracle-controls.captured.txt", "w") as f:
        f.write("\n".join(lines) + "\n")
    print("WROTE code/out/oracle-controls.captured.txt")


if __name__ == "__main__":
    main()
