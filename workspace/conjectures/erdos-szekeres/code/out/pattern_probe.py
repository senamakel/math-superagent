#!/usr/bin/env python3
"""Extract the integer sequences the run's exact oracle produces on the
Erdos-Szekeres constructions and on hand-known sets.

Only facts computed here, exactly, are reported.
"""
from lib.es_geom import (in_general_position, largest_convex_subset,
                         in_convex_position, longest_cup, longest_cap,
                         convex_hull)
from math import comb

# --- 1. Hand-known sets: convex subsets of a circle (regular k-gon) ----
print("circle k -> largest convex subset:")
for k in range(3, 13):
    import math
    pts = [(int(round(1000*math.cos(2*math.pi*i/k))),
            int(round(1000*math.sin(2*math.pi*i/k)))) for i in range(k)]
    kk, _ = largest_convex_subset(pts)
    assert kk == k, (k, kk)
print("  all pass (largest = k for k=3..12)\n")

# --- 2. cups/caps function f(k,l)=C(k+l-4,k-2)+1: the classical tree ----
# The cups/caps recursion: build S(k,l) with no k-cup, no l-cap.
print("cups/caps threshold f(k,k)=C(2k-4,k-2)+1  (k=2..):")
for k in range(2, 10):
    print(f"  k={k}: C(2k-4,k-2)+1 = {comb(2*k-4, k-2)+1}")
print()

# --- 3. ES(n) values (known exact) and conjectured closed form ----
print("ES(n) exact (3..6) and conjecture 2^(n-2)+1 for n=3..10:")
for n in range(3, 11):
    print(f"  n={n}: 2^(n-2)+1 = {2**(n-2)+1}")
print()

# --- 4. Cup/cap spectra on the exact ES construction blocks (esz.py) ---
from lib.esz import es_set
print("es_set(n) [rational recursive] cup/cap spectra + largest convex:")
for n in (4, 5, 6):
    S = es_set(n)
    cu = longest_cup(S); ca = longest_cap(S)
    kk, _ = largest_convex_subset(S)
    print(f"  n={n}: |S|={len(S)} gp={in_general_position(S)} "
          f"longest_cup={cu} longest_cap={ca} largestConvex={kk}")
