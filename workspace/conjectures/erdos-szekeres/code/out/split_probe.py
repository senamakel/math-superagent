"""Probe: census of cups/caps by size and rightmost point in es_construct(n).

Decides the pairing strategy for the split-gon spectrum:
  - distinct x / general position of es_construct(5,6,7)
  - number of cups / caps of each size s = 2..7, grouped by rightmost-by-x
    point index
  - timing for the subset enumeration at n=7 (32 points, C(32,7) subsets)
"""
import sys, time
from collections import Counter
from itertools import combinations
from fractions import Fraction

from lib.es_construct import es_set, es_set_blocks
from lib.cupcap import is_cup, is_cap
from lib.es_geom import in_general_position

def census(n, max_s=7):
    pts = es_set(n)
    N = len(pts)
    by_x = sorted(range(N), key=lambda i: Fraction(pts[i][0]))
    rightmost_of = lambda fs: max(fs, key=lambda i: by_x[i])
    # precompute x-order ranks for fast rightmost
    xrank = {i: r for r, i in enumerate(by_x)}

    cup_cnt = Counter()   # (size, rightmost_rank) -> count
    cap_cnt = Counter()
    t0 = time.time()
    total_subsets = 0
    for s in range(2, max_s + 1):
        for combo in combinations(range(N), s):
            total_subsets += 1
            sub = [pts[i] for i in combo]
            rm = max(xrank[i] for i in combo)
            if is_cup(sub):
                cup_cnt[(s, rm)] += 1
            if is_cap(sub):
                cap_cnt[(s, rm)] += 1
    dt = time.time() - t0
    return pts, cup_cnt, cap_cnt, dt, total_subsets

def main():
    for n in (5, 6, 7):
        pts, cup_cnt, cap_cnt, dt, total = census(n)
        N = len(pts)
        xs = [Fraction(p[0]) for p in pts]
        print(f"n={n}: N={N} distinct_x={len(set(xs))==N} "
              f"general_position={in_general_position(pts)}")
        print(f"  subsets(size 2..7) enumerated: {total}  time={dt:.2f}s")
        by_x = sorted(range(N), key=lambda i: xs[i])
        # aggregate per size
        for s in range(2, 8):
            nc = sum(v for (ss, rm), v in cup_cnt.items() if ss == s)
            na = sum(v for (ss, rm), v in cap_cnt.items() if ss == s)
            print(f"  size {s}: cups={nc} caps={na}")
        # distribution of rightmost ranks for size 7 cups (if any)
        for s in (5, 6, 7):
            per_rm = Counter()
            for (ss, rm), v in cup_cnt.items():
                if ss == s:
                    per_rm[rm] += v
            if per_rm:
                top = per_rm.most_common(6)
                print(f"  cup size {s}: rightmost-rank dist (top 6): {top}")
            per_rm = Counter()
            for (ss, rm), v in cap_cnt.items():
                if ss == s:
                    per_rm[rm] += v
            if per_rm:
                top = per_rm.most_common(6)
                print(f"  cap size {s}: rightmost-rank dist (top 6): {top}")
        # how many cups/caps share a rightmost rank with some other chain
        paired_est = 0
        for rm in range(N):
            c = sum(v for (ss, r), v in cup_cnt.items() if r == rm)
            d = sum(v for (ss, r), v in cap_cnt.items() if r == rm)
            paired_est += c * d
        print(f"  naive cup x cap pair estimate (all sizes, same rightmost): {paired_est}")

if __name__ == "__main__":
    main()