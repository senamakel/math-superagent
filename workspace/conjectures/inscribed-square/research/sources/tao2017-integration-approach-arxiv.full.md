<!-- source: https://arxiv.org/pdf/1611.07441 | converted from PDF -->

AN INTEGRATION APPROACH TO THE TOEPLITZ SQUARE PEG
PROBLEM

TERENCE TAO

Abstract. The “square peg problem” or “inscribed square problem” of Toeplitz asks
if every simple closed curve in the plane inscribes a (non-degenerate) square, in the
sense that all four vertices of that square lie on the curve. By a variety of arguments
of a “homological” nature, it is known that the answer to this question is positive if
the curve is suﬃciently regular. The regularity hypotheses are needed to rule out the
possibility of arbitrarily small squares that are inscribed or almost inscribed on the
curve; because of this, these arguments do not appear to be robust enough to handle
arbitrarily rough curves.
In this paper we augment the homological approach by introducing certain integrals
associated to the curve. This approach is able to give positive answers to the square
peg problem in some new cases, for instance if the curve is the union of two Lipschitz
graphs f, g : rt0, t1s Ñ R that agree at the endpoints, and whose Lipschitz constants
are strictly less than one. We also present some simpler variants of the square problem
which seem particularly amenable to this integration approach, including a periodic
version of the problem that is not subject to the problem of arbitrarily small squares
(and remains open even for regular curves), as well as an almost purely combinatorial
conjecture regarding the sign patterns of sums y1 ` y2 ` y3 for y1, y2, y3 ranging in
ﬁnite sets of real numbers.
 1. Introduction

A subset Γ of the plane R2 is said to inscribe a square if it contains the four vertices
of a square of positive sidelength. Note that despite the terminology, we do not require
the solid square with these four vertices to lie in the region enclosed by Γ (in the case
that Γ is a closed curve); see Figure 1.

The following conjecture of Toeplitz [26] is usually referred to as the Square Peg Problem
or Inscribed Square Problem:

Conjecture 1.1 (Square Peg Problem). [26] Let γ : R{LZ Ñ R
2 be a simple closed
curve. Then γpR{LZq inscribes a square.

In this paper, a curve γ : I Ñ M denotes a continuous map from a domain I that is
either an interval rt0, t1s or a circle R{LZ to a manifold M , with the curve being called
closed in the latter case. Such a curve is called simple if γ is injective.

2010 Mathematics Subject Classiﬁcation. 55N45.
1arXiv:1611.07441v2  [math.GN]  7 Jun 2017
2 TERENCE TAO

Figure 1. A (simple, closed, polygonal) curve inscribing a square.

A recent survey on this problem, together with an extensive list of further references
may be found in [16]; the brief summary below is drawn from that survey.

Thanks to arguments of a homological nature, the above conjecture is known assuming
that the curve γ is suﬃciently regular. For instance:

‚ Toeplitz [26] claimed Conjecture 1.1 for convex curves, but did not publish a
proof. This case was partially resolved by Emch [4], [5] and then fully resolved
in [29], [3]; this case can also be deduced from the “table theorem” of Fenn [7].
‚ Hebbert [10] gave a proof of Conjecture 1.1 for quadrilaterals. A proof of Con-
jecture 1.1 for arbitrary polygons was given in [18]; see also [20], [21] for some
further “discretisations” of the conjecture. See [19] for some computer-assisted
quantitative bounds on one such discretisation.
‚ Emch [6] established Conjecture 1.1 for piecewise analytic curves. An alternate
proof of the analytic case was obtained by Jerrard [11].
‚ Schnirelman [22] (see also [8]) established Conjecture 1.1 for continuously twice
diﬀerentiable curves (and in fact was also able to treat some curves outside this
class). An alternate argument treating continuously twice diﬀerentiable curves
(obeying an additional technical geometric condition) was obtained by Makeev
[14].
‚ Nielsen and Wright [17] established Conjecture 1.1 for curves symmetric around
a line or point.
‚ Stromquist [24] established Conjecture 1.1 for locally monotone curves. An
alternate treatment of this case was given in [28].

INTEGRATION APPROACH TO SQUARE PEG PROBLEM 3

‚ Cantarella, Denne, McCleary [2] established Conjecture 1.1 for C 1 curves, and
also for bounded curvature curves without cusps.
‚ Matschke [15] established Conjecture 1.1 for an open dense class of curves
(namely, curves that did not contain small trapezoids of a certain form), as
well as curves that were contained in annuli in which the ratio between the
outer and inner radius is at most 1 ` ?
2.

One can broadly classify the methods of proof in the above positive results as being
“homological” in nature, in that they use algebraic topology tools such as the intersec-
tion product in homology, bordism, equivariant obstruction theory, or more elementary
parity arguments counting the number of intersections between curves. In fact, many
of these proofs establish the stronger claim that (under some suitable genericity and
regularity hypotheses) there are an odd number of squares with vertices lying on the
curve.

It is tempting to attack the general case of Conjecture 1.1 by approximating the curve
γ by a curve in one of the above classes, applying an existing result to produce squares
with vertices on the approximating curve, and then taking limits somehow (e.g. by a
compactness argument). However, in the absence of some additional regularity hypoth-
esis on the curve, it could conceivably happen that the approximating inscribed squares
degenerate to a point in the limit. Even if the original curve is smooth except for a
single singular point, one could imagine that all squares in the approximating curves
concentrate into that singular point in the limit. This scenario of squares degenerating
to a point is the primary reason for the inability to remove the regularity hypotheses in
the known positive results on the problem.

In this paper we propose to modify the homological approach to the inscribed square
problem, by focusing not only on the parity of intersections between various geometric
objects associated to the curve γ, but also on bounding certain integrals associated to
these curves. As with previous works, one requires a certain amount of regularity (such
as rectiﬁability, Lipschitz continuity, or piecewise linearity) on the curves in order to
initially deﬁne these integrals; but the integrals enjoy more stability properties under
limits than intersection numbers, and thus may oﬀer a route to establish more cases
of Conjecture 1.1. As an instance of this, we give the following positive result towards
this conjecture, which appears to be new. For any I Ă R and any function f : I Ñ R,
we deﬁne the graph Graphf : I Ñ R2 to be the function Graphf ptq :“ pt, f ptqq, so in
particular Graphf pIq Ă R2 is the set

Graphf pIq :“ tpt, f ptqq : t P Iu.

Such a function f is said to be C-Lipschitz for a given C ą 0 if one has |f psq ´ f ptq| ď
C|s ´ t| for all s, t P I. Similarly if f is deﬁned on a circle R{LZ rather than an interval
I (using the usual Riemannian metric on R{LZ).

Theorem 1.2 (The case of small Lipschitz constant). Let rt0, t1s be an interval, and
let f, g : rt0, t1s Ñ R be p1 ´ εq-Lipschitz functions for some ε ą 0. Suppose also that
f pt0q “ gpt0q, f pt1q “ gpt1q, and f ptq ă gptq for all t0 ă t ă t1. Then the set

Graphf prt0, t1sq Y Graphgprt0, t1sq (1.1)

4 TERENCE TAO

inscribes a square.

In other words, Conjecture 1.1 holds for curves that traverse two Lipschitz graphs, as
long as the Lipschitz constants are strictly less than one. The condition of having Lip-
schitz constant less than one is superﬁcially similar to the property of being locally
monotone, as considered in the references [24], [28] above; however, due to a poten-
tially unbounded amount of oscillation at the endpoints Graphf pt0q “ Graphgpt0q and
Graphf pt1q “ Graphgpt1q, the sets in Theorem 1.2 are not necessarily locally monotone
at the endpoints, and so the results in [24], [28] do not directly imply Theorem 1.2.
Similarly for the other existing positive results on the square peg problem.

We prove Theorem 1.2 in Section 3. A key concept in the proof will be the notion of the
(signed) area ş

γ y dx under a rectiﬁable curve γ; see Deﬁnition 3.2. This area can be
used to construct a “conserved integral of motion” when one traverses the vertices of a
continuous family of squares; see Lemma 3.5. Theorem 1.2 will then follow by applying
the contraction mapping theorem to create such a continuous family of squares to which
the conservation law can be applied, and then invoking the Jordan curve theorem to
obtain a contradiction. The hypothesis of f, g having Lipschitz constant less than one
is crucially used to ensure that the curve that one is applying the Jordan curve theorem
to is simple; see Proposition 3.8.

Since the initial release of this paper, we have learned that a very similar method was
introduced by Karasev [12] to obtain a partial result on the related problem of Makeev
[14] of inscribing a given cyclic quadrilateral in a simple smooth closed curve, and
indeed the proof of Theorem 1.2 can be generalised to handle inscribing an equiangular
trapezoid if the Lipschitz constants are small enough; see Remark 3.10. We thank
Benjamin Matschke for this reference and observation.

Without the hypothesis of small Lipschitz constant, the Jordan curve theorem is no
longer available, and we do not know how to adapt the argument to prove Conjecture
1.1 in full generality. However, in later sections of the paper we present some related
variants of Conjecture 1.1 which seem easier to attack by this method, including a
periodic version (Conjecture 4.1), an area inequality version (Conjecture 5.6), and a
combinatorial version (Conjecture 6.8). In contrast to the original square problem, the
periodic version remains open even when the curves are piecewise linear (and this case
seems to contain most of the essential diﬃculties of the problem). Conjecture 5.6 is the
strongest of the new conjectures in this paper, implying all the other conjectures stated
here except for the original Conjecture 1.1 (although it would imply some new cases
of that conjecture). Conjecture 6.8 is a simpliﬁed version of Conjecture 5.6 that is an
almost purely combinatorial claim regarding the sign patterns of triple sums y1`y2`y3 of
numbers y1, y2, y3 drawn from ﬁnite sets of real numbers. It seems to be a particularly
tractable “toy model” for the original problem, though the author was not able to
fully resolve it. The logical chain of dependencies between these conjectures, as well
as some more technical variants of these conjectures that will be introduced in later
sections, is summarised as follows, in which each conjecture is annotated with a very

INTEGRATION APPROACH TO SQUARE PEG PROBLEM 5

brief description:

(square peg)
Conj. 1.1 (quadripartite)
Conj. 5.2 ðù (area ineq.)
Conj. 5.6 (combinatorial)
Conj. 6.8
ó ó ó õ
(special periodic)
Conj. 4.6 ðù (periodic)
Conj. 4.1 (special area ineq.)
Conj. 6.1 ðñ (sym. special area ineq.)
Conj. 6.2

The author is supported by NSF grant DMS-1266164, the James and Carol Collins
Chair, and by a Simons Investigator Award. He also thanks Mark Meyerson, Albert
Hasse, the anonymous referees, and anonymous commenters on his blog for helpful
comments, suggestions, and corrections.

2. Notation

Given a subset E of a vector space V and a shift h P V , we deﬁne the translates

E ` h :“ tp ` h : p P Eu.

Given two subsets E, F in a metric space pX, dq, we deﬁne the distance

distpE, F q :“ inf
pPE,qPF dpp, qq.

We use the asymptotic notation X “ OpY q to denote an estimate of the form |X| ď CY
for some implied constant C; in many cases we will explicitly allow the implied constant
C to depend on some of the ambient parameters. If n is an asymptotic parameter going
to inﬁnity, we use X “ opY q to denote an estimate of the form |X| ď cpnqY where cpnq
is a quantity depending on n (and possibly on other ambient parameters) that goes to
zero as n Ñ 8 (holding all other parameters ﬁxed).

We will use the language of singular homology (on smooth manifolds) in this paper,
thus for instance a 1-chain in a manifold M is a formal integer linear combination of
curves γ : I Ñ M , and a 1-cycle is a 1-chain σ whose boundary Bσ vanishes. Two
k-cycles are homologous if they diﬀer by a k-boundary, that is to say the boundary
BU of a k ` 1-cycle. We integrate (continuous) k-forms on (piecewise smooth) k-chains
in the usual fashion, for instance if σ “ řn
i“1 ciγi is a 1-chain that is an integer linear
combination of curves γi, and θ is a 1-form, then ş

σ θ :“ řn
i“1 ci ş

γi σ. See for instance [9]
for the formal deﬁnitions of these concepts and their basic properties. We will not use
particularly advanced facts from singular homology; perhaps the most important fact we
will use is the claim that if two (piecewise linear) cycles γ1, γ2 in an oriented manifold
are homologous and intersect a smooth oriented submanifold V (without boundary)
transversely, then their intersections γ1 X V , γ2 X V are homologous cycles in V . Indeed,
if γ1 and γ2 diﬀer by the boundary of some cycle σ, then γ1 X V and γ2 X V diﬀer by the
boundary of σ X V (viewed as a cycle with an appropriate orientation); alternatively,
one may use Poincar´e duality and the theory of the cup product.

6 TERENCE TAO

3. Proof of positive result

We now prove Theorem 1.2. It will be convenient to give a name to the space of all
squares.

Deﬁnition 3.1 (Squares). We deﬁne Squares Ă pR
2q
4 to be the set of all quadruples
of vertices of squares in R
2 traversed in anticlockwise order; more explicitly, we have

Squares :“ tppx, yq, px`a, y`bq, px`a´b, y`a`bq, px´b, y`aqq : x, y, a, b P R; pa, bq ‰ p0, 0qu.

By abuse of notation we refer to elements of Squares as (non-degenerate) squares. Thus
we see that a set Γ Ă R2 inscribes a square if and only if Γ
4 intersects Squares. We
also form the closure

Squares :“ tppx, yq, px ` a, y ` bq, px ` a ´ b, y ` a ` bq, px ´ b, y ` aqq : x, y, a, b P Ru

in which the sidelength of the square is allowed to degenerate to zero; this is a four-
dimensional linear subspace of pR
2q4. A quadruple pγ1, γ2, γ3, γ4q of curves γ1, γ2, γ3, γ4 : rt0, t1s Ñ
R
2 is said to traverse squares if one has pγ1ptq, γ2ptq, γ3ptq, γ4ptqq P Squares for all
t P rt0, t1s; note that we allow the square traversed to degenerate to a point. Equiv-
alently, pγ1, γ2, γ3, γ4q traverses squares if and only if there exist continuous functions
x, y, a, b : rt0, t1s Ñ R2 such that

γ1ptq “ pxptq, yptqq

γ2ptq “ pxptq ` aptq, yptq ` bptqq

γ3ptq “ pxptq ` aptq ´ bptq, yptq ` aptq ` bptqq

γ4ptq “ pxptq ´ bptq, yptq ` aptqq.

We will also need the notion of the area under a (rectiﬁable) curve. Recall that a curve
γ : rt0, t1s Ñ R2 is rectiﬁable if the sums řn´1
i“0 |γpsi`1q ´ γpsiq| are bounded for all
partitions t0 “ s0 ă s1 ă ¨ ¨ ¨ ă sn “ t1. If we write γptq “ pxptq, yptqq, this is equivalent
to requiring that the functions x, y : rt0, t1s Ñ R
2 are of bounded variation.

Deﬁnition 3.2 (Area under a curve). Let γ : rt0, t1s Ñ R
2 be a rectiﬁable curve, and
write γptq “ pxptq, yptqq for t P rt0, t1s. The area under γ, denoted by ş

γ y dx, is deﬁned
to be the real number ż

γ y dx :“ ż t1

t0 yptq dxptq

where the integral on the right-hand side is in the Riemann-Stieltjes sense, that is to
say the limit of řn´1
i“0 yps˚
i qpxpsi`1q ´ xpsiqq for any partition t0 “ s0 ă ¨ ¨ ¨ ă sn “ t1
and si ď s˚
i ď si`1 as max0ďiďn´1 |si`1 ´ si| goes to zero.

Of course, if γ is piecewise smooth, this deﬁnition of ş

γ y dx agrees with the usual
deﬁnition of ş

γ y dx as the integral of the 1-form y dx on γ (now viewed as a 1-chain).

Example 3.3. If f : rt0, t1s Ñ R is continuous of bounded variation, then the area
under the curve Graphf is just the usual Riemann integral:
ż

Graphf y dx “ ż t1

t0 f ptq dt.

INTEGRATION APPROACH TO SQUARE PEG PROBLEM 7

Figure 2. The area under the spiral (with the anticlockwise orientation)
is equal to |A| ´ |B| ´ 2|C| ´ 3|D|, where |A| is the area of the region
A, and similarly for |B|, |C|, |D|; the weights `1, ´1, ´2, ´3 attached to
A, B, C, D here are the winding numbers of the spiral together with the
horizontal and vertical line segments used to close up the curve.

In particular, if f is positive, ş

Graphf y dx is the area of the region bounded by Graphf ,
the real axis, and the vertical lines tt0, t1u ˆ R. If γ is not a graph, the area under γ is
more complicated; see Figure 2.

It will be particularly important to understand the area under a closed curve:

Lemma 3.4. Let γ : rt0, t1s Ñ R
2 be a simple closed anticlockwise rectiﬁable curve, and
let Ω be the bounded open region enclosed by this curve as per the Jordan curve theorem.
Then the area under the curve γ is then equal to the negative of the Lebesgue measure
|Ω| of Ω. In particular, this area is non-zero.

Of course, if γ were clockwise instead of anticlockwise, then the negative sign in the
above lemma would be removed; however, it would still be true that the area under this
curve is non-zero.

8 TERENCE TAO

Proof. In the case that γ is a polygonal path, this claim is clear from Stokes’ theorem:
ż
γ y dx “ ż

BΩ y dx “ ´ ż

Ω dx ^ dy. (3.1)

Now we consider the general case. The strategy is to approximate γ by a polygonal
path, apply (3.1), and take limits; but (as with the proof of the Jordan curve theorem)
some care must be taken with the limiting argument.

We can normalise rt0, t1s “ r0, 1s. Let ε0 ą 0 be a small parameter (which will eventually
be sent to zero). By continuity of γ, there exists 0 ă ε1 ă ε0 such that |γptq ´ γpt
1q| ď ε0
whenever t mod 1 and t
1 mod 1 are separated by distance at least ε1 on the unit circle
R{Z. By a further application of continuity and the hypothesis that γ is simple, there
exists 0 ă ε2 ă ε1 such that |γptq ´ γpt
1q| ě ε2 whenever t mod 1 and t
1 mod 1 are
separated by distance at least ε1 on the unit circle R{Z. Now let n be a natural number,
that we assume to be suﬃciently large depending on γ, ε0, ε1, ε2. Let γn : r0, 1s Ñ R
2

be the piecewise polygonal path formed by joining up the points γnpj{nq :“ γpj{nq for
j “ 0, . . . , n by line segments, thus

γn
 ˆj ` θ
n
 ˙ :“ p1 ´ θqγ ˆ j
n
 ˙ ` θγ ˆj ` 1
n
 ˙

for j “ 0, . . . , n ´ 1 and 0 ď θ ď 1. As γ is uniformly continuous, we see for n large
enough that
 |γnptq ´ γptq| ă ε2
2 (3.2)

for all t P r0, 1s. Also, it is clear that the length of γn is bounded by the length of the
rectiﬁable curve γ.

The path γn is closed, but it need not be simple. However, from (3.2), the triangle
inequality, and the construction of ε2, we see that a collision γnptq “ γnpt
1q can only
occur if t mod 1 and t
1 mod 1 diﬀer by at most ε1 in the unit circle. In such a case, γn
can be viewed as the sum (in the sense of 1-cycles) of two closed polygonal paths, one
of which has diameter at most ε0. Deleting the latter path and iterating, we conclude
that γn can be viewed as the sum of a simple closed polygonal path γ0
n and a ﬁnite
number of closed polygonal paths γ1
n, . . . , γk
n of diameter at most ε0; furthermore, the
total lengths of γ0
n, γ1
n, . . . , γk
n sum up to at most the length of γ, and from (3.2) we see
that the curves γ1
n, . . . , γk
n lie within the 2ε0-neighbourhood of γ.

If ε0 is small enough, we can ﬁnd a point z in Ω that is at a distance at least 10ε0 from
γ. The winding number of γ around z is equal to 1. By Rouche’s theorem, the winding
number of γn around z is then also equal to 1, while the winding numbers of γ1
n, . . . , γk
n
around z are equal to 0. Thus the winding number of γ0
n around z is equal to 1; thus
γ0
n has an anticlockwise orientation, and z lies in the region Ωn enclosed by γ0
n. This
argument also shows that the symmetric diﬀerence Ω∆Ωn between Ω and Ωn lies in the
ε0-neighbourhood of γ. As γ is rectiﬁable, this implies that

|Ωn| “ |Ω| ` Opε0q

INTEGRATION APPROACH TO SQUARE PEG PROBLEM 9

where the implied constant in the Opq notation depends on the length of γ. On the
other hand, from (3.1) one has ż

γ0
n y dx “ ´|Ωn|.

For each i “ 1, . . . , k, we see that
ż

γi
n y dx “ ż

γi
npy ´ yiq dx “ Opε0ℓpγi
nqq

where yi is the y-coordinate of an arbitrary point in γi
n, and ℓpγi
nq denotes the length of
γi
n. Summing, we conclude that
 kÿ

i“1
 ż

γi
n y dx “ Opε0q.

Finally, for n suﬃciently large, we have from the rectiﬁability of γ that
ż

γn y dx “ ż

γ y dx ` Opε0q.

Putting all these bounds together, we conclude that
ż

γ y dx “ ´|Ω| ` Opε0q;

since ε ą 0 can be made arbitrarily small, the claim follows. □

The relevance of this area concept to the square peg problem lies in the following simple
identity.

Lemma 3.5 (Conserved integral of motion for squares). Let γ1, γ2, γ3, γ4 : rt0, t1s Ñ R
2

be rectiﬁable curves such that pγ1, γ2, γ3, γ4q traverses squares (as deﬁned in Deﬁnition
3.1). Then we have the identity
ż

γ1 y dx ´ ż

γ2 y dx ` ż

γ3 y dx ´ ż

γ4 y dx “ apt1q
2 ´ bpt1q
2

2 ´ apt0q
2 ´ bpt0q
2

2 , (3.3)

where the functions x, y, a, b : rt0, t1s Ñ R are as in Deﬁnition 3.1.

Proof. From Deﬁnition 3.1 and Deﬁnition 3.2 we have
ż

γ1 y dx “ ż t1

t0 yptq dxptq

ż

γ2 y dx “ ż t1

t0 pyptq ` bptqq pdxptq ` daptqq

ż

γ3 y dx “ ż t1

t0 pyptq ` aptq ` bptqq pdxptq ` daptq ´ dbptqq

ż

γ4 y dx “ ż t1

t0 pyptq ` aptqq pdxptq ´ dbptqq;

10 TERENCE TAO

note from the rectiﬁability of γ1, γ2, γ3, γ4 that x, y, x ` a, y ` b (and hence a, b) are of
bounded variation. After some canceling, we may then write the left-hand side of (3.3)
as ż t1

t0 aptq daptq ´ ż t1

t0 bptq dbptq.

Since a, b are Lipschitz continuous, one has aps1qpaps1q´apsqq “ 1
2aps1q
2 ´ 1
2apsq2 `Op|s´
s1|2q for any s, s
1 P rt0, t1s, which easily implies that
ż t1

t0 aptq daptq “ 1
2 a2pt1q ´ 1
2a2pt0q;

similarly we have ż t1

t0 bptq dbptq “ 1
2 b2pt1q ´ 1
2b2pt0q,

and the claim follows. □

Remark 3.6. Geometrically, this conserved integral reﬂects the following elementary
fact: if a square with vertices p1, p2, p3, p4 (traversed in anticlockwise order) and side-
length l is deformed to a nearby square with vertices p1 ` dp1, p2 ` dp2, p3 ` dp3, p4 ` dp4
and sidelength l ` dl, then the diﬀerence of the areas of the two quadrilaterals with ver-
tices p1, p1 ` dp1, p4 ` dp4, p4 and p2, p2 ` dp2, p3 ` dp3, p3 respectively add up to exactly
half the diﬀerence between the areas l2, pl ` dlq2 of the two squares (see Figure 3).

Remark 3.7. One can interpret Lemma 3.5 in the language of diﬀerential forms as
follows. For i “ 1, 2, 3, 4, let πi : Squares Ñ R2 be the i
th coordinate projection, then
we can pull back the 1-form y dx on R
2 by πi to create a 1-form π˚
i py dxq on the
4-manifold Squares. Then the identity (3.3) may be rewritten as

π˚
1 py dxq ´ π˚
2 py dxq ` π˚
3 py dxq ´ π˚
4 py dxq “ dφ

where φ : Squares Ñ R is the 0-form that takes a square ppx, yq, px ` a, y ` bq, px ` a ´
b, y ` a ` bq, px ´ b, y ` aqq to the quantity a2´b2
2 , and d denotes the exterior derivative.
In particular, the 1-form π˚
1 py dxq ´ π˚
2 py dxq ` π˚
3 py dxq ´ π˚
4 py dxq is exact.

Now we prove Theorem 1.2. Let rt0, t1s, f, g, ε be as in that theorem. It is convenient
to extend the functions f, g : rt0, t0s Ñ R by constants to the whole real line R to form
extended functions ˜f , ˜g : R Ñ R. That is to say, we deﬁne ˜f ptq “ ˜gptq :“ f pt1q “ gpt1q
for t ą t1, ˜f ptq “ ˜gptq :“ f pt0q “ gpt0q for all t ă t0, and ˜f ptq :“ f ptq and ˜gptq :“ gptq
for t0 ď t ď t1. Clearly ˜f , ˜g : R Ñ R continue to be p1 ´ εq-Lipschitz and of bounded
variation.

For any t P R, the map

pa, bq ÞÑ p˜gpt ´ bq ´ ˜f ptq, ˜f pt ` aq ´ ˜f ptqq (3.4)

is a strict contraction on R
2 (with the usual Euclidean metric) with contraction constant
at most 1 ´ ε. Hence, by the contraction mapping theorem (or Banach ﬁxed point
theorem) applied to the complete metric space R
2, there is a unique solution paptq, bptqq P
R
2 to the ﬁxed point equation

paptq, bptqq “ p˜gpt ´ bptqq ´ ˜f ptq, ˜f pt ` aptqq ´ ˜f ptqq; (3.5)

INTEGRATION APPROACH TO SQUARE PEG PROBLEM 11

Figure 3. The diﬀerence in areas between the shaded regions is half the
diﬀerence in areas between the squares. Taking “Riemann sums” of this
fact will yield Lemma 3.5.

furthermore, aptq and bptq depend in a Lipschitz fashion on t (the Lipschitz constant
can be as large as Op1{εq, but this will not concern us). If we then deﬁne1 the functions
γ1, γ2, γ3, γ4 : rt0, t1s Ñ R2 by

γ1ptq “ pt, ˜f ptqq (3.6)

γ2ptq “ pt ` aptq, ˜f ptq ` bptqq (3.7)

γ3ptq “ pt ` aptq ´ bptq, ˜f ptq ` aptq ` bptqq (3.8)

γ4ptq “ pt ´ bptq, ˜f ptq ` aptqq (3.9)

for all t P R, then pγ1, γ2, γ3, γ4q is a quadruple of Lipschitz (and thus locally rectiﬁable)
curves that traverse squares. From (3.5), (3.6), (3.7), (3.9) we have

γ1ptq “ Graph ˜f ptq (3.10)

γ2ptq “ Graph ˜f pt ` aptqq (3.11)

γ4ptq “ Graph˜gpt ´ bptqq (3.12)

for all t P R. In particular, γ1, γ2, γ4 take values in Graph ˜f pRq, Graph ˜f pRq, and
Graph˜gpRq respectively; see Figure 4. As for γ3, we can use the hypothesis of small
Lipschitz constant to establish the following key fact:

1Similar curves also appear in the arguments of Jerrard [11].

12 TERENCE TAO

Figure 4. Portions of the curves γ1, γ2, γ3, γ4, Graphf , and Graphg.
(In some cases, γ1, γ2, γ4 may lie on the enlargements Graph ˜f , Graph˜g of
Graphf , Graphg, which are not shown here.)

Proposition 3.8. The curve γ3 : rt0, t1s Ñ R2 is simple.

Proof. Suppose for contradiction that t, t
1 P rt0, t1s are distinct points such that γ3ptq “
γ3pt
1q. Then if one rotates the curve Graph ˜f clockwise by π{2 around γ3ptq “ γ3pt
1q,
the rotated curve will intersect Graph˜g at the two distinct points γ2ptq and γ2pt
1q (see
Figure 4). As ˜g is 1 ´ ε-Lipschitz, we conclude that the line segment connecting these
two points has slope of magnitude at most 1 ´ ε with respect to the x-axis; as ˜f is also
1´ε-Lipschitz, we similarly conclude that the same line segment has slope of magnitude
at most 1 ´ ε with respect to the y-axis. The two claims are inconsistent, giving the
required contradiction. □

When t “ t0 or t “ t1, we have paptq, bptqq “ p0, 0q as the unique ﬁxed point of (3.5).
Applying Lemma 3.5, we conclude the identity

ż
γ1 y dx ´ ż

γ2 y dx ` ż

γ3 y dx ´ ż

γ4 y dx “ 0. (3.13)

By (3.10) and Example 3.3 we have

ż

γ1 y dx “ ż t1

t0 f ptq dt. (3.14)

INTEGRATION APPROACH TO SQUARE PEG PROBLEM 13

From (3.11) and a change of variables2 ˜t :“ t ` aptq we also have
ż

γ2 y dx “ ż t1

t0 f ptq dt; (3.15)

note that t`aptq may be temporarily decreasing instead of increasing as t increases from
t0 to t1, but the net contributions of such excursions cancel out (by the fundamental
theorem of calculus, or equivalently because 1-forms on a line are automatically exact).
Similarly, from (3.12) and the change of variables ˜t :“ t ´ bptq we have
ż

γ4 y dx “ ż t1

t0 gptq dt. (3.16)

Thus from (3.13) we must have ż

γ3 y dx “ ż t1

t0 gptq dt

or equivalently ż

γ3`p´Graphgq y dx “ 0

where γ3 ` p´Graphgq denotes the concatenation of γ3 with the reversal of the graph
Graphg. This is a closed curve, hence by Lemma 3.4 this curve cannot be simple. Since
γ3 and Graphg are separately simple (the former thanks to Proposition 3.8), we conclude
that there exists t0 ă t, t
1 ă t1 such that

γ3ptq “ Graphgpt
1q.

In particular, γ1ptq, γ2ptq, γ3ptq, γ4ptq all lie in the set Graph ˜f YGraph˜g. Since ˜gptq ą ˜f ptq,
we see from (3.5) that aptq and bptq cannot both vanish; thus pγ1ptq, γ2ptq, γ3ptq, γ4ptqq
lie in Squares. Now we claim that all four vertices of this square in fact lie in the set
(1.1). Indeed, suppose for contradiction that one of the vertices, call it v, was outside
of (1.1), then it lies on the ray tpt, f pt0qq : t ă t0u or on the ray tpt, f pt1qq : t ą t1u.
But in either case, the set Graph ˜f Y Graph˜gztvu is contained in the open double sector
v `tpx, yq : |y| ă |x|u, and hence Graph ˜f YGraph˜g cannot inscribe any square containing
v as a vertex (as one cannot subtend a right angle at v). This implies that the set (1.1)
inscribes a square as required, and Theorem 1.2 follows.

Remark 3.9. It is instructive to compare the above argument with the following homo-
logical argument, which requires additional regularity hypotheses on f, g at the bound-
ary points t0, t1. Namely, suppose in addition to the hypotheses of Theorem 1.2 that f, g
are diﬀerentiable at t0, t1 with g1pt0q ą f 1pt0q and g1pt1q ă f 1pt1q; this corresponds the
curve (1.1) being “locally monotone” in the sense of [24] or [28], even at the endpoints
Graphf pt0q “ Graphgpt0q and Graphf pt1q “ Graphgpt1q. A local analysis then reveals
that the curve t ÞÑ γ3ptq deﬁned above lies in the interior of (1.1) for t close to t0, and
in the exterior of (1.1) for t close to t1, and so it must cross (1.1) at some point; indeed,
if all intersections were transversal, then it must cross this curve an odd number of
times. (Actually, it is not diﬃcult to use the Lipschitz hypotheses to show that this

2This change of variables is easy to justify if the map t ÞÑ t ` aptq is piecewise linear, and the
general case follows by an approximation argument (noting that all functions involved are Lipschitz
continuous).

14 TERENCE TAO

curve can only cross Graphg and not Graphf .) In contrast, the integral argument based
on the conserved integral (3.3) does not give any information on the parity of crossings
(indeed, if f, g are not diﬀerentiable at the endpoints, one could conceivably have an
inﬁnite number of transverse crossings near the endpoints Graphf pt0q “ Graphgpt0q and
Graphf pt1q “ Graphgpt1q), but do not require the functions f, g to be so regular at the
endpoints t0, t1 that a local analysis is possible there.

Remark 3.10. The following observations are due to Benjamin Matschke (private com-
muncation). The above arguments can be generalised to show that for any ﬁxed s, r ą 0,
and with f, g as in Theorem 1.2 but with the Lipschitz constant 1 ´ ε replaced by
tanpα{2q ´ ε with α :“ arctanpr{sq P p0, πs, the set Graphf Y Graphs inscribes a quadru-
ple similar to the equilateral trapezoid

p0, 0q, p1, 0q, ps ` 1, rq, p´s, rq

or equivalently a quadruple of the form

px, yq, px ` a, y ` bq, px ` ps ` 1qa ´ rb, y ` ps ` 1qb ` raq, px ` p´sqa ´ rb, y ` p´sqb ` raq.

Theorem 1.2 corresponds to the endpoint case s “ 0, r “ 1 of this more general claim.
Indeed, by repeating the above arguments one can ﬁnd Lipschitz curves γ1, γ2, γ3, γ4 : rt0, t1s Ñ
R
2 of the form
 γ1ptq “ pt, ˜f ptqq

γ2ptq “ pt ` aptq, ˜f ptq ` bptqq

γ3ptq “ pt ` ps ` 1qaptq ´ rbptq, y ` ps ` 1qbptq ` raptqq

γ4ptq “ pt ` p´sqaptq ´ rbptq, y ` p´sqbptq ` raptqq

for some Lipschitz functions a, b, ˜f : rt0, t1s Ñ R obeying (3.10), (3.11), (3.12), then one
can again verify that γ3 is simple, and a variant of the calculation used to prove Lemma
3.5 establishes the identity

p2s`1q ż

γ1 y dx´p2s`1q ż

γ2 y dx`ż

γ3 y dx´
ż
γ4 y dx “ rp2s ` 1q
2
 `papt1q
2 ´ bpt1q
2q ´ papt0q
2 ´ bpt0q
2q˘

and one can then conclude the claim by repeating the remaining arguments of this
section; we leave the details to the interested reader. On the other hand, when the
equilateral trapezoid is not a rectangle or square, the known homological arguments do
not seem to force the existence of an inscribed copy of the trapezoid even when the curve
is smooth, because there are no symmetry reductions available to make the number of
inscribed copies odd rather than even.

4. Periodic variants of the square peg problem

We now discuss periodic versions of the square peg problem, in which the plane R
2 is
replaced by the cylinder
 CylL :“ pR{LZq ˆ R

INTEGRATION APPROACH TO SQUARE PEG PROBLEM 15

for some ﬁxed period
3 L ą 0. There is an obvious projection map πL : R
2 Ñ CylL
from the plane to the cylinder, which induces a projection π‘4
L : pR
2q4 Ñ Cyl
4
L; we
let SquaresL and SquaresL be the images of Squares and Squares under this latter
projection. More explicitly, we have

SquaresL :“ tppx, yq, px ` a, y ` bq, px ` a ´ b, y ` a ` bq, px ´ b, y ` aqq :

x P R{LZ; y, a, b P R; pa, bq ‰ p0, 0qu

and

SquaresL :“ tppx, yq, px`a, y`bq, px`a´b, y`a`bq, px´b, y`aqq : x P R{LZ; y, a, b P Ru,

where we deﬁne the sum x ` a of an element x P R{LZ and a real number a P R in
the obvious fashion. Again note that SquaresL is an oriented 4-manifold in Cyl
4
L. As
before, a subset Γ of CylL is said to inscribe a square if Γ4 intersects SquaresL. We give
CylL and Cyl
4
L the usual ﬂat Riemannian metric, which is then inherited by SquaresL
and SquaresL.

We have a standard closed curve Graph0,L : R{LZ Ñ CylL in CylL deﬁned by

Graph0,Lptq :“ pt, 0q;

one can think of Graph0,L homologically as a 1-cycle generating the ﬁrst homology of
CylL. Any other closed curve γ : R{LZ Ñ CylL will be homologous to Graph0,L if and
only if it takes the form γpt mod Lq “ πLp˜γptqq
for some continuous lift ˜γ : R Ñ R
2 of γ that is LZ-equivariant in the sense that

˜γpt ` Lq “ ˜γptq ` pL, 0q (4.1)

for all t P R.

Amongst all the curves γ in CylL, we isolate the polygonal curves, in which γ is piecewise
linear (possibly after reparameterisation), that is to say γ is the concatenation of ﬁnitely
many line segments in CylL.

We now introduce the following variant of Conjecture 1.1.

Conjecture 4.1 (Periodic square peg problem). Let L ą 0, and let σ1, σ2 : R{LZ Ñ
CylL be simple curves in CylL homologous to Graph0,L. Suppose also that the sets
σ1pR{LZq and σ2pR{LZq are disjoint. Then σ1pR{LZq Y σ2pR{LZq inscribes a square.

In contrast to Conjecture 1.1, we do not know the answer to Conjecture 4.1 even when
σ1, σ2 are smooth or piecewise polygonal (and we in fact suspect that resolving this case
would soon resolve Conjecture 4.1 in full generality, in analogy to Corollary 5.5 below).
This is because the intersection numbers produced by homological arguments become
even in the periodic setting, rather than odd. Of course, by rescaling we could normalise
L “ 1 without loss of generality in Conjecture 4.1 if desired, but we ﬁnd it preferable
to not enforce this normalisation.

3One could easily normalise L to be 1 if desired, but we will ﬁnd it convenient to allow L to be a
parameter at our disposal.

16 TERENCE TAO

We are able to relate Conjecture 1.1 to a special case of Conjecture 4.1. To state this
special case, we need a further deﬁnition:

Deﬁnition 4.2 (Inﬁnitesimally inscribed squares). Let L ą 0. A closed subset Γ of
CylL is said to inscribe inﬁnitesimal squares if there exists a sequence of squares

Sn “ ppxn, ynq, pxn ` an, yn ` bnq, pxn ` an ´ bn, yn ` an ` bnq, pxn ´ bn, yn ` anqq (4.2)

in SquaresL converging to a degenerate square ppx, yq, px, yq, px, yq, px, yqq for some
px, yq P Γ, such that distpSn, Γ
4q “ op|an| ` |bn|q
as n Ñ 8.

Note that the property of inﬁnitesimally inscribing squares is a purely local property:
to show that a set Γ does not inﬁnitesimally inscribe squares, it suﬃces to show that
for every p P Γ, there is a set Γp that agrees with Γ in a neighbourhood of p that does
not inﬁnitesimally inscribe squares.

We now give two examples of sets with the property of not inscribing inﬁnitesimal
squares.

Lemma 4.3. Let f1, . . . , fk : R{LZ Ñ R be C-Lipschitz functions for some C ă tan 3π
8 “
1 ` ?
2, such that the graphs GraphfipR{LZq for i “ 1, . . . , k are all disjoint. Then the
set Ťk
i“1 GraphfipR{LZq does not inscribe inﬁnitesimal squares.

Proof. By the local nature of inﬁnitesimally inscribing squares, it suﬃces to show that
each GraphfipR{LZq does not inﬁnitesimally inscribe squares. Suppose for contradiction
that there was some i “ 1, . . . , k and a sequence of squares (4.2) with pxn, ynq Ñ
px, yq P GraphfipR{LZq, pan, bnq Ñ p0, 0q, and all vertices staying within op|an| ` |bn|q
of GraphfipR{LZq. As fi is C-Lipschitz continuous, this implies that the eight points
˘pan, bnq, ˘p´bn, anq, ˘pan ´ bn, an ` bnq, ˘pan ` bn, an ´ bnq all lie in the double sector
tpt, uq : |u| ď pC ` op1qq|t|u. However, the arguments of these eight points (viewed as
complex numbers) form a coset of the eighth roots of unity, while the double sector
omits all the complex numbers of argument in r 3π
8 , 5π
8 s if n is large enough; but these
two facts are in contradiction. □

Remark 4.4. If one rotates the standard unit square r0, 1s
2 by π
8 , one obtains a square
with the property that all its sides and diagonals have slope between ´ tan 3π
8 and tan 3π
8 ;
in particular, the vertices of this square can be traversed by the graph of a tan 3π
8 -
Lipschitz function. Gluing together inﬁnitely many rescaled copies of this function, it is
not diﬃcult to show that the condition C ă tan 3π
8 in Lemma 4.3 cannot be improved.

Lemma 4.5. Let Γ1, . . . , Γk be disjoint simple polygonal paths in R
2 (either open or
closed). Then Γ1 Y ¨ ¨ ¨ Y Γk does not inﬁnitesimally inscribe squares.

Proof. Again it suﬃces to verify that a single Γi does not inscribe squares. Suppose for
contradiction that there was a sequence of squares with vertices (4.2) with pxn, ynq Ñ
px, yq P Γi, pan, bnq Ñ p0, 0q, and all vertices staying within op|an| ` |bn|q of Γi.

INTEGRATION APPROACH TO SQUARE PEG PROBLEM 17

We can translate so that px, yq “ p0, 0q. The origin p0, 0q is either a vertex on the path
Γi or an interior point of an edge. Suppose ﬁrst that p0, 0q is an interior point of an
edge, which then lies on some line ℓ. Then for n large enough, all four vertices (4.2) stay
within op|an| ` |bn|q of this line. Applying a suitable translation and rescaling, we can
then obtain another family of squares of unit length, whose vertices (4.2) are bounded
and stay within op1q of ℓ. Using compactness to extract a limit, we obtain a unit square
with all four vertices on ℓ, which is absurd.

Now suppose that p0, 0q is a vertex of Γi, which we may take to be the origin. This
origin is the meeting point of two edges of Γi that lie on two distinct lines ℓ1, ℓ2 passing
through the origin. If (after passing through a subsequence) all four vertices (4.2) lie
within op|an| ` |bn|q of ℓ1, then by rescaling and taking limits as before we obtain a
unit square with all four vertices on ℓ1, which is absurd; similarly if all four vertices lie
within op|an| ` |bn|q of ℓ2. Thus we must have at least one vertex within op|an| ` |bn|q
of ℓ1 and another within op|an| ` |bn|q of ℓ2, which forces the entire square to lie within
Op|an| ` |bn|q of the origin. Rescaling and taking limits again, we now obtain a unit
square with all four vertices on the union ℓ1 Y ℓ2 of the two intersecting lines ℓ1, ℓ2,
which is again absurd regardless of what angle ℓ1 and ℓ2 make with each other. □

For an example of a curve that does inﬁnitesimally inscribe squares, one can consider
any curve that has the local behaviour of a cusp such as tpt
2, t
3q : t P Ru.

We now isolate a special case of Conjecture 4.1:

Conjecture 4.6 (Periodic square peg problem, special case). Conjecture 4.1 is true
under the additional hypothesis that σ1pR{LZqYσ2pR{LZq does not inscribe inﬁnitesimal
squares.

The main result of this section is then

Proposition 4.7. Conjecture 1.1 implies Conjecture 4.6. In particular (by Lemma
4.5), Conjecture 1.1 implies the special case of Conjecture 4.1 when the curves σ1, σ2
are polygonal paths.

To put it another way, if one wished to disprove Conjecture 1.1, it would suﬃce to
produce a union σ1pRq Y σ2pRq of two disjoint periodic curves which did not inscribe
any squares or inﬁnitesimal squares.

Proposition 4.7 is an immediate consequences of the following proposition:

Proposition 4.8 (Transforming periodic sets to bounded sets). Let Γ be a compact
subset of CylL for some L ą 0, and let π´1
L pΓq be its lift to R2. For every large natural

18 TERENCE TAO

number n, let φn : R2 Ñ R
2 denote the map4

φnpx, yq :“ ´
n tanh x
n, y sech
2 x
n
¯ .

Then at least one of the following three statements hold.

(i) Γ inscribes a square.
(ii) Γ inscribes inﬁnitesimal squares.
(iii) For suﬃciently large n, φnpπ´1
L pΓqq Y tp´n, 0q, pn, 0qu does not inscribe a square.

Indeed, to establish Conjecture 4.6 assuming Conjecture 1.1, one simply applies Propo-
sition 4.8 to the set Γ :“ σ1pR{LZq Y σ2pR{LZq; the conclusion (ii) is ruled out by
hypothesis and the conclusion (iii) is ruled out by Conjecture 1.1, leaving (i) as the only
possible option.

Proof. We will assume that (iii) fails and conclude that either (i) or (ii) holds.

By hypothesis, we can ﬁnd a sequence of n going to inﬁnity, and a sequence of squares
with vertices (4.2), such that each square (4.2) is inscribed in φnpπ´1
L pΓqq. The plan is
to transform these squares into squares that either converge to a square inscribed in Γ,
or become an inﬁnitesimal inscribed square in Γ.

We ﬁrst rule out a degenerate case when one of the points p´n, 0q, pn, 0q is one of the
vertices (4.2). Suppose for instance that pxn, ynq was equal to pn, 0q. Since Γ is compact,
we see that π´1
L pΓq is contained in a strip of the form

tpx, yq : y “ Op1qu.

Using the identity
 sech
2pxq “ 1 ´ tanh
2pxq “ Op1 ´ | tanhpxq|q,

we conclude that φnpπ´1
L pΓqq is contained in the region
"
px, yq : ´n ă x ă n; y “ O ˆ1 ´ |x|
n
 ˙* . (4.3)

If pxn, ynq “ pn, 0q and the remaining three vertices of (4.2) lie in φnpπ´1
L pΓqq, this forces
p´an, ´bnq, p´an ` bn, ´an ´ bnq, pbn, ´anq to all have argument Op1{nq when viewed as
complex numbers, which is absurd for n large enough, since these arguments diﬀer by π
4
or π
2 . Thus we have pxn, ynq ‰ pn, 0q (after passing to a subsequence of n if necessary);
a similar argument precludes any of the vertices in (4.2) being equal to p´n, 0q or pn, 0q.

At least one of the four vertices in (4.2) must have a y-coordinate of magnitude at least
|an|`|bn|
2 , since two of these y-coordinates diﬀer by an ` bn and the other two diﬀer by

4One can view this map as an approximation to the conformal map z ÞÑ n tanh z
n in the complex
plane, which “gently pinches” the periodic set π´1
L pΓq to a bounded set in a manner that almost
preserves squares. The use of trigonometric functions here is primarily for notational convenience; one
could also use other maps than φn here as long as they obeyed the above-mentioned qualitative features
of approximate conformality and mapping periodic sets to bounded sets.

INTEGRATION APPROACH TO SQUARE PEG PROBLEM 19

an ´ bn. Applying (4.3), we conclude that the x-coordinate of that vertex lies at a
distance at least cn|an| ` |bn| from p´n, 0q, pn, 0q for some c ą 0 independent of n; by
the triangle inequality, we conclude (for n large enough) that all four vertices have this
property. In particular, we have

|an| ` |bn| “ O ˆ1 ´ |xn|
n
 ˙ .

Observe that in the region (4.3), we may invert φn by the formula

φ
´1
n px, yq :“ ˆ n
2 log n ` x
n ´ x , y
1 ´ x2{n2
 ˙ .

On (4.3), we can compute the partial derivatives

B
Bxφ´1
n px, yq “ ˆ 1
1 ´ x2{n2 , 2x
n2 y
p1 ´ x2{n2q2
 ˙

“ 1
1 ´ x2{n2
 ˆ1, O ˆ 1
n
˙˙

and B
By φ
´1
n px, yq “ ˆ0, 1
1 ´ x2{n2
 ˙

and so by Taylor expansion we see that

φ
´1pxn ` an, yn ` bnq “ φ
´1pxn, ynq ` pan, bnq
1 ´ x2
n{n2 ` O ˆ |an| ` |bn|
np1 ´ x2
n{n2q
 ˙

φ
´1pxn ` an ´ bn, yn ` an ` bnq “ φ
´1pxn, ynq ` pan ´ bn, an ` bnq
1 ´ x2
n{n2 ` O ˆ |an| ` |bn|
np1 ´ x2
n{n2q
˙

φ
´1pxn ´ bn, yn ` anq “ φ
´1pxn, ynq ` p´bn, anq
1 ´ x2
n{n2 ` O ˆ |an| ` |bn|
np1 ´ x2
n{n2q
 ˙ .

Thus, if we set p˜xn, ˜ynq :“ πLpφ
´1pxn, ynqq and p˜an, ˜bnq :“ pan,bnq
1´x2
n{n2 , we see that ˜an, ˜bn “
Op1q, and the four vertices of the square

pp˜xn, ˜ynq, p˜xn ` ˜an, ˜yn ` ˜bnq, p˜xn ` ˜an ´ ˜bn, ˜yn ` ˜an ` ˜bnq, p˜xn ´ ˜bn, ˜yn ` ˜anqq P SquaresL
all lie within Op|˜an| ` |˜bn|{nq of Γ.

By passing to a subsequence, we may assume that p˜an, ˜bnq converges to some pair pa, bq,
which may possibly be equal to p0, 0q. By compactness of Γ, we may similarly assume
that p˜xn, ˜ynq converges to a limit px, yq P Γ. If pa, bq ‰ p0, 0q, then on taking limits using
the closed nature of Γ we conclude that the non-degenerate square

ppx, yq, px ` a, y ` bq, px ` a ´ b, y ` a ` bq, px ´ b, y ` aqq P SquaresL
is inscribed in Γ, giving (i); if instead pa, bq “ p0, 0q then we obtain (ii). □

Remark 4.9. In contrast to the smooth cases of Conjecture 1.1, there are no ho-
mological obstructions to establishing a counterexample to Conjecture 4.1. For in-
stance, when the Lipschitz constants of f, g are strictly less than one, the arguments
of the previous section can be used to produce a quadruplet pγ1, γ2, γ3, γ4q of rectiﬁable
curves γ1, γ2, γ3, γ4 : R{LZ Ñ CylL traversing squares, with γ1, γ2, γ4 taking values in

20 TERENCE TAO

Graphf pR{LZq, Graphf pR{LZq, GraphgpR{LZq respectively, and all four curves homol-
ogous to the standard 1-cycle Graph0,L. In particular, γ3 would (assuming suﬃcient
transversality and regularity) intersect the graphs Graphf pR{LZq and GraphgpR{LZq
an even number of times per unit period, rather than an odd number of times. This is
of course consistent with the curve not intersecting these graphs at all. The use of an
inﬁnite oscillation to switch the parity of intersection from odd to even is reminsicent
of the “Eilenberg-Mazur swindle” (see e.g. [27]).

5. A quadripartite variant

In Conjecture 4.1, the four vertices of the square could be distributed arbitrarily among
the two graphs Graphf pR{LZq and GraphgpR{LZq. It seems to be more natural to force
each vertex to lie in just one of the two graphs. To formulate this more precisely, we
introduce a further deﬁnition:

Deﬁnition 5.1 (Jointly inscribing squares). Let L ą 0. Let Γ1, Γ2, Γ3, Γ4 be four sets in
CylL (possibly overlapping). We say that the quadruplet pΓ1, Γ2, Γ3, Γ4q jointly inscribes
a square if Γ1 ˆ Γ2 ˆ Γ3 ˆ Γ4 intersects SquaresL, or equivalently if there exist x P R{LZ
and y, a, b P R such that
 px, yq P Γ1
px ` a, y ` bq P Γ2
px ` a ´ b, y ` a ` bq P Γ3
px ´ b, y ` aq P Γ4.

See Figure 5.

Note in Deﬁnition 5.1 that we now permit the inscribed square to be degenerate. Con-
jecture 4.1 would then follow from

Conjecture 5.2 (Quadripartite periodic square peg problem). Let L ą 0, and let
σ1, σ2 : R{LZ Ñ CylL be simple closed curves homologous to Graph0,L. Then the quadru-
plet pσ1pR{LZq, σ1pR{LZq, σ2pR{LZq, σ2pR{LZqq

jointly inscribes a square.

Indeed, if σ1, σ2 are as in Conjecture 4.1, we can apply Conjecture 5.2 to obtain x P R{LZ
and y, a, b P R with px, yq, px`a, y`bq P σ1pR{LZq and px`a´b, y`a`bq, px´b, y`aq P
σ2pR{LZq. As σ1pR{LZq and σ2pR{LZq are assumed disjoint in Conjecture 4.1, we have
pa, bq ‰ p0, 0q, and Conjecture 4.1 follows.

We can reverse this implication in some cases:

Proposition 5.3. Conjecture 4.1 implies Conjecture 5.2 in the special case that σipR{LZq
does not inscribe squares for i “ 1, 2.

INTEGRATION APPROACH TO SQUARE PEG PROBLEM 21

Figure 5. Four line segments pΓ1, Γ2, Γ3, Γ4q jointly inscribing a square.
The order (up to cyclic permutation) is important; for instance, in the
given picture, the quadruple pΓ1, Γ4, Γ3, Γ2q does not jointly inscribe a
square.

Note that the hypothesis that σipR{LZq does not inscribe squares is satisﬁed in many
cases; for instance, by modifying the proof of Lemma 4.3 we see that this is the the case
if σi is the graph of a C-Lipschitz function for some C ă tan 3π
8 .

Proof. Let σ1, σ2 be as in Conjecture 5.2, and assume that σ1pR{LZq and σ2pR{LZq
do not separately inscribe squares. Let m be a suﬃciently large natural number, then
σ1pR{LZq and σ2pR{LZq ` p0, mLq will be disjoint. Applying Conjecture 4.1, we may
ﬁnd a square

ppx, yq, px ` a, y ` bq, px ` a ´ b, y ` a ` bq, px ´ b, y ` aqq P SquaresL
inscribed in σ1pR{LZq Y pσ2pR{LZq ` p0, mLqq. In particular we have

y, y ` b, y ` a ` b, y ` a P r´C, Cs Y rmL ´ C, mL ` Cs

for some C ą 0 independent of m. If m is large enough, this forces the quadruple py, y `
b, y`a`b, y`aq to be of the form pOpCq, OpCq, OpCq, OpCqq, the form pmL`OpCq, mL`
OpCq, mL ` OpCq, mL ` OpCqq, or some cyclic permutation of pOpCq, OpCq, mL `

22 TERENCE TAO

OpCq, mL ` OpCqq. In the ﬁrst case, we have a square inscribed in σ1pR{LZq, and in
the second case we have (after translation by p0, mLq) a square inscribed by σ2pR{LZq;
both these cases are ruled out by hypothesis. Thus, after cyclic permutation, we may
assume that

py, y ` b, y ` a ` b, y ` aq “ pOpCq, OpCq, mL ` OpCq, mL ` OpCqq

which implies that the (possibly degenerate) square

ppx, yq, px ` a ´ mL, y ` bq, px ` a ´ b ´ mL, y ` a ` bq, px ´ b, y ` a ´ mLqq P SquaresL
is jointly inscribed by pσ1pR{LZq, σ1pR{LZq, σ2pR{LZq, σ2pR{LZqq, giving Conjecture
5.2 in this case. □

Because the squares in Deﬁnition 5.1 are now permitted to be degenerate, Conjecture
5.2 enjoys good convergence properties with respect to limits:

Proposition 5.4 (Stability of not jointly inscribing squares). Let L ą 0. Let σ1,n, σ2,n : R{LZ Ñ
CylL be sequences of simple closed curves which converge uniformly to simple closed
curves σ1, σ2 : R{LZ Ñ CylL respectively as n Ñ 8. If each of the quadruples

pσ1,npR{LZq, σ1,npR{LZq, σ2,npR{LZq, σ2,npR{LZqq

jointly inscribe a square, then so does

pσ1pR{LZq, σ1pR{LZq, σ2pR{LZq, σ2pR{LZqq.

It is possible to weaken the requirement of uniform convergence (for instance, one can
just assume pointwise convergence if the curves σ1,n, σ2,n are uniformly bounded), but
we will not need to do so here.

Proof. By hypothesis, one can ﬁnd a sequence pn P SquaresL such that pn P σ1,npR{LZqˆ
σ1,npR{LZq ˆ σ2,npR{LZq ˆ σ2,npR{LZq for all n. As σ1,n, σ2,n converge uniformly to
σ1, σ2, the pn are bounded and thus have at least one limit point p, which must lie in
both SquaresL and σ1pR{LZqˆσ1pR{LZqˆσ2pR{LZqˆσ2pR{LZq, giving the claim. □

As one application of this proposition, we have

Corollary 5.5. In order to prove Conjecture 5.2, it suﬃces to do so in the case that
the simple closed curves σ1, σ2 : R{LZ Ñ CylL are polygonal paths.

This can be compared with the situation with Conjecture 1.1, which is known to be
true for polygonal paths, but for which one cannot take limits to conclude the general
case, due to the possibility of the inscribed squares degenerating to zero.

Proof. By Proposition 5.4, it suﬃces to show that any simple closed curve γ : R{LZ Ñ
CylL can be uniformly approximated to any desired accuracy Opεq for ε ą 0 by a simple
polygonal closed curve ˜γ : R{LZ Ñ CylL (note from a winding number argument that
if γ is homologous to Graph0,L, then ˜γ will be also if ε is small enough). By uniform
continuity, there exists a natural number N such that dCylLpγptq, γpt
1qq ď ε whenever

INTEGRATION APPROACH TO SQUARE PEG PROBLEM 23

dR{LZpt, t
1q ď L{N , where dCylL, dR{LZ denote the Riemannian distance functions on
CylL, R{LZ respectively; as γ is simple and continuous, a compactness argument shows
that there also exists 0 ă δ ă ε such that dCylLpγptq, γpt
1qq ą 4δ whenever dR{LZpt, t
1q ě
L{N . Finally, by uniform continuity again, there exists a natural number M ě N such
that dCylLpγptq, γpt
1qq ď δ whenever dR{LZpt, t
1q ď L{M .

Let γ1 : R{LZ Ñ R
2 be the polygonal path such that γ1pjL{M q :“ γpjL{M q for every
j P Z{M Z, with γ1 linear on each interval jL{M `r0, 1{M s. From the triangle inequality
we see that dCylLpγ1ptq, γptqq ď 2δ for all t P R. Unfortunately, γ1 need not be simple.
However, if t, t
1 are such that γ1ptq “ γ1pt
1q, then by the triangle inequality we have
dCylLpγptq, γpt
1qq ď 4δ, and hence dR{LZpt, t
1q ď L{N . Using a greedy algorithm to
iteratively remove loops from the polygonal path γ1 (with each removal decreasing the
number of edges remaining in γ1 in a unit period), we may thus ﬁnd a ﬁnite family
I1, . . . , Ik of disjoint closed intervals in R{LZ, each of length at most L{N , such that
paths γ1|Ij : Ij Ñ CylL is closed for each 1 ď j ď k (i.e. γ1 evaluates to the same point
at the left and right endpoints of Ij), and such that γ1 becomes simple once each of the
intervals Ij is contracted to a point. Note also that all of the loops of γ1 removed by
this process have diameter Opεq. If one then chooses a suﬃciently small neighbourhood
interval ˜Ij for each Ij, and deﬁnes ˜γ to equal γ1 outside Ťk
j“1 ˜Ij, and linear on each of
the ˜Ij, then we see that ˜γ is a simple LZ-equivariant polygonal path that lies within
Opεq of γ, as required. □

We in fact believe the following stronger claim than Conjecture 5.2 to hold:

Conjecture 5.6 (Area inequality). Let L ą 0, and let σ1, σ2, σ3, σ4 : R{LZ Ñ CylL be
simple closed polygonal paths homologous to Graph0,L. If pσ1pR{LZq, σ2pR{LZq, σ3pR{LZq, σ4pR{LZqq
does not jointly inscribe a square, then
ż

σ1 y dx ´ ż

σ2 y dx ` ż

σ3 y dx ´ ż

σ4 y dx ‰ 0. (5.1)

Note that the 1-form y dx is well deﬁned on CylL and σ1, σ2, σ3, σ4 can be viewed as
1-cycles, so the integrals in (5.1) make sense as integration of diﬀerential forms (but one
could also use Deﬁnition 3.2 with the obvious modiﬁcations if desired). One can also
simplify the left-hand side of (5.1) as
ż
σ1´σ2`σ3´σ4 y dx (5.2)

where σ1 ´ σ2 ` σ3 ´ σ4 is interpreted as a 1-cycle. Viewed contrapositively, Conjecture
5.6 then asserts that pσ1pR{LZq, σ2pR{LZq, σ3pR{LZq, σ4pR{LZqq must inscribe a square
whenever the integral (5.2) vanishes.

Clearly, Conjecture 5.2 follows from Conjecture 5.6 by ﬁrst using Corollary 5.5 to reduce
to the case where σ1, σ2 are polygonal paths, and then applying Conjecture 5.6 with
pσ1, σ2, σ3, σ4q replaced by pσ1, σ1, σ2, σ2q.

Conjecture 5.6 is somewhat strong compared with the other conjectures in this paper.
Nevertheless, we can repeat the arguments in Section 3 to obtain some evidence for it:

24 TERENCE TAO

Theorem 5.7. Conjecture 5.6 holds when σ2 “ Graphf2 and σ4 “ Graphf4 for some
p1 ´ εq-Lipschitz functions f2, f4 : R{LZ Ñ CylL and some ε ą 0.

Of course, by cyclic permutation one can replace the role of σ2, σ4 here by σ1, σ3.

Proof. Write σ1ptq :“ px1ptq, y1ptqq. For any t P R{LZ, the map

pa, bq ÞÑ pf4px1ptq ´ bq ´ y1ptq, f2px1ptq ` aq ´ y1ptqq

is a contraction on R
2 with constant at most 1 ´ ε, hence by the contraction mapping
theorem there exist unique continuous functions a, b : R{LZ Ñ R such that

paptq, bptqq “ pf4px1ptq ´ bptqq ´ y1ptq, f2px1ptq ` aptqq ´ y1ptqq

for all t P R{LZ. As σ1, σ2, σ4 are polygonal paths, f2, f4 are piecewise linear functions,
which implies that a, b are also piecewise linear. We then set γ1, γ2, γ3, γ4 : R{LZ Ñ CylL
to be the polygonal paths

γ1ptq :“ σ1ptq

γ2ptq :“ σ1ptq ` paptq, bptqq

“ Graphf2px1ptq ` aptqq

γ3ptq :“ σ1ptq ` paptq ´ bptq, aptq ` bptqq

γ4ptq :“ σ1ptq ` p´bptq, aptqq

“ Graphf4px1ptq ´ bptqq.

Clearly pγ1, γ2, γ3, γ4q traverses squares. Applying Lemma 3.5, we conclude that
ż

γ1 y dx ´ ż

γ2 y dx ` ż

γ3 y dx ´ ż
γ4 y dx “ 0.

Since t ÞÑ Graphf2px1ptq ` aptqq and t ÞÑ Graphf4px1ptq ´ bptqq are homologous to σ2 and
σ4 respectively, and all 1-forms on curves such as Graphf2pR{LZq or Graphf4pR{LZq are
automatically closed, we have ş

γi y dx “ ş

σi y dx for i “ 1, 2, 4. Thus it suﬃces to show
that ż

γ3´σ3 y dx ‰ 0. (5.3)

The argument in Proposition 3.8 (unwrapping the curves from CylL to R
2) shows
that γ3 is simple, and the graph σ3 is of course also simple. As we are assuming
pσ1pR{LZq, σ2pR{LZq, σ3pR{LZq, σ4pR{LZqq to not jointly inscribe squares, γ3pR{LZq
and σ3pR{LZq must stay disjoint. The curve γ3 is homotopic to σ1 and thus also homol-
ogous to Graph0,L. Applying the Jordan curve theorem, we see that the closed polygonal
paths γ3, σ3 enclose some non-empty polygonal region Ω in CylL. By Stokes’ theorem,
we conclude that the left-hand side of (5.3) is equal to some sign times the Lebesgue
measure of Ω, giving (5.3) as required. □

We also have an analogue of Corollary 5.5:

INTEGRATION APPROACH TO SQUARE PEG PROBLEM 25

Proposition 5.8 (Stability of area inequality). Let L ą 0. Suppose that σ1,n, σ2,n, σ3,n, σ4,n : R{LZ Ñ
CylL are simple closed polygonal paths which converge uniformly to simple closed polyg-
onal paths σ1, σ2, σ3, σ4 : R{LZ Ñ CylL respectively. If, for all suﬃciently small h P R
Conjecture 5.6 holds for each of the quadruples pσ1,n, σ2,n, σ3,n, σ4,n`p0, hqq for all n ě 1,
then it also holds for pσ1, σ2, σ3, σ4q.

This proposition will be useful for placing the polygonal paths σ1, σ2, σ3, σ4 in “general
position”.

Proof. We can of course assume that pσ1pR{LZq, σ2pR{LZq, σ3pR{LZq, σ4pR{LZqq does
not jointly inscribe a square, as the claim is trivial otherwise. By Proposition 5.4
applied in the contrapositive, we see that there exists an ε ą 0 and N ě 1 such that
pσ1,npR{LZq, σ1,npR{LZq, σ1,npR{LZq, σ1,npRq ` p0, hqq does not jointly inscribe squares
for any |h| ď ε and n ě N . Applying the hypothesis (and shrinking ε if necessary), we
conclude that ż

σ1,n´σ2,n`σ3,n´σ4,n y dx ´ Lh ‰ 0

for n ě N and |y| ď ε, and hence
ˇ
ˇ
ˇ
ˇ
ˇ
ż

σ1,n´σ2,n`σ3,n´σ4,n y dx
ˇ
ˇ
ˇ
ˇ
ˇ ě Lε;

taking limits as n Ñ 8 we conclude that
ˇ
ˇ
ˇ
ˇ
ż

σ1´σ2`σ3´σ4 y dxˇ
ˇ
ˇ
ˇ ě Lε

giving the claim. □

In the remainder of this section, we discuss how to interpret
5 the area inequality
conjecture (Conjecture 5.6) using the language of homology. Let L ą 0, and let
σ1, σ2, σ3, σ4 : R{LZ Ñ CylL be simple closed polygonal paths. We say that σ1, . . . , σ4
are in general position if the following hold for any distinct i, j, k P t1, 2, 3, 4u:

(i) For any edge e of σi and any edge f of σj, the angle between the direction of e
and the direction of f is not an integer multiple of π
4 .
(ii) For any vertices u, v, w of σi, σj, σk respectively, there does not exist a square
with u, v, w as three of its four vertices.

It is easy to see that one can perturb σ1, σ2, σ3, σ4 by an arbitrarily small amount to be
in general position (e.g. a random perturbation will almost surely work); furthermore
one can ensure that this general position will persist even after shifting σ4 vertically by
an arbitrary amount. Hence by Proposition 5.8, to prove Conjecture 5.6 it suﬃces to
do so under the hypothesis of general position.

5This discussion is not used elsewhere in the paper and may be safely skipped by the reader if
desired.

26 TERENCE TAO

The Cartesian product σ1 ˆ σ2 ˆ CylL ˆ σ4 can be viewed as a (polyhedral) 5-cycle
in Cyl
4
L; by the hypotheses of general position, this cycle intersects the oriented 4-
manifold SquaresL transversely (and in a compact set), giving rise to a 1-cycle σ124 in
SquaresL. For j “ 1, 2, 3, 4, let πj : SquaresL Ñ CylL be the projection map to the
jth coordinate. Because the 5-cycle σ1 ˆ σ2 ˆ CylL ˆ σ4 is homologous to the 5-cycle
Graph0,L ˆGraph0,L ˆCylL ˆGraph0,L, we see on restricting to SquaresL that the 1-cycle
σ124 is homologous to the 1-cycle

Graph
∆
0,L :“ tpp, p, p, pq : p P Graph0,LpR{LZqu (5.4)

(with the usual orientation), and hence the pushforwards γj :“ pπjq˚σ124 (which are
polygonal 1-cycles on CylL) are homologous to Graph0,L and thus to σj for j “ 1, 2, 3, 4.
For j “ 1, 2, 4, γj takes values in the curve σjpR{LZq; as y dx is closed on that curve,
we thus have ż

σ124 π˚
j py dxq “ ż

pπj q˚σ124 y dx “ ż

σj y dx

for j “ 1, 2, 4. On the other hand, from Remark 3.7 (adapted to the cylinder CylL in
the obvious fashion), the 1-form

π˚
1 py dxq ´ π˚
2 py dxq ` π˚
3 py dxq ´ π˚
4 py dxq (5.5)

is exact on SquaresL, and hence
ż

σ124 π˚
1 py dxq ´ π˚
2 py dxq ` π˚
3 py dxq ´ π˚
4 py dxq “ 0.

Putting all this together, we see that the claim (5.1) can be rewritten as
ż

γ3´σ3 y dx ‰ 0. (5.6)

Meanwhile, the hypothesis that pσ1pR{LZq, σ2pR{LZq, σ3pR{LZq, σ4pR{LZqq do not jointly
inscribe squares is equivalent to the assertion that the 1-cycles γ3 and σ3 are disjoint.

The 4-manifold SquaresL is homeomorphic to R{LZ ˆ R
3, and so its ﬁrst homology
is generated by Graph
∆
0,L. One can decompose the 1-cycle σ124 as an integer linear
combination of ﬁnitely many closed polygonal curves in SquaresL (which are allowed
to intersect each other); as σ124 is homologous to Graph
∆
0,L, one of these curves, call it
σ0
124 : R{LZ Ñ SquaresL, must be homologous to mGraph
∆
0,L for some nonzero integer
m, thus it obeys the equivariance σ0
124pt`Lq “ γ0
124ptq`pmL, 0q. By reversing orientation
we may assume m is positive.

We now lift the cylinder CylL up to the larger cylinder CylmL, which is an m-fold cover
of the original cylinder; one can similarly lift SquaresL to the m-fold cover SquaresmL.
The curves σj : R{LZ Ñ CylL lift to curves ˜σj : R{mLZ Ñ CylmL. The 1-cycle σ124
lifts to a 1-cycle ˜σ124 homologous to Graph
∆
0,mL; meanwhile, the curve σ0
124 lifts to m
copies of a curve ˜σ0
124 homologous to Graph
∆
0,mL (and parameterised by R{mLZ), and
contained (as a set) in ˜σ124. We conclude that ˜σ124 ´ ˜σ0
124 is a 1-boundary, thus

˜σ124 “ ˜σ0
124 ` BU

for some 2-cycle U in SquaresmL. We can then deﬁne curves ˜γ0
j : R{mLZ Ñ CylmL for
j “ 1, 2, 3, 4 by ˜γ0
j :“ πj ˝ ˜σ0
124; these curves are the analogues of the curves γ1, γ2, γ3, γ4

INTEGRATION APPROACH TO SQUARE PEG PROBLEM 27

from Section 3. As the 1-form y dx is closed on the curves σjpR{LZq, as well as their
lifts ˜σjpR{mLZq to CylmL, we have
ż

BU π˚
j py dxq “ ż

Bpπj q˚U y dx “ 0

for j “ 1, 2, 4, while from the exact nature of (5.5) gives
ż

BU π˚
1 py dxq ´ π˚
2 py dxq ` π˚
3 py dxq ´ π˚
4 py dxq “ 0

and hence ż

Bpπ3q˚U y dx “ 0.

Hence one can also express (5.6) as ż
˜γ0
3 ´˜σ3 y dx ‰ 0. (5.7)

The 1-cycle ˜γ0
3 ´ ˜σ3 is homologous to Graph0,mL ´ Graph0,mL “ 0 and thus can be
expressed as a 1-boundary ˜γ0
3 ´ ˜σ3 “ BΩ for some 2-cycle Ω in CylmL. By Stokes’
theorem, (5.7) can now be expressed as

´ ż
Ω dx ^ dy ‰ 0. (5.8)

In the case when the σ2, σ4 were graphs of Lipschitz functions of constant less than 1, the
closed path ˜γ0
3 was necessarily simple (and one could take m “ 1); if pσ1pR{LZq, σ2pR{LZq, σ3pR{LZq, σ4pR{LZqq
did not jointly inscribe squares, then ˜γ0
3 avoided σ3, and so by the Jordan curve theorem
the 2-cycle Ω had a deﬁnite sign which yielded (5.8) and thus (5.7), (5.6), (5.1). Unfor-
tunately, in the general case it is possible for the 2-cycle Ω to contain both positive and
negative components, even after stripping out the 1-boundaries BU from ˜σ124 and work-
ing just with ˜σ0
124. However, from working with numerous examples, it appears to the
author that there is always an imbalance between the positive and negative components
of Ω that leads to the inequality (5.8) and hence to Conjecture 5.6. Unfortunately, the
author was unable to locate an argument to establish this claim rigorously.

Remark 5.9. The Jordan curve theorem does imply that the simple closed curve ˜σ3
partitions the cylinder CylmL into two connected components, the region “above” ˜σ3
(which contains all the points in CylmL with suﬃciently large positive y coordinate)
and the region “below” ˜σ3 (which contains all the points in CylmL with suﬃciently large
negative y coordinate). Suppose that pσ1pR{LZq, σ2pR{LZq, σ3pR{LZq, σ4pR{LZqq does
not jointly inscribe a square, so that γ3 avoids σ3. If we let K denote the connected
component of ˜γ3 (viewed as a subset of CylL) that contains (the image of) ˜γ0
3, then K
must then either lie entirely in the region above ˜σ3 or the region below ˜σ3. We conjecture
that this determines the sign in (5.1) (or (5.6), (5.7), (5.8)). Namely, if K is in the region
above ˜σ3, we conjecture that left-hand side of (5.1) (or (5.6), (5.7), (5.8)) must be strictly
positive, and if K is in the region below ˜σ3, then these left-hand sides must be strictly
negative. An equivalent statement of this is that if ˜γ`
3 , ˜γ´
3 : R{mLZ Ñ CylmL are simple
closed polygonal paths that traverse the upper and lower boundary of K respectively
(by which we mean the portions of the boundary of K that can be connected by a path

28 TERENCE TAO

Figure 6. A polygonal path ˜γ0
3 (drawn as a solid line), together with
some additional 1-boundaries Bpπ3q˚U (the two dashed lines). Here, K is
˜γ0
3 together with the component of Bpπ3q˚U that intersects ˜γ0
3. The paths
˜γ´
3 and ˜γ`
3 are drawn as dotted lines; they have been moved slightly away
from γ0
3 for visibility. The area inequalities (5.9) can then be written as
0 ď 2|A| ` |B| ď |A| ` |B| ` |C| ` |D|, where |A| denotes the Lebesgue
measure of the region A in the ﬁgure, and similarly for |B|, |C|, |D|. Each
1-boundary gives a zero contribution to the area under ˜γ3, so one also
has |B| ` |C| “ |D|. In the depicted scenario, the ﬁrst area inequality is
automatically true, but the second one is not necessarily so.

to points in CylmL with arbitrarily large positive or negative y coordinate respectively),
then we have the inequalities
ż
˜γ´
3 y dx ď ż
˜γ0
3 y dx ď ż
˜γ`
3 y dx. (5.9)

This claim, which implies Conjecture 5.6, is an assertion about the relative sizes of the
“holes” in K; see Figure 6.
6. A combinatorial variant

Conjecture 5.6 appears diﬃcult to resolve in general. However, there is a more tractable-
seeming special case of Conjecture 5.6 which captures many of the key features of the
full conjecture:

Conjecture 6.1 (Special case of area inequality). Conjecture 5.6 holds when σ1 “
Graph0,L.
 INTEGRATION APPROACH TO SQUARE PEG PROBLEM 29

Once one makes the restriction σ1 “ Graph0,L, Conjecture 5.6 turns out to collapse from
a two-dimensional problem to a more tractable one-dimensional one. Indeed, suppose
that the tuple pσ1pR{LZq, σ2pR{LZq, σ3pR{LZq, σ4pR{LZqq does not jointly inscribing a
square, with σ1 “ Graph0,L. That is to say, there does not exist x P R{LZ and y, a, b P R
with
 px, yq P σ1pR{LZq

px ` a, y ` bq P σ2pR{LZq

px ` a ´ b, y ` a ` bq P σ3pR{LZq

px ´ b, y ` aq P σ4pR{LZq.

The ﬁrst condition px, yq P σ1pR{LZq simply asserts that y “ 0. If one now deﬁnes the
linearly transformed closed polygonal curves ˜σ2, ˜σ3, ˜σ4 : R{LZ Ñ CylL by the formulae

˜σ2ptq “ px2ptq ´ y2ptq, y2ptqq

˜σ3ptq “ px3ptq, ´y3ptqq

˜σ4ptq “ px4ptq ` y4ptq, y4ptqq

where xi, yi : R Ñ R are the components of σi for i “ 1, 2, 3, 4, then ˜σ2, ˜σ3, ˜σ4 remain
simple, and (on setting ˜x :“ x ` a ´ b) we see that the property of the quadruple

pσ1pR{LZq, σ2pR{LZq, σ3pR{LZq, σ4pR{LZqq

not jointly inscribing squares is equivalent to the non-existence of real numbers ˜x, a, b
such that
 p˜x, bq P ˜σ2pR{LZq

p˜x, ´a ´ bq P ˜σ3pR{LZq

p˜x, aq P ˜σ4pR{LZq.

Also, from the change of variables we see that
ż
˜σj y dx “ p´1q
j ż

σj y dx

for j “ 2, 3, 4. Relabeling ˜σ2, ˜σ3, ˜σ4 as γ1, γ2, γ3, and writing b, ´a ´ b, a as y1, y2, y3 re-
spectively, we thus see that Conjecture 6.1 is equivalent to the following more symmetric
version:

Conjecture 6.2 (Special case of area inequality, symmetric form). Let L ą 0, and let
γ1, γ2, γ3 : R{LZ Ñ CylL be simple closed polygonal paths homologous to Graph0,L, such
that there does not exist points px, yiq P γipR{LZq with x, y1, y2, y3 P R and y1 `y2 `y3 “
0. Then one has ż

γ1`γ2`γ3 y dx ‰ 0.

In this section we show that Conjecture 6.2 is equivalent to an almost purely combi-
natorial statement. To formulate it, we need some deﬁnitions. Recall that the signum
function sgn : r´8, `8s Ñ t´1, `1u on the extended real line r´8, `8s is deﬁned to
equal ´1 of r´8, 0q, 0 on 0, and `1 on p0, `8s.

30 TERENCE TAO

Deﬁnition 6.3 (Non-crossing sums). Let m “ 2, 3, and for each 1 ď i ď m, let
yi,1, yi,2 P r´8, `8s be extended reals. We say that the pairs tyi,1, yi,2u for i “ 1, . . . , m
have non-crossing sums if the following axioms are obeyed:

(i) Either all of the yi,1, yi,2 avoid `8, or they all avoid ´8.
(ii) For any j1, . . . , jm P t1, 2u, the sum y1,j1 ` ¨ ¨ ¨ ` ym,jm (which is well deﬁned by
(i)) is non-zero.
(iii) One has the cancellation
ÿ

j1,...,jmPt1,2up´1q
j1`¨¨¨`jm sgnpy1,j1 ` ¨ ¨ ¨ ` ym,jmq “ 0. (6.1)

or equivalently (by (ii)) ÿ

j1,...,jmPt1,2u:y1,j1 `¨¨¨`ym,jm ą0
p´1q
j1`¨¨¨`jm “ 0.

That is to say, there are as many positive sums y1,j1 ` ¨ ¨ ¨ ` ym,jm ą 0 with the
index sum j1 ` ¨ ¨ ¨ ` jm even as there are positive sums y1,j1 ` ¨ ¨ ¨ ` ym,jm ą 0
with j1 ` ¨ ¨ ¨ ` jm odd (and similarly with “positive” replaced by “negative”).

Otherwise, we say that the pairs tyi,1, yi,2u for i “ 1, . . . , m have crossing sums.

Remark 6.4. The notion of non-crossing sums is invariant with respect to interchanges
between yi,1 and yi,2 for i “ 1, . . . , m, or between the pairs tyi,1, yi,2u for i “ 1, . . . , m,
or by replacing each of the yi,j with their negations ´yi,j. One could deﬁne this concept
for other values of m than m “ 2, 3, but these are the only two values of m we will need
here.

Example 6.5. Let a1, a2, b1, b2 be distinct elements of R Y t´8u. Then the pairs
ta1, a2u and t´b1, ´b2u have non-crossing sums if and only if the number of pairs pi, jq P
t1, 2u ˆ t1, 2u with ai ă bj is even, thus for instance ta1, a2u and t´b1, ´b2u will have
non-crossing sums if a1 ă a2 ă b1 ă b2
or a1 ă b1 ă b2 ă a2
but not if a1 ă b1 ă a2 ă b2.
In particular, if ´8 ă b1 ă b2 ă `8, t´8, au and t´b1, ´b2u have non-crossing sums
if and only if a lies outside of rb1, b2s.

In a more topological form: the pairs ta1, a2u and t´b1, ´b2u have non-crossing sums iﬀ
it is possible to connect p0, a1q and p0, a2q (resp. p0, b1q and p0, b2q) by a curve γa (resp.
γb) in the (one-point compactiﬁcation of the) right half-plane r0, `8q ˆ R, in such a
manner that γa and γb do not cross. See Figures 7, 8.

Example 6.6. The pairs t0, 1u, t0, 6u, t´5, 1u have non-crossing sums because there are
as many positive sums 0 ` 0 ` 1, 0 ` 6 ´ 5, 1 ` 6 ` 1 with an even index sum as there are
positive sums 1 ` 0 ` 1, 1 ` 6 ´ 5, 0 ` 6 ` 1 with an odd index sum. On the other hand,
the pairs t´3, 5u, t´3, 5u, t´3, 5u have crossing sums because there are fewer positive

INTEGRATION APPROACH TO SQUARE PEG PROBLEM 31

Figure 7. The pairs ta1, a2u and t´b1, ´b2u have non-crossing sums: the
sums a1 ` p´b1q, a2 ` p´b1q are positive, while the sums a1 ` p´b2q, a2 `
p´b2q are negative. Note that the path connecting p0, a1q to p0, a2q does
not cross the path connecting p0, b1q to p0, b2q.

sums 5 ` 5 ` 5 with an even index sum than positive sums ´3 ` 5 ` 5, 5 ´ 3 ` 5, 5 ` 5 ´ 3
with an odd index sum.

As we shall see later, the notion of tyi,1, yi,2u for i “ 1, 2, 3 having non-crossing sums
also has a topological interpretation (assuming axiom (i)), namely that there are curves
γi in the one-point compactiﬁcation of r0, `8q ˆ R connecting p0, yi,1q to p0, yi,2q for
i “ 1, 2, 3 such that there do not exist x, y1, y2, y3 P R with y1 ` y2 ` y3 “ 0 and px, yiq
in γi for i “ 1, 2, 3. This may help explain the terminology “non-crossing sums”.

Example 6.7. Suppose that 0 ă a ă b ă c and x, y, z are real numbers such that
tx, x ` au, ty, y ` bu, tz, z ` cu have non-crossing sums. The 23 sums formed from this
triplet may be almost completely ordered as

x ` y ` z ă x ` a ` y ` z ă x ` y ` b ` z ă x ` a ` y ` b ` z, x ` y ` z ` c
ă x ` a ` y ` z ` c ă x ` y ` b ` z ` c ă x ` a ` y ` b ` z ` c

(the reader may wish to ﬁrst see this in the case x “ y “ z “ 0). The sums x ` a ` y `
z, x ` y ` b ` z, x ` y ` z ` c, x ` a ` y ` b ` z ` c have even index sum, and the other four
sums have odd index sum. Therefore, tx, x ` au, ty, y ` bu, tz, z ` cu has non-crossing

32 TERENCE TAO

Figure 8. The pairs ta1, a2u and t´b1, ´b2u have crossing sums: the
sums a1`p´b1q, a2`p´b1q, a1`p´b2q are positive, while the sum a2`p´b2q
is negative. Note that the path connecting p0, a1q to p0, a2q crosses the
path connecting p0, b1q to p0, b2q.

sums precisely when the origin 0 falls in one of the ﬁve intervals

p´8, x ` y ` zq,

px ` a ` y ` z, x ` y ` b ` zq,

px ` a ` y ` b ` z, x ` y ` z ` cq,

px ` a ` y ` z ` c, x ` y ` b ` z ` cq,

px ` a ` y ` b ` z ` c, `8q

(with the third interval deleted if x ` y ` z ` c ă x ` a ` y ` b ` z). In particular, we
see that pair tx, x ` au with the smallest diﬀerence has no inﬂuence on the sign of the
triple sums, that is to say

sgnpx ` y2 ` y3q “ sgnpx ` a ` y2 ` y3q

for y2 P ty, y ` bu and y3 P tz, z ` cu. Conversely, if this pair has no inﬂuence on the
sign of triple sums then the pairs tx, x ` au, ty, y ` bu, tz, z ` cu have non-crossing sums.
This lack of inﬂuence by the pair with the smallest diﬀerence can thus be used as an
alternate deﬁnition of non-crossing sums in the m “ 3 case (and it also works in the
m “ 2 case).
 INTEGRATION APPROACH TO SQUARE PEG PROBLEM 33

One corollary of this analysis is that if ty, y ` bu has no inﬂuence on the sign of the
triple sums, then neither does tx, x ` au; similarly, if tz, z ` cu has no inﬂuence on the
non-crossing sums, then neither does ty, y ` bu.

We are now ready to give the combinatorial formulation of Conjecture 6.2.

Conjecture 6.8 (Combinatorial formulation). Let k1, k2, k3 be odd natural numbers,
and for each i “ 1, 2, 3, let yi,1, . . . , yi,ki be distinct real numbers. Adopt the convention
that yi,0 “ yi,ki`1 “ ´8. Assume the following axioms:

(i) (Non-crossing) For any 1 ď i ď 3 and 0 ď p ă q ď ki with p, q the same parity,
the pairs tyi,p, yi,p`1u and t´yi,q, ´yi,q`1u have non-crossing sums.
(ii) (Non-crossing sums) For any 0 ď p1 ď k1, 0 ď p2 ď k2, 0 ď p3 ď k3 with
p1, p2, p3 the same parity, the pairs ty1,p1, y1,p1`1u, ty2,p2, y2,p2`1u, ty3,p3, y3,p3`1u
have non-crossing sums.

Then one has the inequality
 3ÿ

i“1
 kiÿ

j“1
p´1q
j´1yi,j ă 0. (6.2)

Remark 6.9. In the language of Arn´old, the hypothesis (i) shows that the ordering of
the extended real numbers ´8, yi,1, . . . , yi,ki is given by the permutation of a meander
(formed by gluing together two non-crossing matchings); see [13].

The main result of this section is then

Theorem 6.10. Conjecture 6.2 (and hence Conjecture 6.1) is equivalent to Conjecture
6.8.

6.1. Forward direction. Let us ﬁrst assume Conjecture 6.2 and see how it implies
Conjecture 6.8. Let k1, k2, k3 and yi,j obey the assumptions of Conjecture 6.8, but
suppose for contradiction that (6.2) failed. The plan is then to use the quantities yi,j to
build simple closed polygonal paths γ1, γ2, γ3 : R{LZ Ñ CylL for some L ą 0 to which
Conjecture 6.2 may be applied.

By perturbing one of the yi,j slightly (noting that all the hypotheses on the yi,j are open
conditions) we may assume that the quantity

Q :“
 3ÿ

i“1
 kiÿ

j“1p´1qj´1yi,j (6.3)

is strictly positive. Similarly, we may assume that the diﬀerences |yi,p`1 ´ yi,p| with
i “ 1, 2, 3 and 1 ď p ă ki are all distinct.

We will need a strictly monotone decreasing function φ : r0, `8q Ñ r1, 2s; the exact
choice of φ is unimportant, but for concreteness one can take for instance φptq :“ 1` 1
1`t .

34 TERENCE TAO

Let L ą 0 be a suﬃciently large quantity to be chosen later. We will also need a certain
large and negative quantity ´R (depending on Q, L, and the yi,j) whose precise value
will be speciﬁed later.

By applying Conjecture 6.8(ii) with p1 “ p2 “ p3 “ 0, we see that t´8, y1,1u, t´8, y2,1u, t´8, y3,1u
have non-crossing sums, which implies that

y1,1 ` y2,1 ` y3,1 ă 0.

Similarly if we apply Conjecture 6.8(ii) with p1 “ k1, p2 “ k2, p3 “ k3, we see that

y1,k1 ` y2,k2 ` y3,k3 ă 0.

As a consequence, we may ﬁnd piecewise linear continuous functions f1, f2, f3 : r´1, 1s Ñ
R such that fip´1q “ yi,ki; fip1q “ yi,1 (6.4)

for i “ 1, 2, 3, and such that
 f1ptq ` f2ptq ` f3ptq ă 0 (6.5)

for all ´1 ď t ď 1. For instance, we can set f1, f2, f3 to be the linear functions given by
the boundary conditions (6.4). But we can also subtract an arbitrary positive multiple
of 1 ´ |t| from any of f1, f2, f3 and obey the above requirements. In particular, there is
a quantity ´C0 (independent of L) such that if the quantity ´R mentioned previously
is less than or equal to ´C0, one can ﬁnd f1, f2, f3 solving the above conditions such
that 3ÿ

i“1
 ż 1

´1 fiptq dt “ ´R. (6.6)

Henceforth we ﬁx f1, f2, f3 with these properties.

Let i “ 1, 2, 3. We construct some polygonal paths γi,1, γi,1Ñ2, . . . , γi,ki´1Ñki, γi,ki, γi,kiÑ1
in CylL by the following recipes:

Deﬁnition 6.11.

(i) γi,1 is the rightward horizontal line segment from p´ L
2 ` 1, yi,1q to p0, yi,1q, pro-
jected to CylL.
(ii) For any odd 1 ď p ă ki, γi,pÑp`1 is the piecewise linear path traversing the
vertices

p0, yi,pq, ˆ L
2 ´ φp|yi,p ´ yi,p`1|q, yi,p
˙ , ˆ L
2 ´ φp|yi,p ´ yi,p`1|q, yi,p`1
˙ , p0, yi,p`1q

in that order (that is to say, the concatenation of a rightward horizontal line
segment, a vertical line segment, and a leftward horizontal line segment, if L is
large enough), and then projected to CylL.
(iii) For any even 1 ă p ă ki, γi,pÑp1 is the piecewise linear path traversing the
vertices

p0, yi,pq, ˆ´L
2 ` φp|yi,p ´ yi,p`1|q, yi,p
˙ , ˆ´L
2 ` φp|yi,p ´ yi,p`1|q, yi,p`1
˙ , p0, yi,p`1q

INTEGRATION APPROACH TO SQUARE PEG PROBLEM 35

Figure 9. Construction of the components of γi, in the case ki “ 5.
Notice the interlacing between the p0, yi,pq with p odd and the p0, yi,pq
with p even, and the alternating orientations of γi at these locations.

in that order (that is to say, the concatenation of a leftward horizontal line
segment, a vertical line segment, and a rightward horizontal line segment, if L
is large enough), and then projected to CylL.
(iv) γi,ki is the rightward horizontal line segment from p0, yi,kiq to p L
2 ´ 1, yi,kiq, pro-
jected to CylL.
(v) γi,kiÑ1 is the graph "ˆ L
2 ` t, fiptq
˙ : ´1 ď t ď 1
*

traversed from left to right and then projected to CylL, thus it begins at πLp L
2 ´
1, yi,kiq and ends at πLp L
2 ` 1, yi,1q.

See Figure 9.

Clearly, one can concatenate the paths γi,1, γi,1Ñ2, . . . , γi,ki´1Ñki, γi,ki, γi,kiÑ1 to form a
closed polygonal path γi in CylL (which one can parameterise by R{LZ after a suitable
rescaling). Using the convex fundamental domain r´ L
2 ` 1, L
2 ` 1s ˆ R of CylL, we see
that γi is homotopic in this domain to the horizontal line segment from p´ L
2 ` 1, yi,1q
to p L
2 ` 1, yi,1q, and hence γi is homologous in CylL to Graph0,L.

Using Conjecture 6.8(i), we can show

Lemma 6.12. Suppose L is suﬃciently large. Then for any i “ 1, . . . , 3, the path γi is
simple.

36 TERENCE TAO

Proof. Each of the components γi,1, γi,1Ñ2, . . . , γi,ki´1Ñki, γi,ki, γi,kiÑ1 of γi are separately
simple, and the endpoints are all distinct except for the endpoints of adjacent paths, so
it suﬃces to show that no two of these components meet in the interior.

The interior of the path γi,kiÑ1 lies in the strip p L
2 ´ 1, L
2 ` 1q ˆ R (viewed as a subset of
CylL), while the interior of the other paths lie in either p´ L
2 ` 1, 0q ˆ R or p0, L
2 ´ 1q ˆ R,
again only touching the boundary at endpoints. So it suﬃces to show that there are no
crossings in p´ L
2 ` 1, 0q ˆ R or p0, L
2 ´ 1q ˆ R.

We just verify the claim for p´ L
2 ` 1, 0q ˆ R, as the case of p0, L
2 ´ 1q ˆ R is completely
analogous. The only path components here are γi,1 and γi,pÑp`1 for 1 ă p ă ki even.
To check that γi,1 and γi,pÑp`1 do not cross, it suﬃces from Deﬁnitions 6.11(i), (iii) to
show that yi,1 does not lie between yi,p and yi,p`1. But from Conjecture 6.8(i) we see
that t´8, yi,1u and t´yi,p, ´yi,p`1u have non-crossing sums, which gives the claim by
Example 6.5.

Now we need to check that γi,pÑp`1 and γi,qÑq`1 do not cross when 1 ă p, q ă k1
are even and distinct. By Conjecture 6.8(i), the pairs tyi,p, yi,p`1u and t´yi,q, ´yi,q`1u
have non-crossing sums; thus the interval spanned by tyi,q, yi,q`1u either is disjoint from,
contains, or is contained in the interval spanned by tyi,p, yi,p`1u. In the former case,
the paths γi,pÑp`1 and γi,qÑq`1 are clearly disjoint because from Deﬁnition 6.11(ii), the
y coordinate of any point on the ﬁrst path lies in the interval spanned by tyi,p, yi,p`1u,
and the y coordinate on any point on the second path lies in the interval spanned
by tyi,q, yi,q`1u. By symmetry, the only remaining case to check is when the interval
spanned by tyi,p, yi,p`1u is contained in the interval spanned by tyi,q, yi,q`1u. But in this
case, we have |yi,p ´ yi,p`1| ă |yi,q ´ yi,q`1|, so by Deﬁnition 6.11(iii) and the monotone
decreasing nature of φ, the vertical segment of the curve γi,pÑp`1 lies to the right of
that of γi,qÑq`1. From this we see that the two curves are disjoint. This concludes the
demonstration of simplicity in p´ L
2 ` 1, 0q ˆ R; the case of p0, L
2 ´ 1q ˆ R is similar. □

In a similar fashion, we can use Conjecture 6.8(ii) to show

Lemma 6.13. There does not exist x P R{LZ and y1, y2, y3 P R with y1 ` y2 ` y3 “ 0
such that px, yiq P γipRq for all i “ 1, 2, 3.

Proof. Suppose for contradiction that x, y1, y2, y3 exist with the stated properties.

First suppose that x lies in r L
2 ´ 1, L
2 ` 1s (projected to R{LZ). Then from Deﬁnition
6.11(v) we have yi “ fipx ´ L
2 q for i “ 1, 2, 3, but then from (6.5) we cannot have
y1 ` y2 ` y3 “ 0, a contradiction.

We now treat the case when x lies in r0, L
2 ´ 1s (projected to R{LZ); the remaining case
when x lies in r´ L
2 ` 1, 0s is similar and will be omitted. By Deﬁnition 6.11, we see that
each of the px, yiq lies either on γi,ki or on γi,piÑpi`1 for some odd 1 ď pi ă ki.

INTEGRATION APPROACH TO SQUARE PEG PROBLEM 37

Suppose ﬁrst that each of the px, yiq lie on γi,piÑpi`1. By hypothesis, the quantities
L
2 ´ φp|yi,pi ´ yi,pi`1|q for i “ 1, 2, 3 are distinct; by cyclic permutation we may assume
that L
2 ´ φp|y1,p1 ´ y1,p1`1|q is the smallest of these quantities, or equivalently that
|yi,pi ´yi,pi`1| is minimised at i “ 1. By Deﬁnition 6.11(ii), the x coordinate of γ1,p1Ñp1`1
does not exceed L
2 ´ φp|y1,p1 ´ y1,p1`1|q, which implies that

x ď L
2 ´ φp|y1,p1 ´ y1,p1`1|q,

and hence by further application of Deﬁnition 6.11(ii) we have y2 “ y2,q2 and y3 “ y3,q3
for some q2 P tp2, p2 ` 1u and q2 P tp3, p3 ` 1u; furthermore y1 lies between y1,p1 and
y1,p1`1 inclusive. Since y1 ` y2 ` y3 “ 0, this implies that the sums y1,p1 ` y2,q2 ` y3,q3 and
y1,p1`1`y2,q2 `y3,q3 do not have the same sign. Because i “ 1 minimises |yi,pi ´yi,pi`1|, we
conclude (from Example 6.7) that the pairs ty1,p1, y1,p1`1u, ty2,p2, y2,p2`1u, ty3,p3, y3,p3`1u
do not have non-crossing sums, contradicting Conjecture 6.8(ii).

The case when one or more of the px, yiq lies on γi,ki is treated similarly, with ki now
playing the role of pi (and recalling the convention yi,ki`1 “ ´8. This concludes the
treatment of the case x P r0, L
2 ´ 1s, and the case x P r´ L
2 ` 1, 0s is similar. □

From the previous two lemmas and Conjecture 6.2, we conclude that
ż

γ1`γ2`γ3 y dx ‰ 0 (6.7)

We work in the fundamental domain r´ L
2 `1, L
2 `1sˆR of CylL. On the strip r L
2 ´1, L
2 `
1s ˆ R, the contribution to ş

γ1`γ2`γ3 y dx is ř3
i“1 ş1
´1 fiptq dt “ ´R thanks to Deﬁnition
6.11(v) and (6.6). On the strip r´ L
2 ` 2, L
2 ´ 2s ˆ R, the curve γi for i “ 1, 2, 3 is simply
the union of the line segments r´ L
2 ` 2, L
2 ´ 2s ˆ tyi,pu for p “ 1, . . . , ki (traversed from
left to right for odd p, and right to left for even p), so the contribution to ş

γ1`γ2`γ3 y dx
here is 3ÿ

i“1pL ´ 4q
 kiÿ

j“1
p´1q
j´1yi,j “ pL ´ 4qQ

thanks to (6.3). Finally, the contribution of the remaining strips r´ L
2 ` 1, ´ L
2 ` 2s ˆ
R Y r L
2 ´ 2, ´ L
2 ´ 1s ˆ R is some quantity ´C1 independent of L and R, as can be seen
by translating these strips by ˘ L
2 . The inequality (6.7) thus becomes

pL ´ 4qQ ´ C1 ´ R ‰ 0.

But as Q is positive, we can make this quantity vanish by choosing L large enough and
then setting ´R :“ C1 ´ pL ´ 4qQ; note for L large enough that this value of ´R will
be less than the threshold ´C0 needed so that one can arrange the function f1, f2, f3 to
obey (6.6). This yields the desired contradiction.

6.2. Backward direction. Now we assume Conjecture 6.8 and see how it implies
Conjecture 6.2.

38 TERENCE TAO

By applying (a slight variant of) Proposition 5.8, we see that to prove Conjecture 6.2,
it suﬃces to do so under the additional nondegeneracy hypothesis that all the vertices
of γ1, γ2, γ3 have distinct x-coordinates (in particular, these curves do not contain any
vertical edges). Write γiptq “ pxiptq, yiptqq for some piecewise linear xi : R{LZ Ñ R{LZ
and yi : R{LZ Ñ R. As γi is homologous to Graph0,L, we can ﬁnd a continuous lift
˜xi : R Ñ R of xi with ˜xipt ` Lq “ ˜xiptq ` L for all t P R; we also let ˜yi : R Ñ R be the
periodic lift of yi. As ˜xiptq ´ t is periodic and continuous, it is bounded; by multiplying
the period L by a large integer if necessary, we may assume that

|˜xiptq ´ t| ď L
10 (6.8)

for all t P R and i “ 1, 2, 3.

Using the nondegeneracy hypothesis, we see that for any i “ 1, 2, 3 and any x P R, the
ﬁbre ty P R : px, yq P γipRqu consists of a ﬁnite number kipxq of real numbers, where
the function ki takes values in the odd natural numbers, is periodic in L, and is locally
constant for all x outside of ﬁnitely many residue classes mod L. We can enumerate
these real numbers as ˜yipti,1pxqq, . . . , ˜yipti,kipxqpxqq
where ti,1pxq ă ¨ ¨ ¨ ă ti,kipxqpxq are those real numbers t with ˜xiptq “ x, arranged in
increasing order, thus ˜xipti,jpxqq “ x (6.9)
for all x P R, i “ 1, 2, 3, and 1 ď j ď kipxq. For x outside of ﬁnitely many residue classes
mod L, the functions ti,j are locally linear, and have the LZ-equivariance property

ti,jpx ` Lq “ ti,jpxq ` L

for all x P R, i “ 1, 2, 3, and 1 ď j ď kipxq. Also, from the nondegeneracy hypothesis
we see from the intermediate value theorem that outside of ﬁnitely many residue classes
mod L, ti,j is increasing for odd j and decreasing for even j.

The analogue of the set SquaresL Ă Cyl
4
L in this context is the oriented 3-dimensional
submanifold Sums of Cyl
3
L deﬁned by

Sums :“ tppx1, y1q, px2, y2q, px3, y3qq P Cyl
3
L : x1 “ x2 “ x3; y1 ` y2 ` y3 “ 0u.

The hypotheses of Conjecture 6.2 then assert that the 3-cycle γ1 ˆ γ2 ˆ γ3 in Cyl
3
L
does not intersect Sums. We view Sums as an oriented submanifold of the 4-manifold
V Ă Cyl
3
L deﬁned by

V :“ tppx1, y1q, px2, y2q, px3, y3qq P Cyl
3
L : x1 “ x2 “ x3u.

As we assumed the vertices of γ1, γ2, γ3 to have distinct x coordinates, the 3-cycle
γ1 ˆ γ2 ˆ γ3 intersects V transversely in some 1-cycle γ123. As γ1, γ2, γ3 are homologous
to Graph0,L, γ123 is homologous to the 1-cycle

Graph
∆
0,L :“ tpp, p, pq : p P Graph0,Lu

with the standard orientation.

Now we argue as in the previous section. The 4-manifold V is homeomorphic to R{LZˆ
R
3 and thus has ﬁrst homology generated by Graph
∆
0,L. By the greedy algorithm, one can

INTEGRATION APPROACH TO SQUARE PEG PROBLEM 39

express the 1-cycle γ123 as a ﬁnite integer linear combination of closed paths contained
(as a set) in γ123, each of which is either simple or a 1-boundary; one of these, say
γ0
123 : R{LZ Ñ V , is homologous to mGraph
∆
0,L for some non-zero integer m, and is
thus simple. From the Jordan curve theorem, m must be `1 or ´1; by reversing the
orientation of γ0
123 we can then assume that m “ 1, thus γ0
123 is homologous to Graph
∆
0,L
and is contained (as a set) in γ123. In particular, it avoids Sums. If we write

γ0
123ptq “ ppXptq, Y1ptqq, pXptq, Y2ptqq, pXptq, Y3ptqqq

then X : R{LZ Ñ R{LZ, Y1, Y2, Y3 : R{LZ Ñ R are piecewise linear continuous func-
tions with X homologous to the identity function (in the sense that X lifts to a function
˜X : R Ñ R with ˜Xpt ` Lq “ ˜Xptq ` L for all t P R), with the properties that

pXptq, Yiptqq P γipR{LZq (6.10)

and Y1ptq ` Y2ptq ` Y3ptq ‰ 0 (6.11)
for all t P R{LZ and i “ 1, 2, 3.

Remark 6.14. One can view the functions Xptq, Y1ptq, Y2ptq, Y3ptq from a dynamical
perspective by thinking of pXptq, Yiptqq as the trajectory of a particle Pi that is con-
strained to lie in γipR{LZq, and with all three particles P1, P2, P3 constrained to lie on a
vertical line. We can also constrain the particles P1, P2, P3 to have a constant horizontal
speed; the particles move in one horizontal direction until one of the particles Pi cannot
move any further due to it hitting a vertex v of γi with both edges adjacent to v lying
on the same side of the vertical line containing v. Whenever such a collision occurs, the
horizontal velocity reverses sign, Pi moves from one edge of γi to the next, and the other
two particles reverse themselves and retrace their steps; see Figure 10. Note from our
hypotheses that only one collision occurs at a time. Because the paths γ1, γ2, γ3 have
only ﬁnitely many edges, these trajectories must be periodic; the above homological
considerations ensure that at least one of these trajectories is homologous to Graph
∆
0,L
(possibly after enlarging the period L).

Recall that X : R{LZ Ñ R{LZ lifts to a function ˜X : R Ñ R such that ˜Xpt ` Lq “
˜Xptq ` L for all t P R, thus ˜Xptq ´ t is periodic and therefore bounded. We also lift
Yi : R{LZ Ñ R periodically to ˜Yi : R Ñ R for i “ 1, 2, 3. By lifting and (6.10), we
can then ﬁnd unique continuous functions Ti : R Ñ R with Tipt ` Lq “ Tiptq ` L for all
t P R, such that p ˜Xptq, ˜Yiptqq “ p˜xipTiptqq, ˜yipTiptqqq (6.12)
for all t P R. By replacing L with a large multiple if necessary, we may assume that

| ˜Xptq ´ t|, |Tiptq ´ t| ď L
10 (6.13)

for all t P R and i “ 1, 2, 3.

By continuity and (6.11), we see that the expression ˜Y1ptq` ˜Y2ptq` ˜Y3ptq is either positive
for all t, or negative for all t. By applying the reﬂection px, yq ÞÑ px, ´yq on CylL we
may assume the latter case occurs, thus
˜Y1ptq ` ˜Y2ptq ` ˜Y3ptq ă 0 (6.14)

40 TERENCE TAO

Figure 10. The dynamics of Xptq, Y1ptq, Y2ptq, Y3ptq.

for all t P R{LZ. To establish Conjecture 6.2, it suﬃces to show that
ż

γ1`γ2`γ3 y dx ă 0;

integrating ﬁbre by ﬁbre, it will suﬃce to show that

3ÿ

i“1
 kipxqÿ

j“1 p´1q
j´1 ˜yipti,jpxqq ă 0 (6.15)

for almost every x P R.

Fix x P R; we may assume that x avoids all the x coordinates of vertices of γ1, γ2, γ3.
We abbreviate ki “ kipxq and yi,j :“ ˜yipti,jq
for i “ 1, 2, 3 and 1 ď j ď ki, adopting the conventions yi,0 “ yi,ki`1 “ ´8. Applying
Conjecture 6.8, it will suﬃce to verify the hypotheses (i), (ii) of that conjecture.

Let t` “ t`pxq denote the largest time t` P R for which ˜Xpt`q “ x (such a time exists
thanks to (6.13) and continuity). We claim that Tipt`q “ ti,kipxq for all i “ 1, 2, 3.
Suppose for contradiction that this failed for some i “ 1, 2, 3, then from (6.10) one has
Tipt`q “ ti,ppxq for some 1 ď p ă ki. From (6.13) and the intermediate value theorem we

INTEGRATION APPROACH TO SQUARE PEG PROBLEM 41

must then have Tiptq “ ti,kipxqpxq for some t ą t`, which by (6.12), (6.9) gives ˜Xptq “ x,
contradicting the maximality of t`. Similarly, if t´ “ t´pxq is the smallest time t´ P R
for which ˜Xpt´q “ x, then Tipt´q “ ti,1pxq for i “ 1, 2, 3. From (6.14) applied at the
times t`, t´ we have the inequalities

y1,1 ` y2,1 ` y3,1 ă 0 (6.16)

and y1,k1 ` y2,k2 ` y3,k3 ă 0. (6.17)

Having obtained these inequalities, we will have no further need of the functions X, ˜X, Yi, ˜Yi, Ti
or the curves γ0
123, although we will introduce a variant of these functions shortly.

We now verify the non-crossing property (i) for any given i “ 1, 2, 3. We just verify the
claim when p, q are odd, as the claim when p, q are even is completely analogous. First
suppose that q ă ki. Let γx,i,p denote the restriction of path t ÞÑ p˜xiptq, ˜yiptqq to the
interval t P rti,ppxq, ti,p`1pxqs; deﬁne γx,i,q similarly. The path γx,i,p traces out a piecewise
linear curve in R2 that starts at px, yi,pq, ends at px, yi,p`1q, and does not encounter the
vertical line x ˆ R at any point in between; also, it moves to the right for t near ti,ppxq
(and to the left for t near ti,p`1pxq). Thus, this curve γx,i,p must stay in the right half-
plane rx, `8q ˆ R; actually, by (6.8) we see that it stays in the strip rx, x ` L
2 s ˆ R (say).
Similarly for γx,i,q. On the other hand, as γi is simple and p ă q, the two paths γx,i,p
and γx,i,q cannot meet. From the Jordan curve theorem and Example 6.5, this forces
the endpoints tyi,p, yi,p`1u and tyi,q, yi,q`1u of these paths to be non-crossing, giving (i)
in this case.

Now suppose that q “ ki. In this case we deﬁne γx,i,q to be the restriction of t ÞÑ
p˜xiptq, ˜yiptqq to the interval rti,kipxqpxq, ti,1pxq ` Ls (this interval is well-deﬁned by (6.8)).
This is a path from px, yi,kiq to px ` L, yi,1q that does not cross tx, x ` Lu ˆ R except at
endpoints, and hence lies in the strip rx, x ` Ls ˆ R. It cannot cross γx,i,p, which also lies
in this strip, avoids the right edge, and starts and ends at the points px, yi,pq, px, yi,p`1q
on the left edge. By the Jordan curve theorem, this implies that yi,ki cannot lie between
yi,p and yi,p`1, which by Example 6.5 implies (since yi,ki`1 “ ´8) that tyi,p, yi,p`1u and
tyi,ki, yi,ki`1u are non-crossing. This concludes the establishment of (i) when p, q are
odd; the case when p, q are even is analogous (working to the left of txu ˆ R rather
than to the right, and using the convention yi,0 “ ´8 rather than yi,ki`1 “ ´8) and is
omitted.

Now we verify (ii) for 0 ď p1 ď k1, 0 ď p2 ď k2, 0 ď p3 ď k3 with p1, p2, p3 the same
parity. We just establish the claim when p1, p2, p3 are all odd, as the case when p1, p2, p3
are all even is completely analogous.

In the case p1 “ k1, p2 “ k2, p3 “ k3, we see from (6.17) and the conventions y1,k1`1 “
y2,k2`2 “ y3,k3`3 “ ´8 that the pairs ty1,k1, y1,k1`1u, ty2,k2, y2,k2`1u, ty3,k3, y3,k3`1u. Thus
we may assume that pi ă ki for at least one i; say p1 ă k1.

As in the proof of (i), we can form the curves γx,i,pi for i “ 1, 2, 3, which lie in the strip
rx, x ` Ls ˆ R, with initial point px, yi,piq and ﬁnal point px, yi,pi`1q. For i “ 1, 2, 3, let xi
denote the maximum x coordinate attained by γx,i,pi, thus x ă xi ď x ` L; furthermore

42 TERENCE TAO

xi “ x ` L if pi “ ki and xi ď x ` L
2 otherwise, in particular x1 ď x ` L
2 . As the vertices
of γi have distinct x coordinates, the xi are distinct in the interval rx, x ` L
2 s; without
loss of generality we may then take x1 ă x2, x3. For i “ 1, 2, 3, deﬁne γ1
x,i,pi to be the
connected component of γx,i,pi X rx, x1s ˆ R that contains px, yi,piq; thus γ1
x,1,p1 “ γx,1,p1,
and for i “ 2, 3, γ1
x,i,pi is a piecewise path connecting px, yi,piq to some point on the
vertical line tx1u ˆ R.

Consider the set

S :“ tpx1, y1
1, y1
2, y1
3q P R
4 : px1, y1
iq lies in γ1
x,i,pi for i “ 1, 2, 3u.

The set S is a union of line segments in R
4. It contains the point px, y1,p1, y2,p2, y3,p3q with
exactly one line segment emenating from it; S similarly contains the point px, y1,p1`1, y2,p2, y3,p3q
with exactly one line segment emenating from it. A local analysis (using the non-
degeneracy hypothesis that the vertices of γ1, γ2, γ3 all have distinct x coordinates) then
reveals that every other point px1, y1
1, y1
2, y1
3q in S is either an interior point of a line
segment in S (and avoids all other line segments comprising S), or else is a vertex that
is the endpoint of exactly two edges in S; this claim is most delicate in the case where
x1 “ x1, in which the curves γ1
x,2,p2 and γ1
x,3,p3 have terminated, but γx,1,p1 leaves px1, y1q
in two leftward directions, thus again forming two edges in S (see Figure 11). Because of
this, there must be a path t ÞÑ pX 1ptq, Y 1
1ptq, Y 1
2ptq, Y 1
3ptqq in S from px, y1,p1, y2,p2, y3,p3q
to px, y1,p1`1, y2,p2, y3,p3q (cf. Remark 6.14). By the hypothesis of Conjecture 6.2, we
must have Y 1
1ptq ` Y 1
2ptq ` Y 1
3ptq ‰ 0
for all t. In particular, we conclude that the sums

y1,p1 ` y2,p2 ` y3,p3, y1,p1`1 ` y2,p2 ` y3,p3
have the same sign. A similar argument (using the connected component of γ1
x,i,pi
containing px, yi,pi`1q rather than px, yi,piq as appropriate) shows more generally that
the sums y1,p1 ` y2,q2 ` y3,q3, y1,p1`1 ` y2,q2 ` y3,q3
have the same sign for q2 P tp2, p2 ` 1u and q3 P tp3, p3 ` 1u (this claim is trivially
true when q2 “ k2 ` 1 or q3 “ k3 ` 1. By Deﬁnition 6.3, we conclude that the pairs
ty1,p1, y1,p1`1u, ty2,p2, y2,p2`1u, ty3,p3, y3,p3`1u have non-crossing sums, giving (ii) in the
case that p1, p2, p3 are all odd; the claim when p1, p2, p3 are all even are proven similarly
(using the convention yi,0 “ ´8 instead of yi,ki “ ´8, working to the left of txu ˆ R
rather than to the right, and using (6.16) in place of (6.17)) and is omitted. This
completes the derivation of Conjecture 6.2 from Conjecture 6.8, and establishes Theorem
6.10.
 7. Some special cases of Conjecture 6.8

From Theorem 6.10, we see that any counterexample to Conjecture 6.8 can be converted
to counterexamples for Conjectures 6.2, 6.1, and 5.6, and we believe it likely that such
counterexamples, should they exist, could then be modiﬁed to give counterexamples to
Conjectures 5.2, 4.1, 4.6, and hence the original square peg conjecture (Conjecture 1.1).
On the other hand, after extensive testing of examples, the author is now inclined to

INTEGRATION APPROACH TO SQUARE PEG PROBLEM 43

Figure 11. The local behaviour of a point px1, y1
1, y1
2, y1
3q in S when x1

equals x1.

believe that Conjecture 6.8 is true, and a proof of this conjecture is likely to lead to an
approach to establish Conjecture 5.6 (and hence Conjectures 5.2, 4.1, 4.6) and perhaps
even Conjecture 1.1.

We do not have a proof of Conjecture 6.8 in full generality, however we can verify some
special cases. Firstly, we observe the following analogue of Theorem 5.7 for Conjecture
6.2:

Theorem 7.1. Conjecture 6.2 is true when one of the curves γi is the graph γi “ Graphf
of a piecewise linear function f : Z{LZ Ñ R.

Proof. Suppose that γ3 “ Graphf . By replacing γ3 with Graph0,L and γ2 with the
transformed polygonal path tpx, y ´ f pxqq : px, yq P γ2pZ{LZqu, we may assume without

44 TERENCE TAO

loss of generality that f “ 0. The hypothesis of Conjecture 6.2 then ensures that the
reﬂection ˜γ2 of γ2 across the x axis is disjoint from γ1, hence by the Jordan curve
theorem and Stokes’ theorem as before we have
ż
˜γ2 y dx ‰ ż

γ1 y dx

giving Conjecture 6.2 in this case since ş
˜γ2 y dx “ ´ ş

γ2 y dx. □

From this theorem and the construction used in the proof of Theorem 6.10, we see that
Conjecture 6.8 holds when one of the ki, say k3, is equal to 1. Of course, as Conjecture
6.8 is largely a combinatorial conjecture, one expects to also be able to verify the k3 “ 1
case of Conjecture 6.8 by a direct combinatorial argument, without explicit invocation of
the Jordan curve theorem. We can do this by developing some combinatorial analogues
of the Jordan curve theorem that are valid even when k1, k2, k3 ą 1. For any i P t1, 2, 3u
and y P r´8, `8s, deﬁne the winding number Wipyq by the Alexander numbering rule
[1]
 Wipyq :“ 1
2 ` 1
2
 kiÿ

j“1
p´1q
j´1 sgnpyi,j ´ yq

“ 1
2
 kiÿ

j“1p´1qj´1p1 ` sgnpyi,j ´ yqq
 (7.1)

(where we use the hypothesis that ki is odd), thus Wi is a half-integer on yi,1, . . . , yi,ki, a
locally constant integer outside of these points, and jumps by ˘ 1
2 when one perturbs oﬀ
of one of the yi,j in either direction. Also observe that Wipyq equals 0 near `8, and 1
near ´8. From Fubini’s theorem we can relate the winding number to the alternating
sum řki
j“1p´1q
j´1yi,j by the identity

ż 8

´T Wipyq dy “
 kiÿ

j“1
p´1q
j´1yi,j ` T (7.2)

which holds for all suﬃciently large T . A similar argument gives
ż 8

´T p1 ´ Wip´yqq dy “ ´
 kiÿ

j“1
p´1q
j´1yi,j ` T (7.3)

again for suﬃciently large T .

We can then use the hypothesis (i) of Conjecture 6.8 to give

Lemma 7.2 (Combinatorial Jordan curve theorem). Suppose that the hypotheses of
Conjecture 6.8 hold. Let i “ 1, 2, 3. Then one has Wipyi,jq “ 1
2 for all j “ 1, . . . , ki,
and Wipyq P t0, 1u for all y in r´8, `8sztyi,1, . . . , yi,k`1u.

Proof. Because Wi is locally constant away from tyi,1, . . . , yi,k`1u and jumps by ˘ 1
2 when
it reaches any of the yi,j, it suﬃces to establish the ﬁrst claim. Let 1 ď p ă ki. From

INTEGRATION APPROACH TO SQUARE PEG PROBLEM 45

Conjecture 6.8(i) we have
ÿ

j“q,q`1
p´1q
j´1 sgnpyi,p ´ yi,jq “ ÿ

j“q,q`1
p´1q
j´1 sgnpyi,p`1 ´ yi,jq

for all 0 ď q ď k1 distinct from p with the same parity as p (using the conventions
yi,0 “ yi,k1`1 “ ´8). Direct inspection shows that the claim also holds for q “ p.
Summing over q, and noting that the contributions of j “ 0 or j “ k1 ` 1 are the same
on both sides, we conclude that

k1ÿ

j“1
p´1q
j´1 sgnpyi,p ´ yi,jq “
 k1ÿ

j“1
p´1qj´1 sgnpyi,p`1 ´ yi,jq

and hence Wipyi,pq “ Wipyi,p`1q

for all 1 ď p ă ki. Direct computation also shows that Wipyi,pq “ 1
2 when 1 ď p ď k1
maximises yi,p, and the claim follows. □

Next, for distinct i, i
1 P t1, 2, 3u and y P r´8, `8s, we deﬁne the further winding
number Wii1pyq by the similar formula

Wii1pyq :“ 1
2 ` 1
2
 kiÿ

j“1
 ki1ÿ

j1“1
p´1q
j`j1 sgnpyi,j ` yi1,j1 ´ yq

“ 1
2
 kiÿ

j“1
 ki1ÿ

j1“1
p´1q
j`j1p1 ` sgnpyi,j ` yi1,j1 ´ yqq.
 (7.4)

As before, Wii1pyq will be a locally constant integer away from the sums yi,j ` yi1,j1, that
equals 0 for suﬃciently large positive y and 1 for suﬃciently large negative y. From
Fubini’s theorem we have the analogue
ż 8

´T Wii1pyq dy “
 kiÿ

j“1
p´1q
j´1yi,j `
 ki1ÿ

j“1
p´1q
j´1yi1,j1 ` T (7.5)

for suﬃciently large T . Curiously, one has the convolution identity

W 1
ii1 “ W 1
i ˚ W 1
i1

where the primes denote distributional derivatives, although the author was not able to
make much use of this identity. The winding numbers Wii1 also have some resemblance
to the Steinberg formula [23] for the multiplicity of irreducible representations in a
tensor product, although this is likely to be just a coincidence.

The hypothesis (ii) of Conjecture 6.8 allows us to make the winding number Wii1 vanish
at some points, and also give some control on the complementary winding number Wi2:

Proposition 7.3. Suppose that the hypotheses of Conjecture 6.8 hold. Let i, i
1, i
2 be
distinct elements of t1, 2, 3u.

(i) One has Wii1p´yi2,jq “ 0 for all j “ 0, . . . , k3 ` 1.

46 TERENCE TAO

(ii) If 0 ď p ď ki and 0 ď q ď ki1 have the same parity, then one has

Wi2p´yi,p ´ yi1,bq “ Wi2p´yi,p`1 ´ yi1,bq (7.6)

for b “ q, q ` 1 if |yi,p ´ yi,p`1| ď |yi1,q ´ yi1,q`1|, and

Wi2p´yi,a ´ yi1,qq “ Wi2p´yi,a ´ yi1,q`1q (7.7)

for a “ p, p ` 1 if |yi,p ´ yi,p`1| ě |yi1,q ´ yi1,q`1|.

Proof. By permutation we may set i “ 1, i
1 “ 2, i
2 “ 3. Suppose that 0 ď p1 ď k1,
0 ď p2 ď k2, 0 ď p3 ď k3 have the same parity. By Conjecture 6.8(ii) we have
ÿ

j1“p1,p1`1
 ÿ

j2“p2,p2`1
p´1q
j1`j2 sgnpy1,j1 ` y2,j2 ` y3,p3q

“ ÿ

j1“p1,p1`1
 ÿ

j2“p2,p2`1
p´1q
j1`j2 sgnpy1,j1 ` y2,j2 ` y3,p3`1q;

summing over p1, p2 and noting that the contributions of j1 “ 0, j1 “ k1 ` 1, j2 “ 0, j2 “
k2 ` 1 are the same on both sides we see that

W12p´y3,p3q “ W12p´y3,p3`1q

for all 0 ď p3 ď k3; since W12p´y3,0q “ W12p`8q “ `1, we conclude (i).

Now suppose 0 ď p ď k1 and 0 ď q ď k2 have the same parity and |y1,p ´ y1,p`1| ď
|y2,q´y2,q`1|, and let 0 ď r ď k3 have the same parity as p and q. From Conjecture 6.8(ii)
we see that the pairs ty1,p, y1,p`1u, ty2,q, y2,q`1u, ty3,r, y3,r`1u have non-crossing sums,
which by Example 6.7 implies that at least one of the pairs ty1,p, y1,p`1u, ty3,r, y3,r`1u
have no inﬂuence on the triple sums. This implies that
ÿ

j“r,r`1
p´1q
j´1 sgnpy1,p ` y2,b ` y3,jq “ ÿ

j“r,r`1
p´1q
j´1 sgnpy1,p`1 ` y2,b ` y3,jq

for b “ q, q ` 1; summing in r we obtain (7.6). The claim (7.7) is proven similarly. □

This proposition is already enough to reprove the k3 “ 1 case of Conjecture 6.8 as
follows. By adding y3,1 to all of the y2,j and then sending y3,1 to zero, we may assume
that y3,1 “ 0. Then we have W13pyq “ W1pyq and W23pyq “ W2pyq for all y, and hence
by Proposition 7.3 we have W1p´y2,jq “ 0 for j “ 1, . . . , k2 and W2p´y1,jq “ 0 for
j “ 1, . . . , k1. We conclude that on the set ty P R : W1pyq “ `1u, the function W2p´yq
is locally constant and vanishes at the endpoints, thus we have the inclusion

ty P R : W1pyq “ `1u Ă ty P R : W2p´yq “ 0u. (7.8)

This inclusion is strict because the endpoints y1,j1 of the former set cannot match any
of the endpoints ´y2,j2 of the latter set due to the non-vanishing of the sums y1,j1 `
y2,j2 ` y3,1 “ y1,j1 ` y2,j2. We conclude (using Lemma 7.2) that for suﬃciently large T ,
we have ż 8

´T W1pyq dy ă ż 8

´T p1 ´ W2p´yqq dy

and the desired claim (6.2) then follows from (7.2), (7.3).

INTEGRATION APPROACH TO SQUARE PEG PROBLEM 47

Remark 7.4. The above arguments crucially used the hypothesis in Conjecture 6.8(i).
Indeed, the conjecture is false without this hypothesis; a simple counterexample is when
k1 “ 3, k2 “ k3 “ 1, y1,1 “ ´1, y1,2 “ ´4, y1,3 “ ´2, and y2,1 “ y3,1 “ 0.

We can partially extend these arguments to cover the cases k1, k2, k3 ą 1 as follows. We
use Lemma 7.2 to partition

t0, . . . , k1 ` 1u ˆ t0, . . . , k2 ` 1u “ V 0
12 Y V `1
12 (7.9)

where V `1
12 (resp. V 0
12) consists of those pairs pp, qq for which W3p´y1,p´y2,qq “ `1 (resp.
W3p´y1,p ´ y2,qq “ 0). We will work primarily on V `1
12 , although much of the analysis
below also applies to V 0
12. The set V 0
12 is a combinatorial analogue of the compact set
K in the end of Section 5, while V `1
12 plays the role of the 1-boundaries Bpπ3q˚U that
avoid this compact set.

The set V `1
12 avoids the boundary of t0, . . . , k1 ` 1u ˆ t0, . . . , k2 ` 1u and is thus actually
a subset of t1, . . . , k1u ˆ t1, . . . , k2u. We place a directed graph G
`1
12 “ pV `1
12 , E`1
12 q on
the vertex set V `1
12 as follows. If 0 ď p ď k1 and 0 ď q ď k2 have the same parity and
|y1,p ´ y1,p`1| ď |y2,q ´ y2,q`1|, we connect pp, bq to pp ` 1, bq whenever b P tq, q ` 1u is
odd with pp, bq P V `1
12 , and connect pp ` 1, bq to pp, bq whenever b P tq, q ` 1u is even with
pp, bq P V `1
12 . If instead p, q have the same parity and |y1,p ´ y1,p`1| ą |y2,q ´ y2,q`1|, we
connect pa, qq to pa, q ` 1q whenever a P tp, p ` 1u is odd with pa, qq P V `1
12 and connect
pa, q ` 1q to pa, qq whenever a P tp, p ` 1u is even with pa, qq P V `1
12 . By Lemma 7.3(ii),
this construction only produces edges that start and end in V `1
12 ; indeed, every point
pa, bq in tp, p ` 1u ˆ tq, q ` 1u X V `1
12 will be connected to another point in this set,
either by an outgoing edge (if a ` b has the opposite parity to p or q) or an incoming
edge (if a ` b has the same parity as p or q). Applying this procedure to each square
tp, p ` 1u ˆ tq, q ` 1u with 0 ď p ď k1 and 0 ď q ď k2 the same parity, one obtains a
directed graph G
`1
12 “ pV `1
12 , E`1
12 q in which each vertex has exactly one outgoing edge
and one incoming edge; thus G
`1
12 decomposes into disjoint simple directed cycles. Any
one of these cycles γ can enter a vertical line tau ˆ t0, . . . , k2 ` 1u from the left only
when the second coordinate is odd, and from the right only when the second coordinate
is even; thus γ will intersect such a vertical line at odd second coordinates the same
number of times as at even second coordinates; that is to say
ÿ

b:pa,bqPγp´1q
b “ 0.

Similarly for every horizontal line, thus
ÿ

a:pa,bqPγp´1q
a “ 0

for all 0 ď b ď k2 ` 1. As a consequence, we have
ÿ

pa,bqPγp´1q
a`bpy1,a ` y2,bq “ 0

for each cycle γ, and hence on summing in γ
ÿ

pa,bqPV `1
12
 p´1q
a`bpy1,a ` y2,bq “ 0

48 TERENCE TAO

and hence by (7.9)

ÿ

pa,bqPV 0
12p´1q
a`bpy1,a ` y2,bq “
 k1ÿ

j“1
p´1q
j´1y1,j `
 k2ÿ

j“1
p´1q
j´1y2,j. (7.10)

Next, we claim the identity
ÿ

pa,bqPV `1
12
 p´1q
a`b sgnpy1,a ` y2,b ` y3,rq “ 0 (7.11)

for all 0 ď r ď k3 ` 1. This is certainly the case for r “ 0, so it suﬃces to show that
ÿ

pa,bqPV `1
12
 p´1q
a`b sgnpy1,a ` y2,b ` y3,rq “ ÿ

pa,bqPV `1
12
 p´1qa`bpsgnpy1,a ` y2,b ` y3,r`1q

for all 0 ď r ď k3. Fix such a r. By breaking up V `1
12 into squares, it suﬃces to show
that ÿ

pa,bqPtp,p`1uˆtq,q`1uXV `1
12
 p´1q
a`b sgnpy1,a ` y2,b ` y3,rq

“ ÿ

pa,bqPtp,p`1uˆtq,q`1uXV `1
12
 p´1q
a`b sgnpy1,a ` y2,b ` y3,r`1q (7.12)

whenever 0 ď p ď k1 and 0 ď q ď k2 have the same parity as r. Suppose ﬁrst that
|y1,p`1 ´ y1,p| ď |y2,q`1 ´ y2,q|, then by Lemma 7.3(ii), the set tp, p ` 1u ˆ tq, q ` 1u X V `1
12
is the union of horizontal lines tpp, bq, pp ` 1, bqu. It then suﬃces to show that for each
such line, we have ÿ

aPtp,p`1u;cPtr1,r1`1u
p´1q
a`c sgnpy1,a ` y2,b ` y3,cq “ 0 (7.13)

for all 0 ď r1 ď k3 with the same parity as p, q; but from Conjecture 6.8(ii) and
Example 6.7, the sign of the triple sums of ty1,p, y1,p`1u, ty2,q, y2,q`1u, ty3,r1, y3,r1`1u
are not inﬂuenced by one of ty1,p, y1,p`1u or ty3,r1, y3,r1`1u, giving (7.13). The case when
|y1,p`1´y1,p| ą |y2,q`1´y2,q| is treated similarly (using vertical lines in place of horizontal
lines).

If we now deﬁne the modiﬁed winding number

W 0
12pyq :“ ÿ

pa,bqPV 0
12p´1q
a`bpsgnpy1,a ` y2,b ´ yq

then we see from (7.11) and Proposition 7.3 that

W 0
12p´y3,rq “ 0 (7.14)

for all 0 ď r ď k3 ` 1. From (7.10) and Fubini’s theorem we see that
ż 8

´T W 0
12pyq dy “
 k1ÿ

j“1p´1qj´1y1,j `
 k2ÿ

j“1
p´1q
j´1y2,j ` T

INTEGRATION APPROACH TO SQUARE PEG PROBLEM 49

and ż T

´8p1 ´ W 0
12pyqq dy “ ´
 k1ÿ

j“1
p´1q
j´1y1,j `
 k2ÿ

j“1p´1qj´1y2,j ` T (7.15)

for suﬃciently large T .

On the set ty : W3p´yq “ `1u, we now see that the function W 0
12 is locally constant
(since, by deﬁnition of W 0
12, all the discontinuities y1,p ` y2,q of W 0
12 lie in the set ty :
W3p´yq “ 0u) and equal to 0 on the boundary (thanks to (7.14)). This gives the
inclusion ty : W3p´yq “ `1u Ă ty : W 0
12pyq “ 0u (7.16)
which generalises (a permutation of) (7.8). This gives some (but not all) cases of
Conjecture 6.8:

Proposition 7.5. Conjecture 6.8 holds under the additional assumption that the func-
tion W 0
12pyq ď 1 for all y.

This case of Conjecture 6.8 is analogous to the case of (5.8) when the 2-cycle Ω appearing
in that inequality has a deﬁnite sign.

Proof. The inclusion (7.16) is strict, because the endpoints of the set ty : W3p´yq “ `1u
cannot agree with any of the endpoints of ty : W 0
12pyq “ 0u. We conclude (using Lemma
7.2 and the hypothesis W 0
12 ď 1) that for suﬃciently large T that
ż T

´8 W3p´yq dy ă ż T

´8p1 ´ W 0
12pyqq dy

and the desired inequality (6.2) then follows from (7.2), (7.15). □

This observation can handle several further cases of Conjecture 6.8 (e.g. the perturbative
regime in which the y2,1, . . . , y2,k2 are very small compared to the diﬀerences between the
y1,1, . . . , y1,k1). Unfortunately it is possible for W 0
12 to exceed 1, which means that one
cannot resolve Conjecture 6.8 purely on the strength of the inclusion (7.16). However,
it appears from numerous examples that whenever this occurs, a signiﬁcant portion of
the set ty : W12pyq
0 “ 0u is “closed oﬀ” from W3, in that the set ty : W3p´yq “ `1u is
prohibited from entering that portion, which restores the truth of Conjecture 6.8; the
author was able to make this statement rigorous in the case k3 “ 3 by a rather lengthy
and ad hoc argument, which unfortunately does not seem to extend to the general
case. Rather than present this (somewhat unenlightening) argument here, we give an
example to illustrate this “closing oﬀ” phenomenon. We will take k1 “ k2 “ 3 and
y1,1 ă y1,2 ă y1,3 and y2,1 ă y2,2 ă y2,3 (this ordering is consistent with the non-crossing
hypothesis (i)). We will assume that we are in the “almost perturbative setting” in
which the nine sums sj1,j2 :“ y1,j1 ` y2,j2 for j1, j2 “ 1, 2, 3 are ordered by the relations

s1,1 ă s1,2 ă s1,3, s2,1 ă s2,2 ă s2,3 ă s3,1 ă s3,2 ă s3,3.

thus the only uncertainty in the ordering of these nine sums arises from the relative
positions of s1,3 and s2,1; clearly both orderings are possible. These relations imply the

50 TERENCE TAO

further inequalities
 y2,2 ´ y2,1, y2,3 ´ y2,2 ă y1,2 ´ y1,1, y1,3 ´ y1,2.

By this and many applications of Proposition 7.3(ii) we can see that W3p´y1,p ´y2,qq “ 0
for all p, q P t0, 1, 2, 3, 4u, hence V `1
12 is empty and W 0
12 “ W12 in this case.

First suppose one is in the “fully perturbative” setting where s1,3 ă s2,1 (this for instance
occurs when all the y2,1, y2,2, y2,3 are small compared to the diﬀerences y1,2 ´ y1,1 and
y1,3 ´ y1,2). In this case the winding number W12 “ W 0
12 only takes the values 0 and 1,
with the former occurring on the intervals

ps1,1, s1,2q Y ps1,3, s2,1q Y ps2,2, s2,3q Y ps3,1, s3,2q Y ps3,3, `8q, (7.17)

and Proposition 7.5 gives (6.2) in this case. In this case one can make the error in (6.2)
arbitrarily small; for instance if one takes k3 “ 9 and

y3,1 “ ´s1,1 ´ ε
y3,2 “ ´s1,2 ` ε
y3,3 “ ´s1,3 ´ ε
y3,4 “ ´s2,3 ` ε
y3,5 “ ´s2,2 ´ ε
y3,6 “ ´s2,1 ` ε
y3,7 “ ´s3,1 ´ ε
y3,8 “ ´s3,2 ` ε
y3,9 “ ´s3,3 ´ ε

for some suﬃciently small ε ą 0, one can check that the hypotheses of Conjecture 6.8
hold, and the left and right-hand sides of (6.2) diﬀer by 9ε; see Figure 12.

Now suppose that s1,3 ě s2,1. In this case, W12 “ W 0
12 now takes the value of 0 on the
intervals ps1,1, s1,2q Y ps2,2, s2,3q Y ps3,1, s3,2q Y ps3,3, `8q
but is additionally equal to `2 on the interval ps3,1, s2,3q. The argument used to prove
Proposition 7.5 then fails to establish (6.2), incurring instead an additional additive
error of s1,3 ´ s2,1. However, in this case the portion ps2,2, s2,3q of ty : W12pyq “ 1u
now becomes “closed oﬀ” from the points ´y3,1, . . . , ´y3,k3, in the sense that none of
the ´y3,j can lie in this interval, which also implies that W3p´yq cannot equal 1 in
this interval either. This lets one improve the bound arising from (7.16) by a factor of
s2,3 ´ s2,2, which exceeds the loss of s1,3 ´ s2,1 incurred previously because s2,1 ą s1,2.
This restores Conjecture 6.8 in this case. To see why none of the ´y3,j lie in ps2,2, s2,3q,
suppose for contradiction that this were not the case, and let 1 ď p ď k3 be the largest
index such that ´y3,p P ps2,2, s2,3q. This index p cannot equal k3, because this would
imply that the pairs ty1,1, y1,2u, ty2,3, y2,4u and ty3,p, y3,p`1u have crossing sums (only one
of the eight sums from these pairs is positive), contradicting Conjecture 6.8(ii). The
same argument excludes the case when p is odd and less than k3, since in this case
y3,p`1 avoids ps2,2, s2,3q by hypothesis, and also avoids ps1,3, s2,2q since W 0
12 equals `1
there (here is where we use s1,3 ě s2,1), so one has an odd number of positive sums in
this case. Finally, the index p cannot be even, because ´y3,p`1 lies outside ps2,2, s2,3q

INTEGRATION APPROACH TO SQUARE PEG PROBLEM 51

Figure 12. The perturbative case. The solid line represents those
sums px, y1 ` y2q, where px, y1q lies on a simple curve passing through
p0, y1,1q, p0, y1,2q, p0, y1,3q, and px, y2q lies on a simple curve passing through
p0, y2,1q, p0, y2,2q, p0, y2,3q. Note how the entire region (7.17) (viewed as a
subset of the y-axis, drawn here as a dashed line) lies above the solid line,
in the sense that it is connected to p0, T q for arbitrarily large and negative
´T . The points p0, ´y3,iq for i “ 1, . . . , 9 (not pictured) lie just above
curve in this region.

and also outside ps3,2, s3,3q (as W12 equals `1 there) and hence the triple ty1,2, y1,3u,
ty2,2, y2,3u, ty3,p, y3,p`1u would be crossing (this has an odd number of positive sums),
again contradicting Conjecture 6.8(ii). Thus Conjecture 6.8 holds in all of these cases.
More generally, the author has observed numerically that every creation of a region
where W 0
12 exceeds 1 will invariably be accompanied by a larger region of tW 0
12pyq “ 0u
which is now “closed oﬀ” from W3, and was able to verify this claim rigorously when
k1 “ 3 or k2 “ 3 by ad hoc methods, but was unable to see how to establish such a
claim in general.
 References

[1] J. W. Alexander, Topological Invariants of Knots and Links, Transactions of the American Math-
ematical Society. 30 (1928), 275–306.
[2] J. Cantarella, E. Denne, J. McCleary, Transversality for Conﬁguration Spaces and the “Square-
Peg” Theorem, preprint. arXiv:1402.6174
[3] C. M. Christensen, A square inscribed in a convex ﬁgure, Matematisk Tidsskrift B 1950 (1950),
22–26.

52 TERENCE TAO

Figure 13. The non-perturbative case. There is now a region of winding
number `2 between s2,1 and s1,3. But to compensate for this, the region
between s2,2 and s3,1, which still has a winding number of 0, has been cut
oﬀ from p0, T q for large T . This cut-oﬀ region is necessarily larger (as
measured as a portion of the y-axis) than the region of winding number
`2.

[4] A. Emch, Some properties of closed convex curves in a plane, Amer. J. Math. 35 (1913), 407–412.
[5] A. Emch, On the medians of a closed convex polygon, Amer. J. Math. 37 (1915), 19–28.
[6] A. Emch, On some properties of the medians of closed continuous curves formed by analytic arcs,
Amer. J. Math. 38 (1916), no. 1, 6–18.
[7] R. Fenn, The table theorem, Bull. London Math. Soc. 2 (1970), 73–76.
[8] H. W. Guggenheimer, Finite sets on curves and surfaces, Israel J. Math. 3 (1965), 104–112.
[9] A. Hatcher, Algebraic topology. Cambridge University Press, Cambridge, 2002.
[10] C. M. Hebbert, The inscribed and circumscribed squares of a quadrilateral and their signiﬁcance
in kinematic geometry, Ann. of Math. (2) 16 (1914/15), no. 1-4, 38–42.
[11] R. P. Jerrard, Inscribed squares in plane curves, Trans. Amer. Math. Soc. 98 (1961), 234–241.
[12] R. N. Karas¨ev, On two conjectures of Makeev ; translated from Zap. Nauchn. Sem. S.-Peterburg.
Otdel. Mat. Inst. Steklov. (POMI) 415 (2013), Geometriya i Topologiya. 12, 5–14 J. Math. Sci.
(N.Y.) 212 (2016), no. 5, 521–526.
[13] S. K. Lando, A. K. Zvonkin, Plane and projective meanders, Conference on Formal Power Series
and Algebraic Combinatorics (Bordeaux, 1991). Theoret. Comput. Sci. 117 (1993), no. 1-2, 227–
241.
[14] V. V. Makeev, On quadrangles inscribed in a closed curve, Math. Notes 57 (1995), no. 1-2, 91–93.
[15] B. Matschke, Equivariant topology methods in discrete geometry, Ph.D. thesis, Freie Universit¨at
Berlin, 2011.
[16] B. Matschke, A survey on the square peg problem, Notices Amer. Math. Soc. 61 (2014), no. 4,
346–352.
 INTEGRATION APPROACH TO SQUARE PEG PROBLEM 53

[17] M. J. Nielsen, S. E. Wright, Rectangles inscribed in symmetric continua, Geom. Dedicata 56
(1995), no. 3, 285–297.
[18] I. Pak, Lectures on Discrete and Polyhedral Geometry, http://math.ucla.edu/„pak/book.htm,
2010.
[19] V. Pettersson, H. Tverberg, P. ¨Osterg˚ard, A Note on Toeplitz’ Conjecture, Disc. Comp. Geom. 51
(2014), 722–728.
[20] F. Sagols, R. Mar´ın, The inscribed square conjecture in the digital plane, Combinatorial Image
Analysis, Lecture Notes in Comput. Sci., vol. 5852, Springer, 2009, 411–424.
[21] F. Sagols, R. Mar´ın, Two discrete versions of the inscribed square conjecture and some related
problems, Theoret. Comput. Sci. 412 (2011), no. 15, 1301–1312.
[22] L. G. Schnirelman, On some geometric properties of closed curves, Usp. Mat. Nauk 10 (1944),
34–44.
[23] Steinberg, Robert, A general ClebschGordan theorem, Bulletin of the American Mathematical
Society, 67 (1961), 406–407.
[24] W. R. Stromquist, Inscribed squares and squarelike quadrilaterals in closed curves, Mathematika
36 (1989), 187–197.
[25] T. Tao, Finite time blowup for a supercritical defocusing nonlinear wave system, to appear, Anal.
PDE..
[26] O. Toeplitz, Ueber einige Aufgaben der Analysis situs, Verhandlungen der Schweizerischen Natur-
forschenden Gesellschaft in Solothurn 4 (1911), 197.
[27] V. Po´enaru, What is ... an inﬁnite swindle?, Not. Amer. Math. Soc. 54 (2007), 619–622.
[28] S. Vre´cica, R. T. ˇZivaljevi´c, Fulton-MacPherson compactiﬁcation, cyclohedra, and the polygonal
pegs problem, Israel J. Math. 184 (2011), no. 1, 221–249.
[29] K. Zindler, ¨Uber konvexe Gebilde, Monatshefte f¨ur Mathematik und Physik 31 (1921), 25–56.

UCLA Department of Mathematics, Los Angeles, CA 90095-1555.

E-mail address: tao@math.ucla.edu
