<!-- source: https://arxiv.org/pdf/1804.00740 | converted from PDF -->

arXiv:1804.00740v4  [math.MG]  8 Jul 2019A Trichotomy for Rectangles Inscribed in
Jordan Loops

Richard Evan Schwartz ∗

July 9, 2019

Abstract

We prove a general structural theorem about rectangles inscribed
in Jordan loops. One corollary is that all but at most 4 points of any
Jordan loop are vertices of inscribed rectangles. Another corollary is
that a Jordan loop has an inscribed rectangle of every aspect ratio
provided it has 3 points which are not vertices of inscribed rectangles.

1 Introduction

A Jordan loop is the image of the circle under a continuous injective map into
the plane. O. Toeplitz conjectured in 1911 that every Jordan loop contains 4
points which are the vertices of a square. This is often called the Square Peg
Conjecture. An aﬃrmative answer is known in many special cases. In 1913,
Emch [Emch] proved the result for convex curves. In 1944, L. G. Shnirlmann
[Shn] proved the result for suﬃciently smooth curves. In 1961, R. Jerrald
[Jer] extended this to the case of C 1 curves. Recently T. Tao [Ta] proved
the result for special curves having even lower regularity. The above is a
very partial survey of the literature. The 2014 survey paper by B. Matschke
[Ma1] and the recent book by I. Pak [P] have extensive discussions of the
history of the Square Peg Conjecture and many additional references.
There is also some work done in the case of rectangles. In 1977, H.
Vaughan [Va] gave a proof that every Jordan loop has an inscribed rectangle.

∗ Supported by N.S.F. Research Grant DMS-1204471

1

A recent paper of C. Hugelmeyer [H] combines Vaughan’s basic idea with
some very modern knot theory results to show that a smooth Jordan loop
always has an inscribed rectangle of aspect ratio √3. The recent paper [AA]
proves that any quadrilateral inscribed in a circle can (up to similarity) be
inscribed in any convex smooth curve. See also [Ma2]. In the recent paper
[ACFSST], the authors show that every Jordan Loop contains a dense set
of points which are vertices of inscribed rectangles. For additional work on
inscribed rectangles, see [Mak1], [Mak2], and [MW].
Relatedly, one can consider the situation for triangles. In 1980, M. Mey-
erson [M] proved that all but at most 2 points of any Jordan loop are vertices
of inscribed equilateral triangles. This result is sharp because two points of a
suitable isosceles triangle are not vertices of inscribed equilateral triangles. In
1992, M. Neilson [N] proved that an arbitrary Jordan loop contains a dense
set of points which are vertices of inscribed triangles of any given shape.
We are going to prove a strong version of Meyerson’s Theorem for rect-
angles. Let I(γ) denote the space of all labeled rectangles inscribed in γ.
We always label a rectangle R so that the vertices of R go counterclockwise
around R. We orient γ so that it goes counterclockwise around the region in
the plane it bounds. The space I(γ) is naturally a subset of R8 = (R2)4.
We call a rectangle R inscribed in γ graceful if the cyclic order imparted
on the vertices of R by the ordering on γ coincides with the ordering we
have already given to the vertices of R. Let G(γ) ⊂ I(γ) denote the space of
gracefully inscribed labeled rectangles.
The aspect ratio of a rectangle in I(γ) is the length of the second side
divided by the length of the ﬁrst side. Let ρ(S) denote the union of all the
aspect ratios of rectangles in S. Given S ⊂ I(γ), let V (γ, S) ⊂ γ denote the
subset of γ consisting of points which are vertices of rectangles in S.

Theorem 1.1 (Trichotomy) Let γ be an arbitrary Jordan loop. Then I(γ)
contains a connected set S satisfying one of the following.

1. Members of S have uniformly large area, V (γ, S) = γ, and 1 ∈ ρ(S).

2. Members S have uniformly large diameter, ρ(S) = (0, ∞), and V (γ, S)
contains all but at most 4 points of γ.

3. The set S has members of every suﬃciently small diameter, and V (γ, S)
contains all but at most 2 points of γ.

Moreover, S ⊂ G(γ).
 2

We mention three corollaries. The ﬁrst two corollaries are immediate,
and we will prove the third one in §2.7.

Corollary 1.2 Let γ be any Jordan loop. Then all but at most 4 points of
γ are vertices of rectangles gracefully inscribed in γ.

This result is sharp: There are 4 points of a non-circular ellipse which are
not vertices of any inscribed rectangle.

Corollary 1.3 Let γ be any Jordan loop. If γ has 3 points which are not
vertices of gracefully inscribed rectangles then γ has gracefully inscribed rect-
angles of every aspect ratio.

Corollary 1.4 Let γ be any Jordan loop and let µ be any non-atomic mea-
sure on γ having mass 1. Then γ has a gracefully inscribed rectangle γ such
that the total µ-measure of each pair opposite sides of γ cut oﬀ by R is 1/2.

Remarks:
(1) I describe the cases in the Trichotomy Theorem respectively as elliptic,
hyperbolic, and parabolic, because the geometry of the situation seems to
vaguely resemble the action of these kinds of linear transformations on R2.
(2) Note that there are examples, such as the circle, for which both the hy-
perbolic and elliptic cases occur.
(3) I conjecture that the parabolic case cannot actually occur. This conjec-
ture immediately implies the Square Peg Conjecture.
(4) The elliptic case occurs for any curve with 4-fold rotational symmetry
but I conjecture that the hyperbolic case also occurs for every Jordan loop.
This conjecture implies the much stronger result that every Jordan loop has
an inscribed rectangle of every aspect ratio – a conjecture that is not even
known in the smooth or polygonal cases.
(5) One could view Corollary 1.2 as a version of Meyerson’s Theorem [M] for
rectangles, though our proof is much diﬀerent. Our recent preprint [S1] gives
a proof of Meyerson’s Theorem along the lines of the proof in this paper.
(6) The paper [ACFSST] also has Corollary 1.4 (without the graceful bit)
when γ is rectiﬁable and µ is arc-length measure normalized to have total
length 1. The methods are diﬀerent.

We prove the Trichotomy Theorem by taking a suitable limit of the polyg-
onal case. Let γ be a polygon. By an arc component of I(γ) we mean a

3

connected component of I(γ) which is homeomorphic to an arc. By proper ,
we mean that as one moves towards an endpoint of an arc component in
I(γ), the aspect ratio tends either to 0 or to ∞. Moreover, we insist that
the rectangles at each end of a proper arc accumulate on a chord of γ and
that the two chords are distinct. The left side of Figure 1 below suggests
an example of a proper arc in I(γ) when γ is an equilateral triangle. The
black segments are the two chords of accumulation. This arc actually is a
component of G(γ).

Theorem 1.5 There is an open dense subset P of polygons with the fol-
lowing property. For each γ ∈ P the space I(γ) is a piecewise smooth 1-
manifold whose arc components are proper. Moreover the aspect ratio func-
tion ρ : I(γ) → (0, ∞) is injective in a neighborhood of each smooth point of
I(γ) and, ρ
−1(1) consists entirely of smooth points.

We deﬁne 2 kinds of components of I(γ).

• A component A of I(γ) is a hyperbolic component if the aspect ratio
of the rectangles in A tends to 0 as the rectangles tend towards one
endpoint of A, and to ∞ as they tend to the other endpoint of A. The
example in Figure 1 is a hyperbolic component.

• The operation of cyclically relabeling gives a Z/4 action on the space
I(γ) which has no ﬁxed points. We call a component of I(γ) elliptic if
it is stabilized by the Z/4 action. These components are loops.

We call a component of I(γ) global if it is either hyperbolic or elliptic. The
reason for the name is that V (γ, S) contains all but at most 4 points of
γ when γ is hyperbolic (Lemma 2.3) and all points of γ when γ is elliptic
(Lemma 2.8).
The left and right hand sides of Figure 1 respectively suggest a hyperbolic
and an elliptic component. The ﬁgure on the right, drawn by hand, may
have small inaccuracies. The basic construction is to have the centers of
the rectangles wind once around a small central curve, while the rectangles
themselves rotate one quarter of the way around and return to their original
location but with the corresponding cyclic relabeling. When this operation is
repeated 4 times, one has an elliptic component. It would be simpler to keep
the centers ﬁxed, but I wanted to show an example without 4 fold rotational
symmetry.
 4
 11

1 1

2

2,3
 2
 2

3
 3

3,4
 4

4
 4
 34

1 2

Figure 1: A hyperbolic component and an elliptic component.

The relabeling action permutes the various components of I(γ) and we call
the orbits of this action the unlabeled components. We deﬁne the following
quantities:

• Ω(γ) is the number of unlabelled inscribed squares.

• ΩH(γ) is the number of unlabelled hyperbolic components.

• ΩE(γ) is the number of unlabeled elliptic components.

We will establish the following equation for each γ ∈ P.

Ω(γ) + ΩH (γ) + ΩE(γ) ≡ 0 mod 2. (1)

It is well known that for the generic polygon the number of unlabeled
inscribed squares is odd. See for instance [St] or [P, Theorem 23.11]. Hence
I(γ) always contains a global component. Finally we prove the following
result.

Theorem 1.6 For γ ∈ P the only global components of I(γ) belong to G(γ).

Theorem 1.6 now implies the following result.

Theorem 1.7 For each γ ∈ P the space G(γ) contains a global component.

5

We get the Trichotomy Theorem by taking a suitable limit of Theorem 1.7.
We also mention another corollary of Theorem 1.6: A generic polygon
has an odd number of gracefully inscribed squares. See §3.4. I don’t think
that this corollary follows directly from [P, Theorem 23.11], which makes a
statement about the parity of the number of all inscribed squares.

Here is an outline of the paper. In §2 we will deduce the Trichotomy
Theorem from Theorem 1.7. Following §2, the rest of the paper is about
polygons.
In §3 we will deduce Equation 1 from Theorem 1.5.
In §4 we prove Theorem 1.5. This is really just an exercise in transver-
sality, and many methods would work.
In §5 we prove Theorem 1.6.
We warn the reader about one persistent abuse of terminology. When we
speak of a rectangle in I(γ) (or in related conﬁguration spaces) we mean the
rectangle corresponding to a member of I(γ) and not some kind of conﬁgu-
ration of 4 elements of I(γ). We hope that this does not cause confusion.

One thing I would like to mention is that I discovered all the results
in this paper by computer experimentation. I wrote a Java program which
computes the space G(γ) in an eﬃcient way for polygonal loops γ having up
to about 20 sides.
I would like to thank Arseniy Akopyan, Peter Doyle, Cole Hugelmeyer,
and Sergei Tabachnikov for helpful and interesting conversations related to
this paper. I would also like to thank the referee of this paper for very
helpful comments. I would like to thank the National Science Foundation,
the Simons Foundation, and the Isaac Newton Institute for their generous
support while I worked on this paper.

6

2 The Trichotomy Theorem

In this chapter we deduce the Trichotomy Theorem from Theorem 1.7 using
a limiting argument. We begin with some preliminary material on point-set
topology.

2.1 Hausdorﬀ Limits

Suppose that C is a compact metric space. Let XC denote the set of closed
subsets of C. We deﬁne the Hausdorﬀ distance between closed A, B ⊂ C to
be the inﬁmal ǫ such that each of the two sets is contained in the ǫ-tubular
neighborhood of the other one. This deﬁnition makes XC into a compact
metric space.

Lemma 2.1 Let {An} be a sequence of nonempty closed connected subsets of
C. Suppose that this sequence converges to a subset A ⊂ C in the Hausdorﬀ
metric. Then A is connected.

Proof: If A is disconnected, there are disjoint open sets U, V ⊂ C such that
A ⊂ U ∪ V , and A ∩ U and A ∩ V are both not empty. The following pairs
of sets are compact and disjoint:

(A, C − U − V ) (A ∩ U, C − U), (A ∩ V, C − V ).

(The set A ∩ U is compact because A ∩ U = A − V . Similarly for A ∩ V .)
Hence, there is some ǫ > 0 such that every point in the ﬁrst set of a pair is
at least ǫ from every point in the second pair. Therefore, for all suﬃciently
large n, the set An intersects both U and V . Since An is connected, this
is only possible if C − U − V contains a point xn ∈ An. But then xn is at
least ǫ from A, independent of the choice of n. This contradicts the fact that
An → A in the Hausdorﬀ metric. ♠

Remarks:
(1) Since C is compact, the set A must be non-empty, by the Bolzano-
Weierstrass Theorem.
(2) In our application the sets An will be path connected. However, there is
no guarantee that the limit A is path connected as well. Consider a sequence
of path approximations to the topologist’s sine curve.

7

2.2 The Circular Invariant

Let S1 be the unit circle. Let |α| denote the arc length of an arc α ⊂ S1.
Let Σ ⊂ (S1)4 denote the subset of distinct labeled quadruples, which go
counterclockwise around S1. We call these cyclic quadrilaterals. Let σk be
the kth vertex of σ. Any σ ∈ Σ deﬁnes arcs α0, α1, α2, α3 with αk ⊂ S1 − σ
having endpoints σk and σk+1. The indices are taken mod 4. We write αk(σ)
when we want to emphasize the dependence on σ.
We deﬁne the circular invariant Λ : Σ → (0, ∞) by

Λ(σ) = |α0| + |α2|
|α1| + |α3| . (2)

When σ consists of the vertices of a rectangle, Λ(σ) is the aspect ratio of this
rectangle. Otherwise Λ(σ) is only vaguely related to an aspect ratio.

Lemma 2.2 Let {σn} be a sequence of cyclic quadrilaterals having diameter
greater than some positive δ for all n, and circular invariant converging to
0. Then the arcs α0(σn) and α2(σn) shrink to points and the arcs α1(σn) and
α3(σn) remain uniformly large.

Proof: The hypotheses imply that limn→∞ |α0(σn)| + |α2(σn)| = 0. By the
triangle inequality, min(|α1(σn)|, |α3(σn)|) > δ/2 for n large. ♠

We call A ⊂ Σ extensive if A is connected and Λ(A) = (0, ∞).

Lemma 2.3 If A is extensive then all but at most 4 points of S1 are vertices
of members of A. If, additionally, A contains elements of arbitrarily small
diameter then all but at most 2 points of S1 are vertices of members of A.

Proof: Let πk : A → S1 be the map such that πk(σ) = σk, the kth vertex.
The set Jk = πk(Σ) is connected, and therefore either an open arc, a closed
arc, a half-open arc, or all of S1. If B = S1 − ⋃ Jk contains more than 4
points, there is some interval B′ ⊂ B which has an endpoint in common with
Jk and an endpoint in common with Jk+1 for some k. But then B′ ⊂ αk(σ)
for all σ ∈ A. This bounds Λ(A) away from 0 or ∞, depending on the parity
of k, a contradiction.
If B has at least 3 points, then each member of A is a cyclic quadrilat-
eral which nontrivially intersects each of 3 disjoint circular arcs. There is a
uniform positive lower bound to the diameter of such cyclic quadrilaterals. ♠

8

2.3 A Compactness Result

For K ≥ 1 let Σ(K) = Σ ∩ Λ−1([1/K, K]). (3)

Note that Σ(K) is not compact because for any unit complex number u with
positive imaginary part, the cyclic quadrilateral (1, u, −1, u) lies in Σ(1). In
spite of this problem, we will prove a compactness result that involves Σ(K).
Let γ be a general Jordan loop. We ﬁx, once and for all, some homeo-
morphism φ : S1 → γ. In [Tv], Tverberg gives a way to approximate γ by a
sequence {γn} of parametrized embedded polygons so that the parametriza-
tions φn : S1 → γn converge uniformly to φ. Let Γ denote the set of σ ∈ Σ
such that φ(σ) is the vertex set of a rectangle in G(γ), the space of rectangles
gracefully inscribed in γ. Likewise deﬁne Γn relative to φn and γn.

Lemma 2.4 For each ﬁxed K ≥ 1 there is a compact subset C(K) ⊂ Σ such
that Γn ∩ Σ(K) ⊂ C(K) for all n.

Proof: If this is false then we can pass to a subsequence and cyclically
relabel so that one of the following two things is true.

1. There is a sequence {σn}, with σn ∈ Γn ∩Σ(K), such that |α0(σn)| → 0.

2. There is a sequence {σ′
n} with σ′
n ∈ Γ1 ∩ Σ(K), such that |α0(σ′
n)| → 0.

Consider Case 1. Let Rn be the rectangle in G(γn) corresponding to σn
We claim that |α1(σn)| → 0 as well. If not, then the denominator of the
expression for A(σn) in Equation 2 is uniformly bounded away from 0. But
then so is the numerator. Hence |α2(σn)| is uniformly large. Since φn → φ
uniformly, the side of Rn corresponding to α0(σn) shrinks to a point but
the opposite side corresponding to α2(σn) does not. This is impossible for a
sequence of rectangles. This proves our claim. But now we can repeat the
same argument twice more to show that |αk(σn)| → 0 for k = 0, 1, 2, 3. This
contradicts the fact ∑3
k=0 |αk(σn)| = 2π.
Case 2 is really just an instance of Case 1 relative to the sequence of
polygons {γ′
n}, the sequence of maps {φ′
n}, and the limit φ′ : S1 → γ′. Here
(somewhat trivially)

γ′ = γ′
1 = γ′
2 = γ′
3 = ... = γ1, φ′ = φ′
1 = φ′
2 = φ′
3 = ... = φ1.

So, the argument in Case 1 takes care of Case 2. ♠

9

2.4 Limits of Hyperbolic Components

We keep the notation from the previous sections. In this section we will
consider the special case that G(γn) has a hyperbolic component Hn for all
n. Recall that A ⊂ Σ is extensive if A is connected and Λ(A) = (0, ∞).

Lemma 2.5 The subset An ⊂ Γn corresponding to Hn is extensive.

Proof: Each end of Hn consists of rectangles which accumulate on some
chord of γn. Hence, the circular invariants of the corresponding cyclic quadri-
laterals tend to 0 or ∞, with one case happening at one end and the other
case happening at the other end. Hence Λ(An) = (0, ∞). Also, An is home-
omorphic to the arc Hn and hence also connected. ♠

Lemma 2.6 Γ contains an extensive subset A.

Proof: We keep the same notation as in the previous lemma. To make our
proof more ﬂexible, we only use the property that An is path connected,
and contains a member with circular invariant n and a member with circular
invariant 1/n. Since An is connected, An contains some σn with circular
invariant 1. For each K = 1, ..., n we deﬁne An(K) to be the minimal arc of
An which contains σn and has endpoints with circular invariant 1/K and K
respectively. By construction An(K) is deﬁned for n ≥ K and furthermore
An(K) ⊂ C(K), the compact set from Lemma 2.4. Finally,

An(1) ⊂ ... ⊂ An(n) (4)

For ﬁxed K, the sequence {An(K)} is a sequence of closed connected
subsets of the compact set C(K). Using Cantor’s diagonal trick, and com-
pactness, we can ﬁnd a subsequence so that for each K = 1, 2, 3, ... the
sequence {An(K)} converges to some A(K) ⊂ C(K) as n → ∞. By Lemma
2.1 the set A(K) is connected. Moreover, A(K) contains elements of circular
invariant K and 1/K. Each σ ∈ A(K) is such that φ(σ) is the vertex set of
a non-degenerate limit of gracefully inscribed rectangles. Hence σ ∈ Γ. In
short, A(K) ⊂ Γ. Equation 4 gives us A(2) ⊂ A(3) ⊂ A(4).... The nested
union of connected sets is connected. Therefore A = ⋃
K A(K) is connected.
By construction A is extensive and A ⊂ Γ. ♠

10

2.5 Limits of Elliptic Components

We continue with the notation above. This time we treat the special case
where G(γ) has an elliptic component En for all n. We call the sequence
{En} steady if there is a uniform positive lower bound to the side length of
any rectangle in any G(γn), independent of n, and otherwise wobbly.

Lemma 2.7 If {En} is wobbly then Γ contains an extensive set A.

Proof: Let An ⊂ Σ be the set which corresponds to En. Again, An is con-
nected. It cannot be the case that the circular invariants of members of An
are uniformly bounded away from 0 and ∞. Otherwise, the lack of diam-
eter bound contradicts Lemma 2.4. Therefore, after taking a subsequence,
we can arrange that An either has a member with circular invariant n or a
member with circular invariant 1/n. Given the invariance of An under cyclic
relabeling, we see that An has a member with circular invariant 1/n and a
member with circular invariant n. This is all we used in the proof of Lemma
2.6. So, the same proof works here as well. ♠

Lemma 2.8 We have 1 ∈ ρ(En) and V (En, γn) = γn.

Proof: Recall that ρ is the aspect ratio. Since En is invariant under cyclic
relabeling, we have that r ∈ ρ(En) iﬀ 1/r ∈ ρ(En). Since En is connected,
1 ∈ ρ(En). This is the ﬁrst claim.
Let vk(R) denote the kth vertex of a rectangle R. We take indices mod
4. Choose any rectangle R0 ∈ En. Since En is an elliptic component, there is
a path {Rt| t ∈ [0, 1]} of rectangles in En such that vk(Rt) connects vk(R0)
and vk+1(R0). We write vk(t) = vk(Rt). It suﬃces to prove γn = ⋃ vk([0, 1]).
For the proof, we identify γn with R/4Z so that the vertices of R0 are
[0], [1], [2], [3]. The path vk connects [k] to [k + 1]. Let ̂vk : [0, 1] → R2 be
the lift of vk such that ̂vk(0) = k. Note that ̂vk(0) ̸= ̂vk(1) ∈ Z. Hence the
interval Ik = [̂vk(0), ̂vk(1)] has length at least 1. We have

̂v0(t) < ̂v1(t) < ̂v2(t) < ̂v3(t) < ̂v1(t) + 4. ∀t ∈ [0, 1]. (5)

Equation 5 holds for t = 0 and any failure at time t would result in the
points {vk(t)} not being distinct. Hence Ik+1 = Ik + 1. This immediately im-
plies that ⋃ Ik contains an interval of length 4 and hence so does ⋃ ̂vk([0, 1]).
Hence R/4Z ⊂ ⋃ vk([0, 1]). ♠
 11

Lemma 2.9 If {En} is steady then G(γ) contains a compact connected sub-
set S such that 1 ∈ ρ(S) and V (γ, S) = γ.

Proof: Let An ⊂ Σ be the subset corresponding to En. By hypotheses
there is a single compact subset C ⊂ Σ such that An ⊂ C for all n. Passing
to a subsequence, we take the Hausdorﬀ limit A = lim An. The set A is
connected, by Lemma 2.1. We let S = φ(A). For the same reason as in the
hyperbolic case, S ⊂ G(γ).
Since 1 ∈ ρ(En) for all n, we can ﬁnd some square in S corresponding to
a limit of uniformly large squares in En. Hence 1 ∈ ρ(S).
Let p ∈ γ be any point. Let pn ∈ γn be such that pn → p. Since
V (En, γn) = γn we can ﬁnd a rectangle Rn ∈ En such that pn is a vertex of
Rn. There is a uniform lower bound to the side lengths of these rectangles.
Hence, any limit lim Rn will be a rectangle in S having p as a vertex. Hence
V (S, γ) = γ. ♠

2.6 The Main Argument

Perturbing our polygons if necessary, we can assume that each γn satisﬁes
Theorem 1.7. Passing to a subsequence, we reduce to either the hyperbolic
case considered above, the steady elliptic case, or the wobbly elliptic case.

Case 1: In the steady elliptic case, Lemma 2.9 gives Option 1 of the Tri-
chotomy Theorem.

Case 2: In the hyperbolic case or the wobbly elliptic case, Lemma 2.6 or
Lemma 2.7 guarantees that Γ contains an extensive set A. Let S ⊂ G(γ)
be the subset corresponding to A. Suppose that there is a uniform positive
lower bound to the diameters of members of A. We show that Option 2 of
the Trichotomy Theorem holds.
By Lemma 2.3, at most 4 points of S1 are not vertices of members of A.
Hence V (S, γ) contains all but at most 4 points of γ.
Since S is connected, ρ(S) is connected. Since A is extensive, A contains
a sequence {σn} of circular quadrilaterals whose circular invariant tends to
0. By Lemma 2.2, this is only possible if the two arcs α0(σn) and α2(σn) in
Equation 2 shrink to points and the other two arcs remain uniformly long.
But then the aspect ratios of the corresponding rectangles tend to 0. Hence

12

ρ(S) contains points arbitrarily near 0. The same argument shows that ρ(S)
contains points arbitrarily near ∞. Hence ρ(S) = (0, ∞).

Case 3: The only remaining case is that Γ contains an extensive set A
without the positive lower diameter bound. In this case, Lemma 2.3 shows
that at most 2 points of S1 are not vertices of members of A. Hence V (S, γ)
contains all but at most 2 points of γ. Since A contains members of every
suﬃciently small diameter, the set S does as well. This gives us Option 3 of
the Trichotomy Lemma.

2.7 Non-Atomic Measures

Here we prove Corollary 1.4. Suppose that µ is a non-atomic probability
measure on γ. Call a quadrilateral gracefully inscribed in γ nice if it cuts
γ in such a way that opposite arcs have µ-measure 1/2. We are looking
for a nice inscribed rectangle. Since µ is non-atomic, we can choose our
homeomorphism φ so that φ pushes forward arc length on S1 to 2πµ. Then
nice rectangles correspond to elements of Γ having circular invariant 1.
In Cases 2 and 3 of our proof above, the sets A are extensive and have
such cyclic quadrilaterals. So, Corollary 1.4 is true in Cases 2 and 3 above.
For Case 1, we revisit the proof of Lemma 2.9. Since An is invariant under
cyclic relabeling, we have 1 ∈ Λ(An). So, by Lemma 2.4 we can take a limit
and get 1 ∈ Λ(A). The corrsponding cyclic quadrilateral in A corresponds
to a nice rectangle in the set S.
 13

3 The Parity Equation

3.1 Outline of Proof

In this chapter we deduce Equation 1 from Theorem 1.5. Let P be the open
dense set of polygons from Theorem 1.5. We ﬁx some γ ∈ P for the entire
argument. The space I(γ) of labeled inscribed rectangles is a 1-manifold, by
Theorem 1.5. The cyclic group Z/4 acts on I(γ) by cyclically relabeling the
rectangles. Again, the labeling of a rectangle goes counterclockwise around
the the rectangle. This is a free action: No point of I(γ) is ﬁxed by the
relabeling.
For emphasis, we call the components of I(γ) labeled . An unlabeled com-
ponent is the orbit of a labeled component under the labeling action. We
deﬁne the order of a labeled component to be the number of labeled compo-
nents in its orbit – either 1, 2, or 4.
We say that a labeled rectangle R is associated with the labeled compo-
nent that contains the point representing R. We say that a labeled rectangle
R is associated to an orbit of a labeled component if it is associated to one of
the labeled components in the orbit. Finally, we say that an unlabeled rect-
angle is associated to an unlabeled component if the corresponding labeled
rectangles are associated with the corresponding orbit.
Below we will prove the following 4 claims.

1. The number of unlabeled inscribed squares associated to an unlabeled
hyperbolic component is odd.

2. The number of unlabeled inscribed squares associated to any other
unlabeled arc component is even.

3. The number of unlabeled inscribed squares associated to an unlabeled
elliptic component is odd.

4. The number of unlabeled inscribed squares associated to any other
unlabeled loop component is even.

Combining these claims, we see that the total number of unlabeled inscribed
squares, namely Ω, has the same parity as ΩH + ΩE, the total number of
unlabeled hyperbolic components plus the total number of unlabeled elliptic
components. This is exactly Equation 1.

14

3.2 The Arc Components

Lemma 3.1 Every arc component of I(γ) has order 4.

Proof: Recall that I(γ) is naturally a subset of R8. Given an arc component
ζ, there are two points ζ1, ζ2 in R8 corresponding to the ends of ζ. Up to
cyclic relabeling, each of these points has the form (a, b, a, b, c, d, c, d) where
(a, b) ̸= (c, d). Each of these points encodes the chord of γ corresponding to
an end of ζ, and ζ1 ̸= ζ2.
Suppose that ψ(ζ) = ζ for some cyclic relabeling map ψ. Given the form
of our points, we see that that ζj ̸= ψ(ζj). This means that ψ must inter-
change ζ1 and ζ2. But this means that ψ is a homeomorphism of the arc ζ
which swaps its ends. This situation forces ψ to ﬁx a point of ζ. This is
impossible. ♠

Lemma 3.2 Each labeled hyperbolic component contains an odd number of
labeled inscribed squares and any other labeled arc component contains an
even number of labeled inscribed squares.

Proof: Let ζ be a labeled hyperbolic arc component. Let ρ : ζ → (0, ∞)
be the aspect ratio function. By deﬁnition ρ(p) = 1 if and only if p rep-
resents a square. At one end of ζ, the value of ρ is less than 1. At the
other end, the value of ρ is greater than 1. Given that ρ is injective in a
neighborhood of each point of ρ
−1(1), this means that ρ = 1 an odd number
of times on ζ. The argument for the non-hyperbolic arcs is the same except
that ρ is either greater than 1 at both ends of ζ or less than 1 at both ends. ♠

Proof of Claim 1: Let ζ1, ζ2, ζ3, ζ4 be the hyperbolic components compris-
ing an orbit. There is some odd k such that ζ1 has k labeled inscribed squares
associated to it. But then, by symmetry, the same holds for the other com-
ponents. Hence, there are a total of 4k labeled inscribed squares associated
to these components. But this means that there are k unlabeled inscribed
squares associated to these components. ♠

Proof of Claim 2: The proof of Claim 2 is the same as the proof of Claim
1 except that now k is even. ♠
 15

3.3 The Loop Components

Lemma 3.3 A labeled elliptic component contains 4k labeled inscribed squares
for some odd integer k.

Proof: Let ζ be some labeled elliptic component and r0 be the point of
ζ that has aspect ratio less than 1. Let r1, r2, r3 be the successive images
of r0 under the relabeling map. Let ζk be the arc of ζ bounded by rk and
rk+1 with indices taken mod 4. Consider the restriction of the aspect ratio
function ρ to ζ0. We have ρ(r1) = 1/ρ(r0). So, as we trace out ζ0 from
r0 to r1 we see that ρ starts out less than 1 and ends up greater than 1.
Hence ρ attains the value 1 an odd number k of times on ζ1. By symmetry,
ρ attains the value 1 exactly k times on each arc ζk. This give a total of 4k. ♠

Proof of Claim 3: Let ζ be some labeled elliptic component. The orbit
of ζ is just ζ itself. We have just seen that the number of labeled inscribed
squares associated to ζ is 4k for some odd k. But then the number of unla-
beled inscribed squares associated to ζ is k. ♠

Lemma 3.4 A labeled loop component contains 2k labeled inscribed squares
for some integer k. If the component has order 2 then k is even.

Proof: Let ζ be such a component. Since ζ is a topological loop and ρ is
injective in a neighborhood of each point of ρ
−1(1), the map ρ attains the
value 1 an even number of times. This is the ﬁrst statement.
Suppose then that ζ has order 2. Let r0 be some point of ζ such that
ρ(r0) ̸= 1. Since ζ has order 1, the element of Z/4 which sents vertex 0 to
vertex 2 must be the one which stabilizes ζ. Let r1 be the image of r0 under
this relabeling element. Both r0 and r1 have the same aspect ratio. Hence ρ
attains the value 1 an even number of times on each of the arcs of ζ joining
r0 to r1. ♠

Proof of Claim 4: Let ζ be a labeled loop component which is not elliptic.
Regardless of whether ζ has order 1 or 2, the preceding lemma says that
there are 8h labeled squares associated to the orbit of ζ. Hence there are an
even number of unlabeled squares associated to the orbit of ζ. ♠

16

3.4 Discussion

The analysis above combines with Theorem 1.6 to prove the follownig result.

Corollary 3.5 For γ in P the space G(γ) contains an odd number of squares.

Proof: The analysis above shows that each non-global component of I(γ)
contributes an even number to the total number of unlabeled inscribed squares.
By Theorem 1.6, therefore, I(γ) −G(γ) contains an even number of inscribed
squares. Hence G(γ) contains an odd number of inscribed squares. ♠

Here is a way to deduce Theorem 1.7 from Corollary 3.5 without appealing
to Theorem 1.6. The same argument as above establishes Equation 1 when
we make the counts with respect to components in G(γ). So, if we already
know that there are an odd number of gracefully inscribed squares, then
our new count implies G(γ) has either a hyperbolic component or an elliptic
component. This approach to Theorem 1.7 is more direct, and we originally
took it. However, our direct proof that G(γ) has an odd number of squares,
a homotopy argument, was rather tedious.

17

4 The Moduli Space

4.1 Inscribing Rectangles in Four Lines

For this chapter we work in the complex plane C. Let L = (L0, L1, L2, L3)
be a quadruple of lines in C. We assume throughout the chapter that these
lines are in general position. We say that a rectangle R is gracefully inscribed
in L if the vertices (R0, R1, R2, R3) go cyclically around R (either clockwise
or counterclockwise) and satisfy Ri ∈ Li for i = 0, 1, 2, 3. We let G(L) denote
the set of rectangles gracefully inscribed in L. We think of G(L) as a subset
of R8. In [S2] I worked out quite a bit of the structure of G(L). Here I will
give a more abstract and less detailed treatment, but when relevant I will
point out the stronger results that appear in [S2].
We deﬁne the aspect ratio ρ : G(L) → R by the formula

ρ(R) = ±|R2 − R1|
|R1 − R0|. (6)

The sign is −1 if R is clockwise ordered and +1 if R is counterclockwise
ordered. We allow ρ to be both positive and negative, though ultimately we
just care about the case ρ > 0.

Lemma 4.1 Let G(L, ρ) denote the subset of G(L) consisting of rectangles
having aspect ratio ρ. For generic choice of L, the space G(L, ρ) has at most
one element for every choice of ρ.

Proof: Let R be a rectangle in G(L). We have

R2 − R1 = iρ(R1 − R0), R3 − R2 = R1 − R0.

Writing this as a matrix equaion, we have (R2, R3) = M(R0, R1), where

M = [ −iρ 1 + iρ
1 − iρ iρ
 ] . (7)

Note that det(M) = 1 and trace(M) = 0. This means that M is always
invertible and indeed an involution. Let Π12 = L0 × L1 and Π34 = L2 × L3.
These are both totally real planes in C 2. The solutions we seek are the
points of M(Π12) ∩ Π34. These two planes are either disjoint, or intersect in
a d-dimensional aﬃne subspace for d = 0, 1, 2.

18

The case d = 2 is certainly not generic, and we rule out the case d = 1 with
a dimension count. The space of rectangles of aspect ratio ρ is 5 dimensional.
So, the space of pairs of rectangles having aspect ρ is 9 = 5 + 5 − 1 dimen-
sional. Given two such rectangles R and R′, we can recover the quadruple L
by letting Lk be the line through Rk and R′
k. This accounts for all quadruples
of interest. The space of rectangles of aspect ratio ρ gracefully inscribed in L
is 1-dimensional aﬃne subspace. Thus, we have overcounted the quadruples
of lines of interest by 2 dimensions: Any pair of rectangles in the family
would produce the same quadruple. This the space of quadruples containing
inﬁntely many rectangles of the same aspect ratio has dimension 7. On the
other hand, the space of quadruples of lines has dimension 8. ♠

Remark: In [S2] I show that G(L) contains inﬁnitely many rectangles of
the same aspect ratio if and only if the line through L0 ∩ L1 and L2 ∩ L3 is
perpendicular to the line through L1 ∩ L2 and L3 ∩ L0.

Since L is generic, G(L) contains exactly one rectangle Rρ of aspect ratio
ρ provided that it contains any. Let ρ(L) denote the set of aspect ratios of
rectangles in G(L). We deﬁne the point φk(ρ) ∈ Lk denote the kth vertex of
Rρ. This gives us a map φk : ρ(L) → Lk. We call φk a vertex map.
Let L be the space of generic quadruples. We can identity this space
with an open subset of R8. We can think of our vertex map φk as a map
L × R → C. The point φk(L, ρ) is the vertex of the rectangle Rρ deﬁned
relative to the conﬁguration L. The domain for ρk is naturally the ﬁber
bundle E over L whose ﬁber is ρ(L).

Lemma 4.2 The space E is an open subset of R9 and each ρk is an analytic
function on E.

Proof: Referring to Lemma 4.1, the existence of Rρ means that the two
planes M(Π12) and Π34) are transverse. A small change in ρ or in L does not
change that fact. Hence E is open in R9. The desired point can be found
using linear algebra with inputs that vary analytically with the coordinates
on E. Everything in sight is algebraic, and hence analytic. ♠

Remark: In [S2] I show that the set of centers of rectangles in G(L) is a hy-
perbola minus 2 points, namely those corresponding to degenerate rectangles

19

of aspect ratio 0 and ∞. There are two unequal values a1 and a2, correspond-
ing to the points at inﬁnity of the hyperbola, such that ρ(L) = R−{0, a1, a2}.
Moreover a1a2 equals the cross ratio of the slopes of the lines of L.

There is one degenerate case we need to consider. We say that a repeating
quadruple is one of the form

(L0, L0, L1, L2), (L0, L1, L1, L2), (L0, L1, L2, L2), (L0, L1, L2, L0).
(8)
Here L0, L1, L2 are distinct and non-parallel lines. We call these kinds of
quadruples repeating quadruples. We make the same deﬁnition for G(L).
The same results as above apply in this case. Indeed, it never happens that
G(L) contains inﬁnitely many rectangles of the same aspect ratio.

Permutation Trick: We have now deﬁned two kinds of quadruples, the
generic ones and the generic repeating ones. So far we have been talking
about gracefully inscribed rectangles. Since we are interested in all inscribed
rectangles, rather than just the gracefully inscribed ones, we note that the
permutation of a generic quadruple is still generic and the cyclic or dihe-
dral permutation of a repeating quadruple is still a repeating quadruple. For
instance, if we are interested in the space G′(L) of rectangles having the
property that R0 ∈ L1 and R1 ∈ L3 and R1 ∈ L0 and R3 ∈ L2 then we are
really considering the space G(L
′), where L
′ = (L1, L3, L0, L2) is the suitable
permutation of the lines of L. The space I(γ) divides into diﬀerent subspaces,
depending on the combinatorics of the labelings. The space G(γ) is one of
these. When proving things for I(γ), we will often specialize to the case
of G(γ), with the understanding that the permutation trick just discussed
promotes the proof we give for G(γ) to a proof for I(γ).

Regular and Singular Values: Since φk is analytic, there are ﬁnitely
many values b1, ..., bℓ ∈ ρ(L) such that dφk/da = 0. Here we are diﬀerentiat-
ing with respect to the aspect ratio parameter. We call b1, ..., bℓ the singular
ratios for φk and we call their images on Lk the singular images. We call
a ∈ R a regular ratio if it is not a singular ratio. Geometrically, the kth
vertex of Ra varies monotonically on Lk near a regular value a. We call the
image of a regular ratio a regular image.

20

4.2 The Polygon Space

In this section, we deﬁne our space P of polygons and then show that it is
open and dense in the space of all polygons. What really mean is that there
is a space P(N) for each N ≥ 3, which is a subset of the ﬁnite dimensional
space of all labeled N-gons, and P(N) is open and dense in this space. The
space of all labeled N-gons is simply R2N . So, our space P(N) is an open
dense subset of R2N .
Let γ be a polygon, with sides E1, ..., EN . We insist ﬁrst of all that no two
sides of γ are parallel. This assumption implies that any rectangle gracefully
inscribed in γ has its vertices in at least 3 distinct edges. We say that an
associated quad L = (L0, L1, L2, L3) is a quadruple of lines, cyclically ordered
(counterclockwise) and extending some sides of γ, which is either repeating
or ordinary in the sense above. We say that γ belongs to P if

1. All associated quads are generic or repeating.

2. No inscribed rectangle has more than 1 vertex in common with γ.

3. No inscribed square has a vertex in common with γ.

4. No vertex of γ is a singular image with respect to an associated quad.

Lemma 4.3 P is open and dense in the space of all polygons.

Proof: Condition 1 clearly holds on an open dense set. The remaining
conditions are open because their negation is closed. For instance, if we have
a convergent sequence of N-gons having an inscribed square that shares a
vertex with the polygons, then we can take a limit and get such a square on
the limiting polygon. The other conditions are similar.
We will deal with Condition 2. Given any pair v1, v2 of vertices of γ, let e
be the edge joining v1 and v2 and let λ1 and λ2 be the lines perpendicular to
e through v1 and v2 respectively. Let λ3 be the circle having e as a diameter.
We can perturb so that λi ∩ γ is always a ﬁnite set of points. We can further
perturb so that there are no points vi ∈ λi ∩ γ for i = 1, 2 or v1, v2 ∈ γ3 such
that ∥v1 − e1∥ = ∥v2 − e2∥. Thus, after ﬁnitely many steps, we get Condition
2 and keep Condition 1.
Conditions 3 and 4 involve a single vertex at a time. To show density for
these, we introduce a slide move. This is deﬁned relative to a vertex v and
one of the edges e incident to v. We replace v by a vertex v′ ∈ e very close

21

to v and then consider the new polygon having v′ as a vertex in place of v
and all other vertices the same.
If we have a polygon which fails to have one of the conditions above, we
can associate that failure to a triple (v, e, L) where v is an involved vertex,
e is an involved edge, and L is an associated quadruple one of whose sides
extends e. In case the same problem – e.g. a square sharing a vertex with the
polygon – involves more than one triple (v, e
′, L
′) we count this as a separate
problem. Each slide move, if done with respect to a suﬃciently nearby vertex,
removes one of the problems and does not create any new ones.
For instance, given (v, e, L), there exist points v′ ∈ e arbitrarily close to v
such such that the square in G(L) does not contain v′ and v′ is a regular value
for the relevant vertex map. This follows from the analyticity of everything
in sight: The problem points on e are isolated.
So, we go around making small perturbations ﬁxing one problem at a time
until we are done, and we can make these perturbations as small as we like. ♠

4.3 The Manifold Structure

Now we prove Theorem 1.5. Let γ be a polygon in P.

Lemma 4.4 The space I(γ) is a piecewise smooth manifold.

Proof: We will prove this for G(γ). As discussed above, the permutation
trick promotes the proof to a proof for I(γ). We have a partition

G(γ) = G0(γ) ∪ G1(γ). (9)

The points of Gk(γ) correspond to gracefully inscribed rectangles which have
k points in common with the vertex set of γ.
Each point of G0(γ) corresponds to a rectangle of G(L) for some unique
associated quadruple of lines. All nearby points of G0(γ) are associated to
the same quadruple of lines. Thus G0(γ) is open in G(γ), and every point
of G0(γ) has a neighborhood which is just a copy of a neighborhood of the
corresponding point of G(L). So, by the results in §4.1, the set G0(L) is a
smooth manifold and the aspect ratio function ρ gives a coordinate chart.
Let p ∈ G1(L). Let R be the associated rectangle and let v ∈ R be
the vertex of R which is also a vertex of γ. There are exactly 2 associated

22

quadruples L and L
′ such that the rectangle R associated to p lies in G(L)
and G(L
′). After cyclically relabelling, we can arrange that L0 and L
′
0 are the
two lines extending the edges of γ incident to v, and L
′
j = Lj for j = 1, 2, 3.
Let U and U ′ denote small open subsets of p in G(L) and G(L
′) respec-
tively. Each member of G(γ) suﬃciently close to p lies in one of G(L) or
G(L
′), so a small neighborhood of p in G(γ) is given by

(U ∩ G(γ)) ∪ (U ′ ∩ G(γ)).

Because p is a regular image with respect to L or L
′, the set U intersects
G(γ) in a half-open interval having p as endpoint. The idea here is that as
we vary the point in G(L) the vertex near p move monotonically along L0,
spending half the time on the edge of γ contained in L0 and half the on L0
outside this edge. The same goes for U ′. Thus, the two half-open arcs ﬁt
together to give a neighborhood of p in G(γ) homeomorphic to an arc.
We have shown that every point of G(γ) has an arc neighborhood, and
every point of G0(γ) is smooth. Finally, it follows from the analyticity of the
vertex maps that there are only ﬁnitely many rectangles of G(γ) having any
given point of γ as a vertex. In particular, G1(γ) is just a ﬁnite set of points.
Hence G(γ) is a piecewise smooth 1-manifold. ♠

Lemma 4.5 The aspect ratio function ρ is locally injective at each smooth
point of I(γ), and ρ
−1(1) consists entirely of smooth points.

Proof: The set of smooth points is precisely the set G1(γ) considered above.
The restriction of ρ to a small neighborhood of such a point coincides with
the restriction of ρ to some neighborhood of the corresponding point of I(L).
This restriction is injective by Lemma 4.1. The second statement of the
lemma is exactly Condition 3. ♠

Lemma 4.6 Each arc component of I(γ) is proper.

Proof: We prove this for G(γ) and then use the permutation trick to promote
the proof to one for all of G(γ). We ﬁrst recall what we are trying to prove.
We have G(γ) ⊂ R8. Let A ⊂ G(γ) be an arc component. Let ∂A = A − A
denote the boundary of A in R8. We will show that ∂A consists of 2 distinct
points, both representing chords of γ.

23

In the proof of Lemma 4.4 we saw that the space G1(γ) is a ﬁnite set of
points. So, if a rectangle in G(γ) has suﬃciently large or small aspect ratio
it must be a smooth point. This means that there are two unique associated
quadruples L and L
′ such that the ends of A respectively lie in G(L) and
G(L
′). If the rectangles at one end of A accumulate to something other than a
line segment, then we can take a subsequential limit of these uniformly large
and fat rectangles to get another member of G(L). This rectangle would
also grace L, and hence γ, and it would have a neighborhood in G(γ) that
overlaps with A. This is a contradiction. Hence, as we exit an end of A the
corresponding rectangles accumulate on a line segment.
For the end of A associated to L, the relevant rectangles accumulate to a
chord that has one vertex on two consecutive lines of L and one vertex on the
other two. This chord is uniquely determined by L and, by general position,
uniquely determines L amonst all associated quads. All the same remarks
apply to the other end of A, which is associated to the quadruple L
′.
It remains to show that our chords are distinct. If not, then L = L
′ and
the two ends, which both have their elements in G(L) = G(L
′), have some
rectangles in commn. This is a contradiction. ♠

Remark: The ends of each proper arc of G(γ) are critical points for the
distance function d : γ × γ → [0, ∞), at least after one makes a suitable
deﬁnition for what this means in the polygonal case. After doing thousands
of experiments, I noticed that one end of a proper arc is always a saddle
point (i.e. a point with Morse index 1) and the other end is always either a
maximum or a minimum (i.e. a point with Morse index 0 or 2.) I have no
idea how to prove it, but this fact suggests hidden depths.

24

5 Global Components are Graceful

5.1 The Easy Part

In this chapter we prove Theorem 1.6. We say that a rectangle R ∈ I(γ) is
ungracefully inscribed γ if the cyclic order imparted on R from the ordering
on γ is the clockwise ordering of the vertices of R. Let G∗(γ) denote the
space of rectangles which are ungracefully inscribed in γ.

Lemma 5.1 A global component of I(γ) lies in G(γ) or G∗(γ),

Proof: Consider the hyperbolic case ﬁrst. If the rectangles in the hyperbolic
component A are neither gracefully nor ungracefully inscribed, then there
are a pair of opposite sides of the rectangles such that the endpoints on one
pair of opposite sides interlace on γ with the endpoints on the other pair.
However, at one end of A, these edges are very short. This is only possible
if the rectangles are shrinking to a single point. This is a contradiction.
When A is elliptic, we revisit the proof of Lemma 2.8. The same paths
{vk} exist in the more general setting, but now there is some permutation
{i0, i1, i2, i3} of {0, 1, 2, 3} such that vk(1) = [ik]. Equation 5 holds in this
setting, and tells us that there are integers j0, j1, j2, j3 such that

i0 + j0 < i1 + j1 < i2 + j2 < i3 + j3 < i0 + j0 + 4.

Here ik + jk = ̂vk(1). This forces [i0], [i1], [i2], [i4] to be consecutive residue
classes in Z/4. But then (i0, i1, i2, i3) is a cyclic permutation of (0, 1, 2, 3).
This happens if and only if A ∈ G(γ) or A ∈ G∗(γ). ♠

Remark: The components G(γ) and G∗(γ) might look superﬁcially similar,
but actually they are quite diﬀerent. For instance, G∗(γ) is empty if γ is
convex. Before we prove that G∗(γ) has no global components, we explain
why most of the Trichotomy Theorem follows from what we have already
done. The deﬁnition of the circular invariant and the other proofs in §2,
go through practically word for word if we work with components in G∗(γ)
rather than in G(γ). Thus, if we use Lemma 5.1 in place of Theorem 1.6, we
get the whole Trichotomy Theorem except that the last statment is weaker:
S ⊂ G(γ) or S ⊂ G∗(γ).
 25

5.2 The Elliptic Case

In this section we prove that G∗(γ) contains no elliptic components. We
will deduce this result from a theorem about inscribed triangles. We deﬁne
gracefully and ungracefully inscribed triangles the same way as for rectan-
gles. We say that an essential graceful loop (respectively essential ungraceful
loop) is a continuous loop of gracefully (respectively ungracefully) inscribed
triangles such that each vertex winds a nontrivial number of times around γ.
We prove the following result.

Theorem 5.2 No polygon has an ungraceful loop.

If we had an elliptic component in G∗(γ) we could look at the loop of triangles
made from the ﬁrst 3 points. The same lifting argument as in the proof of
Lemma 5.1 shows that the kth vertex of the rectangle family winds around
γ a nonzero number of times. So, we would get an essential ungraceful loop,
contradicting Theorem 5.2. We prove Theorem 5.2 through two lemmas.

Lemma 5.3 A polygon arbitrarily close to γ in the Hausdorﬀ metric sup-
ports a graceful essential loop.

Proof: We describe a motion of the points a, b, c. We can ﬁnd an arbitrarily
nearby polygon whose convex hull has 8 consecutive vertices v1, ...v8 which
agree with the vertices of a regular polygon. We start with points a, b, c lo-
cated at v5, v6, v7. We then move c all the way around γ counterclockwise
until c = v4. Next, we move b around to v3, then a around to v2. Now
we have a, b, c located at v2, v3, v4. Finally, we slide this triangle over to its
original location. ♠

If an elliptic component of H(γ) lies in G∗(γ) then γ supports an essential
ungraceful loop. But then so do all polygons suﬃciently near γ. (The new
loops won’t necessarily be comprised of right triangles, but we don’t care.)
But then we could have an example of a triangle which supports both a
graceful essential loop and an ungraceful essential loop. So, the following
lemma ﬁnishes the proof of Theorem 5.2.

Lemma 5.4 No polygon can support both an essential graceful loop and an
essential ungraceful loop.
 26

Proof: Let Ω denote the subset of distinct triples of points in γ, with the
order induced by the ordering on γ. Let Ω+ ⊂ Ω be the subset corresponding
to triangles having positive signed area. Likewise deﬁne Ω−. Our graceful
and ungraceful essential loops respectively deﬁne essential loops β+ and β−
in Ω+ and Ω−. We can replace β+ and β− by nearby polygonal loops.
There are nonzero integers n± such that n+β+ and n−β− are homologous.
But then we can ﬁnd a piecewise linear surface-with-boundary that has n+β+
and n−β− as boundary components. The common boundary of ∆+ and ∆−
is piecewise algebraic, and so (after we perturb to put things in general
position) the intersection ∆+ ∩ Σ consists of ﬁnitely many piecewise smooth
loops. The union of these loops is homologous to n+β+, so some component
β0 is essential.
Say that a stick is a triple of collinear points of γ. The loop β0 corrsponds
to a continuous family of sticks having the property that each point of the
stick winds a nonzero number of times around γ. But then there will be a
moment when the middle point of the stick will be a vertex of the convex
hull of γ. At this moment, the other two points of the stick cannot lie on γ,
and we have a contradiction. ♠

5.3 The Hyperbolic Case

Now we prove that G∗(γ) has no hyperbolic component. The argument is
similar. This time let Ω denote the set of quadruples of distinct points in γ,
with the order induced by the ordering on γ. The space Ω is homeomorphic
to the product of a 3-ball and a circle. Let Ω+ (respectively Ω−) denote the
set of quadruples deﬁning embedded quadrilaterals, not necessarily convex,
whose ordering goes counterclockwise (respectively clockwise) around their
boundary. Unlike in the elliptic case, the two sets Ω+ and Ω− do not partition
Ω. That does not bother us.
We distinguish 2 special subsets of ∂Ω. Let ∂0Ω be the set of embedded
quadruples (a, a, b, b) and let ∂1Ω be the set of quadruples (a, b, b, a). A
hyperbolic component deﬁnes a curve joining ∂0Ω to ∂1Ω. The interior of
this curve lies in Ω+ when the hyperbolic component is graceful and in Ω−
when the hyperbolic component is ungraceful.

Lemma 5.5 A polygon arbitrarily close to γ in the Hausdorﬀ metric sup-
ports a path in Ω+ joining ∂0Ω to ∂1Ω.

27

Proof: We describe a motion of points a, b, c, d. Make the same modiﬁcation
to γ as in the proof of Lemma 5.3. (We really don’t need all 8 points here.)
Start out with a = b = v3 and c = d = v6. First move b and c respectively
to v4 and v5. Now move d all the way around γ to v2. At every stage of
this construction we have a convex quadrilateral. Now we have a, b, c, d at
v2, v3, v4, v5. Finally, move b and c back to v2 and v3 respectively. Now we
have b = c = v2 and a = d = v5. ♠

Lemma 5.6 There cannot be paths both in Ω+ and Ω− joining ∂0Ω to ∂1Ω.

Proof: The proof here is similar to the elliptic case. We ﬁrst perturb so
that both paths are polygonal. We then observe that both paths represent
the generator of the relative homology group

H1(Ω, (∂0(Ω) ∪ ∂1(Ω)) = Z.

(The space in question is homotopy equivalent relative the boundary to an
annulus relative its boundary.) So, we can build a piecewise linear surface-
with-boundary Σ whose boundary is made up of a path ∂0Ω, a path in ∂1Ω,
and our 2 curves. After we put things in general position, the intersection
Σ ∩ ∂Ω+ is a union of loops and arcs in Σ, one of which joins ∂0Ω to ∂1Ω.
Call this path β0.
The quadrilaterals in β have 4 distinct points but are not embedded.
One possibility is that the points are all collinear and the other possibility is
shown in Figure 3.
 10
 2

3

Figure 3: A degenerate quadrilateral

In case the points are not all collinear, there is always one segment that
has another vertex between it. In Figure 3, the segment is v0v1 and the
middle point is either v2 or v3. We call v0, v1 a framing segment. We can
always cyclically relabel so that at some point along β0 the segment v0v1
is a framing segment. Perturbing β slightly, we can arrange that the points
along β corresponding to 4 collinear points are isolated. Such totally collinear
conﬁgurations have codimension 1 in ∂Ω+.

28

Consider what happens to a conﬁguration with v0v1 as a framing segment
as we pass through a totally collinear conﬁguration. Figure 4 shows the only
3 possibilities.

0 3 21 0
 2

30 2

30
 2

3

0 3 20
23
 2
 0 3
302

2 03

Figure 4: The only allowable transitions

The framing segment either remains v0v1 or else changes to v2v3. There-
fore, one of the two segments v0v1 or v2v3 is the framing segment at each
point of β0. At β0 ∩ ∂0Ω, we have v0 = v1 and v2 = v3. But the distance
between the point on the framing segment to either endpoint of the draming
segment therefore tends to 0. This shows that there is a sequence of points in
Ω converging to a point of ∂0Ω such that the diameter of some 3 of the points
tends to 0. This contradicts the fact that the points of ∂0Ω come together in
pairs and not in triples. ♠
 29

6 ReferencesAA] A. Akopyan and S Avvakumov, Any cyclic quadrilateral can be in-
scribed in any closed convex smooth curve. arXiv: 1712.10205v1 (2017)

[ACFSST] J. Aslam, S. Chen, F. Frick, S. Saloﬀ-Coste, L. Setiabrate, H.
Thomas, Splitting Loops and necklaces: Variants of the Square Peg Problem,
arXiv 1806.02484 (2018)CDM], J. Cantarella, E. Denne, and J. McCleary, transversality in Con-
ﬁguration Spaces and the Square Peg Problem, arXiv 1402.6174 (2014).

[Emch] A. Emch, Some properties of closed convex curves in the plane,
Amer. J. Math. 35 (1913) pp 407-412.

[H] C. Hugelmeyer, Every Smooth Jordan Curve has an inscribed rectan-
gle with aspect ratio equal to √
3. arXiv 1803:07417 (2018)

[Jer]. R. Jerrard, Inscribed squares in plane curves, T.A.M.S. 98 pp 234-241
(1961)Mak1] V. Makeev, On quadrangles inscribed in a closed curve, Math. Notes
57(1-2) (1995) pp. 91-93

[Mak2] V. Makeev, On quadrangles inscribed in a closed curve and ver-
tices of the curve, J. Math. Sci. 131(1) (2005) pp 5395-5400

[Ma1] B. Matschke, A survey on the Square Peg Problem, Notices of the
A.M.S. Vol 61.4, April 2014, pp 346-351.

[Ma2] B. Matschke, Quadrilaterals inscribed in convex curves,
arXiv 1801:01945v2M] M. Meyerson Equilateral Triangles and Continuous Curves, Fundamenta
Mathematicae, 110.1, 1980, pp 1-9.N] M. Neilson, Triangles Inscribed in Simple Closed Curves, Geometriae
Dedicata (1991)
 30

[NW] M. Neilson and S. E. Wright, Rectangles inscribed in symmetric con-
tinua, Geometriae Dedicata 56(3) (1995) pp. 285-297

[S1] R. E. Schwartz, On Spaces of Inscribed Triangles, preprint 2018.

[S2] R. E. Schwartz, Four lines and a rectangle, preprint 2018.

[Shn], L. G. Shnirelman, On certain geometric properties of closed curves
(in Russian), Uspehi Matem. Nauk 10 (1944) pp 34-44;
available at http://tinyurl.com/28gsys.St], W. Stromquist, Inscribed squares and square-like quadrilaterals in closed
curves, Mathematika 36 (1989) pp 187-197

[Ta], T. Tao, An integration approach to the Toeplitz square peg conjecture
Foum of Mathematics, Sigma, 5 (2017)Tv], H. Tverberg, A Proof of the Jordan Curve Theorem,
Bulletin of the London Math Society, 1980, pp 34-38.Va], H. Vaughan, Rectangles and simple closed curves, Lecture, Univ. of
Illinois at Urbana-Champagne.
 31

This figure "fig2.png" is available in "png"  format from:

http://arxiv.org/ps/1804.00740v4

0
 23
(0,0)

(0,1)v

11

1 1

2

2
 2
 2

3
 33
 3 4
 4

4
 4
 34

1 2arXiv:1804.00740v4  [math.MG]  8 Jul 2019
Letter to Referee: First, thank you very much for your helpful comments.
They inspired me to improve the paper lot. Here I will describe the main
changes.

1: I made a more extensive bibliography, and in the introduction give a bet-
ter picture of other relevant work that has been done. One signiﬁcant change
is that I now discuss the beautiful equilateral triangle result of Meyerson. My
result about quadrilaterals is a pretty direct analogue of Meyerson’s theorem
for equilateral triangles, so it is very good to have that reference. The most
signiﬁcant change is that (as you suggested) I now use and cite the result
that a generic polygon has an odd number of inscribed squares.
I should say, however, that this is a rather subtle point. In the original
paper I was proving the fact that the number of gracefully inscribed inscribed
squares is odd whereas the common result in the literature concerns the num-
ber of all inscribed squares. It isn’t clear to me how to deduce the gracefully
inscribed result from the general result in the literature, though I agree that
the proof I had was very far from optimal.

2: Rather than directly prove the result about the parity of the gracefully
inscribed squares, I analyze the space of all inscribed squares and quote the
result from the literature. I then show that the components of interest to
me – sweepouts and elliptic components – actually must consist entirely of
gracefully inscribed squares. (Incidentally, now I call sweepouts hyperbolic
components. That seems like better terminology.) This new approach just
eliminates all the subtle crud in the original paper associated to my count of
gracefully inscribed squares. That bad proof is just gone.

3: As a byproduct of my new approach, I get the following theorem:

Theorem 0.1 On a counter-clockwise oriented polygon it is impossible to
have a 1 parameter family of clockwise inscribed triangles that winds a non-
trivial number of times around the polygon.

Here clockwise inscribed means that the cyclic order on the vertices in-
duced by the triangles themselves is the clockwise ordering (whereas the
cyclic order on the vertices induced by inclusion in the polygon is counter-
clockwise.) I prove Theorem 0.1 through a mixture of geometry and topology.

1

4. My treatment of the problem of inscribing rectangles into 4 lines is more
conceptual and abstract. In the time between submitting this paper and now,
I worked out what happens for the 4 lines down to the last iota in a (now
cited) preprint. One beautiful result is that the locus of centers of rectangles
inscribed in 4 lines is a hyperbola minus 2 points – corresponding to degener-
ate rectangles. What I do in this paper is deﬁne everything clearly, then give
conceptual proofs of just the results I need to use – e.g. the locations of the
inscribed rectangles vary analyically with the parameters of the lines . Now
that I am not using a complicated variational argument to count the number
of odd gracefully inscribed squares, I don’t need as much information about
the situation for 4 lines and I can make do with more general and abstract
statements. While I don’t include the many results I got in my preprint in
this paper, I point out some of the results in remarks, whenever it is relevant
to the discussion.

5: I reordered the paper. The most signiﬁcant change is that the ﬁrst thing
I now do is deduce the main Theorem about general Jordan loops from the
main Theorem about polygons. This way, the reader can see the interesting
topological argument right away. After §2, the rest of the paper is about
polygons. Incidentally, I really worked to clean up the proof of the main
theorem, because this is probably the most interesting thing for readers.
Someone who knows a lot about the subject will most likely ﬁnd the results
about polygons very believable. So, the newest ideas of the paper are now
put front and center.
 2
