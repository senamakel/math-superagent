"""Cross-check the OEIS catalogued Mycielski vertex/edge sequences against the
verified textbook Mycielski construction. The verified run
(code/out/diag_mycielski.captured.txt) gives C5=5v/5e, Mycielski(C5)=11v/20e,
Mycielski^2(C5)=23v/71e. OEIS A083329 (vertex counts) and A122695 (edge counts)
should reproduce exactly these. This turns a catalogue lookup into a checked
reproduction, so a later reader does not have to take the b-file on faith."""

import sys
sys.setrecursionlimit(10000)


def mycielski_verts_edges(v, e):
    """Canonical (no-mirror) textbook Mycielski: keep G; add a twin vertex u_i
    for each; add cross edge u_i--v_j iff u_j--v_i (i.e. twin_i~twin_j iff
    base_i~base_j); add apex u adjacent to all twins. Vertices 2v+1, edges 3e+v.
    CORRECTED from the earlier 4e+v form, which is the mirror variant B (the
    25/111/467 counts) the run does not use; 4e+v gives 4*5+5=25 != the verified
    20-edge M(C5). The canonical transition is (v,e)->(2v+1, 3e+v): C5(5,5) ->
    M1(11,20) -> M2(23,71) -> M3(47,236), all matching the OEIS catalogue."""
    return 2 * v + 1, 3 * e + v


# OEIS A083329: a(0)=1, a(n)=3*2^(n-1)-1 for n>0  (vertex counts)
# Index n counts Mycielski iterations from K1/empty. We use the raw terms.
A083329 = [1, 2, 5, 11, 23, 47, 95, 191, 383, 767, 1535]
# OEIS A122695: number of edges in n-th Mycielski graph (terms as given)
A122695 = [0, 0, 1, 5, 20, 71, 236, 755, 2360, 7271, 22196]

# Build Mycielski iterates starting from C5 indexing consistently.
# The OEIS A083329 terms: index i -> vertices of the i-th Mycielski graph.
# n=0 is the empty graph (per A122695 comment), n=1 the single vertex, etc.
# We instead just verify the library's verified values match the catalogue
# at the correct offsets.
print("Verify catalogue vs verified Mycielski construction")
print("=" * 60)

# Verify the two closed forms reproduce consecutive catalogue terms.
for name, terms in [("A083329 vertices", A083329), ("A122695 edges", A122695)]:
    ok = True
    for i in range(1, len(terms)):
        if name.startswith("A083329"):
            # a(n) = 3*2^(n-1) - 1 for n>0 ; check a(n) = 2*a(n-1)+1 for n>=2
            if i >= 2 and terms[i] != 2 * terms[i - 1] + 1:
                ok = False
                print(f"  {name}: recurrence fails at i={i}")
        else:
            # a(n) = 6a(n-1)-11a(n-2)+6a(n-3) for n>4
            if i >= 5 and terms[i] != 6 * terms[i - 1] - 11 * terms[i - 2] + 6 * terms[i - 3]:
                ok = False
                print(f"  {name}: recurrence fails at i={i}")
    print(f"  {name}: catalogue self-consistent = {ok}")

# Direct reproduction of the Mycielski vertex/edge counts via the formula.
print("\nMycielski iteration from C5 (5v,5e):")
v, e = 5, 5
print(f"  iter0 (C5):            v={v:3d} e={e:3d}")
for k, (vv, ee) in enumerate([(11, 20), (23, 71), (47, 236)], start=1):
    v, e = mycielski_verts_edges(v, e)
    mark = "OK" if (v, e) == (vv, ee) else "MISMATCH"
    print(f"  iter{k} (Mycielski^{k}(C5)): v={v:3d} e={e:3d}  expect v={vv:3d} e={ee:3d}  {mark}")

# Cross-check that the catalogue terms equal these at the right offsets.
# A083329: index 2 -> 5, index 3 -> 11, index 4 -> 23  (C5, M1, M2 vertices)
# A122695: index 3 -> 5, index 4 -> 20, index 5 -> 71   (C5, M1, M2 edges)
verts_match = (A083329[2], A083329[3], A083329[4]) == (5, 11, 23)
edges_match = (A122695[3], A122695[4], A122695[5]) == (5, 20, 71)
print(f"\nCatalogue A083329[2..4] vs (5,11,23): {verts_match}")
print(f"Catalogue A122695[3..5] vs (5,20,71): {edges_match}")
print(f"\nOVERALL MATCH: {verts_match and edges_match}")
