> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/bernardi_deformations_braid_arrangement_trees.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/1604.06554 | converted from PDF -->

## What it claims

Abstract. We establish general counting formulas and bijections for deformations
of the braid arrangement. Precisely, we consider real hyperplane arrangements such
that all the hyperplanes are of the form xi − xj = s for some integer s. Classical
examples include the braid, Catalan, Shi, semiorder and Linial arrangements, as well
as graphical arrangements. We express the number of regions of any such arrange-
ment as a signed count of decorated plane trees. The characteristic and coboundary
polynomials of these arrangements also have simple expressions in terms of these
trees.
We then focus on certain “well-behaved” deformations of the braid arrangement
that we call transitive. This includes the Catalan, Shi, semiorder and Linial ar-
rangements, as well as many other arrangements appearing in the literature. For
any transitive deformation of the braid arrangement we establish a simple bijection
between regions of the arrangement and a set of labeled plane trees deﬁned by local
conditions. This answers a question of Gessel.

1. Introduction

In this article we establish enumerative…

## Statements it makes

Theorem 3.4. Let S be a ﬁnite set of integers and n be a positive integer. The number
of regions of the hyperplane arrangement AS(n) is

Theorem 3.8. If S is transitive, then regions of the hyperplane arrangement AS(n)
are equinumerous to the trees in TS(n).

Theorem 3.8 is an easy consequence of Theorem 3.4 and the following lemma.

Lemma 3.11. Suppose that the set S is transitive. In this case, a cadet sequence
(v1, . . . , vk) is an S-cadet sequence if and only if for all i ∈ [k − 1],
(*) if lsib(vi+1) ∈ S ∪ {0} then vi < vi+1, and if − lsib(vi+1) ∈ S then vi > vi+1.

Theorem 4.2. The number of regions of the hyperplane arrangement AS is

Theorem 4.6. If S = (Sa,b)1≤a<b≤N is transitive, then the regions of AS are equinu-
merous to the trees in TS.

Theorem 5.2. Let ̂S = (Sa,b)1≤a≤b≤N be an (N +1
2 )-tuple of ﬁnite sets of integers, and
let m = max(|s|, s ∈ ∪Sa,b). Then P̂S(q, y, t) is related to boxed trees by

Theorem 6.3. The generating function of coboundary polynomials P̂S(q, y, t) (deﬁned
by (5.3)) is equal to ̃P̂S(y, t)−q, where ̃P̂S(y, t) is the unique series in Q[y][[t1 . . . , tN ]]
satisfying

Proposition 6.6. If S ⊆ Z is transitive, and m = max(|s|, s ∈ S) then

Corollary 6.8. If [m] ⊆ S ⊂ [−m..m] and {s < 0, s /∈ S} is closed under addition,
then

Corollary 6.9 ([43]). If S ⊆ Z satisﬁes 0 ∈ S, {−s, s ∈ S} = S, and N \ S is closed
under addition, then for all n > 0,

Theorem 6.10. Suppose ̂S = (Sa,b)1≤a≤b≤N is multi-transitive. Let Γ1(x, t), . . . , ΓN (x, t)
be the series deﬁned by the system of linear equations
(6.12)

Corollary 6.12. Suppose that ̂S = (Sa,b)1≤a≤b≤N is multi-transitive, and that for all
1 ≤ a ≤ b ≤ N , the set Sa,b contains 0 and satisﬁes {−s, s ∈ Sa,b} = Sa,b. Then for
all n ̸= (0, . . . , 0),

Corollary 6.12 is an application of the multivariate Lagrange inversion formula [21,
24] that we now recall for the readers’ convenience.

Lemma 6.14 (Lagrange inversion formula). Let t = (t1, . . . , tN ) be indeterminates. Let
g1(t), . . . , gN (t) be series in C[[t]] with non-zero constant terms. Let f1(t), . . . , fN (t) be
the unique series in C[[t]] such that for all i ∈ [N ] fi(t) = tigi(f1(t), . . . , fN (t)). Then
for all a ∈ [N ] and for all tuples n = (n1, . . . , nN ) ∈ NN ,

Corollary 6.15. Suppose that ̂S = (Sa,b)1≤a≤b≤N is multi-transitive, and that for some
a ∈ [N ], Sa,a contains 0 and satisﬁes {−s, s ∈ Sa,a} = Sa,a. Let ̂S′ be the same tuple
as ̂S except Sa,a is replaced by Sa,a \ {0}. Then,

Corollary 6.16. Suppose that ̂S = (Sa,b)1≤a≤b≤N is multi-transitive, and that for all
a < b, Sa,b = S for some set S containing 0 and such that {−s, s ∈ S} = S. Then

Lemma 7.1. Let n ∈ N, and let S = (Su,v)1≤u<v≤n be an (n
2)-tuple of ﬁnite sets of
integers, and let m = max(|s|, s ∈ ∪Su,v). The coboundary polynomial of AS is

Lemma 7.3. The generating functions P̂S(q, y, t) and

Lemma 7.5. Let
ÛS(y, t) = ∑

Claim 7.6.…


*[further statements in the full text]*

*[digest of a 124592 character source; every section, statement, and proof in full at `research/sources/bernardi_deformations_braid_arrangement_trees.full.md`]*
