# Bernardi, "Deformations of the braid arrangement and trees" — summary

- Source: Olivier Bernardi, arXiv:1604.06554 (2016). URL: https://arxiv.org/pdf/1604.06554 (full text: research/sources/bernardi_deformations_braid_arrangement_trees.full.md)
- Content: general counting formulas and bijections for real hyperplane arrangements all of whose hyperplanes are of the form x_i − x_j = s for integer s — deformations of the braid (type-A Coxeter) arrangement. Classical examples include braid, Catalan, Shi, Linial, semiorder. For any such arrangement the number of regions equals a signed count of decorated plane trees ("boxed trees"), and characteristic/coboundary polynomials have tree expressions. For *transitive* deformations (Catalan, Shi, Linial, semiorder, ...) there is an explicit bijection between regions and labeled plane trees defined by local conditions (answers a question of Gessel).
- Bearing on PE597: the run's parity cells are regions of an arrangement built from hyperplanes (L−p_j)/v_j and (p_i−p_j)/(v_i−v_j); after multiplying by the positive product of v's, these are polynomial equalities, not pure x_i−x_j = integer. Bernardi's framework covers exactly the x_i−x_j ∈ ℤ class with region counts via trees; the run's tested counts (n=3 → 32, n=4 → 1202, L-independent) do not match any standard transitive deformation found (Shi n: (n+1)^{n−1}; Linial: ~C·(2.45...)^n; Catalan: n!·(n+1)^{n−2}; semiorder; none give 32, 1202). This refines the "is the parity arrangement a known braid deformation?" question: if the answer were yes, the tree bijection would give the region count directly; the data suggest no.
- Restriction: x_i − x_j = integer only; the torpids arrangement has a different (inverse-speed) shape.

```claim
id: braid-deformation-region-counts-via-trees
statement: For any arrangement of hyperplanes x_i − x_j = s with integer s (1≤i<j≤n), the number of regions equals a signed count of decorated plane trees; for transitive deformations (Catalan, Shi, Linial, semiorder) regions are in bijection with labeled plane trees satisfying local conditions.
hypotheses: hyperplanes x_i − x_j ∈ ℤ; real arrangement.
holds-here: hypotheses do not hold for the torpids finite-finish arrangement (its hyperplanes are not of this form); the theorem bounds what the region-count route can use, and the run's counts 32/1202 are not those of any standard transitive deformation.
status: verified-against-source (arXiv:1604.06554 full text in library); comparison with run's cell counts is the run's own computation
bearing: rules in/out the "known braid-deformation" route for the parity-arrangement region count.
anchor: research/sources/bernardi_deformations_braid_arrangement_trees.full.md
```