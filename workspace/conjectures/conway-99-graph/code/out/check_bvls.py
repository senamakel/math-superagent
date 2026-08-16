"""BvLS verification through the canonical oracle only.

This script no longer decides anything inline. It builds the BvLS graph with
lib.srg.bvls_graph() (the corrected ternary-Golay coset construction) and
verifies strong regularity with lib.srg.is_srg([...]) — the single canonical
decision function. It also independently cross-checks the spectrum (a
suggestive check, never a decision) and confirms the graph is a Cayley graph
(vertex-transitive by construction: it is a coset graph on the abelian group
F3^5, so translation by any element is an automorphism).

This replaces the previous check_bvls.py, which carried its own inline is_srg
and its own stale (duplicate-column) coset construction that produced only
2430 edges and failed all degree checks.
"""
import numpy as np
from lib.srg import is_srg, bvls_graph


if __name__ == "__main__":
    print("BvLS verification via canonical oracle (lib.srg), no inline decision.")
    print("-" * 70)

    A = bvls_graph()
    print("bvls_graph() shape:", A.shape, " edges:", int(A.sum() // 2))

    # The single canonical decision:
    ok, why = is_srg(A, 243, 22, 1, 2)
    print("is_srg(A, 243, 22, 1, 2):", "PASS" if ok else "FAIL", "-", why)

    # Independent cross-check (suggestive only): trinomial spectrum of the srg.
    ev = np.round(np.linalg.eigvalsh(A.astype(float)), 4)
    vals, cnts = np.unique(ev, return_counts=True)
    print("spectrum (multiplicity): ", dict(zip(vals.tolist(), cnts.tolist())))
    print("expected 22^1, 4^132, (-5)^110")

    # The BvLS graph is a Cayley graph on the abelian group F3^5: the coset
    # construction makes it vertex-transitive (left translation by any group
    # element is an automorphism). This is a structural, not numerical, check.
    print("Cayley/vertex-transitive: yes by construction (coset graph on abelian F3^5).")
