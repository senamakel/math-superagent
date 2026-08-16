#!/usr/bin/env python3
"""Convex-layer and cup/cap structure of the ES construction (es_construct).

The ES construction X_n has 2^{n-2} points, no convex n-gon.  We report its
convex layers (repeated hull peeling), which gives an integer sequence
(convex-layer sizes, then layers at each level), and its whole-set cup/cap
spectrum.  All exact.
"""
from lib.es_construct import es_set, es_set_blocks
from lib.es_geom import (convex_hull, longest_cup, longest_cap,
                         in_convex_position, largest_convex_subset)
from fractions import Fraction


def convex_layers(pts):
    """Peel convex hulls; return list of layer sizes (outer first)."""
    remaining = list(pts)
    layers = []
    while remaining:
        hull = convex_hull(remaining)
        layers.append(len(hull))
        hs = set(hull)
        remaining = [p for p in remaining if p not in hs]
    return layers


print("Whole-set cup/cap + convex layers of es_construct es_set:")
for n in (4, 5, 6):
    S = es_set(n)
    if False:
        S = [tuple(Fraction(x) for x in p) for p in S]
    cu = longest_cup(S); ca = longest_cap(S)
    kk, _ = largest_convex_subset(S)
    layers = convex_layers(S)
    nlay = len(layers)
    print(f"  n={n}: |S|={len(S)} cup={cu} cap={ca} largestConvex={kk} "
          f"layers={layers} (nlayers={nlay})")
print()

print("Layer sizes as a function of n (outer layer = hull size):")
for n in (4, 5, 6, 7):
    S = es_set(n)
    layers = convex_layers(S)
    print(f"  n={n}: |S|={len(S)} layer sizes={layers} "
          f"sum={sum(layers)}")
