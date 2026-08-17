# Bouchard, "An upper bound for union-closed family size" (arXiv:2511.10608, 2025)

<!-- source: https://arxiv.org/html/2511.10608 | full text: research/sources/bouchard-upper-bound-family-size-2511.full.md -->

## What it establishes

Let `A` be a union-closed family on universe `[n]`, and `ℓ = ℓ(A)` its
**length** — **one less than the maximum size of a chain (= the max number of
distinct members in a chain of sets under strict inclusion), i.e.
`ℓ = (maximal inclusion-chain length) − 1`**. This is the source's definition,
exactly as §1 and the proof's base case state (e.g. `A = {[n]}` has chain
length 1, so `ℓ = 0`, `|A| = C(n,0) = 1`). It is NOT the size of the largest
member set: for the equality family `A = {S ⊆ [n] : |S| ≥ n−ℓ}` the largest
member is `[n]` (size n), so "size of largest member" would make the bound
`2^n`, never tight — that gloss in an earlier draft of this note was wrong and
is corrected here (see `code/out/bouchard_length_bound_check.py`).

- **Theorem 1**: `|A| ≤ Σ_{i=0}^{ℓ} C(n,i)`, with **equality iff**
  `A = {S ⊆ [n] : |S| ≥ n−ℓ}`, i.e. all subsets of size at least `n−ℓ`.
  This **tightens Erdős's classic bound**, which took the largest `ℓ+1`
  binomial coefficients; under union-closure it is the *first* `ℓ+1`.
- **Theorem 2**: the sharper analytic estimate
  `Σ_{i=0}^{k} C(n,i) ≤ (k^{p}−1)/(k−1) + 2^{n}(1 − 2^{−k})^{p}` for any
  nonnegative integer `p`, with `p̂ = ⌊(n−k)/log₂(k/(1−2^{−k}))⌋ + 1` giving a
  bound valid for all `1 ≤ k ≤ n`. Also gives `|A| ≤ (ℓ^{p}−1)/(ℓ−1) +
  2^{n}(1−2^{−ℓ})^{p}`.
- **Corollary 2.1**: some element of the universe appears in **at most**
  `Σ_{i=0}^{ℓ} C(n-1,i)` of its member sets (the dual, "at most" frequency
  side of the same length-count bound).

## Bearing for this run

- Refines the **Reimer / Erdős size-structure** line already in the library:
  Reimer's `|A| ≤ (2/log₂|A|)·Σ|A|` is an implicit upper bound; this is an
  explicit sharp length-parameterised bound with full equality characterisation.
- Relevant to the **minimal-counterexample** thread: a minimal counterexample
  to UC can be taken separating (WLOG), and bounding its size by its length is
  one route to ruling out small cases. The `(1/2)·2^n` large-family boundary
  (Karpas) combined with `|A| ≤ Σ_{i≤ℓ} C(n,i)` bounds how short the height of
  a counterexample can be.
- Not a new record constant and does not settle UC; a structural refinement.

## Falsifier

A union-closed family on `[n]` with length `ℓ` and
`|A| > Σ_{i=0}^{ℓ} C(n,i)` would refute Theorem 1. (None known; equality case
exhibited by all large subsets.)

```claim
id: bouchard-upper-bound-length
statement: For any union-closed family A on universe [n] with length ℓ (max member-set size;
  one less than the longest chain), |A| ≤ Σ_{i=0}^{ℓ} C(n,i), with equality iff
  A = {S ⊆ [n] : |S| ≥ n−ℓ} (all subsets of size ≥ n−ℓ) (Theorem 1). This tightens Erdős's
  bound (largest ℓ+1 binomial coefficients) to the FIRST ℓ+1 under union-closure. Corollary 2.1:
  some element appears in ≤ Σ_{i=0}^{ℓ} C(n−1,i) member sets (the "at most" dual frequency bound).
  Theorem 2: Σ_{i=0}^{k} C(n,i) ≤ (k^p−1)/(k−1) + 2^n(1−2^{−k})^p with p̂ = ⌊(n−k)/log₂(k/(1−2^{−k}))⌋+1.
hypotheses: A finite union-closed family, universe [n], length ℓ = ℓ(A) one less than max chain size.
holds-here: yes — refines the Reimer/Erdős size-structure line already in the library
  (rarest-count-floor, ecu-n...); relevant to bounding the size of a minimal counterexample by its
  length.
status: asserted (Bouchard arXiv:2511.10608, 2025, proofs in full text; elementary induction, not
  yet oracle-checked)
bearing: an explicit sharp length-parameterised upper bound with full equality characterisation;
  combined with Karpas's |F| < 2^{n−1} for a counterexample, it bounds how short the height of a
  counterexample can be. Not a record constant; a structural refinement.
anchor: research/sources/bouchard-upper-bound-family-size-2511.full.md
follows-from: (standalone size bound)
falsifies: a union-closed family on [n] with length ℓ and |A| > Σ_{i=0}^{ℓ} C(n,i).
```
