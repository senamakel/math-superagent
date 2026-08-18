<!-- source: https://arxiv.org/pdf/0810.1439 | converted from PDF -->

arXiv:0810.1439v2  [math.CO]  11 Nov 2008
Fulton-MacPherson compactiﬁcation,
cyclohedra, and the polygonal pegs problem

Siniˇsa T. Vre´cica

Faculty of Mathematics
University of Belgrade
vrecica@matf.bg.ac.yu
 Rade T. ˇZivaljevi´c

Mathematical Institute
SANU, Belgrade
rade@mi.sanu.ac.yu

To Anders Bj¨orner,
on the occasion of his 60th anniversary.

Abstract

The cyclohedron Wn, known also as the Bott-Taubes polytope, arises both
as the polyhedral realization of the poset of all cyclic bracketings of the word
x1x2 . . . xn and as an essential part of the Fulton-MacPherson compactiﬁcation
of the conﬁguration space of n distinct, labelled points on the circle S1. The
“polygonal pegs problem” asks whether every simple, closed curve in the plane
or in the higher dimensional space admits an inscribed polygon of a given shape.
We develop a new approach to the polygonal pegs problem based on the Fulton-
MacPherson (Axelrod-Singer, Kontsevich) compactiﬁcation of the conﬁguration
space of (cyclically) ordered n-element subsets in S1. Among the results ob-
tained by this method are proofs of Gr¨unbaum’s conjecture about aﬃne regular
hexagons inscribed in smooth Jordan curves and a new proof of the conjecture
of Hadwiger about inscribed parallelograms in smooth, simple, closed curves in
the 3-space (originally established by Makeev in [Mak]).

1 Introduction

The classical “square peg problem”, going back to Toeplitz (1911) and Emch (1913),
asks whether every Jordan curve in the plane has four points forming a square. In
the ﬁrst published account of the problem [Em] the result was established for the case
of closed convex curves. Over the span of almost one hundred years many interesting
cases of the problem were resolved, occasionally after initial partial refutations and
subsequent improvements over the original proofs. The reader is referred to [Gr¨u],
[KlWa], and [Pak] for a more complete overview of the history of the problem and a
brief discussion of the leading contributions by Emch (1911, 1913), Shnirelman (1929,
1944), Jerrard (1961), Stromquist (1989), Griﬃths (1991), and others.

∗Supported by Grants 144014 and 144026 of the Serbian Ministry of Science and Technology.

1

In spite of its simple and mathematically attractive formulation the square peg
problem has not been solved so far in full generality. Other problems of similar nature
were formulated in the meantime and some of them have remained unsolved even in the
case of smooth curves, see [Gr¨u] and [Ha] for examples and [Gri], [Pak] for a broader
outlook on the whole area.
In this paper we emphasize the role of cyclohedra Wn in the “square peg prob-
lem” and other related problems of discrete geometry where polygons are inscribed
in curves, surfaces etc. We start in Section 5 with a complete, reasonably short and
conceptually transparent (if not entirely elementary) solution of the “square peg prob-
lem” in the case of smooth curves. More importantly, this section serves as a model
example of how the “cyclohedron approach” (or the method of canonical compacti-
ﬁcations) can be applied to other problems of this nature. In Section 6, using this
method, we prove the Gr¨unbaum’s conjecture about inscribed aﬃne regular hexagons
in smooth, simple closed curves in the plane. By the same technique we prove a result
in Section 7 (established earlier in [Mak] by diﬀerent methods) which conﬁrms a con-
jecture of Hadwiger about inscribed parallelograms in smooth, simple, closed curves
in the 3-space. These results should not be seen as isolated examples. Rather they
are an indication of the potential of the method for applications to many other classes
of problems where the degeneration of point conﬁgurations and the appearance of the
associated pseudo-solutions has been one of the main obstacles for applying standard
topological methods. In Section 8 we brieﬂy discuss possibilities for extending results
from Sections 5, 6 and 7 to larger classes of curves and oﬀer a broader outlook to the
method of canonical compactiﬁcations (FMASK -compactiﬁcations).

2 Outline of the main idea

Given a Jordan curve Γ ⊂ R2 and its parametrization f : S1 → Γ, the conﬁguration
space of all (labelled) quadrangles inscribed in Γ is parameterized by the torus T 4 ∼=
(S1)4. In order to determine which of these quadrangles are squares one introduces an
associated test map Φ : T 4 → U where U ∼= R4 is the associated test vector space. The
test map is well chosen if q ∈ T 4 is associated to a square inscribed in Γ if and only if
Φ(q) = 0 ∈ U.

• Recall that the conﬁguration space, the test map, and the test space are the
basic ingredients of the well known “conﬁguration space/test map scheme” [ˇZ04]
(CS/T M-scheme for short) for applying (equivariant) topological methods in
combinatorial geometry. This proof scheme has been applied for decades before
it was codiﬁed and named in [ˇZ96], [ˇZ98] and remains one of the main tools for
applying topological methods in geometric combinatorics.

One of the main diﬃculties with the application of the CS/T M-scheme in the “square
peg problem” and its relatives is the appearance of pseudo-solutions, i.e. degenerate
conﬁgurations which pass the test Φ(q) = 0 but are not genuine solutions. Indeed,
the test map Φ often takes into account only the mutual distances of elements of

2

the conﬁguration q, so for example in the square peg problem F does not distinguish
degenerate squares q = (v, v, v, v) from actual squares.
A natural way to get around this diﬃculty is to remove from the conﬁguration space
T 4 the diagonal ∆ = {q | q = (v, v, v, v) for some v ∈ S1} or perhaps more consistently
the “fat diagonal” ∆f := {q = (q1, q2, q3, q4) | qi = qj for some i ̸= j}. The resulting
truncated conﬁguration spaces T 4 \ ∆ and F (S1, 4) := T 4 \ ∆f are no longer compact
and this is often a source of other diﬃculties of topological nature.

Our main new idea is to “blow up” the degenerate conﬁgurations in ∆ (∆f ) and
to modify accordingly (regularize) the test map Φ. This means that we replace the
original conﬁguration space by the Fulton-MacPherson compactiﬁcation [F-M] of the
truncated conﬁgurations space. Actually we use its spherical version and a close relative
due to Axelrod-Singer and Kontsevich [A-S] [Ko], here referred to as the canonical or
FMASK -compactiﬁcation of the conﬁguration space.
In the context of the square peg problem, the conﬁguration space F (S1, 4) :=
(S1)4\∆f is compactiﬁed to the associated FMASK compactiﬁcation F [S1, 4]. The new
test map Ψ : F [S1, 4] → U is deﬁned as the extension of the map Φ
′ : F (S1, 4) → U for
a suitable modiﬁcation Φ
′ of the original test map which essentially takes into account
the rescaling of the degenerate conﬁgurations.
Throughout the paper we mainly work with the subspace S1(n) ⊂ F (S1, n) :=
(S1)n \ ∆f of all cyclically ordered n-tuples of points in S1 and the corresponding
compactiﬁcation S1[n] ⊂ F [S1, n]. As it was shown in [B-T], S1[n] ∼= S1 × Wn, where
Wn is a close relative of Stasheﬀ polytope (associahedron) called cyclohedron. This
allows us to give a direct and elementary exposition of F [S1, n] and S1[n] which is
suﬃcient for all our applications and which is fairly independent of the general theory of
FMASK compactiﬁcations (see however [Si] for a more complete treatment of F [M, n]
and other related compactiﬁcations).

3 FMASK -compactiﬁcation of conﬁguration spaces

Let us recall some elementary facts about the partially ordered set (C(Y ), ⩽) of all
compactiﬁcations of a (locally compact, Hausdorﬀ) space Y .

•1 A compactiﬁcation of Y is a pair cY = (X, c) where c : Y → X is a homeomorphic
embedding and ClX(c(Y )) = X. By deﬁnition c1Y ⩽ c2Y if there exists a
continuous map f : c2Y → c1Y such that c1 = f ◦ c2. Two compactiﬁcations
c1Y and c2Y are considered equivalent (and often identiﬁed) if both c1Y ⩽ c2Y
and c2Y ⩽ c1Y , which turns “⩽” into an order relation on the set C(Y ) of
(equivalence classes) of compactiﬁcations of Y . A simple but important fact is
that each non-empty set C0 ⊂ C(Y ) has the least upper bound with respect to
the order “⩽”, see e.g. [E], Theorem 3.5.9. Indeed, if C0 = {cjY }j∈J then the
smallest compactiﬁcation τ Y such that cjY ⩽ τ Y for all j ∈ J can be described
as the closure of the image of the diagonal embedding ∆ : Y → ∏

j∈J cjY .

3

•2 A map g : Y → Z from Y to a compact Z is not necessarily extendable to a
compactiﬁcation cY prescribed in advance. However, there exists the smallest
compactiﬁcation τ Y such that cY ⩽ τ Y and a map g′ : τ Y → Z such that
g = g′ ◦ τ . Indeed, it is easy to show that the closure ClcY ×Z(Γ(g)) of the graph
Γ(g) ⊂ Y × Z ⊂ cY × Z, in the compact space cY × Z, has all the required
properties. More generally, given a family F = {gj}j∈J of maps gj : Y → Zj,
from Y to compact spaces Zj, there is the smallest compactiﬁcation τ Y = τF Y
greater than cY where all functions gj can be extended.

Example 1. Suppose that Y = (S1)2 \ ∆ is the space of all ordered pairs of distinct
points in S1. Let cY = T 2 = (S1)2 be its “naive compactiﬁcation” and let g : Y → S1

be the map deﬁned by g(x, y) := (x − y)/∥x − y∥. Then the compactiﬁcation τ Y ,
described as the closure of the graph Γ(g) = {(p, g(p)) | p = (x, y) ∈ (S1)2 \ ∆} ⊂
(S1)2 × S1, is the “oriented blow up” of (S1)2 along the diagonal ∆. For the future
reference (Section 7) we denote this compactiﬁcation by ˜F [S1, 2] and observe that it is
homeomorphic to the annulus S1 × [0, 1].

Our main example of the construction of τF Y is the canonical compactiﬁcation (or
the FMASK compactiﬁcation) S1[n] of the conﬁgurations space Y := S1(n) ⊂ (S1)n of
all n-element subsets q = {q1 ≺ q2 ≺ . . . ≺ qn ≺ q1} ⊂ S1 of cyclically ordered points
in S1.
Given consecutive indices i − 1, i, i + 1 (where n + 1 := 1), let F = {θi}n
i=1 be the
collection of functions θi : S1(n) → [0, 1] deﬁned by θi(q) := ∡(qi−1qi)/∡(qi−1qi+1).
The functions θi alow us to reconstruct q ∈ S1(n), up to a rotation. However these
functions cannot be extended to the closure cY := Cl(S1(n)) of S1(n) in (S1)n, since
for example θi(q) is meaningless if qi = qi+1. For this reason it is quite natural to pass
to the compactiﬁcation τF Y where all these functions are well deﬁned.

Deﬁnition 2. The canonical or FMASK compactiﬁcation S1[n] of the space Y :=
S1(n) of all cyclically ordered n-element conﬁgurations in S1 is the compactiﬁcation
τ Y = τF Y associated to cY := Cl(S1(n)) ⊂ (S1)n and the family F = {θj}n
j=1. More
explicitly, τ Y is the closure of the image of the embedding

Λ : Y ֒→ cY ×
 n∏

j=1[0, 1](j)

where Λ = c×∏

j θj is the associated diagonal map. Similarly, by starting with the con-
ﬁguration space F (S1, n) of all (not necessarily cyclically ordered) n-tuples of distinct
points in S1, one obtains the associated FMASK compactiﬁcation F [S1, n].

•3 The construction of the compactiﬁcation τF Y depends functorially on the family
F . This means that τF ⩽ τF ′ if all functions from F are (informally speaking)
expressible by functions from F ′. In particular it is not diﬃcult to formulate a
criterion when two compactiﬁcations τF and τF ′ are equivalent. This can be used
to show the equivalence of S1[n] and F [S1, n] with the more general constructions
of F [M, n] developed in [A-S], [Ko], [Si], see also Deﬁnition 3.

4

For completeness and as an additional illustration of the main construction described in
•2 we ﬁnish this section with the deﬁnition of the FMASK -compactiﬁcation F [Rd, n].
Note that the word “compactiﬁcation” is not quite appropriate here, however the con-
struction of the (partial) compactiﬁcation τF Y is still meaningful and natural from the
geometric point of view.

Deﬁnition 3. The canonical or FMASK-compactiﬁcation F [Rd, n] of the space Y =
F (Rd, n) := (Rd)n \ ∆f of all collections of n, distinct, labelled points in Rd is the
(partial) compactiﬁcation τ Y = τF Y associated to the naive “compactiﬁcation” cY :=
(Rd)n and the family F = {αij}1≤i<≤n ∪ {βijk}i<j<k where αij : Y → Sd−1 is deﬁned
by αij(q) := (qj − qi)/ ∥ qj − qi ∥ while βijk : Y → [0, +∞] is the function that records
the ratio βijk(q) :=∥ qi − qj ∥ / ∥ qi − qk ∥.

4 Cyclohedron Wn

The following proposition reveals the stratiﬁed manifold structure of the space S1[n].

Theorem 4. ([B-T]) For n ≥ 3,
 S1[n] ∼= S1 × Wn (1)

where Wn is a (n − 1)-dimensional, convex polytope, called cyclohedron or the Bott-
Taubes polytope. Wn is combinatorially described as the convex polytope whose face
lattice is isomorphic to the poset of all partial, cyclic bracketings of the word x1x2 . . . xn.

(12)(34)
 ((12)3)4

(1(23))4
1((23)4)

1(2(34))

(34)(12)

3(4(12))

3((41)2) (3(41))2

((34)1)2
 (23)(41)

((23)4)1

(2(34))1
2((34)1)

2(3(41))
 (41)(23)
 4(1(23))

4((12)3)(4(12))3

((41)2)3

Figure 1: Cyclohedron W4.

Proof: (outline) The reader is referred to [B-T], [Mar], [MSS], and [Si] for more detailed
presentation and related background facts. We restrict ourselves to a brief explanation
of the isomorphism (1), suﬃcient for intended applications.

5

The functions θi : S1(n) → [0, 1] and their extensions ¯θi : S1[n] → [0, 1] can be
used as “coordinate functions” on spaces S1(n) and S1[n] respectively. They can be
combined to create 2-dimensional, 3-dimensional, or higher dimensional “navigation
instruments”, with the corresponding screens being one, two, or higher dimensional
simplices ∆
2, ∆
3 etc. For example, given a 4-element subconﬁguration qi ≺ qj ≺ qk ≺ ql
of q = {q1 ≺ . . . ≺ qn}, one can extend the function λ : S1(n) → ∆
2 deﬁned by

λ(q) := 1
∡(qi, ql) (∡(qi, qj), ∡(qj, qk), ∡(qk, ql)) (2)

to a function ¯λ : S1[n] → ∆
2, where ∡(p, q) = ̂p q is the arc length of the (counterclock-
wise) arc with endpoints p and q. Indeed, the function λ can be expressed in terms
of functions θi, consequently it can be extended to S1[n] and its extension similarly
expressed in terms of functions ¯θi.

(a) (b) (c)

Figure 2: Generic conﬁgurations in ∂W4.

The conﬁguration space S1(n) is clearly isomorphic to S1 × Int(∆)n−1. The reader
can use the “navigation screens” to convince herself that the compactiﬁcation of this
space is indeed described by equation (1). For example one can check that the generic
conﬁgurations depicted in Figure 2 (a), (b), and (c), respectively correspond to paral-
lelograms, pentagonal, and hexagonal facets of the cyclohedron W4. □

5 Square pegs in round holes

We begin with a version of the “square pegs in round holes” theorem for C 1-smooth
curves embedded in the 2-space. This result was in this generality proved by Stromquist
[St], see also Schnirelmann [Shn] and Guggenheimer [Gug] for earlier results established
with some extra hypotheses on the smoothness or curvature of the curve. The reader
is referred to [Gr¨u] (p. 84) for a list of references addressing the case of a convex curve
and to [Pa08] for what appears to be the only elementary presentation of the case of
simple closed polygons.

Theorem 5. Every simple closed curve Γ ⊂ R2, which is C 1-smooth, i.e. has a non-
vanishing and continuously moving tangent vector at each point, admits an inscribed
square.
 6

Figure 3: Cyclohedron as a compactiﬁcation/truncation of a simplex.

Our proof of Theorem 5 serves as a model for other proofs of similar nature. For this
reason it is broken into relevant individual steps illustrating FMASK -compactiﬁcation
modiﬁcation of the usual CS/T M-scheme [ˇZ04]. The scheme of the proof is summarized
in Section 5.5.
Theorem 5 is a not the most general result about inscribed squares in Jordan curves,
see [St], and Section 8 for a related discussion from the FMASK -compactiﬁcation point
of view.

5.1 Conﬁguration space S1(4) and the test maps

Suppose that f : S1 → R2 is a smooth embedding satisfying the conditions of Theo-
rem 5. Moreover we silently assume, here and elsewhere in the paper, that the embed-
ding is “counterclockwise” in the sense that the degree of the associated map s ↦→ df /ds
is +1.
Let Γ = Image(f ) ⊂ R2 be the associated smooth curve. Suppose that U :=
U1 ⊕ U2 ⊕ U3 is a vector space such that U1 ∼= R2, U2 ∼= U3 ∼= R and let Φ : (S1)4 → U
be the map deﬁned by
 Φ(t) = (φ1(F (t)), φ2(F (t)), φ3(F (t))) (3)

where F := f ×4 : (S1)4 → R2 ⊕ R ⊕ R is the map induced by f and

φ1(y) = y1+y3
2 − y2+y4
2 ,
φ2(y) = ∥y1 − y3∥ − ∥y2 − y4∥,
φ3(y) = ∥y1 − y2∥ − ∥y2 − y3∥ + ∥y3 − y4∥ − ∥y4 − y1∥.

It is clear that f (t1), f (t2), f (t3), f (t4) are consecutive vertices of a square inscribed in
the curve Γ if and only if Φ(t) = 0.
 7

Let Φ0 : S1(4) → U be the restriction of Φ on the conﬁguration space S1(4) of all
labelled 4-element subsets of S1 such that the labelling agrees with the counterclockwise
(cyclic) order of points on the circle S1.
The symmetric group S4 acts on (S1)4 by permuting coordinates. However, it is
its subgroup Z/4 of cyclic permutations that naturally acts on U and its subspaces Ui,
and turns Φ into a Z/4-equivariant map. In turn Φ0 is also a Z/4-equivariant map and
for the proof of Theorem 5 it would be suﬃcient to show that such an equivariant map
must have a zero.
Finally, let us record for the further reference that the generator ω ∈ Z/2 acts on
S1[4] = S1 × W4 by reversing the orientation while the action on U is the antipodal
action ω(v) = −v, hence it preserves the orientation of U ∼= R4.

5.2 Compactiﬁed conﬁguration space S1[4]

Let S1[4] be the canonical or FMASK -compactiﬁcation of the conﬁguration space
S1(4). We use the basic properties of this compactiﬁcation, as outlined in Section 3,
to deﬁne a modiﬁed test map Ψ0 : S1[4] → U.
Let η : (S1)4 → R be the map deﬁned on the conﬁguration t = (t1, t2, t3, t4) ∈ (S1)4

as the arc-length diameter of the set {t1, t2, t3, t4}, i.e. the minimum arc-length of a
closed arc L ⊂ S1 such that ti ∈ L for each i. Let ξ := η−1 and let Φ
′ be the
modiﬁcation of the test map Φ (equation (3)) deﬁned by

Φ
′(t) := ξ(t) · Φ(t) = (ξ(t)φ1(F (t)), ξ(t)φ2(F (t)), ξ(t)φ3(F (t))). (4)

Finally, let Φ
′
0 be the restriction of Φ0 on S1(4).

Proposition 6. The Z/4-equivariant map Φ
′
0 : S1(4) → U can be extended to a Z/4-
equivariant map Ψ : S1[4] → U such that Ψ(x) ̸= 0 for each x ∈ S1[4] \ S1(4) ∼=
S1 × ∂W4. Moreover, the Z/4-equivariant homotopy class of the restriction Ψ∂ : S1 ×
∂W4 → U \ {0} does not depend on the embedding f : S1 → R2.

Proof: The extension Ψ is clearly unique (if it exists). It is also clear that the only case
to be discussed is the case of points q ∈ S1[4] \ S1(4) such that η(q) = 0, or equivalently
ξ(q) = +∞. These are the points which corresponds to pentagons in Figure 1 and can
be characterized as limits in S1[4] of sequences qn = {t
n
i ≺ t
n
j ≺ t
n
k ≺ t
n
l }, where
(i, j, k, l) is a cyclic permutation of elements {1, 2, 3, 4} and ∡(t
n
i , t
n
l ) ↦→ 0 as n ↦→ +∞.
The last condition implies that all sequences (t
n
i )+∞
n=1 converge to the same point s ∈ S1.
The point q ∈ S1[4], which is the limit (in S1[4]) of the sequence qn ∈ S1(4), is (in the
language of Section 4) best visualized in the 2-dimensional screens described by equa-
tion (2). Since the associated barycentric coordinates ∡(tn
i ,tn
j )
∡(tn
i ,tn
l ) etc. are all well deﬁned
as functions on S1[4], it remains to be checked that the same applies to the functions
φi(F (t))
η(t) that appear in the test map (4), i.e. that these quotient can be meaningfully
(and continuously) extended to points q ∈ S1[4]. Since in the small neighborhood of
s ∈ S1 the function f : S1 → R2 is approximated by a linear function, i.e. the curve Γ

8

is in the vicinity of z = f (s) (up to a higher order inﬁnitesimal) approximated by its
tangent line at z ∈ Γ, we make the following useful observation.

O1 The value of the test function Ψ = (Ψ1, Ψ2, Ψ3) at a point q ∈ S1[4] is equal to
the value of the original test function Φ0 at an “inﬁnitesimal” quadruple qn =
{t
n
i ≺ t
n
j ≺ t
n
k ≺ t
n
l } approximating q, divided by the associated “inﬁnitesimal”
arc-length η(qn).

It follows that Ψ1(q) is always a non-zero vector collinear to the tangent vector of Γ
at z = f (s) with the only exception being the case of the point q represented by an
“inﬁnitesimal parallelogram” i.e. if

lim
n↦→∞ ∡(t
n
i , t
n
j )
∡(t
n
i , t
n
k ) = lim
n↦→∞ ∡(t
n
k , t
n
l )
∡(t
n
j , t
n
l ) = 0.

In this case it is not diﬃcult to check that Ψ3(q) ̸= 0 which comletes the proof of the
ﬁrst part of the proposition.
For the second part, let us suppose that f0, f1 : S1 → R2 are two smooth embeddings
such that both maps s ↦→ dfi/ds, i = 0, 1 have degree +1. Then the independence of
the Z/4-homotopy class of the map Ψ∂ from the embedding f : S1 → R2 follows from
the fact that any two such embeddings can be connected by a regular homotopy i.e.
by a family ft, t ∈ [0, 1] of smooth embeddings such dft(s)/ds ̸= 0 for each s ∈ S1. □

5.3 The obstruction . . .

It remains to be shown that no map in the Z/4-equivariant homotopy class of the map
Ψ∂ can be extended to S1 × W4, i.e. that there does not exist a Z/4-equivariant map
“?” that completes the square
 S1 × ∂(W4)) Ψ∂
−−−→ S3


↓ 

↓∼=

S1 × W4 ?
−−−→ S3
 (5)

The obstruction to the extension problem (5) lives in the equivariant cohomology group

H 4
Z/4((S1 × W4), S1 × ∂(W4)); Z))

where Z = π3(U \{0}) ∼= H3(U \{0}) ∼= H3(S3) ∼= Z inherits the Z/4-module structure
from the Z/4-action on U. By equivariant Poincar´e duality this group is isomorphic to
the group H Z/4
0 ((S1 × W4) \ S1 × ∂(W4)); Z ⊗ ε)) ∼= ZZ/4 ∼= Z/2

where ε is associated orientation character, i.e. the Z/4-module H4(S1[4], ∂S1[4]; Z).

9

5.4 . . . and its evaluation

We evaluate the obstruction in ZZ/4 ∼= Z/2 by counting the zeros of a “generic” (trans-
verse to zero) map ? : S1 × W4 → U (diagram (5)) which extends a map in the
Z/4-equivariant homotopy class of Ψ∂.
Suppose that Γ is a smooth oval in the plane which admits a Z/2 × Z/2 symme-
try. For example we can choose for Γ the ellipse centered at the origin, symmetric
with respect to the coordinate axes (Figure 4). Such an oval (ellipse) has a unique
inscribed square. Suppose that the vertices of this square (in counterclockwise order)
are b1, b2, b3, b4 and that b1 is in the ﬁrst quadrant. Moreover we assume that bj = f (aj)
for some parameters aj ∈ S1.
There is an obvious isomorphism Ta(S1(4)) ∼= ⊕
4
i=1 Tai(S1) of tangent spaces. Let
xi be a local coordinate on S1 deﬁned in the neighborhood of ai. For example let
xi(c) be the (oriented) angle ∡(ai, c) swept by the radius vector moving from ai to c.
Let [ ∂
∂xj ]4
j=1 = [ ∂
∂x1 , ∂
∂x2 , ∂
∂x3 , ∂
∂x4 ] be the associated basis (frame) of tangent vectors in
Ta(S1(4)).
We want to show that the diﬀerential dΨa : Ta(S1(4)) → T0(R4) ∼= R4 of Ψ,
evaluated at a = (a1, a2, a3, a4), is non-degenerate. Let yi := xi ◦ f −1 be the local
coordinate on Γ deﬁned in the neighborhood of bi, induced by xi. It follows that
the diﬀerential dFa : Ta((S1)4) → Tb(Γ4) maps the frame [ ∂
∂xj ]
4
j=1 to [λj ∂
∂yj ]
4
j=1, for
appropriate non-zero scalars λj.
Let α : (R2)4 → R2 × R × R be the map deﬁned by α(y) = (φ1(y), φ2(y), φ3(y)), so
in particular Φ(x) = α(F (x)).
 v1 b1b2

b3 b4

v2

v3 v4

Figure 4:

The frame [ ∂Ψ
∂xj ]
n
j=1 = [dΨ( ∂
∂xj )]4
j=1 is equal, up to rescaling and possibly up to some
changes of signs, to the frame [dα(vi)]4
i=1 where vi is an arbitrary (non-zero) vector in
Tbi(Γ) prescribed in advance. For convenience (Figure 4) we assume that the collection
{vi}4
i=1 is also (Z/2 × Z/2)-invariant.
Let us suppose that the rate of change of α in the direction of vector v1, evaluated
at the point (b1, b2, b3, b4), is

dα(v1) = dαb(v1) = (u; s, t) = (u1, u2; s, t) ∈ R2 ⊕ R ⊕ R.

10
 v1
y1
 b1

b = y2 2
 b = y4 4b = y3 3
 v4

v2

v3
 (1)

(4)(3)

(2)
 Figure 5:

By taking into account the (Z/2 × Z/2)-symmetry of the curve Γ, one easily deduces
that dα(v2) = (u1, −u2; −s, t) dα(v1) = (u1, u2; s, t)
dα(v3) = (−u1, −u2; s, t) dα(v4) = (−u1, u2; −s, t).

It follows that the determinant Det of the frame [dα(vj)]4
j=1 is

Det =
 ∣
∣
∣
∣
∣
∣
∣
∣
 u1 u1 −u1 −u1
u2 −u2 −u2 u2
s −s s −s
t t t t
 ∣
∣
∣
∣
∣
∣
∣
∣
 = −16stu1u2 ̸= 0

which in turn implies that the frame [ ∂Ψ
∂xj ]4
j=1 is also non-degenerate.

5.5 The proof of Theorem 5

Proof of Theorem 5: Assume that f : S1 → R2 is a (counterclockwise) smooth
parametrization of the curve Γ. The zeros of the associated (Z/4-equivariant) “test
map” Φ0 : S1(4) → U (Section 5.1) are in one-to-one correspondence with the squares
inscribed in Γ. After rescaling by a suitable positive, real function ξ, the modiﬁed test
map Φ
′
0 := ξΦ0 is Z/4-equivariantly extended (Section 5.2) to a map Ψ : S1[4] → U,
where S1[4] is the Fulton-MacPherson compactiﬁcation of S1(4). The restriction Ψ∂

of Ψ on the boundary ∂S1[4] of S1[4] has no zeros (Proposition 6). Moreover, its Z/4-
equivariant homotopy class is independent of the original curve Γ. The obstruction
for extending Z/4-equivariantly the map Ψ∂ : ∂S1[4] → U \ {0} to S1[4] is found to
be non-trivial (Sections 5.3 and 5.4) which ﬁnally implies that Φ0 must have a zero in
S1(4). □

11

6 Gr¨unbaum’s conjecture

B. Gr¨unbaum, see [Gr¨u] page 85, conjectured that every Jordan curve in the plane
contains the vertices of an aﬃne-regular hexagon. By deﬁnition a hexagon in the plane
is aﬃne-regular if it is the image of a regular hexagon by an aﬃne automorphism
of the plane. In contrast to the square peg problem, as emphasized in [Gr¨u], the
Gr¨unbaum’s conjecture has been opened even for the case of smooth curves. In this
section we establish this case of the conjecture and refer the reader to Section 8 for a
brief discussion how the smoothness condition can be relaxed.

Theorem 7. Every C 1-smooth, simple, closed curve in the plane contains either the
vertices of an aﬃne-regular hexagon or six collinear points which are the limit conﬁg-
uration of a convergent sequence of aﬃne-regular hexagons.

The proof of Theorem 7 follows the same scheme used in Section 5 so we focus our
attention on diﬀerences and relevant calculations. By assumption Γ ⊂ R2 is a simple,
closed, C 1-smooth curve in the plane, the last condition saying that a parametrization
can be chosen so that the curve has a non-zero, continuously moving tangent vector.
In analogy with the square peg problem we choose for the conﬁguration space the
Fulton-MacPherson compactiﬁcation S1[6] of the space S1(6) of all labelled, cyclically
ordered 6-element subsets {t1 ≺ t2 ≺ . . . ≺ t6 ≺ t1} in S1. Next we introduce the maps
α, β, γ, δ which serve for testing if the points x1, x2, . . . , x6 are consecutive vertices of
an aﬃne-regular hexagon in the plane,

α(x) = x1 + x4 − x2 − x5
β(x) = x2 + x5 − x3 − x6
γ(x) = x3 + x6 − x1 − x4
δ(x) = x1 − x2 + x3 − x4 + x5 − x6.
 (6)

Note that the condition α(x) = 0 says that the midpoints of the large diagonals [x1, x4]
and [x2, x5] coincide while δ(x) = 0, in addition to α(x) = β(x) = γ(x) = 0, guarantees
that the pairs of opposite sides are parallel to and half the length of the large diagonal
separating them.
As in the “square peg problem”, the system of equations

α(x) = β(x) = γ(x) = δ(x) = 0, (7)

admits, aside from genuine aﬃne-regular hexagons, also some degenerate solutions, for
example the hexagons where all vertices collapse to the same point. More generally
there exist solutions where points coincide in pairs, e.g. the solution x1 = x2 = a, x4 =
x5 = −a, x3 = x6 and the solutions obtained from this one by a cyclic permutation
of indices. These two types of degenerate solutions will be referred to as 1-point and
3-point degenerate solutions. The system (7) has also collinear 6-point solutions and
together these are the only degenerate solutions that can occur. In order to understand
better these 6-point “pseudo-solutions”, let us assume that x1+x3+x5 = x2+x4+x6 = 0
and that all these points belong to the real axes. In light of the fact that x1 + x3 =

12

x2, x2 + x4 = x3, etc. we see that if 0 < x2 < x1 then x3 < 0 (Figure 6) which leads to
the following simple but important observation.

Observation 8. Suppose that x1, x2, . . . , x6 are collinear points which are also vertices
of a degenerate, aﬃne-regular hexagon, i.e. a conﬁguration obtained as a limit of a
convergent sequence of aﬃne-regular hexagons. Suppose that these points appear in
this order on a smooth, Jordan curve Γ, i.e. xj = f (tj) where t1 ≺ t2 ≺ . . . ≺ t6 ≺ t1.
Then the order of the appearance of these points on the line (in any direction) is a
non-trivial permutation of indices 1, 2, . . . , 6 diﬀerent from a cyclic permutation.

x1x2x3x4 x5 x6

Figure 6: A degenerate, aﬃne-regular hexagon.

6.1 Compactiﬁed conﬁguration space and the test maps

Let U ′ ∼= U 3
1 ⊕ U2, where U1 ∼= U2 ∼= R2, be the preliminary test space deﬁned as the
total target space for the test maps α, β, γ and δ, described in (6). Since the ﬁrst three
maps are not independent α + β + γ = 0, let V := {(u, v, w) ∈ U 3
1 | u + v + w = 0} and
let the actual “test space” be the direct sum U = V ⊕ U2 ⊂ U ′. Let F : (S1)6 → (R2)6

be the map induced by the embedding f : S1 → R2 and Φ : (S1)6 → U the “test map”
where Φ(t) := (α(F (t)), β(F (t)), γ(F (t))) ⊕ (δ(F (t))). Finally, let Φ0 : S1(6) → U be
the restriction of Φ on the conﬁguration space S1(6).
The next step, as in Section 5.2, is a rescaling of the map Φ0 in order to make
it suitable for an extension on the compactiﬁed conﬁguration space S1[6]. As before
(Section 5.2) let η : S1(6) → R+ be the map evaluating the “circular diameter” of a
conﬁguration t1 ≺ t2 ≺ . . . ≺ t6 ∈ S1(6) and ξ := η−1. Let Φ
′ := ξ · Φ be the rescaled
version of the map Φ and Φ
′
0 its restriction on S1(6).
The proof of the following proposition is similar to the proof of Proposition 6 so we
omit most of the details.

Proposition 9. The Z/6-equivariant map Φ
′
0 : S1(6) → U can be extended to a Z/6-
equivariant map Ψ : S1[6] → U such that Ψ(x) ̸= 0 for each x ∈ S1[6] \ S1(6) ∼=
S1 × ∂W6. Moreover, the Z/6-equivariant homotopy class of the restriction Ψ∂ : S1 ×
∂W6 → U \ {0} does not depend on the (counterclockwise) embedding f : S1 → R2.

Proof: (outline) In order to show that Ψ has no zeros on the boundary S1 × ∂W6
we have to show that “inﬁnitesimal degenerate hexagons” cannot appear as zeros of

13

the map Ψ : S1[6] → U. Indeed, this is ruled out by the Observation 8. The rest of
Proposition 9 is established by the arguments already used in the proof of Proposition 6
so we omit the details. □

6.2 The obstruction and its evaluation

As in Section 5.3, there arises an extension problem

S1 × ∂(W6)) Ψ∂
−−−→ S5


↓ 

↓∼=

S1 × W6 ?
−−−→ S5
 (8)

with the corresponding obstruction living in the group

H 6
Z/6((S1 × W6), S1 × ∂(W6)); Z)) ∼= H Z/6
0 ((S1 × W6) \ S1 × ∂(W6)); Z)) ∼= ZZ/6 ∼= Z/2.

As in Section 5.3 we evaluate the obstruction by choosing a conveniently “generic”
curve Γ ⊂ R2 and counting the number of aﬃne-regular hexagons inscribed in this
curve. A

B Cx
0
1 x
0
2
 x
0
3

x
0
4x
0
5

x
0
6
 Figure 7:

Let Γ be the boundary of a triangle (Figure 7). In order to make it a smooth curve
one is allowed to round its corners, however this will not aﬀect the calculations.
As it is clear from the picture there is only one aﬃne-regular hexagon inscribed
in this curve. It remains to be shown, as in Section 5.4, that a neighborhood of this
hexagon is mapped by the test map to a neighborhood of 0, i.e. that 0 is a regular
point of the test map Ψ.
Assume that x1, x2, . . . , x6 are local coordinates (on the conﬁguration space Γ(6) ∼=
S1(6)), in the neighborhood of the hexagon depicted in Figure 7. More precisely x1
is a point in the neighborhood of x
0
1, constrained to move only on the BC side of the
triangle, similarly x2, . . . , x6 are perturbations of respective points x
0
2, . . . , x
0
6 allowed
to move only on the boundary of the triangle.
It follows, since the function γ can be expressed in terms of α and β, that we
have to compute and establish the non-triviality of the Jacobian J of the map x =
(x1, x2, . . . , x6) ↦→ (α(x), β(x), δ(x)), evaluated at the point (x
0
1, . . . , x
0
6).

14

By inspection, and up to some rescaling of vectors −→
AB, −−→
BC, −→
CA, the Jacobian
matrix is found to have the following form:

J =
 x1 x2 x3 x4 x5 x6

α −−→
BC −
−−→
BC 0 −→
CA −
−−→
AB 0

β 0 −−→
BC −
−→
CA 0 −−→
AB −−−→
−AB

δ −−→
BC −
−−→
BC −→
CA −
−→
CA −−→
AB −
−−→
AB
 (9)

Finally, by choosing −−→
BC, −→
CA and −→
AB to be respectively the column vectors of the
matrix [ 1 −1 0
0 1 −1
 ]

we obtain a matrix with the determinant equal to 3. This calculation conﬁrms that
the hexagon depicted in Figure 7 is indeed a non-degenerate solution of the system of
equations (7) which in turn implies that the obstruction to the extension problem (8)
is a non-trivial element of the group ZZ/6 ∼= Z/2. □

7 Hadwiger’s conjecture

Conjecture 10. ([Ha]) Every simple closed curve in the Euclidean 3-space contains
four distinct points which are the vertices of a parallelogram.

Relying on the same method as in the previous sections we establish a stronger
statement (at least for C 1-smooth curves) that this parallelogram can be claimed to
have all sides pairwise equal i.e. to be a rhombus. As it turned out this theorem was
already established by Makeev in [Mak] whose initial motivation was the question of
inscribing equilateral polygonal lines in space curves.

Theorem 11. ([Mak]) Every C 1-smooth simple closed curve Γ immersed in the Eu-
clidean 3-space contains the vertices of a rhombus.

Proof: By assumption the curve Γ ⊂ R3 admits a C 1-parametrization. In other words
it can be parameterized by an injective C 1-mapping ϕ : S1 → R3 such that the tangent
vector dϕ/dt is nowhere zero, continuous function of t.
As before S1(4) is the conﬁguration space of cyclically ordered four-tuples of distinct
points on the circle. Given a point (t1 ≺ t2 ≺ t3 ≺ t4) ∈ S1(4), let xi = ϕ(ti) for
i = 1, 2, 3, 4. Let Γ(4) := Image(Φ) where Φ : S1(4) → (R3)4 is the map induced by ϕ.
Deﬁne a test map F = Fϕ : S1(4) → R4 as the composition F := Ψ ◦ Φ where
Ψ = (Ψ1, Ψ2) : (R3)4 → R3 ⊕ R is described by equations:

Ψ1(x) = x1 − x2 + x3 − x4
Ψ2(x) = ∥x1 − x2∥ − ∥x2 − x3∥ + ∥x3 − x4∥ − ∥x4 − x1∥. (10)

15

For a given input x = (x1, x2, x3, x4) ∈ R4, the ﬁrst function Ψ1(x) describes a
point in R3 which is equal to 0 if and only if the mid-points of the diagonals of the
quadrilateral with the vertices x1, x2, x3, x4 coincide (i.e. if it is a parallelogram). If in
addition the second function Ψ2 is equal to 0, then such a parallelogram have all sides
equal (i.e. it is a rhombus). This shows that the rhombuses inscribed in the curve Γ
correspond to zeros of the test map F = Fϕ.
Let S1[4] ∼= S1×W4 be the Fulton-MacPherson compactiﬁcation of the conﬁguration
space S1(4). As in the previous sections one can extend, after some rescaling, the
function F to a function ˜F = ˜Fϕ : S1[4] → R4. More explicitly, if η(t) is the arc-length
diameter of the set t = {t1, t2, t3, t4} ⊂ S1 and ξ(t) := η(t)−1 then ˜F is the extension
of the map ξ · F : S1(4) → R4.
The group Z/4 acts on the conﬁguration space S1(4) by cyclic permutations and this
action could be extended to its compactiﬁcation S1[4]. Moreover, both the test map
Fϕ and its extension ˜Fϕ are Z/4-equivariant. The target space R4 ∼= U1 ⊕ U2 naturally
splits as the sum of a 3-dimensional and a 1-dimensional, real Z/4-representation.

Proposition 12. The restriction ˜F ∂
ϕ of the map ˜Fϕ on the boundary S1 × ∂(W4) of
S1[4] = S1 × W4 has no zeros. Moreover, the Z/4-equivariant homotopy class of the
restriction ˜F ∂
ϕ : S1 × ∂(W4) → R4 \ {0} depends neither on the curve Γ nor on its
C 1-parametrization ϕ.

Proof: Let ˜F 1
ϕ : S1 × ∂(W4) → U1 and ˜F 2
ϕ : S1 × ∂(W4) → U2 be the components of
the map ˜F ∂
ϕ = ( ˜F 1
ϕ, ˜F 2
ϕ) : S1 × ∂(W4) → U1 ⊕ U2 ∼= R4. By deﬁnition (equation (10))
˜F j
ϕ, j = 1, 2, is the extension of the map ξ · (Ψj ◦ Φ).
For the majority of the points q ∈ S1 × ∂(W4) already the function ˜F 1
ϕ is non-zero.
More precisely ˜F 1
ϕ(q) is zero only if q is a degenerate parallelogram i.e. if q ∈ S1×(I1∪I2)
where I1 = [(23)(41), (41)(23)] and I2 = [(12)(34), (34)(12)] are the corresponding
edges of the cyclohedron W4 depicted in Figure 1. If q ∈ I1 ∪ I2 then ˜F 2
ϕ(q) ̸= 0, which
completes the proof of the ﬁrst part of the proposition.

For the proof of the second part of the proposition let us begin with a simple
observation that the Z/4-equivariant homotopy class of ˜F ∂
ϕ does not depend on the
smooth reparameterization of the curve Γ. Indeed, such a reparametrization α : S1 →
S1 deﬁnes a nowhere zero vector ﬁeld on S1, which can be linearly contracted to the
zero vector ﬁeld. Hence, there is a smooth homotopy between ϕ and ϕ′ := ϕ ◦ α which
induces a Z/4-equivariant homotopy between ˜F ∂
ϕ and ˜F ∂
ϕ′. Similar argument can be
used in the case when two curves (knots) Γϕ and Γψ are in the same isotopy class, i.e.
if they represent the same knot.

For the general case let us suppose that ϕ and ψ are two C 1-smooth embeddings
(knots) of S1 in R3 which are not necessarily C 1-isotopic. A naive candidate for a
Z/4-equivariant homotopy between ˜F ∂
ϕ and ˜F ∂
ψ is the linear homotopy

G : S1[4] × [0, 1] → R4 (11)

deﬁned by G(q, t) = (G1(q, t), G2(q, t)) := (1 − t) ˜F ∂
ϕ + (1 − t) ˜F ∂
ψ .

16

Observation 1: The second component G2 of the linear homotopy is non-zero
on A = S1 × (I1 ∪ I2). Indeed, the signs of both ˜F 1
ϕ(q) and ˜F 1
ψ(q) (for q ∈ A)
are the same, since they depend solely on the labelling of the vertices of the
degenerate parallelogram q.

It follows from Observation 1 that it is suﬃcient to deﬁne a (nowhere zero) homotopy
G1(q, t) for q ∈ D := ∂S1[4] \ (S1 × (I1 ∪ I2)). If ¯F 1
ϕ, ¯F 1
ψ : D → S2 are the normal-
ized maps associated to ˜F 1
ϕ and ˜F 1
ψ, where by deﬁnition ¯F 1
ϕ(q) := ˜F 1
ϕ(q)/∥ ˜F 1
ϕ(q)∥ and
¯F 1
ψ(q) := ˜F 1
ψ(q)/∥ ˜F 1
ψ(q)∥, then it is suﬃcient to deﬁne a Z/4-equivariant homotopy
¯G1 : D × I → S2 between these two maps.

Observation 2: Both maps ¯F 1
ϕ, ¯F 1
ψ can be canonically and Z/4-equivariantly
factored through the space ˜F (S1, 2) deﬁned in Example 1 (Section 3). More pre-
cisely there exist a “universal” (Z/4 ↦→ Z/2)-equivariant map χ : D → ˜F (S1, 2)
and Z/2-equivariant maps α, β : ˜F (S1, 2) → S2 such that ¯F 1
ϕ = α ◦ χ and
¯F 1
ψ = β ◦ χ.
 (a) (b) (c)

1
 1 1
2 2 23 3
 3

4
 4
 4

Figure 8: The deﬁnition of the map χ.

The deﬁnition of the map χ is quite natural and motivated by the deﬁnition of the map
¯F 1
ϕ in the case when ϕ : S1 ֒→ R2 ⊂ R3 is essentially the identity map. Pictorially it is
described in Figure 8. Let q1 = (x1, x2, x3, x4) be a point in ∂S1[4]. Generic examples
are depicted in Figure 8 (where for simplicity xj is labelled by j).
Recall that a point ˜F (S1, 2) is either an ordered pair (x, y) of points in S1 or a pair
(z, u) where z ∈ S1 and u is a unit tangent vector in Tz(S1). If q = (x1, x2, x3, x4) is the
conﬁguration depicted in Figure 8 (c), then χ(q) := (x3, x4). If q is a point depicted in
Figure 8 (a), then χ(q) := (x1, x3). Finally if q is a point depicted in Figure 8 (b), then
χ(q) = (z, u) where z = x1 = x2 = x3 = x4 and u is the unit tangent vector pointing
in he same direction as the vector x1 − x2 + x3 − x4.

It is not diﬃcult to show that ˜F (S1, 2) is, as a Z/2-space, Z/2-homotopy equivalent
to the circle S1 with the antipodal action. The existence of the Z/4-homotopy ¯G1 :
D × I → S2 follows from Observation 2 and the fact that any two Z/2-maps α, β :
˜F (S1, 2) → S2 are Z/2-homotopic. □

17

Remark 13. The fact that the Z/4-equivariant homotopy class of the map ˜F ∂
ϕ is the
same, whether the curve Γ ⊂ R3 is knotted or not, illustrates the versatility of the
“cyclohedron approach” to the problem of ﬁnding polygonal pegs inscribed in space
curves. This should be compared to the planar case where any two (equally oriented)
embeddings are isotopic, hence the required homotopies can be constructed by more
direct methods.

7.1 Obstruction and its evaluation

Proof of Theorem 11 (cont.): Equipped with Proposition 12, we proceed as in the
earlier sections. The obstruction O for a Z/4-equivariant extension of the (homotopi-
cally unique) map ˜F ∂
ϕ : S1 × ∂W4 → R4 \ {0} to S1 × W4 lives in H 4
Z/4(S1[4], ∂S1[4]; Z),
cf. Section 5.3. The Poincar´e dual of this class belongs to the dual homology group
H Z/4
0 (S1[4]; Z ⊗ ǫ) and can be evaluated by a careful choice of the curve Γ.

Let us consider the curve Γ = Γ1 ∪ J obtained as the union of the non-closed curve
Γ1 = Im(ψ), where ψ : [0, 2π] → R3 is deﬁned by ψ(t) = (cos t, sin t, t), and the interval
J joining the endpoints (1, 0, 2π) and (1, 0, 0) of the curve Γ1. Γ is not a smooth curve
however, by smoothing the corners, we obtain a smooth curve Γ′ such that a rhombus
(x1, x2, x3, x3) is inscribed in Γ if and only if it is inscribed in Γ′. For this reason we
are allowed to use the test map associated to the curve Γ.
Let ϕ : [0, 4π] → R3 be the parametrization of Γ deﬁned by ϕ(t) = ψ(t) for
t ∈ [0, 2π] and ϕ(t) := (1, 0, 4π − t) for t ∈ [2π, 4π].
We will show that there is a precisely one rhombus inscribed in the curve Γ, i.e. a
point x = (x1, x2, x3, x4) ∈ Γ(4) such that Fϕ(x) = 0. Moreover, it will be shown that
the test map F = Fϕ is transverse to 0 ∈ R4, i.e. that 0 is a regular value of F .
The only way to have two chords with coinciding mid-points are if one chord has
the end-points (cos t, sin t, t) and (cos(t + π), sin(t + π), t + π) (and consequently the
mid-point (0, 0, t + π/2), where 0 ≤ t ≤ π), and the other chord has the end-points
(cos π, sin π, π) = (−1, 0, π) and (1, 0, 2t). Among the obtained parallelograms the only
rhombus is obtained when t = π/2.
Let us show that 0 is indeed a regular value of the test map F = Fϕ. The vertices
of the rhombus q = (x1, x2, x3, x4) inscribed in the curve Γ are:

x1 = (0, 1, π
2 ) x2 = (−1, 0, π)
x3 = (0, −1, 3π
2 ) x4 = (1, 0, π) (12)

The corresponding tangent vectors to the curve Γ at these points are:

˙x1 = (−1, 0, 1) ˙x2 = (0, −1, 1)
˙x3 = (1, 0, 1) ˙x4 = (0, 0, −1) (13)

By a slight abuse of language we can interpret { ˙xi}4
i=1 also as a frame of tangent
vectors at q = (x1, x2, x3, x4) ∈ Γ(4), i.e. as a basis of the tangent space Tq(Γ(4)). Let
us evaluate the rate of change of functions Ψ1 and Ψ2 at q ∈ Γ(4) ⊂ R4 in the directions

18

of vectors ˙xi, for i = 1, 2, 3, 4. By deﬁnition (equation (10)) Ψ1(x) = x1 − x2 + x3 − x4,
hence dΨ1( ˙x1) = ˙x1 = (−1, 0, 1) dΨ1( ˙x2) = − ˙x2 = (0, 1, −1)
dΨ1( ˙x3) = ˙x3 = (1, 0, 1) dΨ1( ˙x4) = − ˙x4 = (0, 0, 1). (14)

Let λ = √
2 + π2/4 be the length of the side of the rhombus q = (x1, x2, x3, x4). Since
by deﬁnition (equation (10))

Ψ2(x) = ∥x1 − x2∥ − ∥x2 − x3∥ + ∥x3 − x4∥ − ∥x4 − x1∥

we have

λ dΨ2( ˙x1) = ⟨x1 − x2, ˙x1⟩ − ⟨x1 − x4, ˙x1⟩ = ⟨x4 − x2, ˙x1⟩ = (2, 0, 0) · (−1, 0, 1) = −2
λ dΨ2( ˙x2) = ⟨x2 − x1, ˙x2⟩ − ⟨x2 − x3, ˙x2⟩ = ⟨x3 − x1, ˙x2⟩ = (0, −2, π) · (0, −1, 1) = 2 + π
λ dΨ2( ˙x3) = ⟨x3 − x4, ˙x3⟩ − ⟨x3 − x2, ˙x3⟩ = ⟨x2 − x4, ˙x3⟩ = (−2, 0, 0) · (1, 0, 1) = −2
λ dΨ2( ˙x4) = ⟨x4 − x3, ˙x4⟩ − ⟨x4 − x1, ˙x4⟩ = ⟨x1 − x3, ˙x4⟩ = (0, 2, −π) · (0, 0, −1) = π.

From here and equation (14) we conclude that the Jacobian dF , evaluated at the point
t = {t1 ≺ t2 ≺ t3 ≺ t4} parameterizing the rhombus q, is given by the matrix





 −1 0 1 0
0 1 0 0
1 −1 1 1
−2 2 + π −2 π
 





The determinant of this matrix is −(2π + 4) ̸= 0 which completes the proof that 0 is
a regular value of the test map F .
The conclusion is that there is a precisely one rhombus inscribed in the curve Γ
which is a regular value of the associated test map. This implies that the obstruction
element O is non-zero which completes the proof of Theorem 11. □

8 Concluding remarks and open problems

8.1 Relaxing the smoothness condition

The method of canonical compactiﬁcations was applied in Sections 2–7 to the problem
of inscribing the polygonal pegs in smooth curves. In this section we brieﬂy show how,
with minimal modiﬁcations, the same method can be extended and successfully applied
to the case of non-smooth curves satisfying some weaker, locally deﬁned, condition. As
emphasized in Section 2, the method of canonical compactiﬁcations builds on the “con-
ﬁguration space/test map”-scheme, and introduces two important modiﬁcations. The
ﬁrst modiﬁcation applies to the conﬁguration space S1(n) which is extended (compact-
iﬁed) to the canonical compactiﬁcation (FMASK -compactiﬁcation) S1[n]. Secondly,
the test map Φ : S1(n) → V , for an associated test space V , is modiﬁed to a new test
map Ψ : S1[n] → V . The local properties of the curve enter the stage essentially in the
following two ways.
 19

•1 The requirement that the Jordan curve is C 1-smooth is essentially used (Propo-
sitions 6, 9, and 12) in the deﬁnition of the modiﬁed test map Ψ : S1[n] → V .

•2 Local properties of the curve are used to guarantee that there are no “inﬁnitesimal
squares” inscribed in the curve which in turn guarantees that the test map Ψ has
no zeros on the remainder S1[n] \ S1(n) of the compactiﬁcation.

The second condition is quite natural and in one form or another it is present in
all known results in this area. The most general known conditions that rule out the
existence of inﬁnitesimal inscribed squares have been proposed by Stromquist [St]. At
present it is not clear how this type of condition can be avoided or at least considerably
weakened.
Here we focus on the ﬁrst condition •1 and show that in principle one should be
able to deﬁne the modiﬁed test map Ψ in all cases of interest, provided we are prepared
to use more general forms of canonical compactiﬁcations which include the FMASK -
compactiﬁcation as a special case. In other words one can always deﬁne the modiﬁed
test map Ψ : τ (S1(n)) → V , even if the curve Γ is not C 1-smooth, for a suitable
compactiﬁcation τ (S1(n)) ⩾ S1[n].

Deﬁnition 14. Let F [R2, n] be the canonical or FMASK-compactiﬁcation of the con-
ﬁguration space F (R2, n) of all labelled, n-tuples of distinct points in R2 (Deﬁni-
tion 3). For a given (oriented) Jordan curve Λ ⊂ R2 let Λ(n) be the collection of
all q = (q1, . . . , qn) ∈ F (R2, n) such that qi ∈ Λ for each i and the points qi appear on
Λ in the order which agrees with the chosen orientation on Λ. The canonical compact-
iﬁcation Λ[n] of Λ(n) is deﬁned as the closure of Λ(n) in F [R2, n].

The deﬁnition of Λ[n] is in agreement with the deﬁnition of S1[n] from Section 3
provided S1 is the standard unit circle in R2. Canonical compactiﬁcations Λ[n] for a
suitable Λ can be used as the source space for the test map Ψ. We illustrate the key
idea by giving some hints how the result about the square pegs inscribed in Jordan
curves can be established for piecewise smooth curves Γ.

Let Λm be a regular m-gon in R2 (oriented counterclockwise) and let Λm[n] be the
canonical compactiﬁcation of the conﬁguration space Λm(n). For each piecewise smooth
(oriented) Jordan curve Γ ⊂ R2, which has at most m non-smooth points, there exists
an (orientation preserving) homeomorphism f : Λm → Γ which is smooth (with df ̸= 0)
on each of the segments of Λm. Such a piecewise smooth homeomorphism induces a
continuous map F : Λm(n) → Γ(n) which extends to the map ˜F : Λm[n] → Γ[n] of
associated canonical compactiﬁcations.
Moreover, the primary test map Φ : Λm(n) → U deﬁned by the equation (3) in
Section 5, on multiplication by the rescaling factor η, can be extended to a test map
Ψ : Λm[n] → U. This is established essentially by the same argument already used in
the proof of Proposition 6. The rest of the argument is quite similar to the proof of
the smooth case and does not require new ideas.

20

8.2 Problems and conjectures

The following problem reﬂects our impression that the answer to the Hadwiger’s prob-
lem for smooth curves, given in Section 7, is somewhat exceptional. It seems quite
natural to expect that there should exist a space polygonal peg of some sort which
always appears in some knots while it is missing in some realizations of other knots.

Problem 15. Is there a genuine polygonal peg property that can distinguish knots?
In other words, is there a naturally deﬁned family F of polygonal pegs such that for
some knot type N1 knots K ∈ N1 always exhibit (grip) a polygonal peg from the class
F while for some other knot type N2 there is a representative L ∈ N2 which does not
have this property.

If we stretch somewhat the concept of a “naturally deﬁned family” of polygonal
pegs by allowing families F that are purely non-metric in the sense that a polygonal
peg P belongs to F if and only if it satisﬁes a condition based on (co)incidences of
associated points and lines, then there is a very interesting example showing that the
answer to Problem 15 should be aﬃrmative. Indeed, as shown in [Pan] for generic
polygonal knots and in [Kup] for tame knots (see also [MM]), quadrisecant lines are
always present in nontrivial knots. On the other hand they obviously may be absent
in some realization of the unknot. Moreover, it was shown in [BSCS] that a weighted
sum of quadrisecants is a genuine knot invariant (the second coeﬃcient of the Conway
polynomial). All this serves as a motivation for the following bold conjecture.

Conjecture 16. Polygonal pegs detect all ﬁnite type invariants.

Conjecture 16 looks quite natural, however there is an opposite point of view which
deserves to be explored. Suppose that the existence of a polygonal peg in a knot is
established by the CS/TM -scheme, in the spirit of Sections 6 and 7. The associated test
map incorporates a description of the polygonal peg in terms of its characteristic metric
and/or coincidence properties. For example in the test map (10) for the Hadwiger’s
problem (Section 7) the ﬁrst equation tests the coincidence of mid-points of diagonals,
while the second equation records a pure metric property of a rhombus.
Suppose that a special test map for a concrete polygonal peg can be designed so
that it uses only the metric properties of the peg. The reader is referred to [Mak] and
[Mat], Chapter III, for examples of such polygonal pegs.
Given a smooth knot f : S1 → R3, one can pull back the metric from the ambient
space R3 to a metric on S1 and express the original polygonal peg problem as a question
about the existence of a peg in S1, relative to this metric. The punch line is that if a
polygonal peg problem allows a purely metric test map then, in light of the fact that
any two metrics on S1 are homotopic, the associated obstructions should be the same
(cf. Remark 13). As a consequence such a polygonal peg problem cannot detect a knot.

Acknowledgement: It is a real pleasure to acknowledge valuable comments and
remarks by Benjamin Matschke, Igor Pak, and Dev Sinha, as well as the hospitality of
the Technical University in Berlin (Discrete Geometry Group).

21

References

[A-S] S. Axelrod and I. Singer. Chern-Simons perturbation theory II. Jour. Diﬀ.
Geom. 39 (1994), no. 1, 173-213.

[B-T] R. Bott and C. Taubes. On the self-linking of knots. J. Math. Phys. 35 (1994),
no. 10, 5247-5287.

[BSCS] R. Budney, K. Scannell, J. Conant, and D. Sinha. New perspectives on self
linking. Advances in Mathematics, Vol. 191 No 1 (2005), 78-113.

[Die] T. tom Dieck, Transformation Groups, De Gruyter studies in mathematics vol.
8, Berlin 1987.

[Em] A. Emch. Some properties of closed convex curves in the plane. Amer. J. Math.,
35 (1913), 407–412.

[E] R. Engelking. General Topology. PWN, Warszawa 1977.

[F-M] W. Fulton and R. MacPherson. Compactiﬁcation of conﬁguration spaces. Ann.
of Math. 139 (1994), 183-225.

[Gri] H.B. Griﬃths. The topology of square pegs in round holes. Proc. London Math.
Soc. 62 (1991), 647-672.

[Gr¨u] B. Gr¨unbaum. Arrangements and spreads. AMS, Providence, RI, 1972.

[Gug] H. Guggenheimer. Finite sets on curves and surfaces. Israel J. Math. 3 (1965),
104-112.

[Ha] H. Hadwiger, Ungel¨oste Probleme Nr. 53. Elem. Math. 26 (1971), 58.

[HLM] H. Hadwiger, D.G. Larman, and P. Mani. Hyperrombs inscribed to convex
bodies. J. Combin. Theory Ser. B 24 (1978), 290–293.

[Heb] C.M. Hebbert. The inscribed and circumscribed squares of a quadrilateral and
their signiﬁcance in kinematic geometry. Ann. of Math. 16 (1914/15), 38-42.

[Jer] R.P. Jerrard. Inscribed squares in plane curves. Trans. AMS 98 (1961), 234-241.

[Kak] S. Kakeya. On the inscribed rectangles of a closed curvex curve. Tˆohoku Math.
J. 9 (1916), 163-166.

[Kup] G. Kuperberg. Quadrisecants of knots and links. J. Knot Theory Ramiﬁcations,
3 (1994) 4150.

[KlWa] V.L.Klee and S. Wagon. Old and new unsolved problems in plane geometry and
number theory. MAA, Washington, DC, 1991.

22

[Ko] M. Kontsevich. Operads and motives in deformation quantization. Lett. Math.
Phys. 48 (1999), 35-72.

[Mar] M. Markl. Simplex, associahedron, and cyclohedron. Higher Homotopy Struc-
tures in Topology and Mathematical Physics, Contemporary Math., vol. 227,
Amer. Math. Soc., 1999, pp. 235–265.

[MSS] M. Markl, S. Shnider, and J. Stasheﬀ. Operads in Algebra, Topology and Physics,
Math. Surveys and Monographs 96, Amer. math. Soc., 2002.

[Mak] V.V. Makeev. Quadrangles inscribed in a closed curve and the vertices of a
curve, J. Math. Sci. (N. Y.), Vol. 131, No. 1, 2005. Translated from Zap.
Nauchn. Sem. S.-Peterburg. Otdel. Mat. Inst. Steklov. (POMI)).

[Mat] B. Matschke. Equivariant Topologu and Applications, Diploma Thesis,
TU Berlin, September 2008, http://www.math.tu-berlin.de/~matschke/
DiplomaThesis.pdf.

[MM] H.R. Morton, D.M.Q. Mond. Closed curves with no quadrisecants. Topology 21
(1982) 235243.

[Pa08] I. Pak. The discrete square peg problem, arXiv:0804.0657v1 [math.MG] 4 Apr
2008.

[Pak] I. Pak. Lectures on Discrete and Polyhedral Geometry, book in preparation,
http://www.math.umn.edu/~pak/book.htm.

[Pan] E. Pannwitz. Eine elementargeometrische Eigenschaft von Verschlingungen und
Knoten. Math. Ann. 108 (1933) 629672.

[Si] D. Sinha. Manifold-theoretic compactiﬁcations of conﬁguration spaces.
math.GT/0306385, 2003.

[Shn] L.G. Shnirel’man. On some geometric properties of closed curves (in Russian).
Uspehi Matem. Nauk 10 (1944), 34–44; available at http://tinyurl.com/
28gsy3.

[St] W. Stromquist. Inscribed squares and square-like quadrilaterals in closed curves.
Mathematika 36 (1989), 187-197.

[ˇZ96] R. ˇZivaljevi´c. User’s guide to equivariant methods in combinatorics. Publi-
cations de l’Institut Mathematique (Beograd), 59(73), 114–130, 1996.

[ˇZ98] R. ˇZivaljevi´c. User’s guide to equivariant methods in combinatorics II. Publi-
cations de l’Institut Mathematique (Beograd), 64(78) 1998, 107–132.

[ˇZ04] R.T. ˇZivaljevi´c. Topological methods. Chapter 14 in Handbook of Discrete
and Computational Geometry, J.E. Goodman, J. O’Rourke, eds, Chapman &
Hall/CRC 2004, 305 – 330.
 23
