# Gilmer, "A constant lower bound for the union-closed sets conjecture" (arXiv:2211.09055)

**Full text**: `research/sources/gilmer-constant-lower-bound-2022.pdf.full.md` (587 lines,
PDF of arXiv:2211.09055v2). This is the **breakthrough paper**, Nov 2022.

## What the body establishes (verified in full text)

```claim
id: gilmer-constant-0-01
statement: For any union-closed family F ⊆ 2^[n], F ≠ {∅}, there is i ∈ [n] in at
  least a 0.01 fraction of the sets of F. This is the first constant lower bound,
  improving Knill's and Wójick's Ω(1/log₂|F|) bounds.
  Method (Theorem 1): let A,B be independent samples from a distribution over
  subsets of [n]. If Pr[i∈A] ≤ 0.01 for all i, then H(A∪B) ≥ 1.26·H(A). When
  H(A)>0 this gives H(A∪B) > H(A); sampling A,B uniformly from F with A∪B∈F
  forces H(A∪B) ≤ H(A) (uniform maximizes entropy over its support), contradiction.
hypotheses: F nonempty union-closed, F ≠ {∅}; A,B iid uniform over F.
holds-here: true
status: sourced (proved in this paper)
bearing: the original constant bound and the entropy method; the crossover example
  (Examples 1-2: product-Bernoulli gives H(A∪B)/H(A) = H(2p−p²)/H(p), which is > 1
  for p < (3−√5)/2, = 1 at p = (3−√5)/2, < 1 above) — the exact object the run's
  iid-barrier-exact reproduces.
anchor: research/sources/gilmer-constant-lower-bound-2022.pdf.full.md, Theorem 1, 2
  and Examples 1-2
```

## Structure

- §1 Introduction: Theorem 1 (H(A∪B) ≥ 1.26·H(A) under Pr[i∈A]≤0.01), Theorem 2
  (0.01 constant), Examples 1–3 (product-Bernoulli crossover at (3−√5)/2).
- §2 Notation and Preliminaries.
- §3 Main Result: Lemma 1, Theorem 1.
- §4 Proof of Lemma 1: Lemmas 2–5.
- §5 A possible path towards resolving the conjecture: **Conjecture 1** (its
  information-theoretic strengthening that would imply UC).
- §6 Conclusion.

## Relevances

- Gilmer's own Conjecture 1 (the strengthening) was **refuted** by Ellis
  (2211.12401) and independently by Sawin — recorded in
  `ellis-counterexample-gilmer-conjecture-2022.md`.
- The (3−√5)/2 value appears as the crossover of his extremal example, which is
  exactly what AHS/Chase–Lovett/Pebody/Sawin then proved as a theorem and the run
  reproduces computationally (`iid-barrier-exact`).
