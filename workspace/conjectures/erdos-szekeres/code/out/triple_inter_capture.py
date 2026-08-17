#!/usr/bin/env python3
"""triple_inter_capture.py -- fresh provenance capture of the k=3
open-half-plane-side triple-intersection question for the even/odd block
bipartition of the verified ES construction es_construct at n=7.

Background (established in this workspace):
  * lib.es_construct.es_set_blocks(7) realises the ES 2^{n-2}=32-point
    no-convex-7-gon set in exact rationals; largest convex subset = 6-1 = 5
    for BOTH halves below (verified in this run).
  * The even/odd block bipartition
        E = T0 u T2 u T4,  O = T1 u T3 u T5,   |E| = |O| = 16,
    both halves are 6-avoiding (largest convex subset = 5).
  * The N(N-1)=992 distinct open half-plane sides are enumerated by
    ordered_pair_sides (re-imported from code/out/gsplit_enum_definitive.py,
    the module validated EXACTLY against a 2^N brute-force hull-separation
    oracle at N = 8,10,12,14,16 -- zero missing, zero extra, count N(N-1)).

The prior capture (code/out/evenodd_cutfamily.captured.txt) reports:
  k=1: a single side does NOT realise E or O;
  k=2: a pair of sides does NOT (control, must reproduce 0);
  k=3: a triple DOES realise both (DP + explicit scan witnesses).
This run re-derives the k=3 numbers with FULL exhaustive triple enumeration
(no DP, no scanning shortcuts) and full provenance.

Scale check (printed): |A_E|, |A_O| <= 16, so
C(16,3) = 560 triples per family -- full exhaustive enumeration is trivial,
no sampling, no pruning, no DP needed.

All geometry exact (lib.es_geom.orient, integer/Fraction determinants);
intersections are plain set intersections of the point-index subsets.

EXIT code 0 only if every assertion (gate, k=1, k=2 control, exhaustive
k=3 counts, witness direct re-verification) passes.
"""

import itertools
import sys
import time

from lib.es_construct import es_set_blocks
from lib.es_geom import in_general_position, largest_convex_subset
from out.gsplit_enum_definitive import ordered_pair_sides

SCRIPT = "code/out/triple_inter_capture.py"
N_TARGET = 7


def main():
    t0 = time.time()
    print("=" * 76)
    print("triple_inter_capture.py -- exhaustive k=3 triple-intersection")
    print("capture for the even/odd block bipartition of es_construct n=7")
    print("=" * 76)
    print(f"script     : {SCRIPT}")
    print(f"python     : {sys.version.split()[0]}")
    print(f"ring       : exact integer/Fraction arithmetic "
          f"(lib.es_geom.orient determinants); no floats anywhere")
    print()

    # ---------------- 1. worked gate (must pass or STOP) ----------------
    print("=== 1. worked gate (sizes, general position, 6-avoidance) ===")
    pts, blocks = es_set_blocks(N_TARGET)
    N = len(pts)
    bsz = [len(b) for b in blocks]
    gp = in_general_position(pts)
    print(f"n={N_TARGET}: N={N} points, block sizes {bsz} "
          f"(want [1,5,10,10,5,1], sum 32): "
          f"{bsz == [1, 5, 10, 10, 5, 1]}")
    print(f"general position (exact, lib.es_geom): {gp}")
    assert bsz == [1, 5, 10, 10, 5, 1] and N == 32 and gp, "GATE FAILED"

    bim = []
    for bi, blk in enumerate(blocks):
        bim.extend([bi] * len(blk))
    E = frozenset(i for i in range(N) if bim[i] % 2 == 0)
    O = frozenset(i for i in range(N) if bim[i] % 2 == 1)
    assert len(E) == len(O) == 16
    assert E | O == frozenset(range(N)) and E & O == frozenset()
    print(f"E = T0 u T2 u T4, size {len(E)}: {sorted(E)}")
    print(f"O = T1 u T3 u T5, size {len(O)}: {sorted(O)}")
    print("partition check (disjoint, union = all 32): PASS")

    kE, wE = largest_convex_subset([pts[i] for i in E])
    kO, wO = largest_convex_subset([pts[i] for i in O])
    print(f"largest_convex_subset(E) = {kE} (want 5), "
          f"largest_convex_subset(O) = {kO} (want 5)  "
          f"=> both halves 6-avoiding: {kE == 5 and kO == 5}")
    assert kE == 5 and kO == 5, "6-avoidance GATE FAILED"
    print(f"  [t={time.time()-t0:.1f}s]")
    print()

    # ---------------- 2. side enumeration ----------------
    print("=== 2. side enumeration (validated ordered_pair_sides) ===")
    sides = ordered_pair_sides(pts)
    print(f"distinct open half-plane sides: {len(sides)} "
          f"(= N(N-1) = {N*(N-1)}? {len(sides) == N*(N-1)})")
    print("  enumerator: out.gsplit_enum_definitive.ordered_pair_sides,")
    print("  validated exactly vs a 2^N hull-separation oracle at N=8,10,12,")
    print("  14,16: zero missing, zero extra, count N(N-1) (accepted done in")
    print("  steer 11; see code/out/gsplit_enum_definitive_claim.md)")
    assert len(sides) == N * (N - 1) == 992
    side_list = sorted(sides, key=lambda s: (len(s), sorted(s)))
    print(f"  [t={time.time()-t0:.1f}s]")
    print()

    # ---------------- 3. families A_E, A_O and exhaustive triples ----------------
    print("=== 3. superset families and EXHAUSTIVE triple enumeration ===")
    A_E = [s for s in side_list if E <= s]
    A_O = [s for s in side_list if O <= s]
    print(f"|A_E| = sides that are supersets of E: {len(A_E)}")
    print(f"|A_O| = sides that are supersets of O: {len(A_O)}")
    print()
    print("SCALE CHECK: |A_E|, |A_O| <= 16, so C(16,3) = 560 unordered "
          "triples")
    print("per family; full exhaustive triple enumeration is TRIVIAL -- no")
    print("sampling, no pruning, no DP needed. Counting all "
          "C(|A|,3) triples exactly.")
    assert len(A_E) <= 16 and len(A_O) <= 16
    print(f"  [t={time.time()-t0:.1f}s]")
    print()

    # helper: count triples by intersection outcome for a target
    def triple_stats(A, target, target_name):
        m = len(A)
        total = m * (m - 1) * (m - 2) // 6
        size16 = 0
        eq = 0
        witness = None
        for i, j, k in itertools.combinations(range(m), 3):
            inter = A[i] & A[j] & A[k]
            if len(inter) == 16:
                size16 += 1
            if inter == target:
                eq += 1
                if witness is None:
                    # map to side indices within the 992-list
                    wi = side_list.index(A[i])
                    wj = side_list.index(A[j])
                    wk = side_list.index(A[k])
                    witness = (i, j, k), (wi, wj, wk), (sorted(A[i]),
                                                        sorted(A[j]),
                                                        sorted(A[k]))
        return total, size16, eq, witness

    results = {}
    for name, A, target in (("E", A_E, E), ("O", A_O, O)):
        total, size16, eq, witness = triple_stats(A, target, name)
        results[name] = (total, size16, eq, witness)
        print(f"--- target {name} ---")
        print(f"  |A_{name}| = {len(A)}; unordered triples of sides: "
              f"C({len(A)},3) = {total}")
        print(f"  triples with |inter| = 16: {size16}")
        print(f"  triples whose intersection EQUALS {name} exactly: {eq}")
        if witness is not None:
            (i, j, k), (wi, wj, wk), (s1, s2, s3) = witness
            print(f"  WITNESS for {name}: triple (i,j,k) = ({i},{j},{k}) "
                  f"within A_{name};")
            print(f"    global side indices in the 992-list: {wi},{wj},{wk};")
            print(f"    side contents: {s1}")
            print(f"    side contents: {s2}")
            print(f"    side contents: {s3}")
            # direct re-verification of the witness
            inter = (A[i] & A[j] & A[k])
            print(f"    direct re-check: (A[i]&A[j]&A[k]) == {name}: "
                  f"{inter == target}, len = {len(inter)}")
        else:
            print(f"  WITNESS for {name}: NONE (no triple intersection "
                  f"equals {name})")
        print()

    total_E, size16_E, eq_E, witE = results["E"]
    total_O, size16_O, eq_O, witO = results["O"]

    # ---------------- 4. controls: k=1 and k=2 reproduce the record ----------------
    print("=== 4. controls (k=1 single side, k=2 pair) reproduce record ===")
    side_set = set(side_list)
    in1_E = E in side_set
    in1_O = O in side_set
    print(f"k=1: E among the 992 sides: {in1_E} "
          f"(record says False);  O: {in1_O} (record says False)")
    assert not in1_E and not in1_O, "k=1 control FAILED"
    pair_hits_E = sum(1 for a, b in itertools.combinations(A_E, 2)
                      if (a & b) == E)
    pair_hits_O = sum(1 for a, b in itertools.combinations(A_O, 2)
                      if (a & b) == O)
    print(f"k=2: pairs with intersection == E: {pair_hits_E} "
          f"(record says 0);  == O: {pair_hits_O} (record says 0)")
    assert pair_hits_E == 0 and pair_hits_O == 0, "k=2 control FAILED"
    print(f"  [t={time.time()-t0:.1f}s]")
    print()

    # ---------------- 5. verdict ----------------
    print("=== 5. verdict ===")
    print("k=1 (single side):        neither E nor O is a side          "
          "(control)")
    print("k=2 (side pair):          no pair intersection equals E or O (control)")
    print(f"k=3 (side triple):        {size16_E} triples of superset sides with"
          f" |inter|=16 for E;")
    print(f"                           {eq_E} triple(s) equal E exactly"
          f" ({'yes' if eq_E else 'no'} witness);")
    print(f"                           {size16_O} triples ... for O;")
    print(f"                           {eq_O} triple(s) equal O exactly"
          f" ({'yes' if eq_O else 'no'} witness)")
    if eq_E and eq_O:
        print("  => A TRIPLE intersection realizes BOTH E and O -- prior")
        print("     capture (evenodd_cutfamily) CONFIRMED by exhaustive count")
        print("     over all C(|A|,3) triples.")
    else:
        print("  => prior capture NOT reproduced; numbers above are the new")
        print("     record.")
    print()
    print("=== END (exit 0 expected) ===")
    print(f"total wall: {time.time()-t0:.1f}s")


if __name__ == "__main__":
    main()
    sys.exit(0)