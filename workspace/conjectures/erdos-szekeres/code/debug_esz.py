#!/usr/bin/env python3
"""Debug the ES construction blocks: verify each T(a,b) block satisfies its
no-cup/no-cap hypothesis and flatness using the exact oracle."""
from brute import cup_cap_spectrum, largest_convex_subset, general_position
from lib.esz import es_blocks
from lib import esz
from lib.esz import es_set_exact

print("Blocks for n=5 (sizes sum to 8):")
for i, Ti in enumerate(es_blocks(5)):
    cu, ca = cup_cap_spectrum(Ti)
    print(f"  block i={i}: size={len(Ti)} cup={cu} cap={ca} "
          f"maxSlope={float(esz._max_abs_slope(Ti)):.3f}")
    print(f"     coords={[(float(p[0]),float(p[1])) for p in Ti]}")

print()
print("Full n=5 set coordinates:")
S = es_set_exact(5)
for i, p in enumerate(S):
    print(f"  {i}: ({float(p[0]):.4f}, {float(p[1]):.4f})")
k, ex = largest_convex_subset(S)
print("largest convex subset:", k)
print("general position:", general_position(S))
