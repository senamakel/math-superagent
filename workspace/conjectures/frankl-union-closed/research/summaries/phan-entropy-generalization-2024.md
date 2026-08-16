# Phan — "Entropy approach for a generalization of Frankl's conjecture" (arXiv:2412.18622, Dec 2024)

**Source URL:** https://arxiv.org/abs/2412.18622 · **Full text:** [[phan-entropy-generalization-2024.full]]
**Author:** Veronica Phan (Ho Chi Minh City)

## What it is

A short (preprint, v1) paper giving a **necessary and sufficient condition** for a
finite family of sets to have an element in at least half its members. It applies
to **arbitrary finite families**, not only union-closed ones, so it strictly
generalises the setting. When read for a union-closed family it is exactly
equivalent to Frankl's conjecture — i.e. it is a **reformulation, not a
resolution**.

## The main theorem (Theorem 1)

For a family `F ⊆ 2^[n]`, write `F(S) := { S ∪ F : F ∈ F }`. Then:

> there is an element `i` in at least half of the sets of `F`
> **if and only if**
> there is a family `G ⊆ 2^[n]` with `|G| > 1` such that
> ```
> Σ_{S∈F} log |G(S)|  ≤  |F| · log|G| / 2      (logs base 2)
> ```

- **(Only-if)** is trivial: take `G = {∅, {i}}` for an abundant `i`; then
  `|G(S)| = 1` if `i ∈ S`, else `2`, so the LHS equals `w(i) := #{S∈F : i∉S} ≤ |F|/2`.
- **(If)** rests on Lemma 2: any set-valued random variable `X` on `2^[n]`
  admits non-negative `x_1,…,x_n` with `H(X) = Σ x_i` and
  `H(X ∪ S) ≥ Σ_{i∉S} x_i` for all `S`. Then feeding `X = X_G` (uniform on `G`)
  gives `Σ_i x_i w(i) ≤ (|F|/2) H(X_G)`, so some `i` has `w(i) ≤ |F|/2`.

**Corollary 4** (the form the author stresses): If `F` is union-closed and there
is a **subfamily** `G ⊆ F`, `|G|>1`, satisfying the same inequality, then UC holds
for `F`. This condition depends only on the union structure of `F`, **not on the
ground set**.

## Not a proof — an equivalent criterion

- The theorem is an *equivalence*, so it neither proves Frankl's conjecture nor
  improves the constant. Its value is as a **reformulation**: UC is equivalent to
  "every union-closed `F` admits such a subfamily `G`".
- The author notes the naive choice `G = F` can fail (example
  `F = {∅, {1}, {1,2}}`), and sketches a strategy using `G ⊂ F^N` (the family of
  `N`-fold unions) with a large-`N` density argument — presented as an expectation,
  not a proof.
- It does **not** use or beat the entropy constant `0.38234` (Yu/Cambie); it is a
  structural reformulation in the Gilmer-entropy spirit, not a new bound.

## Why it matters for this run

- It is a **fresh, self-contained reformulation** of the conjecture: "find the
  subfamily `G`". The run's GOAL item 4 (attack one precise claim) could target
  proving such a `G` exists, or hunting a union-closed `F` with no such `G` that
  still satisfies UC (which would be fine) — and hunting a `G`-less
  *counterexample* would fail only because UC holds on small `n`.
- The inequality is **finite and checkable exactly** for small `F`/`G` (integer logs
  via integer exponents). A computational pass could: enumerate small union-closed
  `F`, and for each decide whether some subfamily `G` meets the inequality —
  verifying Corollary 4's criterion is *not vacuous* (there is such a `G`) on
  small cases, and locating where the naive `G=F` choice first fails. That is a
  cheap, genuinely new oracle check the library currently lacks.
- It reframes UC as a statement about the "union-structure" alone (no ground-set
  dependence), which aligns with the theorem's `w(i)` formulation.

## Status

Sourced (arXiv preprint v1, Dec 2024; not peer-reviewed). The equivalence's proof
is elementary and self-contained (verified on reading; not re-run by the oracle).
It is asserted-by-source that this is a reformulation, not a bound or a settled
class. A future exact small-`n` check of "every UC `F` on `n≤4` admits such `G`"
would independently confirm the criterion is non-vacuous.

```claim
id: phan-entropy-criterion
statement: A finite family F ⊆ 2^[n] has an element in ≥ |F|/2 members iff there
  is G ⊆ 2^[n], |G|>1, with Σ_{S∈F} log|G(S)| ≤ |F|·log|G|/2 (logs base 2). For
  union-closed F it suffices to take a subfamily G ⊆ F (Corollary 4). This is
  equivalent to Frankl's conjecture, so it is a reformulation, not a proof or a
  new bound.
hypotheses: F finite family of subsets of [n] (arbitrary, need not be union-closed
  for Theorem 1; union-closed for Corollary 4).
holds-here: yes — it is an exact equivalence (reformulation) for the conjecture's
  statement; it does not change the constant or settle a class.
status: asserted-by-source (preprint; proof elementary, structurally verified on
  reading, not re-run by oracle).
bearing: gives a new finite, exactly-checkable criterion for UC that the run could
  computationally probe on small n; reframes UC as union-structure-only.
anchor: research/sources/phan-entropy-generalization-2024.full.md
```
