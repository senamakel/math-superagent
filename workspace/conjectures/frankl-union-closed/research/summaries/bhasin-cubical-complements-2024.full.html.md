# Bhasin — "A Cubical Perspective on Complements of Union-Closed Families of Sets" (arXiv:2409.17050, Sep 2024)

**Source URL:** https://arxiv.org/abs/2409.17050 (full: https://arxiv.org/html/2409.17050)
**Full text:** [[bhasin-cubical-complements-2024.full.html]] (the `.full.md` copy is
the abstract landing page; use the `.html` copy for content)
**Author:** Dhruv Bhasin (IISER Pune). v1, 25 Sep 2024.

## What it is

A **topological / cubical-homology** treatment of *complements* of union-closed
families. A family whose complement (in `2^[n]`) is union-closed is called
**simply rooted** (terminology from Balla–Bollobás–Eccles). The paper constructs,
for any family `F ⊆ 2^[n]`, a natural **cubical set** `X(F) ⊆ ℝ^n` — the geometric
subset assembled from the "cubes" `[A,B]` (intervals `A⊆C⊆B`) contained in `F` —
and studies its homology.

## Main results

- **Theorem 1.1.** If `F` is simply rooted and `∅ ∈ F`, then `X(F)` is **acyclic**
  (trivial reduced cubical homology). Proof by induction on `|F|`: remove a
  maximum-cardinality set `A`, write `X(F) = X(F∖{A}) ∪ X(F_A)` where `F_A` is
  star-shaped (hence acyclic) and the intersection is handled by the union lemma.
  Both hypotheses are needed — the paper exhibits examples showing neither
  "simply rooted" nor "`∅ ∈ F`" can be dropped.
- **Corollary 1.2 (Euler–Poincaré formula).** For a simply rooted `F` with
  `∅ ∈ F`, with `C_k(F) := {[A,B] : A⊆B, [A,B]⊆F, |B∖A|=k}` the intervals of `F`
  of size gap `k`:
  ```
  Σ_{k=0}^{n} (−1)^k |C_k(F)|  =  1.
  ```
  Equivalently the reduced Euler characteristic `χ̃(X(F)) = 0`. An **elementary
  proof** of the corollary (independent of cubical homology) is given in §2.2 via
  Lemma 2.16.

## Why it matters for this run

- This is the **source the run's approach notes cite as the precedent for the
  topological angle** (`research/approaches-grounding-notes.md`; the
  independence-complex / facet-counts approach note invokes it as "Bhasin cubical
  homology, arXiv:2409.17050") but its full text was never held. Now it is.
- It is an **adjacent-problem / method** contribution, not a bound or a settled
  class of the conjecture: the author states plainly "our results do not improve
  upon Conjecture 1.1." Its value to the run is (a) the simply-rooted ↔
  union-closed dual is a real lever the run's own Balla–Bollobás–Eccles thread
  already uses for large families, and (b) the acyclicity gives an Euler-character
  identity satisfied by all simply-rooted `F` — a candidate global constraint a
  proof could try to exploit (it neither forces nor is forced by an abundant
  element, so it is a constraint, not a proof step).
- The identity `Σ(−1)^k |C_k(F)| = 1` is **exactly checkable** on small `n` by the
  run's oracle: enumerate simply-rooted small `F`, count intervals per gap, and
  verify the alternating sum is 1. That is a cheap, genuinely new oracle check the
  library has not had.

## Status

Sourced (arXiv v1 preprint, not peer-reviewed). Theorem 1.1 + Corollary 1.2 are
asserted-by-source. The corollary's elementary content is checkable exactly by a
small-n oracle routine if a later pass extends the checker to simply-rooted
families; it is a constraint satisfied by all such families, not a proof of
Frankl's conjecture and not a constant improvement.

```claim
id: bhasin-cubical-acyclicity
statement: For any simply rooted family F ⊆ 2^[n] with ∅ ∈ F, the associated
  cubical set X(F) is acyclic; equivalently Σ_{k=0}^{n} (−1)^k |C_k(F)| = 1, where
  C_k(F) = {[A,B] intervals of F with |B∖A| = k}. Simply rooted = complement of a
  union-closed family.
hypotheses: F ⊆ 2^[n], F simply rooted, ∅ ∈ F.
holds-here: true — a global constraint satisfied by all simply-rooted (equivalently
  complement-of-union-closed) families; not a proof of, and does not imply, an
  abundant element.
status: asserted-by-source (arXiv preprint; elementary proof of the corollary given
  in the paper; not re-derived by this run's oracle).
bearing: gives the topological/simply-rooted angle a held primary source; the Euler
  formula is a new exactly-checkable constraint on small n.
anchor: research/sources/bhasin-cubical-complements-2024.full.html.full.md
```
