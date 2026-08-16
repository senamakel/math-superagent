# Summary — CORRIGENDUM: mislabeled file identity

**This file is a corrigendum.** The physical full text at
`research/sources/konieczny_gowers_thuemorse_rudinshapiro.full.md` was downloaded
under the *wrong* arXiv identity. What that file actually contains is:

- **arXiv:1905.03283 (v3, 22 Aug 2021), Jakub Konieczny, *Algorithmic
  classification of noncorrelated binary pattern sequences* [math.NT].**

It is **NOT** the Gowers-norms paper. The correct Gowers-norms source is
`research/sources/konieczny_gowers_thuemorse_rudinshapiro_1611.09985.full.md`
(arXiv:1611.09985, *Gowers norms for the Thue–Morse and Rudin–Shapiro
sequences*), which is what this workspace actually needs for the correlation-
order question. Anyone citing the Gowers-norm statement must cite
`1611.09985`, **never** `1905.03283`.

## What 1905.03283 actually establishes

Binary pattern sequences `a_A(n) = (−1)^{#(n,A)}` (A a finite set of binary
words, `#(n,A)` the number of pattern occurrences in the binary expansion of
n). A sequence is **noncorrelated** when its spectral measure equals Lebesgue
measure (i.e. the autocorrelation `γ_a(m) = E_n a(n)a(n+m)` vanishes for all
m ≥ 1).

- **Theorem A.** There are precisely 2272 noncorrelated binary pattern sequences
  of pattern length ≤ 4.
- **Theorem B.** There is an algorithm running in `2^{O(ℓ)}` operations that
  decides whether a given pattern set `A ⊆ {0,1}^ℓ` yields a noncorrelated
  pattern sequence.
- Background: the Rudin–Shapiro sequence `r(n) = (−1)^{#(11,n)}` **is**
  noncorrelated; the Thue–Morse sequence is *not* noncorrelated (its
  autocorrelation `γ_t(2^ℓ) = −1/3 ≠ 0`) but does have small Gowers norms
  [Kon19].

## Bearing on SUPPLY / the reopened question

Marginal, and it is the *wrong* half of the dichotomy the reopened question
cares about. "Noncorrelated" is autocorrelation-level (order-2, vanishing);
the fold-collapsing Thue–Morse is **not** noncorrelated yet still collapses.
So noncorrelation is neither necessary nor sufficient for the fold collapse,
and this paper does not bear on the order-`K` question. It records the correct
arXiv identity and is kept only to prevent the mislabel from being cited.

```claim
id: konieczny-1905.03283-is-noncorrelated-patterns-not-gowers
statement: The physical file research/sources/konieczny_gowers_thuemorse_rudinshapiro.full.md contains arXiv:1905.03283 (Algorithmic classification of noncorrelated binary pattern sequences), NOT the Gowers-norms paper. The Gowers-norms paper is arXiv:1611.09985.
hypotheses: file identity / provenance only.
holds-here: Corrections a mis-download. The library's Gowers-norm statement must be sourced to 1611.09985.
status: checked (file header read; this is a provenance correction)
bearing: Prevents citing noncorrelated-pattern-sequence results as Gowers-norm results.
anchor: research/sources/konieczny_gowers_thuemorse_rudinshapiro.full.md
```
