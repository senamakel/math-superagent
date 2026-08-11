# Campion Loth, Levet, Liu, Stucky, Sundaram, Yin, "Permutation Statistics in Conjugacy Classes of the Symmetric Group" (arXiv:2301.00898) — superseded duplicate

This file holds the raw arXiv abstract-page HTML for arXiv:2301.00898. It is
**superseded**: the full curated summary is `conjugacy_class_statistics_body.md`
(pointing at `L0/conjugacy_class_statistics_body.full.md` for the complete text),
and every substantive claim lives there. The abstract page adds only bibliographic
data:

- Authors: Campion Loth, Levet, Liu, Stucky, Sundaram, Yin. math.CO / math.PR 05A05.
- v1 2 Jan 2023, v2 17 May 2023; DOI 10.48550/arXiv.2301.00898.
- Abstracts: introduces weighted inversion statistics and studies their distribution
  on each conjugacy class; explicit first moments per class; higher moments independent
  of the conjugacy class when cycle lengths are large (Fulman-style, via permutation
  constraints).

## What the source establishes (repeated here so this file is self-sufficient)

Lemma 4.7 — per-conjugacy-class pair-inversion probability on C_λ (λ=(1^{a_1},2^{a_2},…)):

  Pr_λ[I_{i,j}=1] = 1/2 + a_2/(n(n−1)) − a_1(a_1−1)/(2n(n−1))
      + (j−i−1)·[n − n·a_1 − a_1 + a_1² − 2·a_2] / [n(n−1)(n−2)]

— depends only on n, a_1=#fixed, a_2=#2-cycles and the gap d=j−i (translation
invariance), and is **affine in d**. Theorem 4.8: any weighted inversion statistic
X=Σ_{i<j}wt(i,j)I_{i,j} has E_λ[X] = C_1(n,a_1,a_2)α_n(X) + C_2(n,a_1,a_2)β_n(X), with
α,β independent of λ. This is the proved analogue of the run's empirical gap-affine
f_n(k)=A_n+(k−1)B_n. **Not** a sum over the cyclic subgroup {π^i}.

See `conjugacy_class_statistics_body.md` for full implications and caveats.
