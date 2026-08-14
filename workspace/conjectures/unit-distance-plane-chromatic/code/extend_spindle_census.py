#!/usr/bin/env python3
"""Extend the A^k Minkowski-sum census beyond k=4 to get more terms of the
n(k) (distinct points) and e(k) (unit edges) sequences. Exact arithmetic.

Uses the calibrated field arithmetic in brute.py. For each k reports
n(k) and e(k) (edges certified by brute.is_unit, exact). Skips the full
colouring test (already shown chi=4 for k<=4) to keep the run fast; this is
a sequence-extension pass, not a new colour claim.
"""
import sys, time
from brute import moser_spindle_points, cadd, is_unit

def minkowski_level(A, k):
    pts = list(A)
    for _ in range(k - 1):
        nxt = [cadd(p, q) for p in pts for q in A]
        seen = set(); uniq = []
        for p in nxt:
            key = (p[0], p[1])
            if key not in seen:
                seen.add(key); uniq.append(p)
        pts = uniq
    return pts

def main():
    A = moser_spindle_points()
    lo, hi = int(sys.argv[1]), int(sys.argv[2])
    # carried product from lo..hi cumulative
    pts = list(A)
    for k in range(1, hi + 1):
        if k == 1:
            pts = list(A)
        else:
            nxt = [cadd(p, q) for p in pts for q in A]
            seen = set(); uniq = []
            for p in nxt:
                key = (p[0], p[1])
                if key not in seen:
                    seen.add(key); uniq.append(p)
            pts = uniq
        if k < lo:
            continue
        n = len(pts)
        t0 = time.perf_counter()
        e = 0
        for i in range(n):
            for j in range(i + 1, n):
                if is_unit(pts[i], pts[j]):
                    e += 1
        dt = time.perf_counter() - t0
        print(f"k={k}  n={n}  e={e}  (edges {dt:.1f} s)", flush=True)

if __name__ == "__main__":
    main()
