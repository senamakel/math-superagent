#!/usr/bin/env python3
"""Q2 of coclique-lift via OR-Tools CP-SAT: does a CLEAN 2-(22,4,2) design exist?

Clean := 77 blocks (4-subsets of {0..21}), every point in exactly 14 blocks,
every pair in exactly 2 blocks, and NO two blocks share a triple (equivalently
the 308 covered triples are all distinct).  This is the mu=2 lift necessary
condition for a tight 22-coclique in a putative srg(99,14,1,2).

Encoding:
  x_B in {0,1} for each of 7315 4-subsets.
    sum_{B ∋ i} x_B = 14               (each point in 14 blocks)
    sum_{B ∋ {i,j}} x_B = 2            (each pair in 2 blocks)
  Clean: for every triple T, sum_{B ⊇ T} x_B <= 1.
  Symmetry break: fix block {0,1,2,3} (x = 1); WLOG by relabeling.

CP-SAT provably finds a solution or proves infeasibility; over 10**9-valued
exact integer domain it is exact.  If a solution is found it is verified
independently by direct counting (a second route).  Honest boundary: if the
search is abandoned at a wall clock with unknown status, record machine counts.
"""
import itertools, time, sys
from collections import Counter
from ortools.sat.python import cp_model

V, K, B_T, R, LAM = 22, 4, 77, 14, 2
ALL_BLOCKS = list(itertools.combinations(range(V), K))
BLOCK_IDX = {frozenset(B): i for i, B in enumerate(ALL_BLOCKS)}

def main(budget):
    t0 = time.time()
    model = cp_model.CpModel()
    x = [model.NewBoolVar(f"x{i}") for i in range(len(ALL_BLOCKS))]

    # fixed block {0,1,2,3}
    fx = BLOCK_IDX[frozenset((0,1,2,3))]
    model.Add(x[fx] == 1)

    # point rows
    for i in range(V):
        idxs = [BLOCK_IDX[frozenset(B)] for B in ALL_BLOCKS if i in B]
        model.Add(sum(x[j] for j in idxs) == R)
    # pair rows
    for (i, j) in itertools.combinations(range(V), 2):
        idxs = [BLOCK_IDX[frozenset(B)] for B in ALL_BLOCKS if (i in B and j in B)]
        model.Add(sum(x[j] for j in idxs) == LAM)
    # clean: triple in at most one block
    for (p,q,r) in itertools.combinations(range(V), 3):
        idxs = [BLOCK_IDX[frozenset(B)] for B in ALL_BLOCKS
                if (p in B and q in B and r in B)]
        model.Add(sum(x[j] for j in idxs) <= 1)

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = budget
    status = solver.Solve(model)
    dt = time.time() - t0
    print(f"what ran: code/out/coclique_lift_cpsat.py (OR-Tools CP-SAT, exact integer)")
    print(f"oracle function: CP-SAT feasibility; ring Z")
    print(f"model: 2-(22,4,2) clean design; {len(ALL_BLOCKS)} bools, 22 point rows, "
          f"231 pair rows, 1540 triple<=1 rows, symmetry break {list((0,1,2,3))}")
    print(f"wall clock: {dt:.2f}s")
    print(f"CP-SAT status: {solver.StatusName(status)} "
          f"(branches={solver.NumBranches()}, conflicts={solver.NumConflicts()})")
    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        blocks = [ALL_BLOCKS[j] for j in range(len(x)) if solver.Value(x[j]) == 1]
        # independent exact verification by direct counting
        deg = Counter(); pairs = Counter(); trips = Counter()
        for B in blocks:
            for a in B: deg[a]+=1
            for p in itertools.combinations(B,2): pairs[p]+=1
            for t in itertools.combinations(B,3): trips[t]+=1
        ok = (len(blocks)==77 and set(deg.values())=={14}
              and len(pairs)==231 and set(pairs.values())=={2})
        okc = (len(trips)==308 and set(trips.values())=={1})
        print(f"blocks found: {len(blocks)}")
        print(f"independent verify: deg14={set(deg.values())}, "
              f"pairs2={set(pairs.values())}({len(pairs)} pairs), clean "
              f"(max triple overlap)={max(trips.values()) if trips else 0}")
        print(f"  -> 2-(22,4,2): {ok}, clean: {okc}")
        if ok and okc:
            with open("coclique_lift_clean_design.txt","w") as f:
                for B in blocks: f.write(" ".join(map(str,B))+"\n")
            print("CLEAN DESIGN FOUND -> code/out/coclique_lift_clean_design.txt")
            print("Q2 EXISTENCE (clean): YES -- constructive certificate, "
                  "verified by independent counting")
        else:
            print("Q2: found a design but not clean (should not happen if clean "
                  "constraints active; check constraints)")
    elif status == cp_model.INFEASIBLE:
        print("Q2 EXISTENCE (clean): NO -- CP-SAT proved infeasibility")
        print("=> no clean 2-(22,4,2) design exists; no tight 22-coclique lift "
              "satisfying mu=2 is possible at (99,14,1,2)")
    else:
        print(f"Q2: INCONCLUSIVE -- budget {budget}s exhausted, status "
              f"{solver.StatusName(status)}.  Honest boundary recorded.")

if __name__ == "__main__":
    budget = float(sys.argv[1]) if len(sys.argv) > 1 else 400.0
    main(budget)
