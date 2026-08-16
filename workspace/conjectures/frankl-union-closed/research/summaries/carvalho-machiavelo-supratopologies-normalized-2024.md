# Carvalho & Machiavelo, "On supratopologies, normalized families and Frankl conjecture" (2024)

Source: https://arxiv.org/abs/2408.11213 (A. Carvalho, A. Machiavelo, arXiv
2408.11213, Aug 2024). Full text:
`research/sources/carvalho-machiavelo-supratopologies-normalized-2024.full.md`.

## What this source is

A 2024 preprint that recasts Frankl's union-closed sets conjecture in
**supratopological** and **normalized-family** language and produces new
reduction results. It is recent and complementary to the entropy era
(2022–23), and not yet in the run's library before this.

## Key ideas and results

- A **supratopology** on X is a family of "open sets" closed under finite unions
  but **not** under finite intersections — so a union-closed family `F` IS a
  supratopology on `U(F)`. Frankl's conjecture is exactly: every finite
  supratopological space has a point in at least half the open sets.
- A family is **normalized** if `U¬a` (the union of all sets not containing `a`)
  is a proper subset of the universe for every `a` (no element belongs to every
  set, loosely). **Proposition 2.8 / 2.5**: it suffices to prove Frankl for
  *separating* / *independent* / *normalized* families (each is a reduction of
  the general case).
- **Separating proposition (Prop 2.2)**: a separating union-closed family on an
  n-element universe has ≥ n sets; a normalized separating family has an
  element `a` in every non-empty set.
- **Theorem 4.11 (reduction)**: if `N` is n-normalized and `M` a minimal
  non-empty set of `N`, then `N' = (N \ {M}) ⊖ {a_N}` is (n−1)-normalized; this
  is a genuinely smaller family. This yields an **infinite descendant class**:
  **Theorem 5.5** — every family obtained by successively applying the reduction
  process to a power set **satisfies Frankl's conjecture**.
- **Refined Poonen conjecture**: Conjectures 5.1 (non-power-set families have an
  element in strictly more than half) and 5.2 (if most frequent element is
  exactly half, F is a power set) are shown **equivalent** (Theorem 5.3).
- Relevant to the abundance-profile thread: Conjecture 2.7 (there is a k-set
  contained in ≥ 2^{−k}|F| sets) holds *if* FC holds (Prop 2.8).

```claim
id: carvalho-reduction-descendants
statement: There is a reduction process on normalized union-closed families
  (removing a minimal set and taking a dual/⊖-reduction) under which every
  family obtainable from a power set by successive reductions satisfies Frankl's
  conjecture (Theorem 5.5); the reduction preserves normalization with universe
  size one smaller (Theorem 4.11). Also, propositions 2.5/3.2 reduce FC to
  separating/independent/TD families, and normalized separating families have an
  element in every non-empty set (Prop 2.2).
hypotheses: finite families; normalization and the ⊖ reduction as defined in the
  paper (arXiv:2408.11213, §2, §4).
holds-here: true — stated for the exact finite union-closed families of the
  problem; no contradiction with the entropy-era results found.
status: asserted (preprint, 2024; not cross-checked here)
bearing: supplies a reduction-based structural tool and a class (descendants of
  power sets) newly settled; complements the entropy barrier by a different
  (combinatorial-reduction) route. The normalized-family reductions also bound
  the structure a minimal counterexample would need.
anchor: research/sources/carvalho-machiavelo-supratopologies-normalized-2024.full.md
  (Theorems 4.11, 5.5, Props 2.2, 2.5, 3.2).
```

## What it implies for this run

- Adds a 2024 line of attack not covered before: reduce FC to normalized /
  independent / separating families and then reduce further by a dual operation.
- The descendant-of-power-set class is a **new settled restricted class**
  (alongside chordal bipartite graphs, modular lattices, etc.) worth adding to
  ROOT.md's list.
- Does **not** take the entropy path; it is a candidate alternative route for
  the inventor to consider. Its reduction of FC to the claim that a minimal
  counterexample must be abnormal in a specific way is a live structural lead,
  relevant to the abundance-profile and minimal-counterexample threads.
