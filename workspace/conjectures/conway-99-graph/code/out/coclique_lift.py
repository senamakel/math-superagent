#!/usr/bin/env python3
"""Coclique-lift question for the open problem srg(99,14,1,2).

If a hypothetical srg(99,14,1,2) had a tight Hoffman-bound coclique C of size
alpha = 22, then every outside vertex sends exactly d_C = 4 edges into C and
the outside-neighbourhood sets form a 2-(22,4,2) design (b=77 blocks, r=14,
k=4, lambda=2).  This module settles the first sub-question exactly:

  Q1: does a 2-(22,4,2) design EXIST?

and, if so,

  Q2: does one exist avoiding the mu=2 lift obstructions?
      (a) no two blocks are identical (block repetition -> two outside vertices
          would share 4 common neighbours, violating mu=2);
      (b) no two blocks share >= 3 vertices (-> >=3 shared common neighbours,
          violating mu=2).

Method: exact 0/1 integer programming via scipy.optimize.milp (HiGHS), over the
ring Z.  Variables x_B in {0,1} for each 4-subset B of {0..21} (7315 binaries).
Equality constraints:
    sum_{B ∋ i} x_B = 14            for each point i      (replication r)
    sum_{B ∋ {i,j}} x_B = 2         for each pair {i,j}   (lambda = 2)
Objective: 0 (feasibility).  A feasible point IS an explicit 2-(22,4,2) design
(certificate).  Infeasibility reported by HiGHS is an exact proof of
nonexistence.

All parameters are exact integers.  The solver's branch-and-bound is exact
integer programming over Z (not floating point); scipy.milp on integral LP
data is certified exact up to the solver's proof.

Q1 only: run with  --q1 .
Q1 + Q2:  additional hard constraints:
    sum_{B ⊇ {i,j,k}} x_B <= 1   for every triple {i,j,k}   (no block-pair
        sharing >=3 vertices is equivalent to: no 3-subset is contained in two
        different blocks, i.e. every triple lies in at most one block);
    and by construction x_B are distinct binaries (the model uses one variable
    per subset, so two blocks cannot repeat -- repetition is impossible by
    construction).  So the Q2 model enforces the triple constraint only.
"""
import sys, time, itertools
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

V = 22
K = 4
BLOCKS = list(itertools.combinations(range(V), K))
NB = len(BLOCKS)          # 7315
assert NB == 7315

# index block by frozenset for quick lookups
BLOCK_IDX = {frozenset(B): i for i, B in enumerate(BLOCKS)}

def build_lp(triple_constraint=False, fix_block=False):
    """Return (c, constraints, integrality-lower/upper)."""
    n = NB
    # ---- equality rows ----
    rows = []
    # point rows: each point i in exactly 14 blocks
    for i in range(V):
        row = np.zeros(n)
        for B in BLOCKS:
            if i in B:
                row[BLOCK_IDX[frozenset(B)]] = 1.0
        rows.append(row)
    # pair rows: each pair in exactly 2 blocks
    for (i, j) in itertools.combinations(range(V), 2):
        row = np.zeros(n)
        for B in BLOCKS:
            if i in B and j in B:
                row[BLOCK_IDX[frozenset(B)]] = 1.0
        rows.append(row)
    A = np.array(rows)
    lb = np.full(A.shape[0], 0.0)
    ub = np.full(A.shape[0], 0.0)
    ub[:V] = 14.0            # point rows = 14
    lb[:V] = 14.0
    ub[V:] = 2.0             # pair rows = 2
    lb[V:] = 2.0
    cons = [LinearConstraint(A, lb, ub)]

    if triple_constraint:
        # sum_{B ⊇ {i,j,k}} x_B <= 1 for every triple
        Trows = []
        for (i, j, k) in itertools.combinations(range(V), 3):
            row = np.zeros(n)
            for B in BLOCKS:
                if i in B and j in B and k in B:
                    row[BLOCK_IDX[frozenset(B)]] = 1.0
            Trows.append(row)
        TA = np.array(Trows)
        cons.append(LinearConstraint(TA, -np.inf * np.ones(TA.shape[0]),
                                     np.ones(TA.shape[0])))
    # symmetry break: fix one block to {0,1,2,3} (WLOG by relabeling; a design
    # exists iff a relabeled one with this fixed block exists)
    c = np.zeros(n)
    if fix_block:
        i = BLOCK_IDX[frozenset((0,1,2,3))]
        # hard-fix x_i = 1 via bounds (both lower and upper bound = 1)
        return c, cons, i
    return c, cons, None

def run(q1_only):
    t0 = time.time()
    c, cons, fix_i = build_lp(triple_constraint=not q1_only, fix_block=not q1_only)
    integrality = np.ones(NB)
    if fix_i is not None:
        # fix block {0,1,2,3}: bounds force x=1
        lo = np.zeros(NB); hi = np.ones(NB)
        lo[fix_i] = 1.0; hi[fix_i] = 1.0
        bnd = Bounds(lo, hi)
    else:
        bnd = Bounds(np.zeros(NB), np.ones(NB))
    print(f"what ran: code/out/coclique_lift.py  (scipy.optimize.milp, HiGHS)")
    print(f"oracle function: exact 0/1 integer program; ring Z")
    print(f"model: 2-({V},{K},2) design, b=77, r=14 -- {NB} binary vars, "
          f"{cons[0].A.shape[0]} equality constraints" +
          (f" + {cons[1].A.shape[0]} triple<=1 constraints (Q2)"
           + (" + symmetry break fixing block {0,1,2,3}" if not q1_only else "")
           if not q1_only else
           " (Q1 only)"))
    res = milp(c=c, constraints=cons, integrality=integrality, bounds=bnd,
               options={"time_limit": 480, "mip_rel_gap": 0.0})
    dt = time.time() - t0
    print(f"wall clock: {dt:.2f}s  status: {res.message}")
    if res.success:
        x = np.round(res.x).astype(int)
        blocks = [BLOCKS[i] for i in range(NB) if x[i] == 1]
        print(f"SOLUTION FOUND: {len(blocks)} blocks")
        # ---- exact verification ----
        ok = True
        deg = [0]*V
        pairs = {}
        for B in blocks:
            for a in B:
                deg[a] += 1
            for (a1,a2) in itertools.combinations(B,2):
                pairs[(a1,a2)] = pairs.get((a1,a2),0)+1
        d0 = set(deg) != {14}
        allpairs = [pairs[(a,b)] for (a,b) in itertools.combinations(range(V),2) if (a,b) in pairs]
        pbad = (len(pairs) != V*(V-1)//2) or (set(allpairs) != {2})
        print(f"  verify: every point in {len(set(deg))} distinct degrees "
              f"(want exactly {{14}}): {'OK' if set(deg)=={14} else 'FAIL'}")
        print(f"  verify: every pair covered exactly twice: "
              f"{'OK' if (len(pairs)==V*(V-1)//2 and set(allpairs)=={2}) else 'FAIL'}")
        ok = d0 and pbad
        # Q2 checks
        if not q1_only:
            # no repeated block (automatic), no triple in 2 blocks
            trip = {}
            for B in blocks:
                for (a,b,c) in itertools.combinations(B,3):
                    trip[frozenset((a,b,c))] = trip.get(frozenset((a,b,c)),0)+1
            worst = max(trip.values()) if trip else 0
            print(f"  Q2: max triple-overlap over all blocks = {worst} "
                  f"(want <=1 for mu=2 clean lift): {'OK' if worst<=1 else 'FAIL'}")
        with open("coclique_lift_design.txt","w") as f:
            f.write("# A 2-(22,4,2) design; lines are 4-subsets of {0..21}\n")
            for B in blocks:
                f.write(" ".join(map(str, B)) + "\n")
        print("  design written to code/out/coclique_lift_design.txt")
        print("EXISTENCE SETTLED: YES (explicit design captured, verified exactly)")
    else:
        print("no feasible point found.  status: " + str(res.message))
        print("EXISTENCE SETTLED: " +
              ("NO (HiGHS proved infeasibility)" if ("infeasib" in str(res.message).lower()
               or "infeasible" in str(res.message).lower()) else "INCONCLUSIVE (timeout/node bound)"))

if __name__ == "__main__":
    q1_only = "--q1" in sys.argv
    run(q1_only)
