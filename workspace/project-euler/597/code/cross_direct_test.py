#!/usr/bin/env python3
"""Direct test of 'cross = |left| * |right|' at the treap ROOT, and whether
cross depends only on the root identity.

Uses only the true race oracle; no treap assumption input. For the FULL range
[0,n-1] with root r = argmin W, cross = # (i<r, j>r) pairs i<j with a true
bump chain i->...->j. We check:
  (a) is cross == (r)*(n-1-r) always?
  (b) across many speed vectors sharing the SAME root r, is cross constant?
"""
import sys, os, random
from collections import defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from brute import simulate_order, outcome_parity


def W(args, L, i):
    return args[i] / (L - 40.0 * i)


def analyze(n, L, speeds):
    above = simulate_order(n, L, speeds)
    r = min(range(n), key=lambda i: W(speeds, L, i))
    cross = 0
    for i in range(r):
        for j in range(r + 1, n):
            if j in above[i]:
                cross += 1
    return r, cross


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 500000
    rng = random.Random(2024)
    for (n, L) in [(3, 160.0), (4, 160.0), (4, 400.0), (5, 400.0), (5, 1800.0)]:
        per_root = defaultdict(lambda: defaultdict(int))  # root -> cross -> count
        bad = 0
        nontrivial = 0
        for _ in range(N):
            speeds = [rng.expovariate(1.0) for _ in range(n)]
            r, cross = analyze(n, L, speeds)
            left, right = r, n - 1 - r
            if 0 < r < n - 1:
                nontrivial += 1
                if cross != left * right:
                    bad += 1
            per_root[r][cross] += 1
        print(f"n={n} L={L}: non-leaf-root cases {nontrivial}, "
              f"cross!=|L||R| in {bad} ({100.0*bad/max(1,nontrivial):.3f}%)")
        for r in sorted(per_root):
            val = per_root[r]
            if len(val) > 1:
                print(f"    root={r}: MULTIPLE cross values {dict(val)}  "
                      f"-> cross depends on speeds, NOT root alone")


if __name__ == '__main__':
    main()
