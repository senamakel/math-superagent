"""Calibration of the unit-distance graph oracle pair on the Moser spindle.

Gating calibration from GOAL.md. Builds the 7-vertex Moser spindle from two
unit rhombi sharing a vertex, certifies every edge exactly, and runs the
complete colouring test for k=4 (expect SAT, witness) and k=3 (expect UNSAT).

Expected: chi = 4 — 4-colourable, not 3-colourable.
"""
import os
import sys

import sympy as sp

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))  # ensure code/ importable absolute
from lib.unitgraph import unit_graph, moser_spindle
from lib.coloring import chromatic_colorable, verify_coloring


def main():
    print("=" * 70)
    print("CALIBRATION: Moser spindle — unit-distance graph oracle pair")
    print("=" * 70)

    # ---- 1. exact coordinates ----
    pts = moser_spindle()
    names = ["O", "P1", "P2", "Q", "P1'", "P2'", "Q'"]
    print("\n[1] Exact coordinates (field Q(sqrt3, sqrt11, sqrt33)):")
    for name, (x, y) in zip(names, pts):
        print(f"    {name:4s} = ({sp.srepr(x)}, {sp.srepr(y)})")

    # sanity: no floats anywhere in coordinates
    for (x, y) in pts:
        assert not (sp.sympify(x).has(sp.Float) or sp.sympify(y).has(sp.Float)), "float coordinate!"

    # ---- 2. edge certification ----
    print("\n[2] Edge certification (exact |p_i - p_j|^2 == 1):")
    n, edges = unit_graph(pts)
    print(f"    vertices = {n}")
    print(f"    certified unit edges = {len(edges)} (expected 11)")
    for (i, j) in edges:
        xi, yi = pts[i]
        xj, yj = pts[j]
        d2 = sp.simplify((xi - xj) ** 2 + (yi - yj) ** 2)
        assert d2 == 1, f"edge {i}-{j} not exactly 1: {d2}"
        print(f"      {names[i]:4s} -- {names[j]:4s}   |.|^2 = 1  (shown {d2})")
    assert len(edges) == 11, f"expected 11 edges, got {len(edges)}"
    print("    -> all 11 edges certified EXACTLY, no tolerance.")

    # ---- 3. chromatic number ----
    print("\n[3] Complete colouring test:")
    ok4, col4 = chromatic_colorable(n, edges, 4)
    print(f"    k=4: {'SAT (4-colourable)' if ok4 else 'UNSAT'}")
    if ok4:
        assert verify_coloring(n, edges, col4), "4-colouring witness FAILED independent check"
        print(f"      4-colouring witness -> colour[v]: {col4}")
        bycol = [[] for _ in range(4)]
        for v, c in enumerate(col4):
            bycol[c].append(names[v])
        for c in range(4):
            print(f"      colour {c}: {bycol[c]}")

    ok3, _ = chromatic_colorable(n, edges, 3)
    print(f"    k=3: {'SAT (3-colourable — WRONG)' if ok3 else 'UNSAT (not 3-colourable)'}")

    print("\n[4] Verdict:")
    if ok4 and not ok3:
        print("    chi = 4  ->  calibration PASSED  (matches problem.md expectation)")
    else:
        print("    chi != 4  ->  calibration FAILED")

    # ---- 5. cross-pair audit ----
    print("\n[5] Audit — confirm exactly the 11 claimed edges, no spurious ones:")
    # all pairs by name, but only print the unit ones that we claimed; and
    # also explicitly scan every unordered pair for unit distance to prove
    # that the edge list is complete.
    all_pairs = set()
    for i in range(n):
        for j in range(i + 1, n):
            xi, yi = pts[i]
            xj, yj = pts[j]
            d2 = sp.simplify((xi - xj) ** 2 + (yi - yj) ** 2)
            if d2 == 1:
                all_pairs.add((i, j))
    claimed = set(edges)
    assert all_pairs == claimed, f"edge list incomplete: {claimed ^ all_pairs}"
    print("    full scan of all 21 pairs found exactly the same 11 edges as certified.")


if __name__ == "__main__":
    main()
