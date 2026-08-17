# Hachimori–Kashiwabara, "On the Averaging Problem of Ideal Families Related to Frankl's Conjecture with Formal Proof by Lean 4" (arXiv:2504.13454)

**Source URL:** https://arxiv.org/html/2504.13454
**Full text:** `research/sources/hachimori-kashiwabara-averaging-ideal-families-lean-2025.html.full.md` (55 KB)
**Related (already in library):** Hachimori–Kashiwabara, "Several Minimality Concepts Related to Frankl's Conjecture", Graphs and Combinatorics 2024 (doi:10.1007/s00373-024-02834-0), cited in the library's citation summaries.

## What the paper is

A 2025 paper (with a Lean 4 formalization on GitHub) on the **averaging approach** to Frankl's conjecture. The averaging approach replaces the existence of a *rare/abundant vertex* with the stronger statement that the *average* degree of the vertices is ≤ |F|/2. Every ideal family is shown to satisfy this stronger "average rarity" condition, and the proof is machine-checked in Lean 4.

## The objects (in the intersection-closed dual)

Working with **intersection-closed** families (complements of union-closed ones, as in Poonen's lattice form). A vertex `v` is *rare* if `deg_F(v) ≤ |F|/2`. A family is *average rare* if the average degree of its vertices is ≤ |F|/2 (which implies the existence of a rare vertex).

- **NDS (normalized degree sum):** `NDS(F) = 2·TSH(F) − n·|F|`, where `TSH` = total sum of degrees (sum over vertices of deg), `n = |U|`. `NDS(F) ≤ 0 ⟺ F is average rare`.
- **Ideal family (Def 2.5):** `F ⊆ 2^U` with (1) ∅ ∈ F, (2) U ∈ F, (3) downward-closed except possibly U: for all A,B ∈ F with A ≠ U, if B ⊆ A then B ∈ F. Equivalently: includes all subsets of its non-U hyperedges. Every ideal family is intersection-closed.

## Main theorem (Theorem 4.1)

> For any ideal family F on a nonempty finite ground set U, `NDS(F) ≤ 0`. Consequently all ideal families satisfy the average rarity condition (hence contain a rare vertex).

**Hypotheses:** F an ideal family on a nonempty FINITE ground set; F contains both ∅ and U; downward-closed except U. **Holds here:** the finiteness and intersection-closed hypotheses match this run's setting, but note the ground set must be IN the family (U ∈ F) — an extra structural hypothesis a general union-closed family does not carry. So this is a NEW restricted class settled, not the full conjecture.

**Proof (human + Lean):** induction on |U|. Uses that every ideal family has a rare vertex (Lemma 2.2, injection argument); deletes/contracts a rare vertex v and applies the induction hypothesis to the deletion and contraction minors (Lemmas 2.3, 2.6), which are again ideal families. Case-split on deg(v)=1 vs ≥2 and on whether U∖{v} is a hyperedge.

## Why it matters for this run

1. **It is a mechanically-checked result** — the first Lean 4 formalization on the Frankl line in this library (the library already has Ho's Lean formalization of the generalized Boppana entropy inequality, arXiv:2601.19327). This is a second, independent formalization, valuable as a cross-checkable primary source.
2. **It adds a genuinely new settled class**: ideal families are average-rare (hence Frankl holds for them), with the full hypotheses stated. ROOT.md's "settled classes" list can add this.
3. **The averaging approach** (weighting/FC line) is directly relevant to the run's `cms-averaged-frankl-wrong` claim — the paper notes average-rarity is a *strictly stronger and different* property than the existence of a rare vertex, so it does NOT prove UC for all families. It explicitly distinguishes the "average rare" subclass from Frankl's conjecture (Section 1.2).
4. It is **not** a record-constant source — it does not touch the entropy/coupling frontier (Yu 0.38234 / Liu 0.38271 conditional). The record is unchanged.

## Status / evidence class

- Theorem 4.1: **proved** (human proof in the paper + verified in Lean 4, full implementation in the linked GitHub repository). Asserted-by-source with machine-checked backing.
- Bearing for UC: settles average-rarity (hence UC) for the ideal-family class; does not settle UC in general; does not change the constant record.

## Source URL embedded

https://arxiv.org/html/2504.13454

---

```claim
id: hachimori-ideal-families-average-rare
statement: Every ideal family F ⊆ 2^U on a nonempty finite ground set U satisfies NDS(F) ≤ 0, i.e. 2·TSH(F) ≤ n·|F|; equivalently the average degree of the vertices is ≤ |F|/2, so every ideal family has a rare vertex (hence Frankl's conjecture holds for the class of ideal families).
hypotheses: U finite nonempty, F ⊆ 2^U with ∅ ∈ F, U ∈ F, and F downward-closed except possibly U (for all A,B ∈ F with A ≠ U, B ⊆ A ⟹ B ∈ F). Ground set is IN the family.
holds_here: yes — U finite, family is intersection-closed, matches this run's finite setting. Note the extra hypothesis U ∈ F is not carried by an arbitrary union-closed family, so this settles the ideal-family class only, not UC in general.
status: proved (human proof + verified in Lean 4; full implementation in the authors' GitHub repository [13]).
bearing: adds a new mechanically-checked settled class to ROOT.md; a second Lean 4 formalization on the Frankl line (alongside Ho's generalized Boppana inequality). Does NOT change the constant record (Yu 0.38234 published / Liu 0.38271 conditional) and does not prove UC. The paper explicitly distinguishes average-rarity (a strictly stronger, different property) from the existence of a rare vertex.
anchor: research/summaries/hachimori-kashiwabara-averaging-ideal-families-lean-2025.html.md
answers: (none — records a new settled class, not an open request)
```
