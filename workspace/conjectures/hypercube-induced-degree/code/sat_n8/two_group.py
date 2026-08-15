#!/usr/bin/env python3
"""Construction-family scan: Q_8 split into two groups of 4 coords.

Each vertex x in {0,1}^8 is (a,b), a,b in {0,1}^4; classify by
(wa,wb) = (popcount(a), popcount(b)).  A coordinate flip changes exactly one
of wa,wb by +-1.  We choose S = {x : (wa,wb) in R} for a region R subset of
the 5x5 grid, and measure |S| and D(S) exactly.

Internal degree of a selected vertex at (wa,wb):
  a-flips: wa edges to (wa-1,wb) if in R, (4-wa) to (wa+1,wb) if in R
  b-flips: wb edges to (wa,wb-1) if in R, (4-wb) to (wa,wb+1) if in R

Target: |S| = 129 and D(S) <= 3.  This is a closed-form FAMILY (not an
enumeration of the answer space); a working R is verified by a direct degree
count on the actual 256-vertex set.
"""
from itertools import combinations

C = [1, 4, 6, 4, 1]  # C(4, wa)
GRID = [(wa, wb) for wa in range(5) for wb in range(5)]


def cell_count(wa, wb):
    return C[wa] * C[wb]


def total(R):
    return sum(cell_count(wa, wb) for (wa, wb) in R)


def max_deg(R):
    """Max internal degree over selected vertices (the (wa,wb) formula)."""
    Rset = set(R)
    best = 0
    for (wa, wb) in Rset:
        d = 0
        if wa - 1 >= 0 and (wa - 1, wb) in Rset:
            d += wa          # flip a one-bit -> weight wa-1
        if wa + 1 <= 4 and (wa + 1, wb) in Rset:
            d += 4 - wa      # flip a zero-bit -> weight wa+1
        if wb - 1 >= 0 and (wa, wb - 1) in Rset:
            d += wb
        if wb + 1 <= 4 and (wa, wb + 1) in Rset:
            d += 4 - wb
        best = max(best, d)
    return best


def verify_actual(R):
    """Direct degree count on the real 256-vertex set (independent route)."""
    pop = [bin(x).count('1') for x in range(256)]
    groupA = [x & 0xF for x in range(256)]
    groupB = [(x >> 4) & 0xF for x in range(256)]
    wa_ = [bin(groupA[x]).count('1') for x in range(256)]
    wb_ = [bin(groupB[x]).count('1') for x in range(256)]
    S = [x for x in range(256) if (wa_[x], wb_[x]) in R]
    Sset = set(S)
    nb = {v: [v ^ (1 << k) for k in range(8)] for v in range(256)}
    mx = 0
    for v in S:
        d = sum(1 for u in nb[v] if u in Sset)
        mx = max(mx, d)
    return len(S), mx


# Handpicked promising regions first (diamond-ish, excluding large corners).
candidates = []
# all 3x3 blocks
for r0 in range(3):
    for c0 in range(3):
        R = {(r0 + i, c0 + j) for i in range(3) for j in range(3)}
        candidates.append((f"3x3@{r0},{c0}", R))
# diamonds / shapes
base = {(1, 1), (1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2), (3, 3), (2, 2)}
candidates.append(("diamond3x3", base))

print("Scan handpicked regions: size and D(S):")
for name, R in candidates:
    sz, dd = total(R), max_deg(R)
    tag = "  <== HIT" if sz == 129 and dd <= 3 else ""
    print(f"  {name:<14} size={sz} D={dd}{tag}")

# Now search: we want size exactly 129.  Enumerate all subsets of size |R|=k
# for small k is intractable for 25 cells, so do a targeted greedy/beam over
# cells sorted by count, but *only* report a region with size==129 and D<=3.
# (Construction discovery, then direct verification.)


def beam_search():
    """Beam over subsets of grid cells hitting size 129, minimizing D."""
    # all 25 cells
    allcells = GRID
    from collections import defaultdict
    # state: frozenset of cells; keep the best by (|D|-ish).  We want a
    # region; start from single cells and grow/swap.
    import random
    random.seed(1)
    best = None
    for trial in range(200000):
        R = set()
        # build up
        cells = list(allcells)
        random.shuffle(cells)
        for c in cells:
            # add if keeps size <= 130 and improves toward 129
            if total(R | {c}) <= 130:
                R.add(c)
        sz = total(R)
        if sz == 129:
            dd = max_deg(R)
            if best is None or dd < best[1]:
                best = (frozenset(R), dd)
                if dd <= 3:
                    return R
    return None


print("Beam search for a size-129, D<=3 region...")
Rf = beam_search()
if Rf:
    sz = len(set())
    dd = max_deg(Rf)
    a_sz, a_dd = verify_actual(Rf)
    print(f"found R={sorted(Rf)}")
    print(f"  grid size={total(Rf)} D={max_deg(Rf)}")
    print(f"  ACTUAL verify: |S|={a_sz} D={a_dd}")
else:
    print("no size-129 region found (family too restrictive or search missed)")
