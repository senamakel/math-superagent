<!-- source: https://arxiv.org/pdf/1402.6174 | converted from PDF -->

Transversality in Conﬁguration Spaces and the “Square-Peg” theorem

Jason Cantarella,∗ Elizabeth Denne,† and John McCleary‡

(Dated: April 1, 2021)

We prove a transversality “lifting property” for compactiﬁed conﬁguration spaces as an application
of the multijet transversality theorem: the submanifold of conﬁgurations of points on an arbitrary
submanifold of Euclidean space may be made transverse to any submanifold of the conﬁguration
space of points in Euclidean space by an arbitrarily C 1-small variation of the initial submanifold, as
long as the two submanifolds of compactiﬁed conﬁguration space are boundary-disjoint. We use this
setup to provide attractive proofs of the existence of a number of “special inscribed conﬁgurations”
inside families of spheres embedded in Rn using differential topology. For instance, there is a C 1-
dense family of smooth embedded circles in the plane where each simple closed curve has an odd
number of inscribed squares, and there is a C 1-dense family of smooth embedded (n − 1)-spheres
in Rn where each sphere has a family of inscribed regular n-simplices with the homology of O(n).

Authors’ note: This paper will not be published in this form, but instead, has been split into
three separate papers [6–8]. These papers will be published separately. This paper has been cited
extensively in the literature and so has been left on the arXiv as a reference to the reader.

1. INTRODUCTION

Given a simple closed curve (a Jordan curve) γ in R2, can we ﬁnd four points on γ that form a
square? This question was posed by Toeplitz in 1911 [25] and it has drawn the attention of many
mathematicians over the intervening century. Thinking of the Jordan curve as a “round hole”,
the problem has been affectionately dubbed the “square-peg problem.” We say that the square is
inscribed in γ when the vertices lie on the curve. We do not require that the square lie entirely
in the interior of the curve. Progress on the square-peg problem has chieﬂy been extension of the
class of simple closed curves for which the square can be found. (The interested reader can ﬁnd a
number of survey articles such as [15, 17, 20]. )

Our goals are different. First, by placing the problem in the context of conﬁguration spaces
and their subspaces, we have opened up a set of tools from differential topology that allow fresh
viewpoints through some powerful methods. Our conclusions include the previous work and show
how differentiability assumptions can deliver a strong sense in which squares appear generically.
The use of the multijet transversality theorem [11] is new and holds promise for the application of

∗University of Georgia, Mathematics Department, Athens GA
†Washington & Lee University, Department of Mathematics, Lexington VA
‡Vassar College, Mathematics Department, Poughkeepsie NYarXiv:1402.6174v2  [math.GT]  31 Mar 2021
2

FIG. 1: This picture shows the ﬁve squares inscribed on an irregular planar curve. It turns out to be the case
that the manifold of inscribed 4-tuples on this curve is transverse to the manifold of squares in the plane.
Hence the squares are isolated and there are an odd number of squares. In general, our theorems guarantee
only that a curve arbitrarily C 1-close to this one has this property.

differential topological methods to other conﬁguration problems.

Here is the heart of our method: If we consider the (compactiﬁed) conﬁguration space C4[R2]
of 4-tuples of points in the plane as an 8-dimensional manifold with boundary (and corners), then
Toeplitz’s question can be rephrased more simply as a question about the intersections of the 4-
dimensional submanifold of 4-tuples of points on γ, called C4[γ], with the 4-dimensional subman-
ifold of squares in R2.

We can see with a little effort that for a standard ellipse, these submanifolds intersect in four
points corresponding to cyclic relabelings of a single inscribed square. It is therefore natural to
try to show that squares are transverse to inscribed conﬁgurations in the ellipse and use an isotopy
from the ellipse to γ to connect the square on the ellipse to a cobordant family of squares on the
target curve.

This program requires us to face a few technical obstacles. First, the square might shrink away
during the isotopy. We overcome this obstacle by analyzing the (compactiﬁed) boundary of our sub-
manifolds of inscribed conﬁgurations and showing that, in a precise sense, C1 curves do not admit
inﬁnitesimal squares. Second, we do not know that the submanifold of squares is transverse to the
submanifold of inscribed conﬁgurations on γ. We may vary the submanifold of inscribed conﬁgu-
rations using the standard transversality theorem for manifolds to make it transverse, of course, but
there is no a priori guarantee that the varied submanifold consists of inscribed conﬁgurations on
any single curve. We deal with this problem by an application of the multijet transversality theo-
rem [11]. Third, it turns out to be the case that the four intersections of the submanifold of squares
with the submanifold of inscribed quadruples on the ellipse alternate sign. To count squares we
must mod out by cyclic relabeling of vertices and pass to Z/2Z intersection theory.

The method we use for squares is an example of a general approach to such “special inscribed
conﬁguration” problems: Show that the conﬁgurations one is looking for form a submanifold Z of
conﬁguration space to establish smoothness, prevent “shrink outs” by showing that Z is boundary-
disjoint from the submanifold of inscribed conﬁgurations Cn[γ], ﬁnd the (transverse) intersection

3

of Z and Cn[γ0] explicitly in a base case, use our transversality theorem to conclude that a sub-
manifold γ′ near the target submanifold γ also has Cn[γ′] ⋔ Z. Finally, use standard methods to
build a isotopy from Cn[γ0] to Cn[γ′] that is transverse to Z at every step of the way.

In addition to counting squares (Theorem 24), we show as another example of these methods
that there is a k(k − 1)/2 dimensional family of inscribed simplices of any edgelength ratio in a
generic embedding of Sk−1 in Rk (Theorem 28).

It is important to note that while our results provide a uniﬁed and attractive view of this family
of theorems about special inscribed conﬁgurations, they do not directly address the remaining open
territory in Toeplitz’s question: We give, in the Appendix, an extension of our results to prove that
there exists at least one square on any embedded curve of ﬁnite total curvature without cusps, but
this class of curves is certainly less general than the family of curves for which Stromquist proved
the square peg theorem in [23].
 2. CONFIGURATION SPACES

The compactiﬁed conﬁguration space of n points in Rk is the natural setting for both the square-
peg and inscribed polygon problem. A reader familiar with conﬁguration spaces may skip much of
this section. However we recommend paying attention to the notation we have used for the spaces,
points in the spaces and the strata. Deﬁnition 2, Deﬁnition 3, and Remark 5 are particularly useful.
This section provides a brief overview of (compactiﬁed) conﬁguration spaces. There are many
versions of this classical material (see for instance [2, 10]). We follow Sinha [22] as this gives a
geometric viewpoint appropriate to our setting.

Deﬁnition 1. Given an m-dimensional smooth manifold M , let M ×n denote n copies of M , and
deﬁne Cn(M ) to be the subspace of points p = (p1, . . . , pn) ∈ M ×n such that pj ̸= pk if j ̸= k.
Let ι denote the inclusion map of Cn(M ) in M ×n.

The space Cn(M ) is an open submanifold of M ×n. Our goal is to compactify Cn(M ) to
a closed manifold with boundary and corners, which we will denote Cn[M ], without changing its
homotopy type. The resulting manifold will be homeomorphic to M ×n with an open neighborhood
of the fat diagonal removed. Recall that the fat diagonal is the subset of M ×n of n-tuples for which
(at least) two entries are equal, that is, where some collection of points comes together at a single
point. The construction of Cn[M ] preserves information about the directions and relative rates of
approach of each group of collapsing points.

Deﬁnition 2 ([22] Deﬁnition 1.3). Let [
n
k] denote the number of ordered subsets of k distinct
elements of a set of size n. Given an ordered pair (i, j) of {1, . . . , n}, let πij : Cn(Rm) → Sm−1

be the map that sends p = (p1, . . . pn) to pi − pj
|pi − pj| , the unit vector in the direction of pi − pj.

4

Let [0, ∞] be the one-point compactiﬁcation of [0, ∞). Given an ordered triple (i, j, k) of distinct

elements in {1, . . . , n}, let sijk : Cn(Rm) → [0, ∞] be the map which sends p to |pi − pj|
|pi − pk| .

To deﬁne conﬁguration spaces for points in an arbitrary smooth (C∞) manifold M , we embed
M in Rk so that Cn(M ) is a subspace of Cn(Rk). We then compactify the space as follows:

Deﬁnition 3 ([22] Deﬁnition 1.3). Let An[Rk] be the product (Rk)n×(Sk−1)[n
2]×[0, ∞][
n
3]. Deﬁne
Cn[Rk] to be the closure of the image of Cn(Rk) under the map

αn = ι × (πij) × (sijk) : Cn(Rk) → An[Rk].

If M is smoothly embedded in Rk, then Cn(M ) is smoothly embedded in Cn(Rk) and we deﬁne
Cn[M ] to be the closure of αn(Cn(M )) in An[Rk]. In this case, we will refer to An[Rk] as An[M ]
for convenience; we denote the boundary of Cn[M ] by ∂Cn[M ] = Cn[M ] \ Cn(M ).

We now summarize some of the important features of this construction, including the fact that
Cn[M ] does not depend on the choice of embedding of M in Rk.

Theorem 4. [cf.[22], [5] Theorem 2.3]

• Cn[M ] is a manifold with boundary and corners with interior Cn(M ) having the same
homotopy type as Cn[M ]. The topological type of Cn[M ] is independent of the embedding
of M in Rk, and Cn[M ] is compact if M is.

• The inclusion of Cn(M ) in M n extends to a surjective map fron Cn[M ] to M n which is a
homeomorphism over points in Cn(M ).

Remark 5. When discussing points in Cn[Rk] or Cn[M ], it is easy to become confused. We pause
to clarify notation.

• A point in Rk is denoted by x = (x1, . . . , xk), where each xi ∈ R.

• Points in (Rk)n are also denoted by x, where x = (x1, . . . , xn) and each xi ∈ Rk. (It will
be clear from context which is meant.)

• A point in Cn[Rk] or Cn[M ], is denoted −→x .

• At times, we will need to distinguish between the various entries of −→x ∈ Cn[Rk] or Cn[M ].
In general,
 −→x = (x, (πij)(x), (sijk)(x)) = (x, α(x)),

where x = (x1, . . . , xn) ∈ (Rk)n, and α(x) = ((πij)(x), (sijk)(x)) gives the correspond-

ing set of values in (Sk−1)[
n
2] and [0, ∞][
n
3].
 5

The space Cn[M ] may be viewed as a polytope with a combinatorial structure based on the
different ways groups of points in M can come together. This structure deﬁnes a stratiﬁcation of
Cn[M ] into a collection of closed faces of various dimensions whose intersections are members of
the collection. We will need to understand a bit of the structure of this collection, which is referred
to as a stratiﬁcation of Cn[M ].

Deﬁnition 6 ([5] Deﬁnition 2.4). A parenthesization P of a set T is an unordered collection {Ai}
of subsets of T such that each subset contains at least 2 elements and two subsets are either disjoint
or one is contained in the other. A parenthesization is denoted by a nested listing of the Ai using
parentheses. Let Pa(T ) denote the set of parenthesizations of T , and deﬁne an ordering on it by
P ≤ P ′ if P ⊆ P ′.

For example, for T = {1, 2, 3, 4}, (12)(34) represents a parenthesization whose subsets
are {1, 2} and {3, 4} while ((12)34) represents a parenthesization whose subsets are {1, 2} and
{1, 2, 3, 4}.

We identify each parenthesization P = {A1, . . . , Al} of {1, . . . , n} with a closed subset SP
of ∂Cn[M ] in our stratiﬁcation of Cn[M ]. The idea is that all the points in each Ax collapse
together, but if Ax ⊂ Ay, then the points in Ax collapse “faster” than the points in Ay. Formally,
this becomes the following condition: Let −→p = ((p1 . . . , pn), (πij)(p), (sijk)(p)) be a point in
An[M ]. Then −→p ∈ SP if

• pi = pj if and only if i, j ∈ Ax for some x.

• sijk = 0 (and hence sikj = ∞) if and only if Ax ⊂ Ay, i, j ∈ Ax and k ∈ Ay.

Sinha proves that a stratum SP described by nested subsets {A1, . . . , Ai} has codimension i in
Cn[M ]. In the previous example (12) has codimension 1, while ((12)34) and (12)(34) have codi-
mension 2.

We notice that the deﬁnition of the SP does not depend on the πij. In fact, for connected
manifolds of dimension at least 2, the combinatorial structure of the strata of Cn[M ] depends only
on the number of points. Regardless of dimension, this construction and division of ∂Cn[M ] into
strata is functorial in the sense that

Theorem 7 ([22]). An embedding f : M → N induces an embedding of manifolds with corners
called the evaluation map Cn[f ] : Cn[M ] → Cn[N ] that respects the stratiﬁcations.

Corollary 8. Let f : Rk → Rk be a smooth diffeomorphism. Then the induced map of conﬁguration
spaces Cn[f ] : Cn[Rk] → Cn[Rk] is also a smooth diffeomorphism (on each face of Cn[Rk]).

Proof. This is an immediate corollary of the previous theorem.
 6

Any pair p, q of disjoint points in Rk has a direction (p − q)/ |p − q| associated to it, while
every triple of disjoint points p, q, r has a corresponding distance ratio |p − q| / |p − r|. One way
to think of the purpose of Cn[M ] is that it extends the deﬁnition of these directions and ratios to
the boundary.

Theorem 9 ([22] or [5] Theorem 2.3). Given M ⊂ Rk, in any conﬁguration of points −→p ∈ Cn[M ]
each pair of points pi, pj has associated to it a well-deﬁned unit vector in Rk giving the direction
from pi to pj. If the pair of points project to the same point p of M , this vector lies in TpM .

Similarly, each triple of points pi, pj, pk has associated to it a well-deﬁned scalar in [0, ∞]
corresponding to the ratio of the distances |pi − pj| and |pi − pk|. If any pair of {pi, pj, pk}
projects to the same point in M (or all three do), this ratio is a limiting ratio of distances.

The functions πij and sijk are continuous on all of Cn[M ] and smooth on each face of ∂Cn[M ].

3. SPECIAL SUBMANIFOLDS OF CONFIGURATION SPACES

We are interested in three special submanifolds of particular conﬁgurations deﬁned by geomet-
ric constraints. First, we consider the conﬁguration space of points on a curve.

Deﬁnition 10. Let γ be a C∞-smooth embedding of S1 in Rk, with Cn[γ] : Cn[S1] → Cn[Rk]
the evaluation map on conﬁguration spaces. We abuse notation by using γ to mean either the
embedding or its image in Rk. Similarly, we use Cn[γ] to mean either the evaluation map or its
image — the compactiﬁed conﬁguration space of n points on the simple closed curve γ(S1) ∈ Rk.

By Theorem 7 we know that Cn[γ] is a submanifold of Cn[Rk] and ∂Cn[γ] ⊆ ∂Cn[Rk] with
the stratiﬁcations respected. The coordinates for Cn[γ] are similar to those described in Theorem 9,
as they are the image of the coordinates under γ : S1 → Rk. Volic [27] and Budney et al. [5] have
detailed descriptions of the coordinates for codimension 1 strata. To give an example, observe that
the map Cn[γ] takes (p1, . . . , pn) ∈ Cn(S1) to (γ(p1), . . . , γ(pn)) ∈ Cn[Rk]. If we consider the
stratum where say p1, p2 and p3 degenerate to a point −→q in Cn[S1], then −→q is a conﬁguration
of n − 3 + 1 = n − 2 points plus the πij and sijk information for p1, p2 and p3. In Cn[Rk] we
get a conﬁguration of n − 2 points on γ plus the directions of approach of the colliding γ(pi) and
the relative distances s123, s312, and so forth. The πij are unit tangent vectors to γ. If p1 and p3
approach p2 equally from opposite sides, then in the limit |p1 − p2| + |p2 − p3| = |p1 − p3|, so
the sijk obey the relations

1 + s231 = s132, s213 + 1 = s312, s123 + s321 = 1.

In Cn[S1] the values of πij are in S0 and are mapped to S1 by Cn[γ]. Thus, while the exact
values of the unit tangent vectors πij and πji are unknown for two colliding points on γ, they must
differ by π.
 7

In the case of the circle, the cyclic ordering of points along S1 determines (n − 1)! connected
components of Cn[S1]. Note that some strata are empty in the boundary of each connected com-
ponent of Cn[S1]. For instance, in the component of C4[S1] where points p1, p2, p3 and p4 occur
in order along S1, if p1 and p3 come together, either p2 or p4 must collapse to the same point.
Thus the stratum (13) is empty on the boundary of this component. We will focus on one of these
connected components:

Deﬁnition 11. Let C0
n[γ] denote the component of Cn[γ] where the order of the points p1, . . . , pn
matches the cyclic order of these points along γ according to the given parametrization of γ.

We now consider another submanifold – this one with a more interesting structure.

Deﬁnition 12. Let the subset of square-like quadrilaterals Slq for k = 2 be the subspace of squares
in R2, and for k > 2, the subset of C4[Rk] where s124 = s231 = s342 = 1 and s132 − s241 = 0.
That is, Slq is the space of quadrilaterals in Rk with equal sides and equal diagonals.

Proposition 13. The space Slq ∩ C4(Rk) is an orientable submanifold of C4(Rk), and the (point-
set) boundary of Slq satisﬁes ∂Slq ⊂ ∂C4[Rk].

Proof. Let −→p = ((p1, p2, p3, p4), α(−→p )) be a point in C4[Rk], and consider the mapping
g : C4[Rk] → R4 given by

g(−→p ) = (s
2
124, s
2
231, s
2
342, s
2
132 − s
2
241)

= ( |p1 − p2|2

|p1 − p4|2 , |p2 − p3|2

|p1 − p2|2 , |p3 − p4|2

|p2 − p3|2 , |p1 − p3|2

|p1 − p2|2 − |p2 − p4|2

|p2 − p1|2
 ) .

This mapping is smooth and Slq is the preimage of the point (1, 1, 1, 0). We show that

dg : T−→p C4(R
k) → Tg(−→p )R4

is onto at points −→p ∈ Slq by showing dg has four linearly independent rows. We denote a tangent
vector at −→p by −→v = v(−→p ) = (v1, v2, v3, v4), where each vi is a tangent vector at pi. (Here we
suppress the α(p) information on the strata.)

Let ∆p1 denote a vector at p1 as in Figure 2, deﬁne −→v 1 = (∆p1, 0, 0, 0) and consider

dg−→v 1(p1, p2, p3, p4) = lim
|∆p1|→0 g(p1 + ∆p1, p2, p3, p4) − g(p1, p2, p3, p4)
|∆p1| .
 8

p1
 p2

p3

p4
 ∆p1 ∆p1
p1
 p2

p3

p4

FIG. 2: This ﬁgure shows the general situation where a vertex a of a quadrilateral in Slq is varied. On the
left, we see the case in the plane, where every quadrilateral in Slq is really a square. On the right, we see
the general (space) case, where the quadrilaterals in Slq form a class of special tetrahedra. We compute the
corresponding variation of edgelengths, and of the values of the function which we use to deﬁne the space
of square-like quadrilaterals, in the proof of Proposition 13.

To compute the limit, let us consider a typical quotient term involved:

|p1 − p2 + ∆p1|2

|p1 − p4 + ∆p1|2 − |p1 − p2|2

|p1 − p4|2

= |p1 − p2 + ∆p1|2|p1 − p4|2 − |p1 − p4 + ∆p1|2|p1 − p2|2

|p1 − p4 + ∆p1|2|p1 − p4|2

= 2|p1 − p4|2(p1 − p2) · ∆p1 − 2|p1 − p2|2(p1 − p4) · ∆p1
|p1 − p4 + ∆p1|2|p1 − p4|2

+ |p1 − p4|2|∆p1|2 − |p1 − p2|2|∆p1|2

|p1 − p4 + ∆p1|2|p1 − p4|2 .

Next divide by |∆p1|. We can ignore terms in the numerator with |∆p1|2 because they will vanish
in the limit. We rearrange to get:

2|p1 − p2|
 p1 − p2
|p1 − p2| · ∆p1
|∆p1| − |p1 − p2|
|p1 − p4| p1 − p4
|p1 − p4| · ∆p1
|∆p1|
|p1 − p4 + ∆p1|2 .

Taking the limit as |∆p1| → 0, we get:

lim
|∆p1|→0 1
∆p1
 ( |p1 − p2 + ∆p1|2

|p1 − p4 + ∆p1|2 − |p1 − p2|2

|p1 − p4|2
 ) =

2
ℓ (cos ∠(∆p1, p1p2) − cos ∠(∆p1, p1p4)),

where ℓ = |p1 − p2| = |p2 − p3| = |p3 − p4| = |p1 − p4|, and ∠(∆p1, p1p2) is the angle
between vector ∆p1 and the vector given by p1p2 = p1 − p2.
 9

Similar computations give an explicit form to dg; suppose m = |p1 − p3| = |p2 − p4|. Then

dg−→v 1(p1, p2, p3, p4) = 2
ℓ (cos ∠(∆p1, p1p2) − cos ∠(∆p1, p1p4),

− cos ∠(∆p1, p1p2), 0, m
ℓ cos ∠(∆p1, p1p3)) .

Since the angles made by ∆p1 and the sides and diagonals of a given quadrilateral cannot be chosen
so that all cosines involved vanish at once, dg−→v 1 does not vanish on Slq.

Analogous variations −→v 2, −→v 3, and −→v 4 at p2, p3, and p4 respectively, lead to the following
expressions:

dg−→v 2 = 2
ℓ (cos ∠(∆p2, p2p1), cos ∠(∆p2, p2p3) − cos ∠(∆p2, p2p1),

− cos ∠(∆p2, p2p3), − m
ℓ cos ∠(∆p2, p2p4)
)

dg−→v 3 = 2
ℓ (0, cos ∠(∆p3, p3p2), cos ∠(∆p3, p3p4) − cos ∠(∆p3, p3p2),

m
ℓ cos ∠(∆p3, p3p1)
)

dg−→v 4 = 2
ℓ
 (− cos ∠(∆p4, p4p1), 0, cos ∠(∆p4, p4p3), − m
ℓ cos ∠(∆p4, p4p2)) .

After some elementary row operations, one ﬁnds that carefully chosen variations at p1, p2, p3,
and p4 will give four linearly independent vectors at points in Slq. It follows from the Preimage
Theorem of [13] that g ⋔ (1, 1, 1, 0) and the interior of Slq is a submanifold of C4(Rk).

The boundary points in C4[Rk] are where the points of a conﬁguration come together, along
with the directions of collision and ratios of the sides. There is no difﬁculty in the plane, where
the ratios in the deﬁnition of g may be smoothly extended to the boundary. The boundary ∂Slq is
contained in the (1234) boundary face of C4[R2], and, in fact, the map g is transverse to (1, 1, 1, 0)
on this boundary. (For the sake of brevity we have omitted the details.) Thus in this special case,
Slq is actually a submanifold with boundary of C4[R2], the larger manifold with boundary.

The (pointset) boundary of Slq in C4[Rk] contains both “inﬁnitesimal” squares and conﬁgura-
tions in the (13)(24) face of C4[Rk], where the diagonals are equal to zero while the sidelengths
remain equal and nonzero. Such collisions lead to square-like quadrilaterals that are four-fold cov-
ers of an interval. We may certainly extend the map g to this face, but here we run into trouble:
Since any conﬁguration on the (13)(24) has equal sidelengths and equal diagonals, the map g is
not transverse to (1, 1, 1, 0) when restricted to this boundary face, and our argument does not show
that Slq is a submanifold with boundary of C4[Rk], the larger manifold with boundary.

We next state a useful corollary of these detailed computations. Recall ([13]) that if f : X → Y
is transverse to Z ⊂ Y and Z and X are oriented, the orientation on f −1(Z) at p ∈ X is constructed
by appending a positively oriented basis for the “horizontal” subspace of TpX to a basis for the

10

“vertical” subspace Tpf −1(Z). The vertical basis is considered positively oriented if the combined
basis is a positively oriented basis for X. We will be interested later in the free and properly
discontinuous action of Z/4Z on C4[Rk] and on Slq that cyclically permutes p1, p2, p3 and p4.
Let µ : C4[Rk] → C4[Rk] be the map corresponding to the generator of Z/4Z for this action. It is
clear from the deﬁnition of Slq that µ descends to a map from Slq to Slq.

Proposition 14. The map µ reverses orientation on both C4[Rk] and Slq if k is odd, and preserves
orientation on both Slq and C4[Rk] if k is even.

p1
 p2

p3

p4
 p3

p1
 p2p4

FIG. 3: Two tangent vectors to a conﬁguration −→p in Slq ⊂ C4[Rk] which forms a planar square. For the
tangent vector shown at left, the directional derivatives of |p1 − p3| and |p2 − p3| are positive while the
directional derivatives of all other lengths shown vanish. Clearly, we may construct a similar tangent vector
at each vertex to increase any given edgelength and corresponding diagonal length while leaving all other
lengths unchanged to ﬁrst order. On the right, we see a tangent vector where the directional derivative of
|p1 − p3| is positive, the directional derivative of |p2 − p4| is negative, and the directional derivatives of all
other lengths vanish.

Proof. We ﬁrst note that T−→p Slq ⊂ T−→p C4[Rk], and recall that a tangent vector at −→p is denoted by
−→v = v(−→p ) = (v1, v2, v3, v4), where vi is a tangent vector at pi.

To prove the proposition, we now construct some speciﬁc variations of quadrilaterals in Slq that
will behave nicely under the Z/4Z action. For squares in the plane, Figure 3 shows the construction
of two types of tangent vectors to C4[Rk] at −→p . The ﬁrst three tangent vectors are of the form
−→u = (0, u2, 0, 0), −→v = (0, 0, v3, 0) and −→w = (0, 0, 0, w4). Note −→v is shown at the left in the
ﬁgure and v3 is perpendicular to p3p4. Assume that −→p ∈ Slq has l = |p2 − p1| = |p3 − p2| =
|p4 − p3| = |p1 − p4| and l/
√
2 = |p1 − p3| = |p2 − p4|. As shown in the ﬁgure, we can arrange
to have

D−→u |p1 − p2| = +ℓ/2, D−→u |p2 − p4| = ℓ/2
√2, other directional derivs of lengths = 0,

D−→v |p2 − p3| = +ℓ/2, D−→v |p1 − p3| = ℓ/2
√2, other directional derivs of lengths = 0,

D−→w |p3 − p4| = +ℓ/2, D−→w |p2 − p4| = ℓ/2
√2, other directional derivs of lengths = 0.

11

The fourth tangent vector −→x is shown at the right in Figure 3 and has

D−→x |p1 − p3| = +ℓ/2
√2, D−→x |p2 − p4| = −ℓ/2
√2, other directional derivs of lengths = 0.

Working out the directional derivatives of s2
124, s2
231, s2
342, and s2
132 − s2
241 in these directions, we
see that Dg restricted to the span of −→u , −→v , −→w, and −→x looks like the matrix:

Dg =
 




 1 0 0 0
−1 1 0 0
0 −1 1 0
∗ ∗ ∗ 2






where the ∗ entries represent nonzero values that we don’t need to compute.

Now we make a similar construction for nonplanar conﬁgurations in Slq. Assume the square-
like quadrilateral −→p ∈ Slq has sides of length ℓ = |p1 − p2| etc., and diagonals have length
m = |p1 − p3| = |p2 − p4|. Consider the situation shown in Figure 4. Let us focus on edge
p2p3 for convenience. At p3 the plane determined by p1, p4, and p3 has normal vector, say n.
Consider the tangent vector −→n = (0, 0, n, 0). Since n is perpendicular to vectors p4p3 and p1p3,
the directional derivatives of the lengths of these edges in this direction are zero. On the other hand,
since the tetrahedron is not a planar square, p2p3 is not in the plane normal to n, so the directional
derivative of |p2 − p3| is nonzero. We can now ﬁnd some scalar multiple −→v 3 of (0, 0, n, 0) so that
D−→v 3 |p2 − p3| = ℓ/2. This implies that Dg(−→v 3) = (0, 1, −1, 0).

We can make a similar argument at vertex p1. Let n be a normal vector of the p1p2p3 plane
and ﬁnd −→v 1 parallel to (n, 0, 0, 0) so that D−→v 1 |p1 − p4| = −ℓ/2 and Dg(−→v 1) = (1, 0, 0, 0). A
similar argument at p4 yields a vector −→v 4 with D−→v 4 |p3 − p4| = ℓ/2 while preserving all other
edgelengths to ﬁrst order. Scaling appropriately, we can arrange to have Dg(−→v 4) = (0, 0, 1, 0).

As shown in Figure 4 at right, we can also ﬁnd a tangent direction −→w so that D−→w |p3 − p1| =
ℓ2/2m while the directional derivatives of all other edgelengths vanish. This choice gives
Dg(−→w) = (0, 0, 0, 1). Taken together, we have constructed a subspace of T−→p C4[Rk] given by
Span(−→v 1, −→v 3, −→v 4, −→w) on which
 Dg =
 




1 0 0 0
0 1 0 0
0 −1 1 0
0 0 0 1







Using these bases, we can now compute the effect of the Z/4Z action µ on the orientation of
C4[Rk] and Slq. First, observe that the tangent space to C4[Rk] contains of four copies of T Rk and
that reordering these from (1, 2, 3, 4) to (2, 3, 4, 1) requires 3k2 swaps of basis elements. Thus µ
is orientation preserving or reversing on C4[Rk] as k is even or odd.
 12

p4
 p1

p2

p3
 p4
 p1
p2

p3

FIG. 4: Two types of motions of a quadrilateral with equal sides and equal diagonals in Rk. Such a quadrilat-
eral is always a tetrahedron which projects to a square along the axis joining the midpoints of the diagonals.
The motion on the left increases |p2 − p4| to ﬁrst order while preserving all other edgelengths. The motion
on the right decreases the length |p3 − p4| to ﬁrst order, while preserving all other edgelengths to ﬁrst order.

Now take any positively oriented basis B for T−→p Slq and extend it by a basis B′ so that Dg
maps Span(B′) onto the tangent space to R4 in such a way that the image of Span(B′) is posi-
tively oriented with respect to the orientation of R4. We want to know whether µ(B) is positively
oriented. We know that the combined basis µ(B, B′) is positively or negatively oriented in C4[Rk]
as k is even or odd. It remains to show that Dg maps Span(µ(B′)) onto the tangent space for R4 so
that the image is positively oriented. This comes down to an explicit calculation of determinants.

For a planar conﬁguration −→p ∈ Slq, we use the basis −→u , −→v , −→w, −→x constructed above. We can
compute that, on the space Span(dµ−→p (−→u ), dµ−→p (−→v ), dµ−→p (−→w), dµ−→p (−→x )), we have:

Dg =
 





−1 1 0 0
0 −1 1 0
0 0 −1 0
∗ ∗ ∗ −2





 ,

where again, ∗ represents a value we don’t need to compute. This is a matrix of positive determi-
nant, as desired. For a non-planar conﬁguration in Slq, we use the basis −→v 1,−→v 3,−→v 4,−→w constructed
above and compute that, on Span(dµ(−→v 1), dµ(−→v 3), dµ(−→v 4), dµ(−→w)), we have

Dg =
 





0 1 0 0
0 −1 1 0
1 0 −1 0
0 ∗ 0 −1




 .

Again, this is a matrix of positive determinant, as desired.

The the third interesting submanifold of conﬁguration space is the conﬁguration space of top-
dimensional simplices with edgelengths in a given ratio.
 13

Deﬁnition 15. Suppose we have a ratio of (k+1
2 ) positive distances. It will be convenient to denote
this ratio R by (k + 1)2 coefﬁcients dij where dii = 0 and dji = dij (these are not unique). We
will call such a ratio a simplex distance ratio. The space of conﬁgurations in Ck+1[Rk] given by
points −→p = (p, α(p)) with sijk(p) = dij/dik will be denoted SimpR. This simplex distance ratio
will be called constructible if SimpR is nonempty.

The theory of distance geometry allows us to decide which ratios are constructible by a simple
calculation:

Theorem 16 (Cayley-Menger Theorem [4], (cf. [3], Section 9.7)). A simplex distance ratio R =
{dij} is constructible ⇐⇒ the Cayley-Menger determinant:

D(d11, . . . , dk+1,k+1) =
 ∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣

0 1 1 . . . 1
1 0 d2
12 . . . d2
1,k+1
1 d2
21 0 . . . d2
2,k+1
... ... ... ...
1 d2
k+1,1 d2
k+1,2 . . . 0
 ∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣

is non-negative. In fact, if dij = |pi − pj| for p1, . . . , pk+1 ∈ Rk, the volume V of the simplex
with vertices p1, . . . , pk+1 obeys

V 2(d11, . . . , dk+1,k+1) = (−1)k+1

2k(k!)2 D(d11, . . . , dk+1,k+1).

If we ﬁx the simplex distance ratio R, then we note that when the Cayley-Menger determinant
is positive, the conﬁgurations −→p ∈ SimpR consist of similar copies of the same simplex.

The Cayley-Menger determinant generalizes standard facts in triangle geometry: for instance,
for a triangle with side lengths a,b, and c we can write this determinant explicitly as

D(a, b, c) = a4 −2a
2b
2 −2a2c
2 +b
4 −2b
2c
2 +c
4 = −(a+b+c)(a+b−c)(a−b+c)(−a+b+c).

and conclude that

Area(a, b, c)2 = 1
16 (a + b + c)(a + b − c)(a − b + c)(−a + b + c).

which is Heron’s formula for the area of the triangle. We can see the triangle inequality, (a criteria
for constructability of a triangle), in this formula: the sign of the squared area would be negative
if and only if one of the side lengths was greater than the sum of the other two. Our previous
“degenerate” ratios for square-like quadrilaterals correspond to cases where one of the side lengths
is equal to the other two: in such a case the Cayley-Menger determinant (and the volume of the
simplex) vanish. This motivates the following:
 14

Deﬁnition 17. A simplex distance ratio R = {dij} is degenerate if D(d11, . . . , dk+1,k+1) = 0.

We can characterize the space SimpR in a useful way:

Proposition 18. If R is a constructible, nondegenerate simplex distance ratio, then SimpR is a
submanifold with boundary of Ck+1[Rk], diffeomorphic to O(k) × Rk × [0, ∞), and ∂ SimpR ⊂
(1 · · · k + 1) ⊂ ∂Ck+1[Rk].

Each conﬁguration −→p in SimpR is a similar copy of a single simplex, while the boundary
consists of “inﬁnitesimal” copies of the same simplex.

Proof. To construct a map f : SimpR → O(k) × Rk × [0, ∞) explicitly, take a point
−→p = (p, α(p)) in SimpR where p = (p1, . . . , pk+1), and consider the matrix of vectors
A−→p = [
π12 π13 . . . π1(k+1)]
. Since the simplex distance ratio is nondegenerate, the Cayley-
Menger theorem tells us that the column vectors of A−→p are k linearly independent vectors in Rk.
The Gram-Schmidt process provides a smooth map taking any such conﬁguration to a matrix in
O(k). We denote this process by GS(A−→p ). It is easy to see that the Gram-Schmidt process obeys
the equivariance relation GS(B · A−→p ) = B · GS(A−→p ) for any matrix B ∈ O(k).

We can now deﬁne our map to be f (−→p ) := GS(A−→p ) × p1 × |p1 − p2|. By the equivariance
property above, and the since the action of O(k) on a nondegenerate simplex −→p has no ﬁxed points,
this is a smooth bijection from SimpR to O(k) × Rk × [0, ∞). Note that when |p1 − p2| = 0
(since the ratios of all pairwise distances are ﬁxed) the simplex −→p must be “inﬁnitesimal”, and −→p
must lie in the (1 · · · k + 1) stratum. Indeed we ﬁnd ∂ SimpR ⊂ (1 · · · k + 1) ⊂ ∂Ck+1[Rk].

To show that f is a diffeomorphism, we must consider the differential of the map and prove
that it has no kernel. So consider a variation −→v of −→p . If it moves p1, then Df (−→v ) has a nonzero
component in the Rk coordinates. Noting that the action of −→v on πij changes no sijk, then if
−→v changes any pairwise distance between vertices to ﬁrst order, it changes the pairwise distance
between vertices p1 and p2 to ﬁrst order, and hence Dg(−→v ) has a nonzero component in the [0, ∞)
coordinate. So suppose that −→v changes no πij. By Alexandrov’s theorem on rigidity of convex
polyhedra (see Theorem 25 of [1]) this implies that −→v generates a motion in O(k). Differentiating
the equivariance relation above completes the proof.

By afﬁne independence, SimpR deformation retracts to O(k), and so it has the homology of
O(k). Let this projection be denoted π : SimpR → O(k). Copies of the simplex in SimpR that
share an orientation form a connected component of SimpR diffeomorphic to SO(k)×Rk ×[0, ∞];
we will denote the conﬁgurations −→p = (p1, . . . , pk+1) in SimpR where the matrix with columns
π1(k+1), . . . , πk(k+1) has positive determinant by Simp
+
R.
 15

4. CONFIGURATION SPACES AND TRANSVERSALITY

In this section, we prove a transversality “lifting property” for compactiﬁed conﬁguration
spaces: The submanifold of conﬁgurations of points on a smoothly embedded submanifold M
of Rk may be made transverse to any submanifold Z of the conﬁguration space of points in Rk

by an arbitrarily small variation of M , as long as the two submanifolds of conﬁguration space are
boundary-disjoint. This is a useful technique and parts of it have been proved before. For instance,
Budney et al. [5] prove a special case of this result. We will show that a general form of this result
may be obtained easily from the Multijet Transversality Theorem ([11], Theorem 4.13).

We begin by recalling some details about the construction of jet space and the Whitney C∞

topology on mappings. Then we will state the multijet transversality theorem and show that our
desired result on conﬁguration space transversality follows.

Deﬁnition 19. Let M and N be smooth manifolds, and f be a smooth function f : M → N . The
space of 0-jets J 0(M, N ) = M × N . The 0-jet of f is the function j0f : M → J 0(M, N ) given
by j0f (p) = (p, f (p)).

It is a standard fact that jet space J 0(M, N ) is a smooth manifold. Further, 0-jet spaces may
be extended to k-jet spaces by an inductive procedure involving taking successive derivatives. We
won’t need higher jet spaces here, so we refer the interested reader to [11] for details. We can
extend the deﬁnition of jet space to a space of n-fold multijets as follows.

Deﬁnition 20. The n-fold 0-multijets J 0
n(M, N ) are the conﬁguration space Cn(J 0(M, N )).
Given a smooth function f : M → N , there is a natural smooth map j0
nf : Cn(M ) → J 0
n(M, N )
given by
 j0
nf (−→p ) = (j0f (p1), . . . , j0f (pn)).

If this deﬁnition seems a bit puzzling, recall that the jet j0f (pi) includes the location pi as part
of its data, so there is no danger of “collisions” in the tuple (j0f (p1), . . . , j0f (pn)) because the pi
are distinct by assumption. Notice also that while the space Cn(M ) includes much more data than
the pi, all that additional data is determined uniquely by the pi so the extra information is basically
irrelevant here.

We can now state the theorem we need:

Theorem 21 (0-Multijet Transversality Theorem, [11] Theorem 4.13). Let M and N be smooth
manifolds and let Z be a submanifold of Cn(J 0(M, N )). Let

TZ = {f ∈ C∞(M, N ) | j0
nf ⋔ Z} .

Then TZ is Cm-dense in C∞(M, N ) for any m. In fact, if Z is compact, then TZ is C∞ open in
C∞(M, N ).
 16

We note that the theorem is actually a bit stronger than the version we have stated, as it shows
that TZ is a residual set, meaning a countable intersection of open dense subsets of C∞(M, N ).
We also note that the topology we’re using on C∞(M, N ) is the (standard) Whitney C∞ topology.
We can now apply this to show:

Theorem 22 (Transversality Theorem for Conﬁguration Spaces). Assume that M is a compact
manifold, smoothly embedded in Rk, with corresponding compactiﬁed conﬁguration spaces Cn[M ]
and Cn[Rk]. Assume that Z is a closed topological space contained in Cn[Rk] so that Z ∩ Cn(Rk)
is a submanifold of Cn(Rk) and the (set-theoretic) boundary of Z is contained in ∂Cn[Rk] and
is disjoint from ∂Cn[M ]. Then there exists a manifold M ′ which is C∞ close to M such that
Cn(M ′) ⋔ (Z ∩ Cn(Rk)) inside Cn(Rk) and ∂Z and ∂M ′ are disjoint in ∂Cn[Rk].

Proof. Since M is compact, the closed set Cn[M ] ∩ Z is also compact. Since this compact set is
disjoint from the closed set ∂Cn[Rk], it is separated from ∂Cn[Rk] by some ϵ > 0. Replace Z with
its intersection Z′ with the interior of the complement of an ϵ/2 neighborhood of ∂Cn[Rk]. This Z′

is now an open manifold contained in Cn(Rk) and remaining a bounded distance from ∂Cn[Rk].

Let ι : M → Rk be the inclusion map from M to Rk. We will prove that a C∞-small modiﬁ-
cation ι′ of ι gives Cn[ι′(M )] that is transverse to Z. In the ﬁrst place, since M is compact, a C∞

small modiﬁcation ι′ is still a diffeomorphism onto its image, and hence still a smooth embedding
of M into Rk with image a manifold ι′(M ) = M ′ which is C∞ close to M .

Next, since Cn[−] is a continuous map from C∞(M, Rk) to C∞(Cn[M ], Cn[Rk]), Cn[M ′]
will be C∞ close to Cn[M ] and hence we can choose the modiﬁcation of ι small enough that
the intersections of Cn[M ′] with Z′ are at least (3/4)ϵ from ∂Cn[Rk]. This means that they are
intersections with the original Z and that Cn[M ′] ⋔ Z′ =⇒ Cn[M ′] ⋔ Z. Since Z′ does not
approach ∂Cn[Rk], it sufﬁces to show that we can modify ι so that Cn(ι′) : Cn(M ) → Cn(Rk) is
transverse to Z′.

Generally speaking, the n-fold 0-multijet j0
n(ι) maps Cn(M ) into Cn(J 0(M, Rk)) = Cn(M ×
Rk); that is, it should map a disjoint collection of points pi ∈ M to a disjoint collection of pairs in
the form (pi, ι(pi)) in M × Rk. But since ι is a diffeomorphism onto its image, it is 1 − 1, and the
ι(pi) are distinct as well as the pi. This means that we can think of such a multijet as a map

j0
nι : Cn(M ) → Cn(M ) × Cn(Rk), where j0
n(−→p ) = (−→p , Cn(ι)(−→p )).

Since being a diffeomorphism onto the image is a stable property under C∞ perturbations of a
map, we may view the n-fold 0-multijet of any perturbation ι′ of ι in the same way.

Now deﬁne a (relatively open) submanifold of Cn(M ) × Cn(Rk) by Cn(M ) × Z′. Applying
Theorem 21, we see that there is some map ι′ which is C∞ close to ι so that j0
nι′ is transverse to Z.
We claim that this implies Cn(ι′) ⋔ Z′ and hence completes the proof. This follows easily from

17

the deﬁnition of transversality if we consider the commutative diagram below (π is projection).

Cn(M ) j0
nι′
- Cn(M ) × Cn(Rk)

Cn(Rk)

π

?

C n ( ι ′
) -

5. APPLICATIONS

We have now established that the conﬁguration space of n-tuples of points in Rk can be viewed
as a manifold with boundary Cn[Rk], and that, for any smooth submanifold of M of Rk, there
is a proper embedding of Cn[M ] ↪→ Cn[Rk] so that Cn[M ] is transverse to ∂Cn[Rk]. We now
specialize to the case where M is a sphere Sl and show any C1 embedding γ of Sl in Rk is C1

close to a smooth embedding γ for which Cn[γ′] is guaranteed to have certain intersections with
various “target” submanifolds of Cn[Rk] deﬁned by geometric conditions. This will prove that a
dense set of embeddings of Sl always contain certain inscribed conﬁgurations of points.

These applications will follow the same basic pattern:

• Establish the existence of a transverse intersection between Cn[Sl] and the target submani-
fold Z inside Cn[Rk] for a standard embedding of Sl. Compute the homology class of the
intersection.

• Use our transversality theorem to ﬁnd a smooth embedding γ′ of Sl which is C1-close to the
original embedding γ so that Cn[γ′] ⋔ Z. This will require that Cn[γ] and Z are boundary-
disjoint.

• Use Haeﬂiger’s theorem on smooth embeddings [14] to ﬁnd a smooth map E : Sl×I → RK

with E(−, 0) our standard embedding and E(−, 1) = γ′ (where K may be greater than our
original k). Lift E to a map Cn[Sl] × I → Cn[RK] by functoriality. Now modify this lifted
map using the transversality homotopy theorem to be transverse to Z everywhere.

• Conclude that the intersections Cn[Sl] ∩ Z and Cn[γ′] ∩ Z are cobordant in Cn[Sl] × I and
hence that they represent the same homology class in Z.

We recall Haeﬂiger’s result in a form useful to us (actually, his result is stronger). We use this
result to deform our standard spheres into the spheres of interest. Generally, such an isotopy must

18

FIG. 5: This picture shows three of the ﬁve squares inscribed in an irregular three-lobed curve and two of
the three squares inscribed in an irregular “tooth-shaped” curve. Since each family shares the vertical ﬂip
symmetry of each curve, we show the center (symmetric) square in the second and fourth pictures, while
the ﬁrst and third show half of the asymmetrical squares. While on the left curve the squares are fairly close
together, a computer search reveals that they are certainly distinct.

pass through spheres embedded in a higher-dimensional space, as when the spheres are knotted.
Since differentiable knotting is stronger than topological knotting and we prefer to work in the
differentiable category, we will need even more extra room to work1:

Theorem 23. [14] Any two differentiable embeddings of Sl in Rk are differentiably isotopic
through an isotopy in RK ⊃ Rk when K ≥ max{4l, k}.

5.1. The “square-peg” theorem

We can now prove a version of the square-peg theorem. Recall from Deﬁnition 11 that C0
4 [γ] is
the submanifold of 4-tuples on a curve γ where the points occur in order according to the orientation
of the curve, and from Deﬁnition 12 that Slq is the submanifold of conﬁgurations −→p of 4 points
in Rk with equal “sides” |p1 − p2| = |p2 − p3| = |p3 − p4| = |p4 − p1| and equal “diagonals”
|p1 − p3| = |p2 − p4|.

We will show that when C0
4 [γ] ⋔ Slq, the number of intersections is an odd multiple of 4,
giving an odd number of inscribed “squares” up to cyclic relabeling. We note that when C0
4 [γ] is
not transverse to Slq this count need not be odd, as shown by the examples of Popvassiliev [21].

Theorem 24. For any C1 curve in Rk, there is a C1 -close curve γ where

C0
4 [γ] ∩ Slq = {an odd, ﬁnite set of inscribed squarelike quadrilaterals}.

1 With various topological tameness assumptions, it would be enough to pass through l-spheres in Rl+3 by Zeeman’s
result on PL-unknotting [29], but there seems to be no practical penalty for using the differentiable result as we start
and end with a sphere in the original Rk in any case.
 19

This theorem is illustrated by the three squares inscribed in an irregular curve shown in Figure 5.

Proof. We want to compute the homology class in H0(Slq, Z) of the intersection of C0
4 [γ] and
Slq for a transverse intersection. Unfortunately, while Slq ∩ C0
4 [γ] is indeed 0-dimensional, the
intersection represents 0 in the homology H0(Slq; Z) = Z. The essential problem is that a square-
like quadrilateral can be cyclically relabeled in four ways, and it turns out that these relabelings
alternate signs in H0(Slq; Z). We can ﬁx the problem by identifying these relabelings as a single
conﬁguration:

Proposition 25. The manifolds C4[Rk], C0
4 [γ], and Slq share a smooth, free, and properly discon-
tinuous Z/4Z action given by cyclically relabeling points in a conﬁguration.

• The generator (p1, p2, p3, p4) ↦→ (p2, p3, p4, p1) is always orientation-reversing on
C0
4 [γ]. It is orientation-reversing on both C4[Rk] and Slq if k is even and orientation pre-
serving on C4[Rk] and Slq if k is odd.

• The quotient spaces by the action of Z/4Z, ˆC4[Rk] and ˆC0
4 [γ], are manifolds with boundary
and corners, with ˆC0
4 [γ] non-orientable and ˆC4[Rk] orientable as k is odd or even.

• The intersection of ̂Slq with the complement of an ϵ-neighborhood of the boundary face
(13)(24) (which is preserved under the action), is a manifold with boundary. It is orientable
precisely when ˆC4[Rk] is.

Proof. It is easy to see that this action on C4[Rk] is smooth, free and properly discontinuous and
that it descends to a corresponding action on the submanifolds C0
4 [γ] and Slq (cf. Theorem 4.2
of [22]). The second point was proved in Proposition 14 when we proved that Slq was a sub-
manifold of C4[Rk]. The other points are easy consequences. We note for the third point that the
action is actually an isometry on C4[γ], so it does descend to the ϵ-neighborhood of (13)(24) as
needed.

We now prove:

Proposition 26. In R2, if γ is a planar ellipse x2/a2 + y2/b2 = 1 with a2 ̸= b2, ˆC0
4 [γ] ⋔ ̂Slq and
the intersection represents a single square.

Proof. We will need a lemma:

Lemma 27. Parallel chords meeting an ellipse have midpoints on a line through the center of the
ellipse (where the major and minor axes meet).

Proof. This is true for a circle and preserved under afﬁne mappings.
 20

We prove that the intersection is a single square. First, if we intersect the ellipse with the
lines y = ±x, by symmetry the intersection points form a square. If we parametrize the ellipse
by (x(θ), y(θ)) = (a cos θ, b sin θ) we can work out that cos2 θ = b2/(a2 + b2) and sin
2 θ =
a2/(a2 + b2). We prove that this is the only square inscribed in the ellipse.

Suppose ABCD is any square inscribed in the ellipse. Let M denote the midpoint of AB
and N denote the midpoint of CD. Then, by Lemma 27, M N passes through the center O of the
ellipse. Similarly, if K denotes the midpoint of AD and L the midpoint of BC, then KL passes
through O. Thus O is also the center of the square. Parametrize the ellipse by θ ↦→ (a cos θ, b sin θ).
Then write
 A = (a cos α, b sin α), B = (a cos β, b sin β).

The segment OM is perpendicular to AB and so △OAM and △OBM are congruent and OA ∼=
OB. Thus
 a
2 cos2 α + b
2 sin
2 α = a2 cos2 β + b
2 sin
2 β.

This implies (a2 − b2) cos2 α = (a2 − b2) cos2 β and so, since a ̸= b, we know cos α = ± cos β.
Similarly, sin α = ± sin β. This means that B is the image of A under a symmetry of the ellipse,
and since the same argument works mutatis mutandis for C and D, the square is symmetric under
the ﬂip symmetries of the ellipse. There are two types of inscribed quadrilaterals with this symme-
try: inscribed rectangles in the form (±x, ±y), and the “exceptional” rhombus {(±a, 0), (0, ±b)}.
Since a ̸= b, the only square is our previous set of 4 points (±ab/
√a2 + b2, ±ab/
√a2 + b2).

We now prove that the intersection of ̂Slq and ˆC0
4 [γ] is transverse for the ellipse. We note that
ˆC0
4 [γ] is always far from the (12)(34) face of ˆC4[Rk], so ̂Slq is a manifold at these points. It
sufﬁces to prove transversality for C0
4 [γ] and Slq.

We will now write Slq as the inverse image of ((1, 1, 1, 1), 0) under the map f : C4[Rk] →
{xyzw = 1} ⊂ R4 × R given by (s142, s213, s324, s431) × (s132 − s241) and show that C0
4 [γ] is
transverse to Slq in C4[Rk] by showing that f restricted to C0
4 [γ] is transverse to ((1, 1, 1, 1), 0).

Consider the effect of moving x1 along the ellipse as shown on the left hand side of Fig-
ure 6. We saw above that this point is (a cos θ1, b sin θ1) where cos θ1 = b/
√a2 + b2 and
sin θ1 = a/
√a2 + b2, so the tangent vector to the ellipse dθ1 is (−a2/
√a2 + b2, b2/
√a2 + b2).
We can then compute the image of dθ1 under the differential of (s142, s213, s324, s431) to be a
positive scalar multiple (multiply by 2ab) of

⃗v1 = (a2 + b
2, −a
2, 0, −b
2)

Similarly, dθ2 and dθ3 are scalar multiples of cyclic permutations of ⃗v1. The Gram matrix of these
vectors has determinant 4(a6 + a4b2 + a2b4 + b6)2 ̸= 0. This shows that on C0
4 [γ], the differential
Df is onto the 3-dimensional tangent space to {xyzw = 1} ⊂ R4.
 21

x1x2

x3 x4
 x1x2

x3 x4

FIG. 6: These ﬁgures show that for a non-circular ellipse, C 0
4 [γ] ⋔ Slq at their intersections along the unique
square inscribed in the ellipse. On the left, we see the effect of moving only x1 = (a cos θ1, b sin θ1) along
the ellipse on the sides of the quadrilateral. This motion increases |x4 − x1| while decreasing |x1 − x2| and
a calculation shows that it changes the edgelength ratio vector (s142, s213, s324, s431) by a positive scalar
multiple of (a
2 + b
2, −a
2, 0, −b2). On the right, we see the effect of moving all the xi simultaneously on
the diagonals of the quadrilateral. The motion is decreasing the diagonal |x1 − x3| while increasing the
diagonal |x2 − x4| and a calculation shows the difference of ratios s132 − s241 decreases to ﬁrst order.

We compute the image of dθ1 under the differential of s132 − s241. If we use the facts that the
sides and diagonals of the square are equal, this differential simpliﬁes to a positive multiple of the
derivative of the diagonal |x1 − x3|, which can be written λ2(b2 − a2). Tracking through what
happens as we permute, we see that all the dθi are equal. Summing as in the right-hand side of
Figure 6 we see that this derivative does not vanish, so s132 − s241 ⋔ {0} at these points on C0
4 [γ].
Together, we have proved that f ⋔ ((1, 1, 1, 1), 0) and hence that C0
4 [γ] ⋔ Slq. We conclude that
the quotients ˆC0
4 [γ] and ̂Slq are transverse as well.

We can now complete the proof of Theorem 24. Given a C1 curve in Rk we can ﬁnd a nearby
smooth curve γ. We claim that Slq and C0
4 [γ] are boundary-disjoint in C4[Rk]. Since C0
4 [γ] does
not contact the (13)(24) or ((13)(24)) faces of C4[Rk], we need only consider the portion of Slq
on the interior of the (1234) face. These conﬁgurations are inﬁnitesimal tetrahedra with equal
sides and equal diagonals. However, conﬁgurations on the (1234) face of ∂C0
4 [γ] are inﬁnitesi-
mally collinear conﬁgurations since γ is smooth! This means that they have πij and sijk data very
different from that of conﬁgurations in ∂Slq.

We apply Theorem 22 to perturb that smooth curve to a C1-close curve η with C0
4 [η] ⋔ Slq.
As transversality is a local property and the action of Z/4Z is smooth, free, and properly discon-
tinuous, this implies that ˆC0
4 [η] ⋔ ̂Slq as well. As before, Haeﬂiger’s Theorem 23 guarantees a
differentiable isotopy between the ellipse and η, and we can lift the isotopy to ˆC4[Rk], perturbing
it without changing the ends so that it is transverse to ̂Slq everywhere. This means that the ﬁnite
collection of points (0-manifold) ˆC0
4 [γ] ∩ ̂Slq is cobordant by a 1-manifold to the single square in
the initial ellipse in ̂Slq, and hence that the number of inscribed squares is odd.

A few historical comments are in order here. First, this is certainly not the ﬁrst proof of the

22

square-peg theorem to use an intersection-theoretic approach. Grifﬁths [12] took a similar ap-
proach, though he seems to have failed to appreciate the orientation-reversing nature of the cyclic
permutation on C4[Rk]. As a result, he (wrongly) computes a different intersection number to be
16 instead of zero, and claims as a result to have proved not only the square-peg theorem but a
“rectangular-peg theorem”. The rectangular case does not admit the quotient-space simpliﬁcation
above (there are generally two inscribed rectangles of a given aspect ratio in the ellipse). As far as
we know, the “rectangular-peg theorem” is an open and difﬁcult problem. Matschke [18] proved a
version of the square-peg theorem from a theorem about loops of polygons inscribed in curves by
arguing that a loop of rhombi which was invariant under the cyclic permutation contained a square
by the intermediate value theorem, also an approach followed by Schnirel’man [28].

5.2. Generic spheres have inscribed simplicies

In this section, we explore a sort of reverse version of our basic framework. Previously, we used
Haeﬂiger’s theorem to construct a map E : Sl × I → Rk encoding the isotopy between our initial
and target spheres that was transverse to Z at both ends. But Haeﬂiger’s theorem really gives us a
collection of diffeomorphisms Ft of Rk parametrized by t so that F0 is the identity and F1 maps
our initial Sl to the target Sl and the compositions of F0 and F1 with our standard embedding were
transverse to Z. Now we note that this construction works in reverse: Composing the inclusion
Z ↪→ Cn[Rk] with the family F −1
t we get a family of maps E : Z × I → Cn[Rk] so that E(−, 0)
and E(−, 1) are transverse to Cn[Sl]. Running through the rest of our standard argument, we see
that Cn[Sl] ∩ Z and Cn[γ′] ∩ Z are cobordant in Z × I and hence represent the same homology
class in Z.

For instance, if we let Z = equilateral triangles in R2, we could compute H1(Z; Z) ≃ Z, be-
cause Z deformation retracts to S1, and then show that the submanifold of inscribed equilateral
triangles in a curve represents +1 in H1(Z; Z) = Z. We now prove a more general version of
that theorem for inscribed simplices in higher-dimensional spheres, such as the inscribed regular
tetrahedron in the irregular surface of Figure 7. To do so, recall that we showed in Proposition 18
that the space SimpR of simplices in Rk with vertex-vertex distances in any nondegenerate, con-
structible ratio (cf. Deﬁnition 15) is a submanifold of Ck+1[Rk] homotopic to O(k). Also recall that
Simp
+
R is the set of conﬁgurations in SimpR where the matrix with columns π1(k+1), . . . , πk(k+1)
has positive determinant.

Theorem 28 (Inscribed Simplex Theorem). For any C1 embedding of Sk−1 in Rk and any non-
degenerate, constructible simplex distance ratio R, there is a C1-close embedding γ so that
Simp
+
R ∩ Ck+1[γ] is a smooth, orientable k(k − 1)/2-dimensional manifold. Further, the pro-
jection π : Simp
+
R → SO(k) induces the map

π∗ : Hk(k−1)/2(Simp
+
R ∩ Ck+1[γ]; Z) ≃ Z → Hk(k−1)/2(SO(k); Z) ≃ Z, π∗(+1) = +1.

23

FIG. 7: On the left, we see an irregular embedding of S2 in R3 described in spherical coordinates as a
graph over the unit sphere by the function r(φ, θ) = 1 + sin3 φ sin 3θ/5 − | cos7 φ|. The center and
right images show different views of a single regular tetrahedron inscribed in this surface with edge-
lengths close to 1.15. If this embedding of S2 is transverse to the submanifold of regular tetrahedra, this
tetrahedron is a member of the 3-dimensional family of inscribed regular tetrahedra predicted by Theo-
rem 28. This tetrahedron was found by computer search. Its vertices have spherical (φ, θ) coordinates
(0.224399, 0.224399), (1.5708, 3.36599), (1.5708, 2.0196), (2.91719, 0.224399).

In particular, given a standard simplex ∆ with distance ratio R and any element A ∈ SO(k), there
is a scale and translation so that the scaled, translated copy of A∆ is inscribed in γ.

To get a sense of the meaning of this theorem, it tells us that any C1 embedding of the sphere in
R3 is C1-close to an embedding with a 3-dimensional family of inscribed regular tetrahedra. Since
the space of inscribed quadruples in a sphere is eight dimensional and the regularity of the tetrahe-
dron is encoded by a speciﬁc ratio among six pairwise distances between vertices (a codimension
ﬁve constraint), this result has at least the correct dimension (though it may be surprising that there
is an entire SO(3) of inscribed tetrahedra in such a sphere!).

Proof. As before, we will follow our standard pattern: establish a base case and a modiﬁcation
of the given embedding that ensures a transverse intersection using boundary-disjointness of the
two submanifolds of Ck+1[Rk], use Haeﬂiger’s theorem to ﬁnd an isotopy, and use transversality
to complete the proof.

Proposition 29. If Sk−1 is the unit (k − 1)-sphere, Simp
+
R ⋔ Ck+1[Sk−1] with π : (Simp+
R) ∩
Ck+1[Sk−1] → SO(k) a diffeomorphism.

Proof. We need another useful fact from distance geometry:

Theorem 30 (Proposition 9.7.3.7 [3]). A simplex x = (x1, . . . , xk+1) ∈ Ck+1[Rk] with pairwise
distances dij and D(d11, . . . , dk+1,k+1) > 0 is inscribed in a unique (k − 1)-sphere of radius

24

ρ(d11, . . . , dk+1,k+1) where
 ρ
2 = −
 ∣
∣
∣
∣
∣
∣
∣
∣
∣
 0 d2
12 · · · d2
1,k+1
d2
21 0 · · · d2
2,k+1
... ... ...
d2
k+1,1 d2
k+1,2 · · · 0
 ∣
∣
∣
∣
∣
∣
∣
∣
∣

2D(d11, . . . , dk+1,k+1) (1)

Given any x ∈ Simp
+
R ∩ Ck+1[Sk−1], the theorem immediately implies that the scale and posi-
tion (of the circumcenter) of x are ﬁxed, while the orientation of x is given uniquely by an element
of SO(k), proving the second half of the theorem.

Proving transversality is more interesting. For x ∈ Ck+1[Sk−1], the orthogonal comple-
ment of TxCk+1[Sk−1] in TxCk+1[Rk] is the (k + 1)-dimensional space with orthonormal ba-
sis B = {(x1, 0, . . . , 0), . . . , (0, . . . , xk+1)}. The tangent space Tx Simp
+
R contains the vectors
(e1, . . . , e1), . . . , (ek, . . . , ek) from the translational component of Simp
+
R as well as the vector
(x1, . . . , xk+1) from scaling the conﬁguration x. Writing these vectors in the basis B, we get the
matrix:
 M =
 







x1,1 x2,1 · · · xk+1,1
x1,2 x2,2 · · · xk+1,2
... ... ...
x1,k x2,k · · · xk+1,k
1 1 · · · 1
 






 .

Subtracting the last column from the rest, we get

M ′ = (
x1 − xk+1 x2 − xk+1 · · · xk − xk+1 xk+1
0 0 · · · 0 1
 ) .

The determinant of this matrix is ±1 multiplied by the determinant of the upper-left k × k principal
minor. But that determinant is positive because x ∈ Simp
+
R.

Proposition 31. If γ is a smooth embedding of Sk−1 in Rk and R is a constructible and nonde-
generate simplex distance ratio, the smooth submanifolds Ck+1[γ] and SimpR of Ck+1[Rk] are
boundary disjoint.

Proof. Since R is nondegenerate, ∂ SimpR is contained in the (1 · · · k + 1) face of ∂Ck+1[Rk]
where all points come together.

The collection of πij maps determines a continuous map Π : Ck+1[Rk] → (Sk−1)k(k+1).
Further, SO(k) acts diagonally on both sides of this map. Since R is nondegenerate, for any

25

x ∈ SimpR, the directions in Π(x) do not lie on any great Sk−2 (otherwise, the simplex would lie
in a hyperplane and hence have zero volume). Let χ(p) be the squared distance between a point
conﬁguration in (Sk−1)k(k+1) and the nearest conﬁguration in a (diagonal) great (Sk−2)k(k+1).
Since χ(p) is invariant under the diagonal action of SO(k) on (Sk−1)k(k+1), and Π(x) is invariant
under translation and scaling, the map χ ◦ Π is constant and nonzero on SimpR. However, the
inﬁnitesimal conﬁgurations in the (1 · · · k + 1) face of ∂Ck+1[γ] do lie in a great Sk−2 determined
by the tangent space to γ, and so χ = 0 on this face of ∂Ck+1[γ]. This implies that ∂ SimpR and
∂Ck+1[γ] are disjoint, as desired.

Given a C1 embedding of Sk−1 in Rk, we can smooth it and apply Theorem 22 to ﬁnd a C1-
close smooth (k − 1)-sphere γ with Ck+1[γ] ⋔ Simp
+
R, using Proposition 31 to show that Ck+1[γ]
and Simp
+
R are boundary disjoint, as required by Theorem 22.

As before, Haeﬂiger’s Theorem 23 guarantees a differentiable isotopy between the standard unit
Sk−1 and γ. The new step is that we invert this isotopy to get a map E : Simp
+
R ×I → Ck+1[Rk],
so that E(−, 0) and E(−, 1) are transverse to the standard unit Sk−1, E(Simp
+
R, 0) is the standard
Simp
+
R, and there’s a diffeomorphism of Rk which carries E(−, 1) to Simp
+
R and the standard
Sk−1 to γ. The rest of the proof goes as before.

6. FUTURE DIRECTIONS

One of the recurring features of this work is that the introduction of compactiﬁed conﬁguration
spaces simpliﬁes many of the tricky technical pieces in the proof by exporting the troublesome
behavior to the boundaries. For example, applying a transversality theorem to squares and conﬁg-
urations of inscribed quadrilaterals requires us to have some strategy for dealing with “degenerate”
conﬁgurations. The extension of the πij and sijk data to the boundary of conﬁguration space (with
the associated metric) allowed us to argue easily that there could be no inﬁnitesimal squares in-
scribed on a smooth curve. On the other hand, this is not the only way to address these difﬁculties:
For instance, Stromquist [23] deals with basically the same problem by showing directly that there
are no squares (or square-like quadrilaterals) smaller than some ϵ which can be inscribed on a curve
with some mild smoothness assumptions and hence avoids the dangerous diagonals of the product
space (Rk)4. We give a similar argument in the Appendix to show:

Theorem 32. Any closed curve in Rn of ﬁnite total curvature with no cusps has at least one
inscribed square-like quadrilateral.

We note that since this result is obtained by a limit argument, we cannot rule out the possibility
that several squares come together in the limit to leave an even number of squares inscribed in the
ﬁnal curve, as in the examples of [21]. The appeal of this result is largely that the class of curves
of ﬁnite total curvature is a well-understood space (cf. [24]). It is not hard to see that Stromquist’s
theorem [23] is more general.
 26

A very interesting possible extension of the methods here would be to use the 1-jet version of
multijet transversality to try to prove a transversality theorem for submanifolds of conﬁguration
spaces which do intersect in certain boundary faces. Doing so would allow one to extend the
“counting” and homology arguments above to detect boundary intersections between submanifolds
of conﬁguration spaces. For example, one might try to argue in this way that the space of triangles
with a given angle inscribed in a curve had the homology of the torus, keeping in mind that a
circle’s worth of such “triangles” would be expected to be chords meeting the tangent to the curve
in the speciﬁed angle. Another interesting use for such a theorem would be to try to extend these
theorems to immersed curves with normal crossings (as opposed to simply studying embedded
curves).

We have proved that the space of curves with an odd number of squares are C1-dense among
C1 curves in the plane (or residual among smooth curves). This is not quite the same as proving
that a “generic” C1 curve has an odd number of inscribed squares. It would be very interesting to
try to extend these results to a set of curves which was full-measure among plane curves according
to some natural measure on curves, as Morgan does in [19] for space curves bounding a unique
area-minimizing surface.
 Acknowledgments

The authors would like to ﬁrst thank Gerry Dunn who introduced us to the problem. We would
also like to thank the people who have discussed the problem with us over the years: Jordan Ellen-
berg, Richard Jerrard, Rob Kusner, Benjamin Matschke, Igor Pak, Strashimir Popvassiliev, John
M. Sullivan, Cliff Taubes, and Gunter Ziegler.

[1] A. D. Alexandrov. Convex polyhedra. Springer Monographs in Mathematics. Springer-Verlag, Berlin,
2005. Translated from the 1950 Russian edition by N. S. Dairbekov, S. S. Kutateladze and A. B.
Sossinsky, With comments and bibliography by V. A. Zalgaller and appendices by L. A. Shor and Yu.
A. Volkov.
[2] Scott Axelrod and I. M. Singer. Chern-Simons perturbation theory. II. J. Differential Geom.,
39(1):173–213, 1994.
[3] Marcel Berger. Geometry I. Universitext. Springer-Verlag, Berlin, 2009. Translated from the 1977
French original by M. Cole and S. Levy, Fourth printing of the 1987 English translation.
[4] L. M. Blumenthal and B. E. Gillam. Distribution of points in n-space. Amer. Math. Monthly, 50:181–
185, 1943.
[5] Ryan Budney, James Conant, Kevin P. Scannell, and Dev P. Sinha. New perspectives on self-linking.
Adv. Math., 191(1):78–113, 2005.
 27

[6] Jason Cantarella, Elizabeth Denne, and John McCleary. Conﬁguration Spaces, Multijet Transversality,
and the Square-Peg Problem. Preprint 2021.
[7] Jason Cantarella, Elizabeth Denne, and John McCleary. Square-like quadrilaterals inscribed in embed-
ded space curves. Preprint 2021.
[8] Jason Cantarella, Elizabeth Denne, and John McCleary. Families of similar simplices inscribed in most
smoothly embedded spheres. Preprint 2021.
[9] David Cohen-Steiner and Herbert Edelsbrunner. Inequalities for the curvature of curves and surfaces.
Found. Comput. Math., 7(4):391–404, 2007.
[10] William Fulton and Robert MacPherson. A compactiﬁcation of conﬁguration spaces. Ann. of Math.
(2), 139(1):183–225, 1994.
[11] M. Golubitsky and V. Guillemin. Stable mappings and their singularities. Springer-Verlag, New York,
1973. Graduate Texts in Mathematics, Vol. 14.
[12] H. Brian Grifﬁths. The topology of square pegs in round holes. Proc. London Math. Soc. (3),
62(3):647–672, 1991.
[13] Victor Guillemin and Alan Pollack. Differential topology. AMS Chelsea Publishing, Providence, RI,
2010.
[14] Andr´e Haeﬂiger. Differentiable imbeddings. Bull. Amer. Math. Soc., 67:109–112, 1961.
[15] Victor Klee and Stan Wagon. Old and new unsolved problems in plane geometry and number theory.
The Dolciani Mathematical Expositions, 11. Mathematical Association of America, 1991.
[16] J. Li and T. J. Peters. Isotopic convergence theorem. J. Knot Theory Ramiﬁcations, 22(3):1350012,
18, 2013.
[17] Benjamin Matschke. A survey on the Square Peg Problem. Notices AMS to appear.
[18] Benjamin Matschke. On the Square Peg Problem and some Relatives. arXiv.org, math.MG:186,
December 2009.
[19] Frank Morgan. Almost Every Curve in R3 Bounds a Unique Area Minimizing Surface. Inventiones
Mathematicae, 45:253, 1978.
[20] Igor Pak. Lectures on Discrete and Polyhedral Geometry. Free online text. 2010.
[21] Strashimir G. Popvassilev. On the number of inscribed squares of a simple closed curve in the plane.
arXiv.org, 0810:4806, October 2008.
[22] Dev P. Sinha. Manifold-theoretic compactiﬁcations of conﬁguration spaces. Selecta Math. (N.S.),
10(3):391–428, 2004.
[23] Walter Stromquist. Inscribed squares and square-like quadrilaterals in closed curves. Mathematika,
36(2):187–197, 1989.
[24] John M. Sullivan. Curves of ﬁnite total curvature. In Discrete differential geometry, volume 38 of
Oberwolfach Semin., pages 137–161. Birkh¨auser, Basel, 2008.
[25] Otto Toeplitz. Verhandlungen der Schweizerischen Naturforschended Gesellschaft in Solothura, page
197, August 1911.
[26] A. C. M. van Rooij. The total curvature of curves. Duke Math. J., 32:313–324, 1965.
[27] Ismar Voli´c. A survey of Bott-Taubes integration. J. Knot Theory Ramiﬁcations, 16(1):1–42, 2007.
[28] L G von Schnirelman. On certain geometrical properties of closed curves. Uspehi Matem. Nauk,
10:34–44, 1944.
[29] E. C. Zeeman. Unknotting Combinatorial Balls. The Annals of Mathematics, 78(3):501–526, 1963.

28

Appendix: Finite Total Curvature Curves without Cusps

We have shown that every C1 curve in Rk is C1-close to a smooth curve with an odd number
of inscribed square-like quadrilaterals. This means that any curve which may be approximated
by a sequence of C1 curves may be approximated by a sequence of smooth curves with inscribed
squares. Can we use this argument to extract at least one limiting inscribed square-like quadri-
lateral on any curve in Rk? The problem is clear: The sequence of square-like quadrilaterals on
the approximating curves may have sidelengths approaching zero. If one could construct a general
lower bound on these sidelengths in terms of the global geometry of the “host” curve, this possibil-
ity could be ruled out. We do not know of any explicit example of a family of curves where all the
inscribed square-like quadrilaterals have sidelengths converging to zero, so this approach may yet
be possible. However, this line of attack has been more or less obvious from the start, and nobody
has managed to construct such an argument in the past century.

Our considerably more modest goal in this section is to rule out small square-like quadrilaterals
using local, rather than global, data about the limit curve, and in this way to extend our results to
the class of curves of ﬁnite total curvature without cusps (FTCWC), which is deﬁned below.

Our argument has three parts. First, we show that each curve γ in FTCWC has no inscribed
square-like quadrilaterals with side length smaller than a positive constant, denoted by π-d(γ).
Next, we show that γ is the limit of a sequence of smooth curves γi, for which π-d(γi) → π-d(γ),
each containing an odd number of inscribed square-like quadrilaterals. The ﬁrst two steps then
imply that this sequence of square-like quadrilaterals has a convergent subsequence with limit a
square-like quadrilateral with sidelength at least π-d(γ).

We recall some standard facts about curves of ﬁnite total curvature [24, 26]. The total curvature
of a curve is the supremum of the total turning angles of all polygons inscribed in the curve. If this
supremum is ﬁnite, we say the curve has ﬁnite total curvature or is in FTC. Curves in FTC
have a number of desirable properties. They are always rectiﬁable, and so can be parametrized by
arclength. They are almost everywhere differentiable, and a curve in FTC has one-sided tangent
vectors at every point. In fact, these tangents differ only at countably many corner points. There is
a Radon measure κ on every γ in FTC whose mass on any open subarc of γ is the total curvature
(in the above sense) of the subarc. This measure has a countable number of atoms at corners of the
curve γ. The mass of each atom is the turning angle between these vectors. If this turning angle is
π, we say the corner is a cusp.

Since FTC curves have a second derivative (at least weakly) it is natural to want to approximate
them “in C2” by smooth curves. Unfortunately, this is not quite possible. Note that the tangent
indicatrix to an FTC curve has gaps at the corners of the curve, while the tangent indicatrix of a
smooth curve forms a continuous curve on S2. Thus the tangent vectors to a sequence of smooth
curves approximating an FTC curve can’t converge to tangents of the FTC curve near a corner of
the FTC curve. However, we can come very close to a C2 approximation in the following sense:

29

Deﬁnition 33. Suppose γ is an FTC curve. Let Len(γ, a, b) be the length of the arc of γ between
γ(a) and γ(b) and κ(γ, a, b) be the total curvature of this arc. We say that a sequence of ﬁnite total
curvature curves γi approximate γ uniformly in position, arclength, and total curvature if there are
parametrizations of the γi so that for each ϵ > 0 there exists an N so that for all i > N , we have
the following:

1. For any a, |γi(a) − γ(a)| < ϵ.

2. For any arc (a, b), |Len(γi, a, b) − Len(γ, a, b)| < ϵ.

3. For any arc (a, b), |κ(γi, a, b) − κ(γ, a, b)| < ϵ.

Proposition 34. Any FTC curve γ may be approximated uniformly in position, arclength, and
total curvature by smooth FTC curves γi.

Proof. This is an assembly of standard results about FTC curves. If we inscribe polygons with
vertices equally spaced by arclength in γ, and parametrize them compatibly (so that the vertices
have the same parameter values on γ and on each polygon), the polygons converge uniformly in
position and total curvature (cf. Lemma 4.2 of [16]) and are all ﬁnite-total curvature curves (since
their total curvatures are bounded by that of γ).

To see that they converge uniformly in arclength, ﬁx an arc (a, b) of γ, and observe that the
corresponding arcs of the γi have bounded total curvature, and converge to the arc of γ in Fr´echet
distance because they converge in position. Then use Theorem 5.1 of [26] (see also [9]) which
states that for any rectiﬁable curves K, L,

| Len(K) − Len(L)| ≤ δ(K, L)(π max TC(K), TC(L) + 2)

where δ(K, L) is the Fr´echet distance between K and L. Note that this theorem is not obvious: it
says that the standard examples of curves which converge in Fr´echet distance but not in arclength,
such as a stairstep curve converging to the diagonal of a square, must all have unbounded total
curvature.

To ﬁnish the proof, smooth each polygon by rounding off corners– the smooth curves have the
same total curvature as the polygons (and are hence FTC) and are close to the original polygons in
position, arclength, and total curvature, as required.

Notice that if a square-like quadrilateral pqrs is inscribed in an arc of γ, the total curvature of
the arc γpqrs must be at least as large as the total curvature (or total turning angle) of the inscribed
polygon pqrs. If pqrs is a planar square, it is clear that this turning angle is π. We now prove that
the turning angle is at least π if pqrs is a square-like quadrilateral.

Lemma 35. Any square-like quadrilateral pqrs has the property that κ(pqrs) ≥ π, with equality
if and only if pqrs is a planar square.
 30

p

q
 s
 r

cos θ

sin θ

t θ

FIG. 8: The arc γpqrs of the square-like quadrilateral shown has total curvature given by 2π − 4θ. We
observe, however, that pt has length cos θ and qt has length sin θ, while 2qt = qs = pr is less than 2pt.
Thus cos θ ≥ sin θ and θ ≤ π/4.

Proof. Consider the situation of Figure 8 where pqrs has equal sides pq, qr, rs, and sq and equal
diagonals pr and qs. We may assume without loss of generality that the sides have length 1. We
construct the midpoint t of qs. Since △pqs is isosceles, we can conclude that ∠qps = 2θ and
that ∠ptq is right. We then have pt = cos θ and qt = sin θ. Further, since qs = pr, we have
pr = 2 sin θ.

Since pq = rq and ps = rs, we have △rqs ∼= △pqs. Thus ∠qrs = ∠qps = 2θ and as above
rt = cos θ. So by the triangle inequality (on △ptr) we have pt + tr ≥ pr, or

2 cos θ ≥ 2 sin θ.

This means that θ ≤ π/4, and θ = π/4 if and only if t is on the line pr. In this case pqrs is planar
(and hence it is a square). Now the turning angle of the arc pqrs is π − 2θ at q and r. Thus the total
turning angle of pqrs is 2π − 4θ ≥ π, as desired.

Our overall goal is to prove that there exists an ϵ > 0 for each curve in FTCWC so that no
square-like quadrilateral inscribed in γ has sidelength less than ϵ.

Deﬁnition 36. We deﬁne the π-distance of an FTC curve γ, denoted π-d(γ). The value ℓ is an
admissible distance bound if every open subarc (a, b) of γ with |γ(a) − γ(b)| < ℓ has κ(γ, a, b) <
π. Then
 π-d(γ) = sup
ℓ is admissible ℓ = inf
ℓ is inadmissible ℓ.

Note that if ℓ is inadmissible, then there is some subarc (a, b) with |γ(a) − γ(b)| < ℓ, but
κ(γ, a, b) ≥ π. The point of π-d(γ) is that it provides a lower bound on the side length of a
square-like quadrilateral inscribed in γ.

Lemma 37. Any square-like quadrilateral inscribed in an FTC curve γ has sidelength greater than
or equal to π-d(γ).
 31

Proof. Let pqrs be an inscribed square-like quadrilateral in γ, and consider the arc pqrs which
has end-to-end distance |γ(p) − γ(s)|. By Lemma 35, the square-like quadrilateral is an inscribed
polygon with total curvature at least π. Thus κ(γ, p, s) ≥ π. This means that |γ(p) − γ(s)| is an
inadmissible distance bound, and hence it is at least π-d(γ), as desired.

We now want to show that an embedded curve in FTCWC is the limit of a sequence of smooth
curves with inscribed square-like quadrilaterals with side lengths uniformly bounded above zero.
We proceed in two steps: ﬁrst we’ll show that γ itself has π-d bounded above, then that π-d behaves
nicely under the sort of convergence of curves we introduced above.

Lemma 38. If γ is an embedded curve in FTCWC, then π-d(γ) > 0.

Proof. Suppose not. Since π-d(γ) = 0, there is a sequence of inadmissible ℓi → 0. So there
exists a collection of open subarcs Ai of γ whose endpoints ai, bi have |γ(ai) − γ(bi)| → 0, while
κ(γ, ai, bi) ≥ π. Passing to a subsequence where ai → a and bi → b, we see that γ(a) = γ(b),
and hence a = b because γ is embedded.

Now as the Ai approach {a}, their total curvature κ(Ai) ≥ π. Since γ is compact, we may
pass to a subsequence of Ai that are nested and converge to a point p. Since κ is an outer-regular
measure, this means that κ(p) ≥ π. Since κ(p) is a turning angle, it is always ≤ π. Thus κ(p) = π
and p is a cusp point, contradicting our assumption that γ was in FTCWC.

Since π-d is deﬁned by lengths, distances, and curvatures, we can expect it to behave nicely as
we take limits in the sense of Deﬁnition 33.

Proposition 39. If γi → γ uniformly in position, arclength, and total curvature in the sense of
Deﬁnition 33, and π-d(γ) > 0, then limi→∞ π-d(γi) > 0.

Proof. Suppose not. For any ϵ > 0, there must be inﬁnitely many γi with π-d(γi) < ϵ. Each γi
contains a subarc (ai, bi) with |γi(ai) − γi(bi)| < ϵ, but κ(γi, ai, bi) ≥ π. By compactness, we can
assume that we have passed to a subsequence where ai → a and bi → b.

Now by convergence in position, |γ(a) − γ(b)| ≤ ϵ. Let us expand the open arc (a, b) of γ
slightly to an open subarc (a′, b′) with |γ(a′) − γ(b′)| ≤ 3ϵ, say, and again pass to a subsequence
where (ai, bi) ⊂ (a′, b′) for all i. Now for any δ > 0, by convergence in total curvature, for large
enough i we have ∣
∣κ(γ, a′, b
′) − κ(γi, a
′, b
′)
∣
∣ < δ

so
 κ(γ, a′, b
′) > κ(γi, a
′, b
′) − δ ≥ κ(γi, ai, bi) − δ ≥ π − δ.
 32

where κ(γi, a′, b′) ≥ κ(γi, ai, bi) because (ai, bi) ⊂ (a′, b′). Since δ was arbitrary, this proves that
κ(γ, a′, b′) ≥ π.

However, this means that 3ϵ > |γ(a′) − γ(b′)| is an inadmissible distance bound for γ, and
hence that π-d(γ) < 3ϵ. Since ϵ was arbitrary, this proves that π-d(γ) = 0, providing the required
contradiction.

We are ready to construct an inscribed square-like quadrilateral on any FTCWC curve. We
have done all the hard work above; it remains only to assemble the component pieces.

Theorem 40. There is an inscribed square-like quadrilateral on any embedded curve γ in
FTCWC. In particular, there is an inscribed square-like quadrilateral on any embedded C2-
smooth curve γ.

Proof. First, we may approximate γ by a sequence of smooth curves γi with convergence in po-
sition, arclength, and total curvature by Proposition 34. By making a C2-small perturbation of
each γi, we may assume by Theorem 24 that each γi contains at least one inscribed square-like
quadrilateral . Since our perturbations were C2-small, the sequence of curves γi still enjoys ﬁnite
total curvature and converges to γ in position, arclength, and total curvature.

By Lemma 38 and Proposition 39, there is an ϵ > 0 so that we may pass to a subsequence of γi,
each of which has π-d(γi) > ϵ. By Lemma 37 the inscribed square-like quadrilateral on each γi
has sidelength at least ϵ. This is the crucial point in the proof: by bounding the sidelengths of these
square-like quadrilaterals below, we have ensured that they do not shrink away as we approach the
limiting curve γ.

From here, the argument is standard. We may assume that the inscribed square-like quadrilat-
erals in the γi lie in a compact subset of Slq, and hence that they have a convergent subsequence.
The limit of this subsequence is a square-like quadrilateral inscribed in the limit curve γ.

Note that we have lost something here: it is possible that multiple square-like quadrilaterals
coincide on the limiting curve γ, so the count of inscribed square-like quadrilaterals may no longer
be odd, as shown by the examples of Popvassiliev [21].

Also note that there exist C1 curves that are not FTC; these don’t have corners but have spirals
where curvature diverges. For these curves, Theorem 24 still holds, but we can not conclude from
Theorem 40 that there is at least one square-like quadrilateral . (The spirals prevent the arguments
of Proposition 39 from holding.)
 33
