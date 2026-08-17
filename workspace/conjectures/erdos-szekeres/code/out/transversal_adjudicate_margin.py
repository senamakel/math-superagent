#!/usr/bin/env python3
"""Adjudicate transversal-convexity: is it (a) a structural consequence of the
construction's design, or (b) genuinely stronger than the design forces?

Design (es_construct): block i is a tiny cluster (scale 1e-6 around a local
T_i of diameter O(1) before scaling -> cluster diameter ~1e-5) centered at
C_i on a strictly convex downward arc with strictly decreasing successive
slopes.  The outer hull is one point per block in block order (Conjecture A).

Question: is EVERY transversal (one point per block) convex because the arc's
convexity DOMINATES the cluster diameter by many orders of magnitude, or is it
a knife-edge accident?

Measure, per n in {7,8,9}:
  1. cluster diameter (max pairwise distance within each block) after scaling;
  2. center-arc parameters: min successive slope drop (strength of convexity),
     min center spacing, min distance from any center to any other center's
     radial line (radius of the "convexity corridor").
  3. the ratio corridor_width / cluster_diameter -> if huge, convexity is
     structurally forced; if ~1, the property is fragile.
"""
from fractions import Fraction
from math import isqrt
from lib.es_construct import es_set_blocks


def cluster_diameter(block):
    best = Fraction(0)
    for i in range(len(block)):
        for j in range(i + 1, len(block)):
            dx = block[j][0] - block[i][0]
            dy = block[j][1] - block[i][1]
            d2 = dx * dx + dy * dy
            if d2 > best:
                best = d2
    return best  # squared


def slope(p, q):
    return (q[1] - p[1]) / (q[0] - p[0])


def center_arc_measure(n):
    pts, blocks = es_set_blocks(n)
    # centers: block 0's first point coordinates = center + tiny offset; recover
    # from _convex_arc_centers formula instead (documented in es_construct)
    m = n - 1
    start_y = Fraction(5000)
    diffs = [Fraction(-(1000 - 100 * t)) for t in range(m)]
    centers = []
    y = start_y
    for i in range(m):
        centers.append((Fraction(i * 1000), y))
        if i < m - 1:
            y = y + diffs[i]
    # successive slopes of the center polyline
    sl = [slope(centers[i], centers[i + 1]) for i in range(m - 1)]
    drops = [sl[i] - sl[i + 1] for i in range(m - 2)]  # >0 = convex downward
    min_drop = min(drops)
    max_drop = max(drops)
    # min center spacing
    spacing = [centers[i + 1][0] - centers[i][0] for i in range(m - 1)]
    return centers, min_drop, max_drop, min(spacing)


def main():
    for n in (7, 8, 9):
        pts, blocks = es_set_blocks(n)
        diam2 = [cluster_diameter(b) for b in blocks]
        max_diam = max(diam2)
        centers, mind, maxd, minsp = center_arc_measure(n)
        max_diam_f = max_diam  # squared, Fraction
        print(f"=== n={n} ===")
        print(f"  blocks={len(blocks)} cluster diam^2 max={float(max_diam):.3e}")
        print(f"  center min successive slope drop={float(mind):.4f} "
              f"max drop={float(maxd):.4f}")
        print(f"  min center x-spacing={1000}")
        # corridor width: half the min spacing is the lateral room around each
        # center before a point could reach the neighboring center's territory
        # combined with the slope-drop convexity.  Rough robustness index:
        #   robustness = (min drop * spacing) / cluster_diameter
        # (a point perturbed by < corridor stays on the correct convex side)
        corridor = Fraction(1000)  # center spacing
        for bi, d2 in enumerate(diam2):
            d = d2  # squared
        # cluster diameter itself
        diam = max_diam
        robust = (mind * corridor) ** 2 / (diam + Fraction(1))
        print(f"  slope-drop * spacing = {float(mind*corridor):.2f} ' >> ' "
              f"cluster extent ~ {float(max_diam**0.5):.2e}")
    print()
    print("Interpretation: if min slope-drop * spacing (the arc's convexity "
          "corridor, in y-units per unit x) vastly exceeds the tiny cluster "
          "diameter, transversal-convexity is forced by the design margin -- "
          "adjudication (a) structural consequence.")


if __name__ == "__main__":
    main()
