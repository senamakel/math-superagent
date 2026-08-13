> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/harrison-mudgal-schmidt-sum-product-bremner-2026.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/2603.06483 | converted from PDF -->

## What it claims

Abstract. In this paper we combine methods from additive combinatorics and Diophan-
tine geometry to study the generalised sum-product phenomenon in algebraic groups. As
an application of this circle of ideas, we resolve a conjecture of Bremner on arithmetic pro-
gressions in coordinates of elliptic curves, along with various other generalisations studied
in the literature.
We also prove a uniform Bourgain–Chang-type sum-product estimate for general 1-
dimensional algebraic groups G over C. Using these ideas, we provide an alternative solution
to a problem of Bays–Breuillard. Furthermore, we show an Elekes–Szab´o type result in
the same setting for sets with small doubling, improving upon an earlier result of Bays–
Breuillard when G is not Ga. Our power saving here can be shown to be quantitatively
optimal.
We use a combination of deep, classical results in Diophantine geometry due to David–
Philippon, Laurent and Evertse–Schmidt–Schlickewei along with the recent breakthrough
work on the weak Polynomial Freiman–Ruzsa conjecture over integers due to Gowers–
Green–Manners–Tao.
 1.…

Ma…

## Statements it makes

Theorem 1.1. There is an effectively computable constant C ≥ 1 with the following prop-
erty. Let E be an elliptic curve in Weierstrass form

Conjecture 1.2. For any g ∈ N, any ε > 0 and any set A ⊆ C, one should have

Theorem 1.3. Given integers k ≥ 1 and d ≥ 2, there exists an integer g ≥ 1 such that
the following holds. Let G and H be algebraic groups of dimension 1, and let C1, · · · , Cg be
correspondences of degree d between G and H. Suppose no Ci is a translate of an algebraic
subgroup, and suppose that G is not isomorphic to Ga. Then for all finite, non-empty sets
A ⊆ G, one has max{|gA|, |C1(A) + · · · + Cg(A)|} ≫d,k |A|
k.

Corollary 1.4. For all integers k ≥ 2, there exists an integer g ≥ 2 such that the following
holds. For any non-constant φ1, . . . , φg ∈ C[x] with degree at most d and any finite set
A ⊆ C, one has max{|A
(g)|, |φ1(A) + · · · + φg(A)|} ≫d,k |A|k.

Theorem 1.5. Let G be a connected algebraic group over C of dimension 1. Suppose that
G is not isomorphic to Ga. Let A ⊆ G be a finite set such that |A + A| ≤ K|A| for some
K ≥ 1. Then for any irreducible subvariety V ⊆ G
g, that is not a translate of an algebraic
subgroup of Gg, one has
 |V ∩ A
g| ≪g,deg(V) K C + |A|dim(V)−1,

Definition 1.7. Let G be a 1-dimensional, connected algebraic group over C, and let B be
a projective variety of positive dimension. Let π1 : Gg × B → G
g and π2 : Gg × B → B be
the canonical projection maps. We call an irreducible subvariety V ⊆ Gg × B degenerate,
if there exists a connected algebraic group H ⊆ G
g of positive dimension, and a proper
subvariety W ⊊ Gg/H × B such that
 V = π−1
H (W),

Theorem 1.8. Let G, B, π1 and π2 be as in Definition 1.7, with G not isomorphic to Ga.
Let V ⊆ G
g × B be non-degenerate of dimension g and degree d, and such that π1 and π2
restricted to V are dominant. Let A ⊆ G be a finite, non-empty set such that |A+A| ≤ K|A|.
Then for all X ⊆ A, we have

Theorem 2.1. For all integers d ≥ 1 and g ≥ 2, there is a positive constant 0 < c(d, g) < 1
with the following property. Let C1, · · · , Cg be correspondences of degree d between algebraic
groups G and H of dimension 1. Suppose no Ci is a translate of an algebraic subgroup and

Corollary 2.2. For all integers d ≥ 1 there exists a constant D = D(d) with the following
property. Let G be either Gm or an elliptic curve E, and let C be a correspondence of degree
at most d between G and an algebraic group H of dimension 1, that is not the translate of
an algebraic subgroup. Then for any subgroup Γ ⊆ G(C) of rank r, a proper generalised
arithmetic progression P of rank k in C(Γ) satisfies

Theorem 1.1 follows in a straightforward manner from the above result, see §7. Corollary
2.2 also gives a more general and uniform version of [21, Theorem 6.1].
A nice aspect of our upper bound is that it is completely independent of the rank k of
the progression. Moreover, generalised…


*[further statements in the full text]*

*[digest of a 84544 character source; every section, statement, and proof in full at `research/sources/harrison-mudgal-schmidt-sum-product-bremner-2026.full.md`]*
