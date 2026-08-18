<!-- source: https://arxiv.org/pdf/2107.08139 | converted from PDF -->

arXiv:2107.08139v1  [math.AG]  16 Jul 2021
Upper Bounds on Resolvent Degree and Its Growth Rate

Alexander J. Sutherland
∗

July 20, 2021

Abstract

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
3.2 New Bounds From Iterated Polar Cones . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
3.3 New Bounds from Moduli Spaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
3.4 Upper Bounds on the Bounding Function G(m) . . . . . . . . . . . . . . . . . . . . . . . . . . 23

4 Comparison with Prior Bounds 27

5 Appendices 35
5.1 Explicit Bounds on RD(n) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
5.2 Explicit Approximations of F (m)/G(m) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
5.3 Proof of Technical Lemma . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37

1 Introduction

Consider the following classical problem:

Problem 1.1. Given a general polynomial zn +a1zn−1 +· · ·+an−1z +an, determine a root of the polynomial
in terms of a1, . . . , an in the simplest manner possible.

Recent work on this problem has been cast within the framework of resolvent degree (as in [FW2019]).
Informally, RD(n) is the minimal d for which there exists a formula for the roots of the generic degree n
polynomial using algebraic functions of at most d variables (see Deﬁnitions 2.13 and 2.14). While there are
currently no non-trivial lower bounds on RD(n) and it is possible in theory that RD(n) = 1 for all n, there
is a history of determining upper bounds on RD(n). This includes the work of Bring [Bri1786], Hamilton

∗This work was supported in part by the National Science Foundation under Grant No. DMS-1944862.

1

[Ham1836], Sylvester [Syl887, SH1887, SH1888], Klein [Kle1884, Kle1887, Kle1905], and Hilbert ([Hil1927]).1

Indeed, Hamilton proved that RD(6) ≤ 2, RD(7) ≤ 3, and RD(8) ≤ 4. Hilbert’s sextic conjecture, Hilbert’s
13th problem, and Hilbert’s octic conjecture, respectively, predict that these upper bounds are sharp. In
Section 3 of [Seg1945], Segre indicated the following problem:

Problem 1.2. (Segre, 1945)
Determine the large n behavior of RD(n).

The current upper bounds on RD(n) are found in [Wol2021], where Wolfson introduces a function F (m)
such that RD(n) ≤ n − m for all n ≥ F (m) (Deﬁnition 5.4 and Theorem 5.6, [Wol2021]). In this paper,
we construct a similar function G(m). For 21 ≤ n ≤ 3, 632, 428, 800, we use methods which build upon the
work of Segre. By using a theorem of Debarre and Manivel (see Theorem 3.20, or Theorem 2.1 of [DM1998]),
we are able to streamline Wolfson’s method to obtain better thresholds on upper bounds on RD(n) for
n ≥ 348, 489, 068, 134. For 3, 632, 428, 801 ≤ n ≤ 348, 489, 068, 133, we obtain the same bounds as Wolfson’s
method. More speciﬁcally, we prove the following results:

Theorem 1.3. (Key Properties of G(m))
The function G(m) of Deﬁnition 3.26 has the following properties:

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

The ﬁrst statement of Theorem 1.3 is Theorem 3.27 and, in light of this statement, we refer to F (m)
and G(m) as “bounding functions” for RD(n). Hamilton was the ﬁrst to provide a bounding function for
RD(n) (see [OEIS2021]). Brauer greatly improved Hamilton’s result when he showed that RD(n) ≤ n − m
for n ≥ (m − 1)! + 1 in [Bra1975]. Wolfson improved upon these bounds with his function F (m), but did
not provide an upper bound on F (m) in terms of elementary functions. The construction of G(m) is simpler
than F (m), but is not as explicit as Brauer’s condition. The second statement of Theorem 1.3 gives an upper
bound on RD(n) and its growth rate using elementary functions; it is Theorem 3.28.
The third statement of Theorem 1.3 shows that G(m) provides better asymptotic bounds than F (m); it
is Theorem 4.1. Note that the inequalities when 1 ≤ m ≤ 4 (which imply RD(n) = 1 for 2 ≤ n ≤ 5) are
due to the classical solutions of general polynomials of low degree. Recall that Hilbert’s Octic Conjecture
predicts that RD(8) = 4 and, if true, would imply that the bounds G(5) = F (5) = 9 cannot be improved.
We expect that the general thresholds obtained by G(m) are not sharp (including the cases of G(15) = F (15)
and G(16) = F (16)).

Historical Remarks Many of the approaches above rely on the theory of Tschirnhaus transformations. In
[Wol2021], Wolfson consolidates the history of Tschirnhaus transformations and establishes upper bounds on
RD(n) by determining points of Tschirnhaus complete intersections over ﬁeld extensions of bounded resolvent
degree. In [Wim1927], Wiman used these methods to give an argument that implied RD(n) ≤ n − 5 for n ≥ 9
and Chebotarev2 extended Wiman’s idea to argue that RD(n) ≤ n−6 for n ≥ 21 in [Che1954]. Dixmier noted
in [Dix1993], however, that Wiman’s argument has a gap and provided an algebraic argument to conclude
that RD(n) ≤ n − 5 for n ≥ 9. Moreover, the gap found in Wiman’s argument is also present in the argument
of Chebotarev.
Building on the work of Segre, we introduce (iterated) polar cones for hypersurfaces and intersections of
hypersurfaces, which we use to determine linear subvarieties on intersections of hypersurfaces over extensions
of bounded resolvent degree. In doing so, we ﬁx the gaps in the arguments of Chebotarev and provide a
geometric ﬁx for the arguments of Wiman.

1Chen, He, and McKay provide a modern English translation of [Bri1786] (originally in Latin) in [CHM2017] and the author
provides a modern English translation of [Kle1905] (originally in German) in [Sut2019].
2Note that this is G.N. Chebotarev, son of Nikolai Chebotarev.

2

Outline of the Paper In Section 2, we use the language of polar cones (respectively, iterated polar cones)
and highlight their connection to lines (respectively, k-planes) on intersections of hypersurfaces. In Section
3, we use techniques involving iterated polar cones and moduli spaces to construct a function G(m) which
yields the upper bounds on RD(n). In Section 4, we compare these new bounds to those of Wolfson. In
Appendix 5.1, we give explicit values of G(m) for small values of m. In Appendix 5.2, we provide additional
data on the ratio F (m)/G(m). In Appendix 5.3, we provide the proof of a technical lemma from Section 2.

Conventions

1. We restrict to ﬁelds K which are ﬁnitely generated C-algebras. The interested reader could instead ﬁx
an arbitrary algebraically closed ﬁeld F of characteristic zero (in lieu of C) and the statements (relative
to F ) would hold.

2. For varieties, we follow the conventions of [Har2010]. Namely, we deﬁne a projective (respectively,
aﬃne) variety to be a closed algebraic set in Pn
K (respectively, An
K). When we simply say variety, we
mean a quasi-projective variety. In particular, we do not assume that varieties are irreducible.

3. For a collection of homogeneous polynomials f1, . . . , fs ∈ K[x0, . . . , xr], we write V(f1, . . . , fs) for the
subvariety of Pr
K determined by the conditions f1 = · · · = fs = 0.

4. Given a subvariety V ⊆ Pr
K, we use the notation V (K) to refer to the set of K-rational points of V .

5. We write Kn to mean C(a1, . . . , an), a purely transcendental extension of C with transcendence basis
a1, . . . , an.

6. We write Gr(k, r) to denote the Grassmannian of k-dimensional subspaces of Cr and Gr(k, r) for the
space of k-planes in Pr
C. In particular, Gr(k, r) ∼= Gr(k + 1, r + 1).

7. Given a polynomial ring K[x0, . . . , xr] over a ﬁeld K, we write

• K[x0, . . . , xr](d) for the vector space of degree d polynomials,

• K[x0, . . . , xr]∨
(d) for its dual space,

• S∗ (K[x0, . . . , xr]∨
(d)) for the corresponding free commutative K-algebra, and

• S∗ (K[x0, . . . , xr]∨
(d))GL(K,r+1) for the associated graded ring of GL(K, r + 1)-invariants.

8. We write log to mean the base e logarithm.

With respect to convention 2, note that for generic choices of f1, . . . , fs, V(f1, . . . , fs) is a complete
intersection. However, there are examples of such choices which are not complete intersections, such as the
twisted cubic curve. Our methods apply to all such choices and to avoid confusion, we generally use the
terminology “intersection of hypersurfaces” instead of “complete intersection” to refer to a variety of the
form V(f1, . . . , fs). Additionally, we note that conventions 5 and 6 are primarily for Deﬁnition 3.12 and
Remark 3.14, respectively.

Acknowledgements I thank Jesse Wolfson for his generous support. Next, I thank Joshua Jordan for
several key conversations and general support. I thank Benson Farb, Hannah Knight, Curt McMullen,
and Zinovy Reichstein for helpful comments on a draft. Finally, I thank Kenneth Ascher, Claudio G´omez-
Gonz´ales, and Roman Vershynin for helpful conversations.

2 Polar Cones

2.1 An Introduction to Polar Cones

In [Seg1945], Segre refers to a “well-known fact” which is the main ingredient for many of his proofs. This
fact may no longer be as well-known as it once was. Deﬁnitions 2.1, 2.2, and 2.4 are necessary to state the

3

fact, which we include as Lemma 2.5 and refer to as Bertini’s Lemma (for Hypersurfaces), since the reference
Segre gives for this fact is [Ber1923].

Deﬁnition 2.1. (Polars of a Polynomial)
Let f ∈ K[x0, . . . , xr] be a homogeneous polynomial of degree d and P ∈ Pr(K). For every n ∈ Z≥1, let

[n] = {0, 1, . . . , n} ,
[n]∗ = {1, . . . , n} .

For each 0 ≤ k ≤ d − 1, we set
 Ik := {
(i0, . . . , ir) ∈ Z
r+1
≥0 | i0 + · · · + ir = k} .

We have r + 1 ﬁrst partial derivatives ∂
∂x0 , . . . , ∂
∂xr . To obtain an (ordered) kth partial derivative of f , we
make k successive choices of ﬁrst partial derivatives. Hence, the set of all (ordered) kth partial derivatives is
indexed by I ∗
k = HomSet([k]∗, [r]). For any ι ∈ I ∗
k and 0 ≤ j ≤ r, we set

|ι|(j) := ∣
∣ι
−1(j)
∣
∣

and note that (|ι|(0), . . . , |ι|(r)) ∈ Ik. Additionally, we use the shorthand

∂j0
0 · · · ∂jl
l f := ∂j0+···+jl f

∂x
j0
0 · · · ∂x
jl
l .

With this notation set, the kth polar of f at P is the homogeneous polynomial of degree d − k

t(k, f, P )(y0, . . . , yr) := ∑

ι∈I ∗
d−k
 (∂|ι|(0)
0 · · · ∂|ι|(r)
r f )∣
∣
∣
∣P y|ι|(0)
0 · · · y|ι(r)|
r .

Deﬁnition 2.2. (Polars of a Hypersurface)
Let V = V(f ) be a hypersurface in Pr
K and P ∈ V (K). The kth polar of V at P is

T (k, f, P ) := V (t(k, f, P )) ⊆ Pr
K.

Example 2.3. Using the conventions of Deﬁnition 2.2, we observe that

t(0, f, P )(x0, . . . , xr) = f (x0, . . . , xr),

t(d, f, P )(x0, . . . , xr) = f (P ),

so the 0th polar of V(f ) at P is T (0, f, P ) = V for all P and the d
th polar of V(f ) at P is

T (d, f, P ) =
 {Pr
K, if P ∈ V(f ),
∅, if P ̸∈ V(f ).

Moreover, if V is smooth at P , then T (d − 1, f, P ) is the tangent hyperplane of V at P ; this motivates
the use of T (k, f, P ) for polar hypersurfaces and hence t(k, f, P ) for their deﬁning polynomials.

Deﬁnition 2.4. (Polar Cone of a Hypersurface)
Let V = V(f ) be a degree d hypersurface in Pr
K and P ∈ V (K). The (ﬁrst) polar cone of V at P is

C(V ; P ) :=
 d−1⋂

k=0 T (k, f, P ).

We can now state Lemma 2.5, which motivates the terminology of the previous deﬁnition.

4

Lemma 2.5. (Bertini’s Lemma for Hypersurfaces)
3

Let V = V(f ) be a hypersurface in Pr
K and P ∈ V (K). Then, C(V ; P ) is a cone with vertex P which is
contained in V .

Example 2.6. (Lines on Cubic Surfaces)
Let V ⊆ P3
K be a smooth cubic surface. If K = K, then V contains exactly 27 lines L1, . . . , L27. If
P ∈ V (K) lies on exactly one line L (respectively, exactly two lines L1, L2), then C(V ; P ) = L (respectively,
C(V ; P ) = L1 ∪ L2). Most points Q ∈ V (K), however, do not lie on any line and in such a case C(V ; Q) is
the point Q with multiplicity 6. We will generally consider ﬁelds K which are not algebraically closed, in
which case we may need to pass to an extension of K to obtain a line.

Remark 2.7. For an alternative modern perspective on Deﬁnitions 2.1 and 2.2, Remark 2.3, and Lemma 2.8,
see p.5-6 of [Dol2012] - in particular, equations 1.8 through 1.11. Note that Lemma 2.5 follows directly from
the following technical lemma. The proof of Lemma 2.8 can be found in Appendix 5.3; it is not exceedingly
complicated, but is notationally cumbersome.

Lemma 2.8. (Technical Lemma)
Let P, Q ∈ Pr(K) and f ∈ K[x0, . . . , xr] be a homogeneous polynomial of degree d. Applying a projective
change of coordinates as necessary, we assume that

P = [1 : p1 : · · · : pr],
Q = [1 : q1 : · · · : qr],

so that the line determined by P and Q is

L(P, Q)(K) = {[1 : λp1 + µq1 : · · · : λpr + µqr] | [λ : µ] ∈ P1(K)
} .

For any point Rλ:µ = [1 : λp1 + µq1 : · · · : λpr + µqr] ∈ L(P, Q)(K),

f (Rλ:µ) = f (λP ) + f (µQ) +
 d−1∑

k=1
 1
k! t(d − k, f, λP )(µQ). (1)

Remark 2.9. Lemma 2.5 implies that for every point Q ∈ C(V ; P )(K) \ {P }, the line L(P, Q) determined
by P and Q lies in V . Furthermore, a line L lies on an intersection of hypersurfaces V(f1, . . . , fn) exactly
when it lies on each V(fi). This motivates Deﬁnition 2.10 and implies Lemma 2.11.

Deﬁnition 2.10. (Polar Cone of an Intersection of Hypersurfaces)
Let V = V(f1, . . . , fn) ⊆ Pr
K be an intersection of hypersurfaces and P ∈ V (K). The (ﬁrst) polar cone of
V at P is
 C(V ; P ) :=
 n⋂

i=1 C(V(fi); P ).

Lemma 2.11. (Bertini’s Lemma for Intersections of Hypersurfaces)
Let V = V(f1, . . . , fn) ⊆ Pr
K be an intersection of hypersurfaces and P ∈ V (K). Then, C(V ; P ) is a cone
with vertex P which is contained in V .

Remark 2.12. (Passing to Extensions)
We continue using the notation of Lemma 2.11. It is easy to see that when K is algebraically closed and
dim (C(V ; P )) ≥ 1, the set C(V ; P )(K) \ {P } is not empty. Thus, any choice of Q ∈ C(V ; P ) \ {P } determines
a line on V containing P . When K is not algebraically closed, however, it may be that C(V ; P )(K) = {P }.
In what follows, we will often extend scalars to an extension L/K over which we can determine an L-rational
point.

3See Chapter 8 of [Ber1923] for the reference given in [Seg1945].

5

2.2 Resolvent Degree

Resolvent degree is an invariant introduced independently by Brauer in [Bra1975] and Arnol’d-Shimura in
[AS1976]. Farb and Wolfson summarize the history of resolvent degree and signiﬁcantly broaden the resolvent
degree framework in [FW2019], which we refer the reader to for background on resolvent degree. We now
recall the deﬁnition of resolvent degree for ﬁnite ﬁeld extensions and for generically ﬁnite, dominant, rational
maps of C-varieties. We refer the reader to Section 4 of [Wol2021] for how to extend this deﬁnition to
arbitrary dominant, rational maps. We also remind the reader that in this paper, we work only with ﬁelds
that are ﬁnitely generated C-algebras.

Deﬁnition 2.13. (Resolvent Degree of Field Extensions)
Let L/K be a ﬁnite extension of C-ﬁelds. The resolvent degree of L/K, denoted RD(L/K), is the minimum
d for which there is a tower of ﬁnite ﬁeld extensions

K = E0 ֒! E1 ֒! · · · ֒! Eℓ

such that L embeds into Eℓ over K and for each Ei+1/Ei, there is a ﬁnite extension of ̃Fi/Fi with tr.degC(Fi) ≤
d such that
 Ei+1 ∼= Ei ⊗Fi ̃Fi.

Deﬁnition 2.14. (Resolvent Degree of Generically Finite, Dominant Maps)
Let Y 99K X be a generically ﬁnite, dominant, rational map of C-varieties. The resolvent degree of
Y 99K X, denoted RD(Y 99K X), is the minimum d for which there is a tower of generically ﬁnite, dominant,
rational maps
 Eℓ 99K · · · 99K E1 99K E0 ⊆ X

such that E0 ⊆ X is a dense Zariski open; Eℓ 99K E0 factors through Y 99K X; and for each πi : Ei+1 99K Ei,
there exists a surjective morphism ̃Zi ! Zi with dim (Zi) ≤ d, a Zariski open E◦
i ⊆ Ei, and a morphism
E◦
i ! Zi such that
 π−1
i (E◦
i ) ∼= E◦
i ×Zi ̃Zi.

Remark 2.15. (Compatibility of Resolvent Degree Deﬁnitions)
We note that Deﬁnitions 2.13 and 2.14 are equivalent. For an irreducible, aﬃne C-variety X, the equivalence
of deﬁnitions is derived from the classical equivalence which sends X to its function ﬁeld C(X); the general
case follows from invariance of resolvent degree under birational equivalence. We refer the reader to [FW2019]
for details.

Remark 2.16. (RD(n) Notation)
We write RD(n) for the resolvent degree of the general degree n polynomial. Recall that Kn = C(a1, . . . , an).
If f (z) = zn + a1zn−1 + · · · + an−1z + an ∈ Kn[z], and K ′
n = Kn[z]/(f (z)), then

RD(n) = RD(K ′
n/Kn) = RD (Spec (K ′
n) ! Spec (Kn)) .

Remark 2.17. (RD of a Composition)
We will frequently use the following ﬁeld-theoretic version of Lemma 2.7 of [FW2019] without explicit refer-
ence: given a tower of ﬁeld extensions
 E0 ֒! E1 ֒! · · · Ek,

the resolvent degree of the composition is the maximum of the resolvent degree of the components, e.g.

RD(Ek/E0) = max {RD(Ej /Ej−1) | 1 ≤ j ≤ k} .

Lemma 2.18. (Upper Bound on RD(L/K))
Let L/K be a degree ℓ ﬁeld extension. Then, RD (L/K) ≤ RD(ℓ).

6

Proof. As L and K are C-ﬁelds, they have characteristic zero. Hence, the Primitive Element Theorem yields
that we need only solve a degree ℓ polynomial to determine a primitive element ζ of L/K. The isomorphism
L ∼= K(ζ) then establishes the claim.

We will frequently make use of the previous lemma without explicit reference after giving an upper bound
on the degree of an extension.

Proposition 2.19. (Determining Rational Points over Extensions)
Let V ⊆ Pr
K be a degree d subvariety. Then, there is an extension L/K with RD(L/K) ≤ RD(d) over which
we can determine a rational point of V .

Proof. Set ℓ = dim(V ). For a generic (r − ℓ)-plane Λ, the intersection V ∩ Λ has dimension 0 and thus has d
K-points (with multiplicity) in any algebraic closure K of K; we denote these points by Q1, . . . , Qd. Observe
that the polynomial
 f (z) = (z − Q1) (z − Q2) · · · (z − Qd)

has coeﬃcients deﬁned over K. Let m(z) be an irreducible factor of f (z) over K. We set L := K[z]/(m(z))
and observe that we can determine an L-point of V by construction. Lemma 2.18 yields that RD(L/K) ≤
RD(d).

Remark 2.20. (Extensions Given By Solving Polynomials)
Given Proposition 2.19, we henceforth say that we can determine a point of V by solving a degree d polyno-
mial.

2.3 Iterated Polar Cones and k-Polar Points

As we have established, for an intersection of hypersurfaces V and P ∈ V (K), points of C(V ; P ) \ {P }
determine lines on V . Next, we will iterate the polar cone construction in a method to determine k-planes
on intersections of hypersurfaces (as in Lemma 2.24). To do so, we must ﬁrst introduce additional deﬁnitions
and notation.

Remark 2.21. (Linear Subvarieties)

• For any points P0, . . . , Pk ∈ Pr(K), we denote the linear subsvariety they determine by L(P0, . . . , Pk).
Note that L(P0, . . . , Pk) has dimension at most k.

• Henceforth, when we say k-plane, we mean a linear subvariety of Pr of dimension k. When k = 1, we
say line instead of 1-plane and when k = 2, we say plane instead of 2-plane.

Deﬁnition 2.22. (Iterated Polar Cones & k-Polar Points)
Let V ⊆ Pr
K be an intersection of hypersurfaces and P0 ∈ V (K); we set C1(V ; P0) := C(V ; P0). Given
additional points P1, . . . , Pk−1 ∈ V (K) such that

Pℓ−1 ∈ Cℓ−1(V ; P0, . . . , Pℓ−2) \ L(P0, . . . , Pℓ−2) (2)

for 0 ≤ ℓ ≤ k − 1, the kth polar cone of V at P0, . . . , Pk−1 is

Ck(V ; P0, . . . , Pk−1) := C (
Ck−1(V ; P0, . . . , Pk−2), Pk−1) .

We refer to an ordered collection of points (P0, . . . , Pk) that satisfy (2) for each 0 ≤ ℓ ≤ k − 1 as a k-polar
point of V .

When the points in question have already been speciﬁed, we simply refer to the kth polar cone of V .
When such points exist but have not been speciﬁed, we refer to a kth polar cone of V . It is occasionally
useful to refer to V itself as a zeroth polar cone of V (at any rational point of V ).

Remark 2.23. (Iterated Polar Cones Are Nested)
Note that if (P0, . . . , Pk) is a k-polar point of an intersection of hypersurfaces V ⊆ Pr
K, then

Ck(V ; P0, . . . , Pk−1) ⊆ Ck−1(V ; P0, . . . , Pk−2) ⊆ · · · ⊆ C2(V ; P0, P1) ⊆ C1(V ; P0) = C(V ; P0).

7

Lemma 2.24. (Polar Point Lemma)
Let V ⊆ Pr
K be an intersection of hypersurfaces and let (P0, . . . , Pk) be a k-polar point of V . Then,
L(P0, . . . , Pk) ⊆ V is a k-plane.

Proof. We prove the claim by induction on k and observe that the case of k = 1 follows immediately from
Lemma 2.11. Now, consider arbitrary k > 1 and let (P0, . . . , Pk) be a k-polar point of V . Then, (P1, . . . , Pk)
is a (k − 1)-polar point of C(V ; P0). Recall that C(V ; P0) is a cone and L(P1, . . . , Pk) ⊆ C(V ; P0) is a
(k − 1)-plane which does not contain the vertex P0, hence L(P0, . . . , Pk) ⊆ V is a k-plane.

Deﬁnition 2.25. (Type of an Intersection of Hypersurfaces)

Given an intersection of hypersurfaces V ⊆ Pr
K, we say that V is of type [ d d − 1 · · · 2 1
ℓd ℓd−1 · · · ℓ2 ℓ1
] if V has

multi-degree
 (d, . . . , d
︸ ︷︷ ︸
ℓd many
 , d − 1, . . . , d − 1
︸ ︷︷ ︸
ℓd−1 many
 , · · · , 2, . . . , 2
︸ ︷︷ ︸
ℓ2 many
 , 1, . . . , 1
︸ ︷︷ ︸
ℓ1 many
 ).

If ℓj = 0 for any 1 ≤ j ≤ d − 1, we may omit it in the presentation; e.g. an intersection of four quadrics is

of type [2
4

]. When d ≥ 2 and each ℓj = 1, we abbreviate the notation and say V is of type (1, . . . , d). When

d ≥ 2, ℓ1 = 0, and the other ℓj = 1, we say V is of type (2, . . . , d).
Consider an intersection of hypersurfaces V = Vd ∩ · · · ∩ V1 of type (1, . . . , d) in Pr
K with deg(Vj) = j.
Note that V1 ∼= Pr−1
K and thus we can also consider V as an intersection of hypersurfaces of type (2, . . . , d)
inside V1 ∼= Pr−1
K .

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

for r ≥ (
k+d
d−1)
.

Proof. We proceed by induction on k and note that the k = 1 case follows from the deﬁnition of a polar cone
of an intersection of hypersurfaces, along with the observation that (
1+j
j ) = 1 + j for each 2 ≤ j ≤ n − 1.
Now, suppose the claim is true for an arbitrary k. The number of hypersurfaces of degree j in a (k + 1)
st

polar cone is exactly the number of hypersurfaces of degree at least j in a kth polar cone, e.g. j∑

i=0
 (
k+i
i )
.

However,
 j∑

i=0
 (
k + i
i
 ) = (
k + j + 1
j
 ) = (
(k + 1) + j
j
 )
,

by induction on j, using that (
a
b) = (
a−1
b ) + (
a−1
b−1) for positive integers a > b. This combinatorial argument

also yields that d−1∑

i=0
 (
k+i
i ) = (
k+d
d−1)
.

In Subsection 3.2, we will use iterated polar cones to establish new upper bounds on RD(n). We ﬁrst use
iterated polar cones to determine k-planes on intersections of quadrics.

Proposition 2.27. (k-Polar Points Intersections of Quadrics)

Let V ⊆ Pr
K be an intersection of hypersurfaces of type [2
ℓ
] and take k ≥ 1. For r ≥ (k + 1)ℓ + k, we can

determine a k-polar point (P0, . . . , Pk) over an extension L/K with RD(L/K) ≤ RD(2ℓ). Moreover, for any
point P ∈ V (K), we can determine a k-plane containing P over such an extension L.

8

Proof. When r > (k + 1)ℓ + k, we can restrict to an arbitrary (k + 1)ℓ + k-plane in Pr
K and hence it suﬃces
to consider the case where r = (k + 1)ℓ + k. Note that for a quadric hypersurface, a kth polar cone consists

of the original quadric and k hyperplanes (
e.g. is of type [2 1
1 k
])
. Hence, a kth polar cone of V has type
[
2 1
ℓ kℓ

]. We proceed by induction on k.

When k = 1 and r = 2ℓ + 1, dim(V ) ≥ ℓ + 1 > 0 and Proposition 2.19 allows us to determine a point

P0 ∈ V (L1) over an extension L1/K of degree 2ℓ. The polar cone C(V ; P0) is of type [2 1
ℓ ℓ
], hence

dim (C(V ; P0)) ≥ (2ℓ + 1) − (2ℓ) = 1 > 0.

We use Proposition 2.19 to determine a point P1 ∈ C(V ; P0)(L) \ {P0} over an extension L/L1 of resolvent
degree at most RD (
2ℓ)
. Note that (P0, P1) is a 1-polar point of V by construction.
We now consider the case of an arbitrary k > 1. By induction, we pass to an extension L1/K of degree
at most 2ℓ to determine a (k − 1)-polar point (P0, . . . , Pk−1) of V . Observe that

dim (
Ck(V ; P0, . . . , Pk−1)
) ≥ (k + 1)ℓ + k − (k + 1)ℓ ≥ k.

By Proposition 2.19, we can pass to an extension L/L1 of degree at most 2ℓ to determine an L-rational point
Pk of Ck(V ; P0, . . . , Pk−1) \ L(P0, . . . , Pk−1). By construction, (P0, . . . , Pk) is a k-polar point of V .
For the ﬁnal claim, note that we can replace P0 with P in the proof and then Lemma 2.24 yields
L(P, P1, . . . , Pk) is a suitable k-plane.

3 New Upper Bounds on RD(n)

3.1 Tschirnhaus Transformations

We recall pertinent information about Tschirnhaus transformations here and refer the reader to [Wol2021]
for a more complete treatment. Recall that Kn = C(a1, . . . , an), a purely transcendental extension of C with
transcendence basis a1, . . . , an.

Deﬁnition 3.1. (General Polynomials)
The general polynomial of degree n is the polynomial

φn(z) = zn + a1zn−1 + · · · + an−1z + an ∈ Kn[z].

Deﬁnition 3.2. (Tschirnhaus Transformations)
A Tschirnhaus transformation of the general degree n polynomial is an isomorphism of Kn-ﬁelds

Kn[z]/(φn(z)) ∼= Kn[z]/(ψ(z)),

where
 ψ(z) = zn + b1zn−1 + · · · + bn−1z + bn.

It has type (j1, . . . , jk) if bj1 = · · · = bjk = 0.

Remark 3.3. (Description of Tschirnhaus Transformations)
Given primitive elements ζφ of Kn[z]/(φn(z)) and ζψ of Kn[z]/(ψ(z)), every Kn-algebra isomorphism Υ :
Kn[z]/(φn(z)) ! Kn[z]/(ψ(z)) is determined by Υ(ζφ), which is a Kn-linear combination of powers of ζψ:

Υ(ζφ) = w0 + w1ζψ + · · · + wn−1ζn−1
ψ .

Note that Υ is an isomorphism exactly when there is some j ≥ 1 such that wj ̸= 0. Let An
Kn be the aﬃne
space with coordinates w0, . . . , wn−1 and denote the w0-axis of An
Kn by A1
Kn,0. Corollary 3.3 of [Wol2021]
shows that the space of Tschirnhaus transformations is exactly

̃T n
Kn = An
Kn \ A1
Kn,0.

9

However, we need only work with Tschirnhaus transformations up to re-scaling. Let Pn−1
Kn denote the
projective space with coordinates w0, . . . , wn−1 and observe that the space of Tschirnhaus transformations
up to re-scaling is T n
Kn = Pn−1
Kn \ {[1 : 0 : · · · : 0]} .

Moreover, each bm in Deﬁnition 3.2 is a homogenous polynomial of degree m in the w0, . . . , wn−1 with
coeﬃcients in Kn (e.g. an element an of Kn[w0, . . . , wn−1](m)). In the following deﬁnition, we build upon
the language used in [Wol2021].

Deﬁnition 3.4. (Tschirnhaus Complete Intersections)
Fix n ∈ Z≥1. For any m ∈ {1, . . . , n}, the mth extended Tschirnhaus hypersurface is

τm := V(bm) ⊆ Pn
Kn ,

and the mth extended Tschirnhaus complete intersection is

τ1,...,m := τ1 ∩ · · · ∩ τm ⊆ Pn
Kn.

Similarly, the mth Tschirnhaus hypersurface is

τ ◦
m := τm ∩ T n
Kn = τm \ {[1 : 0 : · · · : 0]} ,

and the mth Tschirnhaus complete intersection is

τ ◦
1,...,m := τ1,...,m ∩ T n
Kn \ {[1 : 0 : · · · : 0]} .

Remark 3.5. (RD Bounds from Tschirnhaus Transformations)
Given a Tschirnhaus transformation Υ (up to re-scaling) of type (1, . . . , m − 1) of φn(z) (i.e. a point of
τ ◦
1,...,m−1), we need only consider the normal form

zn + bmzn−m + · · · + bn−1z + bn, (3)

as Υ−1 takes the roots of (3) to the roots of φn. We can then re-scale the roots over n√
bn (over a cyclic
extension) and arrive at the normal form

zn + cmzn−m + · · · + cn−1z + 1. (4)

Note that (4) is an algebraic function of n − m variables and so if we can determine an L-rational point of
τ ◦
1,...,m−1 over an extension L/Kn of suﬃciently small resolvent degree, we can conclude that RD(n) ≤ n − m.

3.2 New Bounds From Iterated Polar Cones

Deﬁnition 3.6. (Sub-Intersections of Given Level)

Let V ⊆ Pr
K be an intersection of hypersurfaces of type [ d d − 1 · · · 2 1
ℓd ℓd−1 · · · ℓ2 ℓ1
] deﬁned by

V =
 d⋂

i=1
 ℓi⋂

j=1 V(fi,j),

with deg(fi,j) = i for all 1 ≤ j ≤ ℓi. For each 1 ≤ d
′ ≤ d, the sub-intersection of V of level d
′ is the
intersection of all deﬁning hypersurfaces of V of degree d
′ and is denoted Vd′, i.e.

Vd′ := V(fd′,1) ∩ · · · ∩ V(fd′,ℓd′ ).

Theorem 3.7. (The n − 6 Bound)
For n ≥ 21, RD(n) ≤ n − 6.
 10

Proof. First, suppose that we can determine a plane Λ ⊆ τ ◦
1,2,3 over an extension of Kn of low resolvent
degree. Observe that deg (Λ ∩ τ1,...,5) = 20 and, by Proposition 2.19, we can solve a polynomial of degree at
most 20 to determine a point Q of Λ ∩ τ1,...,5.
From Lemma 2.24, it suﬃces to determine a 2-polar point (P0, P1, P2) on τ1,2,3 ⊆ T n such that L(P0, P1, P2) ⊆
τ ◦
1,2,3 for n = 20 over a suitable extension. Indeed, we show the stronger claim that we can determine such a
2-polar point of τ1,2,3 when n = 19 over an extension of resolvent degree at most RD(12), which implies the
result for larger n.
Recall that when n = 19, we work in P18
Kn (as in Remark 3.3). To ensure that the plane Λ associated to
the 2-polar point we determine lies in τ ◦
1,2,3, we pass to a hyperplane H which does not contain [1 : 0 : · · · : 0].
We can determine a point P0 ∈ (τ1,2,3 ∩ H)(L1), where L1/Kn is an extension of degree 6, by Proposition

2.19. The polar cone C(τ1,2,3 ∩ H; P0) has type [3 2 1
1 2 4

] and so

dim (C(τ1,2,3; P0)) ≥ 18 − 7 = 11.

Hence, we can determine a point P1 ∈ C(τ1,2,3 ∩ H; P0)(L2) \ {P0} over a degree 12 extension L2/L1.

The second polar cone C2(τ1,2,3 ∩ H; P0, P1) has type [3 2 1
1 3 7
]. As C2(τ1,2,3 ∩ H; P0, P1)1 is the intersec-

tion of 7 hyperplanes, C2(τ1,2,3 ∩ H; P0P1)1 ∼= P11
L2. Denote one of the quadrics deﬁning C2(τ1,2,3 ∩ H; P0, P1)
by U . Applying Proposition 2.27 to U ∩ C2(τ1,2,3 ∩ H; P0, P1)1 (with ℓ = 1 and k = 5) yields that we
can determine a 5-plane Λ′ ⊆ U ∩ C2(τ1,2,3 ∩ H; P0, P1)1 over a quadratic extension L3/L2. Note that

C2(τ1,2,3 ∩ H; P0, P1) ∩ Λ′ has type [3 2
1 2
] inside Λ′ and

dim (
C2(τ1,2,3 ∩ H; P0, P1) ∩ Λ′) ≥ 5 − 3 ≥ 2.

Thus, we can determine a point P2 ∈ (
C2(τ1,2,3 ∩ H; P0, P1) ∩ Λ′) \ L(P0, P1) over an extension L4/L3 of
degree
 deg (
C2(τ1,2,3 ∩ H; P0, P1) ∩ Λ′) = 3 · 22 = 12,

and (P0, P1, P2) is a 2-polar point of τ1,2,3 ∩ H by construction.

Remark 3.8. (Fixing Gaps in [Che1954])
As noted in Section 1, Chebotarev gave an argument that RD(n) ≤ n − 6 for n ≥ 21 in [Che1954]. However,
his argument had gaps (similar to those of Wiman in [Wim1927] and which are also in the translation
[Sut2021A]). There are two speciﬁc issues. First, Chebotarev uses a geometric argument of Wiman which
assumed without proof that certain intersections of hypersurfaces in aﬃne space were generic (see p.190-191 of
[Che1954] or p.3 of the translation [Sut2021B]). Additionally, Lemma 1 and Lemma 2 of [Che1954] (Lemma
2.1 and Lemma 2.2 of the translation [Sut2021B]) also assume, but do not prove, that certain intersections
of aﬃne hypersurfaces are generic. The above proof of Theorem 3.7 ﬁxes the issues associated to the use of
Lemma 1 and Lemma 2 in the proof of the un-numbered theorem of [Che1954] (Theorem 2.3 of [Sut2021B]).
Additionally, this argument can be adapted to give a geometric proof of Wiman’s claims, although Dixmier
has already given an algebraic proof in the appendix of [Dix1993].

Remark 3.9. (Notation for Theorem 3.10)
We move from ﬁnding a plane on τ ◦
1,2,3 to ﬁnding k-planes on τ ◦
1,2,3,4 to improve the bound on n for which
RD(n) ≤ n − m for m between 7 and 14. To simplify the statement of Theorem 3.10, we introduce two
functions ρ : {1, 2, 3, 4, 5, 6, 7, 8, 9} ! Z and η : {1, 2, 3, 4, 5, 6, 7, 8, 9} ! Z. For each k, ρ(k) is the ambient
dimension needed in our method to determine a k-plane on τ1,2,3,4 and η(k) is the degree of the largest
extension needed. The functions ρ and η are deﬁned by the following values:

k 1 2 3 4 5 6 7 8 9
ρ(k) 25 60 264 806 1773 8905 34546 77040 612581
η(k) 36 108 324 972 2916 8748 26244 78732 236196

Theorem 3.10. (The n − 7, . . . , n − 14 Bounds)
 11

1. For n ≥ 109, RD(n) ≤ n − 7.

2. For n ≥ 325, RD(n) ≤ n − 8.

3. For each 9 ≤ ℓ ≤ 14 and n > (ℓ−1)!
24 , RD(n) ≤ n − ℓ.

Proof. We claim that we can determine a k-plane Λ ⊆ τ ◦
1,2,3,4 over an extension of Kn of resolvent degree at
most RD(η(k)) when n ≥ ρ(k). Given this claim, Λ ∩ τ1,...,k+4 has degree (k+4)!
24 . By Proposition 2.19, we can
solve a polynomial of degree at most (k+4)!
24 to determine a point Q of Λ ∩ τ ◦
1,...,k+4. Then, the new bounds
on resolvent degree follow immediately from Remark 3.5. Note that for the n − 7 bound (respectively, n − 8
bound), k = 2 (respectively, k = 3) and η(k) ≥ (k+4)!
24 .
It remains to determine the k-planes on τ ◦
1,2,3,4 and, by Lemma 2.24, it suﬃces to construct a k-polar
point (P0, . . . , Pk) of τ1,2,3,4 which does not contain [1 : 0 : · · · : 0]. For each k, it suﬃces to prove the claim
when n = ρ(k), as we can always restrict to a Pρ(k)
Kn when n > ρ(k). In each case, we immediately pass to a
hypersurface which does not contain [1 : 0 : · · · : 0] and, to simplify notation, the computations that follow
all start within this hypersurface. Recall that the space of Tschirnhaus transformations (up to re-scaling) is
Pn−1
Kn and we are passing to a hypersurface, so for each k we work in a Pρ(k)−2
Kn . In each case, the extensions
will be enumerated as Lj and we always begin with L1/Kn. Similarly, the k-planes we determine will be
enumerated as Λℓ and we always begin with Λ1. Additionally, Proposition 2.26 gives the type of the relevant
polar cone.

Case: k = 1. Recall that ρ(1) = 25 and thus we work in P23
Kn. By Proposition 2.19, we can determine a
point P0 of τ1,2,3,4 over an extension L1/Kn of degree at most 24. The polar cone C(τ1,2,3,4; P0) has type[
4 3 2 1
1 2 3 4

]. Note that C(τ1,2,3,4; P0)1 is an intersection of 4 hyperplanes and thus C(τ1,2,3,4; P0)1 ∼= P19
L1.

Since C(τ1,2,3,4; P0)2 ∩ C(τ1,2,3,4; P0)1 has type [2
3

] inside C(τ1,2,3,4; P0)1 and

19 = (4 + 1)(3) + 4,

Proposition 2.27 (with k = 4 and ℓ = 3) allows us to determine a 4-plane Λ1 ⊆ C(τ1,2,3,4; P0)2 ∩ C(τ1,2,3,4; P0)1

over an extension L2/L1 of degree at most 8. Observe that C(τ1,2,3,4; P0) ∩ Λ1 has type [4 1
1 2
], hence

dim (C(τ1,2,3,4; P0) ∩ Λ1) ≥ 4 − 3 ≥ 1.

Consequently, we can determine a rational point P1 of C(τ1,2,3,4; P0) \ {P0} over an extension L3/L2 of
degree at most 36. By construction, (P0, P1) is a 1-polar point of τ1,2,3,4.

Case: k = 2. Note that ρ(2) = 60, so we work in P58
Kn. From the k = 1 case, we pass to an extension
L1/Kn of resolvent degree at most RD(36) and assume that we have a 1-polar point (P0, P1). The second

polar cone C2(τ1,2,3,4; P0, P1) has type [
4 3 2 1
1 3 6 10

]. Observe that C2(τ1,2,3,4; P0, P1)1 is an intersection of

10 hyperplanes, hence C2(τ1,2,3,4; P0, P1)1 ∼= P48
L1. Moreover, C2(τ1,2,3,4; P0, P1)2 ∩ C2(τ1,2,3,4; P0, P1)1 has type
[
2
6
] in C2(τ1,2,3,4; P0, P1)1 and
 48 = (5 + 1)(6) + 5.

Thus, applying Proposition 2.27 (with k = 5 and ℓ = 6) allows us to determine a 5-plane Λ1 ⊆
C2(τ1,2,3,4; P0, P1)2∩C2(τ1,2,3,4; P0, P1)1 over an extension L2/L1 of degree at most 64. Note that C2(τ1,2,3,4; P0, P1)∩

Λ1 has type [4 3
1 3
] inside Λ1, hence

dim (
C2(τ1,2,3,4; P0, P1) ∩ Λ1) ≥ 6 − 4 ≥ 2.

As a result, we can determine a rational point P2 of C2(τ1,2,3,4; P0, P1)\ L(P0, P1) over an extension L3/L2
of degree at most 108 and our method ensures that (P0, P1, P2) is a 2-polar point of τ1,2,3,4.

12

Case: k = 3. Recall that ρ(3) = 264 and so we work in P262
Kn . Using the k = 2 case, we pass to an extension
L1/Kn of resolvent degree at most RD(108) and assume that we have a 2-polar point (P0, P1, P2). Observe

that the third polar cone C3(τ1,2,3,4; P0, P1, P2) has type [4 3 2 1
1 4 10 20

]. Thus, C3(τ1,2,3,4; P0, P1, P2)1 is an

intersection of 35 hyperplanes and C3(τ1,2,3,4; P0, P1, P2)1 ∼= P242
L1 . Inside C3(τ1,2,3,4; P0, P1, P2)1, C3(τ1,2,3,4; P0, P1, P2)2∩

C3(τ1,2,3,4; P0, P1, P2)1 has type [ 2
10

]
. However, 28 = 256 is the largest power of 2 less than 4 · 34 = 324. As

a result, we split C3(τ1,2,3,4; P0, P1, P2)2 into two intersections of quadrics:

C3(τ1,2,3,4; P0, P1, P2)2 = W1 ∩ W2,

where W1 has type [2
2

] and W2 has type [2
8
]
. Next, observe that

242 = (80 + 1)(2) + 80,

and thus applying Proposition 2.27 (with k = 75 and ℓ = 2) allows us to determine an 80-plane Λ1 ⊆

W1 ∩ C3(τ1,2,3,4; P0, P1, P2)1 over an extension L2/L1 of degree at most 4. Also, W2 ∩ Λ1 has type [
2
8
] in Λ1

and 80 = (8 + 1)(8) + 8.

We then apply Proposition 2.27 (with k = 8 and ℓ = 8) to determine an 8-plane Λ2 ⊆ W2 ∩ Λ1 over an

extension L3/L2 of degree at most 256. Now, C3(τ1,2,3,4; P0, P1, P2)∩Λ2 has type [4 3
1 4
] in Λ2. Consequently,

dim (
C3(τ1,2,3,4; P0, P1, P2) ∩ Λ2) ≥ 8 − 5 ≥ 3

and we can determine a rational point P3 of C3(τ1,2,3,4; P0, P1, P2) \ L(P0, P1, P2) over an extension L4/L3 of
degree at most 324. By design, (P0, P1, P2, P3) is a 3-polar point of τ1,2,3,4.

Case: k = 4. Observe that ρ(4) = 806, hence we work in P804
Kn . By the k = 3 case, we pass to an extension
L1/Kn of resolvent degree at most RD(324) and assume that we have a 3-polar point (P0, P1, P2, P3). Observe

that the fourth polar cone C4(τ1,2,3,4; P0, . . . , P3) has type [4 3 2 1
1 5 15 35

]. Thus, C4(τ1,2,3,4; P0, . . . , P3)1 is

an intersection of 35 hyperplanes and C4(τ1,2,3,4; P0, . . . , P3)1 ∼= P769
L1 . Note that C4(τ1,2,3,4; P0, . . . , P3)2 ∩

C4(τ1,2,3,4; P0, . . . , P3)1 has type [ 2
15

] in C4(τ1,2,3,4; P0, . . . , P3)1 and 29 = 512 is the largest power of 2 less

than 4 · 35 = 972. Consequently, we split C4(τ1,2,3,4; P0, . . . , P3)2 into two intersections of quadrics:

C4(τ1,2,3,4; P0, . . . , P3)2 = W1 ∩ W2,

where W1 has type [2
6

] and W2 has type [2
9
]
. We have that

769 = (109 + 1)(6) + 109,

and so by applying Proposition 2.27 (with k = 109 and ℓ = 6), we can determine a 109-plane Λ1 ⊆ W1 ∩

C4(τ1,2,3,4; P0, . . . , P3)1 over an extension L2/L1 of degree at most 64. Similarly, W2 ∩ Λ1 has type [2
9
] in Λ1

and 109 = (10 + 1)(9) + 10.

By applying Proposition 2.27 (with k = 10 and ℓ = 9), we determine an 8-plane Λ2 ⊆ W2 ∩ Λ1 over an

extension L3/L2 of degree at most 512. It follows that C4(τ1,2,3,4; P0, . . . , P3) ∩ Λ2 has type [
4 3
1 5

] in Λ2.

Consequently, dim (
C4(τ1,2,3,4; P0, . . . , P3) ∩ Λ2) ≥ 10 − 6 ≥ 4

and we can determine a rational point P4 of C4(τ1,2,3,4; P0, . . . , P3)\ L(P0, P1, P2, P3) over an extension L4/L3
of degree at most 972. Indeed, (P0, . . . , P4) is a 4-polar point of τ1,2,3,4.

13

Case: k = 5. Observe that ρ(5) = 1773, hence we work in P1771
Kn . From the k = 4 case, we pass to an
extension L1/Kn of resolvent degree at most RD(972) and assume that we have a 4-polar point (P0, . . . , P4).

The ﬁfth polar cone C5(τ1,2,3,4; P0, . . . , P4) has type [4 3 2 1
1 6 21 56

]. Hence, C5(τ1,2,3,4; P0, . . . , P4)1 is an

intersection of 56 hyperplanes and C5(τ1,2,3,4; P0, . . . , P4)1 ∼= P1715
L1 . Note that C5(τ1,2,3,4; P0, . . . , P4)2 ∩

C5(τ1,2,3,4; P0, . . . , P4)1 has type [ 2
21

] in C5(τ1,2,3,4; P0, . . . , P4)1. Observe that 211 = 2048 is the largest

power of 2 less than 4 · 36 = 2916 and so we split C5(τ1,2,3,4; P0, . . . , P4)2 into two intersections of quadrics:

C5(τ1,2,3,4; P0, . . . , P4)2 = W1 ∩ W2,

where W1 has type [ 2
10

] and W2 has type [ 2
11

]
. Note that

1715 = (155 + 1)(10) + 155,

and, by applying Proposition 2.27 (with k = 155 and ℓ = 10), we can determine a 155-plane Λ1 ⊆ W1 ∩

C5(τ1,2,3,4; P0, . . . , P4)1 over an extension L2/L1 of degree at most 1024. Also, W2 ∩ Λ1 has type [ 2
11

] in Λ1

and 155 = (12 + 1)(11) + 12,

so we can apply Proposition 2.27 (with k = 12 and ℓ = 11) to determine a 10-plane Λ2 ⊆ W2 ∩ Λ1 over an

extension L3/L2 of degree at most 2048. It follows that C5(τ1,2,3,4; P0, . . . , P4) ∩ Λ2 has type [4 3
1 6
] in Λ2.

Consequently, dim (
C5(τ1,2,3,4; P0, . . . , P4) ∩ Λ2) ≥ 12 − 7 ≥ 5,

and we can determine a rational point P5 of C5(τ1,2,3,4; P0, . . . , P4) \ L(P0, . . . , P4) over an extension L4/L3
of degree at most 2916. By construction, (P0, . . . , P5) is a 5-polar point of τ1,2,3,4.

Case: k = 6. Recall that ρ(6) = 8905 and thus we work in P8903
Kn . Using the k = 5 case, we pass to an
extension L1/Kn of resolvent degree at most RD(2916) and assume that we have a 5-polar point (P0, . . . , P5).

The sixth polar cone C6(τ1,2,3,4; P0, . . . , P5) has type [4 3 2 1
1 7 28 84

]. It follows that C6(τ1,2,3,4; P0, . . . , P5)1

is an intersection of 84 hyperplanes, so C6(τ1,2,3,4; P0, . . . , P5)1 ∼= P8819
L1 . Note that C6(τ1,2,3,4; P0, . . . , P5)2 ∩

C6(τ1,2,3,4; P0, . . . , P5)1 has type [ 2
28

] in C6(τ1,2,3,4; P0, . . . , P5)1 and 213 = 8192 is the largest power of 2 less

than 4 · 37 = 8748. Consequently, we split C6(τ1,2,3,4; P0, . . . , P5)2 into three intersections of quadrics:

C6(τ1,2,3,4; P0, . . . , P5)2 = W1 ∩ W2 ∩ W3,

where W1 has type [2
2

] and both W2, W3 have type [ 2
13

]. We have that

8819 = (2939 + 1)(2) + 2939,

and so by applying Proposition 2.27 (with k = 2939 and ℓ = 2), we can determine a 2939-plane Λ1 ⊆
W1 ∩ C6(τ1,2,3,4; P0, . . . , P5)1 over an extension L2/L1 of degree at most 4. Additionally, W2 ∩ Λ1 has type[ 2
13

] inside Λ1 and
 2939 = (209 + 1)(13) + 209.

We then apply Proposition 2.27 (with k = 209 and ℓ = 13) to determine a 209-plane Λ2 ⊆ W2 ∩ Λ1 over

an extension L3/L2 of degree at most 8192. Similarly, W3 ∩ Λ2 has type [ 2
13

] in Λ2 and

209 = (14 + 1)(13) + 14,

14

and thus we apply Proposition 2.27 (with k = 14 and ℓ = 13) to determine a 14-plane Λ3 ⊆ W3 ∩ Λ2 over an

extension L4/L3 of degree at most 8192. Observe that C6(τ1,2,3,4; P0, . . . , P5) ∩ Λ3 has type [4 3
1 7

] inside Λ3

and dim (
C6(τ1,2,3,4; P0, . . . , P5) ∩ Λ3) ≥ 14 − 8 ≥ 6.

As a consequence, we can determine a rational point P6 of C6(τ1,2,3,4; P0, . . . , P5) \ L(P0, . . . , P5) over an
extension L5/L4 of degree at most 8748. It follows that (P0, . . . , P6) is a 6-polar point of τ1,2,3,4.

Case: k = 7. Note that ρ(7) = 34546, so we work in P34544
Kn . By the k = 6 case, we pass to an extension
L1/Kn of resolvent degree at most RD(8748) and assume that we have a 6-polar point (P0, . . . , P6). Observe

that the seventh polar cone C7(τ1,2,3,4; P0, . . . , P6) has type [4 3 2 1
1 8 36 120

] and so C7(τ1,2,3,4; P0, . . . , P6)1

is an intersection of 120 hyperplanes. Thus, C7(τ1,2,3,4; P0, . . . , P6)1 ∼= P34424
L1 . Inside C7(τ1,2,3,4; P0, . . . , P6)1,

C7(τ1,2,3,4; P0, . . . , P6)2 ∩ C7(τ1,2,3,4; P0, . . . , P6)1 has type [ 2
36

]. Note that 214 = 16384 is the largest power of

2 less than 4 · 38 = 26244. Consequently, we split C7(τ1,2,3,4; P0, . . . , P6)2 into three intersections of quadrics:

C7(τ1,2,3,4; P0, . . . , P6)2 = W1 ∩ W2 ∩ W3,

where W1 has type [2
8

] and both W2, W3 have type [ 2
14

]. We have that

34424 = (3824 + 1)(8) + 3824,

and apply Proposition 2.27 (with k = 3824 and ℓ = 8) to determine a 3824-plane Λ1 ⊆ W1∩C7(τ1,2,3,4; P0, . . . , P6)1

over an extension L2/L1 of degree at most 256. Additionally, W2 ∩ Λ1 has type [ 2
14

] inside Λ1 and

3824 = (254 + 1)(14) + 254.

Consequently, we can apply Proposition 2.27 (with k = 254 and ℓ = 14) to determine a 254-plane

Λ2 ⊆ W2 ∩ Λ1 over an extension L3/L2 of degree at most 16384. Observe that W3 ∩ Λ2 has type [ 2
14

] in Λ2

and 254 = (16 + 1)(14) + 16,

and so, by Proposition 2.27 (with k = 16 and ℓ = 14) to determine a 16-plane Λ3 ⊆ W3 ∩Λ2 over an extension

L4/L3 of degree at most 16384. Observe that C7(τ1,2,3,4; P0, . . . , P6) ∩ Λ3 has type [4 3
1 8
] inside Λ3 and

dim (
C7(τ1,2,3,4; P0, . . . , P6) ∩ Λ3) ≥ 16 − 9 ≥ 7.

It follows that we can determine a rational point P7 of C7(τ1,2,3,4; P0, . . . , P6) \ L(P0, . . . , P6) over an
extension L5/L4 of degree at most 26244. Note that (P0, . . . , P7) is a 7-polar point of τ1,2,3,4.

Case: k = 8. Recall that ρ(8) = 77040 and thus we work in P77038
Kn . By the k = 7 case, we pass
to an extension L1/Kn of resolvent degree at most RD(26244) and assume that we have a 7-polar point

(P0, . . . , P7). Observe that the eighth polar cone C8(τ1,2,3,4; P0, . . . , P7) has type [4 3 2 1
1 9 45 165

] and so

C8(τ1,2,3,4; P0, . . . , P7)1 is an intersection of 165 hyperplanes. Thus, C8(τ1,2,3,4; P0, . . . , P7)1 ∼= P76873
L1 and

C8(τ1,2,3,4; P0, . . . , P7)2 ∩ C8(τ1,2,3,4; P0, . . . , P7)1 has type [ 2
45

] inside C8(τ1,2,3,4; P0, . . . , P7)1. We have that

216 = 65536 is the largest power of 2 less than 4 · 39 = 78732. Consequently, we split C8(τ1,2,3,4; P0, . . . , P7)2
into three intersections of quadrics:

C8(τ1,2,3,4; P0, . . . , P7)2 = W1 ∩ W2 ∩ W3,

15

where W1 has type [ 2
13

] and both W2, W3 have type [ 2
16

]
. Observe that

76873 = (5490 + 1)(13) + 5490.

Thus, we can apply Proposition 2.27 (with k = 5490 and ℓ = 13) to determine a 5490-plane Λ1 ⊆ W1 ∩
C8(τ1,2,3,4; P0, . . . , P7)1 over an extension L2/L1 of degree at most 8192. We also have that W2 ∩ Λ1 has type[ 2
16

] inside Λ1 and
 5490 = (322 + 1)(16) + 322.

As a result, we apply Proposition 2.27 (with k = 322 and ℓ = 16) to determine a 322-plane Λ2 ⊆ W2 ∩ Λ1

over an extension L3/L2 of degree at most 65536. Note that W3 ∩ Λ2 has type [ 2
16

] in Λ2 and

322 = (18 + 1)(16) + 18,

and so Proposition 2.27 (with k = 18 and ℓ = 16) allows us to determine an 18-plane Λ3 ⊆ W3 ∩ Λ2 over an

extension L4/L3 of degree at most 65536. Observe that C8(τ1,2,3,4; P0, . . . , P7) ∩ Λ3 has type [4 3
1 9

] inside

Λ3 and dim (
C8(τ1,2,3,4; P0, . . . , P7) ∩ Λ3) ≥ 18 − 10 ≥ 8.

Consequently, we can determine a rational point P8 of C8(τ1,2,3,4; P0, . . . , P7) \ L(P0, . . . , P7) over an
extension L5/L4 of degree at most 78732. By design, (P0, . . . , P8) is an 8-polar point of τ1,2,3,4.

Case: k = 9. Recall that ρ(9) = 612581 and thus we work in P612579
Kn . By the k = 8 case, we pass to an exten-
sion L1/Kn of resolvent degree at most RD(78732) and assume that we have a 8-polar point (P0, . . . , P8). Note

that the ninth polar cone C9(τ1,2,3,4; P0, . . . , P8) has type [4 3 2 1
1 10 55 220

]. So, C9(τ1,2,3,4; P0, . . . , P8))1 is an

intersection of 220 hyperplanes and C9(τ1,2,3,4; P0, . . . , P8)1 ∼= P612359
L1 . Observe that C9(τ1,2,3,4; P0, . . . , P8)2 ∩

C9(τ1,2,3,4; P0, . . . , P8)1 has type [ 2
55

] inside C9(τ1,2,3,4; P0, . . . , P8)1 and 217 = 131072 is the largest power

of 2 less than 4 · 310 = 236196. Correspondingly, we split C9(τ1,2,3,4; P0, . . . , P8)2 into four intersections of
quadrics: C9(τ1,2,3,4; P0, . . . , P8)2 = W1 ∩ W2 ∩ W3 ∩ W4,

where W1 has type [2
4

] and all of W2, W3, W4 have type [ 2
17

]. Note that

612359 = (122471 + 1)(4) + 122471,

and so, by Proposition 2.27 (with k = 122471 and ℓ = 4), we can determine a 122471-plane Λ1 ⊆ W1 ∩

C9(τ1,2,3,4; P0, . . . , P8)1 over an extension L2/L1 of degree at most 16. Additionally, W2 ∩ Λ1 has type [ 2
17

]

inside Λ1 and 122471 = (6803 + 1)(17) + 6805.

As a result, we apply Proposition 2.27 (with k = 6805 and ℓ = 17) to determine a 6805-plane Λ2 ⊆ W2 ∩Λ1

over an extension L3/L2 of degree at most 131072. Note that W3 ∩ Λ2 has type [ 2
17

] in Λ2 and

6803 = (377 + 1)(17) + 377.

and so Proposition 2.27 (with k = 18 and ℓ = 16) allows us to determine an 18-plane Λ3 ⊆ W3 ∩ Λ2 over an

extension L4/L3 of degree at most 65536. Also, W4 ∩ Λ3 has type [ 2
17

] in Λ3 and

377 = (20 + 1)(17) + 20.

16

From Proposition 2.27 (with k = 18 and ℓ = 16), we can determine a 20-plane Λ4 ⊆ W4 ∩ Λ3 over an

extension L5/L4 of degree at most 131072. We have that C9(τ1,2,3,4; P0, . . . , P8) ∩ Λ4 has type [
4 3
1 10

] inside

Λ4 and dim (
C9(τ1,2,3,4; P0, . . . , P8) ∩ Λ4) ≥ 20 − 11 ≥ 9.

As a result, we can determine a rational point P9 of C9(τ1,2,3,4; P0, . . . , P8)\L(P0, . . . , P8) over an extension
L6/L5 of degree at most 236196 and it follows that (P0, . . . , P9) is a 9-polar point of τ1,2,3,4.

3.3 New Bounds from Moduli Spaces

In [Wol2021], Wolfson uses moduli space methods to determine k-planes on intersections of hypersurfaces
over extensions of scalars of bounded resolvent degree. Wolfson then applies these methods to obtain upper
bounds on RD(n). We will use a similar construction (Theorem 3.24) and thus begin by giving an example
of Wolfson’s process in Example 3.17. To do so, we must introduce additional language and notation.

Deﬁnition 3.11. (Parameter and Moduli Spaces of Hypersurfaces)
Fix d ≥ 2. The parameter space of degree d hypersurfaces in Pr
C is

H(d; r) ∼= P(
r+d
d )−1
C

However, there is a natural action of PGL(C, r+1) on Pr
C which identiﬁes hypersurfaces which are projectively
equivalent. The parameter space of semi-stable, degree d hypersurfaces in Pr
C is the largest proper
Zariski open U ⊆ H(d; r) which is PGL(C, r + 1)-invariant; we denote it by S(d; r). Consequently, the coarse
moduli space of semi-stable, degree d hypersurfaces in Pr
C is thus

M(d; r) := S(d; r)/PGL(C, r + 1).

The semi-stable locus S(d; r) is a dense Zariski open of H(d; r) which is PGL(C, r + 1)-invariant. It
contains another dense, PGL(C, r + 1)-invariant Zariski open S◦(d; r) ⊆ S(d; r) which parametrizes the
smooth hypersurfaces. The coarse moduli space of smooth, degree d hypersurfaces in Pr
C is

M◦(d; r) := S◦(d; r)/ PGL(C, r + 1).

Each of the above parameter and moduli spaces classiﬁes certain objects. We will additionally need to
refer to the spaces classifying these objects with an associated choice of k-plane.

Deﬁnition 3.12. (Parameter and Moduli Spaces of Hypersurfaces with k-Planes)
Continuing with the notation of Deﬁnition 3.11 and recalling that Gr(k, r) is the variety of k-planes in Pr
C,
we denote the parameter space of degree d hypersurfaces with choice of k-plane in Pr
C by H(d; r, k);
it is the incidence variety
 H(d; r, k) = {(V, L) | L ⊆ V } ⊆ H(d; r) × Gr(k, r).

Similarly, we write S(d; r, k), M(d; r, k), and M◦(d; r, k) for the analogous spaces which additionally classify
a choice of k-plane. They similarly arise as incidence varieties or as quotients of incidence varieties by
PGL(C, r + 1).

We now expand these deﬁnitions from classifying hypersurfaces to intersections of hypersurfaces of type
(2, . . . , d).

Deﬁnition 3.13. (Parameter and Moduli Spaces of Intersections of Hypersurfaces)
The parameter space of intersections of hypersurfaces of type (2, . . . , d) in Pr
C is

H(2, . . . , d; r) = H(2; r) × · · · × H(d; r).

17

The natural action of PGL(C, r + 1) action on Pr
C induces a diagonal action on H(2, . . . , d; r) and the
parameter space of semi-stable intersections of hypersurfaces of type (2, . . . , d) in Pr
C is the largest
proper Zariski open U ⊆ H(2, . . . , d; r) which is PGL(C, r + 1)-invariant; it is denoted by S(2, . . . , d; r).
The moduli space of semi-stable intersections of hypersurfaces of type (2, . . . , d) in Pr
C is

M(2, . . . , d; r) = S(2, . . . , d; r)/ PGL(C, r + 1).

In analogy with Deﬁnition 3.12, we write H(2, . . . , d; r, k), S(2, . . . , d; r, k), and M(2, . . . , d; r, k) for the
respective spaces which additionally classify a choice of k-plane; they analogously arise as incidence varieties
or as quotients of incidence varieties by PGL(C, r + 1), as well.

Remark 3.14. (Parameter and Moduli Spaces as Schemes)
For the interested reader, we note that these spaces can be constructed as schemes via classical invariant
theory, beginning with
 H(d; r) = Proj (S∗ (C[x0, . . . , xr]∨
(d))) ,

M(d; r) = Proj (
S∗ (C[x0, . . . , xr]∨
(d))GL(C,r+1)) .

The remaining spaces arise analogously from the same constructions as in the variety case.

We will use the dimension of these parameter and moduli spaces, so we recall the dimensions in the case
of hypersurfaces and give the dimensions in the case of intersections of hypersurfaces of type (2, . . . , d). In
the proof of Proposition 2.26, we observed the combinatorial identity

d∑

i=0
 (
r + i
i
 ) = (
r + d + 1
d
 ).

In Remark 3.15 and Deﬁnition 3.21, we will use the slight variation

d∑

i=2
 (
r + i
i
 ) = (r + d + 1
d
 ) − (r + 2). (5)

Remark 3.15. (Dimension of Parameter and Moduli Spaces)
For ﬁxed d, r ≥ 1, we have
 dim (S(d; r)) = dim (H(d; r)) = (
r + d
d
 ) − 1.

When (
r+d
d ) − (r + 1)
2 < 0, M(d; r) is empty. When (
r+d
d ) − (r + 1)
2 ≥ 0, we have

dim (M◦(d; r)) = dim (M(d; r)) = (
r + d
d
 ) − (r + 1)
2.

Similarly, for d, r for which the following spaces are non-empty, we have

dim (S (2, . . . , d; r)) = dim (H (2, . . . , d; r)) =
 ( d∑

i=2
 (
r + i
i
 ))
 − (d − 1),

dim (M (2, . . . , d; r)) =
 ( d∑

i=2
 (
r + i
i
 ))
 − (r + 1)
2 − (d − 2).

From equation (5), we re-write these quantities as

dim (S (2, . . . , d; r)) = dim (H (2, . . . , d; r)) = (
r + d + 1
d
 ) − (r + d + 1),

dim (M (2, . . . , d; r)) = (
r + d + 1
d
 ) − (r + 1)
2 − (r + d).

18

We now examine how Wolfson’s algorithm determines k-planes on hypersurfaces. A theorem of Waldron
(Theorem 3.16) guarantees the existence of a k-plane on a degree d hypersurface once the ambient dimension
r is above a given threshold:

Theorem 3.16. (Theorem 1.6 of [Wal2008])
Fix d ≥ 3. When r and k are such that

(k + 1)(r − k) − (
k + d
d
 ) ≥ 0,

then the natural maps
 H(d; r, k) ! H(d; r),

M◦(d; r, k) ! M◦(d; r),

are surjective.4

Deﬁnition 2.4 of [Wol2021] shows that the extended Tschirnhaus complete intersections are deﬁned over
Z. Thus, for suitable d, r, k, Waldron’s theorem allows us to determine a k-plane on τd over an extension
L/Kn with RD(L/Kn) ≤ RD (H(d; r, k) ! H(d; r)) ≤ dim (H(d; r)) .

Moreover, Theorem 2.12 of [Wol2021] shows that τ1,2,3 (along with certain other extended Tschirnhaus
complete intersections) are generically smooth. It follows that for suitable r, k, Waldron’s theorem allows us
to determine a k-plane on τ3 over an extension L′/Kn with

RD(L/Kn) ≤ RD (M◦(3; r, k) ! M◦(3; r)) ≤ dim (M◦(3; r)) .

Note that for a generically ﬁnite, dominant, rational map of C-varieties Y 99K X, the upper bound

RD(Y 99K X) ≤ dim(X), (6)

follows directly from Deﬁnition 2.14; it is also included in Lemma 2.5 of [FW2019].

Example 3.17. (Wolfson’s Method)
For n ≥ 1559, we can determine an 8-plane on τ1,2,3,4 over an extension L/Kn with RD(L/Kn) ≤ 78485029.

Proof. First, τ1 is a hyperplane and so τ1 ∼= P1557
Kn . Next, τ2 is a quadric hypersurface in τ1 and thus it
is known classically that there is a 778-plane Λ2 ⊆ τ1,2 over an iterated quadratic extension L1/Kn (see
[Wol2021] for details). τ1,2,3 ∩ Λ2 is a cubic hypersurface in Λ2 and

(63 + 1)(778 − 63) − (
63 + 3
3
 ) = 0,

hence we can determine a 63-plane Λ3 ⊆ τ1,2,3 ∩ Λ2 over an extension L2/L1 with

RD(L2/L1) ≤ RD (M◦(3; 778, 63) ! M◦(3; 778)) ≤ dim (M◦(3; 778)) = 78485029.

Finally, τ1,2,3,4 ∩ Λ3 is a quartic hypersurface in Λ3 and

(8 + 1)(63 − 8) − (
8 + 4
4
 ) = 0,

hence we can determine an 8-plane Λ4 ⊆ τ1,2,3,4 ∩ Λ3 over an extension L3/L2 with

RD(L3/L2) ≤ RD (H(4; 63, 8) ! H(4; 63)) ≤ dim (H(4; 63)) = 766479.

4This is not the entirety of Waldron’s result; see Theorem 1.6 of [Wal2008] for more details.

19

We next provide an example which highlights the current limitations of using iterated polar cones for
determining additional upper bounds on RD(n).

Example 3.18. (Wolfson Method for a 9-Plane on τ1,2,3,4,5)
We can determine a 9-plane on τ1,2,3,4,5 over an extension L/Kn with

RD(L/Kn) ≤ 3298353885918738132194252727911 ( ≈ 3 · 1030 ) ,

as long as
 r ≥ 54097786526 ( ≈ 5 · 1010) .

The core construction is the same as Example 3.17. In Wolfson’s notation, observe that 54097786526 =
ψ(5, 9)4 + 1 and
 dim (M◦(3; ψ(5, 9)3)) = 3298353885918738132194252727911 ( ≈ 3 · 1030 ) .

See the proof of Theorem 5.6 of [Wol2021] for details.

Remark 3.19. (Iterated Polar Cone Comparison)

Observe that a 9th polar cone C9(τ1,2,3,4,5; P0, . . . , P8) of τ1,2,3,4,5 has type [5 4 3 2 1
1 10 55 220 715

]. Thus,

even for n large enough so that we may determine a suitable 66-plane Λ on C9(τ1,2,3,4,5; P0, . . . , P8)1 ∩
C9(τ1,2,3,4,5; P0, . . . , P8)2 (the intersection of the 220 quadrics and 715 hyperplanes deﬁning C9(τ1,2,3,4,5; P0, . . . , P8)),
it still follows that

deg (
C9(τ1,2,3,4,5, P8) ∩ Λ) = 5 · 410 · 355,

= 914616279415496004448658427740160 ( ≈ 9 · 1032 ) ,

> 3298353885918738132194252727911 ( ≈ 3 · 1030 ) ,

= dim (M◦(3; ψ(5, 9)3)) .

Indeed, the degree of the analogous intersection grows exponentially in k whereas the required resolvent
degree for Wolfson’s method grows polynomially in k. Similar issues arise for k-planes on intersections of
hypersurfaces of type (1,2,3,4) for k ≥ 33.

In [DM1998], Debarre and Manivel give an explicit combinatorial condition for an intersection of hyper-
surfaces in Pr
C to contain a k-plane:

Theorem 3.20. (Theorem 2.1 of [DM1998])

Let V ⊆ Pr
C be an intersection of hypersurfaces of type [ d d − 1 · · · 2 1
ℓd ℓd−1 · · · ℓ2 ℓ1
] which is not a quadric

hypersurface. When r and k are such that

(k + 1)(r − k) −
 d∑

i=1 ℓi
(
k + i
i
 ) ≥ 0,

then the natural maps
 H (2, . . . , d; r, k) ! H (2, . . . , d; r) ,

M (2, . . . , d; r, k) ! M (2, . . . , d; r) ,

are surjective. 5

5This is not the entirety of Debarre and Manivel’s result; see Theorem 2.1 of [DM1998] for more details.

20

We will use this result to deal with k-planes on intersections of hypersurfaces directly (instead of using a
recursive process on the set of deﬁning hypersurfaces) to obtain new thresholds for upper bounds on RD(n)
for n ≥ 348, 489, 068, 134 in Theorem 3.24.
Similarly to Wolfson, we can use the upper bound

RD (M(2, . . . , d; r, k) ! M(2, . . . , d; r)) ≤ dim (M(2, . . . , d; r)) ,

once we establish that the Tschirnhaus complete intersections τ1,...,m are semi-stable in Lemma 3.22 and
Proposition 3.23.

Deﬁnition 3.21. (Notation for Lemma 3.22 )
To succinctly state Lemma 3.22 and its applications, we deﬁne a new set function

ϑ : Z≥3 × Z≥1 ! Z≥1,

where ϑ(d, k) is the smallest positive integer r such that

(k + 1)(r − k) −
 d∑

i=2
 (k + i
i
 ) ≥ 0.

Using the combinatorial identity in equation (5), we can equivalently write

ϑ(d, k) = k + ⌈ 1
k + 1
 ((
k + d + 1
d
 ) − (k + 2)
)⌉ .

Lemma 3.22. (k-Planes on an Intersection of Hypersurfaces of Type (2, . . . , d))
Let d ≥ 3, and V ∈ S(2, . . . , d; r)(K) for some C-ﬁeld K. For any k ≥ 1, if r ≥ ϑ(d, k), then we can determine
a k-plane on V over an extension L/K with

RD(L/K) ≤ dim (M(2, . . . , d; ϑ(d, k)) .

Proof. First, observe that it suﬃces to prove the case where r = ϑ(d, k) by restriction. Theorem 3.20 then
yields that V contains a k-plane. We identify V with A0
K ! M(2, . . . , d; ϑ(d, k)) and note that the resolvent
degree of determining a k-plane is exactly the resolvent degree of the map

πK : A0
K ×M(2,...,d;ϑ(d,k)) M(2, . . . , d; ϑ(d, k), k) ! A0
K

determined by the pullback square

A0
K ×M(2,...,d;ϑ(d,k)) M(2, . . . , d; ϑ(d, k), k) M(2, . . . , d; ϑ(d, k), k)

A0
K M(2, . . . , d; ϑ(d, k)).

πK
 πM

However, Lemma 2.5 of [FW2019] yields that

RD (πK) ≤ RD (M(2, . . . , d; ϑ(d, k), k) ! M(2, . . . , d; ϑ(d, k))) ≤ dim (M(2, . . . , d; ϑ(d, k))) .

Proposition 3.23. (Semi-Stability of Tschirnhaus Complete Intersections)
For each d ≥ 3 and n ≥ d + 2, τ1,...,d ∈ S(2, . . . , d; n − 2)(Kn).

Proof. First, note that τ1 ⊆ Pn−1
Kn is a hyperplane, so we can consider τ1,...,d ⊆ τ1 ∼= Pn−2
Kn , e.g. as a Kn-point
of S(2, . . . , d; n − 2).
From the deﬁnition of S(2, . . . , d; n − 2), it suﬃces to show that there is some PGL(Kn, n − 1)-invariant
polynomial in Kn[x0, . . . , xn−1] which does not vanish at τ1,...,d. Theorem 2.12 of [Wol2021] yields that
τ1,2,3 is generically smooth, hence semi-stable. In particular, there is a PGL(Kn, n − 1)-invariant polynomial
f (x0, . . . , xn−1) ∈ Kn[x0, . . . , xn−1] which does not vanish at τ1,2,3 ∈ H(2, 3; n−2)(Kn). When pulled back to
H(2, . . . , d; n − 2)(Kn) via the standard projection map, f (x0, . . . , xn−1) does not vanish at τ1,...,d as well.

21

Theorem 3.24. (Determining a Point on τ1,...,d+k)
Fix k, d ≥ 1. For n ≥ ϑ(d, k) + 3, we can determine a point of τ ◦
1,...,d+k ⊆ T n over an extension L/Kn with

RD(L/Kn) ≤ max {dim (M(2, . . . , d; ϑ(d, k))) , (d + k)!
d!
 } .

Proof. By restriction, it suﬃces to prove the case where n = ϑ(d, k) + 3. As such, we work in Pϑ(d,k)+2
Kn . We

then pass to a hypersurface H which does not contain [1 : 0 : · · · : 0] and τ1 ∩H ∼= Pϑ(d,k)
Kn in this hypersurface.
Hence, Lemma 3.22 and Proposition 3.23 yield that we can determine a k-plane Λ ⊆ τ1,...,d over an extension
L1/Kn with
 RD(L1/Kn) ≤ dim (M(2, . . . , d; ϑ(d, k))) .

Thus, deg (τ1,...,d+k ∩ Λ) = (d+k)!
d! and we can determine a point Q of τ1,...,d+k ∩Λ ⊆ τ ◦
1,...,d+k over an extension

of degree at most (d+k)!
d! .

Remark 3.25. (Wolfson’s Function F )
In Deﬁnition 5.4 and Theorem 5.6 of [Wol2021], Wolfson introduces a monotone increasing function F (r) such
that RD(n) ≤ n − r for n ≥ F (r); we will deﬁne this function explicitly in Section 4. To remain consistent
with the notation in this paper, we write F as a function of m.

Wolfson shows shows that lim
m!∞
 B(m)
F (m) = ∞, where B(m) = (m − 1)! + 1 was the previous best bounding

function, established in [Bra1975]. We construct a similar function G(m) and prove that G similarly improves
on F (Theorem 4.1).

Deﬁnition 3.26. (Deﬁning the Function G(m))
We deﬁne ϕ : Z≥15 × Z≥1 ! Z≥1 by

ϕ(d, k) = max { (d + k)!
d! , dim (M(2, . . . , d; ϑ(d, k)))} .

Next, we deﬁne G : Z≥1 ! Z≥1 for 2 ≤ m ≤ 14 by

m 1 2 3 4 5 6 7 8 9 10
G(m) 2 3 4 5 9 21 109 325 1681 15121

m 11 12 13 14
G(m) 151,201 1,663,201 19,958,401 259,459,201

and for m ≥ 15 by
 G(m) = 1 + min {ϕ(d, m − d − 1) | 4 ≤ d ≤ m − 1} .

Theorem 3.27. (Upper Bounds on RD(n))
For each m ≥ 1 and all n ≥ G(m), RD(n) ≤ n − m.

Proof. (Proof of Theorem 3.27)
The claim for 1 ≤ m ≤ 5 is classical and is covered in [Wol2021]. The case m = 6 is Theorem 3.7 and the
cases of 7 ≤ m ≤ 14 are Theorem 3.10.
Now, ﬁx m ≥ 15. For each 4 ≤ d ≤ m−1, Theorem 3.24 yields that we can determine a point of τ ◦
1,...,m−1 ⊆
T n over an extension of scalars L/Kn with RD(L/Kn) ≤ ϕ(d, m − d − 1) when n ≥ ϑ(d, m − d − 1) + 3. Note
that
 ϑ(d, m − d − 1) + 3 < (
ϑ(d, m − d − 1) + d + 1
d
 ) − (ϑ(d, m − d − 1) + 1)
2 − (ϑ(d, m − d − 1) + d)

= dim (M(2, . . . , d; ϑ(d, m − d − 1)))

≤ ϕ(m, m − d − 1).

It suﬃces to minimize over all such d and so the deﬁnition of G(m) and Remark 3.5 yield the theorem.

In Section 4, we pin down how G(m) improves on F (m). First, we use G(m) to establish an upper bound
on RD(n) using elementary functions `a la Brauer.
 22

3.4 Upper Bounds on the Bounding Function G(m)

While G(m) is simpler than F (m), its deﬁnition does not immediately yield a description in terms of ele-
mentary functions. We state such a description now and use the remainder of the subsection to obtain this
approximation.

Theorem 3.28. (Upper Bound on the Growth Rate of RD(n))

For every positive integer d ≥ 4, G(2d
2 + 7d + 6) ≤ (2d2+7d+5)!
d! . Hence, for n ≥ (2d2+7d+5)!
d! , it follows that

RD(n) ≤ n − 2d
2 − 7d − 6.

To prove Theorem 3.28, we establish a simple criterion for m, in terms of d, so that we can conclude that
G(m) < (m−1)!
d! when that criterion is met.
Recall that ϑ(d, k) is deﬁned such that an intersection of hypersurfaces of type (1, . . . , d) in Pr contains
a k-plane when r ≥ ϑ(d, k). We begin by approximating ϑ(d, m − d − 1) above.

Lemma 3.29. (Upper Bound on ϑ)
Fix m > d ≥ 4. Then
 ϑ(d, m − d − 1) ≤ m − d − 2 + (m
d
 ).

Proof. We ﬁrst recall Deﬁnition 3.21:

ϑ(d, k) = k + ⌈ 1
k + 1
 ((
k + d + 1
d
 ) − (k + 2)
)⌉ .

By using the identiﬁcation k = m − d − 1, we observe that

ϑ(d, m − d − 1) = (m − d − 1) + ⌈ 1
(m − d − 1) + 1
 ((
(m − d − 1) + d + 1
d
 ) − ((m − d − 1) + 2)
)⌉ ,

= (m − d − 1) + ⌈ 1
m − d
 ((
m
d
 ) − (m − d + 1)
)⌉ ,

≤ m − d − 2 + (
m
d
 )
.

Corollary 3.30. (Upper Bound on Parameter Space Dimension)
Fix m > d ≥ 4. Then,

dim (H(2, . . . , d; ϑ(d, m − d − 1))) ≤ (
m − 1 + (
m
d )

d
 ) − (
m − 1 + (m
d
 )) .

Proof. Remark 3.15 established that

dim (H(2, . . . , d; ϑ(d, m − d − 1))) ≤ (
ϑ(d, m − d − 1) + d + 1
d
 ) − (ϑ(d, m − d − 1) + d + 1),

which is non-decreasing in ϑ(d, m − d − 1). Thus, Lemma 3.29 yields

dim (H(2, . . . , d; ϑ(d, m − d − 1))) ≤ (
m − 1 + (
m
d )

d
 ) − (
m − 1 + (m
d
 )) .

We will now introduce a constant Cd and give a bound on log ( Cd
d+1 ), both of which will be useful in the
proof of Lemma 3.33. We also remind the reader that every use of log in this paper refers to the base e
logarithm.
 23

Deﬁnition 3.31. (Constant for the Proof of Lemma 3.33 )
For each d ≥ 4, we set
 Cd := max {(
d + 1
i
 ) | 0 ≤ i ≤ d + 1} .

Lemma 3.32. (Bound on log(Cd))
For each d ≥ 1, it follows that
 log ( Cd
d + 1
 ) ≤ d + 3
2 .

We will frequently use Stirling’s approximations for factorials, including in the proof of Lemma 3.32, and
thus state the version we use explicitly (a stronger version of which can be found in [Rob1955]):

Let a be an positive integer. Then, √2πaa+ 1
2 e−a ≤ a! ≤ aa+ 1
2 e1−a. (7)

Proof. (Proof of Lemma 3.32)
Our proof depends on the parity of d + 1; we begin with the case where d + 1 = 2ℓ is even. Then, Cd =(
2ℓ
ℓ ) = (2ℓ)!
(ℓ!)2 and Stirling’s approximation yields

Cd ≤ (2ℓ)
2ℓ+ 1
2 e1−2ℓ
(√2πℓℓ+ 1
2 e−ℓ)2 = 2d+ 1
2 e
π√
ℓ .

Consequently,
 log ( Cd
d + 1
 ) ≤ log
 ( 2d− 1
2 e
π√
ℓ(d + 1)
 )
 ≤ log ( e
π(d + 1)
√
ℓ
 ) + log (
ed+ 1
2 ) ≤ d + 1
2 .

When d + 1 = 2ℓ + 1 is odd, we observe

Cd = (
2ℓ + 1
ℓ
 ) ≤ (
2ℓ + 2
ℓ + 1
 ) ≤ 2d+ 3
2 e
π√ℓ + 1 ,

and thus
 log ( Cd
d + 1
 ) ≤ log
 ( 2d+ 3
2 e
π√ℓ + 1
 )
 ≤ d + 3
2 .

Recall that for each 1 ≤ d ≤ m − 1 and when n is large enough, we can determine an (m − d − 1)-plane
Λ ⊆ τ ◦
1,...,d over an extension L1/Kn with

RD(L1/Kn) ≤ dim (M(2, . . . , d; ϑ(d, m − d − 1))) .

In such a case, we can determine a point of τ1,...,m−1 ∩ Λ over an extension L2/L1 of degree (m−1)!
d! . Hence,
we set
 ϕ(d, m − d − 1) = max { (m − 1)!
d! , dim (M(2, . . . , d; ϑ(d, m − d − 1))) + m}

in Deﬁnition 3.26. We next give a condition relating ϕ(d, m − d − 1) and ϕ(d + 1, m − d − 2).

24

Lemma 3.33. (The ϕ Condition)
Fix d ≥ 4. For all m ≥ 2d
2 + 7d + 6, it follows that

ϕ(d + 1, m − d − 2) < ϕ(d, m − d − 1). (8)

Proof. For any such d and m, it is always true that

(m − 1)!
(d + 1)! < (m − 1)!
d! .

As a result, to conclude (8), we need only show that

(m − 1)!
d! > (
m − 1 + ( m
d+1
)

d + 1
 )
, (9)

since (
m − 1 + ( m
d+1
)

d + 1
 ) > dim (H(2, . . . , d; ϑ(d, m − d − 1))) > dim (M(2, . . . , d; ϑ(d, m − d − 1))) .

Observe that

(
m − 1 + ( m
d+1
)

d + 1
 ) =
 (m − 1 + ( m
d+1
))
!

(d + 1)! (m − d − 2 + ( m
d+1
)) = 1
(d + 1)!
 d+1∏

i=1
 (
m − i + ( m
d + 1

)) . (10)

Next, we approximate ( m
d+1
)
:

( m
d + 1
) = 1
(d + 1)! · m!
(m − d − 1)! = 1
(d + 1)!
 d+1∏

j=0(m − j) ≤ 1
(d + 1)! md+2 ≤ md+2. (11)

By substituting the inequality (11) into equation (10) and using that m − i ≤ m, we obtain the approxi-
mation (
m − 1 + ( m
d+1
)

d + 1
 ) ≤ 1
(d + 1)!
 d+1∏

i=1
 (
m + md+2) ,

which, after substituting into inequality (9) and multiplying both sides by d!, yields the suﬃcient condition

(m − 1)! > 1
d + 1
 d+1∏

i=1
 (
m + md+2) . (12)

Notice that main term of the right side of inequality (12) is of the form d+1∏

i=1(a + b) = (a + b)
d+1, hence

applying the binomial theorem yields

d+1∏

i=1
 (
m + md+2) =
 d+1∑

i=0
 (
d + 1
i
 ) (
md+2)i md+1−i,

=
 d+1∑

i=0
 (
d + 1
i
 )mdi+2i(m − 1)
d+1−i,

=
 d+1∑

i=0
 (
d + 1
i
 )m(d+1)i+d+1,

= md+1 d+1∑

i=0
 (
d + 1
i
 ) (
md+1)i .

25

However, for any positive integer a and x ≥ a it follows from induction a+1∑

i=0 x
i ≤ 2x
a+1. Applying this to

(m − 1) d+1∑

i=0
 (
d+1
i ) (
(m − 1)
d)i and recalling Cd = max {(
d+1
i ) | 0 ≤ i ≤ d + 1} yields

md+1 d+1∑

i=0
 (
d + 1
i
 ) (
md+1)i ≤ md+1Cd (
2 (
md+1)d+1) . (13)

Substituting inequality (13) into inequality (12) and simplifying, we obtain the condition

(m − 1)! > 2
d + 1 Cdmd2+3d+2.

Next, we apply Stirling’s approximation and re-arrange terms to arrive at the condition

(m − 1)
m− 1
2
em−1 > 2Cd√2π(d + 1) md2+3d+2. (14)

Observe that aa−1 < (a − 1)
a− 1
2 for positive integers a ≥ 8. By requiring m > 8, we need only consider when

mm−1

em−1 > 2Cd
√
2π(d + 1) md2+3d+2. (15)

Multiplying both sides of inequality (15) by ed2+3d+2, dividing both sides by md2+3d+2, and simplifying, we
arrive at the condition ( m
e
 )m−d2−3d−3 > 2Cded2+3d+2
√
2π(d + 1) . (16)

We take log of both sides of inequality (16), which yields

(
m − d
2 − 3d − 3) log ( m
e
 ) > log
 ( 2Cded2+3d+3
√
2π(d + 1)
 )
 . (17)

Requiring m > e2, it suﬃces to consider

m − d
2 − 3d − 3 > log ( 2
√
2π
 ) + log ( Cd
d + 1
 ) + (
d
2 + 3d + 2) . (18)

We note log ( 2√
2π
 ) < 0 and apply the bound on log ( Cd
d+1 ) ≤ d + 3
2 from Lemma 3.32 to obtain the suﬃcient
condition
 m − d
2 − 3d − 3 > (
d + 3
2
 ) + (
d
2 + 3d + 2) ,

which re-arranges to yield our initial supposition

m ≥ 2d
2 + 7d + 6. (19)

Finally, note that for all d ≥ 4, 2d
2 + 7d + 6 > e2 > 8, hence the requirements m ≥ 8, m > e2 used in the
proof are rendered superﬂuous.

Corollary 3.34. (Upper Bound on the Growth Rate of G)
For any d ≥ 4 and m ≥ 2d
2 + 7d + 6, it follows that

G(m) < (m − 1)!
d! .

26

Proof. Recall Deﬁnition 3.26; in particular, for m ≥ 15,

G(m) = min {ϕ(d, m − d − 1) | 15 ≤ d ≤ m − d − 1} + 1.

Consequently, for any d ≥ 4 and m ≥ 2d
2 + 3d, we have

G(m) ≤ ϕ(d + 1, m − d − 2) + 1 < (m − 1)!
d!

from Lemma 3.33.

We now prove Theorem 3.28.

Proof. (Proof of Theorem 3.28)
Fix d ≥ 4. From Corollary 3.34, we have that

G(m) ≤ (2d
2 + 7d + 5)!
d!

for m ≥ 2d
2 + 7d + 6. From Theorem 3.27, it follows that

RD(n) ≤ n − 2d
2 − 7d − 6

for n ≥ (2d2+7d+5)!
d! .

4 Comparison with Prior Bounds

We now give a precise sense of how the bounds from G(m) improve upon the bounds of F (m).

Theorem 4.1. (Comparison With F (m))
Let F be the function deﬁned in Deﬁnition 4.3 (which is originally Deﬁnition 5.4 of [Wol2021]).

1. For every m ≥ 1, G(m) ≤ F (m) with equality if and only if m = 1, 2, 3, 4, 5, 15, or 16.

2. G(m) provides asymptotic improvements on F (m), in the sense that

lim
m!∞ F (m)
G(m) = ∞.

Remark 4.2. Despite Theorem 4.1, G(m) does not yield a strictly better bound on RD(n) for all n. As an
example,
 G(17) = 348, 489, 068, 134, F (17) = 871, 782, 912, 001,

G(18) = 2, 964, 061, 900, 801 F (18) = 14, 820, 309, 504, 001,

so F (17)
G(17) ∼ 2.502 and F (18)
G(18) ∼ 5.000. However, for any integer n between F (17) and G(18), F and G yield
the same upper bound; namely, RD(n) ≤ n − 17.

The remainder of the section is spent proving Theorem 4.1. We will now deﬁne Wolfson’s function F (m).
Our presentation will vary slightly from Wolfson’s and we refer the reader to Section 5 of [Wol2021] for details
of the construction.

Deﬁnition 4.3. (Wolfson’s Functions)
Given (d, k) ∈ Z≥3 × Z≥1, set ψ(d, k)0 = k. For 0 ≤ i < d − 2, set

ψ(d, k)i+1 := ψ(d, k)i + ⌈ 1
ψ(d, k)i + 1 · (
ψ(d, k)i + d − i
d − i
 )⌉ ,

along with ψ(d, k)d−1 := 2ψ(d, k)d−2 + 1.
 27

Additionally, deﬁne

Φ(d, k) := max { (d + k)!
d! , dim (M (3; ψ(d, k)d−2)) + d + k + 1} .

Finally, for m ≤ 3, set F (m) := m + 1 and for m ≥ 4, set

F (m) := 2 ⌊ 1
2
 ( min
1≤d≤m−2 Φ(d, m − d − 1)
)⌋ + 1.

Remark 4.4. (Outline for Section 4)
Our goal is to establish a criterion for m, in terms of d, so that we can conclude F (m) > (m−1)!
d! when this
criterion is met. We do this by examining when

Φ(d, m − d − 1) < Φ(d + 1, m − d − 2).

We ﬁrst show that for any m ≥ d + 3,

dim (M (3; ψ(d, m − d − 1)d−2)) ≤ dim (M (3; ψ(d + 1, m − d − 2)d−1)) , (20)

which will then leave us to consider when

(m − 1)!
d! < dim (M (3; ψ(d + 1, m − d − 2)d−1)) . (21)

We begin by introducing auxiliary functions which will be useful for proving inequality (20) holds for
m ≥ d + 3.

Deﬁnition 4.5. (Auxiliary Functions Ψ(d; i))
For any d ≥ 2, any d − 2 ≥ i ≥ 1 and x ∈ Z≥1, we set

Ψ(d; i)(x) = x + ⌊ 1
x + 1 · (
x + d − i
d − i
 )⌋ .

Remark 4.6. (Key Properties of Ψ(d; i))
The functions Ψ(d, i) satisfy

1. Ψ(d; i + 1) (ψ(d, m − d − 1)i) = ψ(d, m − d − 1)i+1 for i ≤ d − 3, and

2. Ψ(d + 1; i + 1) = Ψ(d, i).

Lemma 4.7. (Ψ(d; i) are Non-Decreasing)
For each m ≥ d + 1 with d ≥ 2 and each d − 2 ≥ i ≥ 1, the function Ψ(d; i)(x) is non-decreasing.

Proof. First, observe that

Ψ(d; i)(x + 1) − Ψ(d; i)(x) = 1 + ⌊ 1
x + 2 · (x + 1 + d − i
d − i
 )⌋ − ⌊ 1
x + 1 · (x + d − i
d − i
 )⌋ ,

thus
 Ψ(d; i)(x + 1) − Ψ(d; i)(x) ≥ 1
x + 2 · (
x + 1 + d − i
d − i
 ) − 1
x + 1 · (x + d − i
d − i
 )
.

Now, observe that

1
x + 2 · (
x + 1 + d − i
d − i
 ) = (x + 1 + d − i)!
(x + 2)(d − i)!(x + 1)! = (x + d − i)!
(d − i)!(x + 1)!
 ( x + d − i + 1
x + 2
 ) ,

and
 1
x + 1 · (
x + d − i
d − i
 ) = (x + d − i)!
(x + 1)(d − i)!x! = (x + d − i)!
(d − i)!(x + 1)! .

28

Hence,
 Ψ(d; i)(x + 1) − Ψ(d; i)(x) ≥ (x + d − i)!
(d − i)!(x + 1)!
 ( x + d − i + 1
x + 2 − 1) ,

and the right side is positive when i ≤ d − 2.

Lemma 4.8. (ψ(d, m − d − 1)d−2 is Non-Decreasing in d)
Fix m ≥ 4. Then,
 ψ(2, m − 3)0 ≤ ψ(3, m − 4)1 ≤ · · · ≤ ψ(m − 3, 2)m−5 ≤ ψ(m − 2, 1)m−4.

Furthermore, for each 2 ≤ d ≤ m − 3,

dim (M (3; ψ(d, m − d − 1)d−2)) ≤ dim (M (3; ψ(d + 1, m − d − 2)d−1)) .

Proof. In light of Remark 4.6 and Lemma 4.7, it suﬃces to show

ψ(d + 1, m − d − 2)1 ≥ ψ(d, m − d − 1)0

to prove the claim. However,

ψ(d + 1, m − d − 2)1 = m − d − 2 + ⌈ 1
m − d − 1 · (
m − 2
d − 1
 )⌉ ≥ m − d − 1 = ψ(d, m − d − 1)0.

Remark 4.9. Having proved Lemma 4.8, we now begin to work towards the second task outlined in Remark
4.4: establishing a criterion for m in terms of d, which, when met, implies

(m − 1)!
d! ≤ dim (M (3; ψ(d + 1, m − d − 2)d−1)) .

Next, we establish simple functions which we use to approximate ψ(d, m − d − 1)d−2 from below.

Deﬁnition 4.10. (Auxiliary Functions Ω and ω(d, i))
For each d ≥ 4 and d − 3 ≥ i ≥ 1, deﬁne ω(d, i) : R>0 ! R>0 by

ω(d, i)(x) = 1
(d − i)! x
d−i−1.

Similarly, for each pair m ≥ d with d ≥ 4, deﬁne the function Ω by

Ω(d, m) = (ω(d, d − 3) ◦ · · · ◦ ω(d, 1)) (m − d − 1).

Remark 4.11. (Bounding Properties of Ω and ω(d, i))
Observe that for each i,
 ω(d, i + 1)(ψ(d, m − d − 1)i) ≤ ψ(d, m − d − 1)i+1.

In particular,
 Ω(d, m) ≤ ψ(d, m − d − 1)d−2.

Example 4.12. Consider the cases when d = 5 and m = 10, 100. Then,

Ω(5, 10) ∼ 1.185, Ω(5, 100) ∼ 1.996 × 108,

ψ(5, 10)3 = 133, ψ(5, 100)3 ∼ 3.633 × 108.

29

Lemma 4.13. (Explicit Form of Ω)
For any d ≥ 4, set
 Cd :=
 d−1∏

i=3
 1
(i!)(i−2)! .

For all m ≥ d + 2, Ω(d, m) = Cd(m − d − 1)
(d−2)!,

Proof. We proceed by induction on d. When d = 4, we have

Ω(4, m) = ρ(4, 1)(m − 5) = 1
3! (m − 5)
2 = C2(m − 5)
2!.

For arbitrary d, recall
 Ω(d, m) = (ω(d, d − 3) ◦ · · · ◦ ω(d, 2) ◦ ω(d, 1)) (m − d − 1),

and
 Ω(d − 1, m − 1) = (ω(d − 1, d − 4) ◦ · · · ◦ ω(d − 1, 2) ◦ ω(d − 1, 1)) (m − d − 1).

By deﬁnition, however, ω(d + 1, i + 1) = ω(d, i). Therefore,

Ω(d, m) = (ω(d, d − 3) ◦ · · · ◦ ω(d, 2) ◦ ω(d, 1)) (m − d − 1),

= (ω(d, d − 3) ◦ · · · ◦ ω(d, 2)) (ω(d, 1)(m − d − 1)) ,
= (ω(d − 1, d − 4) ◦ · · · ◦ ω(d − 1, 1)) (ω(d, 1)(m − d − 1)) ,

= Ω(d − 1, ω(d, 1)(m − d − 1) + d + 1).

By induction, we know that

Ω(d − 1, ω(d, 1)(m − d − 1) + d + 1) = Cd−1 (ω(d, 1)(m − d − 1))(d−3)! ,

= Cd−1
 ( 1
(d − 1)! (m − d − 1)
d−2)(d−3)! ,

= Cd−1
 ( 1
(d − 1)!
 )(d−3)! (
(m − d − 1)
d−2)(d−3)! ,

= Cd(m − d − 1)
(d−2)!.

Consequently, Ω(d, m) = Ω(d − 1, ω(d, 1)(m − d − 1) + d + 1) = Cd(m − d − 1)
(d−2)!.

In the following lemma, we prove an inequality that will be useful in the proof of Proposition 4.15, the
proposition which establishes the criterion we seek.

Lemma 4.14. (Bounding log (Cd))
For each d ≥ 4, log (Cd) ≥ 2(d − 2)! − 2(d − 2)! log(d − 1) − 2(d − 3)! log(d − 1).

Proof. Observe
 log (Cd) = −
 d−1∑

i=3(i − 2)! log(i!) ≥ −
 d−1∑

i=3(i − 2)! log (
e1−iii) ,

30

where the approximation is due to Stirling’s approximation (equation 7). Hence,

log (Cd) ≥ −
 d−1∑

i=3(i − 2)! (1 − i + i log(i)) ,

=
 d−1∑

i=3(i − 1)! −
 d−1∑

i=3(i − 2)!(i) log(i),

=
 d−3∑

j=1(j + 1)! −
 d−3∑

j=1 j!(j + 2) log(j + 2),

=
 d−3∑

j=1(j + 1)! −
 d−3∑

j=1 j!(j + 1) log(j + 2) −
 d−3∑

j=1 j! log(j + 2),

≥
 d−3∑

j=1(j + 1)! − log(d − 1)
 d−3∑

j=1(j + 1)! − log(d − 1)SLd−3
j=1j!,

= (1 − log(d − 1))
 d−3∑

j=1(j + 1)! − log(d − 1)
 d−3∑

j=1 j!.

Recall that for any positive integer a, a∑

i=1 i! ≤ 2(a!). Since d ≥ 4, it follows that 1 − log(d − 1) and − log(d − 1)

are negative, hence
 log (Cd) ≥ 2(1 − log(d − 1))(d − 2)! − 2 log(d − 1)(d − 3)!,
= 2(d − 2)! − 2(d − 2)! log(d − 1) − 2(d − 3)! log(d − 1).

Proposition 4.15. (The Ω Condition)
Fix d ≥ 6. For any m ≥ d
2 − d + 4 such that

m2 − 5
2 m + 1
2 < (d + 1) + log(d) (d + 1
2
 ) + 6(d − 3)!(d − 2 − log(d − 1)),

it follows that
 Φ(d, m − d − 1) < Φ(d + 1, m − d − 2).

Proof. In light of Lemma 4.8, it suﬃces to have

(m − 1)!
d! < dim (M(3, ψ(d + 1, m − d − 2)d−1) + m. (22)

First, we approximate ψ(d + 1, m − d − 2)d−1 below by ⌈Ω(d + 1, m − d − 2)⌉ to get

dim (M (3, ψ(d + 1, m − d − 2)d−1)) + m ≥ dim (M (3, ⌈Ω(d + 1, m − d − 2)⌉)) + m. (23)

Observe that

dim (M (3, ⌈Ω(d + 1, m − d − 2)⌉)) + m

= 1
6
 (⌈Ω(d + 1, m − d − 2)⌉3 + 6 ⌈Ω(d + 1, m − d − 2)⌉2 + 11 ⌈Ω(d + 1, m − d − 2)⌉ + 6)

≥ 1
6 (
Ω(d + 1, m − d − 2)
3 + 6Ω(d + 1, m − d − 2)
2 + 11Ω(d + 1, m − d − 2) + 6)

− (Ω(d + 1, m − d − 2) + 1)
2 + m,

= 1
6 Ω(d + 1, m − d − 2)
3 − 1
6 Ω(d + 1, m − d − 2) + m.

31

Since d ≥ 6 and m ≥ d
2 − d + 4 ≥ 34, it follows that

Ω(d + 1, m − d − 2) ≥ Ω(6, m − 8) ≥ Ω(6, 26) > 5.6 × 1012,

and consequently

1
6 Ω(d + 1, m − d − 2)
3 − 1
6 Ω(d + 1, m − d − 2) + m > 1
7 Ω(d + 1, m − d − 2)
3. (24)

Substituting inequality (24) into inequality (22) and re-arranging, we have the suﬃcient criterion

7(m − 1)!
d! < Ω(d + 1, m − d − 2)
3 = C3
d(m − d − 2)
3(d−2)!.

Next, we apply Stirling’s approximations (equation 7)and obtain

7(m − 1)
m− 1
2 e2−m
√2πdd+ 1
2 e−d < C3
d(m − d − 2)
3(d−2)!,

which we re-arrange as (m − 1)
m− 1
2

em(m − d − 2)3(d−2)! <
 √
2π
7 · ed−2 · d
d+ 1
2 · C3
d. (25)

We take log of both sides of inequality (25) and examine them individually. First, the right side of
inequality (25) becomes
 log
 ( √
2π
7
 )
 + (d + 2) + (d + 1
2
 ) log(d) + 3 log (Cd) . (26)

By applying Lemma 4.14 to log (Cd), observing log ( √
2π
7 ) ≥ −1, and simplifying, it suﬃces to replace
expression (26) with

(d + 1) + (
d + 1
2
 ) log(d) + 6(d − 2)! − 6(d − 2)! log(d − 1) − 6(d − 3)! log(d − 1). (27)

The left side of inequality (25) becomes
(
m − 1
2
 ) log(m − 1) − m − 3(d − 2)! log(m − d − 2). (28)

For m ≥ d
2 − d + 4, log(m − d − 2) > log (
d
2 − 2d + 1) = 2 log(d − 1),

and multiplying by 3(d − 2)! yields

3(d − 2)! log(m − d − 2) > 6(d − 2)! log(d − 1). (29)

By combining expressions (27) and (28) with inequality (29), we obtain
(
m − 1
2
 ) log(m − 1) − m < (d + 1) + (
d + 1
2
 ) log(d) + 6(d − 2)! − 6(d − 3)! log(d).

Using the approximation log(m − 1) < m − 1, we ﬁnally arrive at the condition

m2 − 5
2 m + 1
2 < (d + 1) + (d + 1
2
 ) log(d) + 6(d − 3)! (d − 2 − log(d − 1)) ,

as claimed above.
 32

Using the simple approximations log(d) ≥ log(6) > 1 and d − 2 − log(d − 1) > 1, we arrive at a simpliﬁed
condition.

Corollary 4.16. (The Simpliﬁed Ω Condition)
Fix d ≥ 6. For any m ≥ d
2 − d + 4 such that

m2 − 5
2 m ≤ 6(d − 3)! + 2d + 1,

it follows that
 Φ(d, m − d − 1) < Φ(d + 1, m − d − 2).

Moreover,
 F (m) ≥ (m − 1)!
d! .

Proof. Together, Lemma 4.8 and Proposition 4.15 yield that

Φ(d, m − d − 1) < Φ(d
′, m − d
′ − 1)

for each d < d
′ < m − 2. For any d
′′ < d, we have

(m − 1)!
d! < (m − 1)!
(d′′)! ≤ Φ(d
′′, m − d
′′ − 1).

Hence,
 F (m) ≥ 2 ⌊ 1
2 Φ(d, m − d − 1)
⌋ + 1 ≥ (m − 1)!
d! .

We state and prove a corollary, then we recall and prove Theorem 4.1.

Corollary 4.17. (Bounding the Ratio F (m)
G(m) )

For d ≥ 11 and m ≥ 2d
2 + 11d + 15, F (m)
G(m) > d + 1.

Remark 4.18. We expect that better estimates of F (m)
G(m) could reasonably be obtained. However, Corollary
4.17 suﬃces to prove Theorem 4.1, which establishes that G(m) is the better bounding function and thus we
do not need additional data on the growth rate of F (m).

Proof. (Proof of Corollary 4.17)
Let d ≥ 11. Recall that Corollary 3.34 applies for m ≥ 2d
2 + 7d + 6 and so we set md = 2d
2 + 7d + 6.
Similarly, Corollary 4.16 applies for m ≥ d
2 − d + 4 such that

m2 − 5
2 m ≤ 6(d − 3)! + 2d + 1.

Correspondingly, we set
 Md = max {
m ∈ Z | m2 − 5
2 m ≤ 6(d − 3)! + 2d + 1} .

Observe that 2d
2 + 7d + 6 ≥ d
2 − d + 4 and, since d ≥ 11, we have

md+1 = 2d
2 + 11d + 15 < Md.

33

Corollary 3.34 yields G(md+1) < (md−1)!
(d+1)! and Corollary 4.16 yields that F (md+1) ≥ (md−1)!
d! . As a result,
we have
 F (md+1)
G(md+1) >
 ( (md−1)!
d! )

( (md−1)!
(d+1)! ) = (d + 1)!
d! = d + 1.

In fact,
 (6(d − 3)! + 2d + 1) − (
m2
d+2 − 5
2 md+2
)

is positive and strictly increasing for d ≥ 11, so md+2 < Md. Hence, Corollaries 3.34 and 4.16 yield that

F (m)
G(m) >
 ( (m−1)!
d! )

( (m−1)!
(d+1)! ) = d + 1.

for all m ≥ md = 2d
2 + 7d + 6.

Proof. (Proof of Theorem 4.1)
First, observe that Corollary 4.17 implies that

lim
m!∞ F (m)
G(m) = ∞,

and that G(m) ≤ F (m) for
 m ≥ 2 (
112) + 11(11) + 15 = 378.

The veriﬁcation of that G(m) ≤ F (m) for 1 ≤ m ≤ 59 comes from explicit computation and the relevant
data is provided in Appendices 5.1 and 5.2.
Finally, we address the cases of 60 ≤ m ≤ 377. Recall that Lemma 3.29 yields

ϑ(d, m − d − 1) ≤ m − d − 2 + (m
d
 ).

For a ﬁxed d, ϑ(m, d − m − 1) is bounded above by a polynomial of degree d in m with positive coeﬃ-
cients. Remark 3.15 yields that dim (M(2, . . . , d; ϑ(d, m − d − 1)) is also a polynomial in m, hence there is
a polynomial pd(m) with positive coeﬃcients that bounds dim (M(2, . . . , d; ϑ(d, m − d − 1)) above. Hence,
there is a minimal positive integer ad such that (ad−1)!
d! > pd(ad). Moreover, m!
d! > pd(m) for all m ≥ ad. In
particular,
 G(m) ≤ (m − 1)!
d!

for all m ≥ ad.

We compute explicitly that for all m ≥ 57, (m−1)!
9! > dim (M(2, . . . , 9; ϑ(9, m − 10)) and thus

G(m) ≤ (m − 1)!
9! .

Additionally, we explicitly compute that for m ≤ 377,

(m − 1)!
6! < dim (M(3; ψ(7, m − d − 1)5) .

34

and the same argument proving Corollary 4.16 yields that

F (m) ≥ (m − 1)!
6! .

As a consequence,
 F (m)
G(m) ≥
 (m−1)!
6!
(m−1)!
9! ≥ 9!
6! = 504

for all 60 ≤ m ≤ 376, which yields the theorem.

5 Appendices

5.1 Explicit Bounds on RD(n)

Here we provide initial data on the behavior of G(m) and provide data about F (m) for comparison.

Table 1: Upper Bounds on RD(n)
m G(m) F (m) F (m)/G(m) First Established by
2 3 3 1 Babylonians & Egyptians
3 4 4 1 Ferrari
4 5 5 1 Bring, in [Bri1786]
5 9 9 1 Segre, in [Seg1945]
6 21 41 1.952 Theorem 3.7, ﬁxing the gap in the proof in [Che1954]
7 109 121 1.175
8 325 841 2.645
9 1681 6721 3.998 Theorem 3.10
10 15121 60481 4.000
11 151,201 604,801 4.000
12 1,663,201 6,652,801 4.000
13 19,958,401 78,485,043 3.932 Theorem 3.10 / Theorem 3.24
14 259,459,201 320,082,459 1.234
15 3,632,428,801 3,632,428,801 1 Wolfson, in [Wol2021]
16 54,486,432,001 54,486,432,001 1
17 348,489,068,134 871,782,912,001 2.502 Theorem 3.24
18 2,964,061,900,801 14,820,309,504,001 5

When m = 12, 13, 14, the methods of Theorems 3.10 and 3.24 both obtain the new bound on resolvent degree.

35

5.2 Explicit Approximations of F (m)/G(m)

Here we provide additional data about the ratio F (m)
G(m) . In particular, the behavior exhibited from m = 58 to

m = 59 illustrates why the ratio F (m)
G(m) is not always non-decreasing.

Table 2: F (m)/G(m) for 19 ≤ m ≤ 59
m F (m)/G(m) G(m) given by determining an F (m) given by determining an
19 5.000
20 5.000
21 5.000 (m − 6)-plane on τ1,...,5 (m − 5)-plane on τ1,2,3,4
22 5.000
23 5.000
24 5.000
25 29.930
26 30.000
27 30.000
28 30.000
29 30.000 (m − 7)-plane on τ1,...,6 (m − 5)-plane on τ1,2,3,4
30 30.000
31 30.000
32 30.000
33 30.000
34 146.129
35 210.000
36 210.000
37 210.000
38 210.000 (m − 8)-plane on τ1,...,7 (m − 5)-plane on τ1,2,3,4
39 210.000
40 210.000
41 210.000
42 210.000
43 210.000
44 294.103
45 1680.000
46 1680.000
47 1680.000
48 1680.000
49 1680.000 (m − 9)-plane on τ1,...,8 (m − 5)-plane on τ1,2,3,4
50 1680.000
51 1680.000
52 1680.000
53 1680.000
54 1680.000
55 1680.000
56 2613.173
57 15120.000 (m − 10)-plane on τ1,...,9 (m − 5)-plane on τ1,2,3,4
58 15120.000
59 3024.000 (m − 10)-plane on τ1,...,9 (m − 6)-plane on τ1,...,5

36

5.3 Proof of Technical Lemma

We now recall the statement of Lemma 2.8 and provide a proof. We will continue to use the notation estab-
lished in Deﬁnition 2.1.

Lemma 2.8. (Technical Lemma)
Let P, Q ∈ Pr(K) and f ∈ K[x0, . . . , xr] be a homogeneous polynomial of degree d. Applying a projective
change of coordinates as necessary, we assume that

P = [1 : p1 : · · · : pr],
Q = [1 : q1 : · · · : qr],

so that the line determined by P and Q is

L(P, Q)(K) = {[1 : λp1 + µq1 : · · · : λpr + µqr] | [λ : µ] ∈ P1(K)
} .

For any point Rλ:µ = [1 : λp1 + µq1 : · · · : λpr + µqr] ∈ L(P, Q)(K),

f (Rλ:µ) = f (λP ) + f (µQ) +
 d−1∑

k=1
 1
k! t(d − k, f, λP )(µQ).

Proof. Set p0 = 1 and q0 = 1. Let f ∈ K[x0, . . . , xr] be a homogeneous polynomial of degree d. When r = 1,
the claim follows immediately from the binomial formula. We thus assume r ≥ 2. As partial derivatives are
linear, it suﬃces to consider the case where f is a monomial:

f (x0, . . . , xr) = ax
i0
0 x
i1
1 · · · x
ir
r .

Note that
 f (Rλ:µ) = a
 r∏

j=0 (λpj + µqj)
ij

= a
 r∏

j=0
 ij∑

ℓj =0
 (ij
ℓj
)
(λpj)
ι(j)−ℓj (µqj)
ℓj

= a
 i0∑

ℓ0=0 · · ·
 ir∑

ℓr=0
 

 r∏

j=0
 (ij
ℓj
)
(λpj )
ij −ℓj (µqj)
ℓj
 

 .

To simplify notation, we denote an indexing set

I = {(k0, . . . , kr) ∈ Z
r+1 | 0 ≤ kj ≤ ij}

and, in accordance with the notation of Deﬁnition 2.1, partition it into subsets

Ik = {(k0, . . . , kr) ∈ Z
r+1 | k0 + · · · + kr = k}

for 0 ≤ k ≤ d. Thus, we write

f (Rλ:µ) = a ∑

I
 

 r∏

j=0
 (ij
kj
)
(λpj )
ι(j)−kj (µqj)
kj
 



= a
 d∑

k=0
 ∑

Ik
 

 r∏

j=0
 (ij
kj
)
(λpj)
ij −kj (µqj)
kj
 



37

Note that
 f (λP ) = a
 

 r∏

j=0
(λpj )
ij
 

 = a ∑

I0
 

 r∏

j=0
 (
ij
0
 )
(λpj)
ij −0(µqj )
0


 ,

f (µQ) = a
 

 r∏

j=0
(µqj )
ij
 

 = a ∑

Id
 

 r∏

j=0
 (
ij
ij
)
(λpj)
ij −ij (µqj)
ij
 

 .

Thus,
 f (Rλ:µ) − f (λP ) − f (µQ) = a
 d−1∑

k=1
 ∑

Ik
 

 r∏

j=0
 (ij
lj
 )
(λpj )
ij −kj (µqj)
kj
 

 .

Consequently, it suﬃces to show that

1
k! t(d − k, f, λP )(µQ) = a ∑

Ik
 

 r∏

j=0
 (
ij
lj
 )(λpj)
ij −kj (µqj )
kj
 



for each 1 ≤ k ≤ d − 1. Recall that
 [k]∗ = {1, . . . , k} ,

[r] = {0, 1, . . . , r} ,
I ∗
k = HomSet([k]∗, [r])

and for ι ∈ I ∗
k , we set |ι|(j) = |ι
−1(j)|. Hence,

1
k! t(d − k, f, λP )(µQ)

= 1
k!
 ∑

ι∈I ∗
k
 (∂|ι|(0)
0 · · · ∂|ι|(0)
r f )∣
∣
∣
∣λP (µq0)
|ι|(0) · · · (µqr)
|ι(r)|

= 1
k!
 ∑

ι∈I ∗
k a i0
(i0 − |ι|(0))! · · · ir
(ir − |ι|(r))! (λp0)
i0−|ι|(0) · · · (λpr)
ir −|ι|(r)(µq0)
|ι|(0) · · · (µqr)
|ι(r)|

= a
k!
 ∑

ι∈I ∗
k
 r∏

j=0
 ij
(ij − |ι|(j))! (λpj )
ij −|ι|(j)(µqj )
|ι|(j)

Note that for any ι, ι
′ ∈ I ∗
k whose ﬁbers at every point of [r] have the same cardinality, we have

∂|ι|(0)
0 · · · ∂|ι|(0)
r f = ∂|ι′|(0)
0 · · · ∂|ι′|(0)
r f

as partial derivatives of polynomials commute. Now, given any ι ∈ I ∗
k , we can apply a permutation of the
symmetric group Sk to [k]∗ and not change the number of ﬁbers of each cardinality. However, to get a unique
representative of each unordered class of partial derivative, we must identify any permutations which ﬁx all
of the ﬁbers, but permute the elements within any such ﬁber. Thus, to a given ι, there are

|Sk|
∣
∣S|ι|(0)∣
∣ · · · ∣
∣S|ι(r)|∣
∣ = k!
 r∏

l=0
 1
(|ι|(j))!

38

permutations which give the same unordered partial derivative. Hence,

1
k! t(d − k, f, λP )(µQ) = a
k!
 ∑

ι∈I ∗
k
 r∏

j=0
 ij
(ij − |ι|(j))! (λpj )
ij −|ι|(j)(µqj )
|ι|(j)

= a
k!
 ∑

Ik
 (

k!
 r∏

l=0
 1
(|ι|(j))!
 ) r∏

j=0
 ij
(ij − kj )! (λpj)
ij −kj (µqj )
kj

= a ∑

Ik
 r∏

j=0
 (ij
kj
)
(λpj)
ij −kj (µqj)
kj

which yields the lemma.

References

[AS1976] Arnol’d, V.I. and Shimura, G. Superpositions of algebraic functions. Proc. Symposia in Pure Math,
AMS, Providence, 28:45-46, 1976.

[Ber1923] Bertini, E. Introduzione alla geometria projettiva degli iperspazi con appendice sulle curve alge-
briche e loro singolarit`a. Seconda edizione riveduta ed ampliata. Messina, G. Principato, 1923.

[Bra1975] Brauer, R. On the resolvent problem. Ann. Mat. Pura Appl. (4) 102:45-55, 1975.

[Bri1786] Bring, E. Meletemata quædam Mathematica circa Transformationem Æquationum Algebraicarum
(“Some Selected Mathematics on the Transformation of Algebraic Equations”). Lund, 1786.

[Che1954] Chebotarev, G. N. On the problem of resolvents. Kazan. Gos. Univ. Uˇc. Zap., (2) 114:189-193,
1954.

[CHM2017] Chen, A., He, Y-H., and McKay J. Erland Samuel Bring’s “Transformation of Algebraic Equa-
tions,” 2017. arXiv:1711.09253v1.

[DM1998] Debarre, O and Manivel, L. Sur la vari´et´e des espaces lin´eaires contenus dans une intersection
compl`ete. Math. Ann., 312(3):549-574, 1998.

[Dix1993] Dixmier, J. Histoire de 13e probl`eme de Hilbert. Cahiers du s´eminare d’histoire des math´ematiques,
3(2):85-94, 1993.

[Dol2012] Dolgachev, I. Classical Algebraic Geometry: A Modern View. Cambridge: Cambridge University
Press, 2012.

[FW2019] Farb, B and Wolfson, J. Resolvent degree, Hilbert’s 13th problem and geometry. Enseign. Math.,
65(3-4):303-376, 2019.

[Ham1836] Hamilton, W. Inquiry into the validity of a method recently proposed by George B. Jerrard, esq.,
for transforming and resolving equation of elevated degrees. Report of the Sixth Meeting of the British
Assocation for the Advancement of Science, p.295-348, 1836.

[Har2010] Harris, J. Algebraic Geometry. Springer: New York, 2010.

[Hil1927] Hilbert, D. ¨Uber die Gleichung neunten Grades. Math. Ann., 97(1):243-250, 1927.

[Kle1884] Klein, F. Vorlesungen ¨uber das Ikosaeder und die Auﬂ¨osung der Gleichungen vom f¨unften Grade.
Teubner, Leipzig, 1884.

[Kle1887] Klein, F. Zur Theorie der allgemeinen Gleichungen sechsten und siebenten Grades. Math. Ann.,
28 (4):499-532, 1887.
 39

[Kle1905] Klein, F. ¨Uber die Auﬂ¨osung der allgemeinen Gleichungen f¨unften und sechsten Grades. J. Reine
Angew. Math., 129:150-174, 1905.

[Mor1956] Morrice, G.G. Felix Klein’s “Lectures on the icosahedron and solution of equation of ﬁfth degree,”
2nd and rev. edition, New York, Dover Publications, 1956.

[OEIS2021] OEIS Foundation Inc. (2021), The On-Line Encyclopedia of Integer Sequences,
http://oeis.org/A000905.

[Rob1955] Robbins, H. A Remark on Stirling’s Formula. Amer. Math. Monthly, 62(1):26, 1955.

[Seg1945] Segre, B. The Algebraic Equations of Degrees 5, 9, 157 . . . , and the Arithmetic Upon an Algebraic
Variety. Ann. of Math., 46(2):287-301, 1945.

[Sut2019] Sutherland, A. Felix Klein’s “About the Solution of General Equations of Fifth and Sixth Degree
(Excerpt from a letter to Mr. K. Hensel),” A. Sutherland, 2019, arXiv:1911.02358.

[Sut2021A] Sutherland, A. Anders Wiman’s “On the Application of Tschirnhaus Transformations to the
Reduction of Algebraic Equations,” 2021, arXiv:2106.09247.

[Sut2021B] Sutherland, A. G. N. Chebotarev’s “On the Problem of Resolvents,” 2021, arXiv:2107:.01006.

[Syl887] Sylvester, J.J. On the so-called Tschirnhausen Transformation. J. Reine Angew. Math., 100:465-486,
1887.

[SH1887] Sylvester, J.J. and Hammond, J. On Hamilton’s numbers. Philos. Trans. R. Soc. Lond., A, 178:285-
312, 1887.

[SH1888] Sylvester, J.J. and Hammond, J. On Hamilton’s numbers, Part II. Philos. Trans. R. Soc. Lond.,
A, 179:65-72, 1888.

[Tsc1683] von Tschirnhaus, E. Methodus auferendi omnes terminos intermedios ex data aeqvatione (Method
of eliminating all intermediate terms from a given equation). Acta Eruditorum, p.204-207, 1683.

[Wal2008] Waldron, A. Fano Varieties of Low-Degree Smooth Hypersurfaces and Unirationality, Bachelor
thesis, Harvard University, Cambridge, Massachusetts, 2008.

[Wim1927] Wiman, A. ¨Uber die Anwendung der Tschirnhausen-Transformation auf die Reduktion algebrais-
cher Gleichungen. Nova Acta R. Soc. scient. Uppsala, 4(16), 1927.

[Wol2021] Wolfson, J. Tschirnhaus transformations after Hilbert. Enseign. Math., 66(3):489-540, 2021.

40
