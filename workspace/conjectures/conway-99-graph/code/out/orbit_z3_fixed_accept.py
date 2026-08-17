"""DIRECTIVE 29: fixed-feasibility acceptance test for the orbit-matrix encoder.

The FIND model (code/out/orbit_z3_encoder.py) searches for a symmetric orbit
matrix M satisfying the srg-quotient NECESSARY equation

      M^2 = (k-mu) I + (lam-mu) M + mu*3*J        (orbit length n = 3)

with row sums = k, diagonal in {0,2}, entries in 0..3.  That search is OPTIMAL
at rook m=3 but times out at BvLS m=81.  This acceptance test does the DECISIVE
CHEAP check: take a known-good orbit matrix M0, build the identical model, and
ADD constraints FIXING every M_ij == M0_ij (i<=j).  No search remains, so the
solver must report FEASIBLE near-instantly.  A known-good solution REJECTED
proves the encoding is wrong; ACCEPTED proves the constraints are sound even
where search is slow.

Workflow for each of the two controls:
  1. Verify M0 itself satisfies the equation in EXACT integer arithmetic,
     row sums = k, symmetric, diagonal in {0,2}, entries in 0..3 (assert).
  2. Build the model with the fixed constraints, solve with a small
     max_time_in_seconds (60), and report the LITERAL solver status.

Ring: exact integer (numpy int64 + Python int).  No floats.
"""
import sys
import numpy as np
from ortools.sat.python import cp_model
from lib.srg import bvls_graph, orbit_matrix

# ---- reuse the order-3 translation automorphism on BvLS (as validate run) ----
def _prod_idx(s):
    return s[0] * 81 + s[1] * 27 + s[2] * 9 + s[3] * 3 + s[4]

def bvls_z3():
    a = (1, 0, 0, 0, 0)
    g = [0] * 243
    for s0 in range(3):
        for s1 in range(3):
            for s2 in range(3):
                for s3 in range(3):
                    for s4 in range(3):
                        s = (s0, s1, s2, s3, s4)
                        t = tuple((s[k] + a[k]) % 3 for k in range(5))
                        g[_prod_idx(s)] = _prod_idx(t)
    return g


def verify_M0(M0, k, lam, mu, label):
    """Exact-integer verification of the known-good orbit matrix M0 (m x m).

    Checks, raising AssertionError on failure:
      - symmetric
      - diagonal values in {0, 2}  (a 3-vertex orbit)
      - entries in 0..3
      - every row sums to k
      - M0^2 = (k-mu) I + (lam-mu) M0 + mu*3 J, entry by entry (exact)
    Returns a report string.
    """
    M0 = np.asarray(M0, dtype=np.int64)
    m = M0.shape[0]
    assert M0.ndim == 2 and M0.shape[0] == M0.shape[1], "M0 must be square"
    sym = bool(np.all(M0 == M0.T))
    diag = sorted(set(np.diag(M0).tolist()))
    ok_diag = all(d in (0, 2) for d in diag)
    mn, mx = int(M0.min()), int(M0.max())
    ok_entries = (mn >= 0) and (mx <= 3)
    rowsums = M0.sum(axis=1)
    ok_rows = bool(np.all(rowsums == k))
    # exact integer equation check
    C = M0 @ M0
    rhs = (k - mu) * np.eye(m, dtype=np.int64) \
        + (lam - mu) * M0 \
        + mu * 3 * np.ones((m, m), dtype=np.int64)
    diff = C - rhs
    ok_eq = bool(np.all(diff == 0))
    maxdiff = int(np.max(np.abs(diff))) if m else 0

    lines = [
        f"--- verify known-good M0: {label} ---",
        f"  m={m}, k={k}, lam={lam}, mu={mu}",
        f"  symmetric: {sym}",
        f"  diagonal values: {diag}  (must be subset of {{0,2}}): {ok_diag}",
        f"  entry range [{mn},{mx}] within 0..3: {ok_entries}",
        f"  row sums all == k: {ok_rows}",
        f"  M0^2 = (k-mu)I + (lam-mu)M0 + mu*3*J : {ok_eq}  (max |diff|={maxdiff})",
        f"  ALL CHECKS PASS: {sym and ok_diag and ok_entries and ok_rows and ok_eq}",
    ]
    assert sym and ok_diag and ok_entries and ok_rows and ok_eq, \
        f"known-good M0 for {label} FAILED its own verification"
    return "\n".join(lines)


def build_fixed(m, k, lam, mu, M0, maxseconds):
    """Identical model to orbit_z3_encoder.build(), but every M_ij is FIXED to
    M0_ij (i<=j).  Returns solver, status, and the model's g() accessor."""
    model = cp_model.CpModel()
    M = {}
    for i in range(m):
        for j in range(i, m):
            M[(i, j)] = model.NewIntVar(0, 3, f"M{i}_{j}")
    def g(i, j):
        return M[(min(i, j), max(i, j))]
    # FIX the variables to the known-good value
    for i in range(m):
        for j in range(i, m):
            model.Add(M[(i, j)] == int(M0[i, j]))
    # diagonal in {0,2}
    for i in range(m):
        model.AddAllowedAssignments([M[(i, i)]], [(0,), (2,)])
    # row sums = k
    for i in range(m):
        model.Add(sum(M[(i, j)] if i <= j else M[(j, i)] for j in range(m)) == k)
    # M^2 = (k-mu)I + (lam-mu)M + mu*3 J
    off = lam - mu
    c1 = k - mu
    c2 = mu * 3
    for i in range(m):
        for j in range(m):
            prods = []
            for t in range(m):
                p = model.NewIntVar(0, 9, f"p_{i}_{j}_{t}")
                model.AddMultiplicationEquality(p, [g(i, t), g(t, j)])
                prods.append(p)
            sq = model.NewIntVar(0, 9 * m, f"sq_{i}_{j}")
            model.Add(sum(prods) == sq)
            rhs = c1 * (1 if i == j else 0) + off * g(i, j) + c2
            model.Add(sq == rhs)
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = maxseconds
    solver.parameters.num_search_workers = 4
    st = solver.Solve(model)
    return solver, st


def rook_M0():
    """Known-good 3x3 orbit matrix for rook(3)=srg(9,4,1,2), a fixed-point-free
    order-3 automorphism (diagonal 0, all off-diagonal 2)."""
    return np.array([[0, 2, 2], [2, 0, 2], [2, 2, 0]], dtype=np.int64)


def bvls_M0():
    """Recompute BvLS's genuine order-3 orbit matrix (m=81, diagonal all 2)."""
    A = bvls_graph()
    g = bvls_z3()
    orbits, lengths, M = orbit_matrix(A, g)
    assert set(lengths) == {3}, "expected fixed-point-free order-3 action"
    assert len(orbits) == 81
    return np.asarray(M, dtype=np.int64)


def main():
    print("=== DIRECTIVE 29: fixed-feasibility acceptance test for orbit-matrix encoder ===")
    print("NOTE: 99 with a fixed-point-free order-3 automorphism has m = 33 orbits,")
    print("      smaller than BvLS m=81 (which timed out in find mode) and larger than")
    print("      rook m=3 (which solved).  A 33-orbit 99 run is plausibly within reach,")
    print("      but only AFTER both fixed-feasibility checks pass, and kept SMALL.")
    print()

    results = []
    cases = [
        ("rook(3)", 3, 4, 1, 2, rook_M0(), 60),
        ("BvLS", 81, 22, 1, 2, bvls_M0(), 60),
    ]
    for label, m, k, lam, mu, M0, maxsec in cases:
        print(verify_M0(M0, k, lam, mu, label))
        solver, st = build_fixed(m, k, lam, mu, M0, maxsec)
        status = solver.StatusName(st)
        wall = solver.WallTime()
        print(f"  fixed-feasibility solve ({label}, m={m}): status = {status} "
              f"(wall {wall:.2f}s, bound max {maxsec}s)")
        # A known-good matrix must be accepted; anything else is an encoding bug
        if status == "FEASIBLE" or status == "OPTIMAL":
            print(f"  -> ACCEPTED: constraints are sound even where search is slow.  PASS")
            results.append((label, status, True))
        elif status == "INFEASIBLE":
            print(f"  -> REJECTED: known-good matrix found infeasible.  ENCODING IS WRONG.  FAIL")
            results.append((label, status, False))
        else:  # UNKNOWN / MODEL_INVALID / etc
            print(f"  -> INCONCLUSIVE ({status}).  Not a verdict; check timeout.")
            results.append((label, status, None))
        print()

    print("=== SUMMARY ===")
    ok = True
    for label, status, passed in results:
        verdict = {True: "PASS (ACCEPTED)", False: "FAIL (REJECTED)",
                   None: "INCONCLUSIVE"}[passed]
        print(f"  {label}: literal solver status = {status}  ->  {verdict}")
        if passed is not True:
            ok = False
    if ok:
        print("\nBoth fixed-feasibility checks PASSED: the encoding accepts BvLS m=81 and")
        print("rook m=3 known-good orbit matrices.  The find-mode timeout at m=81 is a")
        print("SEARCH-cost issue, not an encoding error.  A 99 run (m=33 orbits, smaller")
        print("than 81) is now WARRANTED as a next step.")
    else:
        print("\nAt least one check did not pass cleanly: investigate before any 99 run.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
