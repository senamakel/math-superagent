#!/usr/bin/env python3
"""Adjudicate whether transversal-convexity of es_construct is a structural
consequence or an artifact.

Question (from the steering): is "every full transversal (one point from each
block T_0..T_{n-2}) of the ES construction is in convex position" a *structural
consequence* of how the construction is built -- tiny clusters on a strictly
convex arc with the hull taking one point per block in block order -- or a
property of the one canonical es_construct placement?

Method: re-realize the ES block structure with the SAME combinatorial blocks
(the cupcap blocks T_i) but with INDEPENDENTLY chosen:
  (1) cluster scale s (the tiny-cluster radius multiplier), and
  (2) arc geometry (the strictly convex downward arc the centers sit on),
and test whether *every* full transversal remains convex.

If transversal-convexity survives for a broad range of (s, arc), it is a
structural consequence of the design (tiny clusters on a strictly convex arc),
not an artifact of the exact 1e-6 placement.  If it breaks at the first
perturbation of s or the arc, the finding is placement-specific and says
nothing about general n-avoiding sets.

Exact arithmetic throughout (Fractions); convexity via lib.es_geom on
exact Fraction coordinates.
"""
from fractions import Fraction
from math import comb, prod
from itertools import product

from lib.es_construct import es_block, _flatten_y, _bbox
from lib.es_geom import in_convex_position, in_general_position, convex_hull


def build_generic(n, scale_s, arc_kind="parabola", seed_jitter=0):
    """Build 2^{n-2} points as the n-1 blocks T_i on a strictly convex arc.

    scale_s: the tiny-cluster radius multiplier (es_construct uses 1e-6).
    arc_kind: 'canonical' reproduces es_construct's arc exactly;
              'parabola' uses y = -C*x^2 (a strictly downward-convex arc);
              'exp'      uses y = -D*exp(x) (convex arc, asymmetric).
    Returns (points, blocks, centers).
    """
    m = n - 1
    centers = []
    if arc_kind == "canonical":
        start_y = Fraction(5000)
        diffs = [Fraction(-(1000 - 100 * t)) for t in range(m)]
        y = start_y
        for i in range(m):
            centers.append((Fraction(i * 1000), y))
            if i < m - 1:
                y = y + diffs[i]
    elif arc_kind == "parabola":
        # downward-convex: y = 5000 - C*x^2 with centers at x = i*spacing
        spacing = Fraction(1000)
        C = Fraction(1, 3600)      # curvature so the arc is well spread
        for i in range(m):
            x = i * spacing
            centers.append((x, Fraction(5000) - C * x * x))
    elif arc_kind == "exp":
        spacing = Fraction(900)
        D = Fraction(1, 1000)
        for i in range(m):
            x = i * spacing
            centers.append((x, Fraction(4000) - D * (Fraction(1) << (i + 4))))
    else:
        raise ValueError(arc_kind)

    blocks = []
    points = []
    for i in range(m):
        T = es_block(n, i)          # exact cupcap block, already flattened
        T = _flatten_y(T, Fraction(1, 40))
        # normalize T to origin
        x0, x1, y0, y1 = _bbox(T)
        T0 = [(x - x0, y - y0) for (x, y) in T]
        # apply the tiny scale
        sc = Fraction(scale_s)
        block = [(cx + sc * px, cy + sc * py) for (cx, cy) in (centers[i],) for (px, py) in T0]
        blocks.append(block)
        points.extend(block)
    return points, blocks, centers


def all_transversals_convex(n, scale_s, arc_kind):
    points, blocks, centers = build_generic(n, scale_s, arc_kind)
    sizes = [len(b) for b in blocks]
    total = prod(sizes)
    gp = in_general_position(points)
    non_convex = 0
    first_bad = None
    for choice in product(*[range(s) for s in sizes]):
        sub = [blocks[k][choice[k]] for k in range(n - 1)]
        if not in_convex_position(sub):
            non_convex += 1
            if first_bad is None:
                first_bad = (choice, sub)
    return gp, total, non_convex, first_bad


def main():
    print("=== Transversal-convexity: is it structural or placement-specific? ===")
    print("Tests the 'tiny clusters on a strictly convex arc' design rationale.\n")

    # 1. Canonical scale, canonical arc -> should reproduce the run's PASS
    print("--- (1) canonical scale 1e-6, canonical arc ---")
    for n in (5, 6, 7):
        gp, total, nc, bad = all_transversals_convex(n, "1e-6", "canonical")
        print(f"  n={n}: gp={gp} transversals={total} non_convex={nc} "
              f"{'PASS' if nc==0 and gp else 'FAIL'}")
        if bad is not None:
            print(f"     FIRST BAD: {bad[0]}")

    # 2. Vary the cluster scale: does the property survive larger clusters?
    print("\n--- (2) vary cluster scale s (arc = canonical) ---")
    for s in ("1e-4", "1e-3", "1e-2", "1e-1", "1"):
        for n in (5, 6):
            gp, total, nc, bad = all_transversals_convex(n, s, "canonical")
            tag = "PASS" if (nc == 0 and gp) else "FAIL"
            extra = f" first_bad={bad[0]}" if bad is not None else ""
            print(f"  n={n} s={s}: gp={gp} transversals={total} non_convex={nc} {tag}{extra}")

    # 3. Vary the arc geometry (convex arc shape) at canonical tiny scale
    print("\n--- (3) vary arc kind at scale 1e-6 ---")
    for arc in ("parabola", "exp"):
        for n in (5, 6, 7):
            gp, total, nc, bad = all_transversals_convex(n, "1e-6", arc)
            tag = "PASS" if (nc == 0 and gp) else "FAIL"
            extra = f" first_bad={bad[0]}" if bad is not None else ""
            print(f"  n={n} arc={arc}: gp={gp} transversals={total} non_convex={nc} {tag}{extra}")


if __name__ == "__main__":
    main()
