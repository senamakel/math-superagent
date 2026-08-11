# Permutation Statistics on Conjugacy Classes (Campion-Loth et al, arXiv:2301.00898)

Distribution of permutation statistics on a SINGLE conjugacy class C_λ ⊆ S_n
(cycle type λ=(1^{a_1},2^{a_2},…)); elementary bijective proofs, no character theory.
Source: https://arxiv.org/abs/2301.00898 ; full text: [[../../L0.0/conjugacy_class_statistics_body.full.md]]
and companion [[[conjugacy_class_statistics]]].

## Core — the inversion indicator (Lemma 4.7)
For 1≤i<j≤n, I_{i,j}(ω)=1 iff ω(i)>ω(j). Over C_λ:
  Prλ[I_{i,j}=1] = 1/2 + a_2/(n(n-1)) − a_1(a_1−1)/(2n(n-1))
      + (j−i−1)·[n − n·a_1 − a_1 + a_1² − 2·a_2] / [n(n−1)(n−2)].
Consequences (§4.1): depends ONLY on n, a_1=#fixed points, a_2=#2-cycles, and the
gap d=j−i — NOT on absolute positions (translation invariance) — and is AFFINE
(linear) in d. This is the *proved* version of the run's empirical
f_n(k)=#{(π,i):(π^i)(k)<(π^i)(0)}=A_n+(k−1)B_n (translation-invariant, arithmetic
in the gap).

## Weighted statistics & moments
- Thm 4.8: any X=Σ_{i<j} wt(i,j)·I_{i,j} (des, maj, inv are such) has
  Eλ[X]=C_1(n,a_1,a_2)·α_n(X)+C_2(n,a_1,a_2)·β_n(X) with α_n=Σwt, β_n=Σ(j−i−1)wt
  (independent of λ). First moment of ANY weighted inversion statistic depends only
  on n,a_1,a_2. E.g. Eλ[inv]=(3n²−n+2a_2−a_1²+a_1−2n·a_1)/12.
- Higher moments (Thms 1.3,1.5,7.16,7.26, Prop 7.28): for a statistic over a
  constraint set of size m, Eλ[X^k] is independent of λ when every part of λ ≥ mk+1;
  for symmetric stats each is a poly in n of degree ≤mk; Eλ[inv^k] degree-2k, leading
  coeff 4^{−k}; class averages ↔ S_n averages via centralizer/class identity (eq 6.1).

## Relevance to THIS run
The run (memory.md) reduced Q(n) to A_n,B_n from f_n(k)=A_n+(k−1)B_n. This source
proves the analogous gap-affine, translation-invariant per-inversion probability on
each conjugacy class, with slope/intercept controlled by a_1,a_2 of π's cycle type —
a concrete summation route to closed forms for A_n,B_n the run had not closed.

## Caveat
Fixed permutation statistic on a conjugacy class ONLY; does NOT give the sum of
Lehmer/rank over the cyclic subgroup {π^i} of one permutation — that remains the
unresolved core. Complements [[cambie_yan_html]] (inversions in powers, n≥2k+1) from
the other direction.
