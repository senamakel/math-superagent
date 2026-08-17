# Marković — On Vladimir Božin's equivalent to Frankl's union-closed sets conjecture

Source: https://people.dmi.uns.ac.rs/~markovicp/papers/AAA99%20-%20handout.pdf (Petar Marković, Arbeitstagung Allgemeine Algebra 99, Siena, Feb 2020; conference handout, not a journal paper).

Full text: `research/sources/markovic-bozin-equivalent-frankl.full.md`

## What this establishes

A probabilistic (measure-on-sets, not measure-on-elements) **equivalence theorem** for Frankl's conjecture, stated in the intersection-closed (IC) dual form. Let `A ⊆ P(T)` be an IC family (`T, ∅ ∈ A`, closed under intersection), and let `p : A → [0,1]` be a probability measure with `P(a ∈ X) := Σ_{X∈A_a} p(X)` (the `p`-probability that a random set contains `a`), and `f_A(a) := |A_a|/|A|` the uniform frequency.

**Theorem (Božin 2004, the "Equivalence Theorem")**: Frankl's conjecture is true iff for every IC family `A ⊆ P(T)` and every probability measure `p : A → [0,1]` satisfying `P(a ∈ X) ≥ 1 − f_A(a)` for all `a ∈ T`, we have

```
E(log |π_X(A)|) / log |A| ≥ 1/2
```

where `π_X(A) = {X ∩ Y : Y ∈ A}` (the projection of A onto X).

- The `(⇐)` direction is short: if Frankl fails, take `p(T) = 1−q`, `p(∅) = q` for `q > 1/2`, giving ratio `1−q < 1/2`.
- The `(⇒)` direction is a construction: from a violating `(A, p)` it builds an IC family where every element's frequency is `> 1/2`, i.e. a counterexample to Frankl. The construction uses tensor powers `A ⊗ I`, the families `A1, A2, A3, C`, and a convex combination `F = C ∪ {X∪{e_1..e_k}} ∪ {X∪{e_1..e_MAX} : X ∈ A3}` with four growth parameters `K1..K4`.

## Why this is a distinct reformulation

Poonen's weights assign a weight per **element**; Božin's measure assigns weight per **set**, which the source notes is strictly more general ("This is more general than each element having its weight"). The handouts ultimate remark: the author's attempted applications (construct a family + measure making the conclusion fail) have **not succeeded** — so the method has not yet been pushed through.

## Evidence class

- Statement: asserted-by-source (a 2004 Božin theorem, restated in this 2020 handout; primary Božin source not located).
- The `(⇐)` proof is reproduced verbatim in the handout and is short and checkable.
- Not a claim that Frankl holds or fails — it is an equivalence, so it does not improve the constant or settle any class.

## Falsifier / note

This adds no numerical constant. It would be falsified as recorded if Božin's 2004 theorem statement differs from this restatement, or if the construction in `(⇒)` has a hidden error — but the handout is a talk, and the construction should be treated as asserted-by-source, not verified locally.

```claim
id: markovic-bozin-equivalence
statement: Frankl's conjecture holds iff for every intersection-closed (IC)
  family A ⊆ P(T) (T,∅ ∈ A) and every probability measure p: A → [0,1] with
  P(a∈X) := Σ_{X∈A_a} p(X) ≥ 1 − f_A(a) for all a ∈ T (f_A(a)=|A_a|/|A| the
  uniform frequency), we have E[log|π_X(A)|]/log|A| ≥ 1/2, where π_X(A) =
  {X∩Y : Y ∈ A} is the projection of A onto X. (Božin 2004, restated by
  Marković 2020.) The (⇐) direction uses p(T)=1−q, p(∅)=q, q>1/2; the (⇒)
  direction is a tensor-power construction producing a counterexample from a
  violating (A,p). This is a measure-on-SETS reformulation, strictly more
  general than Poonen's per-element weights.
hypotheses: A intersection-closed on T (T,∅ ∈ A); p a probability measure on A;
  the stated per-element coverage condition.
holds-here: yes — an exact equivalence; it neither improves the constant nor
  settles a class, and Marković notes no application pushing it through has
  succeeded yet.
status: asserted-by-source (Božin 2004 theorem restated in a 2020 conference
  handout; primary Božin source not on disk; (⇐) reproduced verbatim and
  checkable, (⇒) construction treated as asserted).
bearing: a distinct reformulation (weights on sets vs elements) the approach
  ledgers had not mapped; a would-be counterexample-hunter route whose (⇒)
  construction is the least verified link.
anchor: research/sources/markovic-bozin-equivalent-frankl.full.md
```

Wikilink the full text: [[markovic-bozin-equivalent-frankl.full]]
