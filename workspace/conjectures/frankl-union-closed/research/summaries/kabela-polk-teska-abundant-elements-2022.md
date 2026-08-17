# Kabela–Polák–Teska, "The number of abundant elements in union-closed families without small sets" (arXiv:2212.09279)

Source: https://arxiv.org/abs/2212.09279 ; full text:
`research/sources/kabela-polk-teska-abundant-elements-2022.html.full.md`
(v2, revised 30 May 2023). Adam Kabela, Michal Polák, Jakub Teska.
Status: arXiv preprint (v2 May 2023); publication status unchecked (see the
`kpt-published-status` note).

## What this paper is

Study of how many *abundant* elements a union-closed family must have, given
the sizes `k` (smallest set) and `n` (largest set) of the family. It answers
parts of the Cui–Hu (2019) strengthening programme: "if the smallest set has
size ≥ k, does the family have ≥ k elements in more than half the sets?"

## Convention (differs slightly from the run's usual one)

Formulated throughout for families **without** `∅`, with *abundant* = belongs
to **more than half** the sets (strict inequality). The authors state (Section
4) this is equivalent to the common formulations with `∅ ∈ F` and "at least
half": applying the theorems to `F ∖ {∅}` transfers exactly. `f` = number of
abundant elements, `k` = smallest set size, `n` = largest set size.

## Theorem 5 (many abundant elements, sufficient conditions)

For any union-closed family `F` with `∅ ∉ F`, sizes `k ≤ n` as above, and `f`
abundant elements:

1. `k ≥ n−3  ⟹  f ≥ k`;
2. `k = n−4  ⟹  f ≥ k−1`;
3. `f ≥ min{n, 2k−n+1}` always.

Statements (1) and (2) are tight (Theorem 6(4) witnesses (2)). These resolve
the Cui–Hu questions for every `k > 2`; **only `k = 2` remains open** (it is
Cui–Hu's Conjecture 4).

## Theorem 6 (constructions with few abundant elements)

`(f,k,n)`-construction = union-closed family with precisely `f` abundant
elements, smallest set size `k`, largest set size `n`.

1. Twin-free `(2,3,8)`, `(3,4,9)`, `(4,5,9)`, `(5,6,10)`-constructions exist.
2. Twin-free `(2,k,n)`-constructions exist whenever
   `Σ_{i=k−1}^{⌊n/2⌋−1} C(⌊n/2⌋−1, i) > C(n−3, k−3) + C(⌊n/2⌋−2, k−2)`;
   this holds for every `k` once `n` is large enough.
3. **A `(2,k,n)`-construction exists for every `k,n` with `n ≥ max{3, 5k−4}`**;
   `n ≥ max{3, 5k−8}` already suffices when `k` is even.
4. A `(k−1, k, n)`-construction exists for every `k,n` with
   `n−4 ≥ k ≥ 3`, `n ≥ 9` (and `(k,n) = (3,8)`).

Item (3) is the precise form of the "exactly two abundant elements, smallest
set of size `k` arbitrarily large" construction that the run's claim
`cambie-survey-two-abundant-capped` attributed to Cambie's survey as `P_k^n`.
The primary source's exact parameter range is `n ≥ 5k−4` (odd `k`) / `5k−8`
(even `k`). So the number of abundant elements cannot be forced past 2 by
growing `k` while `n` grows linearly in `k` — relevant to the run's
`abundance-profile` thread.

## Proposition 7 (relations among the strengthenings)

With `Conj 1` = Frankl (∅∉F, some element in > half), `Conj 2` = Poonen
(unique abundant element ⟹ it is in every set), `Conj 3` = Poonen's twin-free
version (unique abundant element ⟹ `F` is the family of all sets of `2^M`
containing it), `Conj 4` = Cui–Hu k=2 (smallest set size ≥ 2 ⟹ ≥ 2 abundant):

**Conj 3 ⟹ Conj 2 ⟹ Conj 4 ⟹ Conj 1.**

So Cui–Hu's k=2 conjecture is strictly between Frankl and Poonen: proving
Conj 4 proves UC, and Conj 2 implies Conj 4. This is a source-backed placement
of the breadth-two case of the abundance profile.

## Why this source was added

The claim `cambie-survey-two-abundant-capped` was asserted via Cambie's survey
(`cambie-progress-offsprings-2023`) which cites this paper ([11] in its
bibliography); the primary source was not on disk. It now anchors that claim
with exact hypotheses and parameter ranges and provides the Proposition 7
implication chain (a new claim, `kpt-cuihu-k2-between-frankl-poonen`).

```claim
id: kpt-two-abundant-constructions
statement: For every k ≥ 3 and n with n ≥ max{3, 5k−4} there is a union-closed
  family F with ∅ ∉ F, smallest set size k, largest set size n, and precisely
  two abundant elements (elements in more than half the sets of F); for even k
  the range n ≥ max{3, 5k−8} suffices. Twin-free variants exist under the
  binomial inequality of Theorem 6(2). Hence the number of abundant elements
  cannot be forced above 2 by making the smallest set large, as long as the
  largest set grows linearly in k.
hypotheses: F finite union-closed, ∅ ∉ F; k = min |A| over A ∈ F;
  n = max |A|; abundant = in > |F|/2 sets (strict; equivalent to the ≥half,
  ∅∈F convention via F∖{∅}).
holds-here: yes
status: proved (in source; proof on disk, arXiv preprint, publication status
  unchecked)
bearing: anchors and sharpens claim cambie-survey-two-abundant-capped with the
  exact n ≥ 5k−4 / 5k−8 ranges; bounds the abundance-profile thread — a
  minimal counterexample (indeed any UC family) can have as few as 2 abundant
  elements even with all sets large.
anchor: research/sources/kabela-polk-teska-abundant-elements-2022.html.full.md
  (Theorem 6(3))
ceiling: a published journal version superseding the preprint would not change
  the mathematics; a construction with exactly ONE abundant element and
  smallest set ≥ 3 would refute the strictness claims (none exists — Conj 1 is
  Frankl's conjecture itself).
```

```claim
id: kpt-many-abundant-theorem5
statement: If F is union-closed with ∅ ∉ F, k = smallest and n = largest set
  size, and f = number of elements in more than half the sets of F, then:
  (1) k ≥ n−3 ⟹ f ≥ k; (2) k = n−4 ⟹ f ≥ k−1; (3) f ≥ min{n, 2k−n+1}.
  Bounds (1) and (2) are tight (Theorem 6(1),(4)). This resolves the Cui–Hu
  questions for every k > 2; k = 2 (Conjecture 4) remains open.
hypotheses: F finite union-closed, ∅ ∉ F.
holds-here: yes
status: proved (in source; proof on disk, arXiv preprint)
bearing: gives a source-backed lower bound on the abundance profile of any
  family: when the smallest set is close in size to the largest, many elements
  must be abundant. Directly usable in minimal-counterexample arguments.
anchor: research/sources/kabela-polk-teska-abundant-elements-2022.html.full.md
  (Theorem 5)
ceiling: none stated by the authors (statement (3) likely improvable, they note).
```

```claim
id: kpt-cuihu-k2-between-frankl-poonen
statement: Let Conj 4 (Cui–Hu k=2) be: every union-closed F with smallest set
  size ≥ 2 has at least two elements in more than half its sets. Then
  Poonen's twin-free conjecture ⟹ Poonen's unique-abundant conjecture
  ⟹ Conj 4 ⟹ Frankl's conjecture (Conj 1). So Conj 4 is strictly between
  Frankl's and Poonen's conjectures.
hypotheses: ∅ ∉ F convention; strict "more than half" abundant; the four
  conjectures as stated in the paper are equivalent to their common
  formulations.
holds-here: yes
status: proved (in source; proof on disk, arXiv preprint)
bearing: the k=2 abundance question (families with no 1- or 2-element sets) is
  not weaker machinery than UC — it implies UC. A proof of "no small sets
  ⟹ ≥ 2 abundant" is a proof of Frankl's conjecture, so the run should not
  attack it as a strictly easier target.
anchor: research/sources/kabela-polk-teska-abundant-elements-2022.html.full.md
  (Proposition 7)
ceiling: an implication in the reverse direction (Conj 1 ⟹ Conj 4) is not
  claimed and would not contradict the paper.
```

```claim
id: kpt-published-status
statement: As of this run's check, Kabela–Polák–Teska (arXiv:2212.09279, v2
  30 May 2023) is an arXiv preprint; no journal appearance was verified.
hypotheses: none beyond the identity of the paper.
holds-here: yes
status: asserted-by-source (arXiv listing; journal status unchecked, to be
  re-verified if the paper is cited as a published result)
bearing: lets the run cite the theorems with confidence while keeping the
  publication-status claim honest.
anchor: https://arxiv.org/abs/2212.09279
ceiling: a journal/inproceedings record for arXiv:2212.09279 supersedes this.
```