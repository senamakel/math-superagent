#!/usr/bin/env python3
"""Constructive search for a CLEAN 2-(22,4,2) design (Q2).

Clean := no two blocks share >= 3 vertices. Equivalently the 77 blocks cover
their 77*4 = 308 triples all distinct.

This is a bounded finite existence question (22 points, 77 blocks). We use a
randomized greedy backtracking search over candidate 4-subsets, with
exact-integer verification of both the 2-(22,4,2) parameter identities and the
clean (no-repeated-triple) condition. If it returns a design, that design is a
constructive certificate and the line's Q2 is settled YES.

Exact facts used: b=77, r=14, lambda=2, and lambda_3 = 308/1540 (so only 308 of
the 1540 triples are covered by blocks at all; cleanliness forbids any of those
308 from being covered twice).
"""
import random, itertools, sys
from collections import Counter

def build(points_v, k, b_target, r_target, lam_target,
          rng, max_restarts, max_steps):
    """Greedy backtracking to fill block list with clean 2-design."""
    pairs_need = Counter()          # pair -> remaining cover count
    for (a, b) in itertools.combinations(range(points_v), 2):
        pairs_need[(a, b)] = lam_target
    deg = [0]*points_v              # point replication remaining
    for i in range(points_v):
        deg[i] = r_target
    blocks = []
    covered_triples = set()

    def pair_ok(B):
        # B must not exceed any remaining pair cover or replica and not repeat a
        # covered triple
        for a in B:
            if deg[a] <= 0:
                return False
        for p in itertools.combinations(B, 2):
            if pairs_need[p] <= 0:
                return False
        for t in itertools.combinations(B, 3):
            if t in covered_triples:
                return False
        return True

    for step in range(max_steps):
        # choose among candidate blocks: those underlying still-needed pairs
        # deterministic-ish: score by how many needed pairs they cover, with
        # randomness
        cands = []
        P = [p for p, c in pairs_need.items() if c > 0]
        if not P:
            # all pairs satisfied -> done if block count right and degrees
            if len(blocks) == b_target and all(d == 0 for d in deg):
                return blocks
            return None
        # try to construct a block from random needed pairs
        base = set()
        rp = rng.choice(P)
        base.update(rp)
        # extend greedily keeping pair_ok
        # candidate extension points
        attempt = set(base)
        for _ in range(10):
            # try adding a random point that keeps clean & feasible
            opts = [x for x in range(points_v) if x not in attempt]
            rng.shuffle(opts)
            cand_ok = None
            for x in opts:
                trial = tuple(sorted(attempt | {x}))
                tt = tuple(sorted(attempt | {x}))
                # check pair feasibility incrementally
                ok = True
                for p in itertools.combinations(trial, 2):
                    if pairs_need.get(p, 0) <= 0:
                        ok = False; break
                if ok:
                    for t in itertools.combinations(trial, 3):
                        if t in covered_triples:
                            ok = False; break
                if ok:
                    if len(attempt) + 1 == k:
                        cand_ok = trial
                        break
                    else:
                        attempt.add(x)
                        cand_ok = "mid"
                        break
            if cand_ok == "mid":
                continue
            if len(attempt) == k:
                break
        if len(attempt) != k:
            # stuck, restart
            return None
        B = tuple(sorted(attempt))
        # commit
        for a in B:
            deg[a] -= 1
        for p in itertools.combinations(B, 2):
            pairs_need[p] -= 1
        for t in itertools.combinations(B, 3):
            covered_triples.add(t)
        blocks.append(B)
        if len(blocks) > b_target:
            return None
    return None if len(blocks) != b_target else blocks

def verify(blocks, v, k, r, lam, clean):
    n = len(blocks)
    deg = [0]*v
    pairs = Counter()
    trips = Counter()
    for B in blocks:
        for a in B: deg[a]+=1
        for p in itertools.combinations(B,2): pairs[p]+=1
        for t in itertools.combinations(B,3): trips[t]+=1
    ok_deg = set(deg) == {r}
    ok_pairs = len(pairs) == v*(v-1)//2 and set(pairs.values()) == {lam}
    ok_clean = (len(trips) == n*4) and (set(trips.values()) == {1})
    return n==77, ok_deg, ok_pairs, ok_clean, trips, deg

def main():
    v, k, b, r, lam = 22, 4, 77, 14, 2
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    rng = random.Random(seed)
    t0 = __import__('time').time()
    best_trips_overlap = None
    found = None
    for attempt in range(4000):
        bl = build(v, k, b, r, lam, rng, 1, 2000)
        if bl is not None:
            okb, okd, okp, okc, trips, deg = verify(bl, v, k, r, lam, True)
            if okb and okd and okp and okc:
                found = bl
                print(f"attempt {attempt}: CLEAN 2-(22,4,2) FOUND and verified")
                break
            else:
                # count triple overlaps
                m = max(trips.values()) if trips else 0
                if best_trips_overlap is None or m < best_trips_overlap:
                    best_trips_overlap = m
        if attempt % 200 == 0:
            print(f"  attempt {attempt}, best max-triple-overlap so far: "
                  f"{best_trips_overlap}", flush=True)
    dt = __import__('time').time()-t0
    print(f"wall clock: {dt:.2f}s")
    if found:
        with open("coclique_lift_clean_design.txt","w") as f:
            for B in found: f.write(" ".join(map(str,B)) + "\n")
        print("clean design written to code/out/coclique_lift_clean_design.txt")
        print("Q2 EXISTENCE (clean): YES - constructive certificate, verified exactly")
    else:
        print("no clean design found in 4000 attempts.  Q2: inconclusive by "
              "construction (not a proof of nonexistence)")

if __name__ == "__main__":
    main()
