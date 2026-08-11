# Permutation Statistics in Conjugacy Classes of the Symmetric Group

Campion Loth, Levet, Liu, Stucky, Sundaram, Yin — arXiv:2301.00898 (math.CO, 2023)
Source: https://arxiv.org/abs/2301.00898 ; full text at
https://ar5iv.labs.arxiv.org/html/2301.00898
(Companion full text: research/conjugacy_class_statistics_body.full.md)

## What the source establishes

The paper studies the distribution of permutation statistics on a *single conjugacy
class* C_λ of S_n (cycle type λ = (1^{a_1}, 2^{a_2}, …, n^{a_n})), and proves the
following, all by elementary bijective/conjugacy-argument (no character theory).

**Core object — the inversion indicator.**  For 1 ≤ i < j ≤ n, let I_{i,j}(ω)=1 iff
ω(i) > ω(j).  Lemma 4.7 gives an explicit formula for the probability over C_λ:

  Pr_λ[I_{i,j}=1] = 1/2 + a_2/(n(n-1)) − a_1(a_1−1)/(2n(n-1))
      + (j−i−1) · [n − n·a_1 − a_1 + a_1² − 2·a_2] / [n(n−1)(n−2)].

Two consequences (stated explicitly in the paper, §4.1):
  * It depends only on n, a_1, a_2, and the **gap d = j−i** — NOT on the absolute
    positions i, j.  (Translation invariance in the gap.)
  * It is **affine (linear) in the gap d = j−i**, with slope controlled by
    n − n·a_1 − a_1 + a_1² − 2·a_2.
This is precisely the mechanism the run observed empirically for
f_n(k) = #{ (π,i): (π^i)(k) < (π^i)(0) } = A_n + (k−1)·B_n (arithmetic in the gap k,
translation-invariant in the row) — here the same translation-invariance and
gap-affineness are proved for the per-ν inversion indicator on each conjugacy class.

**Weighted inversion statistics — Theorem 4.8.**  Any X = Σ_{i<j} wt(i,j)·I_{i,j}
(des, maj, inv and more are such statistics) has expectation over C_λ equal to
  E_λ[X] = C_1(n,a_1,a_2)·α_n(X) + C_2(n,a_1,a_2)·β_n(X),
where α_n(X)=Σwt(i,j), β_n(X)=Σ(j−i−1)wt(i,j) are independent of λ.  Hence the
first moment of ANY weighted inversion statistic on a conjugacy class depends only
on n, a_1, a_2 (Theorem 1.1).  Concrete first moments are tabulated: e.g.
  E_λ[inv] = (3n² − n + 2a_2 − a_1² + a_1 − 2n·a_1)/12.

**Higher moments / polynomiality — Theorems 1.3, 1.5, 7.16, 7.26, Prop 7.28.**
For a statistic realizable over a constraint set of size m, the k-th moment
E_λ[X^k] is independent of λ whenever every part of λ has size ≥ mk+1.  For
*symmetric* permutation statistics (a class that includes inversions), each such
moment is a polynomial in n of degree ≤ mk; for inv, E_λ[inv^k] is a degree-2k
polynomial with leading coefficient 4^{−k}, and explicit E_λ[inv²] (all parts ≥ 5)
and Var_λ[inv] are given.  Conjugacy class averages over C_λ and over all of S_n
are connected by the class-equation / centralizer identity (eq. 6.1).

## What it implies for THIS problem

The run's core reduction (memory.md) expresses Q(n) from A_n and B_n, where
f_n(k) = A_n + (k−1)B_n counts, over all powers π^i, when (π^i)(k) < (π^i)(0).
That empirical translation-invariance + gap-affineness now has a *proved* analogue in
the literature: on each conjugacy class, the probability of an inversion at gap d is
affine in d and independent of absolute position.  λ here is the cycle type of (the
common cycle type of all powers) — i.e. a_1 = number of fixed points, a_2 = number of
2-cycles of the underlying π.  So the slope and intercept of f_n(k) should be
recoverable by summing this per-ν formula over cycle types — a route to closed forms
for A_n and B_n that this source opens and the run had not closed.

CAVEAT (as in report_literature_ranks_powers.md for Cambie-Yan): this paper's
statements are for a *fixed* permutation statistic evaluated on a conjugacy class;
it does NOT address the sum of *Lehmer/rank* over the cyclic subgroup {π^i} of one
permutation, which remains the unresolved core.  It supplies the per-ν / per-gap
mechanism but not the power-map/iterate sum.

## Assessment

Authoritative primary source (peer-reviewed-style arXiv math.CO, CC-BY, multiple
conjugacy-class results), downloaded from ar5iv HTML rendering.  Distinct from the
existing library (Cambie-Yan = inversion counts in *powers* over all of S_n with
n≥2k+1; this = inversion/statistic expectations on *conjugacy classes*, exact for
all n, no power condition).  Both point at the same gap-affine mechanism from two
different, complementary directions.
