"""Characterize WHICH sets occur in S2_char(n). For each n, print every distinct
set as a bitmask, labelled by the smallest (d,d') pair realizing it, so we can
guess the structural characterization of the occurring sets.

Goal: find a closed description (e.g. sets that are symmetric-difference of two
downsets, or determined by size/run-count/pattern). Emphasize size distribution
per n and how the set of sizes grows.
"""
from collections import Counter, defaultdict
from lib.collapse import S2_char, downset, run_count
from math import comb


def main():
    # size distribution of distinct sets (BY COUNT of distinct sets, not multiplicity)
    for n in [8, 10, 12, 14, 16, 20, 24]:
        c = S2_char(n)
        by_size_cnt = Counter(len(A) for A in c)
        by_size_mult = Counter()
        for A, m in c.items():
            by_size_mult[len(A)] += m
        sizes = sorted(by_size_cnt)
        print(f"n={n:2d} distinct={len(c)} size-count(distinct): "
              + " ".join(f"{s}:{by_size_cnt[s]}" for s in sizes))
        print(f"          size-mult(weighted): "
              + " ".join(f"{s}:{by_size_mult[s]}" for s in sorted(by_size_mult)))


if __name__ == "__main__":
    main()
