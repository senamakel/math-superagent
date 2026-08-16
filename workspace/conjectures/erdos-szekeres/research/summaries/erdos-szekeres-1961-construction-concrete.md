# Erdős–Szekeres 1961 lower-bound construction — concrete statement

Source: P. Erdős and G. Szekeres, "On some extremum problems in elementary geometry",
Ann. Univ. Sci. Budapest. Eötvös Sect. Math. 3-4 (1960/61) 53–62.
Held full text: `research/sources/erdos-szekeres-1961-on-some-extremum-problems-elementary-geometry-renyi.pdf.full.md`
Received May 20, 1960. Scanned PDF from Erdős archive (renyi.hu/~p_erdos/1960-09.pdf).

## What this paper is

The canonical primary construction of the lower bound ES(n) ≥ 2^{n-2}: a set of
2^{n-2} points in general position in the plane containing **no convex n-gon**. This is
the obstruction every candidate upper-bound argument must respect (see problem.md).
It also settles two angle-extremum problems (Theorem 1 & 2, §4) not relevant here.

## The cups-and-caps lemma it builds on

A sequence (xν,yν), x0<x1<...<xk, is *convex* of length k if the successive slopes
(yν−yν−1)/(xν−xν−1) are increasing; *concave* if decreasing. From the 1935 paper:
f(k,l) := least number forcing a concave k-sequence or a convex l-sequence equals
C(k+l−2, k−2)... (the paper states it; note f(k,l)=C(k+l−4,k−2)+1 in modern normalisation).
The paper constructs an explicit set S_{k,l} of f(k,l) points with no concave
k-sequence and no convex l-sequence, via an inductive function g_{kl}(x) (the "S_{k,l}"
construction: monotone increasing, all slopes positive).

## The 2^{n-2}-point construction (Section 2, main result)

Decompose 2^{n-2} = Σ_{k=1}^{n-1} C(n−2, k−1) (binomial row (n−2)).

For k=1,...,n−2 set a_k = C(n-2, k-1). Define subsets S_k (k=1,...,n−1):
- S_1 consists of the single point (1,0).
- S_{k+1} = S'_{k,n−k} + vertical translation by (n−k)a_k − Σ_{i=1}^k a_i, where S'_{k,l}
  is a copy of the cups/caps-extremal set with parameters (k, n−k).

Then S = ⋃_{k=1}^{n−1} S_k has |S| = Σ C(n−2,k−1) = 2^{n−2} points.

**Why no convex n-gon:** For points on the convex hull the paper shows:
- within each S_k all slopes are positive, so a convex polygon meeting S_k in more
  than one point is impossible in that block (a block contributes one vertex at most);
- the slopes of lines joining S_k to S_{k+1} are all in (−1/(n−k+·), −1/(n−k−·)),
  i.e. negative and steeply ordered across blocks;
- hence a convex polygon using blocks S_{k1},...,S_{kr} (k1<...<kr) has at most
  k1 + (kr−k2−1) + (n−kr) = n−1 points.

So every convex polygon in S has fewer than n sides. Combined with ES(n) ≤ C(2n−4,n−2)+1
(upper) this gives 2^{n−2} ≤ ES(n) ≤ C(2n−4,n−2)+1, conjectured sharp.

## Realizability / coordinates

The paper gives the construction geometrically/inductively. Duque–Fabila-Monroy–
Hidalgo-Toscano (arXiv:1602.03075, held) show it can be realized on an integer grid
of size O(n² log³ n). For the run's oracle, use the concrete induction with the c_{kl}
translation amounts so all coordinates are integers where stated.

```claim
id: es1961-construction-held
answers: full-text-faithful-b96b
statement: The explicit 2^{n-2}-point planar construction with no convex n-gon (Erdős–Szekeres lower bound ES(n) ≥ 2^{n-2}) is concretely articulated in the primary source: S = ⋃_{k=1}^{n-1} S_k with |S_k| = C(n-2,k-1), each S_k a positive-slope cups/caps-extremal block, consecutive blocks separated by a strict negative-slope band, so any convex polygon has ≤ n-1 vertices.
hypotheses: points in general position; definition of convex/concave sequence of given length; the f(k,l) cups/caps lemma from the 1935 paper.
holds-here: yes — this is exactly the lower-bound construction every upper-bound proof must respect.
status: checked against primary full text (renyi.hu/~p_erdos/1960-09.pdf), lines 135-220.
bearing: gives the canonical lower-bound witness set for the oracle at n=5,6,7; any candidate upper-bound argument must fail on this set.
anchor: research/sources/erdos-szekeres-1961-on-some-extremum-problems-elementary-geometry-renyi.pdf.full.md
```

## Verification note for this run

The oracle must confirm: (a) the S_5 / S_6 constructions (n=5 → 8 points, n=6 → 16
points) contain no convex 5-gon / 6-gon respectively, with exact integer or rational
coordinates; (b) ES(4)=5, ES(5)=9 via the checker. This source fixes what "the
Erdős–Szekeres construction" means concretely — field the run's witness set against it.
