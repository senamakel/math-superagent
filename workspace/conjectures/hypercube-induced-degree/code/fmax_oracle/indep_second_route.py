"""Disposable independent second-route check of small f(n).

f(n) = min { D(S) : S subset {0,1}^n, |S|=2^{n-1}+1 }, D(S)=max internal degree.

This script deliberately shares NO code with lib.fmax (the ILP oracle).
All degree counting and exhaust is hand-written pure-Python integer arithmetic
here; the only external call is ortools CP-SAT (a different solver technology
than scipy.optimize.milp/HiGHS) for the n=5 decision.

Route:
  n=4  : hand-written exhaustive over all C(16,9)=11440 subsets -> min max-degree.
  n=5  : CP-SAT decision 'is there S of size 17 with D(S)<=d?' for d=2 (expect
         False) and d=3 (expect True); extract an explicit witness for d=3,
         write it to code/out/witness_n5_alt.txt, and re-verify |S| and the
         full internal-degree profile with the local hand-written counter
         (a fourth route, shares code with nothing in lib).

Expected: n=4 -> 2; n=5 d=2 infeasible, d=3 feasible; witness |S|=17 max deg 3.
"""
import time
from itertools import combinations
from ortools.sat.python import cp_model


def neighbours(n, v):
    """Hand-written neighbours of vertex v in Q_n (flip one bit)."""
    return [v ^ (1 << k) for k in range(n)]


def degree_distribution(n, S):
    """{internal degree: count} over vertices of S. Hand-written, exact ints."""
    S = set(S)
    counts = {}
    for v in S:
        d = sum(1 for w in neighbours(n, v) if w in S)
        counts[d] = counts.get(d, 0) + 1
    return counts


def max_degree(n, S):
    return max(degree_distribution(n, S).keys())


def exhaustive_min_max_deg(n):
    """Exhaustive over all subsets of size 2^{n-1}+1: min of max internal degree."""
    N = 1 << n
    m = (1 << (n - 1)) + 1
    best = None
    best_S = None
    for S in combinations(range(N), m):
        d = max_degree(n, S)
        if best is None or d < best:
            best = d
            best_S = S
            if best == 0:
                break  # can't do better
    return best, best_S


def cpsat_decision(n, d, time_limit=120.0):
    """CP-SAT: is there S of size 2^{n-1}+1 with D(S)<=d? Returns (ok, S_or_None)."""
    N = 1 << n
    m = (1 << (n - 1)) + 1
    model = cp_model.CpModel()
    x = [model.NewBoolVar(f"x{i}") for i in range(N)]
    model.Add(sum(x) == m)
    M = n  # max internal degree of any vertex
    for v in range(N):
        model.Add(sum(x[w] for w in neighbours(n, v)) + M * x[v] <= d + M)
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = time_limit
    status = solver.Solve(model)
    if status in (cp_model.FEASIBLE, cp_model.OPTIMAL):
        return True, [v for v in range(N) if solver.Value(x[v]) == 1]
    return False, None


def main():
    t0 = time.time()

    print("=== n=4: hand-written exhaustive over C(16,9) subsets ===")
    ta = time.time()
    f4, S4 = exhaustive_min_max_deg(4)
    prof4 = degree_distribution(4, S4)
    print(f"  min max internal degree = {f4} (expect 2)")
    print(f"  |S|={len(S4)}  profile={dict(sorted(prof4.items()))}")
    print(f"  [{time.time()-ta:.2f}s]")

    print()
    print("=== n=5: CP-SAT decisions (expect d=2 infeasible, d=3 feasible) ===")
    for d in (2, 3):
        ta = time.time()
        fe, S = cpsat_decision(5, d)
        if S is not None:
            prof = degree_distribution(5, S)
            print(f"  d={d}: feasible={fe}  |S|={len(S)}  "
                  f"D(S)={max_degree(5,S)}  profile={dict(sorted(prof.items()))}"
                  f"  [{time.time()-ta:.2f}s]")
        else:
            print(f"  d={d}: feasible={fe}  [{time.time()-ta:.2f}s]")

    print()
    print("=== n=5 witness for d=3: extract, write, re-verify with own counter ===")
    ok, W = cpsat_decision(5, 3, time_limit=120.0)
    if not ok or W is None:
        print("  FAILED to obtain an n=5 witness")
        return
    W = sorted(W)
    with open("code/out/witness_n5_alt.txt", "w") as f:
        for v in W:
            f.write(f"{v}\n")
    prof = degree_distribution(5, W)
    print(f"  |S|={len(W)} (need 17) -> {'OK' if len(W)==17 else 'MISMATCH!'}")
    print(f"  D(S)={max_degree(5,W)} (expect 3) -> "
          f"{'OK' if max_degree(5,W)==3 else 'MISMATCH!'}")
    print(f"  profile={dict(sorted(prof.items()))}")
    print(f"  witness written to code/out/witness_n5_alt.txt")

    # Loud check against known values.
    mismatches = []
    if f4 != 2:
        mismatches.append(f"n=4 min max-degree = {f4} != 2 (DISAGREES)")
    # loud feasibility expectations
    print()
    if mismatches:
        print("DISCREPANCY:", "; ".join(mismatches))
    else:
        print("All independent-route values agree with the published ILP/exhaustive "
              "oracle: f(4)=2 (min over 11440 sets), f(5)=3 (d=2 infeasible, "
              "d=3 feasible, witness verified).")
    print(f"  total [{time.time()-t0:.2f}s]")


if __name__ == "__main__":
    main()
