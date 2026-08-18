> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/sutherland-upper-bounds-resolvent-degree.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/2107.08139 | converted from PDF -->

## What it claims

For each n, let RD(n) denote the minimum d for which there exists a formula for the general polynomial
of degree n in algebraic functions of at most d variables. In 1945, Segre called for a better understanding
of the large n behavior of RD(n). In this paper, we provide improved thresholds for upper bounds on
RD(n). Our techniques build upon classical algebraic geometry to provide new upper bounds for small n
and, in doing so, ﬁx gaps in the proofs of A. Wiman and G.N. Chebotarev in [Wim1927] and [Che1954].

Contents

1 Introduction 1

2 Polar Cones 3
2.1 An Introduction to Polar Cones . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
2.2 Resolvent Degree . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
2.3 Iterated Polar Cones and k-Polar Points . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7

3 New Upper Bounds on RD(n) 9
3.1 Tschirnhaus Transformations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
3.2 New Bounds From Iterated Polar Cones . . . . . . . . . . . . . . . . . . . . .…

## Statements it makes

Theorem 1.3. (Key Properties of G(m))
The function G(m) of Deﬁnition 3.26 has the following properties:

fact, which we include as Lemma 2.5 and refer to as Bertini’s Lemma (for Hypersurfaces), since the reference
Segre gives for this fact is [Ber1923].

Lemma 2.5. (Bertini’s Lemma for Hypersurfaces)
3

Lemma 2.8. (Technical Lemma)
Let P, Q ∈ Pr(K) and f ∈ K[x0, . . . , xr] be a homogeneous polynomial of degree d. Applying a projective
change of coordinates as necessary, we assume that

Lemma 2.11. (Bertini’s Lemma for Intersections of Hypersurfaces)
Let V = V(f1, . . . , fn) ⊆ Pr
K be an intersection of hypersurfaces and P ∈ V (K). Then, C(V ; P ) is a cone
with vertex P which is contained in V .

Lemma 2.18. (Upper Bound on RD(L/K))
Let L/K be a degree ℓ ﬁeld extension. Then, RD (L/K) ≤ RD(ℓ).

Proposition 2.19. (Determining Rational Points over Extensions)
Let V ⊆ Pr
K be a degree d subvariety. Then, there is an extension L/K with RD(L/K) ≤ RD(d) over which
we can determine a rational point of V .

Lemma 2.24. (Polar Point Lemma)
Let V ⊆ Pr
K be an intersection of hypersurfaces and let (P0, . . . , Pk) be a k-polar point of V . Then,
L(P0, . . . , Pk) ⊆ V is a k-plane.

Proposition 2.26. (Type of a kth Polar Cone of an Intersection of Type (1, . . . , d))
Let V ⊆ Pr
K be an intersection of hypersurfaces of type (1, . . . , d) and take k ≥ 1. A kth polar cone
Ck(V ; P0, . . . , Pk−1) is of type
[d d − 1 d − 2 · · · 3 2 1
1 k + 1 (
k+2
2 ) · · · (
k+d−3
d−3 ) (
k+d−2
d−2 ) (
k+d−1
d−1 )
]

Proposition 2.27. (k-Polar Points Intersections of Quadrics)

Theorem 3.7. (The n − 6 Bound)
For n ≥ 21, RD(n) ≤ n − 6.
 10

Theorem 3.10. (The n − 7, . . . , n − 14 Bounds)
 11

Proposition 2.27 (with k = 4 and ℓ = 3) allows us to determine a 4-plane Λ1 ⊆ C(τ1,2,3,4; P0)2 ∩ C(τ1,2,3,4; P0)1

Theorem 3.16. (Theorem 1.6 of [Wal2008])
Fix d ≥ 3. When r and k are such that

Theorem 3.20. (Theorem 2.1 of [DM1998])

Lemma 3.22. (k-Planes on an Intersection of Hypersurfaces of Type (2, . . . , d))
Let d ≥ 3, and V ∈ S(2, . . . , d; r)(K) for some C-ﬁeld K. For any k ≥ 1, if r ≥ ϑ(d, k), then we can determine
a k-plane on V over an extension L/K with

Proposition 3.23. (Semi-Stability of Tschirnhaus Complete Intersections)
For each d ≥ 3 and n ≥ d + 2, τ1,...,d ∈ S(2, . . . , d; n − 2)(Kn).

Theorem 3.24. (Determining a Point on τ1,...,d+k)
Fix k, d ≥ 1. For n ≥ ϑ(d, k) + 3, we can determine a point of τ ◦
1,...,d+k ⊆ T n over an extension L/Kn with

Theorem 3.27. (Upper Bounds on RD(n))
For each m ≥ 1 and all n ≥ G(m), RD(n) ≤ n − m.

Theorem 3.28. (Upper Bound on the Growth Rate of RD(n))

Lemma 3.29. (Upper Bound on ϑ)
Fix m > d ≥ 4. Then
 ϑ(d, m − d − 1) ≤ m − d − 2 + (m
d
 ).

Corollary 3.30. (Upper Bound on Parameter Space Dimension)
Fix m > d ≥ 4. Then,

Lemma 3.32. (Bound on log(Cd))
For each d ≥ 1, it follows that
 log ( Cd
d + 1
 ) ≤ d + 3
2 .

Lemma 3.33.…


*[further statements in the full text]*

*[digest of a 92848 character source; every section, statement, and proof in full at `research/sources/sutherland-upper-bounds-resolvent-degree.full.md`]*
