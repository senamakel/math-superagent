# Goaoc & Welzl, "Convex Hulls of Random Order Types" (2020, JACM 2022)

<!-- source: https://arxiv.org/abs/2003.08456 | full text: research/sources/goaoc-welzl-Convex-Hulls-of-Random-Order-Types-ar5iv.full.md -->
Full text held at `research/sources/goaoc-welzl-Convex-Hulls-of-Random-Order-Types-ar5iv.full.md`
(converted from https://ar5iv.labs.arxiv.org/html/2003.08456). arXiv:2003.08456;
published J. ACM (2022). Authors: Xavier Goaoc, Emo Welzl.

## What it establishes

A structural/probabilistic study of **order types** (realizable simple planar order
types = realizable uniform acyclic oriented matroids of rank 3). Nothing here settles
the ES conjecture, but three results bear directly on the run's order-type apparatus:

1. **Average hull size (Theorem 1.1–1.3).** A size-*n* order type, chosen uniformly
   among all simple order types, has on average **4+o(1) extreme points**. For labeled
   order types the average is exactly `4 − 8/(n²−n+2)` with variance < 3. So "most"
   simple planar order types have an almost-tiny convex hull — a striking structural
   contrast with the ES conjecture's extremal sets (which are constructed to have
   large convex subsets relative to n-gon freedom at N = 2^{n−2}).

2. **Order types with forbidden patterns (Theorem 1.4, §1.3.5).** A proportion
   1 − O(1/n) of size-n order types contain *k* points with 3 extreme points and the
   other k−3 inner points forming a convex chain with one hull edge. This is a
   "relative of the Erdős–Szekeres theorem" in exactly the forbidden-configuration
   direction the run's structural arm needs. §1.3.5 explicitly surveys the
   Károlyi–Solymosi (JCTA 2005) and Károlyi–Tóth (DCG 2012) forbidden-order-type
   program — the same literature the library had only at paywalled abstract and
   which this source restates in context — and notes **no prior count of order types
   avoiding a fixed pattern in general position** was known.

3. **Symmetry groups (Theorem 1.5–1.6).** The symmetry group of an affine set in
   general position is cyclic Z_k with k dividing every layer size but the lonely
   point; of a projective set is a finite subgroup of SO(3): Z_m, D_m, S_4, A_4, or
   A_5. Relevant to isomorph-rejection in any enumeration (GOAL 3): the number of
   labeled order types per unlabeled one is bounded (Cor 6.2), which constrains how
   much symmetry reduction an enumeration can hope to win.

## Why it matters to this run

- The forbidden-pattern layer gives a *third* route into restricted classes (beyond
  split k-gons and decomposable sets): fixing a forbidden non-convex order type T is
  exactly the Károlyi–Tóth F_T(n) abstraction, and this source is now the in-library
  reference for that program alongside the paywalled original (which remains
  documented-but-not-held; treat F_T(n) constants as asserted-by-source via the
  search summaries, not as sourced from the primary text).
- The concentration facts warn the run's own sampling: random grids / random point
  sets almost never hit extremal order types, so any "most sets behave like X" claim
  about ES extremal sets cannot be tested by sampling order types from the uniform
  distribution. The ES construction is an outlier, not typical.

## Claim

```claim
id: goaoc-welzl-average-hull-4
statement: A size-n simple planar order type chosen uniformly at random has on
  average 4+o(1) extreme points (labeled average exactly 4 − 8/(n²−n+2), variance <3).
hypotheses: realizable simple planar order types; uniform distribution; n ≥ 3.
holds-here: this bound is about typical order types, whereas the run cares about
  extremal (atypical) ones; does not bound ES(n) but frames what extremal sets
  must deviate from.
status: asserted-by-source (proved in the paper).
bearing: context for GOAL 1 — extremal sets of 2^{n−2} points are highly atypical
  in having small-largest-convex-subset relative to their size.
anchor: research/summaries/goaoc-welzl-Convex-Hulls-of-Random-Order-Types-ar5iv.md
```

```claim
id: goaoc-welzl-forbidden-pattern-chain
statement: For any fixed k ≥ 3, proportion 1 − O(1/n) of size-n order types contain
  k points with 3 extreme and the rest a convex chain along one hull edge.
hypotheses: simple planar order types in general position; k fixed, n → ∞.
holds-here: gives the vocabulary and structural target for a forbidden-configuration
  restricted class — the Károlyi–Tóth F_T(n) program restated in library.
status: asserted-by-source.
bearing: restricted-class route for GOAL 1/4; not an ES upper bound.
anchor: same file.
```
