#!/usr/bin/env python3
"""Exact backtracking search for a CLEAN 2-(22,4,2) design (Q2 of coclique-lift).

Clean := 77 blocks, each a 4-subset of {0..21}, every point in 14 blocks,
every pair in exactly 2 blocks, and NO triple in more than one block
(equivalently the 308 covered triples are all distinct) -- the mu=2 lift
condition at (99,14,1,2).

This is exact-integer complete enumeration with pruning.  Space is the set of
4-subsets of a 22-set with pair/triple/pruning.  We record the honest boundary
if it does not terminate: attempted nodes, blocks placed, wall clock, depth.

First phase sanity: run the SAME backtracking WITHOUT the clean (triple)
constraint and confirm it finds a plain 2-(22,4,2) (we already have one from
the MILP) -- that proves the backtracking itself works.  Then run with the
clean constraint to seek a clean design.
"""
import itertools, time, sys
from collections import Counter

V, K, B_T, R, LAM = 22, 4, 77, 14, 2

ALL_BLOCKS = list(itertools.combinations(range(V), K))

def solve(clean, time_budget, seed_cap=None):
    t0 = time.time()
    # pair -> remaining cover
    rem = {p: LAM for p in itertools.combinations(range(V), 2)}
    deg = [R]*V
    used_triples = set()
    blocks = []

    # precompute for each block which pairs/triples it uses
    bpairs = {(i, B): B for i, B in enumerate(ALL_BLOCKS)}  # not needed
    pair_usage = {B: tuple(itertools.combinations(B, 2)) for B in ALL_BLOCKS}
    trip_usage = {B: tuple(itertools.combinations(B, 3)) for B in ALL_BLOCKS}

    nodes = 0
    max_depth = 0

    def feasible(B):
        for p in pair_usage[B]:
            if rem[p] <= 0:
                return False
        for a in B:
            if deg[a] <= 0:
                return False
        return True

    def try_place(depth):
        nonlocal nodes, max_depth
        nodes += 1
        if depth > max_depth:
            max_depth = depth
        if time.time() - t0 > time_budget:
            return "timeout"
        if len(blocks) == B_T:
            # all pairs must be exhausted
            if all(c == 0 for c in rem.values()) and all(d == 0 for d in deg):
                return "done"
            return "fail"
        # pick candidate blocks: sort by fewest remaining (most constrained)
        cands = [B for B in ALL_BLOCKS if feasible(B)]
        # order candidates by how many still-needed pairs they have (fewer
        # needed-coverings => higher priority), break ties by block
        cands_pairs = []
        for B in cands:
            need = sum(1 for p in pair_usage[B] if rem[p] > 0)
            cands_pairs.append((need, B))
        cands_pairs.sort(key=lambda x: (x[0], -x[1]))
        for _, B in cands_pairs:
            # apply
            for p in pair_usage[B]:
                rem[p] -= 1
            for a in B:
                deg[a] -= 1
            trips = trip_usage[B]
            if clean:
                if any(t in used_triples for t in trips):
                    for p in pair_usage[B]:
                        rem[p] += 1
                    for a in B:
                        deg[a] += 1
                    continue
                for t in trips:
                    used_triples.add(t)
            blocks.append(B)
            r = try_place(depth + 1)
            if r == "done":
                return "done"
            if r == "timeout":
                return "timeout"
            # undo
            blocks.pop()
            for p in pair_usage[B]:
                rem[p] += 1
            for a in B:
                deg[a] += 1
            if clean:
                for t in trips:
                    used_triples.discard(t)
        return "fail"

    r = try_place(0)
    dt = time.time() - t0
    print(f"  clean={clean}  result={r}  wall={dt:.2f}s  nodes={nodes} "
          f"max_depth={max_depth} blocks_found={len(blocks)}")
    return r, blocks

def verify(blocks, clean):
    deg = [0]*V
    pairs = Counter()
    trips = Counter()
    for B in blocks:
        for a in B: deg[a]+=1
        for p in itertools.combinations(B,2): pairs[p]+=1
        for t in itertools.combinations(B,3): trips[t]+=1
    ok = (len(blocks)==77 and set(deg)=={14}
          and len(pairs)==231 and set(pairs.values())=={2})
    okc = (len(trips)==308 and set(trips.values())=={1}) if clean else True
    max_trip = max(trips.values()) if trips else 0
    return ok, okc, max_trip, len(blocks), sorted(set(deg))

if __name__ == "__main__":
    budget = float(sys.argv[1]) if len(sys.argv) > 1 else 300.0
    print(f"what ran: code/out/coclique_lift_backtrack.py (exact-integer backtracking)")
    print(f"target: 2-(22,4,2) design (b=77,r=14,lambda=2), 4-subsets of 22-set")
    print(f"search space: {len(ALL_BLOCKS)} candidate 4-subsets; pair-exact, "
          f"point-degree-exact, triple-at-most-once (clean) or unconstrained")
    print(f"time budget per phase: {budget}s")
    # sanity: non-clean
    print("\nPhase 1: plain 2-(22,4,2) (sanity that backtracking works)")
    r1, bl1 = solve(clean=False, time_budget=budget)
    if r1 == "done":
        ok, okc, mt, nb, dd = verify(bl1, False)
        print(f"  plain design verify: len==77:{len(bl1)==77} deg14:{dd} "
              f"pairs2:{set(Counter(p for B in bl1 for p in itertools.combinations(B,2)).values())}"
              f" -> {(r1, ok)}")
    print("\nPhase 2: CLEAN 2-(22,4,2) (Q2 lift target)")
    r2, bl2 = solve(clean=True, time_budget=budget)
    if r2 == "done":
        ok, okc, mt, nb, dd = verify(bl2, True)
        print(f"  clean verify: (ok={ok}, okc={okc}, max_triple={mt})")
        if ok and okc:
            with open("coclique_lift_clean_design.txt","w") as f:
                for B in bl2: f.write(" ".join(map(str,B))+"\n")
            print("  CLEAN DESIGN FOUND: code/out/coclique_lift_clean_design.txt")
            print("  Q2: YES (clean 2-(22,4,2) exists, mu=2 lift conditions met)")
        else:
            print("  Q2: partial/failed -- see verify flags")
    else:
        print(f"  Q2: INCONCLUSIVE (budget {budget}s; search is exact but did not "
              f"finish -- honest boundary: wall {budget}s, exact backtracking)")
