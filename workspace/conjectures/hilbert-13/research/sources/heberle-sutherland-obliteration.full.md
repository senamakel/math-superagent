<!-- source: https://arxiv.org/pdf/2110.08670 | converted from PDF -->

arXiv:2110.08670v2  [math.AG]  14 Nov 2022
Upper Bounds on Resolvent Degree via
Sylvester’s Obliteration Algorithm

Curtis Heberle and Alexander J. Sutherland
∗

Abstract

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
3.2 Sylvester’s Obliteration Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12

4 Upper Bounds on Resolvent Degree 14
4.1 Previous Bounds . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
4.2 New Bounds . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
4.3 Obstruction to Further Bounds via the Geometric Obliteration Algorithm . . . . . . . . . . . 18
4.4 Remaining Questions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20

5 Python Implementations of the Obliteration Algorithm and Related Phenomena 22
5.1 Appendix A: The Geometric Obliteration Algorithm . . . . . . . . . . . . . . . . . . . . . . . 22
5.2 Appendix B: Lemmata for Computational Improvements . . . . . . . . . . . . . . . . . . . . . 24
5.3 Appendix C: The Geometric Obliteration Algorithm with Computational Improvements . . . 27
5.4 Appendix D: The Geometric Obliteration Algorithm for Cm−d−1(τ1,...,d; P0, . . . , Pm−d−1) . . . 29

1 Introduction

A classical problem in mathematics is to determine the roots of a general degree n polynomial in one variable
in terms of its coeﬃcients. Modern work on this problem centers around resolvent degree, an invariant whose
ideas permeate classical work, but was not formally deﬁned until the independent deﬁnitions of Brauer
[Bra1975, p.46] and Arnol’d and Shimura [AS1976, p.46]. Farb and Wolfson greatly expanded the context of
resolvent degree in [FW2019, Deﬁnition 2.3, Proposition 2.4, Deﬁnition 3.1].

∗The second author was supported in part by the National Science Foundation under Grant No. DMS-1944862.

1

Following [Wol2021, Example 4.2], we denote the resolvent degree of the general degree n polynomial
by RD(n). Currently, non-trivial lower bounds on RD(n) are unknown [FW2019, Section 1.5]; it is possible
that RD(n) = 1 for all n. Nonetheless, Dixmier [Dix1993] noted that “Every reduction of RD(n) would be
serious progress,” and Wolfson provided new upper bounds on RD(n) [Wol2021, Theorems 5.6 and 5.8] by
constructing a “bounding function” F (m) such that RD(n) ≤ n − m for n ≥ F (m). The current best upper
bounds on RD(n) are given by [Sut2021C, Theorem 3.27], where the second-named author constructs an
improved bounding function G(m) and shows that lim
m!∞
 F (m)
G(m) = ∞.

In this paper, we recover an algorithm from [Syl1887] (henceforth referred to as the “obliteration al-
gorithm”) for solving systems of equations using polynomials of minimal degree. An additional modern
description of the Sylvester’s work and its relevance to resolvent degree is given in [Heb2021]. Here we
present the algorithm primarily from an algebro-geometric viewpoint using the language of “polar cones”
introduced in [Sut2021C, Section 2]. We then use the obliteration algorithm to determine the following new
upper bounds on resolvent degree:

Theorem 1.1. (Upper Bounds on Resolvent Degree)

1. For n ≥ 5, 250, 199, RD(n) ≤ n − 13.

2. For each 14 ≤ m ≤ 17 and n > (m−1)!
120 , RD(n) ≤ n − m.

3. For n ≥ 381, 918, 437, 071, 508, 901, RD(n) ≤ n − 22.

4. For each 23 ≤ m ≤ 25 and n > (m−1)!
720 , RD(n) ≤ n − m.

The above result is found as Theorem 4.6 in Section 4 and leads to the construction of a new bounding
function G
′(m) such that RD(n) ≤ n − m for n ≥ G
′(m) and G
′(m) ≤ G(m) in Corollary 4.9.

Historical Remarks The second-named author uses two distinct methods to construct G(m) [Sut2021C,
Theorems 3.7, 3.10, 3.24]. For general m (Theorem 3.24), the second-named author uses a result of Debarre
and Manivel [DM1998, Theorem 2.1] to improve on the construction of Wolfson which underlies [Wol2021,
Theorem 5.6]. For small m (Theorems 3.7 and 3.10), the second-named author uses iterated polar cone
methods which build upon the methods of [Wim1927], [Che1954], and [Seg1945] (note, however, that Wiman
and Chebotarev do not use the language of polars at all and Segre refers only to individual polars). An
application of Sylvester’s obliteration algorithm to certain small m cases is considered in [Heb2021]. By
combining Sylvester’s obliteration algorithm with the other methods described above, the authors believe
they have exhausted the classical methods related to the theory of Tschirnhaus transformations; implications
of this are discussed in Subsection 4.4.

Outline of the Paper In Section 2, we recall the relevant background on resolvent degree, polar cones,
and Tschirnhaus transformations. In Section 3, we present a modern, geometric version of the obliteration
algorithm and related phemonena, as well as a summary of Sylvester’s original work. In Section 4, we apply
the geometric obliteration algorithm to obtain upper bounds on resolvent degree. In Section 5, we discuss
Python implementations of the geometric obliteration algorithm used for computations relevant for Theorem
4.6.

Conventions

1. We restrict to ﬁelds K which are ﬁnitely generated C-algebras. One could instead ﬁx an arbitrary
algebraically closed ﬁeld F of characteristic zero (in lieu of C) and the statements (relative to F ) would
hold.

2. We follow the conventions of [Har2010] for algebraic varieties. In particular, a projective (respectively,
aﬃne) variety is deﬁned to be a closed algebraic set in Pr
K (respectively, Ar
K). When we say variety
without a speciﬁc modiﬁer, we mean a quasi-projective variety. Note that we do not assume that
varieties are irreducible.

3. Given a, b ∈ Z≥0, we set [a, b] = {x ∈ Z | a ≤ x ≤ b}.

2

4. Given a collection of homogeneous polynomials S = {f1, . . . , fs} ⊆ K[x0, . . . , xr], we write V(f1, . . . , fs)
(and occasionally V(S)) for the subvariety of Pr
K determined by the conditions f1 = · · · = fs = 0.

5. Given a subvariety V ⊆ Pr
K, we write V (K) for the set of K-rational points of V .

6. Given points P0, . . . , Pℓ ∈ Pr(K), we write Λ(P0, . . . , Pℓ) for the linear subvariety of Pr
K that they
determine. Additionally, we refer to a linear subvariety Λ ⊆ Pr
k of dimension k ≥ 3 as a k-plane. We
refer to linear subvarieties of dimension 1 (respectively, 2) as lines (respectively, planes).

7. We use the notation Kn to mean C(a1, . . . , an), a purely transcendental extension of C with transcen-
dence basis a1, . . . , an.

Note that for generic choices of f1, . . . , fs, V(f1, . . . , fs) is a complete intersection. However, there are
examples of such choices which are not complete intersections, such as the twisted cubic curve. Following
the convention of [Sut2021C], we refer to a subvariety V(f1, . . . , fs) as an intersection of hypersurfaces.
Consider a system of equations S where each polynomial has degree at most d and where we denote the

number of polynomials of degree j by ℓj. In such a case, we say that S is of type [ d · · · 1
ℓd · · · ℓ1
]. If ℓj = 0 for

any j ∈ [1, d − 1], the corresponding column may be omitted from the presentation. When d ≥ 2 and each
ℓj = 1, we say S is of type (1, . . . , d).
When V = V (f1, . . . , fs), we say that the type of V is the type of the system {f1, . . . , fs}. We note that
the type of V explicitly depends on the presentation in terms of f1, . . . , fs; it is not unique. However, we
only consider the type of an intersection of hypersurfaces when it is deﬁned by an explicit set of polynomials.

Acknowledgements The authors thank David Ishii Smyth and Jesse Wolfson for their support. The sec-
ond author thanks Joshua Jordan for helpful conversations. Additionally, the authors thank the anonymous
referee for many helpful comments and suggestions.

2 Resolvent Degree, Polar Cones, and Tschirnhaus Transforma-
tions

2.1 Resolvent Degree

We refer the reader to [FW2019] for general deﬁnitions of resolvent degree (Deﬁnitions 1.3, 2.3), a summary
of its history (Section 1), and additional context. We only work over C and thus provide deﬁnitions in this
context.

Deﬁnition 2.1. (Resolvent Degree of Field Extensions)
Let K ′/K be an extension of C-ﬁelds. The resolvent degree of K ′/K, denoted RD (L/K), is the minimal
d for which there exists a tower of ﬁnite extensions

K = E0 ֒! E1 ֒! · · · ֒! Eℓ

such that K ′ embeds into Eℓ over K and the essential dimension of each Ej+1/Ej is at most d.

Deﬁnition 2.2. (Resolvent Degree of Generically Finite, Dominant Maps)
Let Y 99K X be a generically ﬁnite, dominant rational map of C-varieties. The resolvent degree of Y 99K X,
denoted RD (Y 99K X), is the minimal d for which there exists a tower of generically ﬁnite, dominant rational
maps Eℓ 99K · · · 99K E1 99K E0 = X

such that Eℓ 99K X factors as Eℓ 99K Y 99K X and the essential dimension of each Ej+1 99K Ej is at most d.

We ﬁrst note that Deﬁnitions 2.1 and 2.2 agree and is induced by sending an irreducible aﬃne variety X
to the corresponding ﬁeld of rational functions C(X). We refer the reader to [FW2019, Deﬁnition 1.3] for a
precise deﬁnition of essential dimension, but note that we often use approximate essential dimension via the
bounds ed (K ′/K) ≤ tr.deg (K) and ed (Y 99K X) ≤ dim(X).

3

We write RD(n) for the resolvent degree of the general degree n polynomial, which is given precisely as

RD(n) = RD (Cn 99K Cn/Sn) ,

= RD (
C (a1, . . . , an) [z]/ (
zn + a1zn−1 + · · · an−1z + an) /C (a1, . . . , an)
) .

Additionally, resolvent degree is deﬁned for ﬁnite groups [FW2019, Deﬁnition 3.1] and RD(n) = RD (Sn) =
RD (An) [FW2019, Theorem 3.3, Corollary 3.17].
While we restrict ourselves to working over C, we do note lose any generality. Theorem 1.2 of [Rei2022]
yields that RDC (Sn) = RDK (Sn) for any ﬁeld K of characteristic zero and [Rei2022, Theorem 1.3] yields
that RDC (Sn) ≥ RDK (Sn) for any ﬁeld K, i.e. resolvent degree can only go down in positive characteristic.
In Lemma 2.3, we summarize several basic results which will be used frequently (and often without explicit
reference). Item 1 is the ﬁeld-theoretic version of [FW2019, Lemma 2.7] and follows immediately from the
deﬁnition of resolvent degree. Items 2 and 3 are algebraic versions of [FW2019, Lemma 2.9] and can be found
explicitly as follows as [Sut2021C, Lemma 2.18, Proposition 2.19]. Note that items 2 and 3 follow directly
from the primitive element theorem.

Lemma 2.3. (Properties of Resolvent Degree)

1. Let E0 ֒! E1 ֒! · · · ֒! Eℓ be a tower of ﬁeld extensions. Then,

RD(Eℓ/E0) = max {RD(Ej/Ej−1) | j ∈ [1, ℓ]} .

2. Let K ′/K be a degree d ﬁeld extension. Then, RD(K ′/K) ≤ RD(d).

3. Let V ⊆ Pr
K be a degree d subvariety. Then, there is an extension K ′/K with RD(K ′/K) ≤ RD(d)
over which we can determine a K ′-rational point of V .

As a consequence of item 3, we say that we can determine a point of a degree d subvariety V by solving a
degree d polynomial.

2.2 Polar Cones and k-Polar Points

The original theory of polars for hypersurfaces is classical and a classical reference is [Ber1923]; a modern
reference on polars is [Dol2012]. We now recall the key deﬁnitions and results of [Sut2021C, Section 2]; we
use the same notation and begin with the deﬁnition of polars.

Deﬁnition 2.4. (Polars and Polar Cones)
Let f ∈ K[x0, . . . , xr] be a homogeneous polynomial of degree d and P ∈ Pr(K). Observe that the set

I ∗
j := HomSet ([1, j], [0, r])

indexes the (ordered) jth partial derivatives of f for each j ∈ [0, d]. We also use the shorthand

∂j0
0 · · · ∂jℓ
ℓ = ∂j0+···+jℓ

∂x
j0
0 · · · ∂x
jℓ
ℓ .

For each j ∈ [0, d], the jth polar of f at P is the homogeneous polynomial

t(j, f, P ) := ∑

ι∈I ∗
d−j
 (
∂|ι−1(0)|
0 · · · ∂|ι−1(r)|
r f )∣
∣
∣
∣P x
|ι−1(0)|
0 · · · x
|ι−1(r)|
r , (1)

which is of degree d − j. Next, consider the hypersurface H = V(f ). The jth polar of H at P is

T (j, f, P ) := V(t(j, f, P )) ⊆ Pr
K.

Finally, the (ﬁrst) polar cone of H at P is

C(H; P ) :=
 d−1⋂

j=0 T (j, f, P ).

4

Note that T (0, f, P ) = H for all P and T (d, f, P ) = Pr
K if P ∈ H(K). If H is smooth at P , then
T (d − 1, f, P ) is the tangent hyperplane of H at P . Our interest in polars stems from our interest in polar
cones, which are themselves motivated by the following classical result (which is stated as a fact in [Seg1945,
I.5, p.292]; Segre refers readers to [Ber1923, p.203]).

Lemma 2.5. (Bertini’s Lemma for Hypersurfaces)
Let H ⊆ Pr
K be a hypersurface and P ∈ H(K). Then, C(H; P ) ⊆ H is a cone with vertex P .

In particular, for any point Q ∈ C(H; P ) \ {P }, the line Λ(P, Q) lies in H.
Observe that for an intersection of hypersurfaces V(f1, . . . , fs), a line Λ lies on V(f1, . . . , fs) exactly when
Λ lies on each hypersurface V(fj). This observation motivates the following deﬁnition and lemma, which are
originally given as [Sut2021C, Deﬁnition 2.10, Lemma 2.11].

Deﬁnition 2.6. (Polar Cone of an Intersection of Hypersurfaces)
Let V = V(f1, . . . , fs) ⊆ Pr
K be an intersection of hypersurfaces and P ∈ V (K). The (ﬁrst) polar cone of
V at P is
 C(V ; P ) :=
 s⋂

j=1 C(V(fj); P ).

Lemma 2.7. (Bertini’s Lemma for Intersections of Hypersurfaces)
Let V ⊆ Pr
K be an intersection of hypersurfaces and P ∈ V (K). Then, C(V ; P ) ⊆ V is a cone with vertex P .

Iterating the polar cone construction yields a method for determining k-planes on intersections of hyper-
surfaces. We now recall the associated deﬁnitions, ﬁrst given as [Sut2021C, Deﬁnition 2.22].

Deﬁnition 2.8. (Iterated Polar Cones and k-Polar Points)
Let V ⊆ Pr
K be an intersection of hypersurfaces and P0 ∈ V (K). First, set C1(V ; P0) := C(V ; P0). Given
additional points P1, . . . , Pk−1 ∈ V (K) such that

Pℓ ∈ Cℓ(V ; P0, . . . , Pℓ−1) \ Λ (P0, . . . , Pℓ−1)

for ℓ ∈ [1, k − 1], the kth polar cone of V at P0, . . . , Pk−1 is

Ck(V ; P0, . . . , Pk−1) := C (
Ck−1(V ; P0, . . . , Pk−2); Pk−1) .

We refer to an ordered collection of such points (P0, . . . , Pk) as a k-polar point of V .
If the points P0, . . . , Pk−1 have already been chosen, we refer to Ck(V ; P0, . . . , Pk−1) as the kth polar cone
of V . In the event that such points exist, but have not been explicitly chosen, we refer to a kth polar cone of
V . Additionally, it is sometimes useful to refer to V itself as a zeroth polar cone of V (at any of its K-points).

By noting that iterated polar cones are nested, i.e.

Ck(V ; P0, . . . , Pk−1) ⊆ Ck−1(V ; P0, . . . , Pk−2) ⊆ · · · ⊆ C2(V ; P0, P1) ⊆ C(V ; P0) ⊆ V

and that the points P0, . . . , Pk deﬁning a k-polar point (P0, . . . , Pk) are in general position, we arrive at the
following k-plane analogue of Lemma 2.7, which is originally [Sut2021C, Lemma 2.24]:

Lemma 2.9. (Polar Point Lemma)
Let V ⊆ Pr
K be an intersection of hypersurfaces and let (P0, . . . , Pk) be a k-polar point of V . Then,
Λ(P0, . . . , Pk) ⊆ Ck(V ; P0, . . . , Pk−1) ⊆ V is a k-plane.

2.3 Tschirnhaus Transformations

We use the notation and conventions of [Sut2021C, Subsection 3.1] for Tschirnhaus transformations and
refer the reader there for details. Note also that Wolfson provides a more complete history of Tschirnhaus
transformations in [Wol2021, Section 2 and Appendix B]. Let Kn = C(a1, . . . , an) be a purely transcendental
extension of C with transcendence basis a1, . . . , an.
 5

Deﬁnition 2.10. (General Polynomials)
The general polynomial of degree n is the polynomial

φn(z) = zn + a1zn−1 + · · · + an−1z + an ∈ Kn[z].

Deﬁnition 2.11. (Tschirnhaus Transformations)
A Tschirnhaus transformation of the general degree n polynomial is an isomorphism of Kn-ﬁelds

Υ : Kn[z]/(φn(z)) ! Kn[z]/(ψ(z)),

where ψ(z) = zn + b1zn−1 + · · · + bn−1z + bn. We say that Υ has type (j1, . . . , jk) if bj1 = · · · = bjk = 0.

As per Remark 3.3 of [Sut2021C], the space of all Tschirnhaus transformations of the general degree n
polynomial (up to re-scaling) is
 T n
Kn := Pn−1
Kn \ [1 : 0 : · · · : 0] ⊆ Pn−1
Kn .

Note that each bj in Deﬁnition 2.11 is a homogeneous polynomial of degree j in a1, . . . , an.

Deﬁnition 2.12. (Tschirnhaus Complete Intersections)
Fix n ∈ Z≥1. For any m ∈ [1, n − 1], the mth extended Tschirnhaus hypersurface is

τm := V(bm) ⊆ Pn−1
Kn ,

and the mth extended Tschirnhaus complete intersection is

τ1,...,m :=
 m⋂

j=1 τj ⊆ Pn−1
Kn .

Additionally, the mth Tschirnhaus hypersurface is

τ ◦
m := τm ∩ T n
Kn = τm \ {[1 : 0 : · · · : 0]} ,

and the mth Tscihrnhaus complete intersection is

τ ◦
1,...,m := τ1,...,m ∩ T n
Kn = τ1,...,m \ {[1 : 0 : · · · : 0]} .

Remark 2.13. (Strategy for Upper Bounds on RD(n)
If we can determine a K ′-rational point of τ ◦
1,...,m−1 over an extension K ′/Kn of suﬃciently small resolvent
degree, then we can conclude that RD(n) ≤ n − m. Notice that if we can determine an (m − d − 1)-plane
Λ ⊆ τ ◦
1,...,d over an extension L/Kn of low resolvent degree, then we need only further pass to an extension

K ′/L with RD(K ′/L) ≤ RD ( (m−1)!
d! ), by Lemma 2.3.

Lemma 2.9 yields that every k-polar point determines a k-plane, hence Remark 2.13 yields that it will
suﬃce to determine k-polar points on the Tschirnhaus complete intersections τ ◦
1,...,d.

3 The Obliteration Algorithms

In [Syl1887], Sylvester gives an algorithm to determine an upper bound on the number of variables required
to determine a non-trivial solution for a system of homogeneous polynomials of given degrees by solving
polynomials of the same, or lower, degrees. The algorithm centers on Sylvester’s “formula of obliteration”
[Syl1887, p.475], which will be covered in detail in Corollary 3.12 and Proposition 3.15. Consequently, we refer
to Sylvester’s method as the “obliteration algorithm.” In Subsection 3.1, we give a modern description of the
obliteration algorithm via geometry (in terms of varieties, rational points, and polar cones). In Subsection
3.2, we describe the obliteration algorithm in terms of systems of homogeneous polynomials and explain
Sylvester’s classical language.
 6

3.1 The Geometric Obliteration Algorithm

WE now give a geometric construction of Sylvester’s obliteration algorithm. More speciﬁcally, given an
intersection of hypersurfaces V ⊆ Pr
K, we give a bound on the ambient dimension required to be able to
determine a point of V over an extension K ′/K of bounded resolvent degree. Note that this bound depends
only on the type of V .

Deﬁnition 3.1. (Minimal Dimension Bound)

The minimal dimension bound of type [ d · · · 1
ℓd · · · ℓ1
], denoted r(d; ℓd, . . . , ℓ1) is the minimal r′ ∈

Z≥1 ∪ {∞} such that whenever r ≥ r′, we can determine a point of any intersection of hypersurfaces of

type [ d · · · 1
ℓd · · · ℓ1
] in Pr
K over an extension K ′/K with RD (K ′/K) ≤ RD(d). Given an intersection of

hypersurfaces V of type [ d · · · 1
ℓd · · · ℓ1
], we set r(V ) := r(d; ℓd, . . . , ℓ1).

Remark 3.2. (Finiteness of the Minimal Dimension Bound)
The main goal of this section is to establish an upper bound on r(d; ℓd, . . . , ℓ1). More speciﬁcally, we introduce
a recursive, combinatorial bound g(d; ℓd, . . . , ℓ1) in Deﬁnition 3.3 which we will show satisﬁes

r(d; ℓd, . . . , ℓ1) ≤ g(d; ℓd, . . . , ℓ1). (2)

The proof of inequality (2) is exactly the geometric version of the obliteration algorithm.

We now give Deﬁnition 3.3 and note that the underlying geometric intuition is explained in Lemma 3.5
and Remark 3.6.

Deﬁnition 3.3. (Geometric Dimension Bound)

The geometric dimension bound of type [ 1
ℓ1
] is g(1; ℓ1) := ℓ1. Similarly, the geometric dimension bound

of type [2 1
1 ℓ1
] is g(2; 1, ℓ1) := 1 + ℓ1 and the geometric dimension bound of type [ 2 1
ℓ2 ℓ1
] with ℓ2 ≥ 2 is

g(2; ℓ2, ℓ1) := g(2; ℓ2 − 1, ℓ2 + ℓ1 + 1).

For d ≥ 3, the geometric dimension bound of type [d d − 1 · · · 2 1
1 ℓd−1 · · · ℓ2 ℓ1
] is

g(d; 1, ℓd−1, . . . , ℓ2, ℓ1) := g
 

d − 1; ℓd−1, (ℓd−1 + ℓd−2), . . . ,
 d−1∑

j=2 ℓj,
 

d−1∑

j=1 ℓj


 + 1


 .

For d ≥ 3 and ℓd ≥ 2, the geometric dimension bound of type [d d − 1 · · · 2 1
1 ℓd−1 · · · ℓ2 ℓ1
] is

g(d; ℓd, ℓd−1, . . . , ℓ2, ℓ1) := g
 

d; ℓd − 1, (ℓd + ℓd−1) − 1, . . . ,
 

 d∑

j=2 ℓj


 − 1,
 d−1∑

j=1 ℓj


 .

Finally, given an intersection of hypersurfaces V of type [ d d − 1 · · · 2 1
ℓd ℓd−1 · · · ℓ2 ℓ1
], we set

g(V ) := g(d; ℓd, . . . , ℓ1).

Remark 3.4. (Hyperplane Identities)
The deﬁnitions of both the minimal and geometric dimension bounds admit a “hyperplane identity,” which
we use without explicit reference:

1 + r(d; ℓd, . . . , ℓ2, ℓ1) = r(d; ℓd, . . . , ℓ2, ℓ1 + 1),
1 + g(d; ℓd, . . . , ℓ2, ℓ1) = g(d; ℓd, . . . , ℓ2, ℓ1 + 1).

7

We next state Lemma 3.5, which is the technical underpinning of the geometric obliteration algorithm
and which specializes to give the geometric version of Sylvester’s formula of reduction.

Lemma 3.5. (The Reduction Lemma)

Let V be an intersection of hypersurfaces of type [ d · · · 1
ℓd · · · ℓ1
] with d ≥ 2 and which is not a hypersurface.

Take Vd to be a degree d hypersurface and V red to be an intersection of hypersurfaces of type
[ d · · · 1
ℓd − 1 · · · ℓ1
]

if ℓd ≥ 2 and of type [d − 1 · · · 1
ℓd−1 · · · ℓ1
]

if ℓd = 1, such that V = V red ∩ Vd. Let P ∈ V red(K) and take H to be a hyperplane which does not contain
P . Then, g(V ) = g(H ∩ C(V red; P )) = g(C(V red; P )) + 1.

Proof. First, consider when ℓd ≥ 2. From Deﬁnition 2.6, observe that C(V red; P ) has type




 d · · · 1

ℓd − 1 · · ·
 ( d∑

j=1 ℓj
)
 − 1




 .

.
From Deﬁnition 3.3, it follows that

g(V ) = g(d; ℓd, . . . , ℓ1)

= g
 

d; ℓd − 1, (ℓd + ℓd−1) − 1, . . . ,
 

 d∑

j=2 ℓj


 − 1,
 d∑

j=1 ℓj




= g (
C(V red; P )
) + 1

= g (
H ∩ C(V red; P )
) .

Similarly, when ℓd = 1, we have

g(V ) = g(d; ℓd, . . . , ℓ1)

= g
 

d − 1; ℓd−1, (ℓd + ℓd−1), . . . ,
 d∑

j=2 ℓj,
 

 d∑

j=1 ℓj


 + 1




= g (
C(V red; P )
) + 1

= g (
H ∩ C(V red; P )
) .

Remark 3.6. (Geometric Insight for the Reduction Lemma)
The proof of Lemma 3.5 follows immediately from Deﬁnition 3.3, but we wish to address the geometric
reasoning underlying the lemma. Suppose our goal is to determine a point Q of V over an extension of
bounded resolvent degree. Observe that if we can determine a line Λ ⊆ V red, then we need only solve a
degree d polynomial to determine a point of V . As V red is V with Vd removed, it is already “less diﬃcult” to
determine the point P ∈ V red(K) given by assumption (i.e. g(V ) ≥ g(V red)). Additionally, we can determine
a line Λ ⊆ V red by determining a point P ′ ̸= P of C(V red; P ). As H is taken to be a hyperplane which does
not contain P , it suﬃces to determine any point of C(V red; P ) ∩ H, which is also “less diﬃcult” as C(V red; P )
is deﬁned by fewer top degree hypersurfaces.

As in Lemma 3.5, we will frequently want to split an intersection of hypersurfaces V into parts analogous
to V red and Vd, and so we introduce the following terminology and notation.

8

Deﬁnition 3.7. (Reduction and Complement)

Given an intersection of hypersurfaces V of type [ d · · · 1
ℓd · · · ℓ1
] with ℓd ≥ 2, a reduction of V is an inter-

section of hypersurfaces V red of type [ d d − 1 · · · 2 1
ℓd − 1 ℓd−1 · · · ℓ2 ℓ1
] such that V = V red ∩ Vd for some degree

d hypersurface Vd, we which refer to as a complement of V red for V .

When V is an intersection of hypersurfaces of type [ d · · · 1
ℓd · · · ℓ1
] with ℓd = 1, a reduction of V is an

intersection of hypersurfaces V red of type [d − 1 · · · 1
ℓd−1 · · · ℓ1
] such that V = V red ∩ Vd for some degree d

hypersurface Vd, we which refer to as a complement of V red for V .

With Lemma 3.5 and Deﬁnition 3.7 in place, we now state the geometric version of Sylvester’s “formula
of reduction” [Syl1887, p.475].

Corollary 3.8. (Geometric Formula of Reduction)

Let W be an intersection of hypersurfaces of type [ d · · · 1
ℓd · · · ℓ1
]. Then, for any P0 ∈ W (K), any reduction

C(W ; P0)
red, and any P1 ∈ C(W ; P0)
red(K), we have

g (C(W ; P0)) = g (
C (
C(W ; P0)
red; P1)) + 1.

Proof. This follows immediately as a special case of Lemma 3.5 applied to V = C(W ; P0).

We will soon want to successively iterate Lemma 3.5 so that we can eliminate the hypersurfaces of largest
degree from any intersection of hypersurfaces by introducing many hypersurfaces of strictly lower degree.
This is achieved in Proposition 3.10. However, we ﬁrst introduce additional language and notation to refer
to the varieties which arise in this process of reduction.

Deﬁnition 3.9. (Sylvester Reductions)

Let V be an intersection of hypersurfaces of type [ d · · · 1
ℓd · · · ℓ1
] with d ≥ 2 and which is not a hypersurface.

A ﬁrst partial Sylvester reduction of V is

V Syl(d; 1) := C(V red; P0),

where V red is any reduction of V and P0 ∈ V red(K). Proceeding inductively, for any j ∈ [2, ℓd], a jth partial
Sylvester reduction of V is

V Syl(d; j) := C(Hj−1 ∩ V Syl
j−1; Pk) = Hj−1 ∩ C(V Syl
j−1; Pk),

where Hj−1 is a hyperplane which does not contain Pj−1 and Pj ∈ (Hk−1 ∩ V Syl
k−1(d; j − 1)
) (K).
When d ≥ 3, a ﬁrst Sylvester reduction of V is

V Syl
1 := V Syl(d; ℓd).

For each j ∈ [2, d − 1], let λd−j+1 be the number of degree d − j + 1 hypersurfaces deﬁning a (j − 1)
st Sylvester
reduction V Syl
j−1. Then, a jth Sylvester reduction of V is

V Syl
j := (V Syl
j−1)Syl (d − j + 1; λd−j+1).

Continuing with the notation of Deﬁnition 3.9, note that V Syl
j is a variety obtained by repeatedly applying
Lemma 3.5 to V to remove all hypersurfaces of degree > d − j.

9

Proposition 3.10. (The Obliteration Proposition)

Let V be an intersection of hypersurfaces of type [ d · · · 1
ℓd · · · ℓ1
] with d ≥ 2 which is not a hypersurface.

Then, g(V ) = g (
V Syl
1 ) .

for any ﬁrst Sylvester reduction V Syl
1 of V .

Proof. From Lemma 3.5 and Deﬁnition 3.9, it follows immediately that

g (
V Syl(d; j)
) = g (
V Syl(d; j + 1)
)

for each j ∈ [1, ℓd − 1]. Consequently, applying Lemma 3.5 to V and its partial Sylvester reductions yields

g(V ) = g (
V Syl(d; 1)
) = · · · = g (
V Syl(d; ℓd − 1)
) = g (
V Syl(d; ℓd)
) = g (V Syl
1 ) .

Remark 3.11. (Geometric Dimension Bound via Obliteration)
From the deﬁnition of the jth Sylvester reductions, we can iteratively apply Proposition 3.10 to observe that

g(V ) = g (
V Syl
1 ) = · · · = g (
V Syl
d−2) = g (V Syl
d−1) ,

which provides the most succinct description of the central argument of the geometric obliteration algorithm.

We now arrive at the geometric version of Sylvester’s “formula of obliteration” as a specialization of
Proposition 3.10.

Corollary 3.12. (Geometric Formula of Obliteration)

Let W be an intersection of hypersurfaces of type [ d · · · 1
ℓd · · · ℓ1
] with d ≥ 2. For any P0 ∈ W (K) and any

Sylvester reduction C(W ; P0)
Syl
1 , we have

g(C(W ; P0)) = g (
C(W ; P0)
Syl
1 ) . (3)

Proof. This follows immediately as a special case of Proposition 3.10 with V = C(W ; P0).

Remark 3.13. (Explicit Numerics of the Formula of Obliteration)
Sylvester’s formula of obliteration [Syl1887, p.475], which we address in Proposition 3.15, is given nu-
merically and, for notational reasons, he chooses to write the statement in terms of “linear solutions” of
C(W ; P0)
Syl(d; ℓd − 1) instead of g (C(W ; P0)
Syl
1 )
. For this reason, we delay the discussion of numerics of the
formula of obliteration to Subsection 3.2.

As we have established the reduction lemma and the obliteration proposition, which we used to recover
Sylvester’s formula of reduction and formula of obliteration, we proceed to prove inequality (2).

Proposition 3.14. (Minimal vs. Geometric Dimension Bound)

For every type [ d · · · 1
ℓd · · · ℓ1
] of an intersection of hypersurfaces, r(d; ℓd, . . . , ℓ1) ≤ g(d; ℓd, . . . , ℓ1) < ∞.

Proof. (The Geometric Obliteration Algorithm)
We proceed by induction on d. First, observe that when d = 1, it is immediate that

r(1; ℓ1) = ℓ1 = g(1; ℓ1).

We additionally consider the case d = 2 before considering the general case. For the d = 2 case, we proceed
via induction on ℓ2. When ℓ2 = 1, deg(V ) = 2 and thus we can determine a point of V by solving a quadratic
polynomial when
 dim (V ) ≥ r − (ℓ1 + 1) = 0.

10

It follows that
 r(2; 1, ℓ1) = ℓ1 + 1 = g(2; 1, ℓ1).

Now, consider the case where ℓ2 ≥ 2 is arbitrary. Our inductive hypothesis yields

r(2; ℓ2 − 1, λ1) ≤ g(2; ℓ2 − 1, λ1),

for any λ1 ≥ 0. Let V red be a reduction of V with complement V2. As V red is of type [ 2 1
ℓ2 − 1 ℓ1
], we

can determine a point P0 of V red over an iterated quadratic extension whenever r ≥ g(V red). Let H be

a hypersurface which does not contain P0. Note that H ∩ C(V red; P0) is of type [ 2 1
ℓ2 − 1 ℓ2 + ℓ1
] and so

we can similarly determine a point P1 of H ∩ C(V red; P0) over an iterated quadratic extension whenever
r ≥ g(V red) + 1. From Lemma 2.7, we have that

Λ(P0, P1) ⊆ C(V red; P0) ⊆ V red.

Thus, we can determine a point of Λ(P0, P1) ∩ V2 ⊆ V over an additional quadratic extension. From Lemma
3.5, it follows that

r(2; ℓ2, ℓ1) ≤ max {g(2; ℓ2 − 1, ℓ1), g(2; ℓ2 − 1, ℓ1 + ℓ2)} = g(2; ℓ2 − 1, ℓ1 + ℓ2) = g(2; ℓ2, ℓ1).

Now, let us return to our induction on d and consider the case of general d ≥ 2. Our inductive hypothesis
for d yields that r(d−1; λd−1, . . . , λ1) ≤ g(d−1; λd−1, . . . , λ1) for any λd−1 ≥ 1 and λj ≥ 0 for all j ∈ [1, d−2].
We proceed by induction on ℓd. Let V red be a reduction of V with complement Vd. When ℓd = 1, the inductive
hypothesis on d yields that we can determine a point P0 of V red by solving polynomials of degree at most d−1
when r ≥ g(V red). Letting H denote a hyperplane which does not contain P0, we can similarly determine a
point P1 of H ∩ C(V red; P0) over by solving polynomials of degree at most d − 1 when r ≥ g (
C(V red; P0)
) + 1.
It follows that Λ(P0, P1) ⊆ C(V red; P0) ⊆ V red,

and so we can determine a point of Λ(P0, P1) ∩ Vd ⊆ V by solving a degree d polynomial. As a result,

r(d; 1, ℓd−1, . . . , ℓ1) ≤ max {
g(V red), g (
C(V red; P0)
) + 1} = g (C(V red; P0)
) + 1 = g(V ) = g(d; 1, ℓd−1, . . . , ℓ1).

Next, we consider the case of arbitrary ℓd ≥ 2. Our inductive hypothesis for ℓd yields that

r(d; ℓd − 1, λd−1, . . . , λ1) ≤ g(d; ℓd − 1, λd−1, . . . , λ1),

for all λj ≥ 0, j ∈ [1, d − 1]. As a result, we can determine a point P0 of V red by solving polynomials of degree
at most d when r ≥ g(V red). Taking H to be a hyperplane which does not contain P0, we can determine
a point P1 of H ∩ C(V red; P0) by solving polynomials of degree at most d when r ≥ g (
C(V red; P0)
) + 1.
Therefore, Λ(P0, P1) ⊆ C(V red; P0) ⊆ V red,

and we can determine a point a point of Λ(P0, P1) ∩ Vd ⊆ V by solving an additional degree d polynomial.
Consequently,

r(d; ℓd, . . . , ℓ1) ≤ max {g(V red), g (
C(V red; P0)
) + 1} = g (
C(V red; P0)
) + 1 = g(V ) = g(d; ℓd, . . . , ℓ1).

Finally, we note that the polar cone construction introduces only ﬁnitely many hypersurfaces, all of which
are strictly smaller degree. Consequently, iterating Lemma 3.5 yields that g(d; ℓd, . . . , ℓ1) is ﬁnite for every

type [ d · · · 1
ℓd · · · ℓ1
].
 11

3.2 Sylvester’s Obliteration Algorithm

In [Syl1887], Sylvester writes

“In the following memoir I propose to present Hamilton’s process under what appears to me to
be a clearer and more easily intelligible form, to extend his numerical results and to establish the
principles of a more general method than that to which he has conﬁned himself.”

We now propose to serve the analogous role for Sylvester that Sylvester served for Hamilton. Note that
[Syl1887] begins with a “a somewhat more extended statement of the Law of Inertia (Tr¨agheitsgesetz) for
quadratic forms” and provides a brief history of the theory of Tschirnhaus transformations, both of which
we omit here. Sylvester’s law of inertia is well-known (see [Ost1959, Section 1]) and not necessary for our
purposes. We refer the reader to [Wol2021, Section 2 and Appendix B] for a more complete history of
Tschirnhaus transformations.
Throughout this subsection, we consider a system S = {f1, . . . , fs} of homogeneous polynomials. Given
a solution P0 of S, the “ﬁrst emanant” [Syl1887, p.471] of S at P0 is

S(1; P0) := {t(ℓ, fj, P0) | j ∈ [1, s], ℓ ∈ [0, deg(fj) − 1]} ,

where t(ℓ, fj, P0) is as in equation (1) of Deﬁnition 2.4. Given a solution P1 of S(1; P0), Sylvester’s sub-lemma
[Syl1887, p.472] states that any linear combination λ0P0 + λ1P1 (what he calls an “alliance” of P0 and P1) is
a solution of S(1; P0), where [λ0 : λ1] ∈ P1(K). Consequently, Sylvester says that P0 and P1 deﬁne a “linear
solution” of S(1; P0) (and thus also of S, since S ⊆ S(1; P0)).
Note that the geometric version of Sylvester’s sub-lemma [Syl1887, p.472] is Lemma 2.7. The core
algebraic computation reduces to the case of hypersurfaces; see Lemma 2.8 of [Sut2021C]. Additionally, just
as the second-named author constructs iterated polar cones in [Sut2021C], Sylvester analogously introduces
“rth emanants” [Syl1887, p.472] and “the Lemma” [Syl1887, p.472] is the analogue of the polar point lemma
(Lemma 2.9). His proof follows from iterating the sublemma.
Sylvester now focuses on linear solutions [Syl1887, p.475] of systems of equations. First, he introduces
“completed emanants” [Syl1887, p.475] to ensure that P1 is distinct from P0 (and thus P0 and P1 determine a
genuine linear solution). More speciﬁcally, a completed emanant is a system of equations T = S(1; P0) ∪ {g},

where g is a homogeneous linear polynomials such that g(P0) ̸= 0. Next, let S be of type [ d · · · 1
ℓd · · · ℓ1
]
.

Sylvester introduces notation [Syl1887, p.475] to denote the number of variables necessary to determine a lin-
ear solution of S. We modify his notation slightly for clarity and write [d; ℓd, . . . , ℓ1] instead of [p, q, r, . . . , η, θ].
Note that [d; ℓd, . . . , ℓ1] = r (C(V(S); P0)) + 1,

for any P0 ∈ V(S)(K). It follows that Sylvester’s formula of reduction [Syl1887, p.475] is

[d; ℓd, . . . , ℓ1] ≤
 

d; ℓd − 1, ℓd + ℓd−1, . . . ,
 d∑

j=2 ℓj,
 d∑

j=1 ℓj


 + 1,

when ℓd ≥ 2. When ℓd = 1, let d
′ be the largest j ≤ d − 1 such that ℓj is non-zero. Then, Sylvester’s formula
of reduction is
 [d; ℓd, . . . , ℓ1] ≤
 

d
′; ℓd′, ℓd′ + ℓd′−1, . . . ,
 d′
∑

j=2 ℓj,
 d′
∑

j=1 ℓj


 + 1.

Sylvester then claims the his formula of obliteration [Syl1887, p.475] without proof. We state his formula of
obliteration and provide a proof, for the sake of completeness.

Proposition 3.15. (Sylvester’s Formula of Obliteration)

Let S be a system of homogeneous polynomials of type [ d · · · 1
ℓd · · · ℓ1
] with d ≥ 2 and ℓd ≥ 2. Then,

[d; ℓd, . . . , ℓ1] ≤ [d − 1; λd−1, λd−2, . . . , λ2, λ1] + ℓd,

= [d − 1; λd−1, λd−2, . . . , λ2, λ1 + ℓd],

12

where
 λd−j = (
ℓd + j − 1
j
 ) jℓd + 1
j + 1 +
 j−1∑

ν=0
 (
ℓd + ν − 1
ν
 )
ℓd−j+ν.

Proof. It is straightforward to see that iteratively applying Sylvester’s formula of reduction allows us to
reduce to a system of equations of degree at most d − 1. For the explicit numerics, we give a proof via
induction on ℓd. Note that to determine a linear solution of S, it suﬃces to determine a point solution of a
completed emanant T0 of S at some point solution P0. Additionally, we note that the type of T0 is




 d d − 1 · · · 2 1

ℓd ℓd + ℓd−1 · · · d∑

j=2 ℓj
 ( d∑

j=1 ℓj
)
 + 1



 .

Now, suppose that ℓd = 1. We can determine a point solution P1 of T0 by determining a linear solution
of the subsystem T ′
0, which is of type




 d − 1 · · · 2 1

1 + ℓd−1 · · · 1 + d−1∑

j=2 ℓj
 (
1 + d−1∑

j=1 ℓj
)
 + 1




 .

Futhermore, we see that

λd−j = (
1 + j − 1
j
 ) j(1) + 1
j + 1 +
 j−1∑

ν=0
 (
1 + ν − 1
ν
 )
ℓd−j+ν = 1 +
 j−1∑

ν=0 ℓd−j+ν = 1 +
 d−1∑

µ=d−j ℓµ,

so the claim holds when ℓd = 1. Now, consider the case where ℓd ≥ 2 is arbitrary. To determine a point
solution of T0, it suﬃces to determine a linear solution of a subsystem T ′
0, which is of type




 d d − 1 · · · 2 1

ℓd − 1 ℓd + ℓd−1 · · · d∑

j=2 ℓj
 ( d∑

j=1 ℓj
)
 + 1




 .

Thus,
 [d; ℓd, . . . , ℓ1] ≤
 

d; ℓd − 1, (ℓd + ℓd−1), . . . ,
 

 d∑

j=2 ℓd


 ,
 

 d∑

j=1 ℓj


 + 1


 .

By induction, however, we have that


d; ℓd − 1, (ℓd + ℓd−1), . . . ,
 

 d∑

j=2 ℓd


 ,
 

 d∑

j=1 ℓj


 + 1


 ≤ [d − 1; θd−1, . . . , θ1 + ℓd],

where
 θd−j = (
(ℓd − 1) + j − 1
j
 ) j(ℓd − 1) + 1
j + 1 +
 j−1∑

ν=0
 (
(ℓd − 1) + ν − 1
ν
 ) ( j∑

µ=0 ℓd−j+µ
)
 ,

= (
ℓd + j − 2
j
 ) jℓd − j + 1
j + 1 +
 j−1∑

ν=0
 (
ℓd + ν − 2
ν
 ) ( j∑

µ=0 ℓd−j+µ
)
 .

Note that for each µ′ ∈ [0, j − 1], there are exactly µ′ + 1 summands containing ℓd−j+µ′ , namely
(
ℓd − 2
0
 )
ℓµ′, (
ℓd − 1
1
 )
ℓµ′, . . . , (
ℓd + µ′ − 2
µ′
 )
ℓµ′ .

13

Additionally, there are exactly j summands containing ℓd, namely
(
ℓd − 2
0
 )
ℓd, (
ℓd − 1
1
 )
ℓd, . . . , (
ℓd + j − 3
j − 1
 )
ℓd.

As a result,

θd−j = (
ℓd + j − 2
j
 ) jℓd − j + 1
j + 1 +
 j−1∑

ν′=0
 (
ℓd + ν′ − 2
ν′
 )
ℓd +
 j−1∑

µ1=0
 ( µ1∑

µ2=0
 (
ℓd + µ2 − 2
µ2
 ))
 ℓd−j+µ1 ,

= (
ℓd + j − 2
j
 ) jℓd − j + 1
j + 1 + (
ℓd + j − 2
j − 1
 )
ℓd +
 j−1∑

µ1=0
 (
ℓd + µ1 − 1
µ1
 )
ℓd−j+µ1 .

Next, we see that (
ℓd + j − 2
j
 ) jℓd − j + 1
j + 1 = (
ℓd + j − 2
j
 ) jℓd + 1
j + 1 − (ℓd + j − 2
j
 ) j
j + 1 ,

and (
ℓd + j − 2
j − 1
 )ℓd = (
ℓd + j − 2
j − 1
 ) jℓd + 1
j + 1 + (
ℓd + j − 2
j − 1
 ) ℓd − 1
j + 1 .

Noting that (
ℓd+j−2
j ) + (
ℓd+j−2
j−1 ) = (
ℓd+j−1
j )
, it follows that

θd−j = (
ℓd + j − 1
j
 ) jℓd + 1
j + 1 + (
ℓd + j − 2
j − 1
 ) ℓd − 1
j + 1 − (
ℓd + j − 2
j
 ) j
j + 1 +
 j−1∑

µ1=0
 (
ℓd + µ1 − 1
µ1
 )
ℓd−j+µ1 .

However,
(
ℓd + j − 2
j − 1
 ) ℓd − 1
j + 1 − (ℓd + j − 2
j
 ) j
j + 1 = (ℓd + j − 2)!(ℓd − 1)
(j − 1)!(ℓd − 1)!(j + 1) − (ℓd + j − 2)!j
j!(ℓd − 2)!(j + 1) ,

= (ℓd + j − 2)!
(j − 1)!(ℓd − 2)!(j + 1) − (ℓd + j − 2)!
(j − 1)!(ℓd − 2)!(j + 1) ,

= 0,

and thus
 θd−j = (
ℓd + j − 1
j
 ) jℓd + 1
j + 1 +
 j−1∑

µ1=0
 (
ℓd + µ1 − 1
µ1
 )ℓd−j+µ1 = λd−j,

which proves the claim.

Sylvester then applies his formula of obliteration to the question of determining non-zero solutions of
equations which deﬁne the Tschirnhaus complete intersections τ1,...,m−1, including his Triangle of Obliter-
ation. We omit his discussion here as the bounds he obtains are succeeded by the bounds of [Bra1975],
[Wol2021], [Sut2021C], and the next section.

4 Upper Bounds on Resolvent Degree

4.1 Previous Bounds

The current upper bounds on RD(n) were determined by the second-named author in [Sut2021C, Theorem
3.27], which improved upon those of Wolfson [Wol2021, Theorem 5.6]. The general framework used by
both the second-named author (with polar cones) and Wolfson (without polar cones) for constructing their
respective bounding functions G(m) and F (m) was outlined in Remark 2.13. We deﬁne G(m) below, but
ﬁrst we highlight the function’s key properties (and recall that property 1, which both F (m) and G(m) share,
is why we refer to F (m) and G(m) as bounding functions).

14

Theorem 4.1. (Theorem 1.3 of [Sut2021C])
The function G(m) of [Sut2021C, Deﬁnition 3.26] has the following properties:

1. For each m ≥ 1 and n ≥ G(m), RD(n) ≤ n − m.

2. For each d ≥ 4, G(2d
2 + 7d + 6) ≤ (2d2+7d+5)!
d! . In particular, for d ≥ 4 and n ≥ (2d2+7d+5)!
d! ,

RD(n) ≤ n − 2d
2 − 7d − 6.

3. For each m ≥ 1, G(m) ≤ F (m) with equality only when m ∈ {1, 2, 3, 4, 5, 15, 16} and

lim
m!∞ F (m)
G(m) = ∞.

We will now numerically deﬁne G(m) (which will require two additional functions) and then a summary
of the construction of G(m). We refer the reader to [Sut2021C, Section 3] for the full construction of G(m)
and proofs of the statements in Theorem 4.1.

Deﬁnition 4.2. (The Function G(m))
We ﬁrst deﬁne ϑ : Z≥3 × Z≥1 ! Z≥1 so that ϑ(d, k) is the minimal r ∈ Z≥1 such that

(k + 1)(r − k) −
 d∑

j=2
 (k + i
i
 ) ≥ 0.

Explicitly, we have
 ϑ(d, k) = k + ⌈ 1
k + 1
 ((
k + d + 1
d
 ) − (k + 2)
)⌉ .

Next, we deﬁne ϕ : Z≥15 × Z≥1 ! Z≥1 by

ϕ(d, k) = max { (d + k)!
d! , (
ϑ(d, k) + d + 1
d
 ) − (ϑ(d, k) + 1)
2 − (ϑ(d, k) + d)
} .

Finally, we deﬁne G : Z≥1 ! Z≥1. For m ∈ [1, 14], we deﬁne G(m) by

m 1 2 3 4 5 6 7 8 9 10
G(m) 2 3 4 5 9 21 109 325 1681 15121

m 11 12 13 14
G(m) 151,201 1,663,201 19,958,401 259,459,201

and for m ≥ 15 by
 G(m) = 1 + min {ϕ(d, m − d − 1) | 4 ≤ d ≤ m − 1} .

The values of G(m) for m ∈ [1, 5] are classical and described in [Wol2021, Appendix B]. In [Che1954],
Chebotarev gave an argument that RD(n) ≤ n − 6 for n ≥ 21, however his argument had a gap which was
ﬁxed by [Sut2021C, Theorem 3.7]. More speciﬁcally, Chebotarev (like Wiman before him in [Wim1927])
assumed certain intersections of hypersurfaces were generic without proof.
For m ∈ [6, 14], the second-named author determined k-polar points on extended Tschirnhaus complete
intersections τ ◦
1,...,d [Sut2021C, Theorems 3.7, 3.10]. However, the degrees of iterated polar cones grow
exponentially and this method could not be further extended [Sut2021C, Remark 3.19]. For general m, the
second-named author was able to improve on the bounds of Wolfson by using [DM1998, Theorem 2.1] to
minimize the ambient dimension required for Wolfson’s algorithm [Sut2021C, Theorem 3.24].

15

4.2 New Bounds

We will now improve on G(m) for m ∈ [13, 17] ∪ [22, 25]. For m ∈ [7, 16], G(m) is obtained by determining an
(m − 5)-plane on τ ◦
1,2,3,4. Additionally, for m ∈ [17, 24], G(m) is obtained by determining an (m − 6)-plane
on τ ◦
1,2,3,4,5. Finally, for m ∈ [25, 33], G(m) is obtained by determining an (m − 7)-plane on τ ◦
1,2,3,4,5,6.
Our improvements will come from determining an (m − 6)-plane on τ ◦
1,2,3,4,5 for m ∈ [13, 17] and from
determining an (m − 7)-plane on τ ◦
1,2,3,4,5,6 for m ∈ [22, 25]. Note that in each of these cases, one can apply
the geometric obliteration algorithm to obtain improved bounds. However, we will use a slight modiﬁcation
which allows for a minor optimization.

Remark 4.3. (A Modiﬁcation of the Geometric Obliteration Algorithm)

Let V ⊆ Pr
K be an intersection of hypersurfaces of type [ d · · · 1
ℓd · · · ℓ1
]. Recall that successive uses of

Proposition 3.10 yield that
 g(V ) = g (
V Syl
1 ) = · · · = g (
V Syl
d−3) = g (V Syl
d−2) ,

and that V Syl
d−2 is an intersection of type [ 2 1
λ2 λ1
]. In the spirit of the obliteration algorithm, we could indeed

continue to apply Lemma 3.5 until there is a single quadric left, at which point we need only solve a ﬁnal
quadratic polynomial.
However, we also note that deg (
V Syl
d−2) is 2λ2 and thus we can determine a point of WV by solving

a polynomial of degree 2λ2 whenever r ≥ λ2 + λ1. Consequently, we obtain a slight improvement in the
forthcoming bounds on RD(n) by reducing only to a jth partial Sylvester reduction of V Syl
d−2 for some j < λ2
instead of V Syl
d−1.

Deﬁnition 4.4. (Optimal Reduction of Tschirnhaus Complete Intersection)
For each d ≥ 3 and m ≥ d + 2, consider

W = (
Cm−d−1(τ1,...,d; P0, . . . , Pm−d−2)
)Syl

d−2 ,

a (d − 2)
nd Sylvester reduction of an (m − d − 1)
st polar cone of τ1,...,d, which is of type [ 2 1
λ2 λ1
]
. For each

j ∈ [1, λ2 − 1], note that a jth partial Sylvester reduction W Syl(2; j) of W has type
 

 2 1

λ2 − j λ1 + λ2−1∑

ν=λ2−j ν


.

Further, deg (
W Syl(2; j)
) = 2λ2−j.

For each such j, set

ξ(m, d; j) := max
 



(m − d + 1) + (λ2 − j) +
 

λ1 +
 λ2−1∑

ν=λ2−j ν


 , 2λ2−j + 1



 .

The optimal reduction bound of τ1,...,d for m, is

Ξ(m, d) := min {ξ(m, d; j) | j ∈ [0, λ2 − 1]} .

In particular, Ξ(m, d) is deﬁned exactly so that for n ≥ Ξ(m, d), we can determine an (m − d − 1)
th polar
point of τ ◦
1,...,d in Pn−1
Kn over an extension K ′/Kn with RD(K ′/Kn) ≤ RD(Ξ(m; d)).

Remark 4.5. (Ξ(m, d) is Non-Decreasing in m)
Note that Ξ(m, d) is non-decreasing in m for ﬁxed d. This can be seen geometrically from the fact if
(P0, . . . , Pm−d−1) is an (m − d − 1)
st polar point of τ1,...,d, then (P0, . . . , Pm−d−2) must be an (m − d − 2)
nd

polar point of d, so Ξ(m, d) ≥ Ξ(m − 1, d).
 16

We are now ready to state and prove the main theorem.

Theorem 4.6. (Bounds from the Geometric Obliteration Algorithm)

1. For n ≥ 5, 250, 198, RD(n) ≤ n − 13.

2. For each m ∈ [14, 17] and n > (m−1)!
120 , RD(n) ≤ n − m.

3. For n ≥ 381, 918, 437, 071, 508, 900, RD(n) ≤ n − 22.

4. For each m ∈ [23, 25] and n > (m−1)!
720 , RD(n) ≤ n − m.

Proof. We continue to use the notation established in Deﬁnition 4.4. For each m ∈ [13, 17], we set

G
′(m) = max {
Ξ(m, 5), (m − 1)!
120 + 1} ,

and for each m ∈ [22, 25], we set
 G
′(m) = max {
Ξ(m, 6), (m − 1)!
720 + 1} .

In each case, it suﬃces to show the claim when n = G
′(m). Further, note that G
′(m) = Ξ(m, 5) exactly
when m = 13 and G
′(m) = Ξ(m, 6) exactly when m = 22; this claim is justiﬁed by explicit computation and
is given in the tables at the end of the proof. Recall that the space of Tschirnhaus transformations up to
re-scaling is PG′(m)−1
KG′(m) .

Let us ﬁrst consider the case of m ∈ [13, 17] and let H ⊆ PG′(m)−1
Kn be a hyperplane which does not contain

[1 : 0 : · · · : 0]. Note that H ∼= PG′(m)−2
Kn and H ∩ τ1,...,5 = H ∩ τ ◦
1,...,5. Since Ξ(m, 5) ≥ Ξ(m − 1, 5), we can
assume that we have an (m − 7)-polar point (P0, . . . , Pm−7) of H ∩ τ ◦
1,...,5. Consider the minimal j such that
Ξ(m, 5) = ξ(m, 5; j). By deﬁnition of ξ(m, 5; j), we have that

dim (((
Cm−6(H ∩ τ ◦
1,...,5; P0, . . . , Pm−7)
)Syl
3
 )Syl (2; j)
) ≥ m − 6.

Since dim (Λ(P0, . . . , Pm−7)) = m − 7, we can determine a point of

Cm−6 (
H ∩ τ ◦
1,...,5; P0, . . . , Pm−7) \ Λ (P0, . . . , Pm−7) ,

by solving a polynomial of degree at most Ξ(m; 5). By construction (P0, . . . , Pm−6) is an (m − 6)-polar point
and Lemma 2.9 yields that Λ = Λ(P0, . . . , Pm−6) ⊆ τ ◦
1,...,5 is an (m − 6)-plane. We can then determine a
point of Λ ∩ τ ◦
1,...,m−1 by solving a polynomial of degree (m−1)!
120 .

We now consider the similar case of m ∈ [22, 25]. Let H ⊆ PG′(m)−1
Kn be a hyperplane which does not

contain [1 : 0 : · · · : 0]. Note that H ∼= PG′(m)−2
Kn and H ∩ τ1,...,5 = H ∩ τ ◦
1,...,5. Since Ξ(m, 6) ≥ Ξ(m − 1, 6),
we can assume that we have an (m − 8) polar point (P0, . . . , Pm−8) of H ∩ τ ◦
1,...,6. Consider the minimal j
such that Ξ(m, 6) = ξ(m, 6; j). Observe that

dim (((
Cm−7(H ∩ τ ◦
1,...,6; P0, . . . , Pm−8)
)Syl
4
 )Syl (2; j)
) ≥ m − 7,

and so we can determine a point Pm−6 of

Cm−7 (
H ∩ τ ◦
1,...,6; P0, . . . , Pm−8) \ Λ (P0, . . . , Pm−8) ,

by solving a polynomial of degree at most Ξ(m; 6). it follows that (P0, . . . , Pm−7) is an (m − 7)-polar point
of τ ◦
1,...,6 and so Λ = Λ(P0, . . . , Pm−7) ⊆ τ ◦
1,...,6 is an (m − 7)-plane. Consequently, we can determine a point

of Λ ∩ τ ◦
1,...,m−1 by solving a polynomial of degree (m−1)!
720 .
We now show that G
′(m) = Ξ(m, 5) exactly when m = 13 and G
′(m) = Ξ(m, 6) exactly when m = 22.
In the following tables, we note the values of Ξ(m, 5) and (m−1)!
120 + 1 for m ∈ [13, 17] and the approximate
values of Ξ(m, 6) and (m−1)!
720 + 1 for m ∈ [22, 25]. The exact values of Ξ(m, 5) for m ∈ [13, 17] and of Ξ(m, 6)
for m ∈ [22, 25] were computed using Algorithm 5.6, which can be found in Subsection 5.4.

17

m Ξ(m, 5) (m−1)!
120 + 1
13 5,250,198 3,991,681
14 12,253,482 51,891,841
15 26,357,165 726,485,761
16 53,008,668 10,897,286,401
17 100,769,994 174,356,582,401
 m Ξ(m, 6) (m−1)!
720 + 1
22 ∼ 3.819 × 1017 ∼ 7.096 × 1016

23 ∼ 9.526 × 1017 ∼ 1.561 × 1018

24 ∼ 2.262 × 1018 ∼ 3.591 × 1019

25 ∼ 5.137 × 1018 ∼ 8.617 × 1020

4.3 Obstruction to Further Bounds via the Geometric Obliteration Algorithm

Unfortunately, the proof strategy of Theorem 4.6 does not yield further bounds on RD(n). Recall that for
m ≥ 15, G(m) is deﬁned by
 G(m) = 1 + min {ϕ(d, m − d − 1) | d ∈ [4, m − 1]} ,

where
 ϕ(d, k) = max { (d + k)!
d! , (
ϑ(d, k) + d + 1
d
 ) − (ϑ(d, k) + 1)
2 − (ϑ(d, k) + d)
} .

For each d, the values of m for which G(m) = 1 + ϕ(d, m − d − 1) is a set of consecutive integers. Equivalently,
there are positive integers md and m′
d such that G(m) = 1 + ϕ(d, m − d − 1) if and only if m ∈ [md, m′
d]; see
[Sut2021C, Lemma 3.33] for details.
Similarly, we brieﬂy introduce the notation

̺(d, k) = max {
Ξ(d + k + 1, d), (d + k)!
d! + 1}

for d ≥ 4 and k ≥ 1, as well as
 H(m) = min {̺(d, m − d − 1) | d ∈ [4, m − 1]}

for m ≥ 13. For ﬁxed d, note that Ξ(m, d) is a polynomial in m, whereas (d+k)!
d! = (m−1)!
d! grows factorially.
It follows that for each d, there are positive integers Md and M ′
d such that H(m) = ̺(d, m − d − 1) if and
only if m ∈ [Md, M ′
d].
In the following table, we compare the values md and Md for d = 5, 6, 7, 8.

d md Md
5 17 13
6 25 22
7 34 41
8 44 78

This provides further evidence, along with [Sut2021C, Remark 3.19], that iterated polar cone methods are
most eﬀective for intersections of hypersurfaces of small types. Next, we determine an explicit lower bound
on Ξ(m, d).

Lemma 4.7. (Lower Approximation)

Let V ⊆ Pr
K be an intersection of hypersurfaces of type [ d
ℓd
] with d ≥ 3 and ℓd ≥ 2. Denote the type of a

(d − 2)
nd Sylvester reduction V Syl
d−2 by [ 2 1
λ2 λ1
]. Then,

λ1 ≥ λ2 ≥ ⌈25−2d (ℓd − 1)
2d−4⌉ .

18

Proof. Note that the number of degree d − 1 hypersurfaces of V Syl
1 is

θd−1 =
 ℓd−1∑

j=1 ℓd − j = 1
2 (ℓd − 1)ℓd ≥ ⌈ 1
2 (ℓd − 1)
2⌉ .

The same argument yields that the number of degree d − 2 hypersurfaces of V Syl
2 is

θd−2 ≥
 ⌈ 1
2
 ⌈ 1
2 (ℓd − 1)
2⌉2⌉
 ≥ ⌈
2−3(ℓd − 1)
4⌉ .

Proceeding similarly, we see that λ2 = θ2 ≥ ⌈25−2d (ℓd − 1)
2d−4⌉ .

Finally, note that λ1 ≥ λ2 follows immediately from the polar cone construction.

Corollary 4.8. (Lower Bound for Ξ(m, d))
Let d ≥ 4 and m ≥ d + 2. Then,
 Ξ(m, d) ≥
 ⌈
4 ( m − d − 1
2
 )2d−4⌉
 .

Proof. First, Proposition 2.26 of [Sut2021C] yields that an (m − d − 1)
th polar cone of τ1,...,d is of type
[d d − 1 · · · 2 1
1 (
m−d
1 ) · · · (
m−3
d−2 ) (
m−2
d−1 )
] .

Thus, the number of degree d − 1 hypersurfaces of V = (τ1,...,d)
Syl
1 is m − d. Let σ(m, d) be as in Deﬁnition
4.4. It follows from Lemma 4.7 that
 λ1 ≥ λ2 ≥ ⌈
25−2d(m − d − 1)
2d−4⌉ .

Moreover, for each j,

ξ(m, d; j) ≥ λ1 + λ2 ≥ ⌈
25−2d(m − d − 1)
2d−4⌉ + ⌈25−2d(m − d − 1)
2d−4⌉ ≥
 ⌈
4 ( m − d − 1
2
 )2d−4⌉
 ,

and thus it follows that

Ξ(m, d) = min {ξ(m, d; j) | 0 ≤ j ≤ λ2 − 1} ≥
 ⌈
4 ( m − d − 1
2
 )2d−4⌉
 .

While we do not provide a full comparison here, we note that the key obstruction to obtaining further
bounds on RD(n) using the methods of Theorem 4.6 is that Ξ(m, d) has a lower bound which grows ex-
ponentially in d and that m − d − 1 grows much more quickly than d (for example, m − d − 1 ≥ 19 for
m ≥ 26).
Having indicated the obstruction to obtaining further upper bounds on RD(n) using these methods, we
now combine Theorems 4.1 and 4.6 to immediately construct a new bounding function with the same key
properties of G(m).

Corollary 4.9. (The New Bounding Function)
Let G
′ : Z≥2 ! Z≥1 be the function with

G
′(m) = max {
Ξ(m, 5), (m − 1)!
120 + 1} ,

for m ∈ [13, 17], with
 G
′(m) = max {
Ξ(m, 6), (m − 1)!
720 + 1} ,

for m ∈ [22, 25], and with G
′(m) = G(m) for m ̸∈ [13, 17] ∪ [22, 25]. Then, G
′(m) has the following properties:

19

1. For each m ≥ 1 and n ≥ G
′(m), RD(n) ≤ n − m.

2. For each d ≥ 4, G
′(2d
2 + 7d + 6) ≤ (2d2+7d+5)!
d! . In particular, for d ≥ 4 and n ≥ (2d2+7d+5)!
d! ,

RD(n) ≤ n − 2d
2 − 7d − 6.

4.4 Remaining Questions

To the best of the authors’ knowledge, the bounding function G
′(m) of Corollary 4.9 exhausts the tech-
niques and methods for determining upper bounds on resolvent degree from the classical literature (including
[Bri1786, Che1954, Ham1836, Hil1927, Seg1945, Syl1887, SH1887, SH1888, Tsc1683, Wim1927]), as well as
the modern insights from [Bra1975, Sut2021C, Wol2021].
The bounding functions of Brauer, Hamilton, Sylvester, Wolfson, and the second-named author are con-
structed by determining points on the Tschirnhaus complete intersections τ ◦
1,...,m−1 over extensions of bounded
resolvent degree. However, there are solutions of the quintic and the sextic which use alternative constructions
of Tschirnhaus transformations (see [Kle1884, Kle1905] for the respective original works or [Mor1956, Sut2019]
for the respective English translations). We believe it would be insightful to understand whether one can
reduce the general question of determining RD(n) to the more speciﬁc question of determining points on the
Tschirnhaus complete intersections τ ◦
1,...,m−1.

Question 4.10. (Optimal Formulas via Tschirnhaus Complete Intersections)
For every n, let mn be such that RD(n) ≤ n − mn. Is there a formula in n − mn variables for the general
degree n polynomial obtained by determining a point of τ ◦
1,...,mn−1 over an extension K ′/Kn of bounded
resolvent degree?

For general m, the deﬁnition of G
′(m) = G(m) uses the combinatorial condition of [DM1998, Theorem
2.1] to guarantee the existence of k-planes on the τ ◦
1,...,d and then uses the dimension of the relevant moduli
space [Sut2021C, Subsection 3.3]. Notably, this combinatorial condition is non-constructive and relies only
on the type of τ ◦
1,...,d. One might hope that such formulas could be determined using constructive methods
and one approach may be to leverage the speciﬁc geometry of the τ ◦
1,...,d (e.g., using more information than
its type).

Question 4.11. (RD Bounds via Explicit Constructions of k-Planes)
Is there a bounding function G(m) with G(m) ≤ G
′(m) which arises from an explicit construction of k-planes
on the τ ◦
1,...,d? If so, is it possible to determine the bounding function G(m) such that

lim
m!∞ G(m)
G(m) = lim
m!∞ G
′(m)
G(m) = ∞?

Theorem 4.6 was proved using a consequence of the geometric obliteration algorithm, namely that r(V ) ≤
g(V ) for any intersection of hypersurfaces V . Further examination of the relationship between r(V ) and g(V )
is of interest.

Question 4.12. (Minimal Dimension Bound vs. Geometric Dimension Bound)
For which intersections of hypersurfaces V is the inequality r(V ) ≤ g(V ) strict? Are there classical examples
of types of intersections of hypersurfaces where the inequality is not strict?

Let us now brieﬂy consider a cubic hypersurface H = V(f ) ⊆ Pr
K. When r = 3 and H is smooth, the
Cayley-Salmon theorem yields that H contains exactly 27 lines. The resolvent degree of determining a line
on H is at most 3, as was established by Farb and Wolfson [FW2019, Theorem 8.2]. Additionally, that
H has exactly 27 lines is consistent with [DM1998, Theorem 2.1], which states that the Fano variety of
lines of a cubic surface in P3
K is non-empty and has dimension 0. In particular, when r = 3, most points
P ∈ H(K) do not lie on a line of H over an algebraic closure K. When r = 4, however, any polar cone
C(V ; P ) has dimension at least one and thus every point P ∈ V (H) lies on at least one line Λ = Λ(P, Q) ⊆ H
over an algebraic closure K. To determine such a point Q directly, we must solve a polynomial of degree
6 = 3! = deg(C(V ; P )). Hence, we can determine a line through any point P over an extension with K ′/K
with RD(K ′/K) ≤ RD(6) ≤ 2.
 20

Additionally, observe that
 g(C(V ; P )) = g(3; 1, 1, 1) = g(2; 1, 3) = 5.

Thus, when r ≥ 5, we can determine a point Q ∈ C(V ; P ) \ {P } over an extension determined by solving at
most cubic polynomials (i.e., over a solvable extension).

Now, let V ⊆ Pr
K be an intersection of hypersurfaces of type [ d · · · 1
ℓd · · · ℓ1
]. For each k ≥ 1, take sk(V )

to be the minimal s such that
 (k + 1)(s − k) −
 d∑

j=1 ℓj
(
k + j
j
 ) ≥ 0.

One implication of Theorem 2.1 of [DM1998] is that V contains a k-plane for all r ≥ sk(V ). We expect
sk(V ) to be the minimal ambient dimension required for V to contain a k-plane; however, we expect the
resolvent degree of determining such a k-plane to be large. Conversely, we expect r (
Ck(V ; P0, . . . , Pk−1)
) + k,
the ambient dimension required to determine a k-polar point over an extension K ′/K of small resolvent degree
(RD(K ′/K) ≤ RD(d)), to be large.

Question 4.13. (Minimizing Ambient Dimension vs. Minimizing RD of Extensions)
Let V be an intersection of hypersurfaces. How do g (
Ck(V ; P0, . . . , Pk−1)
) + k, r (
Ck(V ; P0, . . . , Pk−1)
) + k,
and sk(V ) compare?

Finally, we recall that we have worked entirely in characteristic zero (more speciﬁcally, over C). As we
discussed in 2.1, we do not lose any generality from the perspective of resolvent degree, as

RD(n) = RDC (Sn) ≥ RDK (Sn)

by [Rei2022, Theorem 1.3], with equality when K has characteristic zero by [Rei2022, Theorem 1.2]. The
foundational result for the polar cone framework we use is the technical lemma [Sut2021C, Lemma 2.8]. For
those who wish to work in characteristic p, one would need to be careful of how the relevant combinatorics,
such as [Sut2021C, Proposition 2.26], change. Additionally, the modern reference for Tschirnhaus transfor-
mations [Wol2021] works over Z. To consider Tschirnhaus transformations in characteristic p, one would
need to give extra consideration to the Tschirnhaus hypersurfaces of degree pk.

21

5 Python Implementations of the Obliteration Algorithm and Re-
lated Phenomena

In Subsection 5.1, we provide an implementation (Algorithm 5.1) of the geometric obliteration algorithm
in Python. In Subsection 5.2, we prove several lemmata which make the computations for the proof of
Theorem 4.6 feasible. Algorithm 5.5 in Subsection 5.3 takes the same input and provides the same output
as Algorithm 5.1, but uses the lemmata of Subsection 5.2 to decrease computation time. Finally, Algorithm
5.6 in Subsection 5.4 computes the information necessary for Theorem 4.6.

5.1 Appendix A: The Geometric Obliteration Algorithm

Algorithm 5.1. (The Geometric Obliteration Algorithm)

• Input: An intersection of hypersurfaces V of type [ d d − 1 · · · 2 1
ℓd ℓd−1 · · · ℓ2 ℓ1
] with d ≥ 2, encoded as

the list DegreeList = [ℓd, ℓd−1, . . . , ℓ2, ℓ1].

• Output: The geometric dimension bound g(d; ℓd, . . . , ℓ1).

The function ComputePolarCone inputs a list which contains the type of an intersection of hypersur-
faces W . It then returns a list which contains the type of a polar cone C(W ; P ). In particular, recall that
for each d
′ < d, each hypersurface H with deg(H) > d
′ deﬁning W contributes exactly one new degree
d
′ hypersurface deﬁning C(W ; P ) and each hypersurface deﬁning C(W ; P ) arises in this manner.

1: function ComputePolarCone(List):

2: counter = List[0]

3: ReturnList = [counter]
4: for index in range(1,len(List)):

5: counter += List[index]
6: ReturnList.append(counter)

7: end for

8: return ReturnList
9: end function

The function ObliterateLargestDegreeHypersurfaces inputs a list which contains the type of an
intersection of hypersurfaces W whose largest degree hypersurface has degree d ≥ 3. It identiﬁes the
number of hypersurfaces of largest degree and proceeds to iteratively remove a hypersurface H of largest
degree and compute a polar cone of the remaining intersection of hypersurfaces W ′ (with an additional
hyperplane included).

Note that an additional hyperplane is added each time to avoid repeated polar cone points, i.e. if P was
the cone point of the previous polar cone point, we pass to a hyperplane which does not contain P to
ensure that the cone point Q of the next polar cone satisﬁes Q ̸= P . Also, the polar cone of a hyperplane
plane at any point is just the hyperplane itself, so to compute the combinatorics, it suﬃces to add one
after computing the polar cone instead of doing it beforehand.

As taking the polar cone of a hypersurface H introduces only hypersurfaces of strictly smaller degree, this
process terminates and ObliterateLargestDegreeHypersurfaces returns a list whose data is the
multi-degree of an intersection of hypersurfaces V ′ whose largest degree hypersurface has degree d − 1.

22

10: function ObliterateLargestDegreeHypersurfaces(List):

11: while List[0] > 0:
12: List[0] -= 1

13: TempList = ComputePolarCone(List)
14: List = TempList

15: List[len(List)-1] += 1

16: end while
17: ReturnList = []

18: for index in range(1,len(List):

19: ReturnList.append(List[index])
20: end for

21: return ReturnList
22: end function

The function ObliterateQuadricsViaLoops works similarly to ObliterateLargestDegreeHy-

persurfaces, but the input is the multi-degree of an intersection of hypersurfaces of type [ 2 1
ℓ2 ℓ1
] and

the loop ends with a single quadric remaining instead of zero quadrics remaining.

23: function ObliterateQuadricsViaLoops(List):
24: while List[0] > 1:

25: List[0] -= 1
26: TempList = ComputePolarCone(List)

27: List = TempList

28: List[len(List)-1] += 1
29: end while

30: return [List[0],List[1]]

31: end function

The procedure Main inputs the multi-degree of an intersection of hypersurfaces V as the list DegreeList
and proceeds to successively “obliterate” the hypersurfaces of largest degree. The ﬁnal step of the
procedure is to return a list of the form [1, α], which is the requisite intersection of a single quadric and
α hyperplanes.

32: procedure Main(DegreeList):

33: for index in range(1,len(DegreeList)-1):
34: TempDegreeList = ObliterateLargestDegreeHypersurfaces(DegreeList)

35: DegreeList = TempDegreeList
36: end for

37: FinalList = ObliterateQuadricsViaLoops(DegreeList)

38: Sum = FinalList[0] + FinalList[1]
39: return Sum

40: end procedure
 23

5.2 Appendix B: Lemmata for Computational Improvements

In this subsection, we give explicit numerics for Proposition 3.10 when d = 2, 3, 4.

Lemma 5.2. (Obliterating Quadrics)

Consider an intersection of hypersurfaces V of type [ 2 1
ℓ2 ℓ1
]. Then,

g(V ) = 1 + ℓ1 + 1
2 (ℓ2 − 1)(ℓ2 + 2).

Proof. First, observe that V Syl(2; 1) has type
[ 2 1
ℓ2 − 1 ℓ1 + ℓ2
] ,

by Deﬁnition 3.9. Similarly, V Syl(2; 2) has type
[ 2 1
ℓ2 − 2 ℓ1 + ℓ2 + ℓ2 − 1

] .

Proceeding in this manner yields that V Syl(2; λ2 − 1) has type



2 1

1 ℓ1 + ℓ2−1∑

j=1 (ℓ2 − j + 1)



 ,

and we note that ℓ2−1∑

j=1 (ℓ2 − j + 1) = 1
2 (ℓ2 − 1) (ℓ2 + 2) .

From Lemma 3.5 and Deﬁnition 3.9, we see that

g(V ) = g (
V Syl(2; λ2 − 1)
) = 1 + ℓ1 + 1
2 (ℓ2 − 1) (ℓ2 + 2) .

Lemma 5.3. (Obliterating Cubics)

Consider an intersection of hypersurfaces V of type [ 3 2 1
ℓ3 ℓ2 ℓ1
]. Then, V Syl
1 is of type [ 2 1
β3 α3
], where

β3 = ℓ2 + 1
2 (ℓ3 − 1)ℓ3,

α3 = ℓ1 + ℓ2ℓ3 + 1
2 ℓ3(ℓ3 + 1) + 1
6 ℓ3 (
2ℓ2
3 − 3ℓ3 + 1) .

Proof. An argument analogous to the proof of Lemma 5.2 yields that

β3 = ℓ2 +
 ℓ3∑

j=1(ℓ3 − j) = ℓ2 + 1
2 (ℓ3 − 1)ℓ3.

Next, observe that V Syl(3; j) has type


 3 2 1

ℓ3 − j ℓ2 + j∑

k=1(ℓ3 − k) λj


 .

Consequently,
 λj+1 = λj + (ℓ3 − j − 1) +
 (

ℓ2 +
 j∑

k=1
(ℓ3 − k)

)
 + 1.

24

Combined with the initial condition λ0 = ℓ1, we obtain that

α3 = ℓ1 +
 

 ℓ3∑

j1=1
(ℓ3 − j1 + 1)



 +
 

 ℓ3∑

j2=1 ℓ2 +
 ℓ3∑

j3=2
 j4−1∑

j4=1 ℓ3 − j4


 ,

= ℓ1 + 1
2 ℓ3(ℓ3 + 1) +
 

ℓ2ℓ3 +
 ℓ3∑

j3=2
 j3−1∑

j4=1 ℓ3 − j4


 ,

= ℓ1 + ℓ2ℓ3 + 1
2 ℓ3(ℓ3 + 1) +
 ℓ3∑

j3=2
 j3−1∑

j4=1
(ℓ3 − j2),

= ℓ1 + ℓ2ℓ3 + 1
2 ℓ3(ℓ3 + 1) + 1
6 ℓ3 (
2ℓ2
3 − 3ℓ3 + 1) .

Lemma 5.4. (Obliterating Quartics)

Consider an intersection of hypersurfaces V ⊆ Pr
K of type [ 4 3 2 1
ℓ4 ℓ3 ℓ2 ℓ1
]
. Then, V Syl
1 is of type [ 3 2 1
γ4 β4 α4
],

where
 γ4 = ℓ3 + 1
2 (ℓ4 − 1)ℓ4,

β4 = ℓ2 + ℓ3ℓ4 + 1
2 (ℓ4 − 1)ℓ4 + 1
6 ℓ4 (
2ℓ2
4 − 3ℓ4 + 1) ,

α4 = ℓ1 + ℓ4
 (
ℓ2 + ℓ3 + 1
2 (ℓ4 + 1)
) + ℓ4
 ( 1
2 ℓ3(ℓ4 + 1) + 1
3 (
2ℓ2
4 − 3ℓ4 + 1)
)

+ 1
24 (ℓ4 − 2)(ℓ4 − 1)ℓ4(3ℓ4 − 1).

Proof. The proofs of Lemmata 5.2 and 5.3 generalize to determine γ4 and β4 in a straightforward manner.
It remains to determine α4. Note that V Syl(4; j) has type




 4 3 2 1

ℓ4 − j ℓ3 + j∑

k1=1
(ℓ4 − k1) ℓ2 +
 ( j∑

k2=1 ℓ4 − k2
)
 + j∑

k3=1
 (
ℓ3 + j−1∑

k4=1
(ℓ4 − k4)

)
 λj
 


 .

As a result,

λj+1 = λj + (ℓ4 − j − 1) +
 (
ℓ3 +
 j∑

k=1(ℓ4 − k)

)
 +
 (

ℓ2 +
 ( j∑

k1=1 ℓ4 − k1
)
 +
 j∑

k2=1
 (

ℓ3 +
 j−1∑

k3=1
(ℓ4 − k3)

))
 + 1.

25

Given the initial condition λ0 = ℓ1, it follows that

α4 = ℓ1 +
 

 ℓ4∑

j1=1 ℓ4 − j1 + 1


 +
 

 ℓ4∑

j2=1 ℓ3 +
 ℓ4∑

j3=2
 j3−1∑

j4=1(ℓ4 − j4)





+
 

 ℓ4∑

j5=1 ℓ2 +
 ℓ4∑

j6=2
 j6−1∑

j7=1(ℓ4 − j7) +
 ℓ4∑

j8=2
 j8−1∑

j9=1 ℓ3 +
 ℓ4∑

j10=3
 j10−1∑

j11=2
 j11−1∑

j12=1
(ℓ4 − j12)



 ,

= ℓ1 + ( 1
2 ℓ4(ℓ4 + 1)
) + (
ℓ3ℓ4 + 1
6 ℓ4 (
2ℓ2
4 − 3ℓ4 + 1)
)

+
 

ℓ2ℓ4 + 1
6 ℓ4 (
2ℓ2
4 − 3ℓ4 + 1) + 1
2 (ℓ4 − 1)ℓ4ℓ3 +
 ℓ4∑

j10=3
 j10−1∑

j11=2
 j11−1∑

j12=1
(ℓ4 − j12)



 ,

= ℓ1 + ℓ4
 (
ℓ2 + ℓ3 + 1
2 (ℓ4 + 1)
) + ℓ4
 ( 1
2 ℓ3(ℓ4 − 1) + 1
3 (
2ℓ2
4 − 3ℓ4 + 1)
) +
 ℓ4∑

j10=3
 j10−1∑

j11=2
 j11−1∑

j12=1(ℓ4 − j12),

= ℓ1 + ℓ4
 (
ℓ2 + ℓ3 + 1
2 (ℓ4 + 1)
) + ℓ4
 ( 1
2 ℓ3(ℓ4 + 1) + 1
3 (
2ℓ2
4 − 3ℓ4 + 1)
) + 1
24 (ℓ4 − 2)(ℓ4 − 1)ℓ4(3ℓ4 − 1).

26

5.3 Appendix C: The Geometric Obliteration Algorithm with Computational
Improvements

Algorithm 5.5. (The Geometric Obliteration Algorithm with Computational Improvements)

• Input: An intersection of hypersurfaces V of type [ d d − 1 · · · 2 1
ℓd ℓd−1 · · · ℓ2 ℓ1
] with d ≥ 2, encoded as

the list DegreeList = [ℓd, ℓd−1, . . . , ℓ2, ℓ1].

• Output: The geometric dimension bound g(d; ℓd, . . . , ℓ1).

We will use the same functions ComputePolarCone and ObliterateLargestDegreeHypersur-
faces which were originally deﬁned in Algorithm 5.1.

We now implement Lemma 5.4 (respectively, Lemmata 5.3 and 5.2) via the following three functions.

1: function ObliterateQuartics(List):

2: a = List[0]

3: b = List[1]
4: c = List[2]

5: d = List[3]
6: gammafour = b + (1/2)*(a-1)*a

7: betafour = c + a*b + (1/2)*a*(a+1) + (1/6)*(a-1)*a*(2*a-1)

8: alphafour = d + a*(b+c+(1/2)*(a+1)) + a*((1/2)*b*(a-1)+(1/3)*((2*(a**2))-(3*a)+1))
9: + (1/24)*(a-2)*(a-1)*a*(3*a-1)

10: return [gammafour,betafour,alphafour]

11: end function

12: function ObliterateCubics(List):
13: a = List[0]

14: b = List[1]

15: c = List[2]
16: betathree = b + (1/2)*(a-1)*a

17: alphathree = c + a*b + (1/2)*a*(a+1) + (1/6)*a*((2*(a**2))-(3*a)+1)

18: return [betathree,alphathree]
19: end function

20: function ObliterateQuadrics(List):

21: a = List[0]

22: b = List[1]
23: alphatwo = b + (1/2)*a*(a+1)

24: return [1,alphatwo]

25: end function
 27

The Main procedure works very similarly to its counterpart in Algorithm 5.1, with the only diﬀerences
being the use of specialized functions to obliterate quartic, cubic, and quadric hypersurfaces.

26: procedure Main(DegreeList):

27: if len(DegreeList) == 2: then
28: FinalDegreeList = ObliterateQuadrics(DegreeList)

29: Sum = FinalDegreeList[0] = FinalDegreeList[1]

30: return Sum
31: else if len(DegreeList) == 3: then

32: TempDegreeList = ObliterateCubics(DegreeList)
33: DegreeList = TempDegreeList

34: TempDegreeList = ObliterateQuadrics(DegreeList)

35: FinalDegreeList = TempDegreeList
36: Sum = FinalDegreeList[0] = FinalDegreeList[1]

37: return Sum

38: else if len(DegreeList == 4: then
39: TempDegreeList = ObliterateQuartics(DegreeList)

40: DegreeList = TempDegreeList
41: TempDegreeList = ObliterateCubics(DegreeList)

42: DegreeList = TempDegreeList

43: TempDegreeList = ObliterateQuadrics(DegreeList)
44: FinalDegreeList = TempDegreeList

45: Sum = FinalDegreeList[0] = FinalDegreeList[1]

46: return Sum
47: else:

48: for index in range(1,len(DegreeList)-3):
49: TempDegreeList = ObliterateLargestDegreeHypersurfaces(DegreeList)

50: DegreeList = TempDegreeList

51: end for
52: TempDegreeList = ObliterateQuartics(DegreeList)

53: DegreeList = TempDegreeList

54: TempDegreeList = ObliterateCubics(DegreeList)
55: DegreeList = TempDegreeList

56: TempDegreeList = ObliterateQuadrics(DegreeList)

57: FinalDegreeList = TempDegreeList
58: Sum = FinalDegreeList[0] = FinalDegreeList[1]

59: return Sum
60: end if

61: end procedure
 28

5.4 Appendix D: The Geometric Obliteration Algorithm for Cm−d−1(τ1,...,d; P0, . . . , Pm−d−1)

Algorithm 5.6. (The Geometric Obliteration Algorithm for Cm−d−1(τ1,...,d; P0, . . . , Pm−d−1))

• Imported Packages: scipy.special, math

• Input: A positive integer d and and another positive integer m ≥ d + 2.

• Output: The optimal reduction bound of τ1,...,d for m, Ξ(m, d).

We will use the same functions ComputePolarCone and ObliterateLargestDegreeHypersur-
faces which were originally deﬁned in Algorithm 5.1, as well as the functions ObliterateQuartics
and ObliterateCubics which originally deﬁned in Algorithm 5.5.

We ﬁrst implement a closed form for the type of an (m− d− 1)
st polar cone of τ1,...,d, which is Proposition
2.26 of [Sut2021C].

1: function PolarConeOfTschirnhausType(Type,Level):
2: ReturnList = [1]

3: for counter in range(1,Type):
4: NewTerm = scipy.special.comb((Level+counter), counter, exact=True)

5: OutputList.append(NewTerm)

6: end for
7: return ReturnList

8: end function
 29

This function takes the type of an (m − d − 1)
st polar cone of τ1,...,d as an input and outputs Ξ(m, d).

9: function ObliterateAMinimalNumberOfQuadrics(List):

10: a = List[0]

11: b = List[1]
12: Dimension = b + (1/2)*(a**2 + a - 2)

13: NumberOfQuadrics = 1
14: DimensionList = [Dimension]

15: while 2**NumberOfQuadrics < Dimension:

16: NumberOfQuadrics += 1
17: Dimension = NumberOfQuadrics

18: + (1/2)*(a**2 + a - NumberOfQuadrics**2 - NumberOfQuadrics)

19: DimensionList.append(Dimension)
20: end while

21: MaxList1 = [2**(NumberOfQuadrics-1)+1, DimensionList[NumberOfQuadrics-2]+m-d+1]
22: MaxList2 = [2**NumberOfQuadrics+1, DimensionList[NumberOfQuadrics-1]+m-d+1]

23: Max1 = max(MaxList1[0], MaxList1[1])

24: Max2 = max(MaxList2[0], MaxList2[1])
25: if Max2 < Max1: then

26: if MaxList2[1] < MaxList2[0]: then

27: return MaxList2[0]
28: else:

29: return MaxList2[1]
30: end if

31: else:

32: if MaxList1[1] < MaxList1[0]: then
33: return MaxList1[0]

34: else:

35: return MaxList1[1]
36: end if

37: end if

38: end function
 30

The Main procedure functions similarly to its counterpart in Algorithm 5.5. The two diﬀerences are that
the degree list is computed based on m and d and the use of ObliterateAMinimalNumberQuadrics
instead of ObliterateQuadrics.

39: procedure Main(m,d):

40: PolarConeLevel = m-d-1
41: DegreeList = PolarConeOfTschirnhausType(d,PolarConeLevel)

42: if len(DegreeList) == 2: then

43: return ObliterateAMinimalNumberQuadrics(DegreeList)
44: else if len(DegreeList) == 3: then

45: TempDegreeList = ObliterateCubics(DegreeList)

46: DegreeList = TempDegreeList
47: return ObliterateAMinimalNumberQuadrics(DegreeList)

48: else if len(DegreeList == 4: then
49: TempDegreeList = ObliterateQuartics(DegreeList)

50: DegreeList = TempDegreeList

51: TempDegreeList = ObliterateCubics(DegreeList)
52: DegreeList = TempDegreeList

53: return ObliterateAMinimalNumberQuadrics(DegreeList)

54: else:
55: for index in range(1,len(DegreeList)-3):

56: TempDegreeList = ObliterateLargestDegreeHypersurfaces(DegreeList)
57: DegreeList = TempDegreeList

58: end for

59: TempDegreeList = ObliterateQuartics(DegreeList)
60: DegreeList = TempDegreeList

61: TempDegreeList = ObliterateCubics(DegreeList)

62: DegreeList = TempDegreeList
63: return ObliterateAMinimalNumberQuadrics(DegreeList)

64: end if

65: end procedure
 31

References

[AS1976] V.I. Arnol’d and G. Shimura, Superpositions of algebraic functions, Proc. Symposia in Pure Math,
AMS, Providence, 28:45-46, 1976.

[Ber1923] E. Bertini, Introduzione alla geometria projettiva degli iperspazi con appendice sulle curve algebriche
e loro singolarit`a. Seconda edizione riveduta ed ampliata. Messina, G. Principato, 1923.

[Bra1975] R. Brauer, On the resolvent problem, Ann. Mat. Pura Appl., (4) 102:45-55, 1975.

[Bri1786] E. Bring, Meletemata quædam Mathematica circa Transformationem Æquationum Algebraicarum
(“Some Selected Mathematics on the Transformation of Algebraic Equations”), Lund, 1786.

[Che1954] G.N. Chebotarev, On the problem of resolvents., Kazan. Gos. Univ. Uˇc. Zap., (2) 114:189-193,
1954.

[CHM2017] A. Chen, Y-H. He, and J. McKay, Erland Samuel Bring’s “Transformation of Algebraic Equa-
tions,” 2017, arXiv:1711.09253v1.

[DM1998] O. Debarre and L. Manivel, Sur la vari´et´e des espaces lin´eaires contenus dans une intersection
compl`ete, Math. Ann., 312(3):549-574, 1998.

[Dix1993] J. Dixmier, Histoire de 13e probl`eme de Hilbert, Cahiers du s´eminare d’histoire des math´ematiques,
3(2):85-94, 1993.

[Dol2012] I. Dolgachev, Classical Algebraic Geometry: A Modern View, Cambridge: Cambridge University
Press, 2012.

[FW2019] B. Farb and J. Wolfson, Resolvent degree, Hilbert’s 13th problem and geometry, Enseign. Math.,
65(3-4):303-376, 2019.

[Ham1836] W. Hamilton, Inquiry into the validity of a method recently proposed by George B. Jerrard, esq.,
for transforming and resolving equation of elevated degrees, Report of the Sixth Meeting of the British
Assocation for the Advancement of Science, 295-348, 1836.

[Har2010] J. Harris, Algebraic Geometry, Springer: New York, 2010.

[Heb2021] C. Heberle, Tschirnhaus Transformations, Resolvent Degree, and Sylvester’s Method of Oblitera-
tion, in preparation.

[Hil1927] D. Hilbert, ¨Uber die Gleichung neunten Grades, Math. Ann., 97(1):243-250, 1927.

[Kle1884] F. Klein, Vorlesungen ¨uber das Ikosaeder und die Auﬂ¨osung der Gleichungen vom f¨unften Grade,
Teubner, Leipzig, 1884.

[Kle1887] F. Klein, Zur Theorie der allgemeinen Gleichungen sechsten und siebenten Grades, Math. Ann.,
28 (4):499-532, 1887.

[Kle1905] F. Klein, ¨Uber die Auﬂ¨osung der allgemeinen Gleichungen f¨unften und sechsten Grades, J. Reine
Angew. Math., 129:150-174, 1905.

[Mor1956] G.G. Morrice, Felix Klein’s “Lectures on the icosahedron and solution of equation of ﬁfth degree,”
2nd and rev. edition, New York, Dover Publications, 1956.

[Ost1959] A.M. Ostrowski, A Quantitative Formulation of Sylvester’s Law of Inertia, Proc. Natl. Acad. Sci.
USA, 45:740-744, 1959.

[Rei2022] Z. Reichstein, Hilbert’s 13th Problem for Algebraic Groups, 2022, arXiv:2204.13202.

[Rob1955] H. Robbins, A Remark on Stirling’s Formula, Amer. Math. Monthly, 62(1):26, 1955.

32

[Seg1945] B. Segre, The Algebraic Equations of Degrees 5, 9, 157 . . . , and the Arithmetic Upon an Algebraic
Variety, Ann. of Math., 46(2):287-301, 1945.

[Sut2019] A. Sutherland, Felix Klein’s “About the Solution of General Equations of Fifth and Sixth Degree
(Excerpt from a letter to Mr. K. Hensel),” 2019, arXiv:1911.02358.

[Sut2021A] A. Sutherland, Anders Wiman’s “On the Application of Tschirnhaus Transformations to the
Reduction of Algebraic Equations,” 2021, arXiv:2106.09247.

[Sut2021B] A. Sutherland, G. N. Chebotarev’s “On the Problem of Resolvents,” 2021, arXiv:2107.01006.

[Sut2021C] A. Sutherland, Upper Bounds on Resolvent Degree and Its Growth Rate, 2021, arXiv:2107.08139

[Syl1887] J.J. Sylvester, On the so-called Tschirnhausen Transformation, J. Reine Angew. Math., 100:465-
486, 1887.

[SH1887] J.J. Sylvester and J. Hammond, On Hamilton’s numbers, Philos. Trans. R. Soc. Lond., A, 178:285-
312, 1887.

[SH1888] J.J. Sylvester and J. Hammond, On Hamilton’s numbers, Part II, Philos. Trans. R. Soc. Lond., A,
179:65-72, 1888.

[Tsc1683] E. von Tschirnhaus, Methodus auferendi omnes terminos intermedios ex data aeqvatione (Method
of eliminating all intermediate terms from a given equation), Acta Eruditorum, 204-207, 1683.

[Wal2008] A. Waldron, Fano Varieties of Low-Degree Smooth Hypersurfaces and Unirationality, Bachelor
thesis, Harvard University, Cambridge, Massachusetts, 2008.

[Wim1927] A. Wiman, ¨Uber die Anwendung der Tschirnhausen-Transformation auf die Reduktion algebrais-
cher Gleichungen, Nova Acta R. Soc. scient. Uppsala, 4(16), 1927.

[Wol2021] J. Wolfson, Tschirnhaus transformations after Hilbert, Enseign. Math., 66(3):489-540, 2021.

Curtis Heberle
curtis.heberle@tufts.edu

Department of Mathematics
Tufts University
503 Boston Avenue
Bromﬁeld-Pearson
Medford, MA 02155

Alexander J. Sutherland (corresponding author)
asuther1@uci.edu

340 Rowland Hall
Department of Mathematics
University of California, Irvine
Irvine, CA 92697

Mathematics Subject Classiﬁcation: 14G25 (Primary); 12E12, 13F20 (Secondary)

Key Words: Resolvent degree, polynomials, rational points

33
