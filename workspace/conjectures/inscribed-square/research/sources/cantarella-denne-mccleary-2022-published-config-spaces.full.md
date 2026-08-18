<!-- source: https://arxiv.org/pdf/2103.07506 | converted from PDF -->

CONFIGURATION SPACES, MULTIJET TRANSVERSALITY, AND THE
SQUARE-PEG PROBLEM

JASON CANTARELLA, ELIZABETH DENNE, AND JOHN MCCLEARY

ABSTRACT. We prove a transversality “lifting property” for compactiﬁed conﬁguration spaces as
an application of the multijet transversality theorem: given a submanifold of conﬁgurations of points
on an embedding of a compact manifold M in Euclidean space, we can ﬁnd a dense set of smooth
embeddings of M for which the corresponding conﬁguration space of points is transverse to any
submanifold of the conﬁguration space of points in Euclidean space, as long as the two submanifolds
of compactiﬁed conﬁguration space are boundary-disjoint. We use this setup to provide an attractive
proof of the square-peg problem: there is a dense family of smoothly embedded circles in the plane
where each simple closed curve has an odd number of inscribed squares, and there is a dense family
of smoothly embedded circles in Rn where each simple closed curve has an odd number of inscribed
square-like quadrilaterals.
 1. INTRODUCTION

Given a simple closed curve (a Jordan curve) γ in R2, can we ﬁnd four points on γ that form
a square? This question was posed by O. Toeplitz in 1911 [47], and it has drawn the attention of
many mathematicians since that time. Thinking of the Jordan curve as a “round hole”, the problem
has been affectionately dubbed the “square-peg” problem. We say that the square is inscribed in
γ when the vertices lie on the curve. (We do not require that the square lie entirely in the interior
of the curve.) In the form posed by Toeplitz, the problem remains open. The earliest contribution
to the problem is due to A. Emch [9, 10, 11] who showed that there are squares on convex curves.
Progress on the square-peg problem has chieﬂy been extension of the regularity class of simple
closed curves for which the square can be found. The interested reader can ﬁnd numerous articles
[8, 24, 36, 30, 46] summarizing the problem, and describing the classes of curves for which the
Toeplitz conjecture has been proved.
The square-peg problem can be framed in terms of conﬁguration spaces of points. First, consider
the compactiﬁed conﬁguration space C4[R2] of 4-tuples of points in the plane as a manifold-with-
boundary (and corners). Then, the existence of inscribed squares can be rephrased more simply as
a question about the intersections of two submanifolds of C4[R2]. The ﬁrst is the submanifold of
4-tuples of points on an embedding γ : S1 ↪→ R2 of a circle in the plane, denoted by C4[γ(S1)];
the second is the submanifold of squares in the plane, denoted by Slq.

Date: June 8, 2022.
2020 Mathematics Subject Classiﬁcation. Primary 53A04, Secondary 55R80, 57Q65, 58A20, 51M04.
Key words and phrases. Conﬁguration spaces, multijet transversality, square-peg problem, squares, square-like
quadrilaterals, Jordan curves, embedded space curves. 1arXiv:2103.07506v2  [math.GT]  7 Jun 2022
2 JASON CANTARELLA, ELIZABETH DENNE, AND JOHN MCCLEARY

Thus, the square-peg problem is an example of the general problem of ﬁnding special geometric
conﬁgurations on families of manifolds. Theorems of a similar nature include S. Kakutani’s theo-
rem [23] that a compact convex body in R3 has a circumscribed cube, that is, a cube each of whose
faces touch the convex body; the work of A. Akoypan and R. Karasev [2] answers whether a convex
polytope admits an inscribed regular octahedron. In addition, there is the work of P.V.M. Blago-
jevi´c and G. Ziegler [5] on inscribed tetrahedra in spheres; G. Kuperberg [25] and V.V. Makeev
[27] on inscribed and circumscribed polyhedra in convex bodies and spheres. Compactiﬁed con-
ﬁguration spaces have also been used by S.T. Vre´cica and R.T. ˇZivaljevi´c, T. Rade [50] in their
paper looking at the polygonal peg problem (inscribed afﬁne regular hexagons in smooth Jordan
curves, and inscribed parallelograms in smooth simple closed curves in R3). There have also been
many papers [1, 3, 14, 15, 21, 22, 26, 31, 41, 40] examining quadrilaterals inscribed in curves and,
more recently, making progress towards solving the rectangular-peg problem (ﬁnding rectangles of
any aspect ratio inscribed in Jordan curves).
Here is an outline of our approach. We suppose that we seek a special conﬁguration of n points
to be found on a compact manifold M that is smoothly embedded in Rk. We let the smooth
embedding be denoted by γ : M ↪→ Rk. Then, in the compactiﬁed conﬁguration space Cn[Rk] of n
points in Rk, there are two subspaces of interest: Cn[γ(M )], the compactiﬁed conﬁguration space
of n points on γ(M ); and Z the subspace of tuples of n points in Rk that satisfy the conditions of
a special conﬁguration. For example, in the square-peg problem, γ(S1) is a smooth simple closed
curve in R2, and the special conﬁgurations Z are squares in R2.
Why do we use compactiﬁed conﬁguration spaces? The open manifold Cn(Rk) of n-tuples of
distinct points in Rk contains Cn(γ(M )) and the interior of Z, and we can ask if these submani-
folds intersect. However, intersection theory in open manifolds is difﬁcult. The compactiﬁcation
of conﬁguration spaces of W. Fulton and R. MacPherson [12] as developed by D.P. Sinha [42],
provides the tools to make intersection theory reasonable. We give an overview of this theory in
Section 2.
In Section 3, we look at intersections of submanifolds of conﬁguration spaces and transversality.
Suppose there is a different, well known, smooth embedding of M in Rk (via i : M ↪→ Rk), and
assume that the conﬁguration space Cn[i(M )] is transverse to Z in Cn[Rk]. Also assume that i(M )
is smoothly homotopy equivalent to γ(M ) in Rk. Standard transversality arguments should allow
us to vary Cn[i(M )] to Cn[γ(M )] while maintaining the transversality of the intersection with Z.
This idea is illustrated in Figure 1. The difﬁculties of this argument include:
(1) It is possible that special conﬁgurations on γ(M ) shrink away to the boundary of Cn[Rk]
during the isotopy. We overcome this problem by assuming that the boundaries ∂Z and
∂Cn[γ(M )] are disjoint in ∂Cn[Rk].
(2) In order to apply transversality arguments, we need to be able to perturb Cn[γ(M )] so the
intersection with Z is transverse. However, when we do so, there is no guarantee that the
varied submanifold consists of conﬁgurations on a perturbed smooth embedding of M in
Rk. We deal with this issue by applying the multijet transversality theorem (Theorem 12).
Given these assumptions, our Theorem 17 (roughly) says there there is an open dense set of
(perturbed) smooth embeddings γ′ : M ↪→ Rk, with Cn[γ′(M )] transverse to Z, and for which ∂Z
and ∂Cn[γ′(M )] are disjoint in ∂Cn[Rk].
 3

Cn[Rk]

Z
 Cn[γ(M )]
 Cn[Rk]

Z
 Cn[i(M )]

FIGURE 1. Here, both Cn[γ(M )] and Cn[i(M )] are boundary disjoint with Z
in ∂Cn[Rk]. We can move from Cn[γ(M )] to Cn[i(M )] while preserving the
transversality of the intersection with Z.

In Section 3.1, we then restrict our attention to smooth embeddings of spheres Sl in Rk, and
use Haeﬂiger’s Theorem [19] to deduce the existence of a differentiable isotopy between our em-
beddings γ(Sl) and i(Sl). We combine all of these steps together in Section 3.2 to get our main
tool, Theorem 21, which can be applied to many settings, including the square-peg problem. In
Theorem 21, we assume that
• γ : Sl → Rk is a smooth embedding of Sl in Rk, with a corresponding embedding of
compactiﬁed conﬁguration spaces Cn[γ] : Cn[Sl] → Cn[Rk];
• Z is a closed topological space contained in Cn[Rk] such that Z ∩Cn(Rk) is a submanifold
of Cn(Rk), and ∂Z ⊂ ∂Cn[Rk];
• Cn[γ(Sl)] and Z are boundary-disjoint;
• there is a standard smooth embedding i : Sl ↪→ Rk, such that Cn[i(Sl)] is transverse to Z
in Cn[Rk].
We then deduce that there is, for all m, a Cm-dense set of smooth embeddings γ′ : Sl ↪→ Rk,
such that the corresponding embeddings on conﬁguration spaces are C0-close to Cn[γ], and that
Cn[γ′(Sl)] is transverse to Z, and moreover Cn[i(Sl)] ∩ Z and Cn[γ′(Sl)] ∩ Z represent the same
homology class in Z.
We next apply our method, Theorem 21, to the square-peg problem. In Section 4.1, we start
by reviewing the structure of C4[γ(S1)], the compactiﬁed conﬁguration space of 4 points on a
smooth embedding of a circle in Rk. We choose Rk, rather than R2, as we will prove a more
general version of Toeplitz’s conjecture. Our main result is about the existence of a square-like
quadrilateral inscribed in a smooth embedding of a circle in Rk. In Section 4.2, we deﬁne the space
of square-like quadrilaterals in Rk denoted Slq. These are quadrilaterals abcd with equal sides
(|ab| = |bc| = |cd| = |da|) and equal diagonals (|ac| = |bd|). We then prove that
(1) Slq is a submanifold of C4(Rk) and ∂Slq ⊆ ∂C4[Rk],
(2) the boundaries of Slq and C4[γ(S1)] are disjoint in ∂C4[Rk].

4 JASON CANTARELLA, ELIZABETH DENNE, AND JOHN MCCLEARY

We next consider the number of intersections of Slq with our standard smooth embedding
i : S1 ↪→ Rk of a circle in Rk. We choose this embedding to be the planar ellipse x2/a2 + y2/b2 = 1
with a > b. However, when we count the number of intersections of Slq with C4[i(S1)], we get an
even number of points. Thus, we need to consider intersections counted up to cyclic relabeling. In
Section 4.3 we carefully construct the quotient spaces needed to make this argument. In Section 4.4
we show that our ellipses have a a single inscribed square up to cyclic relabeling, and moreover
our quotient spaces intersect transversally at this intersection. Finally, our arguments culminate in
Theorem 35, where we conclude that there is, for all m, a Cm-dense
1 set of smooth embeddings of
a circle in Rk each of which has an odd number of square-like quadrilaterals.
It is important to realize that while our results provide a uniﬁed and attractive view of this family
of theorems about special inscribed conﬁgurations, they do not directly address the remaining open
territory in Toeplitz’s question. In [8], we give an extension of our results to prove that there exists
at least one square-like quadrilateral inscribed in any embedding of S1 in Rk which is of ﬁnite total
curvature without cusps. (We note that when k = 2, this class of curves is less general than the
family of curves for which W. Stromquist [44] and B. Matschke [28, 30] proved the square-peg
theorem.)
Finally we note that in [7], we provide another example of our main technique (Theorem 21),
where we show that there is a k(k − 1)/2 dimensional family of inscribed (k + 1)-simplices of any
constructible edgelength ratio in certain generic smooth embeddings of Sk−1 in Rk.

2. CONFIGURATION SPACES

The compactiﬁed conﬁguration space of n points in Rk is the natural setting for the square-
peg and other inscribed polygon problems. In this section we give a brief overview of the theory
of compactiﬁed conﬁguration spaces. There are many versions of this classical material (see for
instance [12, 4]). We follow Sinha [42], as this gives a geometric viewpoint appropriate to our
setting. A reader familiar with conﬁguration spaces may skip much of this section. However we
recommend paying attention to the notation we have used for the spaces, points in the spaces and
the strata. Deﬁnition 2, Deﬁnition 3, and Remark 5 are particularly useful.

Deﬁnition 1 ([42]). Given an m-dimensional smooth manifold M , let M ×n denote the n folk
product of copies of M , and deﬁne Cn(M ) to be the subspace of points p = (p1, . . . , pn) ∈ M ×n

such that pj ̸= pk if j ̸= k. Let ι denote the inclusion map of Cn(M ) in M ×n.

The space Cn(M ) is an open submanifold of M ×n. Our goal is to compactify Cn(M ) to a
closed manifold-with-boundary and corners, which we will denote Cn[M ], without changing its
homotopy type. The resulting manifold will be homeomorphic to M ×n with an open neighborhood
of the fat diagonal removed. Recall that the fat diagonal is the subset of M ×n of n-tuples for which
(at least) two entries are equal, that is, where some collection of points comes together at a single
point. The construction of Cn[M ] preserves information about the directions and relative rates of
approach of each group of collapsing points.

1The density is with respect to the Whitney C ∞-topology, described in detail in Section 3.
 5

Deﬁnition 2 ([42],[6]). Given an ordered pair of distinct elements from {1, . . . , n}, let the map

πij : Cn(Rk) → Sk−1 send p = (p1, . . . pn) to pi − pj
|pi − pj| , the unit vector in the direction of

pi − pj. Let [0, ∞] be the one-point compactiﬁcation of [0, ∞). Given an ordered triple (i, j, l) of

distinct elements in {1, . . . , n}, let rijl : Cn(Rk) → [0, ∞] be the map which sends p to |pi − pj|
|pi − pl| ,

the ratio of distances between pi and pj, and pi and pl. Deﬁne sijl : Cn(Rk) → [0, 1] as the
composition ( 2
π arctan) ◦ (rijl).

We then compactify Cn(Rk) as follows:

Deﬁnition 3 ([42]). (1) Let An[Rk] be the product (Rk)n × (Sk−1)n(n−1) × [0, 1]n(n−1)(n−2).
Deﬁne Cn[Rk] to be the closure of the image of Cn(Rk) under the map

αn = ι × (πij) × (sijl) : Cn(Rk) → An[Rk].

(2) We assume that all manifolds M are smoothly embedded in Rk, which allows us to de-
ﬁne the restrictions of the maps πij and sijl. Then Cn(M ) is smoothly embedded in
Cn(Rk) and we deﬁne Cn[M ] to be the closure of Cn(M ) in M n × (Sk−1)n(n−1) ×
[0, 1]n(n−1)(n−2). We denote the boundary of Cn[M ] by ∂Cn[M ] = Cn[M ] \ Cn(M ).

We now summarize some of the important features of this construction, including the fact that
Cn[M ] does not depend on the choice of embedding of M in Rk.

Theorem 4 ([42], [6]). 1. Cn[M ] is a manifold-with-boundary and corners with interior Cn(M )
having the same homotopy type as Cn[M ]. The topological type of Cn[M ] is independent
of the embedding of M in Rk, and Cn[M ] is compact when M is.
2. The inclusion of Cn(M ) in M ×n extends to a surjective map from Cn[M ] to M ×n which
is a homeomorphism over points in Cn(M ).

Remark 5. When discussing points in Cn[Rk] or Cn[M ], it is easy to become confused. We pause
to clarify notation.
• A point in Rk is denoted by x = (x1, . . . , xk), where each xi ∈ R.
• Points in (Rk)n are also denoted by x, where x = (x1, . . . , xn) and each xi ∈ Rk. (It will
be clear from context which is meant.)
• A point in Cn[Rk] or Cn[M ], is denoted −→x .
• At times, we will need to distinguish between the various entries of −→x ∈ Cn[Rk] or Cn[M ].
In general, −→x = (x, (πij)(x), (sijl)(x)) = (x, α(x)),
where x = (x1, . . . , xn) ∈ (Rk)n, and α(x) = ((πij)(x), (sijl)(x)) gives the correspond-
ing set of values in (Sk−1)n(n−1) and [0, 1]n(n−1)(n−2).

The space Cn[M ] may be viewed as a polytope with a combinatorial structure based on the
different ways groups of points in M can come together. This structure deﬁnes a stratiﬁcation of
Cn[M ] into a collection of closed faces of various dimensions whose intersections are members of
the collection. We will use a bit of the structure of this collection, referred to as a stratiﬁcation of
Cn[M ].
 6 JASON CANTARELLA, ELIZABETH DENNE, AND JOHN MCCLEARY

Deﬁnition 6 ([6]). A parenthesization P of a set T is an unordered collection {A1, . . . , Al} of
subsets of T such that #As ≥ 2, and for s ̸= t either As ∩ At = ∅, or As ⊂ At, or At ⊂ As. A
parenthesization is denoted by a nested listing of the As using parentheses. Let Pa(T ) denote the
set of parenthesizations of T , and deﬁne an ordering on it by P ≤ P ′ if P ⊆ P ′.

For example, for T = {1, 2, 3, 4}, (12)(34) represents a parenthesization whose subsets are
{1, 2} and {3, 4} while ((12)34) represents a parenthesization whose subsets are {1, 2} and {1, 2, 3, 4}.
We identify each parenthesization P = {A1, . . . , Al} of {1, . . . , n} with a closed subset SP of
∂Cn[M ] in our stratiﬁcation of Cn[M ]. The idea is that all the points in each As collapse together,
but if As ⊂ At, then the points in As collapse “faster” than the points in At. Formally, this becomes
the following condition: Let −→p = ((p1 . . . , pn), (πij)(p), (sijl)(p)) be a point in An[M ]. Then
−→p ∈ SP if
• pi = pj if and only if i, j ∈ As for some s.
• sijl = 0 (and hence silj = 1) if and only if i, j ∈ As and l /∈ As (see Proposition 3.3,
Deﬁnition 2.10 [42]).
Sinha [42] proves that a stratum SP described by nested subsets {A1, . . . , Al} has codimension l
in Cn[M ]. In the previous example (12) has codimension 1, while ((12)34) and (12)(34) have
codimension 2.
Any pair p, q of disjoint points in Rk has a direction (p − q)/ |p − q| associated to it, while
every triple of disjoint points p, q, r has a corresponding distance ratio |p − q| / |p − r|. One way
to think of the coordinates of Cn[M ] is that they extend the deﬁnition of these directions and ratios
to the boundary.

Theorem 7 ([42], [6]). Given a manifold M ⊂ Rk, then in any conﬁguration of points −→p ∈ Cn[M ]
the following holds.
(1) Each pair of points pi, pj has associated to it a well-deﬁned unit vector in Rk giving the
direction from pi to pj. If the pair of points project to the same point p of M , this vector
lies in TpM .
(2) Each triple of points pi, pj, pk has associated to it a well-deﬁned scalar in [0, ∞] corre-
sponding to the ratio of the distances |pi − pj| and |pi − pk|. If any pair of {pi, pj, pk}
projects to the same point in M (or all three do), this ratio is a limiting ratio of distances.
(3) The functions πij and sijl are continuous on all of Cn[M ] and smooth on each face of
∂Cn[M ].

We notice that the deﬁnition of the SP does not depend on the πij. In fact, for connected
manifolds of dimension at least 2, the combinatorial structure of the strata of Cn[M ] depends only
on the number of points. Regardless of dimension, this construction and division of ∂Cn[M ] into
strata is functorial in the following sense.

Theorem 8 ([42]). Suppose M and N are embedded submanifolds of Rk and f : M ↪→ N is
an embedding. This induces an embedding of manifolds-with-corners called the evaluation map
Cn[f ] : Cn[M ] ↪→ Cn[N ] that respects the stratiﬁcations. This map is deﬁned by choosing the
ambient embedding of M in Rk to be the composition of f with the ambient embedding of N .

For an embedding f : M ↪→ N , the image of the induced embedding Cn[f ] : Cn[M ] ↪→ Cn[N ]
will be denoted by Cn[f (M )].
 7

Corollary 9. Let f : Rk → Rk be a smooth diffeomorphism. Then the induced map of conﬁguration
spaces Cn[f ] : Cn[Rk] → Cn[Rk] is also a smooth diffeomorphism (on each face of Cn[Rk]).

Proof. This is an immediate corollary of the previous theorem. □

3. CONFIGURATION SPACES AND TRANSVERSALITY

In this section, we prove a transversality “lifting property” for compactiﬁed conﬁguration spaces:
The submanifold of conﬁgurations of points on a smoothly embedded submanifold M of Rk may
be made transverse to any submanifold Z of the conﬁguration space of points in Rk by an arbitrarily
small variation of M , as long as the two submanifolds of conﬁguration space are boundary-disjoint.
This is a useful technique and parts of it have been proved before. For instance, R. Budney et al. [6]
prove a special case of this result. We will show that a general form of this result may be obtained
easily from the Multijet Transversality Theorem ([13], Theorem II.4.13).
We begin by recalling some details about the construction of jet space and the Whitney C∞-
topology on mappings. Then we will state the multijet transversality theorem and show that our
desired result on conﬁguration space transversality follows.

Deﬁnition 10. Let M and N be smooth manifolds, and f be a smooth function f : M → N . The
space of 0-jets J 0(M, N ) = M × N . The 0-jet of f is the function j0f : M → J 0(M, N ) given
by j0f (p) = (p, f (p)).

It is a standard fact that jet space J 0(M, N ) is a smooth manifold. Further, 0-jet spaces may
be extended to k-jet spaces by an inductive procedure involving taking successive derivatives. We
won’t need higher jet spaces here; we refer the interested reader to [13] for details.
We can extend the deﬁnition of jet space to a space of n-fold multijets as follows.

Deﬁnition 11. Let the source map σ : J 0(M, N )×n → M ×n be given by

σ((p1, q1), . . . , (pn, qn)) = (p1, . . . , pn).

Deﬁne the space of n-fold 0-multijets J 0
n(M, N ) = σ−1(Cn(M )). Given a smooth function
f : M → N , there is a natural smooth map j0
nf : Cn(M ) → J 0
n(M, N ) given by

j0
nf (p) = (j0f (p1), . . . , j0f (pn)) = ((p1, f (p1)), . . . , (pn, f (pn))).

The space C∞(M, N ) has the Whitney C∞-topology. Recall from [20], for r ﬁnite, the Cr-
topology on C∞(M, N ) has as subbasis sets of the form

N r(f ; (U, φ), (V, ψ), δ).

This denotes the subset of functions g : M → N that are smooth, and for coordinate charts φ : (U ′ ⊂
M ) → (U ⊂ Rm) and ψ : (V ′ ⊂ N ) → (V ⊂ Rk) and K ⊂ U compact with g(φ−1(K)) ⊂ V ′,
then, for all s ≤ r, and all x ∈ K,

∥Ds(ψgφ
−1)(x) − Ds(ψf φ
−1)(x)∥ < δ.

Here, DsF for a function F : (U ⊂ Rm) → (V ⊂ Rk) is the k-tuple of the sth homogeneous
parts of the Taylor series representations of the projections of F . The topology generated by this
subbasis is the Whitney Cr-topology on Cr(M, N ). The subspace C∞(M, N ) has the Whitney
C∞-topology by taking the union of all subbases for all r ≥ 0.

8 JASON CANTARELLA, ELIZABETH DENNE, AND JOHN MCCLEARY

For M compact, in this topology, it is a standard theorem that the subset Emb
∞(M, N ) ⊂
C∞(M, N ) of smooth embeddings of M into N is an open set (see Theorem 2.1.4 of [20]). An-
other important topological result holds for 0-multijets:

Theorem 12 (0-Multijet Transversality Theorem, [13] Theorem II.4.13). Let M and N be
smooth manifolds and let Z be a submanifold of J 0
n(M, N ). Let

TZ = {f ∈ C∞(M, N ) | j0
nf ⋔ Z} .

Then TZ is Cm-dense in C∞(M, N ) for any m. Moreover, if Z is compact, then TZ is C∞-open
in C∞(M, N ).

Before proceeding any further, we recall the deﬁnition of transversality following [17]. Assume
that f : X → Y is a map between manifolds, and Z is a submanifold of Y . Let x ∈ f −1(Z) and
y = f (x). Then f is said to be transversal to Z, denoted f ⋔ Z, provided that Image(Dfx) +
Ty(Z) = Ty(Y ) holds for each x ∈ f −1(Z). Moreover, following [17], we know that if f ⋔ Z,
then f −1(Z) is a submanifold of X.
We note that Theorem 12 is actually a bit stronger than the version we have stated. In fact, it
shows TZ is a residual set, that is, a countable intersection of open dense subsets of C∞(M, N ).
The deﬁnition of compactiﬁed conﬁguration spaces allows us to view Cn[N ] ⊂ (Rk)n ×
(Sk−1)n(n−1) × [0, 1]n(n−1)(n−2) as a metric space with the sup norm. If we deﬁne the map-
ping pri to be the projection onto the ith space of the product, then this naturally leads to a metric
on the set of continuous functions C0(Cn[M ], Cn[N ]).

Deﬁnition 13. With the above assumptions, the metric on the set C0(Cn[M ], Cn[N ]) is given by

∥F − G∥0 = sup
−→p ∈Cn[M ]{∥pri(F (−→p )) − pri(G(−→p ))∥ | for all i}.

Thus, given a maps f, g : M → N and ϵ > 0, we say that the corresponding maps on conﬁguration
spaces Cn[f ], Cn[g] : Cn[M ] → Cn[N ] are ϵ-close provided ∥Cn[f ] − Cn[g]∥0 < ϵ.

In order to prove a useful result for conﬁguration spaces with special submanifolds, we ﬁrst
prove the following lemma:

Lemma 14. For M compact, the mapping Cn[ ] : C∞(M, N ) → C0(Cn[M ], Cn[N ]) is continu-
ous.

Proof. Because M is compact, so is Cn[M ]. As discussed above, we take Cn[N ] with the metric
topology as a subspace of An[Rk]. The metric topology on C0(Cn[M ], Cn[N ]) is the topology of
compact convergence which coincides with the compact-open topology ([34]). This implies that
Cn[ ] : C∞(M, N ) → C0(Cn[M ], Cn[N ]) is continuous if and only if the adjoint ̂Cn[ ] : Cn[M ] ×
C∞(M, N ) → Cn[N ] is continuous. Since Cn[N ] as a subspace of the product (Rk)n×(Sk−1)n(n−1)×
[0, 1]n(n−1)(n−2), then maps into Cn[N ] are continuous if and only if the compositions with pro-
jections onto a factor are continuous. Consider the composition:

Cn[M ] × C∞(M, N ) ̂Cn[ ]
−→ Cn[N ] prj
−→ F ′
j.
 9

On the factors F ′
j = N , the composition is evaluation on the corresponding factor of Cn[M ] and
hence is continuous. When the factor is a sphere, on points pi ̸= pj with f (pi) ̸= f (pj), the map
is simply the composition of a function f with πij and hence is continuous. When points come
together, either in M or in f (M ), the image is in one of the strata of Cn[N ]. In this case, we can
view pi = pj + tu for u a unit vector. Then

f (pj + tu) − f (pj)
∥f (pj + tu) − f (pj)∥ −→
t→0 1
|det Df (pj)| Df (pj)(u).

On C∞(M, N ) this composition is continuous.
Finally, if F ′
j = [0, 1], then the composition is similarly analyzed using sijl instead of πij to
establish continuity. □

Corollary 15. Let M and N be smooth manifolds, and assume M is compact. Given ϵ > 0 and
f : M ↪→ N ⊂ Rk an embedding, there is an open set U ⊂ C∞(M, N ) containing f such that for
g ∈ Emb
∞(M, N ) ∩ U , the maps Cn[f ] and Cn[g] are ϵ-close: ∥Cn[f ] − Cn[g]∥0 < ϵ.

Proof. Let U be the preimage of the open set of functions Cn[M ] ↪→ Cn[N ] within ϵ of Cn[f ]
under Cn[ ]. This is an open subset of C∞(M, N ) containing f by the previous lemma. Since
Emb
∞(M, N ) is open in C∞(M, N ), it meets U in an open set. Choose g in this open set. □

Let us pause to appreciate what we have proven here. Given an embedding f : M ↪→ N , where
M is compact, we can ﬁnd a smooth embedding g : M ↪→ N in a C∞-neighborhood of f , such
that the corresponding maps between conﬁguration spaces Cn[f ] and Cn[g] are as C0-close as we
like. Note that more is probably true, for example that Cn[f ] and Cn[g] are Cm-close for m ≥ 1.
However, we do not need such a result and have not proved it here.
Next, we see that Corollary 15 leads to two very useful results.

Theorem 16 (Transversality Theorem for Conﬁguration Spaces). Let M and N be smooth
manifolds with M compact, and i : M ↪→ N ⊂ Rk a smooth embedding with corresponding
embedding of conﬁguration spaces Cn(i) : Cn(M ) ↪→ Cn(N ). Assume Z is a submanifold of
Cn(N ). Given an ϵ > 0, there is a C∞-open neighborhood U of i, in which there is, for all m, a
Cm-dense set of smooth embeddings i′ : M ↪→ N , with ∥Cn[i′] − Cn[i]∥0 < ϵ, and Cn(i′) ⋔ Z.

Proof. We embed Z in Cn(M × N ) as W = sh(Cn(M ) × Z), where the shufﬂe map is deﬁned by
sh((p1, . . . , pn), (v1, . . . , vn)) = ((p1, v1), (p1, v1), . . . , (pn, vn)). This map is a diffeomorphism.
Using Theorem 12, we know that the set TW = {f ∈ C∞(M, N ) | j0
nf ⋔ W } is Cm-dense in
C∞(M, N ) for all m.
The preimage of the ϵ-ball around Cn(i) is an open set U in C∞(M, N ) containing i. Since
Emb
∞(M, N ) is open, so is U ∩ Emb
∞(M, N ), and this open set meets the set TW . Choose i′

in the intersection TW ∩ U ∩ Emb
∞(M, N ). By Theorem 12, j0
ni′ ⋔ W , and the set of such i′

remains Cm-dense in C∞(M, N ) for all m.
We want to show that this implies Cn(i′) ⋔ Z. By deﬁnition, j0
ni′ transverse to W means that
for all p with j0
ni′(p) ∈ j0
n(i′)(M ) ∩ W ,

Tj0
ni′(p)Cn(M × N ) ∼= Tj0
ni′(p)W ⊕ Dj0
ni
′(TpCn(M )).

10 JASON CANTARELLA, ELIZABETH DENNE, AND JOHN MCCLEARY

Since W ∼= Cn(M ) × Z, then Tj0
ni′(p)W ∼= TpCn(M ) ⊕ TCn(i′)(p)Z. The key step here is to use
the shufﬂe map to rewrite the decomposition. Since,

j0
ni
′(p)=((p1, i
′p1), . . . , (pn, i
′pn)) sh−1
−−−→ ((p1, . . . , pn), (i′p1, . . . , i′pn)) ∈ Cn(M ) × Cn(N ).

then Dj0
ni
′(TpCn(M )) ∼= TpCn(M ) ⊕ Di
′(TpCn(M )).
The shufﬂe maps also allows us to identify

Tj0
ni′(p)Cn(M × N ) ∼= TpCn(M ) ⊕ TCn(i′)(p)Cn(N ).

Putting all the maps together, we deduce

TCn(i′)(p)Cn(N ) ∼= TCn(i′)(p)Z ⊕ Di
′(TpCn(M )).

In other words, Cn(i′) ⋔ Z. □

Theorem 17 (Transversality Theorem for Compactiﬁed Conﬁguration Spaces). Let M and
N be smooth manifolds, with M compact, and i : M ↪→ N ⊂ Rk a smooth embedding with a
corresponding embedding of compactiﬁed conﬁguration spaces Cn[i] : Cn[M ] ↪→ Cn[N ]. Assume
Z is a closed topological space contained in Cn[N ], such that Z ∩ Cn(N ) is a submanifold of
Cn(N ), and ∂Z ⊂ ∂Cn[N ]. Also assume that ∂Z is disjoint from ∂Cn[i(M )].
Then for any ϵ > 0, there is a C∞-open neighborhood of i, in which there is, for all m, a Cm-
dense set of smooth embeddings i′ : M ↪→ N , with ∥Cn[i′] − Cn[i]∥0 < ϵ, and Cn[i′] ⋔ Z, and for
which ∂Z and ∂Cn[i′(M )] are disjoint in ∂Cn[N ].

Proof. Recall that M and N are embedded in Rk for k large. Since M is compact, the closed set
Cn[i(M )] ∩ Z is also compact. By assumption, Cn[i(M )] ∩ Z is also disjoint from the closed set
∂Cn[N ], thus it is separated from it by some ϵ > 0. Take the intersection of Z with the complement
of an ϵ/2 neighborhood of ∂Cn[N ], and denote this ˆZ. The set ˆZ is an open manifold contained in
Cn(N ), which remains a bounded distance from ∂Cn[N ].
We apply Theorem 16 to this setting, so there is an embedding i′ : M ↪→ N with Cn[i′] : Cn(M ) ↪→
Cn(N ) transverse to ˆZ, which by Corollary 15, we can choose so that Cn[i′(M )] is ϵ/2-close to
Cn[i(M )]. We can thus choose the perturbation i′ so that Cn[i′(M )] ∩ ˆZ is at least (3/4)ϵ away
from ∂Cn[N ]. Thus Cn[i′] ⋔ ˆZ implies Cn[i′(M )] ⋔ ˆZ which in turn implies Cn[i′(M )] ⋔ Z. □

There are many possible applications of Theorem 17. The ﬁrst one we give is to the square-peg
problem in this paper, another is to (k + 1)-simplices inscribed in smoothly embedded (k − 1)-
spheres found in [7]. Thus, we let M = Sl be an l-sphere embedded in N = Rk, and Z is a
submanifold of Cn[Rk] satisfying special conditions. For our work Cn[i(Sl)] ∩ Z will usually
represent certain inscribed conﬁgurations of points in Sl. In this setting Theorem 17 becomes the
following.

Corollary 18. Suppose there is a smooth embedding i : Sl ↪→ Rk of an l-sphere in Rk, with a
corresponding embedding of compactiﬁed conﬁguration spaces Cn[i] : Cn[Sl] ↪→ Cn[Rk]. Assume
that Z is a closed topological space contained in Cn[Rk] such that Z ∩ Cn(Rk) is a submanifold
of Cn(Rk), and ∂Z ⊂ ∂Cn[Rk]. Also assume that ∂Z is disjoint from ∂Cn[i(Sl)].
 11

Then for any ϵ > 0, there is a C∞-open neighborhood of i, in which there is, for all m, a Cm-
dense set of smooth embeddings i′ : Sl ↪→ Rk, with ∥Cn[i′] − Cn[i]∥0 < ϵ, and Cn[i′] ⋔ Z, and for
which ∂Z and ∂Cn[i′(Sl)] are disjoint in ∂Cn[Rk].

3.1. Deformations. In this subsection, we restrict our attention to Sl, an l-sphere embedded in
Rk. We want to be able to deform standard spheres into spheres of interest, and then consider what
happens on the level of conﬁguration spaces. We know such a deformation of spheres exists due to
a result of A. Haeﬂiger, which we have stated in a form useful to us (actually, his result is stronger).

Theorem 19. [19] Any two differentiable embeddings of Sl in Rk are homotopic through a differ-
entiable isotopy in RK ⊃ Rk when K > 3(l + 1)/2.

Generally such an isotopy must pass through spheres embedded in a higher-dimensional space,
as when the spheres are knotted. The classical case of knots in R3 requires embedding a knot
in R4 for unknotting. Since differentiable knotting is stronger than topological knotting and we
prefer to work in the differentiable category, we need even more extra room to work.2 In this case,
simply use the usual embeddings Rk ↪→ Rk+1 ↪→ · · · ↪→ RK to achieve K > 3(l + 1)/2. and
Rk ⊕ ⃗0 ↪→ RK.
There are some useful generalizations of the theorem of Haeﬂiger that may be applied to obtain
isotopies between embeddings. The foundational example, the Whitney-Wu Unknotting Theo-
rem [43, 51, 52], states that if N is a compact, connected n-manifold with n ≥ 2 and m ≥ 2n + 1
then any two embeddings of N into Rm are isotopic. In the cases of interest in this paper, N = Sl

provides a geometrically satisfying setting for the kinds of special inscribed conﬁgurations we
study. It is possible to extend our methods to other manifolds embedded in Euclidean space for
which the existence of special inscribed conﬁgurations may be more difﬁcult and the initial condi-
tions for our techniques harder to ﬁnd. We leave this to the reader, as the robustness of transversality
arguments cannot be underestimated.
Suppose Z is a subspace of Cn[Rk], typically deﬁned by geometric conditions. We want to
understand what happens to the intersection of Z with the conﬁguration spaces of the (isotopic)
embedded spheres. It turns out that the homology classes are preserved.

Theorem 20. Suppose there are two embeddings η, i : Sl ↪→ Rk of an l-sphere in Rk. Assume
that Z is a closed topological space contained in Cn[Rk] such that Z ∩ Cn(Rk) is a submanifold
of Cn(Rk), ∂Z ⊂ ∂Cn[Rk], and ∂Z is disjoint from ∂Cn[i(Sl)]. Also assume that both Cn[i] and
Cn[η] are transverse to Z. Then in Z, the homology class of Cn[i(Sl)] ∩ Z and Cn[η(Sl)] ∩ Z are
equal.

Proof. By Haeﬂiger’s Theorem η is homotopic to i because they are in the same path component of
Emb(Sl, Rk), as long as k > 3(l + 1)/2. By functorality, this gives a homotopy H : Cn(Sl) × I →
Cn(Rk), and H(−, 0) and H(−, 1) are both transverse to Z.
After applying the Transversality Homotopy Extension theorem (see for instance [17]), we get
a map homotopic to H: H ′ : Cn(Sl) × I → Cn(Rk),
with H ′(−, 0) = H(−, 0), H ′(−, 1) = H(−, 1), and H ′ is transverse to Z.

2As before.

12 JASON CANTARELLA, ELIZABETH DENNE, AND JOHN MCCLEARY

We conclude by transversality that the mod 2 intersection numbers are equal. In addition, we
conclude that in Z the homology class of Cn[i] ∩ Z and Cn[η] ∩ Z are equal.
Haeﬂiger’s theorem requires k > 3(l + 1)/2. As noted before, if this is not the case, use the
usual embedding Rk ↪→ RK, to achieve K > 3(l + 1)/2. Then H ′ : Cn(Sl) × I → Cn(RK) still
agrees with H on H(−, 0) and H(−, 1) in the version Rk ⊕ −→
0 ↪→ RK. Since transversality does
not change the intersection number mod 2, nor the homology class, the conclusions stand. □

3.2. Application to conﬁguration spaces. In the rest of the paper, we apply the results of this
section to the square-peg problem using the following steps. These steps can also be used to
solve other problems such as ﬁnding inscribed simplices in spheres as found in [7]. We have thus
specialized the arguments from the previous section to the case where M is a sphere Sl, and show
any smooth embedding γ of Sl in Rk has a neighborhood in which there is a dense set of smooth
embeddings γ′ for which Cn[γ′] is guaranteed to have certain intersections with various “target”
submanifolds of Cn[Rk] deﬁned by geometric conditions. This restates the idea that a dense set of
embeddings of Sl always contain certain inscribed conﬁgurations of points.
Step 0: For any smooth embedding γ : Sl ↪→ Rk, view Cn[γ(Sl)] as a submanifold of
Cn[Rk].
Step 1: Show that certain tuples of points in Rk satisfying a geometric condition, Z, are
a submanifold in Cn(Rk), and with ∂Z ⊂ ∂Cn[Rk]. Prove that Cn[γ(Sl)] and Z are
boundary-disjoint.
Step 2: For a standard embedding i : Sl ↪→ Rk, establish the existence of a transverse inter-
section between Cn[i(Sl)] and Z inside Cn[Rk] (in other words, Cn[i] ⋔ Z). Compute the
homology class of the intersection Cn[i(Sl)] ∩ Z in Z.
Step 3: Use our transversality theorem (Corollary 18) to ﬁnd, for any ϵ > 0, a C∞-open
neighborhood of γ in which there is, for all m, a Cm-dense set of smooth embeddings
γ′ : Sl ↪→ Rk, such that ∥Cn[γ′] − Cn[γ]∥0 < ϵ, and Cn[γ′] ⋔ Z, and for which ∂Z and
∂Cn[γ′(Sl)] are disjoint in ∂Cn[Rk].
Step 4: Use Haeﬂiger’s theorem (Theorem 19) to ﬁnd a smooth map E : Sl × I → RK with
E(−, 0) = i our standard embedding and E(−, 1) = γ′ (where K may be greater than
our original k). Following Theorem 20, conclude that the intersections Cn[i(Sl)] ∩ Z and
Cn[γ′(Sl)] ∩ Z represent the same homology class in Z.
By putting all these steps together, we prove the following theorem:

Theorem 21. Suppose γ : Sl → Rk is a smooth embedding of Sl in Rk, with a corresponding
embedding of compactiﬁed conﬁguration spaces Cn[γ] : Cn[Sl] → Cn[Rk]. Assume that Z is a
closed topological space contained in Cn[Rk] such that Z ∩ Cn(Rk) is a submanifold of Cn(Rk),
and ∂Z ⊂ ∂Cn[Rk]. Also assume that Cn[γ(Sl)] and Z are boundary-disjoint. Suppose there is a
standard embedding i : Sl ↪→ Rk, such that Cn[i] ⋔ Z in Cn[Rk].
Then for all ϵ > 0, there is a C∞-open neighborhood of γ, in which there is, for all m, a Cm-
dense set of smooth embeddings γ′ : Sl ↪→ Rk, such that ∥Cn[γ′] − Cn[γ]∥0 < ϵ, and Cn[γ′] ⋔ Z,
and moreover, Cn[i(Sl)] ∩ Z and Cn[γ′(Sl)] ∩ Z represent the same homology class in Z.

As a simple example of this, if the standard embedding Cn[i(Sl)] has nonzero intersection with
Z, then we know that Cn[γ′(Sl)] has nonzero intersection with Z as well.
 13

Before moving on to the square-peg problem, we note that the steps outlined above work for
the more general setting of smooth embeddings of manifolds M in N ⊂ Rk where M is compact.
There are many kinds of problems that could be solved using this technology.

4. THE SQUARE-PEG PROBLEM

In this section we will apply the method given in Section 3.2 to prove a version of the square-
peg theorem. Most of our effort will be put into the initial steps where we deﬁne the spaces
involved. To do this we ﬁrst give a detailed description of two submanifolds of Cn[Rk]. For the
ﬁrst, we take an embedding γ : S1 ↪→ Rk, and consider C0
4 [γ(S1)] which is the submanifold of
4-tuples on a curve γ where the points occur in order according to the orientation of the curve. The
second is the submanifold Slq ⊂ C4[Rk], which is the submanifold of conﬁgurations of square-like
quadrilaterals. These are 4-tuples of points with equal “sides” and equal “diagonals” (explained in
Section 4.2 below). When k = 2, these are squares, hence our setting generalizes the square-peg
problem. A moment’s thought shows that there is a square-like quadrilateral inscribed in γ when
Slq and C0
4 [γ(S1)] intersect. In fact, we will show that when this intersection is transverse, the
number of intersections is an odd multiple of 4; thus giving an odd number of inscribed squares-
like-quadrilaterals up to cyclic relabeling.

4.1. The conﬁguration space of points on a curve. We now use the results from Section 2 to
familiarize ourselves with the conﬁguration space of n points on an embedded circle in Rk. We
will always assume that our embeddings are regular, that is the tangent vector is nowhere zero.
(Otherwise it is possible to smoothly describe an embedded curve with corners, by allowing the
tangent vector to smoothly change to zero at each corner.)

Deﬁnition 22. Let γ be a C∞-smooth embedding of S1 in Rk, with Cn[γ] : Cn[S1] ↪→ Cn[Rk]
the corresponding embedding on compactiﬁed conﬁguration spaces. We abuse notation by using γ
to mean either the embedding or its image in Rk. We use Cn[γ(S1)] to mean the compactiﬁed
conﬁguration space of n points on the simple closed curve γ(S1) ∈ Rk.

By Theorem 8 we know that Cn[γ(S1)] is a submanifold of Cn[Rk] and ∂Cn[γ(S1)] ⊆ ∂Cn[Rk]
with the stratiﬁcations respected. The coordinates for Cn[γ(S1)] are similar to those described in
Theorem 7, as they are the image of the coordinates under γ : S1 ↪→ Rk. I. Voli´c [49] and Budney et
al. [6] have detailed descriptions of the coordinates for codimension 1 strata. To give an example,
observe that the map Cn[γ] takes (p1, . . . , pn) ∈ Cn(S1) to (γ(p1), . . . , γ(pn)) ∈ Cn(Rk). If
we consider the stratum where say p1, p2 and p3 degenerate to a point −→q in Cn[S1], then −→q is
a conﬁguration of n − 3 + 1 = n − 2 points plus the πij and sijl information for p1, p2 and
p3. In Cn[Rk] we get a conﬁguration of n − 2 points on γ plus the directions of approach of the
colliding γ(pi) and the relative distances s123, s312, and so forth. The πij are unit tangent vectors to
γ. If p1 and p3 approach p2 equally from opposite sides, then in the limit |p1 − p2| + |p2 − p3| =
|p1 − p3|, so the sijk obey the relations

1 + s231 = s132, s213 + 1 = s312, s123 + s321 = 1.

14 JASON CANTARELLA, ELIZABETH DENNE, AND JOHN MCCLEARY

In Cn[S1] the values of πij are in S1 and are mapped to S1 by Cn[γ]. Thus, while the exact
values of the unit tangent vectors πij and πji are unknown for two colliding points on γ, they must
differ by π.
In the case of the circle, the cyclic ordering of points along S1 determines (n − 1)! connected
components of Cn[S1]. We will focus on one of these connected components.

Deﬁnition 23. Let C0
n[γ(S1)] denote the component of Cn[γ(S1)] where the order of the points
p1, . . . , pn matches the cyclic order of these points along γ according to the given parametrization
of γ.

Note that some strata are empty in the boundary of each connected component of Cn[S1] (and
hence Cn[γ(S1)]). For instance, in the component of C4[S1] where points p1, p2, p3 and p4 occur
in order along S1, if p1 and p3 come together, either p2 or p4 must collapse to the same point.
Thus the stratum (13) is empty on the boundary of this component.

4.2. The conﬁguration space of square-like quadrilaterals. In this section we show that Slq
(conﬁgurations of square-like quadrilaterals) is a submanifold of C4(Rk). Thus Slq plays the role
of “Z” in Section 3.2. We also show that the boundaries of Slq and C0
4 [γ(S1)] are disjoint in
C4[Rk].

Deﬁnition 24. We deﬁne Slq to be the subset of square-like quadrilaterals of C4[Rk] such that
r124 = r231 = r342 = 1 and r132 − r241 = 0.

In other words, if −→p = ((p1, p2, p3, p4), α(−→p )) ∈ Slq, then the ﬁrst condition implies
|p1 − p2| = |p2 − p3| = |p3 − p4| = |p4 − p1|, and the second condition implies |p1 − p3| =
|p2 − p4|. Thus when k > 2, Slq is the space of quadrilaterals in Rk with equal sides and equal
diagonals. When k = 2, Slq is the space of squares in R2. Note that we work with rijl here as we
are considering the actual ratios of lengths, rather than the rescaled ratios sijl (see Deﬁnition 2).

Proposition 25. The space Slq ∩ C4(Rk) is an orientable submanifold of C4(Rk).

Proof. Let −→p = ((p1, p2, p3, p4), α(−→p )) be a point in C4[Rk], and consider the mapping g : C4[Rk] →
R4 given by

g(−→p ) = (r2
124, r2
231, r2
342, r2
132 − r2
241)(1)
 =
 ( |p1 − p2|2

|p1 − p4|
2 , |p2 − p3|2

|p1 − p2|2 , |p3 − p4|2

|p2 − p3|2 , |p1 − p3|
2

|p1 − p2|
2 − |p2 − p4|2

|p2 − p1|2
 )
 .(2)

This mapping is smooth and Slq is the preimage of the point (1, 1, 1, 0). In this proof, we show
that Dg : T−→p C4(Rk) → Tg(−→p )R
4

is onto at points −→p ∈ Slq by showing Dg has four linearly independent rows. It then follows
from the Preimage Theorem of [17] that g ⋔ (1, 1, 1, 0) and the interior of Slq is an orientable
submanifold of C4(Rk).
In order to do this, we create a basis of tangent vectors to C4(Rk) that allows Dg to be computed
easily. There are two cases; when −→p ∈ Slq is planar and when it is not. Note that we will use

15

these bases in later proofs, so we give full details here. We denote a tangent vector at −→p by
−→
h = h(−→p ) = (v1, v2, v3, v4), where each vi is a tangent vector at pi. (Here we suppress the
α(p) information on the strata.)
For each of the two cases, we need to know the image of Dg with respect to vectors −→
h . We
compute the derivative of each of the four equations of g with respect to a vector −→
h . The details
for the computation for D−→
h (r2
124) is found below, where we have simpliﬁed using |p1 − p2| =
|p2 − p3| = |p3 − p4| = |p4 − p1| and |p1 − p3| = |p2 − p4|. Thus the ﬁrst row of Dg contains

D−→
h (r2
124) = D−→
h
 ( |p1 − p2|
2

|p1 − p4|
2
 )

= |p1 − p4|
2 2 |p1 − p2| D−→
h (|p1 − p2|) − |p1 − p2|2 2 |p1 − p4| D−→
h (|p1 − p4|)

|p1 − p4|
4

= 2
|p1 − p4|
 (D−→
h (|p1 − p2|) − D−→
h (|p1 − p4|)) .

Using similar reasoning, we compute the column of Dg corresponding to a vector −→
h to be

(3)
 








 2
|p1−p4| (D−→
h (|p1 − p2|) − D−→
h (|p1 − p4|))

2
|p2−p1| (D−→
h (|p2 − p3|) − D−→
h (|p2 − p1|))

2
|p3−p2| (D−→
h (|p3 − p4|) − D−→
h (|p3 − p2|))

2
|p1−p2|2 (|p1 − p3| D−→
h (|p1 − p3|) − |p2 − p4| D−→
h (|p2 − p4|)
)










Case 1: We ﬁrst assume the conﬁguration −→p ∈ Slq is planar, then p1p2p3p4 are the four
vertices of a square. This means the points are inscribed in an ellipse, and without loss of generality,
we choose an ellipse with equation x2/a2 + y2/b2 = 1 and a > b. (Note that for any choice of ratio
a : b there will be a square for precisely one pair of numbers satisfying that ratio. These numbers
are determined by the sidelength of the square.) If we parametrize the ellipse by (x(θ), y(θ)) =
(a cos θ, b sin θ), then we can show that cos2 θ = b2/(a2 + b2) and sin
2 θ = a2/(a2 + b2).
For our ﬁrst tangent vector to C4(Rk), we consider the effect of moving p1 along the ellipse as
shown in Figure 2. For some θ1, this point has coordinates (a cos θ1, b sin θ1) = (ab/
√a2+b2, ab/
√a2+b2).
Our ﬁrst vector is the tangent vector to the ellipse −→
h 1 = (v1, 0, 0, 0), where v1 = (−a2/
√a2+b2, b2/
√a2+b2).
Using symmetry we see the square has sidelength 2ab/
√a2+b2 and for this vector D−→
h 1(|p1 − p2|) =
−a2/a2+b2, D−→
h 1(|p1 − p4|) = b2/a2+b2 and D−→
h 1(|p1 − p3|) = −a2+b2/
√2(a2+b2) . Substituting
these values in the ﬁrst row of Equation 3, we ﬁnd

D−→
h 1(r2
124) =
 √a2 + b2

ab
 (
− a2

a2 + b2 − b2

a2 + b2
 ) = − a
b − b
a .

16 JASON CANTARELLA, ELIZABETH DENNE, AND JOHN MCCLEARY

p1p2

p3 p4

v1

FIGURE 2. This ﬁgure shows the effect of moving only p1 = (a cos θ1, b sin θ1)
along the ellipse on the sides of the quadrilateral. This motion increases |p4 − p1|
while decreasing |p1 − p2|.

We then construct vectors −→
h 2, −→
h 3 and −→
h 4 at the remaining pi in an analogous fashion. (We
note these vectors are linearly independent, since each of them only acts at one vertex of the square.)
Using Mathematica we compute Dg restricted to Span{
−→
h 1, −→
h 2, −→
h 3, −→
h 4} to be the matrix






− a
b − b
a a
b 0 b
a
a
b − a
b − b
a b
a 0
0 b
a − a
b − b
a a
b
− a
b + b
a − a
b + b
a − a
b + b
a − a
b + b
a
 



 .

This matrix has determinant 8(a4 − b4)
a2b2 which is positive, since we assumed a > b. This also
rechecks our previous observation that Dg has four linearly independent rows.
Case 2: We next make a similar construction for nonplanar conﬁgurations in Slq. Assume the
square-like quadrilateral −→p ∈ Slq has sides of length ℓ = |p1 − p2| = |p3 − p2| = |p4 − p3| =
|p1 − p4|, and diagonals have length m = |p1 − p3| = |p2 − p4|.
Figure 3 shows the construction of two types of tangent vectors to C4(Rk) at −→p . The ﬁrst three
tangent vectors are of the form −→
h 1 = (v1, 0, 0, 0), −→
h 2 = (0, 0, v3, 0) and −→
h 3 = (0, 0, 0, v4).
Vector −→
h 2 is shown on the left of Figure 3, and observe that v3 is the vector at p3 perpendicular
to the plane through p1p3p4. This means the directional derivatives of |p3 − p4| and |p3 − p1| in
the direction −→
h 2 are zero (to ﬁrst order). On the other hand, since the quadrilateral is nonplanar,
edge p2p3 is not in the plane normal to v3, so the directional derivative of |p2 − p3| is nonzero.
We deﬁne vectors −→
h 1 and −→
h 3 in a similar way. Vector v1 is perpendicular to the p1p2p3
plane at p1, and vector v4 is perpendicular to the p1p2p4 plane at p4. To summarize, we choose
v1, v3, v4 to be scaled so that

D−→
h 1 |p1 − p4| = −ℓ/2, other directional deriv.’s of lengths = 0,

D−→
h 2 |p2 − p3| = ℓ/2, other directional deriv.’s of lengths = 0,

D−→
h 3 |p3 − p4| = ℓ/2, other directional deriv.’s of lengths = 0.
 17
p4
 p1

p2

p3 v3
 p4
 p1

p2

p3w

FIGURE 3. Two tangent vectors to a conﬁguration −→p ∈ Slq which forms a non-
planar quadrilateral. On the left, we see the tangent vector where the directional
derivative of |p2 − p3| is positive, while the directional derivatives of all other
lengths vanish. A similar tangent vector may be constructed at vertices p1 and
p4. On the right, we see the tangent vector where the directional derivative of
|p1 − p3| is positive while the directional derivatives of all other lengths vanish.

The fourth tangent vector −→
h 4 = (0, 0, w, 0) is shown at the right of Figure 3. Vector w is perpen-
dicular to the plane through p2p3p4 at p3. We can choose w to be scaled so that

D−→
h 4 |p1 − p3| = ℓ2/2m, other directional deriv.’s of lengths = 0.

Substituting these values in Equation 3, we see that various factors of ℓ and m cancel, and Dg
restricted to Span{
−→
h 1, −→
h 2, −→
h 3, −→
h 4} is the matrix:

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
 .

This matrix has determinant 1, and again we see that Dg has four linearly independent rows.
In both cases (Slq planar and non-planar), we have shown that Dg has four linearly indepen-
dent rows and is onto. This means that g ⋔ (1, 1, 1, 0), and the interior of Slq is an orientable
submanifold of C4(Rk). □

We now discuss the behavior of the boundaries of Slq and C0
4 [γ(S1)]. Recall that, a point lies in
∂C4[Rk] when points of a conﬁguration come together, along with the directions of collision and
ratios of the sides.

Lemma 26. The spaces Slq and C0
4 [γ(S1)] are boundary-disjoint in C4[Rk].

Proof. The boundary of Slq can occur in two ways: when both the sidelengths and diagonals
vanish giving an “inﬁnitesimal” square-like quadrilateral, and when the diagonals vanish, but the
sidelengths remain equal and nonzero. That is, ∂Slq lies in the boundary faces (1234) and (13)(24)
respectively of ∂C4[Rk]. We observe that when k = 2, Slq has two connected components: one
is the interior of Slq and the (1234) boundary face, the other is the (13)(24) boundary face. (The

18 JASON CANTARELLA, ELIZABETH DENNE, AND JOHN MCCLEARY

latter is disjoint from the interior of Slq: in the plane, there is no way for the diagonals to vanish
without the sidelengths vanishing too.) When k > 2, Slq is connected.
As we observed in at the end of Section 4.1, C0
4 [γ(S1)] does not contact the (13)(24) or
((13)(24)) faces of C4[Rk]. Thus we need only consider the portion of Slq and C0
4 [γ(S1)] on
the interior of the (1234) face. For Slq, these conﬁgurations are inﬁnitesimal tetrahedra with equal
sides and equal diagonals. Thus each conﬁguration p1p2p3p4 contains four congruent triangles,
each of which has one diagonal and two edges. This means the four internal angles ∠pi−1pipi+1
(mod 4) are all equal. (The remaining eight angles in the four triangles are also equal to one an-
other.) For C0
4 [γ(S1)], since γ is smooth, these conﬁgurations are an inﬁnitesimal collinear quadri-
lateral with internal angles of either 0 or π. Thus the πij and sijk data are completely different for
∂Slq and ∂C0
4 [γ(S1)], and the spaces are are boundary disjoint. □

In Appendix A, we give further details about the structure of the faces of ∂Slq. There, in Propo-
sition 37, we show that each of the boundary (1234) and (13)(24) faces of Slq is a submanifold
of C4[Rk]. The proofs of these results are similar in ﬂavor to the proof of Proposition 25, so are
omitted here. Note that we will refer to Proposition 37 later in the proof of Proposition 31.

4.3. Cyclic actions. The next step on our method is to consider a base case. For us this will
be the ellipse. Step 1 of our method requires us to compute the homology class in H0(Slq, Z)
of the intersection of C0
4 [γ(S1)] and Slq for a transverse intersection. Unfortunately for us,
while Slq ∩ C0
4 [γ(S1)] is indeed 0-dimensional, the intersection represents 0 in the homology
H0(Slq; Z) = Z. The essential problem is that a square-like quadrilateral can be cyclically re-
labeled in four ways, and it turns out that these relabelings alternate signs in H0(Slq; Z). In-
deed H.B. Grifﬁths [16] took a similar approach, though he seems to have failed to appreciate the
orientation-reversing nature of the cyclic permutation on C4[Rk]. As a result, he (wrongly) com-
putes a different intersection number to be 16 instead of zero. Fortunately, we can ﬁx the problem
by identifying these relabelings as a single conﬁguration.

Deﬁnition 27. Let µ : C4[Rk] → C4[Rk] be the map corresponding to the generator of Z/4Z for
the action on C4[Rk] that cyclically permutes p1, p2, p3 and p4, namely

µ(p1, p2, p3, p4) = (p2, p3, p4, p1).

It is clear from the deﬁnition of Slq that µ descends to a map from Slq to Slq.

This action is free
3. To see this, simply repeat the arguments Sinha uses for the symmetric group
(cf. Theorem 4.10 of [42]).

Lemma 28. The map µ reverses orientation on C4[Rk] if k is odd, and preserves orientation if k
is even.

Proof. Observe that the tangent space to C4[Rk] contains of four copies of T Rk and that reordering
these from (1, 2, 3, 4) to (2, 3, 4, 1) requires 3k2 swaps of basis elements. Thus µ is orientation
reversing or preserving on C4[Rk] as k is odd or even. □

3The action is also automatically properly discontinuous as the group is ﬁnite.
 19

In order to understand how the action µ affects the orientation on Slq = g−1(1, 1, 1, 0), note
that Slq carries the preimage orientation. We now review the deﬁnition of the preimage orientation
from [17]. Assume f : X → Y is transverse to Z ⊂ Y , let f (x) = z ∈ Z, and suppose Hx is
a subspace of TxX complementary to the the subspace Tx(f −1(Z)). Then the orientation of Z
and Y induce a direct image orientation on DfxHx. Since Tx(f −1(Z)) contains the entire kernel
of Dfx, then Dfx maps Hx isomorphically onto its image. The induced orientation on DfxHx
deﬁnes an orientation on Hx via the map Dfx. In summary, the two direct sums

DfxHx ⊕ Tz(Z) = Tz(Y ),

Hx ⊕ Tx(f −1(Z)) = Tx(X)

deﬁne the orientation on Hx and on Tx(f −1(Z)).

Proposition 29. The map µ reverses orientation on Slq ∩ C4(Rk) if k is odd, and preserves ori-
entation if k is even.

Proof. Since Slq = g−1(1, 1, 1, 0), where g is given by Equation 1, then T−→p (Slq) ⊂ T−→p (C4[Rk]).

Recall from the proof of Proposition 25, that a tangent vector at −→p is denoted by −→
h = h(−→p ) =
(v1, v2, v3, v4), where vi is a tangent vector at pi and the α(−→p ) information has been sup-
pressed. In the following argument, we will need the two direct sums from the deﬁnition of
preimage orientation translated to our setting. Assuming that g(−→p ) = (1, 1, 1, 0) and noting that
T(1,1,1,0)(1, 1, 1, 0) = {0}, then we obtain

Dg−→p H−→p ⊕ {0} = T(1,1,1,0)(R4),(4)
 H−→p ⊕ T−→p (Slq) = T−→p (C4[Rk]).(5)

To prove the proposition, use the variations of quadrilaterals in Slq seen in the proof of Proposi-
tion 25. These turn out to behave nicely under the Z/4Z action! There are two cases, depending on
whether the point −→p ∈ Slq is a planar square, or is a nonplanar quadrilateral. In both cases we de-
ﬁne H−→p = Span{
−→
h 1, −→
h 2, −→
h 3, −→
h 4} where the −→
h i’s were deﬁned in the proof of Proposition 25.
In each case, we proved the vectors are linearly independent, thus give a basis BH for H−→p , which
is the subspace of T−→p (C4[Rk]) complementary to T−→p (Slq).
In the proof of Proposition 25, we saw that for both cases Dg has positive determinant so is an
orientation preserving isomorphism onto its image. Since R4 and T(1,1,1,0)(R4) have the standard
orientation, we deduce that our bases BH for H are positively oriented using Equation 4. Note that
C4[Rk] inherits a positive orientation from picking a consistent positive orientation on each Rk.
Using Equation 5, we can deﬁne a basis BS of T−→p (Slq) which gives a positive orientation. This
orientation is the preimage orientation of T−→p (Slq).
The map µ : C4[Rk] → C4[Rk] is a diffeomorphism, so is an isomorphism on each tangent
space. We can check whether this isomorphism is orientation preserving or reversing on Slq by
another computation. Now, µ restricts to a map µ : Slq → Slq, and hence Dµ−→p : T−→p Slq →
Tµ(−→p )Slq. Applying Dµ−→p to each side of Equation 5 gives

(6) Dµ−→p (H−→p ) ⊕ Dµ−→p (T−→p (Slq)) ∼= Dµ−→p (T−→p (C4[R
k])) ∼= Tµ(−→p )(C4[Rk]).

20 JASON CANTARELLA, ELIZABETH DENNE, AND JOHN MCCLEARY

Lemma 28 showed that the last isomorphism is orientation preserving if k is even, and ori-
entation reversing if k is odd. We computed above that BH is a positively oriented basis of the
complementary space H−→p . We need to know if these vectors push-forward to a positively oriented
basis for the subspace Dµ−→p (H−→p ). To do this, observe that Equations 4 and 5 hold for any com-
plementary subspace of T−→p (Slq) and any point −→p ∈ Slq, in particular for Dµ−→p (H−→p ) and µ(−→p ).
Thus
 Dg(Dµ−→p (H−→p )) ⊕ {0} = T(1,1,1,0)(R4),(7)
 Dµ−→p (H−→p ) ⊕ Tµ(−→p )Slq = Tµ(−→p )(C4[Rk]).(8)

We thus check what happens to BH under Dg. As before, there are two cases, depending on
whether −→p ∈ Slq is planar or non-planar. We will see below that in both cases det Dg > 0,
and so Dg is orientation preserving. Combining information from Equations 6 and 8 leads us to
conclude the following. When k is even, the orientation of Dµ−→p (T−→p (C4[Rk])) matches that of
Tµ(−→p )(C4[Rk]), and so we deduce that the push-forward orientation on Dµ−→p (T−→p Slq) is equal to
the preimage orientation on Tµ(−→p )Slq as claimed. When k is odd, the push-forward orientation of
Dµ−→p (T−→p (C4[Rk])) is opposite that of Tµ(−→p )(C4[Rk]), and thus the orientation on Dµ−→p (T−→p Slq)
is opposite to the preimage orientation on Tµ(−→p )Slq, also as claimed. Note that we need both cases,
because when k > 2, we can still have planar squares in Slq (and our other variational vector ﬁelds
will be harder to deﬁne).
All that remains to complete the proof, is to show that det Dg > 0 and so Dg is orientation pre-
serving. Case 1: Assume that −→p ∈ Slq is a planar conﬁguration, and use the corresponding basis
{−→
h 1, −→
h 2, −→
h 3, −→
h 4} of vectors moving points along the ellipse from the proof of Proposition 25.
To help keep track of the action of µ, denote µ(−→p ) = (p2, p3, p4, p1) = (ˆp1, ˆp2, ˆp3, ˆp4), and so

ˆp1 = p2, . . . , ˆp4 = p1. Note that Dµ−→p (
−→
h 1) = Dµ−→p
 





v1
0
0
0
 



 =
 




 0
0
0
v1




, and so the vector v1 is

at point ˆp4 = p1. Thus Dµ−→p (
−→
h 1) |ˆp4 − ˆp3| = b2
√a2+b2 , Dµ−→p (−→
h 1) |ˆp1 − ˆp4| = − a2
√a2+b2 , and

Dµ−→p (
−→
h 1) |ˆp4 − ˆp2| = −a2+b2/
√2(a2+b2). Computing using the ﬁrst row of Equation 3 gives

Dµ−→p (−→
h 1)(r2
124) =
 √a2 + b2

ab
 (
0 + a2

a2 + b2
 ) = a
b .

Once again, we use Mathematica and compute that on the space Span{Dµ−→p (−→
h 1), Dµ−→p (
−→
h 2), Dµ−→p (−→
h 3), Dµ−→p (
−→
h 4)},
we have:
 Dg =
 




 a
b − a
b − b
a b
a 0
0 b
a − a
b − b
a a
b
b
a 0 a
b − a
b − b
a
a
b − b
a a
b − b
a a
b − b
a a
b − b
a
 



 .

This matrix has determinant 8(a4 − b4)
a2b2 which is positive (since we assumed a > b).
 21

Case 2: Assume that −→p ∈ Slq corresponds to a nonplanar conﬁguration, and use the other ba-
sis (also named) {
−→
h 1, −→
h 2, −→
h 3, −→
h 4} from the proof of Proposition 25. As before denote µ(−→p ) =
(p2, p3, p4, p1) = (ˆp1, ˆp2, ˆp3, ˆp4). By using similar reasoning, we observe that Dµ−→p (
−→
h 1) |ˆp4 − ˆp3| =
−ℓ/2, and all other derivatives are 0. Thus all entries of the ﬁrst column of Dg are zero, except for

Dµ−→p (
−→
h 1)(r2
342) = 2
ℓ
 (
− ℓ
2 − 0
) = −1.

Once again, we compute that on the space Span{Dµ−→p (−→
h 1), Dµ−→p (
−→
h 2), Dµ−→p (−→
h 3), Dµ−→p (
−→
h 4)},
we have:
 Dg =
 




 0 1 0 0
0 −1 1 0
−1 0 −1 0
0 0 0 −1




 ,

and det Dg = 1 > 0, as desired. □

Remark 30. Note that Proposition 29 can be extended to hold for the (1234) face of ∂Slq. How-
ever, the (13)(24) face needs an additional computation. We have chosen not to include this com-
putation, since ∂Slq and ∂C0
4 [γ(S1)] are disjoint in C4[Rk], and we don’t need it for the following
result.

Proposition 31. The manifolds C4[Rk], C0
4 [γ(S1)], and Slq share a smooth, free, and properly
discontinuous Z/4Z action given by cyclically relabeling points in a conﬁguration.
(1) The generator (p1, p2, p3, p4) ↦→ (p2, p3, p4, p1) is always orientation-reversing on
C0
4 [γ]. It is orientation-reversing on both C4[Rk] and Slq if k is odd, and orientation
preserving on C4[Rk] and Slq if k is even.
(2) The quotient spaces by the action of Z/4Z, ˆC4[Rk] and ˆC0
4 [γ(S1)], are manifolds-with-
boundary and corners, with ˆC0
4 [γ(S1)] non-orientable. Also, ˆC4[Rk] is non-orientable
when k is odd, and orientable when k is even.
(3) The intersection of ̂Slq (the quotient space by the action of Z/4Z) with the complement of
an ϵ-neighborhood of the boundary face (13)(24) (which is preserved under the action), is
a manifold-with-boundary. It is orientable precisely when ˆC4[Rk] is.
(4) The spaces ̂Slq and ˆC0
4 [γ(S1)] are boundary-disjoint in ˆC4[Rk].

Proof. We have already seen that the action on C4[Rk] is smooth, free and properly discontinu-
ous and that it descends to a corresponding action on the submanifolds C0
4 [γ(S1)] and Slq. It is
straightforward to see this action is orientation-reversing on C0
4 [γ(S1)]. Lemma 28 and Propo-
sition 29 proves the last part of (1). Statement (2) follows immediately. Statement (3) follows
from Propositions 25, 37, and 29. We note for (4) that the action is actually an isometry on C4[γ],
so it does indeed descend to the ϵ-neighborhood of (13)(24). Thus the quotient spaces remain
boundary-disjoint. □

In conclusion, the spaces we will apply our method to from Section 3.2 are ˆC4[Rk], Z = ̂Slq
and ˆC0
4 [γ(S1)].

22 JASON CANTARELLA, ELIZABETH DENNE, AND JOHN MCCLEARY

4.4. Base case and conclusion. Before we complete our arguments, we need to consider a base
case. For us this is a planar ellipse.

Lemma 32. In R2, if the image of γ : S1 → R2 is a planar ellipse x2/a2 + y2/b2 = 1 with a > b,
then ˆC0
4 [γ(S1)] ∩ ̂Slq ̸= ∅, and the intersection represents a single square.

Proof. We prove that the intersection is a single square. This is a straightforward computation
relying on the symmetry of the ellipse and is found in Lemma 40 in Appendix C. □

Proposition 33. In R2, if the image of γ : S1 → R2 is a planar ellipse x2/a2 + y2/b2 = 1 with
a > b, then ˆC0
4 [γ(S1)] and ̂Slq intersect transversely (namely, ˆC0
4 [γ] ⋔ ̂Slq), and the intersection
represents a single square.

Proof. Recall that Slq is the preimage of (1, 1, 1, 0) under the map g given by Equation 1. To
prove that C0
4 [γ(S1)] is transverse to Slq, we show that g restricted to C0
4 [γ(S1)] is transverse to
(1, 1, 1, 0). Recall from the proof of Proposition 25 that in Case 1, we considered the planar case.
We started with a square inscribed in an ellipse. We then considered tangent vectors corresponding
to motions of the square along (and tangent to) the ellipse. We computed Dg restricted to these
vectors. Since Dg had nonzero determinant, this means we proved that C0
4 [γ] ⋔ Slq.
Recall that the quotient spaces ˆC0
4 [γ(S1)] and ̂Slq arise from the action of the map µ (see Propo-
sition 31) that cyclically permutes the coordinates. The map µ is differentiable and an isometry. If
we look at the intersection of the quotient spaces ˆC0
4 [γ(S1)] and ̂Slq, then this is isometric to any
of the 4 pre-images. Since transversality is a local computation, it descends to the quotient spaces.
We can then conclude that the quotient spaces ˆC0
4 [γ(S1)] and ̂Slq are transverse as well. □

As we remarked at the beginning of Section 4.3, the number of labeled squares must be even be-
cause every square is counted 4 times. So the homology class of C0
4 [γ(S1)]∩Slq in H0(Slq; Z/2Z)
is zero. However, taking quotients mod Z/4Z ﬁxes this problem, and we conclude the following.

Corollary 34. The homology class of ˆC0
4 [γ(S1)] ∩ ̂Slq in H0( ̂Slq; Z/2Z) is 1.

We are now ready to prove our version of the square-peg theorem.

Theorem 35. Take any regular, C∞-smooth embedding of a curve γ : S1 ↪→ Rk. Then for all
ϵ > 0, there is a C∞-open neighborhood of γ, in which there is, for all m, a Cm-dense set of
smooth embeddings γ′ : Sl ↪→ Rk, with ∥ ˆC0
4 [γ′(S1)] − ˆC0
4 [γ(S1)]∥0 < ϵ, and ˆC0
4 [γ′] ⋔ ̂Slq.
Moreover,
ˆC0
4 [γ′(S1)] ∩ ̂Slq = {an odd, ﬁnite set of inscribed square-like quadrilaterals}.

As a reminder to the reader, we note that the Cm-dense set of smooth embeddings is with respect
to the Whitney C∞-topology from Section 3.

Proof. We follow the method outlined in Section 3.2 for Theorem 21.
Step 0: For any smooth embedding γ : S1 ↪→ Rk, Proposition 31 guarantees ˆC0
4 [γ(S1)] is a sub-
manifold of ˆC4[Rk].
 23

FIGURE 4. This picture shows three of the ﬁve squares inscribed in an irregular
three-lobed curve and two of the three squares inscribed in an irregular “tooth-
shaped” curve. Since each family shares the vertical ﬂip symmetry of each curve,
we show the center (symmetric) square in the second and fourth pictures, while the
ﬁrst and third show half of the asymmetrical squares. While on the left curve the
squares are fairly close together, a computer search reveals that they are certainly
distinct.

Step 1: Propositions 25, 29 and 31 guarantee ̂Slq ∩ ˆC4(Rk) is a submanifold of ˆC4(Rk) with
∂ ̂Slq ⊂ ∂ ˆC4[Rk]. Lemma 26 and Proposition 31 show that ˆC4[γ(S1)] and ̂Slq are
boundary-disjoint.
Step 2: Our standard embedding i : S1 ↪→ Rk is an ellipse. Proposition 33, establishes the exis-
tence of a transverse intersection between ˆC4[i(S1)] and ̂Slq inside ˆC4(Rk). Corollary 34
shows the homology class of the intersection is 1 in H0( ̂Slq; Z/2Z).
Step 3: Fix an ϵ > 0. We can adjust the proof of our transversality theorem (Corollary 18) to apply
to our setting. This gives us a C∞-open neighborhood of γ in which there is, for all m, a
Cm-dense set of smooth embeddings γ′ : S1 ↪→ Rk, such that ∥ ˆC[γ′] − ˆC4[γ]∥ < ϵ, and
ˆC0
4 [γ′] ⋔ ̂Slq, and for which ∂ ̂Slq and ∂ ˆC0
4 [γ′(S1)] are disjoint in ˆC0
4 [Rk].
Step 4: We can adjust the proofs of Theorem 19 and Theorem 20 to our setting. This lets us
conclude that the intersections ˆC0
4 [i(S1)] ∩ ̂Slq and ˆC0
4 [γ′(S1)] ∩ ̂Slq represent the same
homology class in ̂Slq.
This means that the ﬁnite collection of points (0-manifold) ˆC0
4 [γ] ∩ ̂Slq is cobordant by a 1-
manifold to the single square in the initial ellipse in ̂Slq, and hence that the number of inscribed
squares is odd. □

Theorem 35 is illustrated by the 3 squares inscribed in an irregular curve shown on the left and
center-left in Figure 4. This curve has 5 squares in total (an additional 2 squares can be found
using a vertical ﬂip symmetry). The curve on the right and center right in Figure 4 has 3 inscribed
squares in total. We note that when C0
4 [γ] is not transverse to Slq this count need not be odd.
Indeed Popvassiliev [37], and F. Sagols and R. Mar´ın [38] have constructed, respectively, smooth
convex curves, and piecewise linear curves which admit exactly n inscribed squares. In addition,
W. van Heijst [48] proved that any real algebraic curve of degree n in R2 inscribes either inﬁnitely
many squares or at most n4−5m2+4m/4 squares.

24 JASON CANTARELLA, ELIZABETH DENNE, AND JOHN MCCLEARY

A few historical comments are in order here. First, this is certainly not the ﬁrst proof of the
square-peg theorem to use an intersection-theoretic approach. As previously mentioned Grif-
ﬁths [16] took a similar approach, though he (wrongly) computes the intersection number. As a
result, he claims to have proved not only the square-peg theorem but a “rectangular-peg theorem”.
The rectangular case does not admit the quotient-space simpliﬁcation above (there are generally
two inscribed rectangles of a given aspect ratio in the ellipse). For a long while, the “rectangular-
peg theorem” proved to be an open and difﬁcult problem. However, this was recently solved by
J.E. Greene and A. Lobb in [15]. We also note that Matschke [28] proved a version of the square-
peg theorem from a theorem about loops of polygons inscribed in curves by arguing that a loop of
rhombi which was invariant under the cyclic permutation contained a square by the intermediate
value theorem, also an approach followed by L.G. Schnirel’man [39]. Additionally, in his PhD
thesis [29] Matschke claims a similar argument shows any regular C∞-smooth embedding of S1

in Rk has an inscribed square-like quadrilateral.

5. FUTURE DIRECTIONS

We have already mentioned that we have applied the method given in Section 3.2 to the question
of inscribing constructible simplices in embedded spheres in [7]. These results generalize the
results of M.D. Meyerson [32], M. Nielsen [35], and others [18, 29] on inscribing families of
triangles in planar and spatial curves.
One of the recurring features of the method in this paper is that the introduction of compacti-
ﬁed conﬁguration spaces simpliﬁes many of the tricky technical pieces in the proof by exporting
the troublesome behavior to the boundaries. For example, applying a transversality theorem to
squares and conﬁgurations of inscribed quadrilaterals requires us to have some strategy for deal-
ing with “degenerate” conﬁgurations. The extension of the πij and sijk data to the boundary of
conﬁguration space (with the associated metric) allowed us to argue easily that there could be no
inﬁnitesimal squares inscribed on a smooth curve. On the other hand, this is not the only way
to address these difﬁculties: For instance, Stromquist [44] deals with basically the same problem
by showing directly that there are no squares (or square-like quadrilaterals) smaller than some ϵ
which can be inscribed on a curve with some mild smoothness assumptions and hence avoids the
dangerous diagonals of the product space (Rk)4. We give a similar argument in [8] to show:

Theorem 36 ([8]). Let γ : S1 ↪→ Rn be an embedding of S1 in Rn. If γ is in FTCWC, then γ has
an inscribed square-like quadrilateral.

We note that since this result is obtained by a limit argument, we cannot rule out the possibility
that several squares come together in the limit to leave an even number of squares inscribed in the
ﬁnal curve, as in the examples of [37, 38, 48]. The appeal of this result is that it is a generalization
of the square-peg problem to embedded space-curves, and that the class of curves of ﬁnite total
curvature is a well-understood space (cf. [45]). When we set n = 2, we recover the square-peg re-
sult. The regularity class of curves in Theorem 36 is similar in ﬂavor to the curves of low regularity
for square-pegs given by Stromquist [44], Matschke [28, 30], and T. Tao [46], but generalizes to
higher dimensions.
A very interesting possible extension of the methods here would be to use the 1-jet version of
multijet transversality to try to prove a transversality theorem for submanifolds of conﬁguration

25

spaces which do intersect in certain boundary faces. Doing so would allow one to extend the
“counting” and homology arguments above to detect boundary intersections between submanifolds
of conﬁguration spaces. For example, one might try to argue in this way that the space of triangles
with a given angle inscribed in a curve had the homology of the torus, keeping in mind that a
circle’s worth of such “triangles” would be expected to be chords meeting the tangent to the curve
in the speciﬁed angle. Another interesting use for such a theorem would be to try to extend these
theorems to immersed curves with normal crossings (as opposed to simply studying embedded
curves).
We have proved that the space of smooth curves with an odd number of squares are dense
among smooth curves in the plane (or residual among smooth curves). This is not quite the same
as proving that a “generic” smooth curve has an odd number of inscribed squares. It would be very
interesting to try to extend these results to a set of curves which was full-measure among plane
curves according to some natural measure on curves, as F. Morgan does in [33] for space curves
bounding a unique area-minimizing surface.

ACKNOWLEDGMENTS

The authors would like to ﬁrst thank Gerry Dunn who introduced us to the problem. We would
also like to thank the people who have discussed the problem with us over the years: Jordan Ellen-
berg, Richard Jerrard, Rob Kusner, Benjamin Matschke, Igor Pak, Strashimir Popvassiliev, John
M. Sullivan, Cliff Taubes, and Gunter Ziegler.

REFERENCES

[1] Arseniy Akopyan and Sergey Avvakumov. Any cyclic quadrilateral can be inscribed in any closed convex smooth
curve. Forum Math. Sigma, 6:Paper No. e7, 9, 2018.
[2] Arseniy Akopyan and Roman Karasev. Inscribing a regular octahedron into polytopes. Discrete Math., 313(1):122–
128, 2013.
[3] Jai Aslam, Shujian Chen, Florian Frick, Sam Saloff-Coste, Linus Setiabrata, and Hugh Thomas. Splitting loops
and necklaces: variants of the square peg problem. Forum Math. Sigma, 8:Paper No. e5, 16, 2020.
[4] Scott Axelrod and Isadore M. Singer. Chern-Simons perturbation theory. II. J. Differential Geom., 39(1):173–213,
1994.
[5] Pavle V. M. Blagojevi´c and G¨unter M. Ziegler. Tetrahedra on deformed spheres and integral group cohomology.
Electron. J. Combin., 16(2):Research Paper 16, 11, 2009. Special volume in honor of Anders Bj¨orner.
[6] Ryan Budney, James Conant, Kevin P. Scannell, and Dev P. Sinha. New perspectives on self-linking. Adv. Math.,
191(1):78–113, 2005.
[7] Jason Cantarella, Elizabeth Denne, and John McCleary. Families of similar simplices inscribed in most smoothly
embedded spheres, Preprint 2021.
[8] Jason Cantarella, Elizabeth Denne, and John McCleary. Square-like quadrilaterals inscribed in embedded space
curves, Preprint 2021.
[9] Arnold Emch. Some Properties of Closed Convex Curves in a Plane. Amer. J. Math., 35(4):407–412, 1913.
[10] Arnold Emch. On the Medians of a Closed Convex Polygon. Amer. J. Math., 37(1):19–28, 1915.
[11] Arnold Emch. On Some Properties of the Medians of Closed Continuous Curves Formed by Analytic Arcs. Amer.
J. Math., 38(1):6–18, 1916.
[12] William Fulton and Robert MacPherson. A compactiﬁcation of conﬁguration spaces. Ann. of Math. (2),
139(1):183–225, 1994.
[13] Martin Golubitsky and Victor Guillemin. Stable mappings and their singularities. Springer-Verlag, New York,
1973. Graduate Texts in Mathematics, Vol. 14.

26 JASON CANTARELLA, ELIZABETH DENNE, AND JOHN MCCLEARY

[14] Joshua Evan Greene and Andrew Lobb. Cyclic quadrilaterals and smooth Jordan curves, 2020.
[15] Joshua Evan Greene and Andrew Lobb. The rectangular peg problem. Ann. of Math. (2), 194(2):509–517, 2021.
[16] H. Brian Grifﬁths. The topology of square pegs in round holes. Proc. London Math. Soc. (3), 62(3):647–672, 1991.
[17] Victor Guillemin and Alan Pollack. Differential topology. AMS Chelsea Publishing, Providence, RI, 2010. Reprint
of the 1974 original.
[18] Aryaman Gupta and Simon Rubinstein-Salzedo. Inscribed triangles of Jordan curves in Rn, 2021.
[19] Andr´e Haeﬂiger. Differentiable imbeddings. Bull. Amer. Math. Soc., 67:109–112, 1961.
[20] Morris W. Hirsch. Differential topology, volume 33 of Graduate Texts in Mathematics. Springer-Verlag, New York,
1994. Corrected reprint of the 1976 original.
[21] Cole Hugelmeyer. Every smooth Jordan curve has an inscribed rectangle with aspect ratio equal to √
3, 2018.
[22] Cole Hugelmeyer. Inscribed rectangles in a smooth Jordan curve attain at least one third of all aspect ratios. Ann.
of Math. (2), 194(2):497–508, 2021.
[23] Shizuo Kakutani. A proof that there exists a circumscribing cube around any bounded closed convex set in R3.
Ann. of Math. (2), 43:739–741, 1942.
[24] Victor Klee and Stan Wagon. Old and new unsolved problems in plane geometry and number theory. The Dolciani
Mathematical Expositions, 11. Mathematical Association of America, 1991.
[25] Greg Kuperberg. Circumscribing constant-width bodies with polytopes. New York J. Math., 5:91–100, 1999.
[26] V. V. Makeev. On quadrangles inscribed in a closed curve and the vertices of the curve. Zap. Nauchn. Sem. S.-
Peterburg. Otdel. Mat. Inst. Steklov. (POMI), 299(Geom. i Topol. 8):241–251, 331, 2003.
[27] V. V. Makeev. Inscribed and circumscribed polyhedra for a convex body and a problem on continuous functions on
a sphere in Euclidean space. Algebra i Analiz, 18(6):187–204, 2006.
[28] Benjamin Matschke. On the Square Peg Problem and some Relatives. arXiv.org, math.MG:186, December 2009.
[29] Benjamin Matschke. Equivariant topology methods in discrete geometry. PhD thesis, Freie Universit¨at, 2011.
[30] Benjamin Matschke. A survey on the square peg problem. Notices Amer. Math. Soc., 61(4):346–352, 2014.
[31] Benjamin Matschke. Quadrilaterals inscribed in convex curves. Trans. Amer. Math. Soc., 374(8):5719–5738, 2021.
[32] Mark D. Meyerson. Equilateral triangles and continuous curves. Fund. Math., 110(1):1–9, 1980.
[33] Frank Morgan. Almost Every Curve in R3 Bounds a Unique Area Minimizing Surface. Inventiones Mathematicae,
45:253, 1978.
[34] James R. Munkres. Topology: a ﬁrst course. Prentice-Hall, Inc., Englewood Cliffs, N.J., 1975.
[35] Mark J. Nielsen. Triangles inscribed in simple closed curves. Geom. Dedicata, 43(3):291–297, 1992.
[36] Igor Pak. Lectures on Discrete and Polyhedral Geometry. Free online text. 2010.
[37] Strashimir G. Popvassilev. On the number of inscribed squares of a simple closed curve in the plane. arXiv.org,
0810:4806, October 2008.
[38] Feli´u Sagols and Ra´ul Mar´ın. Two discrete versions of the inscribed square conjecture and some related problems.
Theoret. Comput. Sci., 412(15):1301–1312, 2011.
[39] L. G. Schnirel’man. On certain geometrical properties of closed curves. (russian). Uspehi Matem. Nauk, 10:34–44,
1944.
[40] Richard Evan Schwartz. A trichotomy for rectangles inscribed in Jordan loops. Geom. Dedicata, 208:177–196,
2020.
[41] Richard Evan Schwartz. Inscribed rectangle coincidences. Adv. Geom., 21(3):313–324, 2021.
[42] Dev P. Sinha. Manifold-theoretic compactiﬁcations of conﬁguration spaces. Selecta Math. (N.S.), 10(3):391–428,
2004.
[43] Stephen Smale. Generalized Poincar´e’s conjecture in dimensions greater than four. Ann. of Math. (2), 74:391–406,
1961.
[44] Walter Stromquist. Inscribed squares and square-like quadrilaterals in closed curves. Mathematika, 36(2):187–197,
1989.
[45] John M. Sullivan. Curves of ﬁnite total curvature. In Discrete Differential Geometry, volume 38 of Oberwolfach
Semin., pages 137–161. Birkh¨auser, Basel, 2008.
[46] Terence Tao. An integration approach to the Toeplitz square peg problem. Forum Math. Sigma, 5:Paper No. e30,
63, 2017.
 27

[47] Otto Toeplitz. Ueber einige aufgaben der analysis situs. Verhandlugen Der SchwizerischeAn Naturfoschenden
Gesellshaft in Solothurn, 4:197, 1922.
[48] Wouter van Heijst. The algebraic square peg problem. Master’s thesis, Aalto University, 2014.
[49] Ismar Voli´c. A survey of Bott-Taubes integration. J. Knot Theory Ramiﬁcations, 16(1):1–42, 2007.
[50] Siniˇsa T. Vre´cica and Rade T. ˇZivaljevi´c. Fulton-MacPherson compactiﬁcation, cyclohedra, and the polygonal pegs
problem. Israel J. Math., 184:221–249, 2011.
[51] Hassler Whitney. Differentiable manifolds. Ann. of Math. (2), 37(3):645–680, 1936.
[52] Wen-ts¨un Wu. On the isotopy of C r-manifolds of dimension n in euclidean (2n + 1)-space. Sci. Record (N.S.),
2:271–275, 1958.
 APPENDIX A. STRUCTURE OF THE BOUNDARY OF Slq

Here, we give further results about the structure of the boundary of Slq, which we recall lies in
the (1234) and (13)(24) faces of ∂C4[Rk].

Proposition 37. Each of the boundary (1234) and (13)(24) faces of Slq is a submanifold of
C4[Rk].

Proof. Let us consider the (1234) boundary face, where both the sidelengths and diagonals of the
square-like quadrilateral vanish. Following Sinha [42] (Theorems 3.12 and 3.14), the boundary
face (1234) is diffeomorphic to the manifold Rk × ˜C4(Rk) × {0}, where ˜C4(Rk) corresponds to
conﬁgurations of 4 points up to scaling and translation. We are then able to smoothly extend the
ratios in the deﬁnition of g (Equation 1) to the boundary. Let (p, y1, y2, y3, y4) ∈ Rk × ˜C4(Rk),
and without loss of generality assume p is the center of mass of the conﬁguration, and the vectors
∑
i yi = 4p. It is straightforward to see that r2
ijl becomes ˜r2
ijl = |yi−yj |
|yi−yl| . Thus the arguments in
the proof of Proposition 25 carry over directly, and g is transverse to (1, 1, 1, 0) on this boundary
face. Hence Slq is a submanifold on the (1234) boundary face.
On the (13)(24) boundary face, the square-like quadrilaterals are four-fold covers of an interval
with π13 perpendicular to π24. This information is not given by our deﬁning map g (Equation 1)
and we will be unable to show that g is transverse on this face. We solve this problem by ﬁnding a
different map that deﬁnes Slq, and that is also transverse on the (13)(24) face. We deﬁne the map
f : C4[Rk] → R4 by

(9) f (−→p ) = ((π14 + π34) · π13, (π41 + π21) · π24, π13 · π24, r2
132 − r2
241) .

In Proposition 39 (in Appendix B) we prove that Slq = f −1(0, 0, 0, 0). Note that a point in Slq in
the (13)(24) face is captured by −→p = (p1 = p3, p2 = p4, π13, π24) ∈ Rk × Rk × Sk−1 × Sk−1.
We are only interested in (13)(24) face, so we make appropriate adjustments to f and restrict it to
become ˆf : C4[Rk] → R3 deﬁned by

ˆf (−→p ) = ( ˆf1(−→p ), ˆf2(−→p ), ˆf3(−→p )) = ((2π14) · π13, (2π41) · π24, π13 · π24) .

By design, Slq = ˆf −1(0, 0, 0) on the (13)(24) face. In order to use the Preimage Theorem of [17],
we follow the ideas behind the proof of Proposition 25, and ﬁnd three tangent vectors to C4[Rk]
on which it is easy to show D ˆf has three linearly independent rows. We ﬁrst compute a typical

28 JASON CANTARELLA, ELIZABETH DENNE, AND JOHN MCCLEARY

column of D ˆf , where we have differentiated with respect to a vector −→v .

(10)
 


D−→v (2π14) · π13 + (2π14) · D−→v π13
D−→v (2π41) · π24 + (2π41) · D−→v π24
D−→v (π13) · π24 + (π13) · D−→v π24
 



p1 = p3 v

p2 = p4
w
 p1
 p2
 p3

p4

FIGURE 5. On the left a point −→p in the (13)(24) face of ∂Slq. The vectors v and
w are the variations which move −→p to a square-like quadrilateral in the interior of
Slq. This is shown on the right. The vectors v and w are perpendicular to each
other, and also to the line (of symmetry) through p1 = p3 and p2 = p4.

The deﬁnition of Slq on the (13)(24) face guarantees that the line segment p1p4 is perpendicular
to both π13 and π24. The tangent vectors to Slq on the (13)(24) boundary face may be represented
by a vector −→v = (v1, v2, v3, v4), where v1, v2 ∈ Rk are tangent vectors to p1 and p4 respectively,
and v3, v4 ∈ Sk−1 are tangent vectors to π13 and π24 respectively. Our ﬁrst tangent vector is −→v 1 =
(0, 0, 1
2 π14, 0), which moves π13 in the π14 direction (perpendicular to both π13 and π24). Thus
D−→v 1π13 = 1
2 π14 and the directional derivatives of the other πij are 0. A short computation using
Equation 10 shows D−→v 1 ˆf1 = 0 · π13 + (2π14) · ( 1
2 π14) = 1, D−→v 1 ˆf2 = 0, and D−→v 1 ˆf3 = ( 1
2 π14) ·
π24 + π13 · 0 = 0. We repeat this computation for our second tangent vector −→v 2 = (0, 0, 0, 1
2 π41)
which moves π24 in the π41 direction (perpendicular to both π13 and π24), and also for our third
tangent vector −→v 3 = (0, 0, π24, 0) which moves π13 in the π24 direction (perpendicular to both
π13 and π41). With respect to the basis vectors π13, π24, π41, we ﬁnd

D ˆf =
 


1 0 0
0 1 0
0 0 1



 .

Hence D ˆf is onto and ˆf is transverse to (0, 0, 0), and thus Slq is a submanifold on the boundary
face (13)(24). □

Remark 38. The reader might wonder why we did not simply use f to deﬁne Slq throughout the
paper. It turns out that it is much, much harder to ﬁnd appropriate tangent vectors to use in the
proofs of Propositions 25, 37, and 29. We chose to simplify the computations at the cost of using
two functions to deﬁne Slq.
 29

We conclude this section by noting that we have not proven the stronger result that Slq is a
submanifold-with-boundary and corners of C4[Rk]. While this is most likely true, we do not need
this, or indeed any of the results in Appendices A or B, for our main theorem.

APPENDIX B. A SECOND APPROACH TO SQUARE-LIKE QUADRILATERALS.

The results in this appendix ﬁll in the details needed for the proof of Proposition 37. Recall that
we deﬁne Slq to be the subset of square-like quadrilaterals of C4[Rk] such that r124 = r231 =
r342 = 1 and r132 − r241 = 0. Equivalently, a point −→p = (p1, p2, p3, p4, α(p)) ∈ C4[Rk] is a
square-like quadrilateral when it has equal sides and equal diagonals. That is

|p1 − p2| = |p2 − p3| = |p3 − p4| = |p4 − p1|(11)
 |p1 − p3| = |p2 − p4|(12)

Before we continue we recall a result about dot product. Assume that for four unit vectors
⃗u1, ⃗u2, ⃗v1, ⃗v2, we have ⃗u1 · ⃗v1 = ⃗u2 · ⃗v2. Then cos θ1 = cos θ2, where 0 ≤ θi ≤ π are the angles
between the vectors. Hence θ1 = θ2. The converse also holds.
Again, assume that p1p2p3p4 is a square-like quadrilateral, so that △p1p4p2 is isosceles. Then
two internal angles (∠p1p4p2 = ∠p1p2p4) of the triangle are equal, and their corresponding
external angles are also equal. In addition, the line joining p1 to the midpoint of p2p4 bisects
∠p2p1p4 and is an altitude. Translating these ideas to taking the dot product of unit vectors gives
the following equivalent equations:

π14 · π24 = π12 · π42 = −π12 · π24 equal internal angles,

(π14 + π12) · π24 = 0

−(π14 + π12) · π24 = 0 angle bisector is the altitude,

(π41 + π21) · π24 = 0 we use this equation below,
π41 · π24 = π21 · π42 equal external angles.

Any of these ﬁve equations implies that △p1p2p4 is isosceles and that |p1 − p4| = |p1 − p2|.
We now prove there is a second way of deﬁning Slq (ﬁrst seen in Equation A). Recall that we
deﬁned the map f : C4[Rk] → R4 by

f (−→p ) = ((π14 + π34) · π13, (π41 + π21) · π24, π13 · π24, r2
132 − r2
241) .

Proposition 39. The quadrilateral p1p2p3p4 is square-like (satisﬁes Equations 11 and 12) if and
only if −→p = (p1, p2, p3, p4, α(p)) ∈ f −1(0, 0, 0, 0).

Proof. First assume that p1p2p3p4 has equal sides and equal diagonals. Then triangles △p4p1p3
and △p1p2p4 are both isosceles triangles. The discussion above shows that this implies (π14 +
π34) · π13 = 0, and (π41 + π21) · π24 = 0. Since the diagonals are equal in length, r2
132 − r2
241 = 0
is automatically true.
Note that showing π13 · π24 = 0, is the same as showing the diagonals p1p3 and p2p4 are
perpendicular to one another. When k = 2 (or the quadrilateral is planar), then the square-like
quadrilateral is in fact a square, and the diagonals of squares are perpendicular. When k > 2, we
need a different argument. Set m1 to be the midpoint of p1p3 and m2 to be the midpoint of p2p4.

30 JASON CANTARELLA, ELIZABETH DENNE, AND JOHN MCCLEARY

Then △p1p2p4 has altitude p1m2, and △p3p2p4 has altitude p3m2. Thus the plane through the
points p1p3m2 is perpendicular to p2p4, and so π13 · π24 = 0.
Now assume that −→p = (p1, p2, p3, p4, α(p)) ∈ f −1(0, 0, 0, 0). Since r2
132 − r2
241 = 0, then the
diagonals are equal in length. Now (π14 + π34) · π13 = 0 and (π41 + π21) · π24 = 0, shows that
△p4p1p3 and △p1p2p4 are both isosceles triangles. Since these triangles share side p1p4, we
get |p3 − p4| = |p4 − p1| = |p1 − p2|. Using the same notation as above, we let m2 be a point
on p2p4 such that p1m2 is an altitude of △p1p2p4. Thus p1m2 is perpendicular to p2p4. Since
π13 · π24 = 0, then p1p3 is perpendicular to p2p4. This means that the plane though p1p3m2 is
perpendicular to p2p4, and so p3m2 is also perpendicular to p2p4. Thus △p4m2p3 ∼= △p2m2p3
(SAS) and hence |p4 − p3| = |p2 − p3|. Altogether we see that all the sides have the same length,
and so the quadrilateral is indeed square-like. □

APPENDIX C. THE ELLIPSE

In order to complete the proof of our main theorem, we need to show that in any ellipse, there is
a single inscribed square.

Lemma 40. In R2, if γ is a planar ellipse x2/a2 + y2/b2 = 1 with a2 ̸= b2, then ˆC0
4 [γ] ∩ ̂Slq ̸= ∅
and the intersection represents a single square.

Proof. We will need a lemma:

Lemma 41. Parallel chords meeting an ellipse have midpoints on a line through the center of the
ellipse (where the major and minor axes meet).

Proof. This is true for a circle and is preserved under afﬁne mappings. □

We prove that the intersection ˆC0
4 [γ]∩ ̂Slq is a single square. First, if we intersect the ellipse with
the lines y = ±x, by symmetry the intersection points form a square. We prove that this is the only
square inscribed in the ellipse. If we parametrize the ellipse by (x(θ), y(θ)) = (a cos θ, b sin θ),
we can work out that cos2 θ = b2/(a2 + b2) and sin
2 θ = a2/(a2 + b2).
Suppose ABCD is any square inscribed in the ellipse. Let M denote the midpoint of AB and N
denote the midpoint of CD. Then, by Lemma 41, M N passes through the center O of the ellipse.
Similarly, if K denotes the midpoint of AD and L the midpoint of BC, then KL passes through O.
Thus O is also the center of the square. Using our parametrization of the ellipse, we can write

A = (a cos α, b sin α), B = (a cos β, b sin β).

The segment OM is perpendicular to AB and so △OAM and △OBM are congruent and OA ∼=
OB. Thus a
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
√a2 + b2). □

31

MATHEMATICS DEPARTMENT, UNIVERSITY OF GEORGIA, ATHENS GA 30602
Email address: jason@math.uga.edu

MATHEMATICS DEPARTMENT, WASHINGTON & LEE UNIVERSITY, LEXINGTON VA 24450
Email address: dennee@wlu.edu

MATHEMATICS & STATISTICS DEPARTMENT, VASSAR COLLEGE, POUGHKEEPSIE NY 12604
Email address: mccleary@vassar.edu
