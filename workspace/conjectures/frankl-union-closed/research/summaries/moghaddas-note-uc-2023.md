<!-- source: https://arxiv.org/pdf/2309.01704 -->

# Moghaddas Mehr, "A Note on the Union-closed Sets Conjecture" (2023) — summary

**Source URL:** https://arxiv.org/pdf/2309.01704
**Full text:** `research/sources/moghaddas-note-uc-2023.full.md`
**Bibliographic:** arXiv:2309.01704v3 [math.CO], 9 Sep 2023.

## What this paper is

A short note translating the union-closed sets conjecture into binary-matrix
language: rows of M are the indicator vectors of F's sets, and union-closure
becomes closure of the rows under the bitwise OR. The conjecture becomes: a
non-zero binary matrix with distinct rows closed under OR has a column with ≥ n/2
ones. The note proves this for weaker logical closures, in particular:

**Theorem 1.1.** If M is a non-zero n×m binary matrix with distinct rows closed
under **material conditional** (¬M_i ∨ M_j is a row whenever M_i, M_j are), then
some column M_{-k} has at least n/2 ones.

The author presents this as "a weaker version of the Union-Closed Set
Conjecture" — a natural relaxation, not a proof of the full conjecture. The paper
works through negation (¬), conjunction, and material conditional closures, each
yielding the n/2 column bound for the corresponding matrix class.

## Why it's in the library

The frontier listed this note (cited 3× by on-disk sources:
bouchard-2411.10608, colbert-2412.18740, and the Moghadass Mehr 2025 isomorphism
paper already on disk). It is the same author's earlier step toward the
isomorphism/lattice reconstruction work (`moghaddas-isomorphism-union-closed-2025`).
It confirms the standard context claims (Vučković–Živković n≤12; Roberts–Simpson
4q−1; Karpas (1/2−c)2^n; Gilmer 0.01 → (3−√5)/2) in one place.

## Claim blocks

```claim
id: moghaddas-material-conditional-bound
statement: For a non-zero n×m binary matrix with distinct rows closed under
  material conditional (¬M_i ∨ M_j a row whenever M_i, M_j are rows), some
  column has at least n/2 ones.
hypotheses: M non-zero, distinct rows, closed under ¬M_i ∨ M_j.
holds-here: yes — this is a different (weaker) closure assumption than
  union-closure, so it does NOT settle UC; it is a bound for the material-
  conditional matrix class.
status: asserted-by-source (arXiv:2309.01704v3)
bearing: Confirms the "closure under a logical operator ⇒ abundant column"
  pattern for the material-conditional relaxation; useful background for the
  matrix/linear-algebraic formulations of UC.
anchor: research/sources/moghaddas-note-uc-2023.full.md
falsifies: A material-conditional-closed matrix violating the n/2 column bound.
```