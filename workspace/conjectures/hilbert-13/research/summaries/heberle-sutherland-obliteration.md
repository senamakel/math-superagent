> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/heberle-sutherland-obliteration.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/2110.08670 | converted from PDF -->

## What it claims

For each n, let RD(n) denote the minimum d for which there exists a formula for the general polynomial
of degree n in algebraic functions of at most d variables. In this paper, we recover an algorithm of Sylvester
for determining non-zero solutions of systems of homogeneous polynomials, which we present from a
modern algebro-geometric perspective. We then use this geometric algorithm to determine improved
thresholds for upper bounds on RD(n).

Contents

1 Introduction 1

2 Resolvent Degree, Polar Cones, and Tschirnhaus Transformations 3
2.1 Resolvent Degree . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
2.2 Polar Cones and k-Polar Points . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
2.3 Tschirnhaus Transformations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5

3 The Obliteration Algorithms 6
3.1 The Geometric Obliteration Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
3.2 Sylvester’s Obliteration Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . .…

## Statements it makes

Theorem 1.1. (Upper Bounds on Resolvent Degree)

Lemma 2.3. (Properties of Resolvent Degree)

Lemma 2.5. (Bertini’s Lemma for Hypersurfaces)
Let H ⊆ Pr
K be a hypersurface and P ∈ H(K). Then, C(H; P ) ⊆ H is a cone with vertex P .

Lemma 2.7. (Bertini’s Lemma for Intersections of Hypersurfaces)
Let V ⊆ Pr
K be an intersection of hypersurfaces and P ∈ V (K). Then, C(V ; P ) ⊆ V is a cone with vertex P .

Lemma 2.9. (Polar Point Lemma)
Let V ⊆ Pr
K be an intersection of hypersurfaces and let (P0, . . . , Pk) be a k-polar point of V . Then,
Λ(P0, . . . , Pk) ⊆ Ck(V ; P0, . . . , Pk−1) ⊆ V is a k-plane.

Lemma 2.9 yields that every k-polar point determines a k-plane, hence Remark 2.13 yields that it will
suﬃce to determine k-polar points on the Tschirnhaus complete intersections τ ◦
1,...,d.

Lemma 3.5. (The Reduction Lemma)

Corollary 3.8. (Geometric Formula of Reduction)

Proposition 3.10. (The Obliteration Proposition)

Corollary 3.12. (Geometric Formula of Obliteration)

Proposition 3.14. (Minimal vs. Geometric Dimension Bound)

Proposition 3.15. (Sylvester’s Formula of Obliteration)

Theorem 4.1. (Theorem 1.3 of [Sut2021C])
The function G(m) of [Sut2021C, Deﬁnition 3.26] has the following properties:

Proposition 3.10 yield that
 g(V ) = g (
V Syl
1 ) = · · · = g (
V Syl
d−3) = g (V Syl
d−2) ,

Theorem 4.6. (Bounds from the Geometric Obliteration Algorithm)

Lemma 4.7. (Lower Approximation)

Corollary 4.8. (Lower Bound for Ξ(m, d))
Let d ≥ 4 and m ≥ d + 2. Then,
 Ξ(m, d) ≥
 ⌈
4 ( m − d − 1
2
 )2d−4⌉
 .

Corollary 4.9. (The New Bounding Function)
Let G
′ : Z≥2 ! Z≥1 be the function with

Theorem 4.6 was proved using a consequence of the geometric obliteration algorithm, namely that r(V ) ≤
g(V ) for any intersection of hypersurfaces V . Further examination of the relationship between r(V ) and g(V )
is of interest.

Algorithm 5.1. (The Geometric Obliteration Algorithm)

Lemma 5.2. (Obliterating Quadrics)

Lemma 5.3. (Obliterating Cubics)

Lemma 5.4. (Obliterating Quartics)

Algorithm 5.5. (The Geometric Obliteration Algorithm with Computational Improvements)

Algorithm 5.6. (The Geometric Obliteration Algorithm for Cm−d−1(τ1,...,d; P0, . . . , Pm−d−1))

*[digest of a 76525 character source; every section, statement, and proof in full at `research/sources/heberle-sutherland-obliteration.full.md`]*
