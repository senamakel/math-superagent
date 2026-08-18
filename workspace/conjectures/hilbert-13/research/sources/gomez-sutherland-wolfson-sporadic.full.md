<!-- source: https://arxiv.org/pdf/2310.09375 | converted from PDF -->

arXiv:2310.09375v2  [math.AG]  27 Feb 2024
Generalized Versality, Special Points, and Resolvent Degree for the
Sporadic Groups

Claudio G´omez-Gonz´ales, Alexander J. Sutherland, and Jesse Wolfson
∗

Abstract

Resolvent degree is an invariant measuring the complexity of algebraic and geometric phenomena,
including the complexity of ﬁnite groups. To date, the resolvent degree of a ﬁnite simple group G has
only been investigated when G is a cylic group; an alternating group; a simple factor of a Weyl group
of type E6, E7, or E8; or PSL (2, F7). In this paper, we establish upper bounds on the resolvent degrees
of the sporadic groups by using the invariant theory of their projective representations. To do so, we
introduce the notion of (weak) RD
≤d
k -versality, which we connect to the existence of “special points” on
varieties.

Contents

1 Introduction 1

2 Background 4
2.1 Torsors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
2.2 Accessory Irrationalities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
2.3 Resolvent Degree . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
2.3.1 Resolvent Degree for Varieties, Fields, and Algebraic Groups . . . . . . . . . . . . . . 6
2.3.2 Resolvent Degree of a Functor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8

3 Generalized Versality and Special Points 10

4 Resolvent Degree and the Sporadic Groups 16
4.1 Upper Bounds on the Resolvent Degree of the Sporadic Groups . . . . . . . . . . . . . . . . . 16
4.2 Context for Sporadic Group Bounds . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21

A Power Series Expansions of Molien Series 23

1 Introduction

What is the least d for which a solution of the general degree n polynomial admits a formula using only
(algebraic) functions of d or fewer variables? As Abel realized, the general degree n polynomial has Galois
group Sn and this question, in modern language, asks for the resolvent degree of the symmetric group,
denoted RDC(Sn) = RDC(An) =: RDC(n),

an invariant ﬁrst introduced independently by Brauer [Bra1975] and Arnol’d-Shimura [AS1976]. To the best
of our knowledge, Klein was the ﬁrst to consider this question for other ﬁnite groups, most notably the
group PSL (2, F7) [Kle1879]. Note that for a ﬁnite group G with Jordan-H¨older decomposition {G1, . . . , Gs},
[FW2019, Theorem 3.3] yields that

RDk(G) ≤ max {RDk(G1), . . . , RDk(Gs)} ,

∗The third author was supported in part by NSF Grant DMS-1944862.

1

with equality if every Gj can be realized as a subgroup of G.1

Following Klein and the classiﬁcation of ﬁnite simple groups, one is led to the following question [FW2019,
Problem 3.5]:

Problem 1.1 (RDk(G) for Finite Simple G). Compute the resolvent degree of all ﬁnite simple groups G.

To date, Problem 1.1 has only been addressed by providing upper bounds on RDk(G) when G is a cyclic
group (in which case RDk(G) ≡ 1), an alternating group (see [HS2023, Sut2021, Wol2021], or [Ham1836,
Hil1927, Kle1879, Kle1884, Kle1887, Kle1905, Seg1945, Tsc1683] for classical references), when G is a simple
factor of a Weyl group of type E6, E7, or E8 [FW2019, FKW2023, Rei2022], or when G = PSL (2, F7) (see
[Kle1879] for the classical reference or [FKW2023] for a modern version).
The Classiﬁcation of Finite Simple Groups says that a ﬁnite simple group G falls into one of four categories:

1. G is cyclic of prime order;

2. G is an alternating group (An, n ≥ 5);

3. G is a simple group of Lie type (of which there are 16 families); or

4. G is one of 26 ﬁnite simple groups that do not belong to one of the inﬁnite families above.

The 26 groups in (4) are known as the sporadic groups. In this paper, we investigate Problem 1.1 by giving
upper bounds on RDk(G) for all sporadic groups G. For each group G, we use the invariant theory of a
projective representation over C of minimal dimension to construct a complex G-variety XG with the property
that RDk(G) ≤ dimC(XG). For G one of the Mathieu groups M11, M12, M23, M24, we prove nothing new: the
projective representation in these cases is just the projectivization of the permutation representation, XG is
the vanishing locus of the ﬁrst four (M11, M12) or ﬁve (M23, M24) elementary symmetric polynomials, and the
bounds on RDk(G) follow from the bounds on RDk(Sn) which appear previously in the literature (with S11
and S12 in [Seg1945], and S23 and S24 in [Sut2021]). Our primary interest is thus the remaining 22 sporadic
groups. Here, our bounds appear to be genuinely new, and we obtain them by proving that the variety XG
is “RD
≤d
C -versal” for d < dimC(XG) (see Deﬁnition 3.2, Lemma 3.6, and Theorem 4.7 for the construction of
XG), from which the bound on RDk(G) follows by [FW2019, Proposition 3.10]. More explicitly, we have:

Corollary 1.2 (Appears as Corollary 4.9: Explicit Form of Theorem 4.7). For any ﬁeld k, we have

RDk(J2) ≤ 5, RDk(M24) ≤ 18, RDk(He) ≤ 48, RDk(Fi23) ≤ 776,

RDk(M11) ≤ 6, RDk(HS) ≤ 18, RDk(J1) ≤ 51, RDk(Fi24’) ≤ 779,
RDk(M12) ≤ 7, RDk(McL) ≤ 19, RDk(Fi22) ≤ 74, RDk(J4) ≤ 1328,

RDk(M22) ≤ 8, RDk(Co3) ≤ 20, RDk(HN) ≤ 129, RDk(Ly) ≤ 2475,

RDk(Suz) ≤ 10, RDk(Co2) ≤ 20, RDk(Th) ≤ 244, RDk(B) ≤ 4365,
RDk(J3) ≤ 16, RDk(Co1) ≤ 21, RDk(O’N) ≤ 338, RDk(M) ≤ 196874.

RDk(M23) ≤ 17, RDk(Ru) ≤ 26,

The proof of Theorem 4.7 is comprised of two distinct parts, which are set up in Sections 3 and 4,
respectively. First, in [FW2019, Deﬁnition 3.8], notions of solvable versality and RDk-versality for ﬁnite
groups G were introduced. In [FKW2023], this was generalized by deﬁning 1) a notion of a class of accessory
irrationalities E [FKW2023, Deﬁnition 4.1] and, given such a class E, by deﬁning 2) a notion of E-versality
[FKW2023, Deﬁnition 4.4]. A connection to resolvent degree was brieﬂy discussed in [FKW2023, Paragraph
4.1.3 and Lemma 4.9], along with a discussion of historical roots of these notions of generalized versality and
a call to better understand them [FKW2023, Remark 4.10]. We build on this framework here, introducing
new examples of classes of accessory irrationalities E = RD≤d
k (“accessory irrationalities of resolvent degree
at most d”) which have been implicit in the literature, and broadening [FKW2023, Deﬁnition 4.4] and the
attendant lemmas to allow for arbitrary algebraic groups G.
Second, Duncan and Reichstein [DR2015, Theorem 1.1 (a,b)] reframed versality in terms of rational
points on twisted forms. Building on this, we connect the above generalizations of versality to the existence

1In fact, it seems reasonable to expect that the inequality can be made into an equality without assumptions on G.

2

of “special points”—a catch-all term we use to encompass points deﬁned via any speciﬁed class E of accessory
irrationalities—as in Theorem 1.3. This perspective, with E = RD
≤d
k , is implicit in [Rei2022, Lemma 14.5],
and our hope is that by making it explicit, we can make it more widely known and used. Concretely, for a
ﬁeld K and a class of accessory irrationalities E, let K E denote an E-closure of K (see Section 2.2).

Theorem 1.3 (Appears as Theorem 3.9: Generalized Versality and Special Points). Let G be an algebraic
group over k and let X be an irreducible, generically free, quasiprojective G-variety. Let E be a class of
accessory irrationalities. Then:

1. X is weakly E-versal if and only if for every G-torsor T → Spec(K) with K ﬁnitely generated over k,
T X (
K E) ̸= ∅.

2. If G is smooth, X is E-versal if and only if for every G-torsor T → Spec(K) with K ﬁnitely generated
over k, K E-points are dense in T X.

In Section 4, we apply the framework of E-versality outlined in Section 3 to the 22 sporadic groups not
equal to M11, M12, M23, or M24. More speciﬁcally, we use the invariant theory of a projective representation
for each sporadic group G to construct a complex variety XG which we then show is RD
≤dG
C -versal for some
dG ≤ dimC (XG). Results of Reichstein, namely [Rei2022, Theorems 1.2, 1.3], then allow us to conclude the
upper bounds on RDk(G) for all ﬁelds k.

Outline of the Paper The remainder of this paper proceeds as follows. In Section 2, we introduce the
relevant background on torsors (Section 2.1), accessory irrationalities (Section 2.2) and resolvent degree
(Section 2.3). In Section 3, we recall the framework of E-versality and connect it to the existence of E-points.
In Section 4, we establish upper bounds on the resolvent degree of the sporadic groups (Section 4.1) and
understand these bounds in terms of the prior literature (Section 4.2).

Supplementary Materials Some results in this paper rely on calculations performed with GAP [GAP2022]
and SageMath [Sag2022]. Along with this paper, we have included supplementary ﬁles which can be used to
verify all computations. They can be found on the arXiv submission of this paper, as well as at the following
web address:

https://www.alexandersutherland.com/research/RD-for-the-Sporadic-Groups .

In addition to the SageMath script, we have also included the relevant data and outputs as plain text ﬁles.
The supplementary ﬁles on the arXiv can be accessed by downloading the source package.

Correctness of Information for Sporadic Groups The computations for the Molien series (or the
coeﬃcients thereof) for projective representations of sporadic groups in this project rely on the GAP character
table library [Bre2013] of the computer algebra system GAP [GAP2022]. We refer the reader to [BMO2017] for
details on correctness, while noting the excerpt “all character tables contained in the ATLAS, incorporating
the corrections, and many more, are stored electronically in the character table library [Bre2013] of the
computer algebra system GAP [GAP2015].”

Conventions

1. We deﬁne a K-variety to be a quasiprojective scheme of ﬁnite type over K. We do not require varieties
to be reduced or irreducible.

2. For a collection of homogeneous polynomials {f1, . . . , fs} ⊆ K [x0, . . . , xn], we write V (f1, . . . , fs) for
the subvariety of Pn
K determined by the (scheme-theoretic) intersection f1 = · · · = fs = 0.

3. We denote the K-points of a variety X by X(K).

4. Unless otherwise speciﬁed, when we refer to an algebraic group, we mean an arbitrary algebraic group
(it need not be ﬁnite, linear, nor smooth).

5. Given a ﬁeld K, we denote a separable closure of K by K sep.

6. For maps between varieties, we denote regular morphisms by →, and rational maps by 99K.

3

Acknowledgements The authors would like to thank Aaron Landesman and Daniel Litt for helpful com-
ments on a draft, and Alice Silverberg for help with a reference. The authors thank the anonymous referee
for helpful comments and suggestions.

2 Background

In this section, we recall the necessary background on torsors, accessory irrationalities, and resolvent degree.
We ﬁx a ground ﬁeld k.

2.1 Torsors

Consider an algebraic group G over k, i.e. a group scheme of ﬁnite type over k. We refer the reader to
[Poo2017, Chapter 5] for a good summary and list of references for algebraic groups. For example, recall
that results of Chow and Conrad (see e.g. [Poo2017, Theorem 5.2.20]) show that G is automatically a quasi-
projective k-scheme. Let X be a quasiprojective G-variety over k. In this section, K always denotes a ﬁnitely
generated k-ﬁeld.

Deﬁnition 2.1 (G-Torsors). A right (respectively, left) G-torsor over X is a ﬂat morphism Y → X of
k-schemes such that G acts on Y on the right (respectively, left) by σ : G × Y → Y and such that the map

G × Y → Y ×X Y

(g, y) ↦→ (σ(g, y), y),

is an isomorphism. We say that the G-torsor Y → X is split if it admits a section; this is equivalent to its
class [Y ] in H 1(k, G) being trivial.

Next, we introduce twisted varieties.

Deﬁnition 2.2 (Twists). Let G be an algebraic group over k. Let T → Spec(K) be a G-torsor. G acts on
T × X diagonally and yields a G-torsor T × X → T X. We say T X is the twist of X by T .

Note that our assumption of quasiprojectivity of X implies that T X is well-deﬁned as the geometric quotient
of T × X by G; see [Poo2017, Section 5.12.5] for details when G is smooth, and [Flo2008, Proposition 2.12]
in general.
In Section 3, we will want to move interchangeably between torsors over ﬁnitely generated k-ﬁelds and
their integral models.

Deﬁnition 2.3 (Integral Models). Given a G-torsor T → Spec(K) over k, an integral model of T →
Spec(K) is a morphism Y → Y /G, where Y is a generically free G-variety with k (Y /G) = K, along with an
isomorphism Y ×Y /G Spec(K) ∼= T .2

For further background on G-torsors, we refer the reader to [Mil1980, Ch. 3, Sec. 4] and [Poo2017, Section
5.12] for general results and to [Rei2022, Section 10] for connections of G-torsors to essential dimension and
resolvent degree.

2.2 Accessory Irrationalities

Accessory irrationalities appear prominently in work of Klein [Kle1884] (see also [Kle1879, Kle1887, Kle1905]
and Chebotarev [Che1932, Che1934]). The ﬁrst formal deﬁnition of which we are aware appears in [FKW2023,
Deﬁnition 4.1] in the language of branched covers. We recall this here, introduce an equivalent formulation
in the language of ﬁeld extensions, give new examples of E, and introduce the notion of a closure of a ﬁeld
with respect to a class of accessory irrationalities (Deﬁnition 2.17).
Following [FKW2023, 4.1.1], we consider branched covers p : Y // X of normal k-varieties, i.e. dominant,
ﬁnite maps. More generally, we will use branched cover to refer to a generically ﬁnite, dominant rational

2Note that our assumption that k(Y /G) = K implies that Y /G is irreducible. In particular, all integral models are birational
to each other.
 4

map p : Y 99K X. Branched covers form a category in the usual fashion, and they are preserved under
pullback in the following sense: if f : X ′ // X is any map of normal k-varieties, then we denote by f ∗Y the
normalization of Y ×X X ′ and observe that f ∗p : f ∗Y // X ′ is again a branched cover.

Deﬁnition 2.4 (Deﬁnition 4.1 of [FKW2023]). Let k be a ﬁeld. Let Varν
k denote the category of normal
k-varieties. Let Bran: (Varν
k)
op // Cat

be the functor3 which sends a ﬁnite type normal k-scheme X to its category of branched covers. A class of
accessory irrationalities E is a subfunctor E ⊂ Bran such that

1. For any X, E(X) ⊂ Bran(X) is a full subcategory.

2. For any X, the identity X // X is in E(X).

3. E(X ∐ X ′) = E(X) × E(X ′).

4. If E, E′ ∈ E(X), then E ×X E′ ∈ E(X).

5. If U ⊂ X is a dense open, then E(X) // E(U ) is an equivalence of categories.

6. If E // X ′ // X are branched covers and if E // X is in E(X), then E // X ′ is in E(X ′).

For the present paper, and to make explicit the connection to the perspective in [Rei2022], we rephrase
this in the language of ﬁeld extensions.

Deﬁnition 2.5 (Deﬁnition 4.1 of [FKW2023] via Field Extensions). Let k be a ﬁeld, let Fields/k be the
category of ﬁelds over k, and let Fin : Fields/k // Cat

be the functor which sends a k-ﬁeld K to the category of ﬁnite, semi-simple commutative K-algebras.4 A
class of accessory irrationalities E is a subfunctor E ⊂ Fin such that:

1. For all K, E(K) ⊂ Fin(K) is a full subcategory.

2. For all K, we have K ∈ E(K).

3. If E, E′ ∈ E(K), then E ⊗K E′ ∈ E(K).

4. If K ֒→ L is a ﬁnite extension of k-ﬁelds, L ֒→ E is ﬁnite, and K ֒→ L ֒→ E is in E(K), then E ∈ E(L).

Lemma 2.6 (Equivalence of Deﬁnitions). Deﬁnitions 2.4 and 2.5 are equivalent: the assignment X ↦→ k(X)
induces an equivalence between the category of subfunctors of Bran satisfying the axioms of Deﬁnition 2.4
and the category of subfunctors of Fin satisfying the axioms of Deﬁnition 2.5.

Proof. Let E ⊂ Bran be a class of accessory irrationalities. By assumptions 3 and 5 of Deﬁnition 2.4, we see
that E is determined up to equivalence by its restriction to the sub-category of irreducible, aﬃne, normal
k-varieties. For any such X, we have a natural equivalence of categories

Fin (k(X)) ∼= {k(E) | E // X ∈ Bran(X)}.

Denote by (k ◦ E)(X) the full sub-category of Fin(k(X)) determined by E(X) under the above equivalence.
The assumptions of Deﬁnition 2.4 on E imply that k ◦ E satisﬁes the assumptions of Deﬁnition 2.5, as claimed.
It remains to show that any subfunctor E ⊂ Fin satisfying Deﬁnition 2.5 arises as above. Fix such a
subfunctor E ⊂ Fin. For X ∈ Varν
k, let ̃E(X) ⊂ Bran(X) be the full subcategory consisting of all branched
covers Y 99K X such that for any irreducible component Xi ⊂ X, the restriction Y |Xi 99K Xi has

k(Xi) ֒→ k(Y |Xi ) ∈ E(k(Xi)).

3We follow standard usage and do not distinguish between a functor and a pseudo-functor when the latter is the manifestly
appropriate notion given the target in question. Note that the natural isomorphisms required for pseudo-functoriality are
canonical in this case, as they come from the universal property of normalization and ﬁber product.
4N.b. Wedderburn’s theorem implies that any ﬁnite semi-simple commutative algebra over a ﬁeld is a ﬁnite product of ﬁnite
extensions of that ﬁeld.
 5

This deﬁnition ensures that ̃E ⊂ Bran satisﬁes Assumptions 3 and 5 of Deﬁnition 2.4. The remaining
assumptions follow from the corresponding assumptions of Deﬁnition 2.5, and by direct inspection, we see
that k ◦ ̃E ∼= E as claimed.

Motivated by classical examples in the literature (see Example 2.8), we introduce terminology for special
classes of accessory irrationalities.

Deﬁnition 2.7 (Saturation and Closure Under Extensions). Let E : Fields/k // Cat be a class of accessory
irrationalities.

1. We say E is saturated if for all ﬁnite extensions of k-ﬁelds K ֒→ L, that K ֒→ L ֒→ E is in E(K)
implies that L ∈ E(K).

2. We say E is closed under extensions if for all ﬁnite extensions of k-ﬁelds K ֒→ L, L ∈ E(K) and
E ∈ E(L) together imply that K ֒→ L ֒→ E is in E(K).

Example 2.8 (Example 4.3(3) of [FKW2023]).

1. Let Ab(K) be the category of ﬁnite semisimple commutative K-algebras which split as products of
abelian extensions of K. Then the assignment K ↦→ Ab(K) deﬁnes a saturated class of accessory
irrationalities which is not closed under extensions.

2. Let Sol(K) be the full subcategory of ﬁnite semisimple commutative K-algebras which split as products
of solvable extensions of K. Then the assignment K ↦→ Sol(K) deﬁnes a saturated class of accessory
irrationalities which is closed under extensions.

Note that Sol is the closure of Ab under extensions, i.e. it is the minimal class of accessory irrationalities
which contains Ab and is closed under extensions.

2.3 Resolvent Degree

Resolvent degree was ﬁrst deﬁned independently by Brauer [Bra1975] and Arnol’d-Shimura [AS1976] in the
context of ﬁeld extensions. The ﬁrst contemporary reference on resolvent degree is [FW2019]. We begin
by reviewing the deﬁnition of resolvent degree for algebraic groups, and then introduce the notion of the
resolvent degree of a functor.

2.3.1 Resolvent Degree for Varieties, Fields, and Algebraic Groups

We recall the deﬁnitions here and refer the reader to [FW2019, Wol2021, Rei2022] for more background.

Deﬁnition 2.9 (Essential Dimension of a Branched Cover of Varieties). Let Y 99K X be a branched cover
of k-varieties (i.e. a generically ﬁnite, dominant rational map). The essential dimension of Y 99K X over
k, denoted edk(Y 99K X), is the minimal d for which there exists

1. a branched cover ˜Z // Z with dimk Z = d,

2. a dense Zariski open U ⊂ X,

3. a map f : U // Z, and

4. an isomorphism f ∗ ˜Z ≃ Y |U over U .

Deﬁnition 2.10 (Resolvent Degree of a Branched Cover of Varieties). Let Y 99K X be a branched cover of
k-varieties. The resolvent degree of Y 99K X over k, denoted RDk(Y 99K X), is the minimal d for which
there exists a tower of branched covers
 Xr 99K · · · 99K X0 = X,

with a factorization Xr 99K Y 99K X such that edk(Xj 99K Xj−1) ≤ d for all 1 ≤ j ≤ r.

6

The deﬁnition of the resolvent degree of an extension of k-ﬁelds extends straightforwardly to the case
of ﬁnite, semisimple commutative algebras over k-ﬁelds, and the basic properties carry over as well. In
particular, we have the following example.

Example 2.11 (The class RD≤d
k ). Fix d ≥ 0. For a k-ﬁeld K, let RD
≤d
k (K) denote the category of all ﬁnite
semisimple commutative K-algebras A such that RDk(A/K) ≤ d. The proof of [FW2019, Lemma 2.5(2)]
shows that the assignment K ↦→ RD
≤d
k (K) is indeed functorial, while that of [FW2019, Lemma 2.7] shows
that it satisﬁes the deﬁnition of a saturated class of accessory irrationalities which is closed under extensions.

Reichstein extended the above notion of essential dimension in [Rei2000] as follows:

Deﬁnition 2.12 (Essential Dimension of a G-Variety). Let G be an algebraic group over k. Let X be a
generically free G-variety. The essential dimension of X 99K X/G is the least d such that there exists a
dominant, G-equivariant rational map X 99K Y with d = dim(Y /G).

Following [Rei2021, Rei2022], we build on this here.

Deﬁnition 2.13 (Resolvent Degree of a G-Variety). Let G be an algebraic group. Let X be a quasi-projective
G-variety over k. The resolvent degree of X 99K X/G is

RDk(X 99K X/G) = min {max{RDk(E 99K X/G), edk(X|E 99K E)}} .

where the minimum is over generically ﬁnite dominant maps E 99K X/G.

Remark 2.14. The above deﬁnition diﬀers slightly from that of [Rei2021, Rei2022]. We show in Lemma 2.27
below that it agrees with Reichstein’s.

Recall that a G-variety X is primitive if G acts transitively on the set of geometrically irreducible
components of X. A G-variety is generically free if the locus of points with trivial (scheme theoretic)
stabilizer is dense and open. We record the following elementary lemma for later use.

Lemma 2.15 (Faithful and Irreducible Implies Generically Free). Let G be a ﬁnite group and X an irreducible
G-variety. Then the action of G on X is generically free if and only if it is faithful.

Proof. That generically free implies faithful is immediate. For the converse, note that given g ∈ G \ {1}, the
(scheme theoretic) ﬁxed set X g ⊂ X is a closed subset, which is not all of X because the action is faithful. If
X is irreducible, then X cannot be written as the union of a ﬁnite number of proper closed subsets. Therefore,
X \ ⋃
g∈G\{1} X g is a non-empty open in which every point has trivial scheme theoretic stabilizer. As X is
irreducible, this open is dense, and thus the action is generically free.

Deﬁnition 2.16 (Resolvent Degree of an Algebraic Group). Let G be an algebraic group. The resolvent
degree of G over k is

RDk(G) := sup {RDk(X 99K X/G) | X is a primitive, generically free G-variety over k} .

In the course of investigating the resolvent degree of an algebraic group, it is often useful to pass to an
extension K ′/K of bounded resolvent degree, or more generally to an extension K ′/K in some speciﬁed class
of accessory irrationalities E; following [AS1976, Rei2022] we can formalize the maximal such extension as
follows.

Deﬁnition 2.17 (E-Closure). Let E : Fields/k // Cat be a saturated class of accessory irrationalities. Let
K be a k-ﬁeld and ﬁx an algebraic closure K ֒→ K. Consider the set

SE := {K ֒→ K ′ ֒→ K | K ′ ∈ E(K)}.

We deﬁne an E-closure of K to be the compositum

K E := K (SE ) ֒→ K.

We say that K is E-closed if K = K E. Note that, by deﬁnition, for any ﬁnite extension of k-ﬁelds
K ⊂ L ⊂ K, if L ∈ E(K) then L ⊂ K E . Conversely, because E is saturated, if L ⊂ K E, then L ∈ E(K).

7

Example 2.18 (Common E-Closures).

1. For E = Ab, K ֒→ K Ab is the usual abelian closure (i.e. maximal abelian extension).

2. For E = Sol, K ֒→ K Sol is the usual solvable closure.

3. For E = RD≤d
k , we write K (d) := K RD≤d
k . This closure was ﬁrst considered in [AS1976] and studied
in some detail recently in [Rei2022]. For d = 0, K = K (0). As radicals have resolvent degree 1, we
see K Sol ֒→ K (d) whenever d ≥ 1. If d ≤ d
′, then RD
≤d
k is a subfunctor of RD≤d′

k , and one sees that

K (d) ֒→ K(d′) as expected. For more details, see [Rei2022, Section 6].

2.3.2 Resolvent Degree of a Functor

Reichstein extended the notion of resolvent degree to “split” functors in [Rei2021, Section 8] (see also [Rei2022,
Section 7]). In this subsection, we extend this to a deﬁnition of resolvent degree for arbitrary functors
(Deﬁnition 2.22), and we show in Lemma 2.27 that this deﬁnition recovers Reichstein’s deﬁnition if the
functor is split. In particular, this establishes the equivalence of Deﬁnition 2.16 and Reichstein’s deﬁnition
of the resolvent degree of an algebraic group [Rei2022, Deﬁnition 10.1].
We begin by deﬁning the resolvent degree of a functor F : Fields/k // Sets, building on Merkurjev’s
deﬁnition of essential dimension in this context [BF2003].

Deﬁnition 2.19 (Merkurjev). Let F : Fields/k // Sets be a functor. Let K be a k-ﬁeld, and let α ∈ F (K).
Deﬁne the essential dimension of α by

edk(α) := min{tr. degk L | α ∈ Im(F (L) // F (K))}.

Deﬁne the essential dimension of F by

edk(F ) := sup
K,α∈F (K) edk(α).

Example 2.20 (Essential Dimension of Fin). Let F = Fin as above. Let K be a k-ﬁeld and let α : K ֒→ L
be a ﬁnite extension of K, and let Y 99K X be any branched cover of k-varieties such that

(k(X) ֒→ k(Y )) ∼= (K ֒→ L).

Tracing through the deﬁnitions, one immediately obtains that

edk(α) = edk(L/K) = edk(Y 99K X)

where the left-hand side denotes the quantity deﬁned in Deﬁnition 2.19, the middle term denotes the essential
dimension of a ﬁnite extension of k-ﬁelds as in [BR1997, Deﬁnition 2.1], and the right-hand side denotes the
quantity of Deﬁnition 2.9.

Also recall the ﬁeld theoretic formulation of Deﬁnition 2.10 [Bra1975], which by [FW2019, Propositon
2.4] is equivalent to Deﬁnition 2.10 under the assignment X ↦→ k(X):

Deﬁnition 2.21 (Brauer). Let K ֒→ L be a ﬁnite extension of k-ﬁelds. The resolvent degree of L over
K, RDk(L/K) is the minimal d for which there exists a ﬁnite tower of ﬁnite extensions of k-ﬁelds

K = K0 ֒→ K1 ֒→ · · · ֒→ Kr

and an embedding L ֒→ Kr over K with edk(Ki+1/Ki) ≤ d for all i.

Motivated by [FW2019, Proposition 2.13], we combine Brauer’s and Merkurjev’s deﬁnitions to obtain the
following.
 8

Deﬁnition 2.22 (Resolvent Degree of a Functor). Let F : Fields/k // Sets be a functor. Let K be a k-ﬁeld
and let α ∈ F (K). We deﬁne the resolvent degree of α by

RDk(α) := min
L/K ﬁnite max{RDk(L/K), edk(α|L)}

Deﬁne the resolvent degree of F by
 RDk(F ) := sup
K,α∈F (K) RDk(α).

Example 2.23 (Resolvent Degree of Fin and H 1(−, G)).

1. Consider the functor Fin : Fields/k // Sets. Let α : K ֒→ L be a ﬁnite extension of k-ﬁelds considered
as an element α ∈ Fin(K). Then, by inspection

RDk(α) = RDk(L/K)

where the left-hand side is as in Deﬁnition 2.22 and the right-hand side is as in Brauer’s Deﬁnition 2.21.

2. For an algebraic group G over k, consider the functor H 1(−, G) : Fields/k → Sets. For each K/k,
the elements of H 1(K, G) are isomorphism classes of G-torsors over Spec(K), where the local triviality
condition is with respect to the fppf topology. Given a G-torsor T // K with class α ∈ H 1(K, G), let
X 99K X/G be an integral model. By inspection, we see that

RDk(α) = RDk(X 99K X/G)

where the left-hand side is as in Deﬁnition 2.22 and the right-hand side is as in Deﬁnition 2.13. Similarly,

RDk(H 1(−, G)) = RDk(G),

i.e. for algebraic groups, the resolvent degree of H 1(−, G) agrees with Deﬁnition 2.16.

In [Rei2021], Reichstein deﬁnes a notion of resolvent degree for certain functors F : Fields/k //MarkedSets
taking values in pointed sets. Following the notation of [Rei2021], for such F and K a k-ﬁeld, let 1 ∈ F (K)
denote the distinguished element.

Deﬁnition 2.24 (Split Functors). A functor F : Fields/k // MarkedSets is split if for all K/k and all
α ∈ F (K), there exists a ﬁnite extension L/K such that α|L = 1 ∈ F (L). In such a case, we say that α is
split by L/K.

Deﬁnition 2.25 (Reichstein). Let F : Fields/k // MarkedSets be a split functor. Given α ∈ F (K), deﬁne
the split resolvent degree of α by

RDsp
k (α) := min{RDk(L/K) | α is split by L/K}

Deﬁne the split resolvent degree of F by

RDsp
k (F ) := sup
K,α∈F (K) RDsp
k (α).

Remark 2.26 (On Split Resolvent Degree).

1. Given a split functor F , we will continue to write RDk(F ) to denote the resolvent degree of F considered
as a functor F : Fields/k //MarkedSets //Sets (i.e. where we forget the distinguished element). Below
we will to show that RDk(F ) = RD
sp
k (F ) for any such F .

2. A motivating example of a split F is given by H 1(−, G) for G an algebraic group. As above, write
RDsp
k (G) := RDsp
k (H 1(−, G)). As Reichstein observes [Rei2021, Conjecture 17] (see also [Rei2022,
Conjecture 1.4]), a folklore conjecture implicit in work of Tits is that if G is a connected complex

9

algebraic group and K is a C-ﬁeld, then every G-torsor over K splits over a solvable extension L/K.
In particular, Tits’ conjecture implies that

RDsp
C (G) = RDC(G) ≤ 1

for every connected complex algebraic group G. Reichstein proves unconditionally [Rei2022, Theorem
1.1] that RDsp
C (G) ≤ 5.

3. The norm-residue isomorphism theorem implies that

RD
sp
k (H ∗(−; µn)) = RDk(H ∗(−; µn)) = 1

for every ﬁeld k of characteristic prime to n. In particular, torsion Galois cohomology cannot detect
RD > 1.

Lemma 2.27 (Equivalence of Split Resolvent Degree for Split Functors). Let F : Fields/k // MarkedSets
be a split functor. Then RD
sp
k (F ) = RDk(F ).

In particular, for G an algebraic group over k, Deﬁnition 2.16 agrees with [Rei2022, Deﬁnition 10.1].

Proof. For any k-ﬁeld K, edk(1K) = 0 by deﬁnition (since 1k|K = 1K ∈ F (K)). Therefore, the deﬁnitions
immediately give that RDk(F ) ≤ RDsp
k (F ).

We now show the opposite inequality. Observe that it suﬃces to prove that for all k-ﬁelds K and all α ∈ F (K),
we have RDsp
k (α) ≤ RDk(α).

By [Rei2022, Lemma 7.6(b)], edk(α) ≥ RD
sp
k (α).

But then, for any ﬁnite extension L/K, we have

max{RDk(L/K), edk(α|L)} ≥ max{RDk(L/K), RD
sp
k (α|L)}

= max{RDk(L/K), min{RDk(L′/L) | α|L is split by L′/L}}
= min{max{RDk(L/K), RDk(L′/L)} | α|L is split by L′/L}

≥ min{RDk(L′/K) | α is split by L′/K}
=: RDsp
k (α)

where the ﬁnal inequality follows from [FW2019, Lemma 2.7]. Minimizing the left hand side of the above
inequality over all ﬁnite extensions L/K, we obtain that

RDk(α) ≥ RD
sp
k (α)

as desired.

3 Generalized Versality and Special Points

As stated at the beginning of Section 2, we ﬁx a ground ﬁeld k throughout. By Deﬁnition 2.16, for any
algebraic group G and any primitive, generically free G-variety X, we have

RDk(X 99K X/G) ≤ RDk(G).

It is natural to ask for which G-varieties X we have RDk(X 99K X/G) = RDk(G). We will relate this question
to the notion of versality and generalizations thereof. First, we recall the deﬁnition of a versal G-variety.

10

Deﬁnition 3.1 (Section 1 of [DR2015]). Let G be an algebraic group deﬁned over k. We say that an
irreducible, generically free G-variety X is:

• weakly versal for G if for every G-torsor T → Spec(K), there is a G-equivariant k-morphism T → X.

• versal for G if every G-invariant open subvariety of X is weakly versal.

Note that X being versal for G is closely related to G ↷ X being a generic group action; the diﬀerence
being that versality does not require X/G to be rational (see [DR2015, Remark 2.8]).
In [FW2019, Proposition 3.7], the authors show that for a ﬁnite group G and any versal G-variety X,
RDk(G) = RDk(X 99K X/G). While versality is a suﬃcient condition, it was known classically that versality
is not necessary. Indeed, Klein showed in [Kle1884] that RDC(A5) = 1 by using the projective representation
A5 ↷ P1
C (see [Mor1956] for an English translation), despite the fact that P1
C 99K P1
C/A5 is not A5-versal.
This motivates the following generalizations of versality.

Deﬁnition 3.2 (Deﬁnition 3.8 of [FW2019] and Deﬁnition 4.4 of [FKW2023]). Let G be an algebraic group
deﬁned over k and let X be an irreducible, generically free G-variety. Let E be a class of accessory irrational-
ities. We say that X is:

• weakly E-versal for G if for every G-torsor T → Spec(K), there is an extension K ֒→ K ′ ∈ E(K)
and a G-equivariant k-morphism T ×Spec(K) Spec(K ′) → X;

• E-versal for G if every G-invariant open subvariety of X is weakly E-versal;

• weakly RDk-versal for G if for every G-torsor T → Spec(K), there is an extension K ֒→ ̃K with

RDk (K ֒→ ̃K) ≤ RDk(X 99K X/G) and a G-equivariant k-morphism

T ×Spec(K) Spec ( ̃K) → X;

• RDk-versal for G if every G-invariant open subvariety of X is weakly RDk-versal.

It is immediate that for an irreducible G-variety X, we have the implications

X is versal for G ⇒ X is E-versal for G for any E.

X is solvably versal for G ⇒ X is RD
≤1
k -versal for G.

X is RD≤d
k -versal for G ⇒ X is RD
≤d′

k -versal for G for any d ≤ d
′.

X is RD
≤d
k -versal for G for d ≤ RDk(X 99K X/G) ⇒ X is RDk-versal for G.

Klein showed that while P1
C is not versal for A5, it is solvably versal for A5. It is currently unknown if
RDk-versality is strictly weaker than solvable versality (see e.g. [CGR2006, Problem 9.3]). Nonetheless, by
[FW2019, Proposition 3.10], RDk(X 99K X/G) = RDk(G) when X is RDk-versal for G and G is ﬁnite; note
that the proof given carries over unchanged for general smooth algebraic groups G.
We have relatively few techniques for showing a G-variety is RDk-versal (especially when it is not already
versal or solvably versal), and essentially none for obstructing the existence of RDk-versal varieties of a given
dimension. For example, Hilbert’s Sextic Conjecture [Hil1927] — which remains open — predicts that there
are no RDC-versal A6-curves.
The proof of [FW2019, Proposition 3.10] (see also [FKW2023, Paragraph 4.1.3 and Lemma 4.9]), adapted
to the context of Deﬁnition 3.2, immediately yields the following:

Proposition 3.3 (RDk(G) via RD
≤d
k -versality). Let G be an algebraic group over k. Then,

RDk(G) = min
d≥0
 {max {d, dim(X)} | X is a G-variety which is RD≤d
k -versal for G
} .

Remark 3.4 (Equivalence of Deﬁnitions). The style of Deﬁnition 3.2 has been chosen for ease of comparison
with the literature on versality, e.g. [DR2015]. For comparison with [FKW2023], and for use in what follows,
we will now give an equivalent characterization in Lemma 3.6.

11

Deﬁnition 3.5 (G-Equivariant Rational Correspondence). Let G be an algebraic group and take X, Y to
be G-varieties. A G-equivariant rational correspondence from Y to X is a G-invariant subvariety
C ⊆ Y × X such that the projection C/G → Y /G is a generically ﬁnite, dominant morphism.

Lemma 3.6 (E-Versality via G-Equivariant Rational Correspondences). Let G be an algebraic group, X an
irreducible, generically free G-variety, and E a saturated class of accessory irrationalities. Then X is:

• weakly E-versal for G if for any generically free G-variety Y , there exists a G-equivariant rational
correspondence C ⊆ Y × X such that C/G → Y /G is in E(Y /G);

• E-versal for G if every non-empty G-invariant open subvariety of X is weakly E-versal for G. More-
over, these conditions are equivalent to the conditions stated in [FKW2023, Deﬁnition 4.4]

Proof. We begin by proving the equivalence of the conditions of the lemma with [FKW2023, Deﬁnition 4.4].
First, observe that any G-equivariant rational correspondence C ⊆ Y × X with C/G → Y /G in E(Y /G) gives
the data of [FKW2023, Deﬁnition 4.4]; indeed, item (1) of [FKW2023, Deﬁnition 4.4] is the given accessory
irrationality, item (2) is the map C/G → X/G (from projecting onto the second factor), and the isomorphism
(3) C/G ×X/G X ∼= C follows from generic freeness.
Conversely, given the data speciﬁed in [FKW2023, Deﬁnition 4.4], i.e. E // Y /G in E(Y /G) with f : E →
X/G and f ∗X ∼= E ×Y /G Y , let
 C/G := Im(E // Y /G × X/G),

C = C/G ×X/G X ⊂ Y × X.

Then, C is a G-invariant rational correspondence; C/G //Y /G is in E(Y /G), as E //Y is; and E is saturated.
We conclude that the conditions of the lemma are in fact equivalent to those of [FKW2023, Deﬁnition 4.4].
Since [FKW2023, Deﬁnition 4.4] does not mention torsors, for the sake of completeness we now show that
the conditions of [FKW2023, Deﬁnition 4.4] are equivalent to those of Deﬁnition 3.2. For this, it suﬃces to
prove the statement about weak E-versality (as the statement about E-versality amounts to verifying that
every dense Zariski open U ⊂ X is weakly E-versal). To go from a G-torsor T // Spec(K) as in Deﬁnition 3.2
to the data of [FKW2023, Deﬁnition 4.4] pick an integral model; to go the other way, restrict to a generic point
of an irreducible component of Y /G.5 From the proof of Lemma 2.6, we see that under this correspondence,
an extension K ֒→ K ′ is in E(K) if and only if any integral model E // Y /G is in E(Y /G). The equivalence
of the two deﬁnitions now follows by inspection.

In [DR2015], Duncan and Reichstein connect versality to existence of rational points. Speciﬁcally:

Theorem 3.7 (Versality and Rational Points, Theorem 1.1 (a,b) of [DR2015]). Let G be a linear algebraic
group over k and take X to be an irreducible, generically free, quasiprojective G-variety. Then, X is:

1. weakly versal if and only if for every G-torsor T → Spec(K), T X(K) ̸= ∅;

2. versal if and only if for every G-torsor T → Spec(K), K-points are dense in T X.

Remark 3.8 (Linear Algebraic Groups vs. Smooth Algebraic Groups). Duncan and Reichstein restrict their
attention to linear algebraic groups G (they also leave the assumption of “generically free” implicit in their
statement). In [DR2015, Remark 2.6], they state that this is “vitally important” for their reformulations of
versality. On the other hand, a careful reading of [DR2015, Sections 1-4] shows that linearity can be weakened
to smoothness at the cost only of rendering their Theorem 1.1(b) (that versality is equivalent to the density
of K-points in all twisted forms) potentially vacuous, as versal varieties do not exist for general smooth G.

Motivated by this result, along with [Rei2022, Lemma 4.15], we establish analogous claims about E-
versality.

Theorem 3.9 (Generalized Versality and Special Points). Let G be an algebraic group over k and let X be an
irreducible, generically free, quasiprojective G-variety. Let E be a saturated class of accessory irrationalities.
Then:

5[FKW2023] writes ˜Y // Y for our Y // Y /G.
 12

1. X is weakly E-versal if and only if for every G-torsor T → Spec(K) with K ﬁnitely generated over k,
T X (
K E) ̸= ∅.

2. If G is smooth, X is E-versal if and only if for every G-torsor T → Spec(K) with K ﬁnitely generated
over k, K E-points are dense in T X.

Remark 3.10 (Context for Smoothness). Cartier showed that every algebraic group over a ﬁeld k of char-
acteristic 0 is smooth (see [Poo2017, Corollary 5.2.18]), so in this case, no assumption on G is needed in
the second part of the theorem. We assume smoothness in order to reduce the proof to a Galois descent
argument. More generally, it seems reasonable to expect that the theorem holds without any assumptions
on G and k, at the cost of using fppf descent in lieu of Galois descent. We do not pursue this here.

Proof of Theorem 3.9. We begin by showing the ﬁrst statement. Suppose that X is weakly E-versal. Let
K be a ﬁeld which is ﬁnitely generated over k and consider a G-torsor T → Spec(K) with integral model
Y → Y /G. The G-equivariant isomorphism Y ×Y /G Spec(K) ∼= T induces

(Y × X)/G ×Y /G Spec(K) ∼= T X.

As X is weakly E-versal for G, there exists a G-equivariant rational correspondence C ⊆ Y × X with C/G 99K
Y /G in E(Y /G). Taking the quotient of the inclusion C → Y × X yields the morphism C/G → (Y × X)/G
of Y /G-varieties. We can restrict the morphisms C/G → Y /G and (Y × X)/G → Y /G along the generic
point Spec(K) → Y /G and obtain the following morphism of pullback diagrams, where Spec(L) denotes the
generic point of C/G:
 Spec(L) //

&&▼▼▼▼▼▼▼▼▼▼▼

  
 Spec(K)
 ▲▲▲▲▲▲▲▲▲▲
 ▲▲▲▲▲▲▲▲▲▲

T X //

  
   
 Spec(K)

  

C/G
 &&▼▼▼▼▼▼▼▼▼▼▼ // Y /G
 ▲▲▲▲▲▲▲▲▲▲
 ▲▲▲▲▲▲▲▲▲▲

(Y × X)/G // Y /G

Since C/G → Y /G is in E(Y /G) (by assumption), L ∈ E(K) (by 5 of Deﬁnition 2.4). From Deﬁnition
2.17, there is an inclusion of K-ﬁelds L ֒→ K E. Consequently, the constructed K E-point

Spec (
K E) → Spec(L) → T X,

shows that T X (
K E ) ̸= ∅.
Now, suppose that T → Spec(K) and Y → Y /G are as above and Spec (K E) → T X is a K E-point. Since
T X is a K-variety, there is a ﬁnite extension K ֒→ E such that Spec (
K E) → T X factors as

Spec (
K E) → Spec(E) → T X.

As E is saturated, E ∈ E(K). Now, let C/G denote the closure of Spec(E) in (Y × X)/G and take C ⊆ Y × X
to be the preimage of C/G under the quotient map Y × X → (Y × X)/G. Consequently, C is a G-
invariant subvariety, C → Y is a G-equivariant, generically ﬁnite, dominant morphism (by construction),
and C/G 99K Y /G is in E(Y /G) by construction. From Lemma 3.6, we see that X is weakly E-versal.
It remains to show the second claim. First, note that for any variety Z and ﬁeld ̃K, ̃K-points are dense in
Z if and only if each Zariski open of Z contains a ̃K-point. Next, in the setting of the theorem, for a Zariski
open V ⊂ T X, consider the quotient map q : T × X // T X, along with the projection map pX : T × X // X,
and set U = pX (q−1(V )) ⊂ X.
 13

By inspection, U ⊂ X is a G-invariant Zariski open, and V ⊂ T U . Therefore, if T X (K E) is dense in T X,
then T U (
K E) ̸= ∅ for every G-invariant Zariski open U ⊂ X. From our argument above, we conclude that
every such U is weakly E-versal for G, and thus X is E-versal for G. It remains to show the converse.
Suppose that X is E-versal for G. We need to show that T X (K E) is dense. As G is smooth, we can
identify ´etale and fppf cohomology with coeﬃcients in G (see e.g. [Mil1980, Remark III.4.8(a)]); this allows
us to make arguments via Galois descent.
Recall that a (right) G-torsor T // Spec(K) with cocycle τ ∈ H 1(K, G) is also a (left) G
τ -torsor, where
G
τ is the inner twist of G over K determined by τ . We can see this explicitly as follows. Indeed, let K sep

denote a separable closure of K. Then, letting Gal(K) := AutK(K sep), we obtain a 1-cocycle

τ : Gal(K) // G(K sep)

from T by picking an element 0 ∈ T (K sep). Explicitly, τ is deﬁned to be the map such that for σ ∈ Gal(K)

σ0 = 0 · τ (σ)

where we write σx to denote the σ-translate of a K sep point x of a K-variety. Note that τ (σ) is uniquely deter-
mined because T (K sep) is a principal right G(K sep)-set. Further, the choice of 0 determines an isomorphism
of right G(K sep)-sets
 ϕ0 : G(K sep) ∼=
→ T (K sep)

g ↦→ 0 · g

The left action of G(K sep) on itself now deﬁnes a left G(K sep)-action on T (K sep) via

g · (0 · h) := 0 · gh.

By inspection, this is not equivariant for the standard Gal(K)-action on G(K sep), but rather for the τ -twisted
action σ · g := τ (σ) (σg) (
τ (σ)
−1) .

By Galois descent, just as in [Poo2017, 5.12.5.1], we conclude that T // Spec(K) is actually a G
τ − G
bitorsor, and therefore, the twist T X carries a left action of G
τ .
Now, given a Zariski open V ⊂ T X as above, consider the Zariski open G
τ · V ⊂ T X. Then V (
K E) ̸= ∅ if
and only if G
τ · V (
K E) ̸= ∅. Now let q : T × X // T X denote the quotient map, let pX : T × X // X denote
the projection, and set U := pX (q−1(V )) ⊆ X. Note that U is a G-invariant Zariski open by inspection.
Since X is E-versal for G, U is weakly E-versal. By the proof of the ﬁrst statement of the theorem above, we
have that T U (
K E) ̸= ∅. To conclude, we claim that

G
τ · V = T U.

Granting this claim, we have, by the above, that V (
K E ) ̸= ∅, and thus that T X (
K E) is dense in T X, as
claimed. We prove the claim by a straightforward Galois descent argument. Indeed, our choice of 0 ∈ T (K sep)
determines an isomorphism

T U (K sep) ∼= {(0 · g, u) ∈ G(K sep) × U (K sep)}/(0 · g, u) ∼ (0, g · u)

= {(0 · g, x) ∈ G(K sep) × X(K sep) | ∃[(0 · h, v)] ∈ V (K sep) s.t. h · v = x}/(0 · g, x) ∼ (0, g · x)
= {(0 · gh, v) ∈ G(K sep) × X(K sep) | [(0 · h, v)] ∈ V (K sep)}/(0 · g, x) ∼ (0, g · x)

= (G
τ · V )(K sep).

By inspection, this isomorphism is Gal(K)-equivariant, and thus T U = G
τ · V as claimed.

Taken together, Proposition 3.3 and Theorem 3.9 allow us to re-contextualize problems about the resolvent
degree of algebraic groups as questions about special points on twists of G-varieties. Indeed, we can ask about
necessary and suﬃcient conditions for a variety over K to have an E-point or a dense collection of E-points.
As an example, we have the following, which appeared as [FKW2023, Lemma 4.7] for the case of ﬁnite G.

14

Lemma 3.11 (E-Versality and Composition). Let G be a smooth algebraic group over k, let E be a saturated
class of accessory irrationalities which is closed under extensions, and let Y be a primitive G-variety which is
E-versal for G. Suppose X is an irreducible, generically free G-variety which admits a G-equivariant rational
correspondence C ⊂ Y × X such that C → X is dominant and C/G → Y /G is in E(Y /G). Then X is
E-versal.

Remark 3.12 (Representatives for E-Versality). In contrast to the deﬁnition of E-versality, Lemma 3.11 allows
us to test E-versality of X by looking at correspondences from the single G-variety Y , rather than from all
G-varieties.

Proof of Lemma 3.11. For weak E-versality, let Z be a generically free G-variety. From Lemma 3.6, there is
a G-equivariant rational correspondence D ⊆ Z × Y with D/G → Z/G in E(Z/G). Then, we can consider
C ×Y D ⊆ Z × X, which is G-invariant, and we see that (C ×Y D)/G → D/G → Z/G is in E(Z/G) because
(C ×Y D)/G → D/G is in E(D/G), D/G → Z/G is in E(Z/G), and E is closed under extensions.
For E-versality, by Theorem 3.9, it suﬃces to show that T X(K E) is dense in T X for any G-torsor
T // Spec(K). Fix such a T . By Theorem 3.9, T Y (K E) is dense in T Y . By assumption, C // Y is
generically ﬁnite, dominant and C/G // Y /G is in E(Y /G). Therefore, by the deﬁnition of K E as an E-
closure, the density of T Y (K E ) in T Y implies that T C (
K E) is dense in T C as well. But, the map T C // T X
is dominant, by assumption, so we conclude that T X (
K E) is dense in T X as claimed.

Theorem 3.9 connects (weak) E-versality of X for G to existence of special points (i.e. K E-points), but
still requires one to consider twists of X by all torsors over ﬁnitely generated k-ﬁelds. Just as Proposition
3.3 allows us to reduce from all G-varieties X to those which are E-versal, the following deﬁnition will give
us the language to reduce the class of torsors one must consider.

Deﬁnition 3.13 (E-Versality for G-torsors). Let G be an algebraic group over k. Let E be a class of accessory
irrationalities. A G-torsor T → Spec(K) is E-versal for G if there exists any integral model Y → Y /G of
T → Spec(K) such that Y is an E-versal G-variety.

Note that, because all integral models are birational to each other, if T → Spec(K) is E-versal, then every
integral model Y → Y /G is E-versal. We can now restate a variant of Lemma 3.11 as follows:

Lemma 3.14 (An Equivalent Version of Lemma 3.11). Let G be a smooth algebraic group over k. Let E be
a saturated class of accessory irrationalities that is closed under extensions. Suppose that T → Spec(K) is a
G-torsor which is E-versal for G and X is a generically free G-variety. Then, X is E-versal if and only if
T X has a dense collection of K E -points.

Proof. From Theorem 3.9, if X is E-versal, then T X has a dense collection of K E-points.
Now, suppose that T X has a dense collection of K E-points and let Y → Y /G be an integral model of
T → Spec(K) (which, as remarked above, is E-versal because T → Spec(K) is). Let Spec (
K E ) → T X be a
K E-point of T X. As established in the proof of Theorem 3.9, T X is the generic ﬁber of (Y ×X)/G → Y /G and
we take C/G ⊆ (Y × X)/G to be the closure of our K E -point Spec (
K E) → T X. We set C = C/G ×(Y ×X)/G
(Y × X) and observe that C ⊆ Y × X is a G-equivariant rational correspondence with C/G → Y /G in
E(Y /G), by construction. By assumption, Y → Y /G is E-versal and thus X is E-versal by Lemma 3.11.

In another direction, we also have:

Lemma 3.15 (E-Versality for Non-Abelian, Finite, Simple Groups). Assume char(k) = 0. Let G be a non-
abelian, ﬁnite, simple group G, let E be a class of accessory irrationalities, and let X be a smooth, irreducible,
generically free G-curve over k. Then X is weakly E-versal for G if and only if X is E-versal for G.

Proof. By deﬁnition, E-versality immediately implies weak E-versality. Now, suppose that X is weakly
E-versal. Let Y be a generically free G-variety with dim(Y ) ≥ 1 and consider a G-equivariant rational
correspondence C ⊆ Y × X with C/G → Y /G in E(Y /G). It suﬃces to show that the G-equivariant map
C → X is dominant. Denote the scheme-theoretic image of C in X by Z. Then, Z is an irreducible
G-invariant subscheme. If dim(Z) = 1, then the map is dominant and we are done. Now, suppose that
dim(Z) = 0. Then, Z red ∈ X is a ﬁxed point for G. However, the stabilizer of any point in X is abelian
[RY2000, Theorem 1.1], hence there are no ﬁxed points for G and thus dim(Z) ≥ 1.

15

Let us now revisit Hilbert’s Sextic Conjecture. In light of Proposition 3.3, Theorem 3.9, and Lemma 3.15,
we can re-state the conjecture as follows:

Conjecture 3.16 (Hilbert’s Sextic Conjecture). Let T → Spec (C(x, y)) be the A6-torsor associated to the
Valentiner action A6 ↷ P2
C. For any smooth, irreducible, generically free A6-curve X, T X (
C(x, y)
(1)) = ∅.

Similarly, [CGR2006, Problem 9.3] for A6 can be re-stated as:

Problem 3.17 (Chernousov-Gille-Reichstein). Does there exist a smooth, irreducible, generically free A6-
curve X with T X (
C(x, y)
Sol) ̸= ∅?

More generally, showing that RDk(G) > 1 is a question of obstructing the existence of K (1)-points for a
suﬃcient supply of K-curves (namely, twists of G-curves over k). Many tools in the literature for obstructing
rational points appear to be inadequate for this. For example, by [MS1983, Theorem 16.1], the Brauer group
of a solvably closed ﬁeld is trivial. More generally, the same holds for H 1(−, G) for any connected algebraic
group G without simple factors of type E8 (see [Rei2022, Theorem 1.1]); conjecturally, the same holds for all
connected algebraic groups (see [Rei2022, Conjecture 1.4] and the discussion just preceding it). It would be
instructive to turn this observation (that G connected implies H 1(K Sol, G) = 1) into a proof that Brauer-
Manin style invariants are insuﬃcient to obstruct solvable points on varieties over e.g. two-dimensional
C-ﬁelds. We echo Poonen’s view in [Poo2017, p. 257] that “We need some new obstructions!”

4 Resolvent Degree and the Sporadic Groups

4.1 Upper Bounds on the Resolvent Degree of the Sporadic Groups

Recall that the Classiﬁcation of Finite Simple Groups consists of 18 inﬁnite families and 26 sporadic groups.
The 26 sporadic groups are often organized as in Figure 1.

Figure 1: Historical Organization of Sporadic Groups
Cluster Generation Description Groups
Happy Family First The Mathieu Groups M11, M12, M22, M23, M24,
Happy Family Second The Leech Lattice Groups Co1, Co2, Co3, Suz, McL, HS, J2,
Happy Family Third Other Monster Subgroups Fi22, Fi23, Fi24’, Th, HN, He, B, M,
The Pariahs The Pariahs J1, J3, J4, O’N, Ru, Ly.

From [Rei2022, Theorems 1.2 and 1.3], RDk(G) ≤ RDC(G) for any ﬁnite simple group. Thus, to determine
upper bounds on the resolvent degree of the sporadic groups, it suﬃces to work over C. For each sporadic
group G, we will determine a complex G-variety XG such that RDC(G) ≤ dimC (XG). We begin by considering
a minimal dimensional projective representation. It is immediate that any linear representation of G yields a
projective representation of G, however these are not the only projective representations of G. Indeed, there
are groups Γ such that the projectivizations of linear representations of Γ correspond exactly to projective
representations of G. Such a group Γ is called a Schur cover of G (or sometimes a Schur representation
group of G). Each sporadic group G is perfect, hence the Schur covers of G are isomorphic and so we simply
refer to the Schur cover of G henceforth. Explicitly, the Schur cover of G is a central extension of G by the
Schur multiplier Sch(G) = H 2 (G, C∗), which is a ﬁnite abelian group whose exponent divides the order of
G. For more on projective representations of ﬁnite groups, we refer the reader to [Isa1976, Chapter 11].
Given G and a projective representation P(ρ) : G → PGL(V ) coming from a linear representation ρ of the
Schur cover, we are not interested in just P (V ), but G-invariant subvarieties thereof. We can construct such
invariant subvarieties by looking at the vanishing of G-invariant polynomials. Note that the vector space of
homogeneous polynomials of degree d which are invariant under the Schur cover of G is Sym
d
a.G (V ∨). We
set md(ρ) = dim (Sym
d
a.G (V ∨)) and note that the Molien series of ρ is the generating function

M (ρ; t) := ∑

d≥0 md(ρ)td.

16

We now introduce notation for the minimal projective representations for each sporadic group and address
computing the relevant Molien series.

Notation 4.1 (Representations of Sporadic Groups). For the groups G = M11, M23, M24, J1, J4, Co3, Co2,
Fi22, Fi23, HS, McL, He, HN, Th, Ly, B, and M, a projective representation of minimal dimension arises as
the projectivization of an irreducible linear representation of G. When G is not one of HS, McL, Fi22, or
B, this claim is immediate, as the Schur multiplier is trivial. For the cases G = HS, McL, Fi22, and B, one
can verify this claim by inspecting the character tables of the Schur covers. We set d(G) to be the minimal
dimension of a non-trivial linear representation of G and ρG to be the representation corresponding to the
ﬁrst character χ in the ATLAS character table for G for which χ(1) = d(G) (note that ρG is necessarily
irreducible by our minimality assumption). Additionally, set VG to be the vector space corresponding to ρG.
For the groups G = M22, J2, J3, Co1, Fi24’, Suz, Ru, and O’N, a projective representation of minimal
dimension only arises as the projectivization of an irreducible linear representation of the Schur cover of G.
Correspondingly, we set a(G) = |Sch(G)|, d(G) to be the minimal dimension of a non-trivial representation
of the Schur cover (denoted by a.G), ρG to be the representation corresponding to the ﬁrst character in the
ATLAS character table for a.G for which χ(1) = d(G) (as above, our minimality assumption guarantees that
ρG is irreducible), and VG to be the vector space corresponding to ρG.
When G is clear from the context, we simply write a and d. Additionally, we note that the order of the
characters in the ATLAS [CCNPW1985] is the same as in GAP character table library [Bre2013].

Remark 4.2 (Schur Multiplier M22). In [BF1966, p.739-741], it is incorrectly claimed that a (M22) = 3. In
the correction [BF1968], it is incorrectly asserted that a (M22) = 6. Finally, [Maz1979, Section V] correctly
establishes that Sch (M22) ∼= Z/12Z.

Remark 4.3 (The Unique Case of M12). There is another error in [BF1966, p.739-741], where they incorrectly
claim that a (M12) = 1. However, [BF1968] correctly establishes that a (M12) = 2.
An observant reader may have noticed that M12 does not appear in Notation 4.1. While we will use the
same notation conventions, ρM12 is not a projective representation of minimal dimension for M12. While
the Schur cover 2. M12 admits a 10-dimensional linear representation, we will instead take ρM12 to be the
ﬁrst 11-dimensional linear representation of ρM12. We will justify this choice in Remark 4.11, after we prove
Theorem 4.7.

Remark 4.4 (Computation of Molien Series / Molien Series Coeﬃcients). For the sporadic groups G where
|G| and d(G) are suﬃciently small (M11, M12, M22, M23, M24, J1, J2, J3, Co3, Co2, Co1, Suz, HS, McL,
Ru, and He), we compute the Molien series M (ρG; t) as a rational function using the character table library
[Bre2013] in SageMath by accessing GAP. For the remaining groups G (J4, Fi22, Fi23, Fi24’, HN, Th, O’N, Ly,
B, and M), we store data for ρG from the character table library [Bre2013], which we then use to compute
the ﬁrst 20 coeﬃcients m1 (ρG) , . . . , m20 (ρG) of M (ρG; t) in SageMath. The SageMath script, data ﬁles (for
J4, Fi22, Fi23, Fi24’, HN, Th, O’N, Ly, B, and M), and output ﬁles (for all sporadic groups), are available at

https://www.alexandersutherland.com/research/RD-for-the-Sporadic-Groups,

or by downloading the source package on the arXiv version of this work. Additionally, for every sporadic
group G, we record the beginning of the power series expansion of M (ρG; t) in Appendix A.

For each sporadic group G, Figure 2 records dim (P (VG)) and a list of the degrees of the invariants we
will use in what follows. Note that ordering of the groups in Figure 2 is determined by dim (P (VG)). Our
construction for J2 does not require any invariants, so we leave the corresponding entry blank. Additionally,
our proof will use the minimal dimensional permutation representation for the sporadic groups other than M11,
M12, M23, and M24, hence Figure 2 includes dim (PermG) as well. For each G, we denote this representation
by PermG and observe that dim (PermG) = [G : H], where H is a maximal subgroup of G of maximal order.
For details on maximal subgroups, see [DLP2023] when G = M, [Wil2009] when G = Fi22, Fi23, Fi24’, J4,
Th, and B, [Wil2017] for a survey, and [CCNPW1985]) for all other cases.

17

Figure 2: Dimensions of Projective Representations and Degrees of Invariants
Group G dim (P (VG)) Degrees of Relevant Invariants dim (PermG)
J2 5 N/A 100
M11 9 2, 3, 4 11
M22 9 4 22
M12 10 2, 3, 4 12
Suz 11 12 1782
J3 17 6 85
M23 21 2, 3, 4, 5 23
HS 21 2, 4, 5 100
McL 21 2, 5 275
M24 22 2, 3, 4, 5 24
Co3 22 2, 6 276
Co2 22 2, 8 2300
Co1 23 2, 12 98280
Ru 27 4 4060
He 50 3, 4 2058
J1 55 2, 3, 4, 4 266
Fi22 77 2, 6, 8 3510
HN 132 2, 6, 7 1140000
Th 247 2, 8, 8 143127000
O’N 341 6, 6, 6 122760
Fi23 781 2, 3, 4, 5, 5 31671
Fi24’ 782 3, 6, 6 306936
J4 1332 4, 6, 6, 7 173067389
Ly 2479 6, 6, 6, 6 8835156
B 4370 2, 4, 6, 8, 8 13571955000
M 196882 2, 3, 4, 5, 6, 6, 6, 7 97239461142009186000

We now introduce the notation required for Theorem 4.7.

Notation 4.5 (Notation for Theorem 4.7). Let G be a sporadic group. When md (ρG) = j, we denote a basis
for Sym
d
a.G (V ∨
G ) by f G
d,1, . . . , f G
d,j. When j = 1, we simply write f G
d . Without loss of generality, we order the
basis such that the basis elements which are algebraically independent from lower degree invariants are listed
ﬁrst; see Remark 4.6 for more details. When the group G is clear from context, we omit the superscript.
Using this notation, we now deﬁne the relevant G-invariant subvarieties of VG. Speciﬁcally, we will deﬁne a
variety XG = ZG ∩ YG. We begin with the cases where YG is non-trivial:

ZM11 = V (f4,1) , YM11 = V (f2, f3) , XM11 = V (f2, f3, f4,1) ⊆ P (VM11 ) = P9,

ZM12 = V (f4,1) , YM12 = V (f2, f3) , XM12 = V (f2, f3, f4,1) ⊆ P (VM12 ) = P10,

ZM23 = V (f4,1, f5,1) , YM23 = V (f2, f3) , XM23 = V (f2, f3, f4,1, f5,1) ⊆ P (VM23 ) = P21,

ZHS = V (f4,1, f5) , YHS = V (f2) , XHS = V (f2, f4,1, f5) ⊆ P (VHS) = P21,

ZMcL = V (f5) , YMcL = V (f2) , XMcL = V (f2, f5) ⊆ P (VMcL) = P21,

ZM24 = V (f4,1, f5,1) , YM24 = V (f2, f3) , XM24 = V (f2, f3, f4,1, f5,1) ⊆ P (VM24 ) = P22,

ZCo3 = V (f6,1) , YCo3 = V (f2) , XCo3 = V (f2, f6,1) ⊆ P (VCo3 ) = P22,

ZCo2 = V (f8,1) , YCo2 = V (f2) , XCo2 = V (f2, f8,1) ⊆ P (VCo2 ) = P22,

ZCo1 = V (f12,1) , YCo1 = V (f2) , XCo1 = V (f2, f12,1) ⊆ P (VCo1 ) = P23,

ZJ1 = V (f3, f4,1, f4,2) , YJ1 = V (f2) , XJ1 = V (f2, f3, f4,1, f4,2) ⊆ P (VJ1 ) = P55,

18

ZFi22 = V (f6, f8,1) , YFi22 = V (f2) , XFi22 = V (f2, f6, f8,1) ⊆ P (VFi22 ) = P77,

ZHN = V (f6, f7) , YHN = V (f2) , XHN = V (f2, f6, f7) ⊆ P (VHN) = P132,

ZTh = V (f8,1, f8,2) , YTh = V (f2) , XTh = V (f2, f8,1, f8,2) ⊆ P (VTh) = P247.

In the following cases, we have XG = ZG and YG = P (VG):

ZM22 = XM22 = V (f4) ⊆ P (VM22 ) = P9,

ZSuz = XSuz = V (f12) ⊆ P (VSuz) = P11,

ZJ3 = XJ3 = V (f6) ⊆ P (VJ3 ) = P17,

ZRu = XRu = V (f4) ⊆ P (VRu) = P27,

ZHe = XHe = V (f3, f4) ⊆ P (VHe) = P50,

ZO’N = XO’N = V (f6,1, f6,2, f6,3) ⊆ P (VO’N) = P341,

ZFi23 = XFi23 = V (f2, f3, f4,1, f5,1, f5,2) ⊆ P (VFi23 ) = P781,

ZFi24’ = XFi24’ = V (f3, f6,1, f6,2) ⊆ P (VFi24’) = P782,

ZJ4 = XJ4 = V (f4, f6,1, f6,2, f7,1) ⊆ P (VJ4 ) = P1332,

ZLy = XLy = V (f6,1, f6,2, f6,3, f6,4) ⊆ P (VLy) = P2479,

ZB = XB = V (f2, f4,1, f6,1, f8,1, f8,2) ⊆ P (VB) = P4370,

ZM = XM = V (f2, f3, f4,1, f5,1, f6,1, f6,2, f6,3, f7,1) ⊆ P (VM) = P196882.

In the exceptional case of J2, we further have that XJ2 = ZJ2 = YJ2 = P (VJ2 ) = P5.

Remark 4.6 (Non-Uniqueness of XG, YG, ZG). We note that the XG, YG, and ZG are only deﬁned up to a
choice of invariant polynomials. As an example, consider the case G = Co3. First, note that m2 (ρCo3 ) = 1 and
thus f2 is unique up to a constant. Next, m4 (ρCo3 ) = 1 and thus the only degree four invariant, up to scaling,
is (f2)
2. Finally, m6 (ρCo3 ) = 2 and so we take f6,1 to be any polynomial in Sym
6
Co3 (
V ∨
Co3 ) \ Span {
(f2)
3}

and f6,2 to be any polynomial in Span {
(f2)3}
. However, all of the arguments that follow depend only on
the degrees of the intersections deﬁning XG, YG, and ZG and are consequently independent of this choice.

We are now ready to give upper bounds on the resolvent degree of the sporadic groups.

Theorem 4.7 (Bounds on Resolvent Degree of the Sporadic Groups). For each sporadic group G, we have

RDk(G) ≤ dimC(XG).

for every ﬁeld k. Further, for G not equal to M11, M12, M23, M24, the variety XG is RD
≤dG
C -versal for
dG = RDC(deg(ZG)).

Remark 4.8. We expect that the variety XG is RD
≤dG
k -versal for the Mathieu groups M11, M12, M23, M24,
but proving this requires new techniques.

We will also give an explicit form of Theorem 4.7 in Corollary 4.9.

Proof. As observed above, by [Rei2022, Theorems 1.2 and 1.3], it suﬃces to prove the theorem for k = C.
When G is one of M11, M12, M23, or M24, the upper bounds on RDC(G) are classical. In these cases, Mn < Sn
and the bounds follow from the inequality RDC(Mn) ≤ RDC(Sn) [FW2019, Lemma 3.13] and the classical
upper bounds on RDC(Sn) (see [Sut2021, Theorem 3.7] for the construction and the bounds on S23, S24; see
[FW2019, Sut2021] for modern references for S11, S12 or [Hil1927, Seg1945] for classical references).
We now restrict to the case where G is not one of M11, M12, M23, M24. Note that dG ≤ dimC (XG),
hence Proposition 3.3 yields that we need only show that each XG is RD
≤dG
C -versal. Since ﬁnite groups are
smooth, Theorem 3.9 allows us to reduce to showing that a) XG is generically free, and b) for every G-torsor
T → Spec(K) with K ﬁnitely generated over C, K (dG)-points are dense in T X G.

19

We start with generic freeness. Since G is simple, and the representation ρG is irreducible, we see that
P(VG) has no ﬁxed points and thus is a faithful G-variety. By Lemma 2.15, it suﬃces to show that XG is
irreducible, but this follows for degree reasons. Indeed, for all simple sporadic G not equal to M11, M12,
M23, or M24, the degree of XG is less than the cardinality of the smallest permutation representation of G
(see Figure 2 and preceeding discussion). Since XG has at most deg XG irreducible components, and since
G permutes them, we conclude that XG is irreducible, and thus generically free.
To apply Theorem 3.9 to conclude the RD≤dG
C -versality of XG, we just need to show that K (dG) points
are dense in every twisted form of XG. As observed in [Rei2022, Proof of Proposition 14.1 (p.33)], the
G-equivariant closed immersion XG ֒→ P (VG) naturally induces the closed immersion T XG ֒→ T P (VG).
Note that T P (VG) is a Severi–Brauer variety and thus splits over K Sol ⊆ K (dG) by the Merkurjev-Suslin
theorem [MS1983]. It follows that T XG is an intersection of hypersurfaces in P (VG) over K (dG) of the same
degrees as for XG. Indeed, the same argument applies to T YG ֒→ T P (VG) and T ZG ֒→ T P (VG) and we have
T XG = T ZG ∩ T YG over K (dG).
Now, observe that for each G, we either have that YG = P (VG) (and thus XG = ZG) or YG = V (
f G
2 )
.
In the ﬁrst case, we have deg (XG) = deg (ZG) = dG, and the density of K (dG)-points is immediate. In the
second case, YG is a quadric hypersurface and XG = YG ∩ ZG, hence [Rei2022, Lemma 14.4(b)] yields that
K (dG)-points are dense on XG.

Corollary 4.9 (Explicit Form of Theorem 4.7). For any ﬁeld k, we have

RDk(J2) ≤ 5, RDk(M24) ≤ 18, RDk(He) ≤ 48, RDk(Fi23) ≤ 776,
RDk(M11) ≤ 6, RDk(HS) ≤ 18, RDk(J1) ≤ 51, RDk(Fi24’) ≤ 779,

RDk(M12) ≤ 7, RDk(McL) ≤ 19, RDk(Fi22) ≤ 74, RDk(J4) ≤ 1328,
RDk(M22) ≤ 8, RDk(Co3) ≤ 20, RDk(HN) ≤ 129, RDk(Ly) ≤ 2475,

RDk(Suz) ≤ 10, RDk(Co2) ≤ 20, RDk(Th) ≤ 244, RDk(B) ≤ 4365,
RDk(J3) ≤ 16, RDk(Co1) ≤ 21, RDk(O’N) ≤ 338, RDk(M) ≤ 196874.

RDk(M23) ≤ 17, RDk(Ru) ≤ 26,

Remark 4.10 (Further Expectations). In the cases where G is one of M22, Ru, He, Fi23, or Fi24’, we expect
that we can do slightly better. Indeed, we believe that we can replace XG, YG, and ZG with
̃ZM22 = V (f6) , ̃YM22 = V (f4) , ̃XM22 = V (f4, f6) ⊆ P (VM22 ) = P9,
̃ZRu = V (f8) , ̃YRu = V (f4) , ̃XRu = V (f4, f8) ⊆ P (VRu) = P27,
̃ZHe = V (f4, f5) , ̃YHe = V (f3) , ̃XHe = V (f3, f4, f5) ⊆ P (VHe) = P50,
̃ZFi23 = V (f4, f5,1, f5,2, f6) , ̃YFi23 = V (f2, f3) , ̃XFi23 = V (f2, f3, f4, f5,1, f5,2, f6) ⊆ P (VFi23 ) = P781,
̃ZFi24’ = V (f6,1, f6,2, f9) , ̃YFi24’ = V (f3) , ̃XFi24’ = V (f3, f6,1, f6,2, f9) ⊆ P (VFi24’) = P782.

In these cases, one can use the polar cone methods of [Sut2021] to construct linear subvarieties of suitable
dimension and satisfactorily low resolvent degree on each ̃YG. However, new methods are required to show
that each ̃XG = ̃YG ∩ ̃ZG is generically free.
Remark 4.11 (The Unique Case of M12, II). As noted in Remark 4.3, ρM12 is the only case where we are not
using a projective representation of minimal dimension. As we have seen, we constructed

XM12 = V (f2, f3, f4) ⊆ P10 = P (VM12) .

Now, let ̃ρM12 be the ﬁrst 10-dimensional representation of the Schur cover 2. M12. The lowest degree
invariants of ̃ρM12 have degrees 6, 8, 8, and 8 respectively. Consequently, the best analogous construction
would yield ̃XM12 = V (f6) ⊆ P9 = P ( ̃VM12 ) .

Since dim (XM12) < dim ( ̃XM12), XM12 is the preferred construction.
For every other sporadic group G with non-trivial Schur cover a.G, either there is not a lower dimensional
projective representation or the dimension of the new projective representation is small enough to outweigh
any diﬀerences in the invariant theory.
 20

4.2 Context for Sporadic Group Bounds

We conclude by providing additional context for these numerical results and connect the bounds for the
Mathieu groups to known bounds for symmetric groups.

Mathieu Groups and Symmetric Groups As noted in Section 1, RDk(G) for ﬁnite simple groups has
only been addressed in the literature when G is a cyclic group (for which RDk ≡ 1 by Kummer theory), an
alternating group [HS2023, Sut2021, Wol2021], when G = W (E6)+, W (E7)
+, or W (E8)
+ (see [FW2019,
Section 8] for E6 and E7, see [Rei2022, Proposition 15.1] for E6, E7, and E8), or when G = PSL(2, 7)
([Kle1879], [FKW2023, Proposition 4.13]). Nonetheless, each of the Mathieu groups have explicit embeddings
Mn ֒→ Sn for n = 11, 12, 22, 23, 24 and thus RDk(Mn) ≤ RDk(Sn) [FW2019, Lemma 3.13]. At present,
this paper contributes nothing new for M11, M12, M23, M24. In the case of M22, our bound of 8 signiﬁcantly
beats the bound RDC(S22) ≤ 16 [Sut2021, Theorem 3.7]. As remarked above, it would be interesting to
conﬁrm that for M11, M12, M23, M24, the variety XG is also RD
≤dG
C -versal. It would also be interesting to
know for which n and which ﬁelds k we have RDk(Mn) < RDk(Sn), and for which n and which ﬁelds k we
have RDk(Mn) = RDk(Sn).

Relations Between the Sporadic Groups For a ﬁnite group H and a subgroup H ′, we have RDk(H ′) ≤
RDk(H) [FW2019, Lemma 3.13]. Additionally, for a short exact sequence of algebraic groups

1 → A → B → C → 1,

we have that RDk(B) ≤ max {RDk(A), RDk(C)} ([FW2019, Theorem 3.3] for ﬁnite groups, [Rei2022, Propo-
sition 10.8] in general).
For any sporadic group S which is a subquotient of another sporadic group G, with H < G and S = H/H ′,
we only have the inequalities

RDk(H) ≤ RDk(G), RDk(H) ≤ max {RDk(S), RDk(H ′)} .

Nonetheless, it is natural to ask how the bounds given by dim (XS) and dim (XG) in Theorem 4.7 compare.
The ATLAS contains a table of which sporadic groups S are subquotients of another sporadic group G
[CCNPW1985, p.238], which we include below. Let (G, S) be the cell corresponding to row G and column
S. Note that (G, S) has a + with a green background if S is a subquotient of G; (G, S) has a − with a red
background if S is not a subquotient of G; (G, S) has a • with a yellow background when G = S; and (G, S)
is black when |G| < |S|.
We implement two changes from the table in the ATLAS. Firstly, at the time of publishing the ATLAS,
it was unknown if J1 is a subquotient of M. Wilson showed that J1 is not a subgroup of M in [Wil1986],
which completed the proof that J1 is not a subquotient of M, and we have updated the (M, J1) cell as a
result. Secondly, due to page size restrictions, we split the single table in the ATLAS into two smaller tables:
Figures 3 and 4.
Finally, we note that

dim (XJ2) < dim (XM11 ) ≤ dim (XM12) < dim (XM22) < dim (XSuz) < dim (XJ3) < dim (XM23)

< dim (XM24) = dim (XHS) < dim (XMcL) < dim (XCo3 ) = dim (XCo2 ) < dim (XCo1 ) < dim (XRu)
< dim (XHe) < dim (XJ1 ) < dim (XFi22) < dim (XHN) < dim (XTh) < dim (XO’N) < dim (XFi23)

< dim (XFi24’) < dim (XJ4) < dim (XLy) < dim (XB) < dim (XM) ,

and thus one can verify using Figures 3 and 4 that whenever S is a subquotient of G, we have dim (XS) ≤
dim (XG).
 21

Figure 3: Sporadic Groups Subquotient Table from the ATLAS, I
M11 M12 J1 M22 J2 M23 HS J3 M24 McL He Ru Suz O’N Co3 Co2
M11 •
M12 + •
J1 − − •
M22 − − − •
J2 − − − − •
M23 + − − + − •
HS + − − + − − •
J3 − − − − − − − •
M24 + + − + − + − − •
McL + − − + − − − − − •
He − − − − − − − − − − •
Ru − − − − − − − − − − − •
Suz + + − − + − − − − − − − •
O’N + − + − − − − − − − − − − •
Co3 + + − + − + + − − + − − − − •
Co2 + − − + − + + − − + − − − − − •
Fi22 + + − + − − − − − − − − − − − −
HN + + − + − − + − − − − − − − − −
Ly + − − + − − − − − + − − − − − −
Th − − − − − − − − − − − − − − − −
Fi23 + + − + − + − − − − − − − − − −
Co1 + + − + + + + − + + − − + − + +
J4 + + − + − + − − + − − − − − − −
Fi24’ + + − + − + − − + − + − − − − −
B + + − + − + + − − + − − − − − +
M + + − + + + + − + + + − + − + +

Figure 4: Sporadic Groups Subquotient Table from the ATLAS, II
Fi22 HN Ly Th Fi23 Co1 J4 Fi24’ B M
Fi22 •
HN − •
Ly − − •
Th − − − •
Fi23 + − − − •
Co1 − − − − − •
J4 − − − − − − •
Fi24’ + − − − + − − •
B + + − + + − − − •
M + + − + + + − + + •

Linear Representations, Projective Representations, and XG Let G be a ﬁnite simple group. Every
non-trivial linear and projective representation of G is faithful, so the corresponding quotient maps yield
upper bounds on RDk(G) [FKW2023, Example 4.6]. For each sporadic group G, we now compare XG with a
minimal-dimensional linear representation WG and a minimal-dimensional projective representation P (VG)
(continuing with the notation of Notation 4.1). In the cases where the linear representation comes from the
Schur cover, we include the Schur cover as well.
 22

Figure 5: Minimal Linear Representations, Projective Representations, and XG
Group G dim (WG) dim (P (VG)) dim (XG)
M11 10 9 6
M12 11 10 7
M23 22 21 17
HS 22 21 18
McL 22 21 19
M24 23 22 18
Co3 23 22 20
Co2 23 22 20
He 51 50 48
J1 56 55 51
Fi22 78 77 74
HN 133 132 129
Th 248 247 244
Fi23 782 781 776
J4 1333 1332 1328
Ly 2480 2479 2475
B 4371 4370 4365
M 196883 196882 196874

Figure 6: Minimal Linear Representations, Projective Representations, XG, and the Schur Covers
Group G dim (WG) dim (P (VG)) dim (XG) a.G
J2 14 5 5 2. J2
M22 20 9 8 12. M22
Suz 143 11 10 6. Suz
J3 85 17 16 3. J3
Co1 276 23 21 2. Co1
Ru 378 27 26 2. Ru
O’N 10944 341 338 3. O’N
Fi24’ 8671 782 779 3. Fi24’

A Power Series Expansions of Molien Series

For each sporadic group G, we record the initial terms of the power series expansions of M (ρG; t) in Figure
7.
 Figure 7: Power Series Expansions
Group Initial Terms for the Power Series Expansion of M (ρG; t)
J2 1 + t12 + t20 + 2t24 + t28 + 2t30 + 3t32 + t34 + 4t36 + 2t38 + O (
t40)

M11 1 + t2 + t3 + 2t4 + 3t5 + 5t6 + 6t7 + 11t8 + 16t9 + 26t10 + 38t11 + 61t12 + 91t13 + O (
t14)

M12 1 + t2 + t3 + 2t4 + 2t5 + 5t6 + 4t7 + 9t8 + 10t9 + 17t10 + 20t11 + 36t12 + 39t13 + 67t14 + O (
t15)

M22 1 + t4 + t6 + 2t8 + 3t10 + 6t12 + 9t14 + 15t16 + 26t18 + O (
t20)

Suz 1 + t12 + t18 + 3t24 + 3t30 + 7t36 + O (
t40)

J3 1 + t6 + t9 + 10t12 + 26t15 + 143t18 + 680t21 + 3310t24 + 14229t27 + 55826t30 + O (
t33)

M23 1 + t2 + t3 + 2t4 + 3t5 + 6t6 + 9t7 + 17t8 + 27t9 + 49t10 + 86t11 + 159t12 + 292t13 + O (
t14)

HS 1 + t2 + 2t4 + t5 + 5t6 + 3t7 + 12t8 + 9t9 + 29t10 + 28t11 + 77t12 + 87t13 + 220t14 + O (
t15)

McL 1 + t2 + t4 + t5 + 2t6 + 3t7 + 5t8 + 6t9 + 10t10 + 14t11 + 21t12 + 29t13 + 48t14 + 70t15 + O (
t16)

23

M24 1 + t2 + t3 + 2t4 + 2t5 + 5t6 + 5t7 + 11t8 + 14t9 + 25t10 + 35t11 + 65t12 + 89t13 + O (
t14)

Co3 1 + t2 + t4 + 2t6 + 3t8 + t9 + 5t10 + 2t11 + 9t12 + 3t13 + 14t14 + 7t15 + 23t16 + 13t17 + O (
t18)

Co2 1 + t2 + t4 + t6 + 2t8 + 3t10 + t11 + 5t12 + t13 + 7t14 + 2t15 + 11t16 + 3t17 + 16t18 + O (
t19)

Co1 1 + t2 + t4 + t6 + t8 + t10 + 2t12 + 2t14 + 3t16 + 4t18 + O (
t20)

Ru 1 + t4 + 2t8 + 6t12 + 2t14 + 22t16 + 27t18 + 154t20 + 439t22 + 1966t24 + 7189t26 + O (
t28)

He 1 + t3 + t4 + t5 + 4t6 + 5t7 + 13t8 + 30t9 + 82t10 + 245t11 + 907t12 + 3424t13 + O (
t14)

J1 1 + t2 + t3 + 8t4 + 34t5 + 361t6 + 2820t7 + 22346t8 + 156939t9 + 1021469t10 + O (
t11)

Fi22 1 + t2 + t4 + 2t6 + 5t8 + t9 + 13t10 + 4t11 + 60t12 + 31t13 + 488t14 + 912t15 + O (
t16)

HN 1 + t2 + t4 + 2t6 + t7 + 5t8 + 6t9 + 27t10 + 92t11 + 637t12 + 5018t13 + 47239t14 + O (
t15)

Th 1 + t2 + t4 + t6 + 4t8 + 15t10 + 50t11 + 1854t12 + 31610t13 + 607473t14 + O (
t15)

O’N 1 + 16t6 + 426595t9 + 14039408007t12 + 230067642077481t15 + O (
t18)

Fi23 1 + t2 + t3 + 2t4 + 3t5 + 9t6 + 15t7 + 57t8 + 324t9 + 7961t10 + 456255t11 + O (t12)

Fi24’ 1 + t3 + 3t6 + 11t9 + 355t12 + 17843536t15 + 1848868683076t18 + O (
t21)

J4 1 + t4 + 2t6 + 2t7 + 31t8 + 521t9 + 60960t10 + 7118797t11 + 795955946t12 + O (
t13)

Ly 1 + 23t6 + 21041t7 + 697156t8 + 191631120t9 + 47708455027t10 + O (
t11)

B 1 + t2 + 2t4 + 3t6 + 7t8 + 20t10 + 3t11 + 243t12 + 8164t13 + 2665262t14 + O (
t15)

M 1 + t2 + t3 + 2t4 + 2t5 + 6t6 + 6t7 + 16t8 + 27t9 + 68t10 + 182t11 + 956t12 + O (
t13)

References

[AS1976] V.I. Arnol’d and G. Shimura, VII. Superpositions of algebraic functions, in Problems of Present
Day Mathematics, Mathematical Developments Arising from Hilbert Problems, Proc. Symposia in Pure
Math, AMS, Providence, 28:45-46, 1976.

[BF2003] G. Berhuy and G. Favi, Essential dimension: a functorial point of view (after A. Merkurjev)., Doc.
Math., 8:279-330, 2003.

[Bra1975] R. Brauer, On the resolvent problem, Ann. Mat. Pura Appl., (4) 102:45-55, 1975.

[Bre2013] T. Breuer, The GAP Character Table Library, Version 1.2.2 ; 2013, available at
http://www.math.rwth-aachen.de/ Thomas.Breuer/ctbllib.

[BMO2017] T. Breuer, G. Malle, and E.A. O’Brien, Reliability and reproducibility of Atlas information,
Finite simple groups: thirty years of the atlas and beyond, Contemp. Math., 694:21-31, Amer. Math.
Soc., Providence, RI, 2017.

[BR1997] J. Buhler and Z. Reichstein, On the essential dimension of a ﬁnite group, Comp. Math., (2)
106:159-179, 1997.

[BF1966] N. Burgoyne and P. Fong, The Schur multipliers of the Mathieu groups, Nagoya Math J., 27:733-
745, 1966.

[BF1968] N. Burgoyne and P. Fong, A correction to: “The Schur multipliers of the Mathieu groups”, Nagoya
Math J., 31:297-304, 1968.

[Che1932] N.G. Chebotarev, Die Probleme der modernen Galoisschen Theorie, In:Proceeedings of the ICM,
1932.

[Che1934] N.G. Chebotarev, Die Probleme der modernen Galoisschen Theorie, Comment. Math. Helv.,
6:235-283, 1934.

[Che1954] G.N. Chebotarev, On the problem of resolvents, Kazan. Gos. Univ. U˘c. Zap., (2) 114:189-193,
1954.

[CGR2006] V. Chernousov, P. Gille, and Z. Reichstein, Resolving G-torsors by abelian base extensions, J.
Algebra, 296:561-581, 2006.
 24

[CCNPW1985] J.H. Conway, R.T. Curtis, S.P. Norton, R.A. Parker, and R.A. Wilson, ATLAS of ﬁnite
groups, Eynsham: Oxford University Press, 1985.

[DLP2023] H. Dietrich, M. Lee, and T. Popiel, The maximal subgroups of the Monster, 2023,
arXiv:2304.14646.

[Dol2012] I. Dolgachev, Classical Algebraic Geometry, Cambridge University Press, 2012.

[DR2015] A. Duncan and Z. Reichstein, Versality of algebraic group actions and rational points on twisted
varieties, with an appendix containing a letter from J.P. Serre, J. Algebraic Geom., 24(3):499-530, 2015.

[FKW2023] B. Farb, M. Kisin, and J. Wolfson, Modular functions and resolvent problems, with an appendix
by Nate Harman, Math. Ann., 386:113-150, 2023.

[FW2019] B. Farb, and J. Wolfson, Resolvent degree, Hilbert’s 13th problem and geometry, Enseign. Math.,
65(3-4):303-376, 2019.

[Flo2008] M. Florence, On the essential dimenion of cyclic p-groups, Invent. Math., 171:175-189, 2008.

[GAP2022] The GAP Group, GAP – Groups, Algorithms, and Programming, Version 4.12.1 ; 2022,
https://www.gap-system.org.

[GAP2015] The GAP Group, GAP – Groups, Algorithms, and Programming, Version 4.7.7 ; 2015,
https://www.gap-system.org.

[Ham1836] W. Hamilton, Inquiry into the validity of a method recently proposed by George B. Jerrard, esq.,
for transforming and resolving equations of elevated degrees, Report of the Sixth Meeting of the British
Association for the Advancement of Science, 295-348, 1836.

[HS2023] C. Heberle and A. Sutherland, Upper bounds on resolvent degree via Sylvester’s obliteration algo-
rithm, New York J. Math., 29:107-146, 2023.

[Hil1927] D. Hilbert, ¨Uber die Gleichung neunten Grades, Math. Ann., 97(1):243-250, 1927.

[Isa1976] I.M. Isaacs, Character theory of ﬁnite groups, Pure and App. Math., No. 69, Academic Press, New
York-London, 1976.

[Kle1879] F. Klein, Ueber die Auﬂ¨osung gewisser Gleichungen vom siebenten und achten Grade, Math. Ann.,
15:252-282, 1879.

[Kle1884] F. Klein, Vorlesungen ¨uber das Ikosaeder und die Auﬂ¨osung der Gleichungen vom f¨unften Grade,
Teubner, Leipzig, 1884

[Kle1887] F. Klein, Zur Theorie der allgemeinen Gleichungen sechsten und siebenten Grades, Math. Ann.,
28(4):499-532, 1887.

[Kle1905] F. Klein, ¨Uber die Auﬂ¨osung der allgemeinen Gleichungen f¨unften und sechsten Grades, J. Reine
Angew. Math., 129:150-174, 1905.

[Maz1979] P. Mazet, Sur le multiplicateur de Schur du groupe de Mathieu M22, C. R. Acad. Sci. Pari S´er.
A-B, 14:A659-A661, 1979.

[MS1983] A. Merkurjev and A. Suslin, K-Cohomology of Severi-Brauer Varieties and the Norm Residue
Homomorphism, Math. USSR Izv., 21(2):307-340, 1983.

[Mil1980] J.S. Milne, ´Etale cohomology, Princeton Math. Ser., No. 33, Princeton Univ. Press, Princeton, NJ,
1980.

[Mor1956] G.G. Morrice, English translation: Lectures on the icosahedron and solution of equations of the
ﬁfth degree, 2nd and rev. edition, Dover Pub., New York, NY, 1956.

25

[Poo2017] B. Poonen, Rational Points on Varieties, Graduate Studies in Mathematics, vol. 186, AMS,
xv+337pp, 2017.

[Rei2000] Z. Reichstein, On the notion of essential dimension for algebraic groups, Transform. Groups,
5(3):265-304,2000.

[Rei2021] Z. Reichstein, From Hilbert’s 13th problem to essential dimension and back, Eur. Math. Soc. Mag.,
122:4-15, 2021.

[Rei2022] Z. Reichstein, Hilbert’s 13th Problem for Algebraic Groups, to appear in Enseign. Math.

[RY2000] Z. Reichstein and B. Youssin, Essential dimensions of algebraic groups and a resolution theorem
for G-varieties, with an appendix by J. Koll´ar and E. Szab´o, Canad. J. Math., 52(5):1018-1056, 2000.

[Sag2022] The Sage Developers, SageMath, the Sage Mathematics Software System; 9.5, 2022,
https://www.sagemath.org.

[Seg1945] B. Segre, The Algebraic Equations of Degree 5, 9, 157..., and the Arithmetic Upon an Algebraic
Variety, Ann. of Math., 46(2):287-301, 1945.

[Sut2021] A. Sutherland, Upper Bounds on Resolvent Degree and Its Growth Rate, 2021, arXiv:2107:.08139.

[Tsc1683] E. von Tschirnhaus, Methodus auferendi omnes terminos intermedios ex data aequatione (Method
of eliminating all intermediate terms from a given equation), Acta Eruditorum, 204-207, 1683.

[Wil1986] R.A. Wilson, Is J1 a Subgroup of the Monster?, Bull. Lond. Math. Soc., 18(4):349-350, 1986.

[Wil2009] R.A. Wilson, The ﬁnite simple groups, Graduate Texts in Mathematics, vol. 251, Springer-Verlag
London, Ltd., London, xvi+298, 2009.

[Wil2017] R.A. Wilson, Maximal subgroups of sporadic groups, Finite simple groups: thirty years of the atlas
and beyond, Contemp. Math., 694:57-72, Amer. Math. Soc., Providence, RI, 2017.

[Wol2021] J. Wolfson, Tschirnhaus transformations after Hilbert, Enseign. Math., 66(3):489-540, 2021.

Author: Claudio G´omez-Gonz´ales

Aﬃliation: Carleton College; Department of Mathematics and Statistics

E-mail: cgonzales@carleton.edu

Author: Alexander J. Sutherland

Aﬃliation: The Ohio State University; Department of Mathematics

E-mail: sutherland.159@osu.edu

Author: Jesse Wolfson

Aﬃliation: University of California, Irvine; Department of Mathematics

E-mail: wolfson@uci.edu

MSC Classes: 14L30 (Primary); 13A50, 20C25, 20C34 (Secondary)

Keywords: resolvent degree, torsors, versality, rational points, sporadic groups, Monster group

26
