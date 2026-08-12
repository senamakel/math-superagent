<!-- source: https://arxiv.org/pdf/2304.14239 | converted from PDF -->

The Best Ways to Slice a Polytope

Marie-Charlotte Brandenburg, Jes´us A. De Loera, and Chiara Meroni

Dedicated to G¨unter M. Ziegler on the occasion of his 60 th birthday.

Abstract

We study the structure of the set of all possible aﬃne hyperplane sections of a convex
polytope. We present two diﬀerent cell decompositions of this set, induced by hyperplane
arrangements. Using our decomposition, we bound the number of possible combinatorial
types of sections and craft algorithms that compute optimal sections of the polytope
according to various combinatorial and metric criteria, including sections that maximize
the number of k-dimensional faces, maximize the volume, and maximize the integral of a
polynomial. Our optimization algorithms run in polynomial time in ﬁxed dimension, but
the same problems show hardness otherwise. Our tools can be extended to intersection
with halfspaces and projections onto hyperplanes. Finally, we present several experiments
illustrating our theorems and algorithms on famous polytopes.

1 Introduction

What is the best way to slice a 3-dimensional permutahedron? Figure 1 shows three of many
possible “best slices”. In this article we give a ﬁnite description of all aﬃne hyperplane
sections of an arbitrary polytope, called slices, and explain how to compute the optimal ones.
Our methods apply also to the investigation of the number of combinatorial types of slices.

(a) aﬃne section of maximal
volume (unique up to symmetry) (b) central section of minimal
volume (unique up to symmetry) (c) aﬃne section with maximal
number of vertices

Figure 1: Three optimal sections of the permutahedron, the convex hull of per-
mutations of (1, 2, 3, 4), shown in pink. See Example 5.1.

MSC classes: 52B55, 52C35, 52A38, 52A40, 52B11, 90C27, 52C45, 14P10.
Keywords: polytopes, hyperplane sections, hyperplane arrangements, optimal slices, volume, integration over
polyhedral regions, combinatorial types of polytopes, extremal problems on polytopes.

1arXiv:2304.14239v1  [math.CO]  27 Apr 2023
Sections or slices of convex bodies have been the focus of many researchers. To mention
just a few highlights, a variety of problems from number theory can be rephrased as questions
about volumes of sections or projections of convex bodies. For example, the sharp version
of Siegel’s Lemma is equivalent to an estimate for the minimum volume of a central slice (of
arbitrary dimension) of a unit cube [Kol05; Vaa79]. Similarly, the search for maximal volume
slices of cubes, cross-polytopes, simplices and other convex bodies comes from applications in
functional analysis and probability [Bal86; Bal89; K¨on21; MP88; Pou22; Web96]. Moreover,
the research around the famous Busemann-Petty problem and Bourgain’s slicing conjecture
relates the volume of a convex body to the volume of its sections by hyperplanes through
the origin [Gar06; GKZ23; KL22; Kla23; KM22; NT22]. Slices also play an important role
in geometric tomography and inverse moment problems for convex sets (see [Gar06, Chapter
8] and [GLPR12; KS21; Wal68]). From a discrete point of view, the combinatorial analysis
of hyperplane sections of polytopes, specially for polyhedral norm balls, has applications in
algebraic and enumerative combinatorics [ASVM21; CL91; FMGN97; Kho06; Law79; PP15].

Our contributions. The present paper addresses the fundamental question in computational
convexity of ﬁnding optimal or extremal hyperplane sections of a polytope. Most work has
concentrated on maximizing the volume of central hyperplane sections, while aﬃne sections
have been less studied and mostly for norm balls [K¨on21; LT20; MSZZ13; NT22; Pou22]. Our
results apply to both cases and seek to do research for more polytopes.
Our ﬁrst main contribution describes two diﬀerent ways to parametrize all aﬃne hyper-
plane sections of a polytope.

Theorem 1.1. Given a polytope P ⊂ Rd, there exist two diﬀerent parametric decompositions
of the space of all aﬃne hyperplanes in Rd into ﬁnitely many cells, called slicing chambers.
Each decomposition is organized by a pair (R, C) of arrangements (cf. Table 1), where each
region of R deﬁnes a parametric hyperplane arrangement C. The following holds for slicing
chambers in both decompositions:

(i ) Two aﬃne hyperplanes H1, H2 belong to the same slicing chamber if and only if H1, H2
intersect the same set of edges of P . In particular, P ∩ H1 is combinatorially equivalent
to P ∩ H2 and they admit the same triangulations.

(ii ) For ﬁxed dimension d, the number of slicing chambers is bounded by a polynomial in
the number of vertices of P .

(iii ) Restricted to a ﬁxed slicing chamber, the integral ∫
P ∩H f (x) dx of any polynomial is a
rational function, which solely depends on the combinatorial information described in
(i ). In particular, this holds for the volume of P ∩ H.

We note the relevant prior work in the direction of Theorem 1.1. The central hyperplane
arrangement in Table 1 already appeared in the 1970’s in [JP78], for an algorithm which
ﬁnds a halfspace containing the maximum number of the points placed on the unit-sphere.
Here, the halfspaces are bounded by central hyperplanes containing the origin. Later, again
in a central hyperplane setting, Filliman presented a decomposition of the Grassmannian of
hyperplanes into cells, where rational function formulas for volumes of sections of central
hyperplanes hold [Fil92]. However, his formulas are not suitable for general aﬃne sections of
polytopes. More recently, [BBMS22] used one of the decompositions we present in this paper
to compute intersection bodies of polytopes. In contrast, our techniques extend earlier work

2

Hyperplane Arrangement Notation Proofs in Reference Object

⟲ central arrangement C⟲ Subsection 2.1 intersection body

cocircuit arrangement R⟲ Subsection 3.1 oriented matroid

↑ parallel arrangement Cu
↑ Subsection 2.2 ﬁber polytope

sweep arrangement R↑ Subsection 3.2 sweep polytope

Table 1: An overview of the two pairs of hyperplane arrangements in this paper.

and are valid for all aﬃne sections. Using the structure of Theorem 1.1, we obtain formulas
for the integral of polynomials (and hence the volume) over hyperplane sections or halfspace
sections that are nonsingular rational functions in each slicing chamber. Our formulas rely
on the integration formulas from [BBDL+11; LA01].
The slicing chambers are nicely organized. Each row of Table 1 points to the section which
explains how to build them. Our ﬁrst slicing chamber decomposition is organized in terms of
the cocircuit arrangement generated by all hyperplanes spanned by sets of d − 1 vertices of P .
For each region of the cocircuit arrangement we identify a vector t that we use to translate
P , and from it we obtain a new central hyperplane for each vertex v + t of the translated
polytope P + t. This ﬁrst approach was used in the study of intersection bodies of polytopes
[BM23]. The second slicing chamber decomposition is organized diﬀerently. This time we
consider the regions of the sweep arrangement, dual to the sweep polytope [PP21]. Each point
u in a region of the sweep arrangement identiﬁes a direction. We then decompose P into
blocks deﬁned by translations of u⊥, while maintaining the combinatorics. These slabs are
our second type of slicing chambers. They are the same pieces used to compute the monotone
path polytope of P [BKS94], a special instance of ﬁber polytopes [BS92].
There are many applications of Theorem 1.1. Regarding combinatorial applications, we
can use slicing chambers to bound the number of combinatorial types of slices. This is an
interesting but hard problem. For instance, we do not even know all combinatorial types of
sections for regular cubes of dimension greater than ﬁve [FMGN97; Law79]. For each slicing
chamber of both our arrangements the combinatorial type of hyperplane sections is ﬁxed.
Thus, as a second main contribution, we recover an upper bound on the number of diﬀerent
combinatorial types of sections by aﬃne hyperplanes of the polytope P .

Theorem 1.2. For d-dimensional polytopes with n vertices, an upper bound on the number
of combinatorial types of hyperplane sections is O(n2d+12d).

We stress that using Theorem 1.1 we can compute not only a bound for the exact number
of combinatorial types of slices, but we also get an algorithm to list them for speciﬁc polytopes.
Our third main contribution, which relies again on Theorem 1.1, is a family of algorithms to
ﬁnd optimal aﬃne hyperplane sections, halfspace sections, and projections of polytopes.

Theorem 1.3. Let P ⊂ Rd be a polytope and f (x) a polynomial in Q[x1, . . . , xd]. Denote by
fk(P ) the number of k-dimensional faces of P and let wk+1 be a weight function deﬁned on
all (k + 1)-dimensional faces F of P . Let H be an aﬃne hyperplane, H +
0 denote a halfspace
deﬁned by a central hyperplane, and πH denote the projection of P in the direction orthogonal
to H. We give algorithms to ﬁnd an optimal solution for the following problems:

3

(i ) (section of maximum volume/integral) max
H⊂Rd vol(P ∩ H), max
H⊂Rd
 ∫

P ∩H f (x) dx.

(ii ) (optimal number of k-dimensional faces) max
H⊂Rd fk(P ∩ H), max
H +
0 ⊂Rd fk(P ∩ H +
0 ).

(iii ) (optimal weighted k-dimensional faces) max
H⊂Rd ∑

F ⊂P
F ∩H̸=∅
 wk+1(F ), min
H⊂Rd ∑

F ⊂P
F ∩H̸=∅
 wk+1(F ).

(iv ) (central halfspace of optimal integral) max
H +
0 ⊂Rd
 ∫

P ∩H +
0 f (x) dx, min
H +
0 ⊂Rd
 ∫

P ∩H +
0 f (x) dx.

(v ) (projections of optimal integral) max
H⊂Rd
 ∫

πH (P ) f (x) dx, min
H⊂Rd
 ∫

πH (P ) f (x) dx.

If P is a rational polytope and the dimension d is ﬁxed, then all these problems can be solved
in polynomial time.

As the number of items in Theorem 1.3 suggests, there are many possible applications of
Theorem 1.1, both for combinatorial as well as metric criteria. Maximal combinatorial slices
of polytopes are of interest in the context of algebraic and topological combinatorics. For
instance, a variation of the upper bound theorem for polytopes is to ﬁnd an upper bound for
f -vectors of slices of a polytope. Khovanskii investigated this problem and asked to compare
the h-vector of a section of the polytope by a generic aﬃne plane of dimension l and the
h-vector of the original polytope [Kho06, Section 7]. The volume of special slices of the
permutahedron ﬁxed by a permutation was analyzed in [ASVM21], and it turns out to agree
with the slice depicted in Figure 1b for certain cases.
Optimal combinatorial halfspace sections in computational geometry have been studied
for the maximization of the number of vertices on the sphere [JP78]. Moreover, there are
interesting applications regarding optimization of volumes and integrals of hyperplane sections
(e.g., moments [GLPR12; KS21]). It is very diﬃcult to ﬁnd the slices which have maximal
or minimal (through a given point) volume, even for most basic polytopes. For instance, the
aﬃne hyperplane section of maximum volume has been identiﬁed for the d-dimensional cube
[Bal86] and the cross-polytope [Kol05; MP88]; an analogous result for the simplex concerns
hyperplanes through the centroid [Web96]. We hope our algorithms will add new information.
Our fourth main contribution is experimental. As indicated in Theorem 1.3, our algo-
rithms work well for many optimality criteria, both concerning combinatorial and metric
properties. Applying the algorithm from Theorem 1.3 we computed the optimal slices of
famous polytopes in low dimensions, such as the Platonic solids, the permutahedron, and the
cross-polytope. This is an interesting result, since very little is known about optimal slices or
combinatorial types of speciﬁc polytopes [ASVM21; Bal86; CF86; Law79; NT22].
Overview: We begin in Subsection 2.1 by reviewing central hyperplane sections, and show
that the integral of a polynomial over all such sections is a piecewise rational function. In
Subsection 2.2 we show the analogue for parallel sections in a ﬁxed direction, and for orthog-
onal projections in Subsection 2.3. We merge these results in Section 3 to arbitrary aﬃne
hyperplane sections. The proofs of Theorems 1.1 and 1.2 are the main content of Section 3.
Algorithmic results are proved in Section 4. The proof of Theorem 1.3 is in Subsection 4.1.
While our algorithm runs in polynomial time for rational polytopes and polynomials in ﬁxed

4

dimension, the problems are hard in non-ﬁxed dimension (see Subsection 4.2). We close with
our experimental results in Section 5. We provide the maximal volume slices for all Platonic
solids, we investigate the 3-dimensional permutahedron for diﬀerent optimality criteria, and
we present lists of all combinatorial types of slices of the cross-polytope of dimensions 4 and
5. In this paper we use notions from polyhedral combinatorics and computational convex
geometry (see [GK94a; GK94b; GK97; Gr¨u67; Zie95]).

2 Sections and Projections

We begin our study of hyperplane sections and projections of a polytope. We analyze two
families of hyperplane sections: rotational and translational ones. By rotational or central
slices we mean hyperplanes that pass through a common point, which we assume to be the
origin. On the other hand, translational or parallel slices are parallel aﬃne hyperplane sections
with a common normal vector. These two points of view mirror two standard constructions
in convex geometry, namely intersection bodies and monotone path polytopes, respectively.
In both settings, the combinatorial type of the hyperplane section P ∩ H is governed by a
hyperplane arrangement C, which is either central or parallel. In the open chambers of the
hyperplane arrangements, one can then integrate polynomials over the slices parametrically,
as rational functions. This is the main result of this section, stated in Theorems 2.5 and 2.12.
A similar situation arises when looking at projections. We describe the associated hyperplane
arrangement, exploiting the duality with intersections, and prove an analogous result for the
integral over the projections in Theorem 2.18. Notice that we state our theorems for full-
dimensional polytopes. Analogous results can be stated and proved for lower-dimensional
polytopes by considering them inside their aﬃne span.

2.1 Rotational slices

We discuss now rotational slices of a ﬁxed polytope P ⊂ Rd which are obtained by hyperplanes
passing through the origin with normal vector u ∈ Sd−1. We show that given a polynomial
f , the integral of f over these sections is a piecewise rational function in variables u1, . . . , ud.
More speciﬁcally, the hyperplanes we consider in this section are of the form

{x ∈ Rd | ⟨u, x⟩ = 0}, where u ∈ Sd−1.

Understanding the volume of central hyperplane sections is a crucial step in the construction
of the intersection body of P [Lut88]. Indeed, in this section we make use of results from
[BBMS22], which studies intersection bodies of polytopes. A key argument is the existence
of a central hyperplane arrangement, as follows.

Lemma 2.1 ([BBMS22, Lemma 2.4]). Let P be a full-dimensional polytope in Rd and consider
the central hyperplane arrangement

C⟲(P ) = {v⊥ | v is a vertex of P and not the origin},

where v⊥ = {x ∈ Rd | ⟨x, v⟩ = 0} denotes the central hyperplane with normal vector v.
The maximal open chambers C of C⟲(P ) satisfy the following property: For all x ∈ C, the
hyperplane x⊥ intersects a ﬁxed set of edges of P . In particular, the polytopes Q = P ∩ x⊥

are of the same combinatorial type for all x ∈ C.

5

A (maximal, open) slicing chamber, or simply chamber, of C⟲(P ) is a connected component
of Rd \ C⟲(P ). In order to simplify the notation, we write C ⊂ C⟲(P ) when C is a maximal
chamber of the hyperplane arrangement C⟲(P ). We illustrate the above statement on a 2-
dimensional example. This will serve as a running example which we develop throughout the
article to illustrate the main concepts and constructions.

Example 2.2. Consider the pentagon P = conv((−1, −1), (1, −1), (1, 1), (0, 2), (−1, 1)) ⊂ R2.
Any generic hyperplane through the origin intersects P in a pair of edges of P . There are 6
diﬀerent such pairs, and the normal vectors of all hyperplanes intersecting a ﬁxed pair forms
a maximal open chamber of the hyperplane arrangement

C⟲(P ) = (1, 1)
⊥ ∪ (1, −1)
⊥ ∪ (0, 2)
⊥,

as depicted in Figure 2, left. This hyperplane arrangement only consists of three distinct
hyperplanes, since (−1, −1)⊥ = (1, 1)⊥ and (1, −1)⊥ = (−1, 1)⊥. An arrangement with six
distinct hyperplanes is obtained, e.g., for P +t with t = −( 1
3 , 1
2 ), in Figure 2, right. ⋄

Figure 2: Left: The polytope P and the central hyperplane arrangement C⟲(P )
from Example 2.2. Right: P + t and C⟲(P + t) for t = −( 1
3 , 1
2 ).

We are interested in integrating polynomials over the hyperplane sections of the polytope.
This is a generalization of a volume computation, namely the integral of the constant function
1. For this purpose, we will need the following lemma which provides a recipe to eﬃciently
integrate powers of linear forms over simplices via rational function formulas.

Lemma 2.3 ([LA01, Theorem 2.1],[BBDL+11, Remark 9]). Let ∆ = conv(s1, . . . , sn) ⊂ Rd

be a simplex, let p ∈ Rd and D ∈ Z≥0. Then, writing |k| = ∑n
j=1 kj, we have
∫

∆⟨p, x⟩
D dx = (n − 1)! vol(∆) D!
(D + n − 1)!
 ∑

k∈Zn
≥0,
|k|=D
 ⟨p, s1⟩k1 · · · ⟨p, sn⟩kn.

Additionally, we will make use of the following result about the decomposition of poly-
nomials into sums of powers of linear forms. Lemma 2.4 shows one way to express any
polynomial of degree D as a sum of Dth powers of linear forms. As a consequence, if we know
how to integrate powers of linear forms, we know how to integrate any polynomial.

Lemma 2.4 ([BBDL+11, Equation 13]). Any monomial can be written as a sum of powers
of linear forms of the same degree as follows:

xα1
1 xα2
2 · · · x
αd
d = 1
|α|!
 ∑

p∈Zd
≥0
p≤α
 (−1)
|α|−|p|(
α1
p1
 ) · · · (
αd
pd
 )(p1x1 + · · · + pdxd)|α|,

where |α| = α1 + · · · + αd and p ≤ α means that pi ≤ αi for all coordinates i ∈ [d].

6

We note that another formula for polynomial integration over simplices is described in
[Las21]. However, since the vertices of our simplices are parametrized by the normal vector
of the central hyperplane, this formula is not suitable in our setting.
We now prove the main result of this section. The proof of this result is an adaption for
integration of the proof of [BBMS22, Theorem 2.6], which deals with volume computation.

Theorem 2.5. Let P ⊂ Rd be a full-dimensional polytope, let f (x) = ∑
α cαxα be a polyno-
mial, and let C ⊂ Rd be a maximal open slicing chamber of the central hyperplane arrangement
C⟲(P ) from Lemma 2.1. Restricted to directions u ∈ C ∩ Sd−1, the integral ∫

P ∩u⊥ f (x) dx is
a rational function in variables u1, . . . , ud.

Proof. Let Q(u) = P ∩ u⊥ for some u ∈ C ∩ Sd−1 and ﬁx a triangulation T of Q(u) without
any additional vertices. By construction, the set of edges of P which intersect u⊥ are uniquely
determined by C, and thus the triangulation of P ∩ u⊥ can be chosen for all u ∈ C ∩ Sd−1.
Let v1(u), . . . , vn(u) be the vertices of Q(u) and let conv(ai, bi) be the corresponding edges
of P such that vi(u) ∈ conv(ai, bi). Given a simplex ∆ ∈ T with vertices vj1(u), . . . , vjd(u)
its volume can be computed as vol(∆) = 1
(d−1)! | det M∆(u)| where

M∆(u) =
 







vj2(u) − vj1(u)
vj2(u) − vj1(u)
...
vjd(u) − vj1(u)
u
 






 , vj(u) = ⟨bj, u⟩aj − ⟨aj, u⟩bj
⟨bj − aj, u⟩ ,

and for a ﬁxed region C, the sign of the determinant of M∆(u) is constant for all u ∈ C ∩Sd−1.
We now apply Lemma 2.4 to rewrite our polynomial f as a combination of powers of linear
forms, in order to then apply Lemma 2.3. For any x, we have that

f (x) = ∑

α
 cα
|α|!
 ∑

p∈Zd
≥0
p≤α
 (−1)
|α|−|p|(
α1
p1
 ) · · · (
αd
pd
 )
(p1x1 + · · · + pdxd)
|α|.

Hence, the integral of f over Q(u) can be computed exactly:
∫

Q(u)f (x) dx = ∑

α
 cα
|α|!
 ∑

p∈Z
d
≥0
p≤α
 (−1)|α|−|p|(α1
p1
 ) · · · (
αd
pd
 ) ∫

Q(u)⟨p, x⟩
|α| dx (1)

= ∑

α
 cα
|α|!
 ∑

p∈Z
d
≥0
p≤α
 (−1)|α|−|p|(α1
p1
 ) · · · (
αd
pd
 ) ∑

∆∈T
 ∫

∆⟨p, x⟩
|α| dx

= ∑

α
 cα
|α|!
 ∑

p∈Z
d
≥0
p≤α
 (−1)|α|−|p|(α1
p1
 ) · · · (
αd
pd
 ) ∑

∆∈T
 [

(d − 1)! vol(∆) |α|!
(|α| + d − 1)!

∑

k∈Z
d
≥0,
|k|=|α|
⟨p, vj1(u)⟩
k1 · · · ⟨p, vjd (u)⟩
kd ]

7

= ∑

∆∈T |det M∆(u)| ∑

α
 cα
(|α| + d − 1)!
 ∑

p∈Z
d
≥0
p≤α
 (−1)|α|−|p|(α1
p1
 ) · · · (
αd
pd
 )

∑

k∈Z
d
≥0,
|k|=|α|
⟨p, vj1(u)⟩
k1 · · · ⟨p, vjd (u)⟩
kd ,

which is a rational function in variables u1, . . . , ud.

Remark 2.6. For all hyperplane arrangements we encounter in this and the following sec-
tions we deﬁne chambers and regions as connected components of the complement of the
arrangement, and thus the chambers and regions are open and full-dimensional by deﬁnition.
All statements regarding the integration of a polynomial are stated solely for these open
full-dimensional polyhedra. However, since the rational functions do not have poles at the
boundary of the regions and chambers, we can extend these statements to the closures of
these polyhedra, which yields rational functions on the entire induced polyhedral complex.
Thus all statements also hold on these lower-dimensional faces: The integral is a rational
function, and these functions are specializations of the rational functions which are deﬁned
on the maximal polyhedra containing such a face.
Example 2.7. Continuing Example 2.2, we illustrate the statement of Theorem 2.5. We
compute the volume ∫
P ∩u⊥ 1 dx, the sum of the ﬁrst moments ∫

P ∩u⊥ x1 + x2 dx and the sum
of the second moments ∫

P ∩u⊥ x2
1 + x1x2 + x2 dx over all central sections of the pentagon P
from Example 2.2. As shown in Figure 3, each of the integrals is a rational function in u1, u2
along each of the chambers of the central hyperplane arrangement C⟲(P ). One can check
that the functions in two adjacent chambers agree along the common face, as explained in
Remark 2.6. We note that the fact that the volume is a factor of the latter two integrals is an
artefact of low dimension, where every section is a 1-dimensional simplex, and so no further
triangulation is needed. ⋄

2.2 Translational slices

In this section we analyze translational slices of a polytope P ⊂ Rd, which are obtained by
translates of a hyperplane with a ﬁxed normal vector u ∈ Sd−1. Similarly to Subsection 2.1,
we show that for a ﬁxed polynomial f the integral over these aﬃne sections is a univariate
polynomial. Concretely, ﬁx a vector u ∈ Sd−1 and consider the family of aﬃne hyperplanes

H(β) = {x ∈ Rd | ⟨u, x⟩ = β}

orthogonal to u, parametrized by β ∈ R. Parallel, or translational, slices arise naturally in
the context of monotone path polytopes, which are special instances of ﬁber polytopes [BS92].
Also in this case, there is a hyperplane arrangement, consisting of parallel hyperplanes, which
governs the combinatorial structure of the translational slices.

Lemma 2.8. Let P ⊂ Rd be a polytope and ﬁx a direction u ∈ Sd−1. Consider the aﬃne
hyperplane arrangement, made of parallel hyperplanes

Cu

↑ = {H(⟨u, v⟩) | v is a vertex of P }.

The maximal open chambers C of Cu
↑ (P ) satisfy the following property: For all H(β) ∈ C, the
hyperplanes H(β) intersects a ﬁxed set of edges of P . Moreover, the polytopes Q(β) = P ∩H(β)
are normally equivalent, i.e., they have the same normal fan.

8

2
u2

− 2
u2

− 3u1−u2
u1(u1−u2)

− 3u1+u2
u1(u1+u2) 3u1−u2
u1(u1−u2)

3u1+u2
u1(u1+u2)

∫
P ∩u⊥ 1 dx = vol(P ∩ u⊥)
 0

0

(u1+u2) vol(P ∩u⊥)
2u1

(u1−u2)2 vol(P ∩u⊥)
2u1(u1+u2) (u1+u2) vol(P ∩u⊥)
2u1

(u1−u2)2 vol(P ∩u⊥)
2u1(u1+u2)

∫
P ∩u⊥ x1 + x2 dx

(u2
1−u1u2
2+u2
2) vol(P ∩u⊥)
3u2
2

(u2
1−u1u2
2+u2
2) vol(P ∩u⊥)
3u2
2

g(u) vol(P ∩u⊥)
(u1−u2)2

g(u) vol(P ∩u⊥)
(u1+u2)2 g(u) vol(P ∩u⊥)
(u1−u2)2

g(u) vol(P ∩u⊥)
(u1+u2)2

∫

P ∩u⊥ x2
1 + x1x2 + x2
2 dx

Figure 3: The integrals of the sum of moments over central sections of the pen-
tagon, as described in Example 2.7, with g(u) = (3u2
1+u2
2)(u2
1−u1u2+u2
2)
3u2
1 .

Proof. Let C be a ﬁxed chamber of Cu
↑ and H(β) ∈ C. The hyperplane H(β) intersects an
edge conv(v1, v2) in its interior if and only if ⟨u, v1⟩ < β < ⟨u, v2⟩. Thus, the set of edges
intersected by H(β) is ﬁxed in each chamber C. Consequently, the set of intersected faces
of arbitrary dimension is ﬁxed along the open chamber C. Thus, the combinatorial type of
Q(β) is ﬁxed, and so is the combinatorial type of its normal fan. Note that any facet F of
P ∩ H(β) arises as intersection of a facet G of P with H(β), and the normal vector of F is a
projection of the normal vector of G onto H(β). Since projections are invariant under aﬃne
translations of H(β), all aﬃne sections within C are normally equivalent.

Remark 2.9. We note that the hyperplane arrangement Cu
↑ (P ) induces a partition of R1:

{⟨u, v⟩ | v is a vertex of P }.

Indeed, this partition and Cu
↑ (P ) are equivalent, as β can be uniquely determined from H(β),
when the normal vector u is ﬁxed, and vice versa. In the remaining of this article, we allow
ourselves to write β ∈ C instead of H(β) ∈ C for a chamber C of the parallel arrangement
Cu
↑ (P ), as we have chosen the convention in Lemma 2.8 purely for esthetic reasons. As already
pointed out in the rotational case, we will write C ⊂ Cu
↑ (P ) for the maximal chambers.

9

Remark 2.10. For generic u ∈ Sd−1, the linear functional ⟨u, ·⟩ induces an ordering v1, . . . , vn
on the vertices of P such that ⟨u, vi⟩ < ⟨u, vi+1⟩ for all i = 1, . . . , n − 1. By construction, a
chamber of Cu
↑ (P ) consists precisely of those parallel hyperplanes which are orthogonal to u
and separate vi from vi+1 for some i ∈ [n − 1].

Example 2.11. Recall the pentagon P from Example 2.2 with vertices

v1 = (−1, −1), v2 = (1, −1), v3 = (1, 1), v4 = (0, 2), v5 = (−1, 1).

For a generic direction u the hyperplane arrangement Cu
↑ (P ) induces six slicing chambers, four
of which have nonempty intersection with P . Figure 4 shows the arrangement for a non-generic
(left) and a generic (right) choice of u, namely for u = 1
2 (−1, −1) and u = 1√5 (1, 2). The

parallel hyperplane arrangement for the pentagon P and u = 1√5 (1, 2) induces the ordering
of the vertices v1, v2, v5, v3, v4. ⋄

u u

Figure 4: The parallel arrangement Cu
↑ for normal directions u = 1
2 (−1, −1) on
the left and u = 1√5 (1, 2) on the right.

We now prove the analogue of Theorem 2.5 for parallel aﬃne sections.

Theorem 2.12. Let P ⊂ Rd be a full-polytope, let f (x) = ∑
α cαxα be a polynomial, ﬁx
a normal direction u ∈ Sd−1 and let C ⊂ Rd be a maximal open chamber of the hyperplane
arrangement Cu
↑ (P ) from Lemma 2.8. Restricted to values β ∈ C, the integral ∫
P ∩H(β) f (x) dx
is a polynomial in the variable β.

Proof. This proof has the same structure as the proof of Theorem 2.5. The main diﬀerence
lies in the parametrization of the vertices of the sections of the polytope.
Let β ∈ C and Q(β) = H(β) ∩ P . Let v1(β), . . . , vn(β) denote the vertices of Q(β) and
let conv(ai, bi) be the edge of P such that vi(β) = conv(ai, bi) ∩ H(β). From

vi(β) = λai + (1 − λ)bi, ⟨u, vi(β)⟩ = β,

we obtain
 vi(β) = β
⟨u, bi − ai⟩ (bi − ai) + ⟨u, bi⟩ai − ⟨u, ai⟩bi
⟨u, bi − ai⟩ ,

which depends linearly on β. Let T be a triangulation of Q(β) which uses only the vertices
of Q(β). By construction of C this triangulation can be chosen equal for every β ∈ C. Let

10

vj1(β), . . . , vjd(β) denote the vertices of a simplex ∆ ∈ T , and let

M∆(β) =
 







vj2(β) − vj1(β)
vj2(β) − vj1(β)
...
vjd(β) − vj1(β)
u
 






 .

Repeating the computation of (1) in the proof of Theorem 2.5, ∫
P ∩H(β) f (x) dx equals

∑

∆∈T |det M∆(β)| ∑

α
 cα
(|α| + d − 1)!
 ∑

p∈Z
d
≥0
p≤α
(−1)|α|−|p|(α1
p1
 ) · · · (
αd
pd
 ) ∑

k∈Z
d
≥0,
|k|=|α|

⟨p, vj1(β)⟩
k1 · · · ⟨p, vjd (β)⟩kd ,

which is a polynomial in β, for β ∈ C.

Example 2.13. We continue Examples 2.2 and 2.11 by computing integrals of sums of
moments over parallel sections of the pentagon P , with respect to the normal direction
u = 1√
5 (1, 2). The polynomials describing the function ∫
P ∩H(β) f (x) dx for f (x) = 1,
f (x) = x1 + x2, and f (x) = x2
1 + x1x2 + x2
2 respectively, for each chamber in the arrangement,
are shown in Figure 5. ⋄

The above discussion has a discrete version, where instead of volumes or integrals we count
lattice points in the section. There are several discrete variants of well-known continuous
inequalities in convex geometry and Brunn-Minkowski theory [FH22]. While we are unable
to do optimization over discrete sections of polytopes, we obtain the following partial result.
We give give a sketch of the proof in Remark 2.15.

Theorem 2.14. The Ehrhart function Ehr(P ∩H(β)) that counts lattice points of dilations of
polytopes is a piecewise rational function in β. In ﬁxed dimension and for a rational polytope
P , these formulas can be computed in polynomial time.

Remark 2.15. Theorem 2.14 is a direct consequence of the theory of rational functions encod-
ing the lattice points of polyhedra [BP99]. Each lattice point is thought of as the exponent
vector of a monomial, turning the set of all lattice points in P into a Laurent polynomial
gP (x) = ∑
α∈P ∩Zd xα. This monomial sum can be written as a sum of rational functions

gP (x) = ∑

i∈I Ei xui

d∏

j=1
(1 − xvij ) ,

where I is an indexing set, Ei ∈ {1, −1}, and ui, vij ∈ Zd for all i and j. The formula above
coincides for polytopes with the same normal fan, which, by Lemma 3.7, is the case within
the chambers of Cu
↑ (P ). Moreover, assuming the dimension d is ﬁxed, the size of the sum is
polynomial in the input size.

Remark 2.16. In the setting of rotational slices, computing the number of lattice points in
the section P ∩ H is a much more diﬃcult problem than the translational case. This lies in
the fact that the polytopes P ∩ u⊥
1 and P ∩ u⊥
2 are not normally equivalent, even for ui in
the same chamber.
 11

5β+3
√5
2
 √5

−5β+7
√5
6
 −10β+8
√5
3

∫
P ∩H(β) 1 dx = vol(P ∩ H(β))
 (3 √
5β +1) vol(P ∩ H (β ))

4
 5β
2

(7 √
5β − 1) vol(P ∩ H (β ))

12

( √
5β +2) vol(P ∩ H (β ))

3

∫

P ∩H(β) x1 + x2 dx

(10β 2
+3 √
5β +3) vol(P ∩ H (β ))

4
 √
5(5β 2
+1)4

(50β 2
− 5 √
5β +13) vol(P ∩ H (β ))

36

2(10β 2
− 7 √
5β +14) vol(P ∩ H (β ))

9

∫

P ∩H(β) x2
1 + x1x2 + x2
2 dx

Figure 5: The integrals over the sum of moments over aﬃne sections of the
pentagon in direction 1√5 (1, 2), as described in Example 2.13.

2.3 Projections and polarity

The dual version of intersections is given by projections. It is therefore natural to wonder
if any of the results of the previous sections apply in this context. They actually do apply,
and involve hyperplane arrangements that we have already encountered. If central, rotating
sections are connected to the construction of intersection bodies, and parallel, translating
sections to monotone path polytopes, here we should keep in mind the concept of projection
bodies [Gar06, Chapter 4]. This is another construction coming from convex geometry and it
encodes in its support function the volume of all (d − 1)-dimensional projections of a given
convex body in Rd. In our setting, we denote by P ◦ the polar of P and we identify Rd with
its dual space, via the standard scalar product.

Lemma 2.17. Let P ⊂ Rd be a polytope containing the origin in its interior and let P ◦

be the polar of P . Consider the aﬃne hyperplane arrangement C⟲(P ◦). The maximal open
chambers C of C⟲(P ◦) satisfy the following property: For all u ∈ C, the projection πu(P ) has
as vertices the projections of a ﬁxed set of vertices of P . In particular, the polytopes πu(P )
are combinatorially equivalent.
 12

Proof. Let C be a maximal open chamber of C⟲(P ◦), and let u ∈ C. By polarity of projections
and intersections, we have that
 πu(P ) = (P ◦ ∩ u
⊥)◦ .

Since the combinatorial type of P ◦ ∩ u⊥ does not change when u ∈ C, the combinatorial type
of πu(P ) does not change as well. Moreover, the vertices of πu(P ) are the projection of those
vertices of P , whose corresponding facet F of P ◦ deﬁnes a facet F ∩ u⊥ of P ◦ ∩ u⊥.

Applying the same strategy as in the proofs of Theorems 2.5 and 2.12, we obtain an anal-
ogous result about the integral of a polynomial for projections of polytopes, which constitutes
the ﬁrst step towards the proof of Theorem 1.3 (v).

Theorem 2.18. Let P ⊂ Rd be a full-dimensional polytope, let f (x) = ∑
α cαxα be a poly-
nomial, and let C ⊂ Rd be a maximal open chamber of the hyperplane arrangement C⟲(P ◦) in
Lemma 2.17. Restricted to directions u ∈ C ∩Sd−1, the integral ∫

πu(P ) f (x) dx is a polynomial
in variables u1, . . . , ud.

Proof. Also in this case, the proof is a straightforward consequence of the proof of Theo-
rem 2.5, after determining the parametrization of the vertices of the projection.
Let Q(u) = πu(P ) for some u ∈ C. By construction, the vertices of P whose projections
are vertices of Q(u) are uniquely determined by C, and thus the triangulation T of πu(P )
can be chosen for all u ∈ C ∩ Sd−1. Let πu(v1), . . . , πu(vn) be the vertices of Q(u) and let

M∆(u) =
 







πu(vj2) − πu(vj1)
πu(vj3) − πu(vj1)
...
πu(vjd) − πu(vj1)
u
 






 , πu(vj) = vj − ⟨u, vj⟩u,

where πu(vj1), . . . , πu(vjd) are the vertices of ∆ ∈ T . Repeating the computation of (1), the
integral of f over Q(u) can be computed exactly as

∑

∆∈T|det M∆(u)| ∑

α
 cα
(|α| + d − 1)!
 ∑

p∈Z
d
≥0
p≤α
(−1)|α|−|p|(α1
p1
 ) · · · (
αd
pd
 ) ∑

k∈Z
d
≥0,
|k|=|α|

⟨p, πu(vj1)⟩
k1 · · · ⟨p, πu(vjd )⟩
kd

which is a polynomial in u1, . . . , ud, for u ∈ C ∩ Sd−1.

Remark 2.19. If D is the degree of f , then the degree of the polynomial ∫
Q(u) f (x) dx is at
most 2d(D + 1) − 1. When f is a constant then our function is the support function of a
zonotope, the projection body of P [Sch14, Section 10.9], and must therefore be linear in u.

Example 2.20. We continue Examples 2.2 and 2.13 and compute the volume of all projec-
tions of the pentagon P . The polynomials describing vol(πu(P )), for u ∈ S1, in each chamber
of the arrangement C⟲(P ◦) are shown in Figure 6. ⋄

There is also another possible approach, based on [Law91, pp. 260-261] and [Fil92, Theo-
rem 1], which is however more complicated. It involves again polarity, but of the hyperplane
sections of P . This alternative approach is also based on the fact that πu(P ) = (P ◦ ∩ u⊥)◦,

13

and there are formulas to compute the volume of the polar of a polytope from the polytope
itself. Lawrence formula is stated only for simple polytopes, but by Brion’s theorem and
signed cone decompositions methods [Bar02] we can obtain a more general formula which
holds for any polytope. The second formula holds for non-codegenerate polytopes, so in order
to apply it one should verify this property for all projections πu(P ). Because of these subtle
conditions of genericity, we prefer to use here the above approach of triangulating directly the
projection, which already implies a good bound on the complexity of associated optimization
problems, as we will discuss at the end of Subsection 4.1 when proving the complexity part
of Theorem 1.3 (v).
 2(u1 + u2)

−2(u1 + u2)
 3u1 + u2

−3u1 − u2

2(u2 − u1)
 2(u1 − u2)

−3u1 + u2
 3u1 − u2

Figure 6: The volume of all the projections πu(P ), for u ∈ S1, of the pentagon
P , as described in Example 2.20.

3 Merging the two types of slices

In Subsections 2.1 and 2.2 we parametrically computed the integral of a polynomial f over
central and parallel hyperplane sections of a polytope P . In this section, we generalize the
results to arbitrary aﬃne sections, based on the following observation. There are two natural
ways to consider all hyperplane sections. One can ﬁrst choose a point in Rd as a center and
then examine all (rotational) hyperplanes through that point; or one can ﬁrst ﬁx a direction
and examine all the aﬃne (parallel) hyperplanes orthogonal to it. In Subsection 3.1, we take
the ﬁrst point of view, generalizing the approach of central sections from Subsection 2.1. This
yields an aﬃne hyperplane arrangement R⟲(P ) in the space of translation vectors of P . On
the other hand, in the spirit of the second point of view on hyperplane sections, generalizing
the approach of parallel sections from Subsection 2.2 yields a central hyperplane arrangement
R↑(P ) in the space of normal vectors of aﬃne hyperplanes, as we discuss in Subsection 3.2.
Another standard procedure to turn central hyperplane sections into aﬃne ones uses
homogenization. Namely, embed the d-dimensional polytope P in Rd+1 inside the hyperplane
xd+1 = 1. Then all (d − 1)-dimensional slices of P can be obtained by hyperplanes through
the origin in Rd+1. However, since in this setting the polytope P is not full dimensional,
the parametric computation of the volume of the section would involve ﬁnding a parametric
orthonormal basis. This is not suitable for computations, where we prefer to stick to rational
data. For these reasons, we do not discuss this approach in more detail.

14

3.1 Translating the rotation

In Subsection 2.1 we ﬁxed a polytope P and considered hyperplanes through the origin with
normal vectors u ∈ Sd−1, yielding a central hyperplane arrangement C⟲(P ), in which each
maximal open chamber consists of normal vectors u such that the central hyperplane u⊥

intersects a ﬁxed set of edges of P . In this section we extend this construction, allowing to
vary the position of the origin by considering translations P + t.

Lemma 3.1 ([BM23, Lemma 3.2, Proposition 3.4]). Let P ⊂ Rd be a full-dimensional polytope
and let R be a maximal region of the aﬃne hyperplane arrangement

R⟲(P ) = {aﬀ(−v1, . . . , −vd) | v1, . . . , vd are aﬃnely independent vertices of P },

called the cocircuit arrangement. Then, the following holds:

(i ) For all t ∈ R, the central hyperplane arrangements C⟲(P + t) deﬁne the same realizable
oriented matroid χ. Moreover, the hyperplanes deﬁning a chamber C(t) of C⟲(P + t)
are parametrized linearly by t1, . . . , td.

(ii ) Let t, t′ ∈ R and let C(t) ⊂ C⟲(P + t), C(t′) ⊂ C⟲(P + t′) be maximal chambers such
that the topes (cocircuits) of χ corresponding to C(t), C(t′) agree. Then,

{e edge of P | (e + t) ∩ u⊥ ̸= ∅} = {e edge of P | (e + t′) ∩ (u′)
⊥ ̸= ∅}

for any u ∈ C(t), u′ ∈ C(t′). In words, u⊥ and (u′)⊥ intersect the same set of edges
(of P + t and P + t′, respectively).

We refer to R⟲(P ) as the cocircuit arrangement of P , and a region R is an open con-
nected component of Rd \ R⟲(P ). As before, in order to simplify the notation, we will write
R ⊂ R⟲(P ) for a region of the arrangement. Notice that we are dealing at the same time
with two distinct hyperplane arrangements: R⟲(P ) and C⟲(P ). The names of the arrange-
ments correspond to the names we use for their complement: the connected components of
Rd \ C⟲(P ), as deﬁned in Subsection 2.1, are called chambers, whereas the connected com-
ponents of Rd \ R⟲(P ) are called regions. Putting the two arrangements together, we can
parametrize all hyperplanes in Rd. A point t in a region of R⟲(P ) ﬁxes a translation of P
or, analogously, it ﬁxes the position of the origin with respect to the polytope. Then, the
chambers of C⟲(P + t) parametrize the hyperplanes through the chosen origin. When we
change t, we capture new hyperplane sections.

Example 3.2. We continue the Examples 2.2 and 2.7. The cocircuit arrangement R⟲(P )
consists of (5
2
) = 10 hyperplanes, subdividing R2 into 11 bounded and 26 unbounded regions,
as shown in Figure 7a. Let

R = {t ∈ R2 | ⟨
( −3
1 ) , t⟩ > −2, ⟨
( −1
−1 ) , t⟩ > 0, ⟨( 3
1 ) , t⟩ > −2, ⟨
( 1
−1 ) , t⟩ > 0, ⟨( 0
1 ) , t⟩ > −1}

be the pentagonal shaded region of R⟲(P ). Note that R contains the translation vector
t = −( 1
3 , 1
2 ) from Example 2.2. For all t ∈ R the central arrangement C⟲(P + t) deﬁnes
the same oriented matroid. In particular, all central hyperplane arrangements have the same
combinatorial structure, and are parametric in t1, t2, as shown in Figure 7b. Varying t
induces a rotation of the hyperplanes deﬁned by ⟨vi + t, x⟩ = 0, where vi are the vertices of
P . Note that the (strict) inequalities deﬁning R guarantee that under these rotations no two
hyperplanes in C⟲(P + t) collapse. ⋄

15

(a) The cocircuit arrangement R⟲(P ).
The region R is shaded in gray.
 ⟨v1 + t, x⟩ = 0

⟨v5 + t, x⟩ = 0

⟨v4 + t, x⟩ = 0
⟨v2 + t, x⟩ = 0

⟨v3 + t, x⟩ = 0

C(t)

(b) The (parametric) central
arrangement C⟲(P + t) for t ∈ R.

Figure 7: The hyperplane arrangements from Example 3.2.

We have used hyperplane arrangements to identify the diﬀerent slicing chambers. We now
want to count them, using classical properties of arrangements of hyperplanes in d-dimensional
Euclidean space. For the theory of enumeration of faces and cells in a hyperplane arrangement
we refer the reader to [Sta07; Zas75]. As we will see in Section 4, this allows us to answer
any purely combinatorial question regarding the slices of a polytope, in polynomial time.

Proposition 3.3. Let P ⊂ Rd be a polytope with n vertices. In the cocircuit arrangement
R⟲(P ) there are at most (n
d) aﬃne hyperplanes. There are at most O(nd2) d-dimensional
polyhedral regions and the total number of chambers (including lower-dimensional cells) in the
associated cocircuit arrangement is bounded by O(nd22d). Thus, the number of slicing cham-
bers (counting also cells of lower dimension for both regions and chambers) is O(nd2+d22d).

Proof. We denote by fk the number of polyhedral faces of dimension k. By the classic
Zaslavsky’s theorem (see [Zas75] or [Sta07, Proposition 2.4]), the number of top-dimensional
polyhedral regions fd(R⟲(P )) of the arrangement is

fd(R⟲(P )) ≤
 d∑

i=1
 ((n
d)

i
 ) ∼ O(nd2).

Note that one can write precise formulas, when the associated matroid is known (see [Sta07]),
but the generic case provides an upper bound. Moreover, it is well-known that one can bound
the number of k-faces in the arrangement by the inequality (see [FSTT91]):

fk(R⟲(P )) ≤ (d
k
)fd(R⟲(P )), 0 ≤ k ≤ d,

which implies that the desired bound on all polyhedral regions (top dimensional or not) is
O(nd22d). For each such region we have a corresponding hyperplane arrangement C⟲(P + t)
to consider, which has n hyperplanes and thus at most ∑d
i=1 (n
i ) full-dimensional slicing
chambers. Therefore, for each choice of region, we get a number of slicing chambers of order
O(nd) or, counting also its lower-dimensional faces, of order O(nd2d). This number multiplied
by the upper bound for the number of cells of R⟲(P ), gives a bound of order O(nd2+d22d).

These pairs consisting of cocircuit arrangement and the corresponding central arrangement
of vertices (after a choice of center) detect all the changes in the combinatorial structure of

16

the hyperplane sections of P . In ﬁxed dimension d, the number of regions and of faces of
these regions is polynomial in the number of vertices of P , and on each of these cells the
hyperplane section P ∩ H has a given combinatorial type.
We can extend Theorem 2.5 to take into account translations when integrating a poly-
nomial over hyperplane sections of P . This is an extension of [BM23, Theorem 3.5], which
contains an analogous statement for the volume.

Theorem 3.4. Let P ⊂ Rd be a full-dimensional polytope and let f (x) = ∑
α cαxα be a
polynomial. Let R ⊂ Rd be a region of the cocircuit arrangement R⟲(P ) and let C(t) ⊂ Rd

be a chamber of the central arrangement C⟲(P + t), for t ∈ R. Restricted to t ∈ R and
u ∈ C(t) ∩ Sd−1, the integral ∫

(P +t)∩u⊥ f (x) dx is a rational function in variables t1, . . . , td,
u1, . . . , ud.

Proof. By Lemma 3.1, the chambers C(t) of C⟲(P + t) are linearly dependent on t, when
t ∈ R. Let u ∈ C(t). As in the proof of Theorem 2.5, we triangulate (P + t) ∩ u⊥, obtaining

M∆(t, u) =
 







vj2(t, u) − vj1(t, u)
vj3(t, u) − vj1(t, u)
...
vjd(t, u) − vj1(t, u)
u
 






 ,

vj(t, u) = ⟨bj + t, u⟩(aj + t) − ⟨aj + t, u⟩(bj + t)
⟨bj − aj, u⟩

= ⟨bj + t, u⟩aj − ⟨aj + t, u⟩bj
⟨bj − aj, u⟩ + t,

where vj(t, u) denotes a vertex of a simplex ∆ in the triangulation T , which lies on the
interior of the edge conv(aj + t, bj + t) of P + t. Repeating the computation of (1) in the
proof of Theorem 2.5 yields
∫

(P +t)∩u⊥ f (x) dx = ∑

∆∈T |det M∆(t, u)| ∑

α
 cα
(|α| + d − 1)!
 ∑

p∈Z
d
≥0
p≤α
 (−1)|α|−|p|(α1
p1
 ) · · · (
αd
pd
 )
·

· ∑

k∈Z
d
≥0,
|k|=|α|
⟨ p, vj1 (t, u) ⟩k1 · · · ⟨ p, vjd (t, u) ⟩
kd ,

which is a rational function in t1, . . . , td, u1, . . . , ud.

This result implies that ∫

(P +t)∩u⊥ f (x) dx is a piecewise rational function. The domains
over which it is rational are pairs of polyhedra in the following sense. Each region R is
a polyhedron in Rd, and each chamber C(t) is a polyhedron in Rd parametrized by t. In
particular, the domain of rationality is a semialgebraic subset of R2d with the following shape:

{(t, u) ∈ R2d | t ∈ R, u ∈ C(t)} ∩ (Rd × Sd−1) ,

for some region R ⊂ R⟲(P ) and chamber C(t) ⊂ C⟲(P + t), where t ∈ R. Notice that the
condition u ∈ C(t) is quadratic in the variables t1, . . . , td, u1, . . . , ud, see Example 3.2. We
can bound the degree of the polynomials appearing in the integration formula, independently
of the chamber and region they come from, as follows.

17

Proposition 3.5. In each of slicing chambers the rational function ∫
(P +t)∩u⊥ f (x) dx respects
the following degree bounds:

deg numerator
 (∫

(P +t)∩u⊥ f (x) dx
)
 ≤ (f1(P ) − (d − 1)
)(D + d − 1) + d(D + 1),

deg denominator
 (∫

(P +t)∩u⊥ f (x) dx
)
 ≤ (f1(P ) − (d − 1)
)(D + d − 1).

Here fk(P ) denotes the number of k-dimensional faces of P and D = deg f .

Proof. We want to study the degree of numerator and denominator of the piecewise rational
function ∫

(P +t)∩u⊥ f (x) dx. We ﬁx a region R ⊂ R⟲(P ) and a chamber C(t) ⊂ C⟲(P + t),
for t ∈ R. By the proof above, the integral of f over the hyperplane section (P + t) ∩ u⊥ is
the sum over all simplices ∆ ∈ T of |det M∆(t, u)| multiplied by

∑

α
 cα
(|α| + d − 1)!
 ∑

p∈Z
d
≥0
p≤α
 (−1)
|α|−|p|(
α1
p1
 ) · · · (αd
pd
 ) ∑

k∈Z
d
≥0,
|k|=|α|
⟨ p, vj1(t, u) ⟩k1 · · · ⟨ p, vjd (t, u) ⟩kd , (2)

where vj1(t, u), . . . , vjd(t, u) are the vertices of the simplex ∆. Since the denominator of
vji(t, u) is the same in every coordinate of the vector, we can pull it out of the scalar product
with p; moreover, denoting D = deg f , we have that ki ≤ D for all i = 1, . . . , d. Therefore,
(2) becomes ϕ∆(t, u)
∏i⟨u, bji − aji⟩D

where vji belongs to the edge of P with extrema aji, bji, and ϕ∆ is a polynomial.
It is not hard to see that if we sum a bunch of rational functions such that the degree of
their numerator minus the degree of their denominator is constant for all summands, then
also the diﬀerence of the degrees of numerator and denominator of the sum of these functions
is going to be that same number. Using this elementary fact, and noticing that for every
summand in (2) the degree of the numerator is twice the degree of the denominator, we can
deduce that deg ϕ∆(t, u) = 2 deg (∏i⟨u, bji − aji⟩D) = 2 · d · D.
Let us now describe the rational function |det M∆(t, u)|. All but the last row of the matrix
have entries that are quotients of a cubic and a quadratic polynomial, in t1, . . . , td, u1, . . . , ud.
The denominator of each entry of the (i − 1)th row is ⟨u, bji − aji⟩⟨u, bj1 − aj1⟩ for all
i = 2, . . . , d. The determinant is thus the quotient of a polynomial of degree 3(d − 1) + 1 and
another polynomial of degree 2(d − 1). Then,

|det M∆(t, u)| ϕ∆(t, u)
∏i⟨u, bji − aji⟩D = φ∆(t, u)
⟨u, bj1 − aj1⟩D+d−1 ∏i̸=1⟨u, bji − aji⟩D+1 ,

for some other polynomial φ∆ of degree 2dD + 3(d − 1) + 1. Notice that the diﬀerence between
the degrees of numerator and denominator is d(D + 1), independently of the simplex ∆.
We are now ready to sum over the simplices in the triangulation. Since the summands
have similar denominators, with some possible redundancy, we obtain the following expression
for ∫

(P +t)∩u⊥ f (x) dx:

∑

∆∈T
 φ∆(t, u)
⟨u, bj1 − aj1⟩D+d−1 ∏i̸=1⟨u, bj − aj⟩D+1 = ψ(t, u)
∏j⟨u, bj − aj⟩D+d−1 , (3)

18

where the product now runs over all vertices of (P + t) ∩ u⊥. Since for all the summands in
the left-hand side of (3) we know that the diﬀerence between the degrees of numerator and
denominator is d, we deduce that deg ψ(t, u) = (f0((P + t) ∩ u⊥))(D + d − 1) + d(D + 1).
Therefore, using [BBMS22, Theorem 5.6] to bound f0((P + t) ∩ u⊥), we obtain the degree
bounds claimed in the statement, valid in every chamber of every region.

Example 3.6. We continue Example 3.2. Let R be the pentagonal shaded region of the
cocircuit arrangement R⟲(P ) in Figure 7a and let

C(t) = {x ∈ R2 | ⟨v1 + t, x⟩ > 0, ⟨v4 + t, x⟩ > 0}.

The integral over the constant function 1 for t ∈ R and u ∈ C(t) is

vol((P + t) ∩ u
⊥) = ∫

(P +t)∩u⊥ 1 dx = − t1u1 + t2u2 + 3u1 − u2
u1(u1 − u2) .

Note that for t = (0, 0) this specializes to the polynomial in the corresponding chamber in
Figure 3 from Example 2.7, as explained in Remark 2.6. The bounds from Proposition 3.5 in
this case are 6 for the degree of the numerator and 4 for the degree of the denominator, both
of which are not tight. ⋄

3.2 Rotating the translation

In this section we extend the theory developed in Subsection 2.2, where we ﬁxed a polytope
P and a unit direction u ∈ Sd−1, and studied the sections of P by parallel aﬃne hyperplanes
H(β) with normal vector u. Recall from Remark 2.10 that u induces an ordering on the
vertices of P . We obtained a parallel hyperplane arrangement Cu
↑ (P ) where, for each chamber,
the hyperplanes H(β) intersect P in a ﬁxed set of edges, and separate two vertices which are
consecutive in the induced ordering. Now, we allow ourselves to ﬁrst vary the direction
u ∈ Sd−1, and then construct Cu
↑ (P ), depending on u.

Lemma 3.7. Let P ⊂ Rd be a full-dimensional polytope and let R be a region of the central
hyperplane arrangement

R↑(P ) = {(vi − vj)
⊥ | vi, vj are distinct vertices of P }.

Then the following holds: For all u ∈ R the linear functional ⟨u, ·⟩ induces the same ordering
v1, . . . , vn of the vertices of P .

The central hyperplane arrangement R↑(P ) is called sweep arrangement or lineup ar-
rangement [PP21]. The above lemma implies the following: Let u, u′ ∈ R, i ∈ [n − 1] and let
C(u) ⊂ Cu
↑ (P ), C(u′) ⊂ Cu′

↑ (P ) such that all hyperplanes in C(u) and C(u′) separate vi from
vi+1. Then, any two hyperplanes H(u, β) ∈ C(u), H(u′, β′) ∈ C(u′) intersect P in the same
set of edges. However, the polytopes P ∩ H(u, β) and H(u′, β′) are not normally equivalent.

Example 3.8. We continue Examples 2.11 and 2.13. The sweep arrangement of P is shown
in Figure 8. It consists of 6 distinct hyperplanes, subdividing R2 into 12 regions. Each of these
regions corresponds to a possible ordering of the vertices of P induced by a linear functional.
The shaded region

R = {x ∈ R2 | ⟨v1 − v2, x⟩ < 0, ⟨v5 − v3, x⟩ < 0, ⟨v2 − v5, x⟩ < 0, ⟨v3 − v4, x⟩ < 0}

corresponds to the ordering v1, v2, v5, v3, v4 from Example 2.11. ⋄

19

(v1 − v5)⊥ = (v2 − v3)⊥

(v1 − v4)⊥

(v1 − v2)⊥ = (v3 − v5)⊥

(v1 − v3)⊥ = (v4 − v5)⊥

(v2 − v5)⊥ = (v3 − v4)⊥

(v2 − v4)⊥

Figure 8: The sweep arrangement of P from Example 3.8. The region R is shaded
in gray.

Each region R ⊂ R↑(P ) corresponds to the same ordering of the vertices of P , i.e., the
parallel arrangement Cu
↑ (P ) has the same combinatorial structure for all u ∈ R∩Sd−1. Also in
this case we have a ﬁnite number of regions, each of which deﬁnes a ﬁnite number of chambers.
The following is the analogue of Proposition 3.3 for the count of total parallel slicing chambers,
including also lower-dimensional cells of the arrangements. This will provide also the proof
of Theorem 1.2.

Proposition 3.9. Assuming that P ⊂ Rd has n vertices, the sweep arrangement Cu
↑ (P ) has
at most (n
2) aﬃne hyperplanes. There are at most O(n2d) d-dimensional polyhedral regions
in R↑(P ) and the total number of regions (including lower-dimensional cells) in the sweep
arrangement is bounded by O(n2d2d). For each region in R↑(P ) we have an arrangement of
parallel hyperplanes Cu
↑ (P ), thus the ﬁnal number of slicing chambers (even of lower dimen-
sion) is O(n2d+12d).

Proof. Each hyperplane of the sweep arrangement of a polytope P is identiﬁed by a pair of
vertices: their diﬀerence is the normal of the hyperplane. As in Proposition 3.3, by Zaslavsky’s
theorem (see [Zas75] or [Sta07, Proposition 2.4]) one can prove that the number of top-
dimensional polyhedral regions fd(R↑(P )) of the sweep arrangement is

fd(R↑(P )) ≤
 d∑

i=1
 ((n
2)

i
 ) ∼ O(n2d).

Again, we can bound the number of k-faces in the arrangement by the inequality (see
[FSTT91]):
 fk(R↑(P )) ≤ (d
k
)fd(R↑(P )), 0 ≤ k ≤ d,

which implies the desired bound on all polyhedral regions in the sweep arrangement (of all
dimensions) of O(n2d2d).
For each such region of the sweep arrangement we have a corresponding parallel hyperplane
arrangement Cu
↑ . For each choice of translation direction u, the number of chambers is of the
order of O(n). Indeed, the chambers of this arrangement are much easier, as they are deﬁned,
in the worst case, by n parallel hyperplanes, one for each vertex of P ; each chamber is bounded
by exactly two parallel hyperplanes. Thus, the total number of d-dimensional chambers is

20

O(n2dn) and the ﬁnal total count of slicing chambers is bounded by O(n2d+12d) when we
consider all the lower-dimensional regions and the corresponding chambers.

Proof of Theorem 1.2. Given a polytope P , both Proposition 3.3 and Proposition 3.9 provide
an upper bound for the number of combinatorial types of hyperplane sections of P . Among
the two bounds, the smallest is O(n2d+12d), and the claim follows.

Recall our notation H(u, β) = {x ∈ Rd | ⟨u, x⟩ = β}. Once more, we can extend
Theorem 2.12 by ﬁrst choosing the direction u, and then considering all parallel sections with
normal vector u. This is a second way to parametrize all aﬃne hyperplane sections, and the
following result is the analogue of Theorem 3.4.

Theorem 3.10. Let P ⊂ Rd be a full-dimensional polytope and let f (x) = ∑
α cαxα be a
polynomial. Let R ⊂ Rd be a region of the sweep arrangement R↑(P ) and let C(u) ⊂ R be
a chamber of the parallel arrangement Cu
↑ (P ), for u ∈ R. Restricted to u ∈ R ∩ Sd−1 and
β ∈ C(u), the integral ∫
P ∩H(u,β) f (x) dx is a rational function in variables u1, . . . , ud, β.

Proof. By Lemma 3.7 the chambers C(u) of Cu
↑ (P ) are linearly dependent on u when re-
stricting to u ∈ R ∩ Sd−1. Let β ∈ C(u). As in the proof of Theorem 3.4, we triangulate
P ∩ H(u, β), obtaining the matrix

M∆(u, β) =
 







vj2(u, β) − vj1(u, β)
vj2(u, β) − vj1(u, β)
...
vjd(u, β) − vj1(u, β)
u
 






 ,

vj(u, β) = β
⟨u, bi − ai⟩ (bi − ai) + ⟨u, bi⟩ai − ⟨u, ai⟩bi
⟨u, bi − ai⟩ ,

where vj(u, β) denotes the vertex of a simplex ∆ in the triangulation T , which lies on the
interior of the edge conv(aj + t, bj + t) of P . Repeating the computation of (1) in the proof
of Theorem 2.5 yields
∫

P ∩H(u,β) f (x) dx = ∑

∆∈T |det M∆(u, β)| ∑

α
 cα
(|α| + d − 1)!
 ∑

p∈Z
d
≥0
p≤α
 (−1)|α|−|p|(α1
p1
 ) · · · (
αd
pd
 )·

· ∑

k∈Zd
≥0,
|k|=|α|
⟨ p, vj1(u, β) ⟩
k1 · · · ⟨ p, vjd (u, β) ⟩kd ,

which is a rational function in u1, . . . , ud, β.

This result implies that ∫

P ∩H(u,β) f (x) dx is a piecewise rational function. The domains
over which it is rational are now polyhedra, in contrast to Subsection 3.1, up to restriction to
a sphere, and they live in Rd+1:

{(u, β) ∈ Rd+1 | u ∈ R, β ∈ C(u)} ∩ (Sd−1 × R) ,

for some region R ⊂ R↑(P ) and chamber C(u) ⊂ Cu
↑ (P ), where u ∈ R ∩ Sd−1. In this
translational setting, the chamber C(u) has shape ⟨vi, u⟩ ≤ β ≤ ⟨vi+1, u⟩, and therefore it

21

deﬁnes a polyhedron in Rd+1. There is one such polyhedron, and hence one such rational
function, for each chamber of every region. The following is the analogue of Proposition 3.5
in the translational setting.

Proposition 3.11. In each of the slicing chambers the rational function ∫

P ∩H(u,β) f (x) dx
respects the following degree bounds:

deg numerator
 (∫

P ∩H(u,β) f (x) dx
)
 ≤ (f1(P ) − (d − 1)
)(D + d − 1) + 1,

deg denominator
 (∫

P ∩H(u,β) f (x) dx
)
 ≤ (f1(P ) − (d − 1)
)(D + d − 1).
 (4)

Here fi(P ) denotes the number of i-dimensional faces of P and D = deg f .

Proof. We can repeat exactly the same computations in the proof of Proposition 3.5. The
only diﬀerence is that in this framework lies in the rational function |det M∆(u, β)|. All but
the last row of the matrix have entries that are quotients of two quadratic polynomials. The
denominator of each entry of the ith row is ⟨u, bji − aji⟩⟨u, bj1 − aj1⟩ for all i = 2, . . . , d. The
determinant is thus the quotient of a polynomial of degree 2(d−1)+1 and another polynomial
of degree 2(d − 1). Therefore, in the end, the degrees of numerator and denominator of∫
P ∩H(u,β) f (x) dx diﬀer only by 1.

Example 3.12. We continue Examples 3.8, 2.11 and 2.13. Let R denote the region of the
sweep arrangement of P deﬁned in Example 3.8, which is depicted in Figure 8 as shaded
cone. Figure 9 shows the volume of P ∩ H(u, β), i.e., the integral of the constant function
1, parametrically for directions u ∈ R ∩ Sd−1 and β ∈ Cu
↑ (P ). Note that, in accordance with
Remark 2.6, the rational functions that are displayed specialize to the ones in Figure 5 when
evaluated at u = 1√5 (1, 2). ⋄

β+u1+u2
u1u2
 2
u2

− β−u1−3u2
(u1+u2)u2
 2(β−2u2)
(u1+u2)(u1−u2)

u

Figure 9: The function ∫

P ∩H(u,β) 1 dx = vol(P ∩ H(u, β)) for u ∈ R ∩ Sd−1, as
deﬁned in Example 3.12.

To conclude, we note that this section presented two diﬀerent cell decompositions, inspired
by the rotational and the translational approach respectively. Each of these decompositions
is given by the choice of a pair of hyperplane arrangements, namely the cocircuit arrangement
and the central arrangement, or the sweep arrangement and the parallel arrangement. The
structure was summarized in Table 1, presented in the introduction.

22

4 Computational complexity of ﬁnding optimal slices

The aim of this section is to use the results of Theorem 1.1, explained in more details in
Section 3, in order to obtain Theorem 1.3. We make use of the structure of the pairs of
hyperplane arrangements from the previous sections for optimization purposes. The proofs of
Theorems 3.4 and 3.10 imply the existence of algorithms to ﬁnd a slice of a polytope where
the integral of a polynomial attains the largest value. In particular, we can ﬁnd the slice
with the largest volume. In the same spirit, we can also ﬁnd the slice of P with maximal (or
minimal) combinatorial properties.
Related optimization problems involving halfspaces and projection can also be solved with
minor adjustments of our algorithm. Furthermore, we can combine the optimization criteria
in Theorem 1.3 to ﬁnd, e.g., a slice of maximal volume of a ﬁxed combinatorial type. All of
these achievements are related to both problems in combinatorial optimization and convex
geometry. We will prove that some of them are in general hard from the point of view of
complexity theory, but our algorithms have polynomial complexity in ﬁxed dimension. In the
following sections, we always assume that the input of our algorithms are rational. Therefore,
from now on, a polytope P is going to be rational, unless otherwise stated, and a polynomial
f is going to have rational coeﬃcients.

4.1 Polynomial-time complexity in ﬁxed dimension

Probably the most important feature of our hyperplane arrangements and the associated
chamber decomposition is that within each chamber, an aﬃne hyperplane intersects the poly-
tope P in a ﬁxed set of edges. Thus, they capture all the combinatorial types of hyperplane
sections of a polytope. This allows us to tackle optimization questions regarding combinatorial
aspects of the slices of a polytope, proving the ﬁrst part of Theorem 1.3 (ii).

Proposition 4.1. We have an algorithm that receives as input a polytope P ⊂ Rd, and
outputs the maximizer and the maximum of fk(P ∩ H) over all hyperplanes H, where fk(K)
is the number of k-dimensional faces of K. The algorithm runs in polynomial time for d ﬁxed.

Proof. The proof is elementary and it is follows directly from our construction of the hyper-
plane arrangements. We will prove it using the sweep arrangement and parallel slices, but
an analogous proof can be obtained in the rotational setting. Fix a region R ⊂ R↑(P ) and a
chamber C(u) ⊂ Cu
↑ (P ) for some u ∈ R ∩ Sd−1. Then, for every u in the relative interior of
R ∩ Sd−1 and for every β in the interior of C(u), the hyperplane section P ∩ H(u, β) has the
same combinatorial type. By Proposition 3.9, we have polynomially many cases to check for
ﬁxed dimension d.

A straightforward generalization of the proof of Proposition 4.1 provides a proof of the
weighted version of the optimization problem stated in Theorem 1.3 (iii). Indeed, it is enough
to do the weighted count in each chamber of each region, and compare them. The second
part of Theorem 1.3 (ii) also follows from Proposition 4.1, since the hyperplanes in a given
slicing chamber separate the same sets of k-dimensional faces of P .
Based on our hyperplane arrangement and our previous results, we can also solve some
metric optimization problems. For each chamber of each region, the function describing the
integral of a polynomial (or, in particular, the volume) over a section of P is piecewise rational
by Theorems 3.4 and 3.10. More precisely, let R be a region of R(P ) for either ⟲ or ↑ . Let C

23

be a slicing chamber of C for points in the given region R. Then, there exist two polynomials
pC, qC such that ∫
P ∩H f (x) dx = pC
qC for a given polynomial f and hyperplanes H from the
slicing chamber. We can ask for the hyperplane section which maximizes ∫

P ∩H f (x) dx by
maximizing the single rational functions in their respective chambers, and then taking the
maximum over this ﬁnite list of values. From the point of view of complexity, the two types
of hyperplane arrangements behave in similar but diﬀerent ways:

max pC(t, u)
qC(t, u)
s.t. t ∈ R ⊂ R⟲(P ),

u ∈ C(t) ⊂ C⟲(P + t),

u ∈ Sd−1,
 (5)
 max pC(u, β)
qC(u)
s.t. u ∈ R ⊂ R↑(P ),

u ∈ Sd−1,

β ∈ C(u) ⊂ Cu

↑ (P ).
 (6)

Out of any of these optimization problems, we get (at least) one solution for every chamber
of every region. Comparing all the results leads to a maximum over all hyperplane sections.

Example 4.2. Continuing the showcase of the pentagon, we give an example for the max-
imization of the integral of the constant polynomial f = 1, both for the radial and the
translational case within a ﬁxed region. In other words, we seek to ﬁnd the slice of maximum
volume in this example. We begin with the radial case. The pentagonal region R⟲ ⊂ R⟲(P )
from Example 3.2 is

R⟲ = {t ∈ R
2 | − 3t1 + t2 ≥ −2, −t1 − t2 ≥ 0, 3t1 + t2 ≥ −2t1 − t2 ≥ 0, t2 ≥ −1},

and is shown in Figure 7a (recall from Remark 2.6 that we are allowed to take closures of
regions and chambers). We have seen in Example 3.6 that, when restricting to t ∈ R⟲, one
of the slicing chambers in the central arrangement is

C⟲(t) = {x ∈ R2 | (t1 − 1)x1 + (t2 − 1)x2 ≥ 0, t1x1 + (t2 + 2)x2 ≥ 0},

and that, restricted to this region and chamber, the volume of P ∩ H(t, u) is given by

p(t, u)
q(t, u) = −(t1u1 + t2u2 + 3u1 − u2)
(u1 − u2)u1 ,

where u ∈ C⟲(t) ∩ Sd−1. Maximizing this function subject to t ∈ R, u ∈ C⟲(t) ∩ Sd−1 yields√10, and a maximizer is given by t = ( 5
12 , − 3
4 ) ∈ R and u = 1√10 (−3, 1) ∈ C⟲(t) ∩ Sd−1. In-

deed, for this choice of parameters, (P +t)∩u⊥ yields the line segment conv((− 7
12 , − 7
4 ), ( 5
12 , 5
4 ))
and the Euclidean volume of this line segment inside its aﬃne span is √10.
For the translational case, we have seen in Example 3.8 that one of the regions in the
sweep arrangement R↑(P ) is

R↑ = {x ∈ R2 | x1 ≥ 0, x1 − x2 ≤ 0}.

By Example 3.12, when restricting to the chamber C↑(u) = {β ∈ R | ⟨u, v5⟩ ≤ β ≤ ⟨u, v3⟩},
for u ∈ R↑ ∩ Sd−1, the volume is given by

pC(u, β)
qC(u) = −(β − u1 − 3u2)
(u1 + u2)u2 .

24

The maximum of this function subject to u ∈ R↑ ∩ Sd−1, β ∈ C↑(u) is 2√2 and obtained at
u = 1√2 (1, 1) ∈ R↑ ∩ Sd−1 and β = ⟨u, v5⟩ = 0, which is smaller than the maximum we have

found in the rotational case. Indeed, one can check that the maximum value √10 is (among
other regions) attained in the region

R′

↑ = {x ∈ R2 | x1 − 3x2 ≤ 0, x1 − x2 ≥ 0},

which contains the unit vector u = 1√10 (3, −1) ∈ R′
↑. ⋄

How do the two optimization problems (5) and (6) compare? Both problems must be
solved for a ﬁnite (in fact polynomial) number of regions, each with a ﬁnite number of cham-
bers. For the rotational version, namely (5), Proposition 3.3 gives an upper bound on the
total number of slicing chambers, whereas Proposition 3.9 bounds the total number for the
translational version (6). Both of these bounds are polynomial in the number of vertices of
P for ﬁxed dimension d. However, these two problems are very diﬀerent from a complexity
point of view. The complexity analysis for the maximization problem is based on [BPR06,
Algorithm 14.9], which we summarize in the following lemma.

Lemma 4.3 ([BPR06, Algorithm 14.9]). Let D be an ordered domain contained in a real
closed ﬁeld (such as D = Z or D = Q). Let P ⊂ D[x1, . . . , xk] be a ﬁnite set and let S be
a semialgebraic set deﬁned by polynomial inequalities involving only the polynomials in P.
Consider F ∈ D[x1, . . . , xk]. Denote by s the number of elements of P, by δ an upper bound
on the degree of the elements of P and F . Then, the complexity of computing an inﬁmum of
F over S, and a minimizer in case such point exists, is s2k+1δO(k).

We now apply Lemma 4.3 to our concrete situation of an optimization problem coming
from our slicing chambers. Recall that we assume the polytope P and the polynomial f to
be deﬁned over Q.

Proposition 4.4. Let P be a polytope in ﬁxed dimension d. For each region R and each
chamber C in both the rotational or the translational setting, there is a polynomial time algo-
rithm that computes the maximum and the maximizer of the rational function ∫

P ∩H f (x) dx.

Proof. We prove the result in the translational setting. A similar estimate can be obtained
in the rotational setting, as explained below in Remark 4.5. Fix a region R ⊂ R↑(P ) and a
slicing chamber C ⊂ Cu
↑ (P ) for u ∈ R. Then R and C are respectively of the form

Au ≥ 0, ℓ1(u) ≤ β ≤ ℓ2(u),

where A is a matrix and ℓi(u) = ⟨vi, u⟩ for some vertices v1, v2 of P . Restricted to hyperplanes
H(u, β), u ∈ R, β ∈ C, the integral is a rational function ∫
P ∩H(u,β) f (x) dx = pC (u,β)
qC (u) . We
introduce an auxiliary variable z ∈ R and deﬁne the following set:

SC = {(u, β, z) ∈ Rd+2 | qC(u) z − pC(u, β) = 0, Au ≥ 0,
 d∑

i=1 u
2
i = 1, ℓ1(u) ≤ β ≤ ℓ2(u)}.

Finding the maximum of (5) is equivalent to ﬁnding the maximum of z subject to (u, β, z) ∈
SC. We can ﬁnd such an optimal value by using [BPR06, Algorithm 14.9]. Let δ be the
degree of qC(u, β) z − pC(u, β), which by (4) is bounded by (f1(P ) − (d − 1)
)(D + d − 1) + 1,

25

where f1(P ) denotes the number of edges of P . Bounded the number of rows of A by the
number of hyperplanes in R↑(P ) yields that the number of polynomials deﬁning SC is at most
s = 1 + (n
2) + 1 + 2. Thus, according to Lemma 4.3, the complexity of ﬁnding the optimal
value of our problem is at most

s
2d+5δO(d) = ((n
2
) + 4)2d+5 ((f1(P ) − (d − 1)
)(D + d − 1) + 1)O(d),

where n = f0(P ) is the number of vertices P . For ﬁxed d, the running time is polynomial.

Remark 4.5. Notice that we can solve the optimization problem (6) in complete analogy by
applying [BPR06, Algorithm 14.9]. The comparison of the complexity of the two problems
reduces to the comparison of the total number of chambers and the number of hyperplanes
needed to deﬁne each chamber. Since these two numbers depend in any case polynomially only
on the number of vertices of P (when the dimension d is ﬁxed), the complexity of our algorithm
is polynomial in both variants. As noted in Subsections 3.1 and 3.2, the domains over which
the objective function is rational are polytopes in the translational case and semialgebraic
sets deﬁned by quadrics in the rotational case. Overall, the translational setting is cheaper.

By Propositions 3.3 and 3.9 we have to apply Lemma 4.3 only polynomially many times.
Putting all of this together, we can prove our main result on optimizing integrals and volumes
over the slices of a polytope. This was stated earlier as Theorem 1.3 (i). We summarize the
algorithm analysis in the rotational and translational settings in Table 2.

Theorem 4.6. We have an algorithm that receives as input a rational convex polytope P ⊂ Rd

and a polynomial f of degree D with rational coeﬃcients, and outputs the maximizer and
the maximum of ∫

P ∩H f (x) dx over all aﬃne hyperplane sections. The algorithm runs in
polynomial time for ﬁxed d.

Proof. In Subsections 3.1 and 3.2 we have presented two diﬀerent decompositions of the
space of all possible aﬃne hyperplane sections of P . To compute the section which maximizes∫
P ∩H f (x) dx we need to solve problem (5) or (6) for each region and chamber respectively,
yielding a total number of (#regions)(#chambers) many optimization problems. To set up
each of the optimization problems we detect the edges of P which are intersected by the
hyperplanes, yielding the necessary combinatorial information of the slice P ∩ H. This allows
us to compute a triangulation of P ∩ H and to write the objective function as in the proofs
of Theorems 3.4 and 3.10. By construction, the triangulation will have number of simplices
bounded polynomially in terms of the number of vertices of P ∩ H. More precisely, for a
k-dimensional polytope with m vertices, the largest number of top-dimensional simplices in
the triangulation is bounded by O(m⌈(k+1)/2⌉) [DLRS10, Proposition 2.6.5].
In our situation, k + 1 = d, which is a constant, and m, the number of vertices of the
slice P ∩ H, is polynomially bounded by the number of edges and vertices of P . This is a
polynomial in the number of variables, as well as the number of facet inequalities of P , and
can be computed in polynomial time in ﬁxed dimension. Thus, the mathematical programs
can be encoded in time polynomial in the input size of P . Finally, Proposition 4.4 and
Remark 4.5 imply that both Problem (5) and Problem (6) are solvable in polynomial time.
We repeat this for each slicing chamber, which means we do this polynomially many times
by Propositions 3.3 and 3.9. Putting all together the total complexity of computation is
polynomial in the input.
 26

regions upper bound
num. of regions chambers upper bound
num. of chambers
per region
 cost of
optimizing in
one chamber

⟲ R⟲ ∑d
i=1 ((n
d)
i ) C⟲ ∑d
i=1 (n
i ) s2d+5δO(d)

as in Rmk. 4.5

↑ R↑ ∑d
i=1 ((n
2)
i ) Cu
↑ n − 1 s2d+5δO(d)

as in Prop. 4.4

Table 2: Details of complexity analysis in the two methods of classifying slices.
In each case s, δ are, respectively, the number of equations and upper bound on
degree of the equations. They diﬀer for the two decomposition methods.

It is important to note that, with little eﬀort, the methods we used to prove Theorem 1.3
(i) can be extended to prove the additional computational results in items (iv) and (v) on
projections and halfspace intersections. The latter is related to the densest hemisphere prob-
lem: Given a set K of n points on the unit sphere Sd in d-dimensional Euclidean space, a
hemisphere of Sd is densest if it contains a largest subset of K. This problem is already
known to be solvable in polynomial time when the dimension d is ﬁxed [JP78].
The proofs of the complexity of our algorithm in the case of projections and halfspace
sections are in complete analogy to the previous discussion. Thus, we only sketch the key
missing details in the following proof.

Proof of Theorem 1.3 (iv ), (v ). For (iv), it suﬃces to note that the same slicing chambers of
the central arrangement C⟲(P ) that we used earlier, keep the vertices on the corresponding
halfspace H +
0 intact, and the combinatorial type of P ∩ H +
0 does not change. Similarly,
the triangulation we use for the section P ∩ H0 can be easily extended to a triangulation
of P ∩ H +
0 . Therefore, Theorem 2.5 can be generalized to prove that in each chamber the
integral of the halfspace intersection is a rational function. Then, an analogous version of
Theorem 4.6 implies the polynomiality of the maximization or minimization.
Theorem 1.3 (v) is based on the results proved in Subsection 2.3. We can compute both the
polar P ◦ of our polytope and the associated hyperplane arrangement C⟲(P ◦) in polynomial
time in ﬁxed dimension, and C⟲(P ◦) has polynomially many maximal open chambers. Since
projections do not distinguish between central and aﬃne hyperplanes, we do not need to use
regions in this framework. In each chamber the function ∫

πu(P ) f (x) dx is a polynomial in
u ∈ C ∩Sd−1, and its degree is bounded by 2d(D +1)−1. Therefore, we can use Lemma 4.3 to
compute the maximum or the minimum of this polynomial over all projections, in polynomial
time when the dimension d is ﬁxed.

4.2 Hardness in non-ﬁxed dimension

In Subsection 4.1 we showed that several optimization problems are solvable in polynomial
time for ﬁxed dimension. The purpose of this section is to show that this does not hold
true when the dimension is not ﬁxed. We begin by proving the hardness of ﬁnding slices of
maximum volume. For this, we use the following lemma, whose proof was kindly provided to
us by Francisco Criado Gallart.
 27

Lemma 4.7. Let K ⊂ {x ∈ Rd | xd = 0} be a (d − 1)-dimensional convex body. There exists
a pyramid C ⊂ Rd over K such that

max
H aﬀ. hyperplane vol(C ∩ H) = vol(K)

where K = C ∩ {x ∈ Rd | xd = 0} and the maximum is uniquely attained at this hyperplane.

Proof. Consider a point p = (p1, . . . , pd−1) in the interior of K, let h > 0 and deﬁne the
pyramid over K as C = conv (K, ( p
h ) ) ⊂ Rd.

Our claim is that there exists h > 0 such that the largest hyperplane section of C is the base
K. The proof will be divided into two steps. The ﬁrst one concerns proving that there exists
h > 0 such that the width of C is achieved uniquely in direction of (0, . . . , 0, 1). Recall that
the width of C is deﬁned as [GK94a]

ω(C) = min
u∈Sd−1
 (max
x∈C ⟨u, x⟩ − min
x∈C⟨u, x⟩
) .

Since p lies in the interior of K, there exists r > 0 such that the (d − 1)-dimensional ball
Bp,r centered at p of radius r is strictly contained in K. Therefore, taking h = r
2 , the cone
̃C = conv (Bp,r, ( p
h ) ) is contained in C. Using some elementary geometry, it can be proved
that ω( ̃C) = r
2 and it is achieved uniquely in direction (0, . . . , 0, 1). Since ̃C ⊂ C, the width
of C is at least r
2 . By construction, the width of C is strictly larger than the width of ̃C in
all directions except (0, . . . , 0, 1), where they coincide. Hence, ω(C) = h.
The second step of the proof is to show that, with this choice of h so that the width of C is
realized by the last coordinate vector, the base of C is the hyperplane section with the largest
volume. Notice that the volume of a section which does not intersect the base K is always
smaller that the volume of K itself, by construction. Therefore, assume that the section with
largest volume is not the base but it is deﬁned by a hyperplane H such that H ∩ K ̸= ∅ and
let u be a normal vector to H. Let p1, p2 ∈ C be respectively the maximizer and minimizer
of ⟨u, x⟩ over C. Then ⟨u, p1⟩ − ⟨u, p2⟩ > ω(C) = h and the bipyramid conv ((H ∩ C), p1, p2)

is contained in C. Then, we have the following chain of (in)equalities:

1
d vol K · h = vol C > vol (conv ((H ∩ C), p1, p2))

= 1
d vol(H ∩ C) · (⟨u, p1⟩ − ⟨u, p2⟩)

> 1
d vol K · (⟨u, p1⟩ − ⟨u, p2⟩)

which implies that ⟨u, p1⟩ − ⟨u, p2⟩ < h, giving a contradiction since we chose h to be the
width of C.

It is well-known that it is #P -hard to compute volumes of polytopes in arbitrary dimen-
sion, when presented in facet or vertex descriptions [BW91; DF88; Kha93; Law91]. We can
therefore combine these classical results with Lemma 4.7, yielding that it is hard to ﬁnd the
slice of a polytope with maximal volume.
 28

Proposition 4.8. Let P be a rational polytope of arbitrary dimension. It is #P -hard to
compute the volume of the hyperplane section P ∩ H with largest volume.

Proof. Suppose by contradiction that one could compute the volume of the largest hyperplane
section of any polytope P eﬃciently. Now consider the pyramid P = conv(Q, ( p
h )) where
p ∈ Q, h > 0 and Q is a zonotope or an order polytope, or any polytope for which it is
known that it is #P -hard to compute the volume (for details see [BW91; DF88; DGH98]).
By Lemma 4.7 we can chose h > 0 in such a way that the section of P with largest volume is
actually Q. This implies, by our hypothesis, that we could compute the volume of Q eﬃciently
too, which gives a contradiction.

Proposition 4.8 implies that, given a family of polytopes, computing their hyperplane
sections with the largest volume is in general a hard task. However, by Theorem 1.3(i), with
our hyperplane arrangements we can compute it in polynomial time when the dimension of
the polytopes in the family is ﬁxed. Similarly, by Theorem 1.3(ii) and (iv) we can detect
the slices with the maximum number of vertices. The following proposition shows that the
weighted analogue of this task is N P -hard. Furthermore we show that same holds for the of
maximizing the number of vertices which are contained in the intersection of P with a central
halfspace.

Proposition 4.9. Let P be a polytope of arbitrary dimension with weights on its edges. It
is N P -hard to compute the hyperplane section P ∩ H that maximizes the sums of weights of
edges it intersects. Similarly, given an arbitrary polytope with vertices in a sphere with center
o, ﬁnding a halfspace section, for hyperplanes passing through o, that maximizes the number
of vertices inside the halfspace is N P -hard for arbitrary dimension.

Proof. The hardness proof will be a reduction to the It is well-known the MAX-CUT problem
is NP-hard (it is in the original list of famous NP-hard problems in [GJ79]). W Note that
every graph G with N nodes is a subgraph of the complete graph KN , which is the graph
of the (N − 1)-dimensional simplex ∆N . We assign weight 1 to the edges of G and zero
otherwise. Now note that every subset of vertices of ∆N can be separated by a hyperplane as
long as edges that are not in G have weight zero they do not count in the weighted cuts. Thus,
solving the max cut on the original graph G is equivalent to solving the task of Theorem 1.3
(iii) for vertices inside the simplex ∆N . We have proved that the problem is already hard
for simplices whose edges have weights zeros and ones, therefore the hardness of the stronger
statement in the proposition follows.
For the second part of the statement, notice that the densest hemisphere problem, men-
tioned already in Subsection 4.1, is a special case of Theorem 1.3 (iv), where the vertices of
the polytope are taken on the sphere. Therefore its hardness directly implies hardness for our
statement. Now, in a now classic paper in computational geometry Johnson and Preparata
showed when d is ﬁxed there exists a polynomial time algorithm which solves the problem
in polynomial time [JP78]. But they also showed densest hemisphere is known to be N P -
hard when the dimension d are arbitrary, which implies our statement is hard in arbitrary
dimension.

To conclude, we conjecture that this is N P -hard even without weights and more in general
for all dimensions of faces. We also conjecture that it is #P -hard to compute the best
projection. This is suggested by the fact that it is hard to compute the volume of zonotopes
as this implies that computing the volumes of projections of polytopes is hard [DGH98].

29

Conjectures. Let P be a polytope. Then,

(i ) it is N P -hard to ﬁnd a hyperplane H which maximizes the number of i-dimensional
faces of P ∩ H.

(ii ) it is #P -hard to ﬁnd a hyperplane H which maximizes the volume of the orthogonal
projection of P onto H.

(iii ) it is N P -hard to ﬁnd a central hyperplane H0 which maximizes the volume of the half-
space section P ∩ H +
0 .

5 Experimental results

In this last section, we present some explicit computations carried out using the algorithms
from the proofs of Theorems 2.5, 2.12, 3.4 and 3.10. We present slices of maximal volume of all
ﬁve Platonic solids, optimal slices of the 3-dimensional permutahedron for various optimality
criteria, and present the diﬀerent combinatorial types of polytopes which can occur as aﬃne
hyperplane sections of the cross-polytope of dimension 4 and 5.
Taking into account the complexity analysis from Section 4, we chose to use the approach
from Subsection 3.2 to compute general aﬃne hyperplane sections. Since the maximum
volume slice of a centrally symmetric polytope is always a central section, we used the ap-
proach from Subsection 2.1 to ﬁnd the slice of maximum volume for the centrally symmetric
Platonic solids. We implemented the algorithm in SageMath (version 9.2) [Sag21] for
all approaches, which computes the respective arrangements and the rational functions, or
representatives of the combinatorial properties respectively. The implementations of all al-
gorithms are available upon request. The maximization relies on the Maximize-command of
Mathematica (version 13.2) [Wol22].
We emphasize that all computations have been performed on an ordinary laptop, and that
our implementations can be largely optimized. For example, the computation for each region
is independent and thus, after ﬁnishing the computation of the regions, this process can be
parallelized.

Example 5.1 (Permutahedron). Let P ⊂ R4 be the 3-dimensional permutahedron deﬁned as
the convex hull of the permutations of (1, 2, 3, 4). This is a 3-dimensional polytope contained
in the hyperplane {x1 + x2 + x3 + x4 = 10} ⊂ R4 having Euclidean volume 32. One of the
hyperplane sections of P with maximum volume is the convex hull of the points

(1, 2, 3, 4), (1, 3, 2, 4), (2, 4, 1, 3), (3, 4, 1, 2), (4, 3, 2, 1), (4, 2, 3, 1), (3, 1, 4, 2), (2, 1, 4, 3).

The other such slices can be obtained by symmetry. The hyperplane in the aﬃne span of P
which produces that section has equation

{x1 + x2 + x3 + x4 = 10} ∩ {x1 + x4 = 5},

and the volume of the section is 14. This is visualized in Figure 1a in the introduction.
On the other hand, the slice of P through the origin having minimal volume is provided
by the intersection of P with

{x1 + x2 + x3 + x4 = 10} ∩ {x1 − x2 = 0},

30

and the volume of this polygon is 8√2. It is the convex hull of the points

( 3
2 , 3
2 , 3, 4), ( 3
2 , 3
2 , 4, 3), ( 5
2 , 5
2 , 1, 4), ( 5
2 , 5
2 , 4, 1), ( 7
2 , 7
2 , 1, 2), ( 7
2 , 7
2 , 2, 1),

displayed in Figure 1b. Notice that this is the slice of the permutahedron ﬁxed by the
permutation σ = (12), object of interest for [ASVM21].
From a purely combinatorial point of view, there are eight diﬀerent types of slices of the
permutahedron. These are polygons with 3, 4, . . . , 10 vertices. A section with 10 vertices is
shown in Figure 1c. Figure 10 presents the three optimal slices discussed in this example,
projected onto their aﬃne spans. ⋄

(a) Slice of maximum volume. (b) Slice of minimum volume
containing the origin. (c) Slice with maximum num-
ber of vertices.

Figure 10: Optimal slices of the 3-permutahedron for diﬀerent optimality criteria.

Example 5.2 (Platonic solids and maximum volume). Using our algorithm, we can ﬁnd
the slice with the largest volume of the Platonic solids. Due to their symmetries, such a
hyperplane is not unique. We give here the description of one possible answer. The others
can be recovered using the symmetries of the polytopes. We summarize our ﬁndings in Table 3
and we visualize them in Figure 11. We point out the surprising case of the dodecahedron, for
which the slice with the largest volume does not contain any vertex of the dodecahedron. ⋄

Figure 11: The Platonic solids and their pink hyperplane section (unique up to
symmetry) with the largest volume.
 31

P vertices of P vol P hyperplane H vol(P ∩ H)

tetrahedron (±1, 0, − 1√2 ), 2
√2
3 2x + 1 = √2z √3
(0, ±1, 1√2 )

cube (±1, ±1, ±1) 8 x + y = 0 4
√2

octahedron
 (±1, 0, 0),
 4
3 z = 0 2(0, ±1, 0),

(0, 0, ±1)

icosahedron
 (0, ± 1
2 , ±( √
5+1
4 )
)
,
 5(
√
5+3)
12 z = 0 (
√5+1)(
√5+3)
8 ∼ 2.12
( ± ( √
5+1
4 ), 0, ± 1
2 )
,
( ± 1
2 , ±( √5+1
4 ), 0
)

dodecahedron
 (0, ±(√5 − 1), ±(2
√5 − 4))
 400 − 176
√5 x = √5−1
2 z
 320(15127
√5−33825)

(3
√
5−7)4(
√5−1)
√−2√5+10
(±(2
√5 − 4), 0, ±(
√5 − 1))

(±(
√5 − 1), ±(2
√5 − 4), 0) ∼ 4.49
(±(√5 − 3), ±(3 − √5), ±(3 − √5))

Table 3: The sections of maximum volume of the Platonic solids.

Example 5.3 (Cross-polytope and combinatorial types). How many combinatorial types of
aﬃne hyperplane sections P ∩ H can occur when P is a cross-polytope? Using our algorithm,
we obtained that if P is the 3-dimensional cross-polytope, its (2-dimensional) hyperplane
sections can be of four combinatorial types: a triangle, a quadrilateral, a pentagon or an
hexagon. We note that the pentagon can only be obtained when the deﬁning hyperplane
contains a vertex of the cross-polytope.
If P is the 4-dimensional cross-polytope, then we get nine diﬀerent combinatorial types,
summarized in Table 4. We compute this by ﬁrst computing the sweep arrangement R↑(P ),
which consists of 384 maximal regions, and then sample a direction u ∈ R for each of the 1696
cones in R↑(P ) that have dimension at least 1. We then construct the arrangement Cu
↑ (P ) of
parallel hyperplanes, and store the combinatorial type of one hyperplane section for each cell
of the arrangement.
The sweep arrangement of the 5-dimensional cross-polytope has 24482 cones of positive
dimension, 3840 of which are of dimension 5. After running our algorithm, we get only 14
distinct combinatorial types of hyperplane sections. These are summarized in Table 5. We
point out that both in the case of dimension 4 and 5, there are exactly two combinatorial
types of sections of the cross-polytope whose f -vectors agree. These maximize the number of
k-dimensional faces for all k.
Finally, we note the duality between intersections and projections, as discussed in Sub-
section 2.3. Since the cross-polytope is polar to the cube, the duality is inherited by their
sections and projections. Therefore, we deduce that there are 5, 9, 14 combinatorial types of
projections of the 3, 4, 5-dimensional cube onto a hyperplane, respectively. ⋄

32

P ∩ H

f -vector (4, 6, 4) (6, 12, 8) (8, 18, 12)

H x1 + x2 + x3 + x4 = 1 2x1 = 1 x1 + x2 + x3 = 0

P ∩ H

f -vector (8, 17, 11) (9, 19, 12) (10, 20, 12)

H 2x1 + 2x2 + x3 + x4 = 1 2x1 + 2x2 + x3 = 1 2x1 + 2x2 = 1

P ∩ H

f -vector (10, 21, 13) (12, 24, 14) (12, 24, 14)

H 2x1 + 2x2 + 2x3 + x4 = 1 x1 + x2 + x3 + x4 = 0 2x1 + 2x2 + 2x3 = 1

Table 4: The nine pink polytopes are all possible combinatorial types of hyper-
plane sections of the 4-dimensional cross-polytope.

33

P ∩ H

f -vector (5, 10, 10, 5) (8, 24, 32, 16) (10, 34, 48, 24) (11, 36, 48, 23)

H x1 + x2 + x3 2x1 = 1 x1 + x2 2x1 + 2x2 + x3
+x4 + x5 = 1 +x3 = 0 +x4 + x5 = 1

P ∩ H

f -vector (12, 39, 51, 24) (13, 41, 52, 24) (14, 42, 52, 24) (14, 48, 62, 28)

H 2x1 + 2x2 2x1 + 2x2 2x1 + 2x2 = 1 x1 + x2
+x3 + x4 = 1 +x3 = 1 +x3 + x4 = 0

P ∩ H

f -vector (14, 46, 59, 27) (16, 51, 63, 28) (17, 54, 66, 29) (18, 54, 64, 28)

H 2x1 + 2x2 + 2x3 2x1 + 2x2 2x1 + 2x2 + 2x3 2x1 + 2x2
+x4 + x5 = 1 +2x3 + x4 = 1 +2x4 + x5 = 1 +2x3 = 1

P ∩ H

f -vector (20, 60, 70, 30) (20, 60, 70, 30)
H 2x1 + 2x2 + 2x3 + 2x4 = 1 x1 + x2 + x3 + x4 + x5 = 0

Table 5: The edge-graphs of the combinatorial types of sections of the 5-
dimensional cross-polytope. The graphs alone distinguish the combinatorial type.

Acknowledgements. This work was started during a visit to the Max Planck Institute
in Leipzig and then fully developed at the Institute for Computational and Experimental
Research Mathematics of Brown University (an NSF institute supported by the National
Science Foundation under Grant No. DMS-1929284), during the semester program “Discrete
Optimization: Mathematics, Algorithms, and Computation”. Marie-Charlotte Brandenburg
was funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) –
SPP 2298. We are grateful to Francisco Criado Gallart for suggesting the proof of Lemma 4.7
and allowing us to include it in our paper. We want to thank Amitabh Basu, Saugata Basu,
Peter B¨urgisser, Daniel Dadush, Jim Lawrence, Michael Roysdon, Martin Skutella, L´aszl´o
V´egh, Stefan Weltge, and other participants for suggestions and comments.

34

References

[ASVM21] Federico Ardila, Anna Schindler, and Andr´es R. Vindas-Mel´endez. “The equivariant
volumes of the permutahedron”. In: Discrete Comput. Geom. 65.3 (2021), pp. 618–635.
issn: 0179-5376. doi: 10.1007/s00454-019-00146-2.

[Bal86] Keith Ball. “Cube slicing in Rn”. In: Proc. Amer. Math. Soc. 97.3 (1986), pp. 465–473.
issn: 0002-9939. doi: 10.2307/2046239.

[Bal89] Keith Ball. “Volumes of sections of cubes and related problems”. In: Geometric aspects
of functional analysis (1987–88). Vol. 1376. Lecture Notes in Math. Springer, Berlin,
1989, pp. 251–260. doi: 10.1007/BFb0090058.

[Bar02] Alexander Barvinok. A course in convexity. Vol. 54. Graduate Studies in Mathematics.
American Mathematical Society, Providence, RI, 2002, pp. x+366. isbn: 0-8218-2968-8.
doi: 10.1090/gsm/054.

[BBDL+11] Velleda Baldoni, Nicole Berline, Jesus A. De Loera, Matthias K¨oppe, and Michele
Vergne. “How to integrate a polynomial over a simplex”. In: Math. Comp. 80.273
(2011), pp. 297–325. issn: 0025-5718. doi: 10.1090/S0025-5718-2010-02378-6.

[BBMS22] Katalin Berlow, Marie-Charlotte Brandenburg, Chiara Meroni, and Isabelle Shankar.
“Intersection bodies of polytopes”. In: Beitr¨age zur Algebra und Geometrie. Contri-
butions to Algebra and Geometry 63.2 (2022), pp. 419–439. issn: 0138-4821. doi: 10.
1007/s13366-022-00621-7.

[BKS94] Louis J. Billera, Mikhail. M. Kapranov, and Bernd Sturmfels. “Cellular strings on
polytopes”. In: Proc. Amer. Math. Soc. 122.2 (1994), pp. 549–555. issn: 0002-9939.
doi: 10.2307/2161048.

[BM23] Marie-Charlotte Brandenburg and Chiara Meroni. “Intersection Bodies of Polytopes:
Translations and Convexity”. 2023. arXiv: 2302.11764.

[BP99] Alexander Barvinok and James E. Pommersheim. “An algorithmic theory of lattice
points in polyhedra”. In: New perspectives in algebraic combinatorics (Berkeley, CA,
1996–97). Vol. 38. Math. Sci. Res. Inst. Publ. Cambridge Univ. Press, Cambridge,
1999, pp. 91–147.

[BPR06] Saugata Basu, Richard Pollack, and Marie-Fran¸coise Roy. Algorithms in real algebraic
geometry. Second. Vol. 10. Algorithms and Computation in Mathematics. Springer-
Verlag, Berlin, 2006, pp. x+662. isbn: 978-3-540-33098-1. doi: 10 . 1007 / 3 - 540 -
33099-2.

[BS92] Louis J. Billera and Bernd Sturmfels. “Fiber polytopes”. In: Ann. of Math. (2) 135.3
(1992), pp. 527–549. issn: 0003-486X. doi: 10.2307/2946575.

[BW91] Graham Brightwell and Peter Winkler. “Counting linear extensions”. In: Order 8.3
(1991), pp. 225–242. issn: 0167-8094. doi: 10.1007/BF00383444.

[CF86] G. Don Chakerian and Paul Filliman. “The measures of the projections of a cube”. In:
Studia Sci. Math. Hungar. 21.1-2 (1986), pp. 103–110. issn: 0081-6906.

[CL91] G. Don Chakerian and Dave Logothetti. “Cube slices, pictorial triangles, and probabil-
ity”. In: Math. Mag. 64.4 (1991), pp. 219–241. issn: 0025-570X. doi: 10.2307/2690829.

[DF88] Martin E. Dyer and A. M. Frieze. “On the complexity of computing the volume of
a polyhedron”. In: SIAM J. Comput. 17.5 (1988), pp. 967–974. issn: 0097-5397. doi:
10.1137/0217060.

[DGH98] Martin E. Dyer, Peter Gritzmann, and Alexander Hufnagel. “On the complexity of
computing mixed volumes”. In: SIAM J. Comput. 27.2 (1998), pp. 356–400. issn: 0097-
5397. doi: 10.1137/S0097539794278384.

35

[DLRS10] Jes´us A. De Loera, J¨org Rambau, and Francisco Santos. Triangulations. Vol. 25. Algo-
rithms and Computation in Mathematics. Structures for algorithms and applications.
Springer-Verlag, Berlin, 2010, pp. xiv+535. isbn: 978-3-642-12970-4. doi: 10.1007/
978-3-642-12971-1.

[FH22] Ansgar Freyer and Martin Henk. “Bounds on the lattice point enumerator via slices and
projections”. In: Discrete Comput. Geom. 67.3 (2022), pp. 895–918. issn: 0179-5376.
doi: 10.1007/s00454-021-00310-7.

[Fil92] Paul Filliman. “The volume of duals and sections of polytopes”. In: Mathematika 39.1
(1992), pp. 67–80. issn: 0025-5793. doi: 10.1112/S0025579300006860.

[FMGN97] Hiroshi Fukuda, Nobuaki Muto, Kikuko Goto, and Gisaku Nakamura. “Sections of
hyper-cube in ﬁve dimensions”. In: Forma 12.1 (1997), pp. 15–33. issn: 0911-6036.

[FSTT91] Komei Fukuda, Shigemasa Saito, Akihisa Tamura, and Takeshi Tokuyama. “Bounding
the number of k-faces in arrangements of hyperplanes”. In: Discrete Appl. Math. 31.2
(1991). First Canadian Conference on Computational Geometry (Montreal, PQ, 1989),
pp. 151–165. issn: 0166-218X. doi: 10.1016/0166-218X(91)90067-7.

[Gar06] Richard J. Gardner. Geometric tomography. Second. Vol. 58. Encyclopedia of Mathe-
matics and its Applications. Cambridge University Press, New York, 2006, pp. xxii+492.
isbn: 9781107341029. doi: 10.1017/CBO9781107341029.

[GJ79] Michael R. Garey and David S. Johnson. Computers and intractability. A Series of
Books in the Mathematical Sciences. A guide to the theory of NP-completeness. W. H.
Freeman and Co., San Francisco, Calif., 1979, pp. x+338. isbn: 0-7167-1045-5.

[GK94a] Peter Gritzmann and Victor Klee. “On the complexity of some basic problems in
computational convexity. I. Containment problems”. In: Discrete Math. 136.1-3 (1994).
Trends in discrete mathematics, pp. 129–174. issn: 0012-365X. doi: 10.1016/0012-
365X(94)00111-U.

[GK94b] Peter Gritzmann and Victor Klee. “On the complexity of some basic problems in com-
putational convexity. II. Volume and mixed volumes”. In: Polytopes: abstract, convex
and computational (Scarborough, ON, 1993). Vol. 440. NATO Adv. Sci. Inst. Ser. C:
Math. Phys. Sci. Kluwer Acad. Publ., Dordrecht, 1994, pp. 373–466. doi: 10.1007/
978-94-011-0924-6_17.

[GK97] Peter Gritzmann and Victor Klee. “Computational convexity”. In: Handbook of discrete
and computational geometry. CRC Press Ser. Discrete Math. Appl. CRC, Boca Raton,
FL, 1997, pp. 491–515.

[GKZ23] Apostolos Giannopoulos, Alexander Koldobsky, and Artem Zvavitch. “Inequalities for
sections and projections of convex bodies”. 2023. arXiv: 2302.04347.

[GLPR12] Nick Gravin, Jean B. Lasserre, Dmitrii V. Pasechnik, and Sinai Robins. “The in-
verse moment problem for convex polytopes”. In: Discrete Comput. Geom. 48.3 (2012),
pp. 596–621. issn: 0179-5376. doi: 10.1007/s00454-012-9426-4.

[Gr¨u67] Branko Gr¨unbaum. Convex polytopes. Pure and Applied Mathematics, Vol. 16. With
the cooperation of Victor Klee, M. A. Perles and G. C. Shephard. Interscience Pub-
lishers John Wiley & Sons, Inc., New York, 1967, pp. xiv+456.

[JP78] David S. Johnson and Franco P. Preparata. “The densest hemisphere problem”. In:
Theoret. Comput. Sci. 6.1 (1978), pp. 93–107. issn: 0304-3975. doi: 10.1016/0304-
3975(78)90006-3.

[Kha93] Leonid Khachiyan. “Complexity of polytope volume computation”. In: New trends in
discrete and computational geometry. Vol. 10. Algorithms Combin. Springer, Berlin,
1993, pp. 91–101. doi: 10.1007/978-3-642-58043-7\_5.

36

[Kho06] Askold Khovanskii. “Combinatorics of sections of polytopes and Coxeter groups in
Lobachevsky spaces”. In: The Coxeter legacy. Amer. Math. Soc., Providence, RI, 2006,
pp. 129–157.

[KL22] Bo’az Klartag and Joseph Lehec. “Bourgain’s slicing problem and KLS isoperimetry
up to polylog”. In: Geom. Funct. Anal. 32.5 (2022), pp. 1134–1159. issn: 1016-443X.
doi: 10.1007/s00039-022-00612-9.

[Kla23] Bo’az Klartag. “Logarithmic bounds for isoperimetry and slices of convex sets”. 2023.
arXiv: 2303.14938.

[KM22] Bo’az Klartag and Vitali Milman. “The Slicing Problem by Bourgain”. In: Analysis at
Large: Dedicated to the Life and Work of Jean Bourgain. Ed. by Artur Avila, Michael
Th. Rassias, and Yakov Sinai. Cham: Springer International Publishing, 2022, pp. 203–
231. isbn: 978-3-031-05331-3. doi: 10.1007/978-3-031-05331-3_9.

[Kol05] Alexander Koldobsky. Fourier analysis in convex geometry. Vol. 116. Mathematical
Surveys and Monographs. American Mathematical Society, Providence, RI, 2005, pp. vi+170.
isbn: 0-8218-3787-7. doi: 10.1090/surv/116.

[K¨on21] Hermann K¨onig. “Non-central sections of the simplex, the cross-polytope and the
cube”. In: Adv. Math. 376 (2021), Paper No. 107458, 35. issn: 0001-8708. doi: 10.
1016/j.aim.2020.107458.

[KS21] Astrid Kousholt and Julia Schulte. “Reconstruction of convex bodies from moments”.
In: Discrete Comput. Geom. 65.1 (2021), pp. 1–42. issn: 0179-5376. doi: 10.1007/
s00454-020-00225-9.

[LA01] Jean B. Lasserre and Konstantin E. Avrachenkov. “The multi-dimensional version of
∫ b
a xpdx”. In: Amer. Math. Monthly 108.2 (2001), pp. 151–154. issn: 0002-9890. doi:
10.2307/2695528.

[Las21] Jean B. Lasserre. “Simple formula for integration of polynomials on a simplex”. In:
BIT 61.2 (2021), pp. 523–533. issn: 0006-3835. doi: 10.1007/s10543-020-00828-x.
url: https://doi.org/10.1007/s10543-020-00828-x.

[Law79] Jim Lawrence. “Cutting the d-cube”. In: J. Res. Nat. Bur. Standards 84.1 (1979), 51–
53 (1978). issn: 0022-4340. doi: 10.6028/jres.084.004.

[Law91] Jim Lawrence. “Polytope volume computation”. In: Math. Comp. 57.195 (1991), pp. 259–
271. issn: 0025-5718. doi: 10.2307/2938672.

[LT20] Ruoyuan Liu and Tomasz Tkocz. “A note on the extremal non-central sections of the
cross-polytope”. In: Adv. in Appl. Math. 118 (2020), pp. 102031, 17. issn: 0196-8858.
doi: 10.1016/j.aam.2020.102031.

[Lut88] Erwin Lutwak. “Intersection bodies and dual mixed volumes”. In: Adv. in Math. 71.2
(1988), pp. 232–261. issn: 0001-8708. doi: 10.1016/0001-8708(88)90077-1.

[MP88] Mathieu Meyer and Alain Pajor. “Sections of the unit ball of L
n
p ”. In: J. Funct. Anal.
80.1 (1988), pp. 109–123. issn: 0022-1236. doi: 10.1016/0022-1236(88)90068-7.

[MSZZ13] James Moody, Corey Stone, David Zach, and Artem Zvavitch. “A remark on the
extremal non-central sections of the unit cube”. In: Asymptotic geometric analysis.
Vol. 68. Fields Inst. Commun. Springer, New York, 2013, pp. 211–228. doi: 10.1007/
978-1-4614-6406-8\_9.

[NT22] Piotr Nayar and Tomasz Tkocz. “Extremal sections and projections of certain convex
bodies: a survey”. 2022. arXiv: 2210.00885.

[Pou22] Lionel Pournin. “Shallow Sections of the Hypercube”. In: Israel Journal of Mathematics
(Nov. 2022). doi: 10.1007/s11856-022-2400-9.

37

[PP15] Arnau Padrol and Julian Pfeiﬂe. “Polygons as sections of higher-dimensional poly-
topes”. In: Electron. J. Combin. 22.1 (2015), Paper 1.24, 16. doi: 10.37236/4315.

[PP21] Arnau Padrol and Eva Philippe. “Sweeps, polytopes, oriented matroids, and allowable
graphs of permutations”. 2021. arXiv: 2102.06134.

[Sag21] The Sage Developers. SageMath, the Sage Mathematics Software System (Version 9.2).
2021. url: https://www.sagemath.org.

[Sch14] Rolf Schneider. Convex bodies: the Brunn-Minkowski theory. expanded. Vol. 151. Ency-
clopedia of Mathematics and its Applications. Cambridge University Press, Cambridge,
2014, pp. xxii+736. isbn: 978-1-107-60101-7.

[Sta07] Richard P. Stanley. “An introduction to hyperplane arrangements”. In: Geometric
combinatorics. Vol. 13. IAS/Park City Math. Ser. Amer. Math. Soc., Providence, RI,
2007, pp. 389–496. doi: 10.1090/pcms/013/08.

[Vaa79] Jeﬀrey D. Vaaler. “A geometric inequality with applications to linear forms”. In: Paciﬁc
J. Math. 83.2 (1979), pp. 543–553. issn: 0030-8730. url: http://projecteuclid.org/
euclid.pjm/1102784529.

[Wal68] David W. Walkup. “A simplex with a large cross section”. In: Amer. Math. Monthly
75 (1968), pp. 34–36. issn: 0002-9890. doi: 10.2307/2315102.

[Web96] Simon Webb. “Central slices of the regular simplex”. In: Geom. Dedicata 61.1 (1996),
pp. 19–28. issn: 0046-5755. doi: 10.1007/BF00149416.

[Wol22] Wolfram Research, Inc. Mathematica (Version 13.2). Champaign, IL. 2022. url: https:
//www.wolfram.com/mathematica.

[Zas75] Thomas Zaslavsky. “Facing up to arrangements: face-count formulas for partitions of
space by hyperplanes”. In: Mem. Amer. Math. Soc. 1.issue 1, 154 (1975), pp. vii+102.
issn: 0065-9266. doi: 10.1090/memo/0154.

[Zie95] G¨unter M. Ziegler. Lectures on polytopes. Vol. 152. Graduate Texts in Mathematics.
Springer-Verlag, New York, 1995, pp. x+370. isbn: 0-387-94365-X. doi: 10.1007/978-
1-4613-8431-1.

Marie-Charlotte Brandenburg
Max Planck Institute for Mathematics in the Sciences
Inselstraße 22, 04103 Leipzig, Germany
marie.brandenburg@mis.mpg.de

Jes´us A. De Loera
Department of Mathematics
One Shields Avenue, Davis CA 95616, USA
deloera@math.ucdavis.edu

Chiara Meroni
Institute for Computational and Experimental Research in Mathematics
121 South Main Street, Providence 02903, RI, USA
chiara_meroni@brown.edu
 38
