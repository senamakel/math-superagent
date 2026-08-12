# Gebendorfer 2026 — Power-of-Two Cycles in Cubic Bipartite Vertex-Transitive Graphs of Girth Six

Source: https://doi.org/10.5281/zenodo.18526153 (Zenodo, v3, published 2026-02-08).
NOT peer-reviewed — self-published Zenodo preprint (indices 0 citations). Treat as
**asserted-by-source**, not established, unless independently checked.

## Claim

Every **cubic bipartite vertex-transitive graph of girth six** contains a simple cycle
whose length is a power of two — specifically one of **8, 16, or 32** (sharp bound
kmin ≤ 5). Confirms the Erdős–Gyárfás conjecture for this class.

## Method (as described)

- Uses the **Potočnik–Vidali classification** of cubic vertex-transitive graphs of girth
  6, which partitions them into four families (Desargues graph exception + toroidal
  hexagonal skeletons / hyperbolic triangulation truncations / dihedral-scheme truncations).
- Novel **port voltage framework** encoding the interaction between ring structures and
  matching edges.
  - **Toroidal family**: local hexagon combinatorics gives cycles of length 8 or 16.
  - **Hyperbolic and dihedral truncation families**: two obstructions — a local
    corner-cost bound from antipodal port geometry excluding 8-cycles, and a global
    Z2-holonomy obstruction excluding 16-cycles. Despite these, a canonical ground-state
    walk in the quotient graph lifts to a simple **32-cycle**.
- Computational verification over the complete census of cubic vertex-transitive graphs
  up to **1280 vertices** confirms the theorem and identifies exactly **14 extremal graphs**
  attaining kmin = 5.

## Place in the run's picture

This is the first time the previously-unobtainable "Gebendorfer girth-6 cubic bipartite
vertex-transitive" paper (a REQUESTS open row) is on disk — closing that row. It sits
adjacent to (agent) the cubic-bipartite frontier (Tranquilli ≥60) and the Potočnik–Vidali
classification. The result, if correct, settles the conjecture for a further symmetric
restricted class.

## Caveats / falsifiers

- Not peer-reviewed; single-author preprint with 0 citations. The girth-6 girth-12
  companion papers are also self-published Zenodo.
- The 32-cycle conclusion for the excluded families is the load-bearing step; it should
  be checked against the actual graph census on disk before being reported as established.
- The claimed **full proof** of the EG conjecture by the same author
  (zenodo.18232846, "A Proof of the Erdos-Gyárfás Conjecture", 2026-01-13) is **withdrawn**:
  the record now returns HTTP 410 GONE. Do NOT cite the full proof as established — it
  contradicts the field's standing open status and has been removed.
