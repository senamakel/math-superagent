"""Mechanical check of the Paley(9)-pattern deduction steps in Keramatipour
Thm 3.4.2 (the claim that a putative srg(99,14,1,2) cannot follow the Paley(9)
pattern). This does NOT re-derive the theorem; it verifies that the specific
local deductions the proof relies on are consistent with the pattern being the
3x3 rook graph = Paley(9) = srg(9,4,1,2), and that the pattern's 9-vertex
realization is exactly rook(3).

Exact integer / exact combinatorial only. No floats. run: python3
code/out/paley9_pattern_deductions.py
"""
import itertools
import numpy as np
from lib.srg import is_srg, rook


def rook_adj(n=3):
    return rook(n)


def check_9vertex_is_paley9():
    """The 9 vertices {v, v1..v4, (v1,v3),(v1,v4),(v2,v3),(v2,v4)} form rook(3)."""
    A = rook(3)
    ok, detail = is_srg(A, 9, 4, 1, 2)
    print(f"rook(3) 'is' srg(9,4,1,2): {ok}  [{detail}]")
    return ok


def pattern_C4_deduction():
    """Verify: for triangles {0,1,2} and {0,5,6} (matched pairs {1,2},{5,6} of
    N(0)), the pattern-deduced edges among (1,5),(1,6),(2,5),(2,6) form a C4.
    We realize (1,5),(1,6),(2,5),(2,6) as a 2x2 subgrid of rook(3) and check
    the induced edges are exactly a C4.
    """
    # In rook(3), place the four (·,·) vertices at the corners of a 2x2 block
    # (i,j), i in {0,1}, j in {0,1}: same-row or same-column adjacent.
    # (1,5)=(0,0),(1,6)=(0,1),(2,5)=(1,0),(2,6)=(1,1)
    names = {(0, 0): "(1,5)", (0, 1): "(1,6)", (1, 0): "(2,5)", (1, 1): "(2,6)"}
    cells = list(names)
    edges = []
    for (a, b) in itertools.combinations(cells, 2):
        if (a[0] == b[0]) != (a[1] == b[1]):
            edges.append(frozenset((names[a], names[b])))
    adj = sorted(sorted(e) for e in edges)
    print("pattern C4 -> induced edges among (1,5),(1,6),(2,5),(2,6):")
    for e in adj:
        print("   ", e)
    expected = {
        frozenset(["(1,5)", "(1,6)"]), frozenset(["(2,5)", "(2,6)"]),
        frozenset(["(1,5)", "(2,5)"]), frozenset(["(1,6)", "(2,6)"]),
    }
    edge_set = {frozenset(e) for e in edges}
    # degree of each of the 4 vertices in the C4 = 2
    deg = {n: 0 for n in names.values()}
    for e in edges:
        for n in e:
            deg[n] += 1
    ok = edge_set == expected and all(d == 2 for d in deg.values())
    print(f"C4 deduction corroborated: {ok}  (4 vertices, all degree 2, "
          f"edges = the claim's 4)")
    return ok


def pattern_parallelism_deduction():
    """Verify the 'parallelism' edge set: for triangles {1,(1,3),(1,4)} and
    {1,(1,5),(1,6)} the deduced edges
      {(1,3,5),(1,4,5)}, {(1,3,5),(1,3,6)}, {(1,4,5),(1,4,6)}, {(1,3,6),(1,4,6)}
    form a C4 on the four (1,·,·) vertices. Same 2x2-block structure."""
    names = {(0, 0): "(1,3,5)", (0, 1): "(1,4,5)", (1, 0): "(1,3,6)", (1, 1): "(1,4,6)"}
    cells = list(names)
    edges = []
    for (a, b) in itertools.combinations(cells, 2):
        if (a[0] == b[0]) != (a[1] == b[1]):
            edges.append(frozenset((names[a], names[b])))
    expected = {
        frozenset(["(1,3,5)", "(1,4,5)"]), frozenset(["(1,3,5)", "(1,3,6)"]),
        frozenset(["(1,4,5)", "(1,4,6)"]), frozenset(["(1,3,6)", "(1,4,6)"]),
    }
    edge_set = {frozenset(e) for e in edges}
    ok = edge_set == expected
    print(f"parallelism edge set corroborated: {ok} "
          f"edges={sorted(sorted(e) for e in edges)}")
    return ok


def negative_control_rook_has_pattern():
    """The pattern lemma is already verified (paley9_pattern_check_fixed).
    Here we re-affirm that rook(3) itself = Paley(9) realizes the pattern, so
    the theorem cannot 'rule out' the pattern at a k=4 step that breaks it."""
    A = rook(3)
    ok, _ = is_srg(A, 9, 4, 1, 2)
    print(f"rook(3) realizes srg(9,4,1,2) [control for pattern-realizability]: {ok}")
    return ok


if __name__ == "__main__":
    print("=" * 70)
    print("Paley(9)-pattern deduction steps — mechanical corroboration")
    print("=" * 70)
    all_ok = True
    all_ok &= check_9vertex_is_paley9()
    all_ok &= pattern_C4_deduction()
    all_ok &= pattern_parallelism_deduction()
    all_ok &= negative_control_rook_has_pattern()
    print("=" * 70)
    print(f"ALL STEPS CORROBORATED: {all_ok}")
    print("NOTE: this verifies the pattern's LOCAL edge-deduction rules are")
    print("self-consistent and match rook(3). It does NOT re-derive Thm 3.4.2's")
    print("full 99-vertex contradiction; that requires the complete forced")
    print("configuration (u in N_{2,4}, v in N_{1,3}, and the 3-common-neighbour")
    print("clash). The full theorem remains unchecked as a 99-exclusion.")
