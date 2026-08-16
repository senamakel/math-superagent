"""Verify the adopted route's load-bearing intersection formula.

Claim (downset-row-code-distance-closed-form): for the fold row set
    M_d = { n-1-d+o : o bitwise submask of d },  d in [2, n-1],
the intersection of two rows is the row of the AND:
    M_d ∩ M_d' = M_{d ∧ d'},   so   |M_d ∩ M_d'| = 2^{pc(d ∧ d')},
and hence the symmetric difference distance
    |M_d △ M_d'| = 2^{pc(d)} + 2^{pc(d')} - 2^{pc(d ∧ d') + 1}.

This is the foundation of condition (C) (F_n(z) = O(n) for |z|<1), which
reduces density-1 SUPPLY to the single arithmetic second-moment statement (A).
It is currently hand-checked ONLY (5 pairs at n=5,7); this is the mechanical
check over all pairs and a larger n range.
"""
import sys
sys.path.insert(0, "/workspace/code")
from lib.downset_rows import row_positions, popcount


def check_pair(n, d1, d2):
    M1 = row_positions(n, d1)
    M2 = row_positions(n, d2)
    inter = M1 & M2
    # predicted intersection = M_{d1 & d2}
    pred = row_positions(n, d1 & d2)
    ok_set = (inter == pred)
    # predicted size
    pred_size = 1 << popcount(d1 & d2)
    # predicted symmetric-difference distance
    pred_dist = (1 << popcount(d1)) + (1 << popcount(d2)) - (1 << (popcount(d1 & d2) + 1))
    actual_dist = len(M1 ^ M2)
    return ok_set, (pred_size == len(inter)), (pred_dist == actual_dist)


def main():
    bad_set = bad_size = bad_dist = 0
    pairs_checked = 0
    for n in range(8, 65):
        for d1 in range(2, n):
            for d2 in range(2, n):
                if d1 == d2:
                    continue
                pairs_checked += 1
                ok_set, ok_size, ok_dist = check_pair(n, d1, d2)
                if not ok_set:
                    bad_set += 1
                if not ok_size:
                    bad_size += 1
                if not ok_dist:
                    bad_dist += 1
    print(f"pairs checked: {pairs_checked}")
    print(f"intersection-as-set mismatches: {bad_set}")
    print(f"intersection-size mismatches:   {bad_size}")
    print(f"distance-formula mismatches:    {bad_dist}")
    if bad_set == bad_size == bad_dist == 0:
        print("ALL PASS: M_d ∩ M_d' = M_{d∧d'}, |M_d∩M_d'|=2^{pc(d∧d')}, dist formula exact")


if __name__ == "__main__":
    main()
