# Baek & Balko 2025, "The Erdős–Szekeres Conjecture Revisited", SoCG 2025

Source: https://doi.org/10.4230/LIPIcs.SoCG.2025.13
Full text: [[baek-balko - The Erdos-Szekeres Conjecture Revisited - SoCG 2025 correct.full]]
(The mis-download `... SoCG 2025.full.md` is superseded by this correct copy.)

## What it establishes

```claim
id: baek-balko-split
statement: Every set of at least 2^{k-2}+1 points in general position contains a 'split k-gon', and this is tight: 2^{k-2}+1 is exactly the threshold for split k-gons.
hypotheses: planar, general position
holds-here: yes
status: proved
bearing: a relaxed version of the ES conjecture is TRUE and its threshold equals the conjectured exact value — evidence the 2^{k-2}+1 quantity is the right one, and a template for weakening the convex-position condition.
anchor: research/sources/baek-balko - The Erdos-Szekeres Conjecture Revisited - SoCG 2025 correct.full.md
```

```claim
id: baek-balko-decomposable
statement: The Erdős–Szekeres conjecture ES(k)=2^{k-2}+1 holds for 'decomposable' point sets: every decomposable set of 2^{k-2}+1 points contains k in convex position.
hypotheses: decomposable point set, general position
holds-here: yes
status: proved
bearing: a restricted class (a natural ≥1 for GOAL/R0OT: restricted classes already settled). Decomposable = recursively built from the ES construction's block structure.
anchor: research/sources/baek-balko - The Erdos-Szekeres Conjecture Revisited - SoCG 2025 correct.full.md
```

Also: the ordered-3-uniform-hypergraph analogue of ES is NOT true (contrast — shows the geometric
setting is special); new 2^{k-2}-point no-k-gon constructions generalizing all previously known
ones, enabling computational attack at large k.

## Significance for the run

This is the strongest currently-known *exact-threshold* result: the split-k-gon relaxation is tight
at exactly 2^{k-2}+1, and the full conjecture holds for decomposable sets. It suggests the
structural route: prove convex-position can be forced from a split k-gon + extra structure, or
that every extremal 2^{k-2}-set is near-decomposable. The decomposition/Tverberg-type machinery in
the paper is directly reusable for structural lemmas about hypothetical extremal sets.
