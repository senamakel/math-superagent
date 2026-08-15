# Lovász's neighborhood-complex theorem χ(G) ≥ conn(N(G)) + 3

**Source URL:** Kozlov, "Chromatic numbers, morphism complexes, and Stiefel-Whitney
characteristic classes", arXiv:math/0505563 (survey), and the primary Lovász 1978 paper
"Kneser's conjecture, chromatic number, and homotopy", J. Combin. Theory Ser. A 25 (1978)
319–324 (https://doi.org/10.1016/0097-3165(78)90022-5). Babson–Kozlov "Topological
obstructions to graph colorings", Electron. Res. Announc. AMS (2003)
https://doi.org/10.1090/s1079-6762-03-00112-4.

**How obtained:** Publisher/preprint hosts blocked at the network boundary (tool
refusals, confirmed). Obtained through the server-side retrieval layer (`read_sources`),
which returned the exact statement quoted below. Source summary.

## What it establishes

**Definition (Lovász 1978).** The *neighborhood complex* N(G) of a graph G has as its
vertices the non-isolated vertices of G, and as its simplices exactly the subsets of V(G)
that possess a common neighbour. Equivalently the maximal simplices are precisely the
neighbourhoods N(v), v ∈ V(G). N(G) is homotopy-equivalent to the Hom complex Hom(K2, G).

**Theorem (Lovász [Lov78], as stated by Kozlov).** Let G be a graph such that N(G) is
k-connected for some k ∈ Z, k ≥ -1. Then

```
χ(G) ≥ k + 3.
```

Equivalently `χ(G) ≥ conn(N(G)) + 3`.

**The k ≥ -1 convention.** The parameter k is allowed to be -1 (non-emptiness), in which
case the bound reads χ(G) ≥ 2. **Calibration check:** the Petersen graph KG(5,2) has χ=3
and N(G) a wedge of circles (conn=0), giving 0+3=3 ✓. So `conn(N(G)) ≥ 2 ⇒ χ(G) ≥ 5` is
the certificate this run's approach wants.

**Kneser–Lovász:** χ(KG(n,k)) = n - 2k + 2, proved as the lower bound via this
neighborhood-complex / Borsuk-Ulam machinery.

## Relevance to this run
The `neighborhood-complex-topological` approach derives from this: a plane unit-distance
graph with conn(N(G)) ≥ 2 (N(G) 2-connected) is provably not 4-colourable. The approach is
**refuted** as a 5-certifier (N(G) is high-dimensional; certifying 2-connectivity needs
hard homotopy triviality; value capped at χ=3 on the triangular lattice by Lovász's own
theorem) but kept as a cheap negative filter.

## Hypotheses
- G any finite simple graph. k ≥ -1. Holds here for every finite plane unit-distance graph.

## Claim block

```claim
id: lovasz-neighborhood-theorem-chi-ge-conn-plus-3
statement: For any graph G with neighborhood complex N(G) (vertices the
  non-isolated vertices, simplices the subsets sharing a common neighbour),
  if N(G) is k-connected for some k >= -1 then chi(G) >= k + 3.
  Equivalently chi(G) >= conn(N(G)) + 3. (Lovasz 1978; N(G) is
  homotopy-equivalent to the Hom complex Hom(K2,G).)
hypotheses: G finite simple graph; k an integer >= -1 (k=-1 reads chi >= 2).
holds-here: YES — every plane unit-distance graph is finite simple; conn(N(G)) >= 2
  would certify chi >= 5.
status: asserted-by-source (Lovasz 1978, JCT-A 25:319-324; stated verbatim by
  Kozlov arXiv:math/0505563 and Babson-Kozlov EJC survey). Calibration: Petersen
  KG(5,2), chi=3, conn(N(G))=0, 0+3=3 (consistent).
bearing: the theorem behind the neighborhood-complex-topological approach,
  which this run has refuted as a 5-certifier (hard homotopy triviality, value
  capped) but keeps as a cheap negative filter.
anchor: research/sources/lovasz-1978-neighborhood-complex-theorem.md
falsifies: a graph with conn(N(G)) >= 2 that is 4-colourable — impossible if both
  the theorem and the connectivity computation are correct; the genuine failure
  is every construction having conn(N(G)) <= 1.
```

## Cross-references
- Approach: `research/approaches/neighborhood-complex-topological.md`.
- Claim ledger: id `lovasz-neighborhood-theorem-chi-ge-conn-plus-3`.
