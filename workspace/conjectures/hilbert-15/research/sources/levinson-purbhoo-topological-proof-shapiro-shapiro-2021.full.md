<!-- source: https://arxiv.org/pdf/1907.11924 | converted from PDF -->

A topological proof of the Shapiro–Shapiro
conjecture

Jake Levinson and Kevin Purbhoo
†

July 12, 2021

Abstract

We prove a generalization of the Shapiro–Shapiro conjecture on Wronskians of
polynomials, allowing the Wronskian to have complex conjugate roots. We decom-
pose the real Schubert cell according to the number of real roots of the Wronski
map, and deﬁne an orientation of each connected component. For each part of
this decomposition, we prove that the topological degree of the restricted Wronski
map is given as an evaluation of a symmetric group character. In the case where
all roots are real, this implies that the restricted Wronski map is a topologically
trivial covering map; in particular, this gives a new proof of the Shapiro–Shapiro
conjecture.

1 Introduction

1.1 The Shapiro–Shapiro conjecture

In the mid-1990s, B. Shapiro and M. Shapiro formulated a striking conjecture about the
real Schubert calculus. They considered the real 1-parameter family of ﬂags osculating
a rational normal curve, and postulated the following: for every 0-dimensional inter-
section of Grassmannian Schubert varieties deﬁned relative to these osculating ﬂags,
all points of the intersection are real.
This conjecture is now a theorem of Mukhin, Tarasov, and Varchenko [18, 19], and
it is notable for several reasons. For typical real ﬂags, there is no reason to expect all
points of a 0-dimensional Schubert intersection to be real, and in general they will not
be. For most ﬂag varieties (in type A, and beyond) it is not known whether it is even
possible to choose ﬂags such that the solutions to a Schubert intersection problem are
all real. In the Grassmannian case, this was resolved by Vakil [35], but the Shapiro–
Shapiro conjecture provides a radically different way of addressing this question.

†Research supported by NSERC Discovery Grant RGPIN-04741-2018.

1arXiv:1907.11924v2  [math.AG]  8 Jul 2021
It has long been known that solutions to Schubert problems can be counted using
families of combinatorial objects, such as Young tableaux. It is, however, much more
difﬁcult to establish precise correspondences between these objects and individual so-
lutions. A core obstruction to such a project is the presence of monodromy among the
solutions. On one hand, standard geometric arguments involving Schubert varieties
rely on Kleiman’s transversality theorem [13], which tells us that Schubert varieties
deﬁned relative to generic ﬂags intersect transversely. This space of ﬂags has an in-
tractable fundamental group and, in general, Schubert problems with these ﬂags have
large monodromy groups [1, 15, 34]. The Shapiro–Shapiro conjecture, on the other
hand, uses ﬂags deﬁned with respect to a tuple of distinct points on RP
1 – data with a
small fundamental group. This affords the possibility of establishing an explicit map-
ping. Since the resolution of the Shapiro–Shapiro conjecture in 2005 (see below), this
project has been carried out successfully [24, 30].
There are several equivalent formulations of the Shapiro–Shapiro conjecture, which
connect it to other parts of algebraic geometry and representation theory. It can be
stated in terms of limit linear series [6], parameterized rational curves [14], families
(of Schubert problems and of representations) over the moduli space of stable curves
M 0,n [10, 29, 30, 37], and it has applications in combinatorics [24, 26], K-theory [9,
21], and control theory [4, 5, 28]. The geometry has also been generalized to other
homogeneous spaces, to elliptic curves, and more [2, 16, 20, 23, 25, 27].
The most elementary formulation involves Wronskians of polynomials. If f1, . . . , fd
are polynomials with coefﬁcients in a ﬁeld of characteristic zero, their Wronskian is the
polynomial
 Wr( f1, . . . , fd) :=
 |
|
|
|
|
|
|
|
|
 f1 f ′
1 f ′′
1 . . . f (d−1)
1
f2 f ′
2 f ′′
2 . . . f (d−1)
2
... ... ... ...
fd f ′
d f ′′
d . . . f (d−1)
d
 |
|
|
|
|
|
|
|
|
 .

Recall that a linear subspace v ⊂ C[z] is real if v is invariant under complex conjugation.
Equivalently, v is real if v has a basis in R[z].

Theorem 1.1 (Shapiro–Shapiro conjecture). If f1(z), . . . , fd(z) ∈ C[z] are linearly in-
dependent polynomials such that Wr( f1, . . . , fd) has only real roots, then the subspace of
C[z] spanned by ( f1, . . . , fd) is real.

Up to a scalar, the Wronskian depends only on the span of f1, . . . , fd, and is zero if
and only if f1, . . . , fd are linearly dependent; as such, Wr deﬁnes a map from a Grass-
mannian to projective space of the same dimension, called the Wronski map. Roughly,
the connection to Schubert calculus comes from the fact that Schubert varieties in this
Grassmannian map to linear spaces under the Wronski map.
Motivated by the Shapiro–Shapiro conjecture, Eremenko and Gabrielov [4] com-
puted the topological degree of the Wronski map over R. Their computation provides

2

a lower bound for the number of real solutions to certain Schubert intersection prob-
lems. Unfortunately this result is not strong enough to deduce Theorem 1.1: the lower
bound on the number of real solutions is always strictly less than the number of complex
solutions (except in the trivial cases, when the Grassmannian is a projective space).
Mukhin, Tarasov, and Varchenko [18, 19] have since given two proofs of Theo-
rem 1.1. The second proof moreover establishes the transversality of Shapiro-type
Schubert intersections. Both proofs are quite complicated: they use machinery from
quantum integrable systems, Fuchsian differential equations, and representation the-
ory. Their work establishes deep connections between these different areas and Schu-
bert calculus. However, their approach also has two major drawbacks. First, it is heavily
algebraic, using the Bethe Ansatz as a black box for solving systems of equations. As
such, the proof offers little geometric insight into why the Shapiro–Shapiro conjecture
is true. Second, there are several modiﬁcations and generalizations of the Shapiro–
Shapiro conjecture which are still open problems (see [32]). It is not known how to
adapt the Mukhin–Tarasov–Varchenko machinery to handle these related conjectures.
The purpose of this paper is to formulate and prove a generalization of Theorem 1.1,
using geometric and topological methods. We address not only the case where the roots
of Wr( f1, . . . , fd) are all real, but all cases where Wr( f1, . . . , fd) has real coefﬁcients.
When the roots are all real, we obtain a new, independent, conceptually simpler proof
of the Shapiro–Shapiro conjecture. Our main theorem is a degree computation, sim-
ilar in some respects to that of Eremenko and Gabrielov, but with a signiﬁcant twist.
The statement is less obvious, more powerful, and involves a surprising connection to
characters of the symmetric group.

1.2 Decomposition of real Schubert cells

The real Wronski map is a morphism from the real Grassmannian Gr(d, Rd+m−1[z]), the
space of d-planes inside the vector space of polynomials of degree at most d + m − 1,
to projective space. In this paper, we will mainly focus on the restriction of this map to
a Schubert cell.
Let Pn(R) denote the set of real monic polynomials of degree n. For a partition
λ ⊢ n with d parts, the real Schubert cell X λ(R) consists of all d-dimensional linear
subspaces of R[z] that have a basis of polynomials ( f1, . . . , fd), with deg fi = λi + d − i.
The Wronskian Wr( f1, . . . , fd) is a polynomial of degree n, which, up to a scalar multiple,
is independent of the choice of basis. Rescaling so that Wr( f1, . . . , fd) is monic, we obtain
a map Wr : X λ(R) → Pn(R); this is the Wronski map restricted to X λ(R).
Regarded as algebraic varieties Pn(R) and X λ(R) are both isomorphic to afﬁne
space An(R), and the Wronski map is a ﬁnite morphism from An(R) to itself. The alge-
braic degree of this morphism is f λ = #SYT(λ), the number of standard Young tableaux
of shape λ. This comes from a standard calculation in the Schubert calculus: the inter-
section number of n Schubert divisors with an n-dimensional Schubert variety. Notably,
we also have f λ = χ λ(1n), where χ λ is the irreducible symmetric group character asso-

3

ciated to the partition λ.
Regarded as a manifold, Pn(R) can be further decomposed according to the number
of real and non-real roots of polynomials. Let µ = 2n21n1 be a partition of n with parts
of size at most 2. Let Pn(µ) ⊆ Pn(R) be the subset consisting of polynomials with n1
distinct real roots, and n2 conjugate pairs of non-real roots. (Real roots are required to
be distinct, non-real roots are not.) The closure, Pn(µ), consists of all real polynomials
with at least n1 real roots (not necessarily distinct), and at least n2 conjugate pairs of
roots (which are no longer required to be non-real).

Example 1.2. The polynomial z(z2 + 1)
2 is in P5(221). The polynomial z3(z2 + 1) is in
both P5(213) and P5(221), but does not lie in any P5(µ).

Note that Pn(µ) is a contractible open semi-algebraic subset of Pn(R); in particular
it is a connected orientable (but as yet, not oriented) manifold. We orient all spaces
Pn(µ) simultaneously, in the obvious way, by ﬁxing an orientation of Pn(R) and deﬁning
the orientation of Pn(µ) to be the restriction the orientation of the ambient space.
Deﬁne X λ(µ) := Wr−1(Pn(µ)). Then X λ(µ) is an open semi-algebraic subset of
X λ(R); hence X λ(µ) is an orientable manifold. However, unlike Pn(µ), X λ(µ) typi-
cally has many components.
The restricted Wronski map Wr : X λ(µ) → Pn(µ) is a proper map of n-dimensional
manifolds over a connected base. Therefore, with the additional data of an orientation
of X λ(µ), this map has a well-deﬁned topological degree. However, there many possi-
ble choices of orientation for X λ(µ) (two choices for each component), and the degree
depends on the choice of orientation.
This brings us to our main result. We will deﬁne an orientation of X λ(µ), called the
character orientation.

Theorem 1.3. With the character orientation, the topological degree of the restricted
Wronski map Wr : X λ(µ) → Pn(µ) is equal to χ λ(µ).

As an immediate consequence, we obtain new proofs of some previously known
results. The ﬁrst is a bound on the number of real points in the ﬁbre of the Wronski
map. The algebraic degree of a ﬁnite morphism gives an upper bound for the number
of real preimages of any real point in the base; the topological degree gives a lower
bound.

Corollary 1.4. For g ∈ Pn(R), let Ng be the number of real points in the ﬁbre Wr−1(g),

counted with algebraic multiplicity. If g ∈ Pn(µ), then

|χ λ(µ)| ≤ Ng ≤ f λ .

Corollary 1.4 is equivalent to a special case of a theorem of Mukhin and Tarasov [17],
which gives a lower bound for the number of real points in a Schubert intersection,
with respect to (not-necessarily real) ﬂags osculating a rational normal curve. Such

4

Schubert problems were previously studied in [11, 12], where it was observed that
there are non-trivial restrictions on the number of real intersection points. Mukhin and
Tarasov’s theorem was the ﬁrst to offer an explanation for some of these observations,
using the machinery developed in [19]. Our approach can also be used to recover these
inequalities. In Section 5.3, we sketch how to extend our argument to the general
case using standard techniques. The two approaches are very different — Mukhin and
Tarasov’s argument is predominantly algebraic, whereas ours is topological — and it is
not clear why they produce exactly the same inequalities.
In the case where µ = 1n, the lower and upper bounds in Corollary 1.4 agree,
and we deduce the following statement, which is a formulation of the Shapiro–Shapiro
conjecture (equivalent to Theorem 1.1).

Corollary 1.5. Wr : X λ(1n) → Pn(1n) is a topologically trivial covering map of degree
f λ.
 Here, the statement about the degree is immediate from Corollary 1.4, and the
fact that the map is topologically trivial follows from an argument of Eremenko and
Gabrielov (see Section 6.2 for details). Theorem 1.3 and Corollaries 1.4 and 1.5 also
have straightforward generalizations in which the Schubert cell X λ(R) is replaced by
an open Richardson variety. We discuss these in Section 6.1.
Although Theorem 1.3 does not imply the strong transversality statement proved by
Mukhin, Tarasov, and Varchenko in [19], it does imply some important special cases of
it. For example, when rephrased in terms of Schubert intersections, Corollary 1.5 asserts
that a Shapiro-type intersection of n Schubert divisors with an n-dimensional Schubert
variety is transverse. There are a few other similar corollaries, which we discuss in Sec-
tion 6.2. A number of known applications of the Shapiro–Shapiro conjecture depend on
these special cases, but do not require the full power of the Mukhin–Tarasov–Varchenko
transversality theorem. For example, the geometric proof of the Littlewood-Richardson
rule in [24] and the cyclic sieving results in [26] rely only on these special cases, and
are thus consequences of Theorem 1.3.

1.3 Aspects of the character orientation

The key to Theorem 1.3 and the main novelty of this paper is the deﬁnition of the
character orientation. In Section 1.4, we explain how this deﬁnition works in the special
case where λ = (n−1, 1): this case is particularly accessible and will serve as a recurring
example throughout the paper. In the general case, the deﬁnition requires additional
background on the Wronski map, and will be given in Section 3. For now, we mention
three features that are partially inferrable from the statement of Theorem 1.3.

1. Although X λ(µ) is an open submanifold of X λ(R), in general the character ori-
entation of X λ(µ) is not a restriction of some orientation of the ambient space
X λ(R). If it were, then the degree of Wr : X λ(µ) → Pn(µ) would be equal to the

5

degree of the total map Wr : X λ(R) → Pn(R), and hence would be independent
of µ. Instead, the deﬁnition of the character orientation begins by choosing an
orientation on ambient space X λ(R); we then twist the orientation by a certain
real regular function. As such, some components of X λ(µ) will be oriented the
same as the ambient orientation, and some will be oriented opposite to it.

2. The character orientation is deﬁned globally on each component of X λ(µ), rather
than locally. This is more or less mandatory, because a priori, we do not know
enough about the topology of X λ(µ) to make any kind of local to global argu-
ments.

3. The character orientation exhibits a kind of skew-symmetry with respect to Grass-
mann duality. If λ∗ denotes the conjugate partition to λ, there is an isomorphism
δ : X λ∗(R) → X λ(R) such that Wr ◦ δ is the Wronski map on X λ∗(R). This
restricts to a diffeomorphism δ : X λ∗(µ) → X λ(µ). Algebraically, X λ(µ) and
X λ∗(µ) are indistinguishable. Yet according to Theorem 1.3, the Wronski map
can have different topological degrees on these two spaces. The difference is only
a sign, since χ λ∗(µ) = (−1)n2χ λ(µ), but it is not a global sign (it depends on µ).
This seems bizarre, as it implies that the orientation cannot depend only on the
abstract geometry of the Wronski map. The situation is reconciled by the fact
that there is a second orientation on X λ(µ) called the dual character orientation,
which is interchanged with the character orientation under δ. We show that the
two orientations coincide on X λ(µ) if n2 is even, and are opposites if n2 is odd,
which explains the signs.

Once we have formulated this deﬁnition, our proof of Theorem 1.3 proceeds along
the following lines. For each µ we choose a polynomial hµ(z) ∈ Pn(µ), such that we can
identify all points in the ﬁbre Wr
−1(hµ). We label these points by tableaux. The topolog-
ical degree of the map Wr : X λ(µ) → Pn(µ) is then a signed count of points in the ﬁbre
(the sign is positive if the Wronski map is locally orientation preserving, and negative
otherwise). To compute the signs, we connect up all of these points by a network of
paths in X λ(R), and count the number of sign changes along each path. Since the points
are labelled by tableaux, we are left with a problem of counting certain tableaux with
signs. We recognize this enumeration problem as a case of the Murnaghan–Nakayama
rule, which gives us the answer as a character evaluation.

1.4 An example

We illustrate Theorem 1.3 with an elementary example: the case where λ = (n − 1, 1).
Here, to compute Wr
−1(g) for g ∈ Pn(R), we are looking for polynomials ( f1, f2) such
that deg( f1) = n, deg( f2) = 1 and

Wr( f1, f2) = f1 f ′
2 − f ′
1 f2 = g . (1.1)

6

Two solutions to this equation represent the same point of X λ(R), if they are linearly
equivalent, i.e. they are bases for the same subspace of R[z].
We claim that Wr−1(g) ⊂ X λ(R) can be identiﬁed with the critical points of g. To see
this, take derivatives of both sides of the equation (1.1), which gives f1 f ′′
2 − f ′′
1 f2 = g ′.
Since f2 is a linear polynomial, f ′′
2 = 0, and we obtain

− f ′′
1 f2 = g ′ .

It follows that all solutions to (1.1) are of the form where f2(z) = z − c, g ′(c) = 0.
Furthermore, it is easy to check that if g ′(c) = 0, then up to linear equivalence, there
is a unique polynomial f1 such that Wr( f1(z), z − c) = g(z). Thus for λ = (n − 1, 1), we
identify X λ(R) with
 {(g, c) ∈ Pn(R) × A1(R) | g ′(c) = 0} .

The Wronski map is identiﬁed with the projection onto the ﬁrst factor.
From this description, we see immediately that Corollary 1.5 is true for λ = (n−1, 1):
if g is a degree n polynomial with n distinct real roots then g has n − 1 = f λ distinct real
critical points. There are n − 1 components of X λ(1n): the ith component is the set of
pairs (g, c) such that g ∈ Pn(1n), and c is the unique critical point of g between the ith

and (i + 1)
th smallest roots of g; this clearly maps diffeomorphically to Pn(1n).
Before we consider Theorem 1.3, let us ﬁrst compute the topological degree of the
full map Wr : X λ(R) → Pn(R). The Wronski map fails to be locally one-to-one in a
neighbourhood of (g, c) when c is a double or higher order critical point of g, i.e. when
g ′(c) = g ′′(c) = 0. Thus we see that the Jacobian of the Wronski map is, up to a scalar,
the function ∂ Wr : X λ(R) → R, ∂ Wr(g, c) = g ′′(c) (here, the partial derivatives in
the Jacobian are computed with respect to afﬁne coordinates on X λ(R) and Pn(R)).
It follows that we can ﬁnd orientations of X λ(R) and Pn(R) such that the Wronski
map is locally orientation preserving at (g, c) ∈ X λ(R) if and only if (−1)n g ′′(c) > 0.
We call these the ambient orientations. (The global sign (−1)n is not necessary for this
example in isolation, but ensures that the Wronski map is locally orientation preserving
at (g, c0), where c0 is the smallest critical point of g, in accordance with conventions
used throughout this paper.)
To compute the topological degree of the Wronski map with respect to the ambient
orientations, we can pick any g ∈ Pn(R) with distinct real critical points, and count the
critical points of g with signs: c is counted positively if (−1)n g ′′(c) > 0, and negatively
if (−1)n g ′′(c) < 0 (see Figure 1.1, left). These signs must alternate, so the degree is 1
if n is even, and 0 if n is odd. This agrees with Eremenko and Gabrielov’s result (see
Section 5.2).
Now, let C be a component of X λ(µ). The character orientation of C is deﬁned
to be consistent with the ambient orientation if (−1)n−1 g(c) > 0 for all (g, c) ∈ C ,
and opposite to the ambient orientation if (−1)n−1 g(c) < 0 for all (g, c) ∈ C . One of
these two conditions must hold, because we cannot have g(c) = 0 for (g, c) ∈ C , or

7

+
 −
 +
 −
 +
 −
 +
 +
 −
 +
 +
 −

Figure 1.1: The signs of the critical points of a polynomial in P7(2
213), with respect to
the ambient orientation (left), and the character orientation (right).

else c would be a double real root of g. Thus, the Wronski map is locally orientation
preserving at (g, c) with respect to the character orientation if and only if − g′′(c)
g(c) > 0.
To compute the topological degree with respect to the character orientation, we
pick any g ∈ Pn(µ) with distinct critical points and count the critical points of g with
signs. This time, c is counted positively if − g ′′(c)
g(c) > 0, and negatively if − g′′(c)
g(c) < 0 (see
Figure 1.1, right). For example, if n1 > 0, we can take g to be a polynomial with n1
distinct real roots, and n1 − 1 distinct real critical points, which will all be counted with
positive signs. If n1 = 0, we can take g to have no real roots and 1 real critical point,
which is counted with a negative sign. In either case, we see that the topological degree
is n1 − 1 = χ λ(2n21n1), in agreement with Theorem 1.3.
We will revisit this example several times in Sections 2 and 3, to illustrate other
aspects of Theorem 1.3.

Remark 1.6. For every partition λ and g ∈ Pn(R), there is a function Θλ
g called the mas-
ter function, whose critical points are identiﬁed with Wr−1(g). This fact is the starting
point for Mukhin, Tarasov and Varchenko’s proof of Theorem 1.1 in [18]. In general,
Θλ
g is rational function of several variables, and the analysis of its critical points cannot
be carried out in an elementary way; λ = (n − 1, 1) is exceptionally nice because it is
the only case in which Θλ
g is a univariate function. Our proof of Theorem 1.3 is not
based on the master function, but instead generalizes this example in a different way.

1.5 Outline

Section 2 begins with an overview of the main properties of the Wronski map that will
be needed throughout the paper. These include the connection with Schubert varieties,
and an explicit formula for the Wronski map in coordinates. We then use these proper-
ties to compute certain points in the ﬁbre Wr
−1(g), in two important special cases. We
recall the statement of the Murnaghan–Nakayama rule, and state a lemma which labels

8

the real points in certain “special ﬁbres” of the Wronski map by Murnaghan–Nakayama
tableaux (Lemma 2.15).
In Section 3, we deﬁne the ambient orientation of Pn(R) and X λ(R), the character
orientation of X λ(µ), and the dual character orientation. For each of these orientations,
we consider how the sign of a point in X λ(R) changes when traversing certain paths.
We state two lemmas, which provide a collection of paths connecting up all of the real
points in the aforementioned special ﬁbres of the Wronski map (Lemmas 3.15 and 3.16).
Since the sign changes along these paths are predictable, we can compute the signs of
all points in each of our special ﬁbres. Theorem 1.3 follows from this computation.
To complete the argument, we still need to prove Lemmas 2.15, 3.15 and 3.16. This
is the goal of Section 4. We work with Speyer’s model of the Shapiro–Shapiro conjecture
[30], in which the Wronski map is replaced by a related family over the moduli space
of genus zero stable curves. The big advantage of this formulation is that it has a rich
boundary structure, on which explicit ﬁbre calculations can be carried out with relative
ease. This allows us to analyze ﬁbres and paths by degeneration arguments. We begin
Section 4, by reviewing Speyer’s construction, and explaining how to compute ﬁbres of
this map over stable curve that is a P1-chain. We prove Lemma 2.15 by replacing poly-
nomials with appropriate curves, and allowing these curves to degenerate to P1-chains.
The assertions of the lemma essentially translate into properties of this degeneration.
The paths in Lemmas 3.15 and 3.16 are constructed and analyzed using similar ideas.
In Section 5 we discuss Corollary 1.4 and other related results. We show that in
several cases, the lower bound in Corollary 1.4 is tight. We use the results of Section 3 to
give a quick proof of the Eremenko–Gabrielov lower bound, and compare these results.
We also discuss the relationship between Corollary 1.4 and the Mukhin–Tarasov bound
in more detail.
We conclude with some generalizations of our main results and open questions, in
Section 6.

Remark 1.7. Many of the geometric objects we are considering have a dual nature as al-
gebraic varieties/schemes over R and differentiable manifolds, and we will often move
back and forth between these points of view. For the most part, topological statements
(involving orientations, paths, continuity, etc.) use the analytic topology. When we talk
about ﬁbres of a morphism over R, we normally mean the scheme theoretic ﬁbre. It
should hopefully be clear from context how to interpret these types of statements.

2 Preliminaries

2.1 The Wronski map

We begin this section by recalling some of the fundamental properties of the Wronski
map. We omit proofs of results that are fairly well established, and refer the reader to
[24], [31] or [32] for further details or additional background.

9

Let F be a ﬁeld of characteristic zero. We denote the vector space of polynomials of
degree at most ℓ over F by Fℓ[z]. The Wronski map Wr : Gr(d, Fd+m−1[z]) → P(Fdm[z]),
maps a d-plane spanned by polynomials f1, . . . , fd to the line in Fdm[z] spanned by
Wr( f1, . . . , fd).
When the choice of ﬁeld F is not relevant to discussion at hand, we will sometimes
suppress it from our notation. In this case, we may also write the Wronski map as
Wr : Gr(d, d + m) → Pdm.
The group GL2(F) acts on Fℓ[z] by Möbius transformations. If φ =   φ11 φ12
φ21 φ22  ∈
GL2(F) and f (z) ∈ Fℓ[z], the action is given by

φ f (z) := (φ21z + φ11)
ℓ f • φ22z + φ12
φ21z + φ11
 − .

This induces a PGL2(F) action on Gr(d, Fd+m−1[z]) and P(Fdm[z]), and the Wronski map
is PGL2(F)-equivariant with respect to these actions.
We deﬁne a family of ﬂags over P1(F) = F ∪ {∞}:

F•(a) : F0(a) ⊂ F1(a) ⊂ · · · ⊂ Fd+m(a) .

For a ∈ F, Fi(a) := (z+a)d+m−iF[z]∩Fd+m−1[z] is the subspace of polynomials in Fd+m[z]
divisible by (z + a)d+m−i, i = 0, . . . , d + m. We also set Fi(∞) := Fi−1[z] = lima→∞ Fi(a).
We note that φ(F•(a)) = F•(φ(a)) for φ ∈ PGL2(F).
Let λ = (λ1, . . . , λd) be a partition, with m ≥ λ1 ≥ · · · ≥ λd ≥ 0. Then λ indexes a
Schubert cell relative to the ﬂag F•(a):

X ◦
λ(a) := x ∈ Gr(d, d+m) |
| dim(x ∩ F j(a)) − dim(x ∩ F j−1(a)) = η j, j = 1, . . . , d+m} ,

where η j = 1 if j = m + i − λi for some i, and η j = 0 otherwise. Its closure

X λ(a) := X ◦
λ(a)

is the Schubert variety. These conventions are such that |λ| is the codimension of X λ(a)
in Gr(d, d + m).
We will often identify the partition λ with its diagram, λ = {(i, j) | 1 ≤ i ≤ d, 1 ≤
j ≤ λi}, which is represented pictorially as an array of |λ| boxes, with λi boxes in
row i. We will write X (a) to denote the Schubert variety associated to the partition
= (1, 0, . . . , 0), X (a) for the partition = (2, 0, . . . , 0), etc.
The relationship between these Schubert varieties and the Wronski map is given by
the following lemma.

Lemma 2.1. Let x ∈ Gr(d, d + m), and let g = Wr(x).

(i) For a ∈ F, (z + a)
ℓ divides g(z) if and only if x ∈ X λ(a) for some partition λ ⊢ ℓ.
If (z + a)
ℓ is the largest power of (z + a) that divides g(z), then λ is unique and
moreover x ∈ X ◦
λ(a).
 10

(ii) deg(g) ≤ dm − ℓ if and only if x ∈ X λ(∞) for some λ ⊢ ℓ. If deg(g) = dm − ℓ,
then in fact λ is unique and moreover x ∈ X ◦
λ(∞).

It follows that Schubert varieties of the form X λ(a) intersect properly.

Lemma 2.2. Let a1, . . . , ak ∈ P1 be distinct, and let α
1, . . . , αk be partitions such that
∑k
i=1 |αi| = dm. the intersection
 X α1(a1) ∩ · · · ∩ X αk(ak)

is proper and hence a ﬁnite scheme of length equal to the Schubert intersection number∫

Gr(d,d+m)[X α1] . . . [X αk] .

The Wronski map Wr : Gr(d, d + m) → Pdm is a ﬁnite morphism [6]. Its degree
is the length of the ﬁnite scheme Wr
−1(g), for any g ∈ Pdm. This is independent of
F. If F is algebraically closed, then we can assume g(z) = ∏dm
i=1(z + ai), with distinct
roots. Lemma 2.1 shows that the ﬁbre is an intersection of dm Schubert divisors on
Gr(d, d + m), Wr−1(g) = X (a1) ∩ · · · ∩ X (adm) ,

and hence the degree is #SYT(md).
The Plücker coordinates on the Grassmannian are homogeneous coordinates [xλ]
indexed by the same partitions λ as the Schubert varieties. For x ∈ Gr(d, d + m), choose
a basis ( f1, . . . , fd), and let M be the d × (m + d) matrix Mi j = f ( j−1)
i (0). Then xλ is the
maximal minor of M , with columns 1 + λd, 2 + λd−1, . . . , d + λ1.

Proposition 2.3. In terms of Plücker coordinates, the Wronski map is

Wr(x; z) =
 dm∑

ℓ=0
 ∑

λ⊢ℓ f λxλ zℓ

ℓ! .

2.2 The Schubert cell X λ

The complementary partition to λ is λ∨ := (m − λd, . . . , m − λ1). The Schubert cell
X ◦
λ∨(∞) ⊂ Gr(d, d + m) will play a special role, and we denote it by X λ. The use of a
superscript is to indicate that |λ| is the dimension of X λ, rather than the codimension.
Concretely, X λ(F) is the variety of d-planes in F[z] that have a basis ( f1, . . . , fd), with
deg fi = λi + d − i. We note that this characterization is independent of m.
Now, ﬁx λ ⊢ n, and suppose κ = (κ1, . . . , κd) is another partition. We write κ ⊂ λ if
κi ≤ λi for all i. For a ∈ A1, the Schubert variety X κ(a) intersects the Schubert cell X λ

non-trivially if and only if κ ⊂ λ. The intersection

X λ
κ (a) := X κ(a) ∩ X λ

is a half-open Richardson variety.
When we restrict the Wronski map to X λ, the properties of the previous section
translate into the following facts:
 11

(i) The algebraic image of the Wronski map restricted to X λ(F) is the subvariety
of P(Fdm[z]) of polynomials of degree exactly n. Rescaling so that the leading
coefﬁcient is 1, we identify this image with Pn(F), the afﬁne space of monic poly-
nomials of degree n in F[z].

(ii) The subgroup B+ ⊂ PGL2(F) of upper triangular matrices acts on X λ(F) and
Pn(F) by afﬁne transformations, and the Wronski map is B+-equivariant.

(iii) If x ∈ X λ(F), and g = Wr(x), then (z + a)
ℓ divides g(z) if and only if x ∈ X λ
κ (a)
for some κ ⊢ ℓ.

(iv) The map Wr : X λ(F) → Pn(F) is a ﬁnite morphism of afﬁne varieties of degree
f λ. In this case, the degree computation follows from the fact that the ﬁbre over
g(z) = ∏n
i=1(z + ai) is

Wr−1(g) = X (a1) ∩ · · · ∩ X (an) ∩ X λ∨(∞) .

(v) For x ∈ X λ(F), the Plücker coordinates satisfy xκ = 0 for κ ̸⊂ λ, and can be nor-
malized so that xλ = 1. In terms of normalized Plücker coordinates, the Wronski
map Wr : X λ(F) → Pn(F) is

Wr(x; z) = zn + • f λ

n!
 −−1 n−1∑

ℓ=0
 ∑

κ⊢ℓ f κxκ zℓ

ℓ! . (2.1)

The Schubert cell X λ(F) is isomorphic to afﬁne space An(F). Explicitly, a point
x ∈ X λ(F) has a unique basis of polynomials ( f1, . . . , fd), of the form

fi(z) = zλi +d−i

(λi + d − i)! +
 λi∑

j=1 (−1)i+λ∗
j z j−λ∗
j +d−1

( j − λ∗
j + d − 1)! · x i j , (2.2)

where λ∗ denotes the conjugate partition. The coefﬁcients (x i j)(i, j)∈λ of these poly-
nomials give the afﬁne coordinates of the point x. The coordinate ring of X λ(F) is
F[x] := F[x i j | (i, j) ∈ λ].

Example 2.4. For λ = 532, here are the polynomials speciﬁed in (2.2).

f1(z) = + x11 + x12z − x13 z3

3! + x14 z5

5! + x15 z6

6! + z7

7!
f2(z) = − x21 − x22z + x23 z3

3! + z4

4!
f3(z) = + x31 + x32z + z2

2!

Remark 2.5. The precise signs and constants in (2.2) are not too important for most
practical purposes. They are chosen so that our afﬁne coordinates are a subset of the
normalized Plücker coordininates. This has the additional beneﬁt that the coordinates

12

are well-behaved under Grassmann duality. The duality isomorphism δ : X λ∗ → X λ is
simply deﬁned by x i j 7→ x ji in afﬁne coordinates. Using Proposition 2.3, one can show
that if Wr : X λ → Pn is the Wronski map on X λ, then Wr◦δ : X λ∗ → Pn is the Wronski
map on X λ∗.

Proposition 2.6. Suppose λ/κ has at most one box in each column, or at most one box in
each row. Then X λ
κ (0) is the afﬁne subspace of X λ deﬁned in afﬁne coordinates by xi j = 0
for (i, j) ∈ κ.

Proof. X λ
κ (0) is deﬁned in Plücker coordinates by xα = 0 for all α ⊂ λ such that κ ̸⊂ α.
In the case where λ/κ has at most one box in each column (or each row), the equations
xi j = 0, (i, j) ∈ κ are a subset of these deﬁning equations. This subset cuts out an
afﬁne space V of dimension |λ/κ|, and so X λ
κ (0) is a closed subvariety of V . Since
dim X λ
κ (0) = |λ/κ|, we have X λ
κ (0) = V .

By writing the Wronski map in afﬁne coordinates, we can solve some speciﬁc in-
stances of the inverse Wronskian problem by direct calculation. The most important
examples of this are given in the next two lemmas.

Lemma 2.7. Let κ ⊂ λ be a partition such that |κ| = n−1. If g(z) = zn−1(z + a) ∈ Pn(R),
then there is a unique (reduced) point x ∈ Wr−1(g) ∩ X λ
κ (0) and x is real.

Proof. Suppose the unique box of λ/κ is in row i1, and column j1. By Proposition 2.6,
X λ
κ (0) is deﬁned by x i j = 0, for (i, j) ̸= (i1, j1). Thus, (2.1) simpliﬁes to

Wr(x; z) = zn + • f λ

n!
 −−1 · f κ x i1 j1 zn−1

(n − 1)! .

Thus the unique solution to Wr(x) = g is given in afﬁne coordinates by x i1 j1 = af λ

nf κ ,
xi j = 0 for (i, j) ̸= (i1, j1).

The distance between two boxes (i1, j1) and (i2, j2) in the diagram of λ is deﬁned
to be |i1 − i2| + | j1 − j2|.

Lemma 2.8. Let κ ⊂ λ be a partition such that |κ| = n − 2. Let L be the distance between
the two boxes of the skew shape λ/κ. Let g(z) = zn−2(z + a1)(z + a2) ∈ Pn(R) (hence,
a1, a2 ∈ R or a1 = a2 ∈ C).

(i) If L = 1, then there is a unique (reduced) point x ∈ Wr−1(g) ∩ X λ
κ (0) and x is real.

(ii) If L > 1, then Wr
−1(g) ∩ X λ
κ (0) is a ﬁnite scheme of length two. The two points
x, x
′ ∈ Wr−1(g) ∩ X λ
κ (0) are identiﬁed with solutions to to a quadratic equation with
discriminant (a1 + a2)
2 − 4(1 − L−2)a1a2. Hence:

• If (a1 + a2)
2 − 4(1 − L−2)a1a2 > 0, then x, x
′ are distinct and real.

13

• If (a1 + a2)
2 − 4(1 − L−2)a1a2 = 0, then x = x
′ is a double real point.

• If (a1 + a2)
2 − 4(1 − L−2)a1a2 < 0, then x, x
′ are not real.

Proof. The proof of (i) is similar to Lemma 2.7, and we omit it. For (ii), suppose that
the positions of the two boxes of λ/κ are (i1, j1) and (i2, j2). Since L > 1, these are both
corners of λ. Let β 1 and β 2 denote the partitions of size n − 1, obtained by deleting
corners (i1, j1) and (i2, j2) from λ respectively. Proceeding as in the proof Lemma 2.7,
X λ
κ (0) is deﬁned by x i j = 0 for (i, j) ∈ κ, and (2.1) simpliﬁes to

Wr(x; z) = zn + • f λ

n!
 −−1 · Łf β 1 x i1 j1 zn−1

(n − 1)! + f β 2 x i2 j2 zn−1

(n − 1)! + f κ xi1 j1 x i2 j2 zn−2

(n − 2)!
 Ÿ .

Equating coefﬁcients of Wr(x) = g, and solving for xi1 j1 we obtain

nf β 1

f λ x 2
i1 j1 + (a1 + a2)x i1 j1 + (n − 1)
−1 f β 2

f κ a1a2 = 0 .

The discriminant of this quadratic equation is

(a1 + a2)
2 − 4n(n − 1)
−1 f β 1f β 2

f λf κ a1a2 .

Using the hook-length formula [7] for f λ, it is easy to check that n(n − 1)
−1 f β1 f β2

f λf κ =
(1 − L−2), from which the result follows.

2.3 Tableaux

Suppose µ = (µ1, . . . , µk) is a composition of n, i.e. an ordered list of positive integers
summing to n. There is a partition associated to µ, obtained by sorting the parts of µ in
decreasing order. We adopt the convention that whenever we use notation of the form
“ · (µ)” in a context where µ is supposed to be a partition, we will implicitly mean to
use this associated partition. For example, χ λ(µ) means χ λ evaluated at the partition
associated to µ.

Deﬁnition 2.9. A weakly increasing tableau of shape λ and content µ is a ﬁlling of the
diagram of λ with positive integer entries, weakly increasing along rows and columns,
such that µb of the entries are equal to b, for b = 1, . . . , k. We denote the set of all such
tableaux by Tab(λ; µ).

In particular, the set of standard Young tableaux of shape λ is SYT(λ) = Tab(λ; 1n).
For T ∈ Tab(λ; µ) let T (i, j) denote the entry in row i and column j. Let shape(T |≤b)
be the partition deﬁned by the entries of T less than or equal to b. Let shape(T |b) :=
shape(T |≤b)/shape(T |≤b−1) be the skew shape associated to the entries equal to b. We
note the following identity.
 14

Proposition 2.10. ∑

T ∈Tab(λ;µ)
 k∏

b=1 #SYT(shape(T |b)) = f λ .

The Murnaghan–Nakayama rule computes characters of symmetric group represen-
tations in terms of tableaux. We recall the statement.

Deﬁnition 2.11. T ∈ Tab(λ; µ) is a Murnaghan–Nakayama tableau if shape(T |b) is
a connected shape containing no 2 × 2 square, for all b = 1, . . . , k. We denote the set of
Murnaghan–Nakayama tableaux of shape λ and content µ by MN(λ; µ). The sign of a
Murnaghan–Nakayama tableau is

sgn(T ) :=
 k∏

b=1(−1)
rows(T |b)−1 .

where rows(T |b) the number of non-empty rows in shape(T |b).

Theorem 2.12 (Murnaghan–Nakayama rule).
∑

T ∈MN(λ;µ) sgn(T ) = χ λ(µ) .

We now specialize to the case where µi ∈ {1, 2}, for all i = 1, . . . , k. With this
assumption, several things simplify. For a tableau T ∈ Tab(λ; µ), shape(T |b) consists of
either

• a single box (iff µb = 1);
• two boxes forming a horizontal domino (i.e. in the same row);
• two boxes forming a vertical domino (i.e. in the same column); or
• two boxes that are non-adjacent.

Denote the number of b such that shape(T |b) falls into each of these cases by # (T ),
# (T ), # (T ), and # (T ) respectively. Proposition 2.10 reduces to the statement
∑

T ∈Tab(λ;µ) 2
# (T ) = f λ .

T is a Murnaghan–Nakayama tableau if and only if # (T ) = 0, in which case we have
sgn(T ) = (−1)
# (T ).

Example 2.13. For λ = 543, µ = (1, 1, 2, 2, 1, 1, 1, 2, 1), consider the tableau

T = 1 2 4 6 7
3 3 4 9
5 8 8 ∈ Tab(λ; µ) .

We have # (T ) = 6, # (T ) = 2, # (T ) = 1, and # (T ) = 0. Hence, T is a Murnaghan–
Nakayama tableau, with sgn(T ) = −1.
 15

2.4 Special ﬁbres of the Wronski map

We continue to assume that µ = (µ1, µ2, . . . , µk) is a composition of n, with µi ∈ {1, 2}
for i = 1, . . . , k. We now assign points in X λ to tableaux in Tab(λ; µ).
We begin working over the ﬁeld C((u)) of formal Laurent series. Note that if x(u) ∈
Gr(d, C((u))d+m), we can always take limu→0 x(u) to obtain a point in Gr(d, Cd+m). De-
ﬁne polynomials
 Hµ(u, z) :=
 k∏

b=1
  zµb + ( 1
2 uµb + 1
2 uµb+µb−1)
µb ,

where µb := n + 1 − ∑b
i=1 µi. Note that if we evaluate at any u ∈ (0, 1), Hµ(u, z) ∈
Pn(µ). The roots of Hµ are either of the form −u j or ± i
2 (u j + u j+1), where i denotes the
imaginary unit.

Example 2.14. For µ = (2, 1, 2, 2, 1),

Hµ(u, z) =  z2 + ( 1
2 u7 + 1
2 u8)
2 z + u6 z2 + ( 1
2 u4 + 1
2 u5)
2 z2 + ( 1
2 u
2 + 1
2 u3)
2 z + u
1 .

Lemma 2.15. Consider the Wronski map Wr : X λ(C((u))) → Pn(C((u))). The ﬁbre
Wr−1(Hµ) consists of f λ distinct points in X λ(C((u))). For each point x(u) ∈ Wr−1(Hµ),
the normalized Plücker coordinates  xκ(u)

κ⊂λ are power series with a positive radius of
convergence. For each T ∈ Tab(λ; µ), there is a set WT consisting of 2
# (T ) distinct points
in X λ(C((u))), with the following properties.

(a) ⋃
T ∈Tab(λ;µ) WT = Wr−1(Hµ).

(b) For x(u) ∈ WT , and b = 1, . . . , k,

lim
u→0
   1 0

0 uµb  x(u) ∈ X shape(T |≤b) ,

using the action of PGL2 on the Grassmannian.

(c) For x(u) ∈ WT , x(u) ∈ X λ(R((u))) if and only if T is a Murnaghan–Nakayama
tableau.

We prove Lemma 2.15 in Section 4.4. It follows that for ﬁxed λ, and for all sufﬁcient
small ϵ > 0, the following are true:

• For every µ and every point x ∈ Wr−1(Hµ), the series xκ(ϵ) converges for all κ ⊂ λ.

• For x(u) ∈ WT , the point x(ϵ) ∈ X λ(C), deﬁned by Plücker coordinates  xκ(ϵ)

κ⊂λ,
is real if and only if T is a Murnaghan–Nakayama tableau.
• All of the points x(ϵ) are distinct.

Pick such a suitable ϵ, and put hµ(z) := Hµ(ϵ, z) ∈ Pn(µ). For T ∈ MN(λ; µ) put
wT := x(ϵ) ∈ X λ(µ), where x(u) is the unique point in WT .

16

h13

1 2
3
 1 3
2
 h21

1 1
2
 1 2
1
 h12

Figure 2.1: Plots of the polynomials hµ, for λ = , and the Murnaghan–Nakayama
tableaux corresponding to each critical point.

Corollary 2.16. The ﬁbre Wr−1(hµ) is reduced, and the set of real points in Wr−1(hµ) is

{wT | T ∈ MN(λ; µ)} .

Remark 2.17. Lemma 2.15 could be stated much more generally: essentially, the proof
uses only the asymptotic behaviour of the roots of Hµ, as u → 0. As such, the def-
inition of Hµ is somewhat arbitrary, in that there are other choices that would work
equally well. However, Lemma 2.15 is not the only consideration. The choices we have
made here will be particularly convenient later on, for constructions involving paths in
Sections 4.5 and 4.6.

Example 2.18. Consider λ = . Here, ϵ = 1
2 is sufﬁciently small, and we have

h13(z) = (z + 1
8 )(z + 1
4 )(z + 1
2 )

h21(z) = (z2 + ( 3
16 )
2)(z + 1
2 )

h12(z) = (z + 1
8 )(z + ( 3
8 )
2) .

As explained in Section 1.4, when λ is of the form (n − 1, 1), the points of the ﬁbre
Wr−1(hµ) correspond to the critical points of hµ. The polynomials h13 and h21 each
have two real critical points, and h12 has zero real critical points. According to Corol-
lary 2.16, the real points of Wr−1(hµ) (hence the real critical points of hµ) are in bijec-
tion with tableaux in MN(λ, µ). Indeed, we have #MN( , 13) = #MN( , 21) = 2,
and #MN( , 12) = 0.
The precise identiﬁcation between critical points of hµ and Murnaghan–Nakayama
tableaux is as shown in Figure 2.1. We can verify this by computing of Wr
−1(Hµ) directly.
For example, for µ = 1
3, Hµ(u, z) = (z + u3)(z + u
2)(z + u), and the two points x0(u),

17

x1(u) of Wr−1(Hµ) are spanned by the following polynomials in R[[u]][z]:

x0(u) = 〈z3 + 3
2 u2z2 + 3u5z + · · · , z + 2
3 u + · · · 〉

x1(u) = 〈z3 + 2uz2 + 4u
4z + · · · , z + 1
2 u2 + · · · 〉 .

Here we have only explicitly written the leading term in u for each coefﬁcient of z.
Recall that the critical point associated to xi is the root of the linear polynomial in the
basis for xi; as u → 0, these roots are asymptotically − 2
3 u < − 1
2 u2, so x0 corresponds to
the smaller of the two critical points. To see which point corresponds to which tableau,
we use part (b) of Lemma 2.15.

lim
u→0
   1 0
0 u3 x0(u) = 〈 3
2 z2 + 3z, 2
3 〉 ∈ X lim
u→0
   1 0
0 u
3 x1(u) = 〈2z2 + 4z, 1
2 〉 ∈ X

lim
u→0
   1 0
0 u2 x0(u) = 〈z3 + 3
2 z2, 2
3 〉 ∈ X lim
u→0
   1 0
0 u
2 x1(u) = 〈2z2, z + 1
2 〉 ∈ X

lim
u→0
   1 0
0 u1 x0(u) = 〈z3, z + 2
3 〉 ∈ X lim
u→0
   1 0
0 u
1 x1(u) = 〈z3 + 2z2, z〉 ∈ X

This shows that x0 corresponds to 1 2
3 and x1 corresponds to 1 3
2 .

3 Orientations

3.1 Ambient orientations

We begin by ﬁxing orientations on afﬁne spaces Pn(R), and X λ(R), which we will refer
to as the ambient orientations. These will serve as a point of reference for deﬁning
orientations of Pn(µ) and X λ(µ). Each component of these will either be oriented the
same, or opposite to the ambient space in which it lies.
The degree of a map depends only on the relative orientations of the spaces: revers-
ing the orientations of both the domain and codomain leaves the degree unchanged.
Thus we can begin by making one choice without loss of generality. We select either ori-
entation as the ambient orientation for Pn(R). Everything else will be deﬁned relative
to this choice.
Let T0 ∈ SYT(λ) be the standard Young tableau with entries 1, . . . , n in order, from
left to right and top to bottom (i.e. the unique tableau such that T0(i, j) < T0(i′, j′)
whenever i < i′). We deﬁne the ambient orientation of X λ(R) to be the orientation for
which the Wronski map is locally orientation preserving in a neighbourhood of wT0.
As stated in the introduction, the orientation on Pn(µ) will simply be the restriction
of the ambient orientation. The character orientation of X λ(µ) is the complicated one,
and will be deﬁned next.

3.2 The character orientation

Let κ ⊂ λ be a partition. The half-open Richardson varieties X λ
κ (a), a ∈ A1 deﬁne a
ﬂat family of afﬁne subvarieties of X λ over A1. Let Eλ
κ ⊂ X λ × A
1 be the total space of

18

this family. Let π1 : X λ × A1 → X λ be the projection onto the ﬁrst factor, and deﬁne
Z λ
κ := π1(Eλ
κ ) to be the algebraic image of Eλ
κ under this projection. Informally, Z λ
κ ⊂ X λ

is the union of all X λ
κ (a), a ∈ A
1.

Proposition 3.1. Z λ
κ is a closed subvariety of X λ.

Proof. Let E be the closure of Eλ
κ in X λ × P
1, where X λ = X λ∨(∞) is the Schubert
variety. Note that E → X λ is proper and that

E ⊂ ⋃

a∈A1(X (a) ∩ X λ) × {a} ,

so in particular, the ﬁbre E∞ = π1(π
−1
2 (∞)) is contained in the limiting ﬁbre

lim
a→∞ X (a) ∩ X λ = ∂ X λ .

Therefore E∞ does not intersect the Schubert cell X λ. Let E|X λ = E ∩ (X λ × P1). Then
π1 : E|X λ → X λ is again proper, so π1(E|X λ) is closed. By the above,

π1(E|X λ) = π1(E ∩ (X λ × A
1)) = π1(Eλ
κ ) = Z λ
κ .

Proposition 3.2. Z λ
κ is irreducible, and dim Z λ
κ = |λ| − |κ| + 1.

Proof. The ﬁbres of Eλ
κ over A
1 are all isomorphic to the irreducible variety X λ
κ (0), so
Eλ
κ is integral and has dimension |λ| − |κ| + 1. Therefore Z λ
κ = π1(Eλ
κ ) is irreducible
and has dimension at most |λ| − |κ| + 1. It has dimension at least |λ| − |κ| + 1 since a
point of Z λ
κ lies on only ﬁnitely-many varieties X λ
κ (a), and each of these has dimension
|λ| − |κ|.

Proposition 3.3. If x ∈ Z λ
κ , then Wr(x) has a root of multiplicity |κ|. Conversely, if Wr(x)
has a root of multiplicity ℓ, then x ∈ Z λ
κ for some partition κ ⊢ ℓ.

Proof. This follows from Lemma 2.1.

Now suppose that |κ| = 2. In this case, by Proposition 3.2, Z λ
κ is a closed hyper-
surface in X λ ∼= An. Therefore the deﬁning ideal of Z λ
κ (F) is generated by a single
polynomial Φλ
κ(x) ∈ F[x]. Since Z λ
κ is deﬁned over Q, this polynomial has rational
coefﬁcients; in particular we can think of Φλ
κ as a real valued function on X λ(R).
The discriminant variety ∆n ⊂ Pn is the hypersurface deﬁned the vanishing of the
discriminant function g 7→ Discz(g(z)). We have g ∈ ∆n if and only if g has a repeated
root. By Proposition 3.3, Wr−1(∆n) = Z λ ∪ Z λ .

Since the polynomials hµ are not in ∆n, the points wT , T ∈ MN(λ; µ) are not in Z λ
κ for
either κ ⊢ 2. In particular, Φλ
κ(wT0) ̸= 0, and we will assume that Φλ
κ(wT0) > 0.
We call the two functions Φλ(x) and Φλ (x) the character orientation function and
the dual character orientation function, respectively.

19

Lemma 3.4. Let C be a component of X λ(µ), and κ ⊢ 2. Then exactly one of the following
must be true:

(a) Φλ
κ is globally non-negative on C ; or

(b) Φλ
κ is globally non-positive on C .

Proof. Since dim Z λ
κ = n − 1, and dim C = n, Φλ
κ cannot be identically zero on C .
Therefore at most one of (a) and (b) holds.
To see that at least one of these holds, we show that C \ Z λ
κ (R) is connected. Since
Φλ
κ is by deﬁnition non-vanishing on C \ Z λ
κ (R) this implies either (a) or (b) holds.
Suppose that x ∈ Z λ
κ (R) ∩ C . Since x ∈ Z λ
κ (R), Wr(x) ∈ ∆n, i.e. Wr(x) must have a
repeated root. On the other hand, by deﬁnition if x ∈ X λ(µ) then Wr(x) cannot have a
repeated real root. Therefore, Wr(x) must have a repeated non-real root.
Let K = {g ∈ Pn(R) | g has a repeated non-real root}. Then K has real codimension
2 in Pn(R). Since Wr is a proper map with ﬁnite ﬁbres, Wr−1(K) has codimension 2
in X λ(R). Since we just showed Z λ
κ (R) ∩ C ⊂ Wr−1(K), it follows that Z λ
κ (R) ∩ C has
codimension at least 2, and hence C \ Z λ
κ (R) is connected.

Deﬁnition 3.5. The character orientation of X λ(µ) is deﬁned as follows. For each
component C of X λ(µ) we orient according to the sign of the character orientation
function.

(a) If Φλ is globally non-negative on C , then the character orientation of C is the
same as the ambient orientation.

(b) If Φλ is globally non-positive on C , then the character orientation of C is opposite
to the ambient orientation.

The dual character orientation of X λ(µ) is the orientation obtained similarly, using
the dual character orientation function.

Remark 3.6. A common way to deﬁne an orientation on a manifold X is to specify a
global non-vanishing volume form on X . The non-vanishing condition can be relaxed
slightly to allow the form to vanish on a set of codimension 2. From this perspective,
the character orientation on X λ(µ) is simply the ambient orientation multiplied by the
character orientation function.

Example 3.7. Recall, from Section 1.4, that for λ = (n − 1, 1), X λ is identiﬁed with
the set of pairs (g, c), where g ∈ Pn and g ′(c) = 0. On Pn, the variety deﬁned by
the discriminant is irreducible, but working on X λ, we have the additional data of a
speciﬁed critical point, and we can identify two components of Wr
−1(∆n). Speciﬁcally
Z λ consists pairs (g, c) such that c is a double (or higher order) root of g; this is cut
out by the additional equation g(c) = 0. Z λ is the closure of the set of pairs (g, c) such
g has a double root at some point other than c. In this case, the character orientation

20

function is Φλ(g, c) = (−1)n−1 g(c). (The sign is explained by the fact that the point
wT0 corresponds to the pair (h1n, c0), where c0 is the smallest critical point of h1n, and
(−1)n−1h1n(c0) > 0.) As noted in Section 1.4, this function is in fact globally positive or
globally negative on any component of X λ(µ). The dual character orientation function
is Φλ (g, c) = (−1)n−1Discz(g(z))/g(c).

3.3 Signs of points in X λ(R)

Let ∂ Wr : X λ(F) → F denote the Jacobian of the Wronski map Wr : X λ(F) → Pn(F)
(with respect to afﬁne coordinates). The ramiﬁcation divisor of Wr : X λ → Pn, is the
hypersurface in X λ on which ∂ Wr vanishes. We denote it by R
λ.
For x ∈ X λ(µ) \ R
λ(R), deﬁne the sign of x to be sgn(x) = 1 if the Wronski map is
orientation preserving with respect to the character orientation in a neighbourhood of
x, and sgn(x) = −1 otherwise. Similarly, deﬁne the dual sign of x, denoted sgn
∗(x),
using the dual character orientation. Deﬁne the ambient sign of x, denoted asgn(x)
using the ambient orientation.
Our main goal is to prove the following theorem.

Theorem 3.8. For every T ∈ MN(λ; µ),

sgn(wT ) = sgn(T ) .

Our strategy is to join the points wT together by paths, and count the number of
times the sign changes along a path. Let γ : [0, 1] → X λ(R), t 7→ γt be a path, and
assume the following:

• γ0, γ1 /∈ R
λ(R) ∪ Z λ (R) ∪ Z λ(R);

• γt ∈ R
λ(R) ∪ Z λ (R) ∪ Z λ(R) for only ﬁnitely many values of t.

These conditions ensure that sgn(γt), sgn
∗(γt) and asgn(γt) are deﬁned at all but ﬁnitely
many points, including γ0 and γ1.
We ﬁrst establish the main properties of interest in detecting sign changes along
paths in X λ(R). In Section 3.4, we then discuss how the existence of sufﬁciently nice
paths allows us to prove Theorem 3.8.

Proposition 3.9. If sgn(γt) changes at the point t, then either γt ∈ Rλ(R), or γt ∈ Z λ(R).
If sgn
∗(γt) changes at the point t, then either γt ∈ R
λ(R), or γt ∈ Z λ (R). If asgn(γt)
changes at the point t, then γt ∈ R
λ(R).

Proof. If sgn(γt) changes, then either the sign of the Jacobian of Wr reverses, or the
orientation of the space reverses. The former can happen only when ∂ Wr(γt) = 0, i.e.
the path crosses R
λ(R), and the latter can happen only when only when Φλ(γt) = 0, i.e.
the path crosses Z λ(R). The other statements are similar.

For the converse, we need a slightly stronger condition.

21

Deﬁnition 3.10. Let V ⊂ X λ be an algebraic hypersurface deﬁned over R, and let
γ : [0, 1] → X λ(R) be a path such that γt ∈ V (R) for only ﬁnitely many values of t.
Let t ∈ (0, 1) be such a value. We say γ has a simple crossing of V (R) at t, if γt is
an algebraically smooth point of V (R), and γ crosses V (R) at t. (Formally, “crossing”
means the following: There exists an open neighbourhood U ⊂ X λ(R) of γt such that
for every sufﬁciently small ε > 0, γt−ε and γt+ε are in different components of U \V (R).)

Remark 3.11. In the above deﬁnition, the path γ itself need not be a smooth function
of t at the crossing point — only the hypersurface it crosses needs to be smooth. In
fact, the paths we consider will be constructed piecewise, in such a way that they are
non-differentiable at precisely the points where they cross one of the hypersurfaces of
interest.

Proposition 3.12. If γ has a simple crossing of R
λ(R) or Z λ(R) at t, then sgn(γt) changes
at t. If γ has a simple crossing of Rλ(R) or Z λ (R) at t, then sgn
∗(γt) changes at t. If γ
has a simple crossing of Rλ(R) at t, then asgn(γt) changes at t.

Proof. All three statements follow immediately from the following more general state-
ment. Let V ⊂ X λ be a hypersurface, deﬁned as the zero locus of a polynomial Φ. If γ
has a simple crossing of V (R) at t, then Φ(γt) changes sign at t.
To prove this, note that since V is smooth at γt, we may, by perturbing γ, assume
that γ is smooth and transverse to V (R). The function Φ(γt) vanishes at t, and d
d t Φ(γt)
cannot vanish at t, since (by transversality) the tangent vector to γ at t is not in the
tangent space of V at γt. Therefore Φ(γt) changes signs at t.

Remark 3.13. For any point x ∈ X λ(µ) \ R
λ(R), µ = 2n21n1, there exists a path γ from
wT0 to x such that all crossings are simple. Let gt = Wr(γt). We note that whenever the
number of real roots of g changes, γt must have a simple crossing of Z λ at t, or a simple
crossing of Z λ at t, but not both. We therefore have a relationship between sgn(x) and
sgn
∗(x): sgn(x) · sgn
∗(x) = (−1)n2 .

Equivalently this shows that the dual character orientation of X λ(µ) is the same as the
character orientation if n2 is even, and opposite if n2 is odd.

The following technical lemma will help to identify simple crossings of R
λ(R).

Lemma 3.14. Let ψ : X → Y be a quasiﬁnite map of smooth varieties of the same dimen-
sion. Let R ⊂ X be the ramiﬁcation divisor (deﬁned locally by the vanishing of the Jacobian
determinant). Then the smooth locus of R is

R
sm = {x ∈ R : the ramiﬁcation degree at x is exactly 2} .

Proof. The claim is local on X and Y , so we may assume X = Spec(A, mx ) and Y =
Spec(B, m y) are spectra of regular local rings, and ψ is induced by a map of local rings

22

ψ∗ : B → A, with ψ∗(m y) ⊂ mx . We have a short exact sequence of modules of differen-
tials 0 → ψ∗ΩY → ΩX → ΩX /Y → 0 ,

and the ramiﬁcation locus R is deﬁned by the vanishing of the determinant of the map
of free A-modules ψ∗ΩY → ΩX .
First assume the ramiﬁcation degree is exactly 2, that is, the scheme-theoretic ﬁbre
has length 2: vdimC(B/m y ⊗B A) = vdimC(A/ψ∗(m y)) = 2 .

In particular ψ∗(m y) must contain m
2
x (otherwise the quotient will be too large). In fact,
ψ∗(m y) has the form m
2
x + L, where L ⊂ mx /m
2
x is some codimension-1 vector subspace.
Consider the map m y/m2
y → mx /m2
x induced by ψ. By the above, the image of this
map is L. Choosing and lifting bases to obtain minimal generators of the ideals, we may
assume mx = (x1, . . . , x n) and m y = ( y1, . . . , yn) where

ψ∗( y1) = 0 mod mx and ψ∗( yi) = x i for 2 ≤ i ≤ n . (3.1)

In particular, ψ∗(d yi) = d x i for 2 ≤ i ≤ n.
As for y1, we have ψ∗( y1) ∈ m
2
x . By Cohen-Macaulayness Sym2(mx /m
2
x ) = m
2
x /m
3
x .
So, write ψ∗( y1) mod m
3
x as a quadratic polynomial q(x1, . . . , x n). Taking differentials
we get
 ψ∗(d y1) =
 n∑

i=1
 ∂ q
∂ xi d xi mod m
2
x 〈d x1, . . . , d x n〉 .

Note that ∂ q
∂ x1 is a linear form and is non-zero, since ∂ q
∂ x1 = 0 would imply x 2
1 /∈ ψ∗(m y).
Thus the matrix for the map ψ∗ΩY → ΩX has the form






 ∂ q
∂ x1 + s1 0 . . . 0
∂ q
∂ x2 + s2 1 . . . 0
... 0 ... ...
∂ q
∂ xn + sn 0 · · · 1








with si ∈ m
2
x for all i, and the determinant is ∂ ψ = ∂ q
∂ x1 + s1. This cuts out a smooth
divisor since ∂ ψ is part of a minimal generating set for mx .
We have shown that R
sm contains the points of ramiﬁcation index 2. For the reverse
direction, the proof is similar in spirit. Since we will not need it, we omit it.

3.4 Paths for the proof of Theorem 3.8

To prove Theorem 3.8, we will establish the following two Lemmas.

Lemma 3.15. Let T ∈ MN(λ; µ), µ = (µ1, . . . , µk), and suppose µb = 2. Let T ′ be
the tableau obtained from T by incrementing entries b + 1, . . . , k by 1, and changing the
lower-right b to b + 1. There exists a path γ : [0, 1] → X λ from wT ′ to wT , such that:

23

(a) γt /∈ R
λ(R) for all t ∈ (0, 1).

(b) If shape(T |b) is a horizontal domino, then γt /∈ Z λ(R) for all t ∈ (0, 1), and there
is exactly one t ∈ (0, 1) such γt ∈ Z λ (R), and this is a simple crossing.

(c) If shape(T |b) is a vertical domino, then γt /∈ Z λ (R) for all t ∈ (0, 1), and there is
exactly one t ∈ (0, 1) such γt ∈ Z λ(R), and this is a simple crossing.

Lemma 3.16. Let T ′ ∈ MN(λ; µ
′), µ′ = (µ
′
1, . . . , µ
′
k+1). Suppose µ′
b = µ
′
b+1 = 1, and the
entries b and b + 1 of T ′ are non-adjacent. Let T ′′ be the tableau obtained by swapping
these two entries. There exists a path γ : [0, 1] → X λ from wT ′ to wT ′′, such that:

(a) There is exactly one t ∈ (0, 1) such that γt ∈ R
λ(R), and this is a simple crossing.

(b) There is exactly one t ∈ (0, 1) such that γt ∈ Z λ (R), and this is a simple crossing.

(c) There is exactly one t ∈ (0, 1) such that γt ∈ Z λ(R), and this is a simple crossing.

Example 3.17. We now continue Example 2.18, to illustrate Lemmas 3.15 and 3.16 in
the case where λ = . Here, the four relevant tableaux are

T0 = 1 2
3 T1 = 1 3
2 T2 = 1 1
2 T3 = 1 2
1 .

It is clear from Figure 2.1 that we can ﬁnd a path g : [0, 1] → P3(R) from h13 to h21 such
that gt has two distinct real critical points, c0,t < c1,t, for all t ∈ [0, 1]. Lifting this path
to X λ(R), we obtain two paths: γ0, γ1 : [0, 1] → X λ(R), γi,t = (gt, ci,t) for i = 1, 2; γ0
connects wT0 to wT2, and γ1 connects wT1 to wT3. Note that the larger critical point c1,t
must change sign along the path gt, and so for some t, gt(c1,t) = 0. As explained in
Example 3.7, this means that γ0 crosses Z λ (R) and γ1 crosses Z λ(R). Since gt has two
distinct critical points for all t, neither path crosses R
λ(R). These are the two types of
paths described in Lemma 3.15.
To connect wT0 to wT1, we need a path γ : [0, 1] → X λ(R), from (h13, c0) to (h13, c1),
where c0 < c1 are the two critical points of h13. To do this, we begin with a different
path g : [0, 1
2 ] → Pn(R) such that g0 = h13, gt has a two real critical points, c0,t < c1,t,
for t ∈ [0, 1
2 ), and g1/2 has a double critical point. Again, we can lift this path to X λ(R)
in two ways, but this time the two lifted paths meet at the ﬁbre over g1/2. We can then
combine these two lifts into a single path:

γt =
 ¨(gt, c0,t) for t ∈ [0, 1
2 ]

(g1−t, c1,1−t) for t ∈ [ 1
2 , 1].

This is illustrated in Figure 3.1. There are three special points along this path. Since g1/2
has a double critical point, we have γ1/2 ∈ R
λ(R). There is also a point t ∈ (0, 1
2 ) such

24

Figure 3.1: Connecting wT0 to wT1, for λ = .

that gt has a double real root at c0,t. This means that γt ∈ Z λ(R), and γ1−t ∈ Z λ (R).
This is the type of path described in Lemma 3.16.
Figure 3.2 shows (a two-dimensional projection of) the Schubert cell X λ(R), along
with Z λ (R), Z λ(R) and R
λ(R), and the three paths described in this example.

Lemmas 3.15 and 3.16 will be proved in Section 4.6. Modulo these, we can now
prove Theorems 3.8 and 1.3.

Proof of Theorem 3.8. By the deﬁnition of the character orientation, sgn(wT0) = 1. By
Lemma 3.16 we can connect all the points wT , T ∈ SYT(λ) by a network of paths γt
such that sgn(γt) changes twice along each path. It follows that sgn(wT ) = sgn(wT0) =
1 = sgn(T ), for all T ∈ SYT(λ).
For T ∈ MN(λ; µ), µ ̸= 1n, we can connect T to some T ′ as in Lemma 3.15. Then
sgn(T ) = sgn(T ′) if shape(T |b) is a horizontal domino, sgn(T ) = −sgn(T ′) if shape(T |b)
is a vertical domino. Following the path γ connecting wT to wT ′, we see that sgn(γt)
does not change in the horizontal domino case, and sgn(γt) changes once in the vertical
domino case. The result now follows by a simple induction.

Proof of Theorem 1.3. Since hµ ∈ Pn(µ), the topological degree of Wr : X λ(µ) → Pn(µ)
is ∑

x∈Wr−1(hµ) sgn(x) = ∑

T ∈MN(λ;µ) sgn(wT ) = ∑

T ∈MN(λ;µ) sgn(T ) = χ λ(µ) ,

where the equalities above are by Corollary 2.16, Theorem 3.8, and Theorem 2.12,
respectively.

4 Stable curves

4.1 Families over M 0,n+3

In order to connect up points wT ∈ X λ(R), we work with a different model of the
Shapiro–Shapiro picture, in which Wr : X λ → Pn is replaced by a related ﬁnite ﬂat map
Ψ : Y λ → M 0,n+3, over the moduli space of genus 0 stable curves with n + 3 marked
points. This model was described by Speyer [30]. We give a brief overview of Speyer’s
construction and the properties we will need. Since our goal is not to prove these

25

R
λ Z λZ λ
 wT0

1 2
3
 wT1

1 3
2

wT2 1 1
2 wT31 2
1

Figure 3.2: The points wT0, wT1 ∈ X λ(1
3) (shaded), wT2, wT3 ∈ X λ(21) (unshaded),
and the three paths connecting them. The paths cross Z λ, Z λ , and R
λ as described in
Lemmas 3.15 and 3.16.

properties, some of the exposition will be simpliﬁed. In order to make the connection to
the Wronski map explicit, we will also describe the construction in a more coordinatized
way.
Consider the set A1 = {0, 1, ∞, a1, . . . , an}, where each element is regarded purely
as a formal symbol. For a stable curve C ∈ M 0,n+3, we will label the marked points
with the n + 3 symbols from A1. M0,n+3 ⊂ M 0,n+3 is the open subvariety of smooth
curves, isomorphic to P1 with distinct marked points. If C ∈ M0,n+3, we will choose
coordinates on C such that the marked points labelled 0, 1, ∞ are placed at 0, 1, ∞ ∈ P1

respectively. Abusing notation somewhat, we also write ai to denote the coordinate
of the point labelled ai in C, whenever it appears in a formula. More generally, if
C ∈ M 0,n+3, there is a unique morphism C → P1 such that the points labelled 0, 1, ∞
in C map to 0, 1, ∞ ∈ P1. In this case ai will denote the coordinate of the image of the
point labelled ai in P1. This allows us to associate a polynomial

pol(C) = pol(C, z) := ∏

ai ̸=∞
(z + ai)

to every curve C ∈ M 0,n+3.
Let Aℓ denote the set of all ordered ℓ-tuples of distinct elements of A1. For p, q, r dis-
tinct points of P1, deﬁne φp,q,r(s) = (p−s)(q−r)
(p−q)(s−r) for s ∈ P1; this is the unique transformation
such that φp,q,r(p) = 0 , φp,q,r(q) = 1 , φp,q,r(r) = ∞ .

Given a curve C ∈ M0,n+3 and (p, q, r) ∈ A3, we interpret φp,q,r ∈ PGL2 to be the unique
projective linear transformation of P1 that sends marked points (p, q, r) to (0, 1, ∞)

26

respectively. We have an injection Gr(d, d + m) × M0,n+3 → Gr(d, d + m)
A3 × M 0,n+3,

(x, C) 7→ • φp,q,r(x)

(p,q,r)∈A3 , C− .

Deﬁne fGr(d, d + m) to be the closure of the image of this map. The projection

Ψ : fGr(d, d + m) → M 0,n+3

deﬁnes a family over M 0,n+3. We also have a projection map onto Gr(d, d + m) for each
(p, q, r) ∈ A3; In particular, let

π : fGr(d, d + m) → Gr(d, d + m)

onto the Grassmannian factor corresponding to (p, q, r) = (0, 1, ∞) ∈ A3.
For C ∈ M0,n+3, the ﬁbre Ψ −1(C) of this family is isomorphic to Gr(d, d + m). Specif-
ically, π : Ψ −1(C) → Gr(d, d + m) is an isomorphism (and the same is true for if we
replace π by the projection onto any other Grassmannian factor) [30, Proposition 3.3].
If on the other hand C ∈ M 0,n+3 is a nodal curve, the ﬁbre is a ﬂat degeneration of the
Grassmannian [30, Theorem 3.2].
Speyer’s construction also allows arbitrary Schubert conditions placed at the marked
points of the curve. For (p, q, r) ∈ A3, s ∈ A1, and a partition λ, let

Uλ(p, q, r; s) :=
 



X λ(0) if p = s

X λ(1) if q = s

X λ(∞) if r = s

Gr(d, d + m) otherwise .

Deﬁne
 eX λ(s) :=
   ∏

(p,q,r)∈A3 Uλ(p, q, r; s) × M 0,n+3
!
 ∩ fGr(d, d + m) .

The restricted map Ψ : eX λ(s) → M 0,n+3, deﬁnes a family in which the ﬁbre over a
smooth curve C ∈ M0,n+3 is identiﬁed with the Schubert variety X λ(s). Speciﬁcally, if
C ∈ M0,n+3, π : Ψ −1(C) → X λ(s) is an isomorphism [30, Proposition 3.3]. If C ∈ M 0,n+3
is a nodal curve, the ﬁbre is a degeneration of the Schubert variety. Speyer describes
these degenerate ﬁbres explicitly [30, Theorem 1.2], and in Section 4.2, we will state
this result for the special case we need.
Speyer also proves that intersections of the varieties eX λ(s) are well-behaved [30,
Theorem 1.1].

Theorem 4.1. For any partitions α
s ⊂ md, s ∈ A1,

Ψ : ⋂

s∈A1 eX αs(s) → M 0,n+3

deﬁnes a ﬂat, proper, Cohen–Macaulay family over M 0,n+3 of relative dimension dm −∑

s∈A1 |α
s|.
 27

We will be primarily interested in the family deﬁned by the following intersection.

Y λ := eX (a1) ∩ · · · ∩ eX (an) ∩ eX λ∨(∞) . (4.1)

In this case, Ψ : Y λ → M 0,n+3 is a ﬁnite morphism. Let Y λ := Ψ −1(M0,n+3) denote the
restriction of this family to M0,n+3.

Remark 4.2. The marked points 0 and 1 do not appear in the deﬁnition of Y λ, and
it is possible to deﬁne a similar ﬁnite family over M 0,n+1, with only marked points
∞, a1, . . . , an. The reason for including the two additional marked points is to provide
the following connection to the Wronski map.

Proposition 4.3. The diagrams below commute.

Y λ π
−−−→ X λ

Ψ

↓ 

↓Wr

M 0,n+3 −−−→
pol Pn
 Y λ π
−−−→ X λ

Ψ

↓ 

↓Wr

M0,n+3 −−−→
pol Pn

In the ﬁrst diagram, X λ = X λ∨(∞) is the closure of X λ in Gr(d, d + m), and Pn = Pn is
the closure of Pn in Pdm. The second diagram is a ﬁbre product: Y λ = M0,n+3 ×Pn X λ.

Proof. Over a smooth curve C ∈ M0,n+3, π restricts to an isomorphism Ψ −1(C) →
X (a1) ∩ · · · ∩ X (an) ∩ X λ∨(∞) [30, Proposition 3.3]. By Lemma 2.1, X (a1) ∩ · · · ∩
X (an) ∩ X λ∨(∞) = Wr−1(pol(C)); hence the second diagram is a ﬁbre product. Taking
closures everywhere in the second diagram gives the ﬁrst diagram, which therefore also
commutes.

4.2 P1-chains

The families eX λ∨(∞) and Y λ are deﬁned as subvarieties of Gr(d, d + m)
A3 ×M 0,n+3, but
this encoding is highly redundant — locally, we only need a small number of factors to
get a faithful image. The only nodal curves we will need in this paper are curves that
are P1-chains, and if we restrict to these, the families eX λ∨(∞) and Y λ have a simpler
description.
Suppose C ∈ M 0,n+3 has components C1, C2, . . . , Ck+1. Choose an isomorphism Ci →
P1, and for each point p ∈ C, let p(i) ∈ P1 denote the image of p under the contraction
map C → Ci → P1; we call (p(1), . . . , p(k+1)) ∈ (P1)k+1 the C-coordinates of p ∈ C. We
thereby associate a polynomial to each component:

pol(i)(C) = pol
(i)(C, z) := ∏

a(i)
j ̸=∞
(z + a(i)
j ) .

By a P1-chain, we mean that the nodes and marked points are arranged as follows:

28

0 ∞

1

a5
 a8 a2

a3 = a4
 a1
 a6

a7

Figure 4.1: A P1-chain in M 0,11 with four components.

(1) There is a node oi ∈ C, joining Ci to Ci+1, i = 1, . . . , k. We assume our coordinates
are such that o(i)
i = ∞ and o(i+1)
i = 0.

(2) The marked points 0, 1, ∞ are on C1, Cb0, Ck+1 respectively, where 1 ≤ b0 ≤ k + 1.
We assume our coordinates are such that 0
(1) = 0, 1
(b0) = 1, and ∞
(k+1) = ∞.

(3) For j = 1, . . . , n, put b j := i if a j ∈ Ci. For i = 1, . . . , k + 1, let µi := #{ j | b j = i}.
We require µi ≥ 1 for i ̸= b0, but µb0 = 0 is allowed. We write µ = (µ1, . . . , µk+1).
(This is equivalent to the stability condition on the curve.)

(4) We allow the possibility a double marked point, where two of the marked points
a1, . . . , an are at the same point of C. In the usual way of thinking about M 0,n+3,
when two marked points collide, the curve gains a new P1-component (sometimes
called a “bubble”) containing the two marked points, attached to the original
curve at the collision point. But since this resolution is canonical, it is also ﬁne
to think of this as a double marked point on C. We will take this perspective,
and we will not count these extra bubbles when counting the components of C.
The marked points must still be distinct from the nodes o1, . . . , ok, and we do not
allow triple marked points, or any other conﬁguration normally forbidden by the
deﬁnition of a stable curve.

Remark 4.4. We can specify a P1-chain by specifying values for k, b0, b1, . . . , bn, and
a(b1)
1 , . . . , a(bn)
n . Note, however, that this is also specifying C-coordinate isomorphisms
Ci → P1, which are not part of the actual data of the curve, and are not canonical if
k ≥ 1. Each of the coordinate maps Ci → P1, i ̸= b0 can be rescaled by any non-zero
scalar, without changing the curve. (The map Cb0 → P1, however, is pinned down by
conditions 1 and 2.) In particular, there is more than one way to specify the same
nodal curve in M 0,n+3. For example, there is a unique curve with n+1 components and

b j = j + 1 for all j; the values of a(b j )
j specify coordinates on this curve, but do not help
specify the curve itself.

Example 4.5. An example of P1-chain is shown in Figure 4.1. In this example we have
b5 = 1, b2 = b3 = b4 = b8 = 2, b0 = b1 = 3, and b6 = b7 = 4. The dashed circle on
each P1 represents points with real C-coordinates, and the solid outer circle represents

29

points with pure imaginary C-coordinates. In this case,

a(3)
1 = − 1
2 , a(2)
2 = 1 , a(2)
3 = a(2)
4 = i , a(1)
5 = −1 , a(4)
6 = i
2 , a(4)
7 = − i
2 , a(2)
8 = 1
2 .

Note that a3 = a4 is a double marked point. The associated polynomials are:

pol
(1)(z) = (z − 1)

pol
(2)(z) = z(z + 1)(z + 1
2 )(z + i )
2

pol
(3)(z) = z5(z − 1
2 )

pol
(4)(z) = z6(z + i
2 )(z − i
2 ) ,

and since b0 = 3, pol(z) = pol(3)(z).

For j = 1, . . . , n, let π j : fGr(d, d + m) → Gr(d, d + m) denote the projection onto the
Grassmannian factor corresponding to (0, a j, ∞) ∈ A3. When we restrict our base to
the open subvariety of P1-chains in M 0,n+3,

eX λ∨(∞) (π1,...,πn)
−−−−−→ Gr(d, d + m)n × M 0,n+3

restricts to an injective map. Since all calculations in this paper take place within this
restriction, we will henceforth identify eX λ∨(∞) with its image under this map.
Let C be a P1-chain, and let Q(C) denote the ﬁbre of the map Ψ : eX λ∨(∞) → M 0,n+3
over C (regarded as a subvariety of Gr(d, d + m)n). If C has more than one compo-
nent, then Q(C) is a reducible scheme, and its components are indexed by Tab(λ; µ),
where µ = (µ1, . . . , µk+1) is as above. Write Q T (C) for the component indexed by
T ∈ Tab(λ; µ). Write Q(b)
T for the closure of X shape(T |≤b)
shape(T |≤b−1)(0).

Theorem 4.6. We have an isomorphism Q T (C) → ∏k+1
b=1 Q(b)
T ,

y 7→ (y
(1), . . . , y
(k+1)) , (4.2)

characterized by π j(y) = φ0,a(b j )

j ,∞(y(b j )) , for j = 1, . . . , n . (4.3)

Proof. The existence of such an isomorphism is the content of [30, Theorem 1.2], in the
case where the curve is P1-chain, and there is only one Schubert condition. The details
of the isomorphism, in general, are described in [30, Section 3].

We call (y(1), . . . , y(k+1)) ∈ ∏k+1
b=1 Q(b)
T the C-coordinates of the corresponding point
y ∈ Q T (C).
Let Y (C) denote the ﬁbre of the map Ψ : Y λ → M 0,n+3 over C. Then Y (C) ⊂ Q(C),
so every point in Y (C) is in some component Q T (C). Write YT (C) := Y (C) ∩ Q T (C).

30

Theorem 4.7. Every point of Y (C) is in YT (C) for some unique T ∈ Tab(λ; µ). Under the
isomorphism (4.2), YT (C) is identiﬁed with ∏k+1
b=1 Y (b)
T (C), where

Y (b)
T (C) = X shape(T |≤b)
shape(T |≤b−1)(0) ∩ Wr−1(pol
(b)(C)) .

Proof. First, suppose C has no double marked points. Then by deﬁnition,

Y (C) = Q(C) ∩
 n⋂

j=1 π
−1
j X (1) .

By (4.3), intersecting Q T (C) with π
−1
j X (1) corresponds to intersecting the factor Q(b j )
T
with X (a(b j )
j ). Thus YT (C) is identiﬁed with

k+1∏

b=1
 •
Q(b)
T ∩ ⋂ X (a(b j )
j )
− ,

where the intersection is taken over all j such that b j = b. The result now follows from
Lemma 2.1. In the case where C has a double marked point, we deduce the result by
taking limits and observing that

lim
a′→a X (a) ∩ X (a′) = X (a) ∪ X (a) .

In the case where the curve has a double marked point, we distinguish the following
two cases.

Corollary 4.8. If C has a double marked point, a j = a j′ on component Cb, and y ∈ YT (C),
then we have either π j(y) ∈ X (1) ∩ Q(b)
T or π j(y) ∈ X (1) ∩ Q(b)
T but not both.

Proof. By deﬁnition y(b) ∈ Q(b)
T , and by Theorem 4.7, y(b) ∈ Wr−1(pol
(b)(C)). Since
pol
(b)(C) has a double root at a(b)
j , by Lemma 2.1 we have y(b) ∈ X (a(b)
j ) or y(b) ∈

X (a(b)
j ) but not both. Applying (4.3) gives the result.

Remark 4.9. For many of the nodal curves we consider, we will have b0 = k + 1 and
µk+1 = 0, i.e. 1 and ∞ are the only marked points Ck+1. When this happens, Q(k+1)
T
is a point, and y(k+1) does not appear on the right side of (4.3). We will therefore
sometimes drop the (k + 1)-term from our notation, e.g. writing µ = (µ1, . . . , µk), or
YT (C) = ∏k
b=1 Y (b)
T (C), etc.

4.3 Real structures

For each quadruple (p, q, r, s) ∈ A4 of distinct elements of A1, there is a natural map
θp,q,r,s : M 0,n+3 → M 0,4, which forgets all marked points except for p, q, r, s, and con-
tracts any unstable components of the curve. Using the canonical identiﬁcation of M 0,4

31

with P1 (in which (p, q, r) 7→ (0, 1, ∞)), we rewrite this as θp,q,r,s : M 0,n+3 → P1,

θp,q,r,s(C) = (ˆp − ˆs)(ˆq − ˆr)
(ˆp − ˆq)(ˆr − ˆr)

where ˆp, ˆq, ˆr, ˆs denote the images of points p, q, r, s in M 0,4, in any coordinates. The
product of all such maps gives an embedding

M 0,n+3 ↪→ (P1)
A4 . (4.4)

From this construction we obtain the standard real structure on M 0,n+3, which is
inherited from the standard real structure on P1: the complex conjugate of a stable
curve C ∈ M 0,n+3 is obtained by conjugating each of the nodes and marked points.
Similarly, there is a standard real structure on on fGr(d, d +m), deﬁned via its embedding
in Gr(d, d + m)
A3 × M 0,n+3. For either of these spaces, we will denote this complex
conjugation map by ξ.
The standard notion of a real point of M 0,n+3 and Y λ does not precisely correspond
to the notion of a real point of Pn or X λ. Informally a point of M 0,n+3 is real iff all
nodes and marked points are real, whereas a point of Pn is real whenever its roots are
a mixture of real points and complex conjugate pairs. Thus the real points of M 0,n+3
map to the closure of Pn(1n) ⊂ Pn(R). To study curves such that pol(C) ∈ Pn(µ) for
µ ̸= 1n, we need to consider other real structures on M 0,n+3, in which speciﬁed pairs of
marked points are required to be complex conjugates of each other.
Let Sn denote the symmetric group of permutations of {1, . . . , n}. Sn acts on M 0,n+3
by permuting the marked points a1, . . . , an, and on fGr(d, d + m) by also permuting the
corresponding factors in Gr(d, d +m)
A3. If σ ∈ Sn is an involution, we deﬁne ξσ := σ◦ξ
acting on either M 0,n+3 or fGr(d, d + m) (or any of its ξ- and Sn-invariant subvarieties,
e.g. eX λ∨(∞) or Y λ). If σ ∈ Sn is the identity element, then ξσ = ξ; otherwise, ξσ is the
complex conjugation for a different real structure on these spaces. The real points with
respect to this real structure are the ξσ-ﬁxed points, and for any ξ- and Sn-invariant
subvariety V of fGr(d, d + m) or M 0,n+3, we denote the ξσ-ﬁxed points of V by V (Rσ).

Proposition 4.10. Let σ ∈ Sn be an involution. We have the following commutative
diagram. Y λ(Rσ) π
−−−→ X λ(R)

Ψ

↓ 

↓Wr

M 0,n+3(Rσ) −−−→
pol Pn(R)

If C ∈ M0,n+3 and pol(C) ∈ Pn(R), then there is a unique involution σ ∈ Sn such that
C ∈ M0,n+3(Rσ). If y ∈ Y (C) and π(y) ∈ X λ(R), then σ is also the unique involution
such that y ∈ Y λ(Rσ).
 32

Note that, when σ has cycle type µ, the images of Y λ(Rσ) and M 0,n+3(Rσ) are the
closures of X λ(µ) ⊂ X λ(R) and Pn(µ) ⊂ Pn(R).

Proof. We have pol ◦ σ = pol, so for C ∈ M 0,n+3, ξσC = C implies that pol(C) is real.
Since σ does not permute 0, 1, ∞, it ﬁxes the (0, 1, ∞)-factor in Gr(d, d + m)
A3, so
π ◦ σ = π, and so a similar argument applies for the map π.
If C ∈ M0,n+3 and pol(C) is real, then pol(ξC) = pol(C) = pol(C). It follows that ξ is
just permuting the marked points of C, i.e. ξC = σC for some σ ∈ Sn, or equivalently
C ∈ M0,n+3(Rσ) (σ must therefore be an involution, since ξ is an involution). Finally,
suppose y ∈ Y (C) and π(y) is real. Then

π(σy) = π(y) = π(y) = π(ξy)

and Ψ(σy) = σC = ξC = Ψ(ξy) ,

so by the last part of Proposition 4.3, it follows that σy = ξy.

If C is a P1-chain, then we have the following characterization. We say that the
C-coordinates are ξσ-compatible, if a(i)
j is the complex conjugate of a(i)
σ( j) for all i =
1, . . . , k + 1, j = 1, . . . , n (this requires a j and aσ( j) to be on the same component of
C). Note that this implies that C ∈ M 0,n+3(Rσ) is ξσ-ﬁxed. Conversely if C is ξσ-
ﬁxed there exists a choice of ξσ-compatible C-coordinates (though not every choice of
C-coordinates is ξσ-compatible).

Proposition 4.11. Let σ ∈ Sn be an involution, and let C be a P1-chain with ξσ-compatible
C-coordinates. For y ∈ Y (C), we have ξσy = y if and only if (y(1), . . . , y(k+1)) are real.

Proof. First suppose ξσy = y. This means that

π j(y) = ξπσ( j)(σy) . (4.5)

for j = 1, . . . , n. Let b ∈ {1, . . . , k}. If the component Cb in the chain does not contain
any of the marked points a1, . . . , an, then Q(b)
T consists of a single real point, so y(b) is
real. Otherwise, let a j be a marked point on Cb, and let a = a(b)
j be its coordinate. Then

aσ( j) ∈ Cb and since the coordinates are ξσ-compatible, a(b)
σ( j) = a. By (4.3), we have

π j(y) = φ0,a,∞(y(b))

and ξπσ( j)(σy) = ξφ0,a,∞(σy(b)) = ξφ0,a,∞(y(b)) = φ0,a,∞(ξy(b)) ,

which implies that y(b) is real.
Conversely, if y(b) is real, the calculation above shows that (4.5) holds for all j such
that a j is on Cb. If y(b) is real all b, then (4.5) holds for all j, so ξσy = y.

Remark 4.12. There is a well-known CW-complex description of M 0,n(R) in terms of
associahedra [3]. It would be interesting to see an analogous description of M 0,n(Rσ)
and of the attachments between the twisted structures for each σ.

33

0 ∞

1a1

a2

a3

a4

a5
a6

a7

a8
 Figure 4.2: The nodal curve Cµ(0) for µ = (2, 1, 2, 2, 1).

4.4 Special ﬁbres

Let µ = (µ1, . . . , µk), be a composition with µi ∈ {1, 2}. Recall that µb = n + 1 − ∑b
i=1 µi.
Working over C((u)), we deﬁne Cµ(u) ∈ M0,n+3(C((u))) to be the curve whose marked
points a1, . . . , an are speciﬁed as follows:

a j =
 




u j if j = µi for some i, µi = 1

i
2 (u j + u j+1) if j = µi for some i, µi = 2

− i
2 (u j−1 + u j) if j − 1 = µi for some i, µi = 2
 (4.6)

Note that pol(Cµ(u), z) = Hµ(u, z).

Proposition 4.13. The limit curve limu→0 Cµ(u) is the P1-chain Cµ(0), with k + 1 compo-
nents, b0 = k + 1, speciﬁed by the following coordinate data:

• if j = µi, µi = 1, then b j = i and a(b j )
j = 1;

• if j = µi, µi = 2, then b j = b j+1 = i and (a(b j )
j , a(b j+1)
j+1 ) = ( i
2 , − i
2 ).

Proof. Using the embedding (4.4), it sufﬁces to show that for all (p, q, r, s), we have
limu→0 θp,q,r,s(Cµ(u)) = θp,q,r,s(Cµ(0)). There are several cases, but this is straightfor-
ward. Note that a j’s from distinct µi’s have distinct leading orders as u → 0, which
greatly simpliﬁes the calculation.

Example 4.14. For µ = (2, 1, 2, 2, 1), the curve Cµ(u) has marked points 0, 1, ∞ and

a7 = i
2 (u7 + u
8) ,

a8 = − i
2 (u7 + u8) , a6 = u6 , a4 = i
2 (u4 + u5) ,

a5 = − i
2 (u4 + u
5) ,
 a2 = i
2 (u2 + u3) ,

a3 = − i
2 (u2 + u3) , a1 = u1 .

The polynomial pol(Cµ(u), z) = Hµ(u, z) is given in Example 2.14. The limit curve Cµ(0)
is shown in Figure 4.2.

Let σ ∈ Sn be the involution

σ( j) =
 



 j if j = µi, µi = 1

j + 1 if j = µi, µi = 2

j − 1 if j − 1 = µi, µi = 2.
 (4.7)

34

This is the unique involution such that the curve Cµ(u) is ξσ-ﬁxed. Moreover, the Cµ(0)-
coordinates in Proposition 4.13 are ξσ-compatible.
We can now prove Lemma 2.15. First, we establish the analogous result for the limit
ﬁbre Y (Cµ(0)).

Lemma 4.15. For T ∈ Tab(λ; µ), YT (Cµ(0)) consists of 2
# (T ) reduced points. If # (T ) =
0, the unique point in YT (Cµ(0)) is ξσ-ﬁxed. If # (T ) > 0, then none of the points in
YT (Cµ(0)) are ξσ-ﬁxed.

Proof. By Theorem 4.7, this is identiﬁed with ∏n
b=1 Y (b)
T (Cµ(0)), where

Y (b)
T (Cµ(0)) = X shape(T |≤b)
shape(T |≤b−1)(0) ∩ Wr−1(pol(b)(C)) .

Now,
 pol
(b)(C) =
 ¨zµ1+···+µb−1(z + 1) if µb = 1

zµ1+···+µb−1(z − i )(z + i ) if µb = 2.

By Lemmas 2.7 and 2.8, there is a unique point in Y (b)
T (Cµ(0)) when shape(T |b) is either
a single box, or two adjacent boxes. If shape(T |b) has two boxes that are non-adjacent,
of distance L > 1 apart, then the discriminant in Lemma 2.8 is −(1 − L−2) < 0, so both
solutions are non-real. Thus we see that ∏k
b=1 Y (b)
T (Cµ(0)) consists of 2# (T ) points,

which are all non-real, unless # (T ) = 0 (in which case ∏k
b=1 Y (b)
T (Cµ(0)) consists of a
single real point).
By Proposition 4.11, it follows that YT (Cµ(0)) consists of 2
# (T ) points; none are
ξσ-ﬁxed, unless # (T ) = 0.

Note that by Lemma 4.15, Y (Cµ(0)) = ⋃
T ∈Tab(λ;µ) YT (Cµ(0)) consists of f λ distinct
(reduced) points. Abusing notation slightly, we deﬁne

YT (Cµ(u)) := {y(u) ∈ Y (Cµ(u)) | lim
u→0 y(u) ∈ YT (Cµ(0))} .

Proof of Lemma 2.15. The curves Cµ(u) are actually deﬁned over C(u), and hence the
points of Y (Cµ(u)) are deﬁned over some algebraic extension of C(u). This, together
with the fact the limit points over Cµ(0) are distinct implies that the f λ points of Y (Cµ(u))
are distinct and their coordinates are deﬁned by power series with a positive radius of
convergence.
If y(u) ∈ Y λ(C((u))) is ξσ-ﬁxed, then limu→0 y(u) is ξσ-ﬁxed. Conversely, if y(u) is
not ξσ-ﬁxed, then either limu→0 y(u) is also not ξσ-ﬁxed, or limu→0 y(u) = limu→0 ξσy(u).
The latter does not occur for points in Y (Cµ(u)), since the points of Y (Cµ(0)) are dis-
tinct. Therefore y(u) ∈ Y (Cµ(u)) is ξσ-ﬁxed if and only if limu→0 ∈ Y (C) is ξσ-ﬁxed.
Now, deﬁne WT := {π(y(u)) | y(u) ∈ YT (Cµ(u))} .

35

Since π : Y (C) → Wr−1(Hµ) is an isomorphism, WT consists of 2
# (T ) points, deﬁned by
power series with a positive radius of convergence. To see that the normalized Plücker
coordinates are power series, note that limu→0 x(u) ∈ X λ for x(u) ∈ Wr−1(Hµ), which
would be false if some normalized Plücker coordinate involved a negative power of u.
Moreover, this isomorphism establishes property (a). To see that property (b) holds, let
x(u) ∈ WT , and write x(u) = π(y(u)), y(u) ∈ YT (Cµ(u)). Then

lim
u→0
   1 0

0 u
µb  x(u) = y(0)
(b) ,

which is in X shape(T |≤b) by Theorem 4.7. By Proposition 4.10, none of the points of WT
are real except when # (T ) = 0, so property (c) holds.

4.5 Paths in M 0,n+3

Fix a composition µ = (µ1, . . . , µk), with µi ∈ {1, 2}, and an index b such that µb = 2.
Let µ′ = (µ1, . . . , µb−1, 1, 1, µb+1, . . . , µk). We now deﬁne curves Gt(u) ∈ M 0,n+3, for
each t ∈ [0, 1], u ∈ [0, ϵ], where ϵ is a (sufﬁciently small) positive real number. These
curves have the property that G0(u) = Cµ′(u) and G1(t) = Cµ(u), so for ﬁxed u, t 7→
Gt(u) is a path from Cµ′(u) to Cµ(u) in M 0,n+3.
First, suppose u > 0. In this case, we can specify Gt(u) by specifying the marked
points a1, . . . , an. Let c := µb. For j /∈ {c, c + 1}, a j is independent of t, and is deﬁned
by (4.6). The marked points ac and ac+1 depend on t, and are deﬁned as follows.

ac =
 ¨(1 − t)uc + tuc+1 if 0 ≤ t ≤ 1
2
eπi (t− 1
2 )( 1
2 uc + 1
2 uc+1) if 1
2 ≤ t ≤ 1

ac+1 =
 ¨tuc + (1 − t)uc+1 if 0 ≤ t ≤ 1
2
e−πi (t− 1
2 )( 1
2 uc + 1
2 uc+1) if 1
2 ≤ t ≤ 1.

For t ̸= 1
2 , a1, . . . , an are distinct and distinct from {0, 1, ∞} so this uniquely speciﬁes
a curve in M0,n+3. For t = 1
2 , we have a double marked point, ac = ac−1 but all other
marked points are distinct, so this is still a P1-chain (though not in M0,n+3).
Note that the marked points ac and ac+1 begin at uc and uc+1 respectively (when
t = 0). They come together along the real axis and collide (when t = 1
2 ) to produce a
double marked point at 1
2 (uc + uc+1). Then they move apart as a conjugate pair along a
circle in the complex plane, to end up at ± i
2 (uc + uc+1) (when t = 1). See Figure 4.3.
For u = 0 we deﬁne the curve Gt(0) := limu→0 Gt(u), for every t ∈ [0, 1]. For
t = 0, 1 we have G0(0) = Cµ′(0) and G1(0) = Cµ(0), as described in Proposition 4.13.
These curves have k + 2 and k + 1 components respectively. For t ∈ (0, 1), Gt(0) is a
P1-chain with k + 1 components, b0 = k + 1, speciﬁed by the following coordinate data:

• for j /∈ {c, c + 1}, b j and a(b j )
j are the same as for Cµ(0);

36

0 ∞

1

i
2 (uc + uc+1)

− i
2 (uc + uc+1)

uc+1 uc

Figure 4.3: The path Gt(u) in M 0,n+3, for u > 0.

• bc = bc+1 = b, and
 a(b)
c =
 ¨1 − t if 0 < t ≤ 1
2
1
2 eπi (t− 1
2 ) if 1
2 ≤ t ≤ 1

a(b)
c+1 =
 ¨t if 0 < t ≤ 1
2
1
2 e−πi (t− 1
2 ) if 1
2 ≤ t ≤ 1.

See Figure 4.4. Note that as t → 0, ac+1 approaches a node; hence at t = 0, a new
component forms such that ac and ac+1 are on different components.

Proposition 4.16. The map
 G : [0, 1] × [0, ϵ] → M 0,n+3
(t, u) 7→ Gt(u)

is continuous.

Proof. Using the embedding (4.4), we must show that for each (p, q, r, s), the map
(t, u) 7→ θp,q,r,s(Gt(u)) is continuous. Since Gt(u) is a P1-chain for all (t, u), it sufﬁces to
show this for (p, q, r, s) = (0, a j1, ∞, a j2), j1 < j2. This is straightforward. For example,
in the case (p, q, r, s) = (0, ac, ∞, ac+1), we ﬁnd that θp,q,r,s(Gt(u)) = ac+1
ac , which is a
ratio of two continuous functions, and the denominator is never zero.

37

0 1 ∞ac+1 ac

· · · · · ·

Figure 4.4: The limiting path Gt(0) in M 0,n+3.

All of the curves Gt(u) are real, but not all with respect to the same real structure.
Deﬁne σ ∈ Sn as in (4.7), and deﬁne σ′ ∈ Sn analogously, with µ
′ in place of µ. For
(t, u) ∈ [0, 1
2 ] × [0, ϵ] we have Gt(u) ∈ M 0,n+3(Rσ′), and for (t, u) ∈ [ 1
2 , 1] × [0, ϵ] we
have Gt(u) ∈ M 0,n+3(Rσ). If t = 1
2 , the curve is real with respect to both real structures,
which is possible because G1/2(u) has a double marked point, and is therefore not in
M0,n+3.

4.6 Paths in Y λ

We now lift the family of paths Gt(u) in M 0,n+3 to a family of paths in Y λ. Projecting
to X λ will give the paths we need for Lemmas 3.16 and 3.15, thereby allowing us to
prove these statements.
Let µ, µ
′ be as in the previous section. Suppose T ′ ∈ MN(λ; µ′). Let T ∈ Tab(λ; µ)
be the tableau obtained by decrementing all entries b + 1, . . . , k + 1. Then T may or
may not be a Murnaghan–Nakayama tableau: we have T ∈ MN(λ; µ) if and only if b
and b + 1 are adjacent in T ′. We consider these two cases separately.
First, suppose T ∈ MN(λ; µ). Then T and T ′ are as in the statement of Lemma 3.15.
In this case, Gt(u) lifts isomorphically to a family of curves in Y λ, as shown in Figure 4.5.

Lemma 4.17 (Path lifting, / case). For sufﬁciently small ϵ > 0, there exists a contin-
uous map
 Γ : [0, 1] × [0, ϵ] → Y λ

(t, u) 7→ Γt(u) ,

with the following properties.

(a) (Path lifting.) For all (t, u), Ψ(Γt(u)) = Gt(u).

(b) (Connecting T to T ′.) Γ0(u) ∈ YT ′(Cµ′(u)) and Γ1(u) ∈ YT (Cµ(u)).

(c) (No ramiﬁcation.) For all (t, u), Γt(u) is a reduced point of the ﬁbre Y (Gt(u)).

(d) (Compatibility with real structure.) Γt(u) ∈ Y λ(Rσ′) for t ∈ [0, 1
2 ], and Γt(u) ∈
Y λ(Rσ) for t ∈ [ 1
2 , 1].
 38

Gt(u)

Γt(u)
 t = 0 t = 1
2
 t = 1

Cµ′(u)
 Cµ(u)

YT ′(Cµ′(u)) YT (Cµ(u))

Ψ

Figure 4.5: The lift Γ of Gt(u) constructed in Lemma 4.17. The endpoints of Gt(u)
are Cµ′(u) (at t = 0) and Cµ(u) (at t = 1), which lift to YT ′(Cµ′(u)) and YT (Cµ(u))
respectively. The ﬁbre over t = 1
2 maps to Z λ or Z λ in X λ(R), depending on shape(T |b).

(e) (Crossing Z λ or Z λ .) For u > 0, π(Γ1/2(u)) ∈ Z λ if shape(T |b) is a horizontal
domino, and π(Γ1/2(u)) ∈ Z λ if shape(T |b) is a vertical domino.

Proof. By Lemma 4.15, there is a unique reduced point Γ0(0) ∈ YT ′(G0(0)) and by a
similar argument, there is a unique reduced point Γt(0) ∈ YT (G0(0)) for all t ∈ (0, 1].
This deﬁnes a continuous path Γt(0), t ∈ [0, 1]. As in the proof of Lemma 4.15 we
see that Γt(0) is ξσ′-ﬁxed for 0 ≤ t ≤ 1
2 , and ξσ-ﬁxed for 1
2 ≤ t ≤ 1. When t = 1
2 ,
the curve G1/2(0) has a double marked point ac = ac+1, c = µb. By Corollary 4.8,
πc(Γ1/2(0)) ∈ X (1)∩Q(b)
T or πc(Γ1/2(0)) ∈ X (1)∩Q(b)
T . But by Lemma 2.2, if shape(T |b)
is a vertical domino then X (1) ∩ Q(b)
T is empty, and if shape(T |b) is a vertical domino,
then X (1) ∩ Q(b)
T is empty. Thus we must have πc(Γ1/2(0)) ∈ X (1) if shape(T |b) is a
horizontal domino, and πc(Γ1/2(0)) ∈ X (1) if shape(T |b) is a vertical domino.
Since all points of these ﬁbres are reduced and the map Ψ : Y λ → M 0,n+3 is ﬁnite,
this extends uniquely to a continuous family Γ : [0, 1] × [0, ϵ] → Y λ, satisfying (a)
and (c), for some sufﬁciently small ϵ. By construction, (b) is also satisﬁed. For ﬁxed
t ∈ [0, 1
2 ], Gt(u) is ξσ′-ﬁxed for all u. Thus, Γt(u) can only cease to be ξσ′-ﬁxed at a
double point of the ﬁbre Y (Gt(u)). Since property (c) ensures that there are no such
points for u ∈ [0, ϵ], Γt(u) is ξσ′-ﬁxed for all such u. A similar argument holds for
t ∈ [ 1
2 , 1], which establishes (d). When t = 1
2 , ac = ac+1 is a double marked point
of the curve G1/2(u); by continuity, πc(Γ1/2(u)) ∈ X (1) if shape(T |b) is a horizontal

39

domino, and πc(Γ1/2(u)) ∈ X (1) if shape(T |b) is a vertical domino. But on Y λ, πc and
π are related by a transformation φ ∈ B+ ⊂ PGL2(C), so the previous statement implies
(e).

Proof of Lemma 3.15. Let Γt(u) be as in Lemma 4.17. Consider the path γ : [0, 1] →
X λ(C), deﬁned by γt := π(Γt(ϵ)), t ∈ [0, 1]. First note that γt is in fact a path in
X λ(R), by property (d) and Proposition 4.10. Next note that if follows from property
(b) and the deﬁnition of WT (see Proof of Lemma 2.15), π(Γ0(u)) ∈ WT ; therefore
γ0 = wT ′. Similarly γ1 = wT .
Let gt := Wr(γt) the image of the path γt in Pn(R). Note that we also have gt =
pol(Gt(ϵ)) By property (c) and Proposition 4.3, γt is a reduced point of Wr
−1(gt). In
particular, this means γt /∈ R
λ(R), for all t ∈ (0, 1).
By property (e), γ1/2 ∈ Z λ (R) if shape(T |b) is a horizontal domino, and γ1/2 ∈ Z λ(R)
if shape(T |b) is a vertical domino. Since t = 1
2 is the only value of t for which gt has a
repeated root, there are no other crossings of either of these varieties. To see that the
crossing at t = 1
2 is a simple crossing, note that since γ1/2 /∈ R
λ(R), Wr : X λ(R) → Pn(R)
is a diffeomorphism in a neighbourhood of γ1/2. Thus γt has a simple crossing of Z λ (R)
or Z λ(R) at t = 1
2 if and only if gt has a a simple crossing of the discriminant variety
∆n(R). Since gt = pol(Gt(ϵ)) is given completely explicitly, it is straightforward to
check that this is a simple crossing.

Now, suppose T /∈ MN(λ; µ). This means that b and b + 1 are non-adjacent in
T ′. Therefore switching the positions of these entries results in another tableau T ′′.
Note that both T ′, T ′′ ∈ MN(λ; µ′), and are related as in the statement of Lemma 3.16.
Moreover, this relation is symmetrical, and both are related to T in the same way.
Note that since T is not a Murnaghan–Nakayama tableau, by Lemma 4.15 the ﬁbre
YT (G1(0)) = YT (Cµ(0)) has no ξσ-ﬁxed points. We will therefore not be able to lift
all Gt(u) to Y λ, in a way that satisﬁes properties (a)–(d) of Lemma 4.17, because we
already know (d) must be false at (t, u) = (1, 0). Instead, we restrict the domain from
[0, 1] × [0, ϵ] to the subset over which (d) will hold. We then obtain two different lifts
of Gt(u) over this domain, which are associated to the two tableaux T ′ and T ′′. See
Figure 4.6.

Lemma 4.18 (Path lifting, case). For sufﬁciently small ϵ > 0, there exists a subset
K ⊂ [0, 1] × [0, ϵ] and continuous maps

Γ ′ : K → Y λ

(t, u) 7→ Γ ′
t (u)
 Γ ′′ : K → Y λ

(t, u) 7→ Γ ′′
t (u) ,

with the following properties.

(a) (Path lifting.) For all (t, u) ∈ K, Ψ(Γ ′
t (u)) = Ψ(Γ ′′
t (u)) = Gt(u).

40

Gt(u)

Γ ′′
t (u)

Γ ′
t (u)
 t = 0 t = 1
2
 tmax t = 1

Cµ′(u)
 Cµ(u)

Ψ

Figure 4.6: The two lifts Γ ′, Γ ′′ of Gt(u) constructed in Lemma 4.18. The ﬁbres over
t = 1
2 map to Z λ and Z λ in X λ(R), while the ﬁbre over t = tmax(u) maps to Rλ(R).

(b) (Shape of K.) K is of the form

K = {(t, u) | u ∈ [0, ϵ], t ∈ [0, tmax(u)]} .

where tmax : [0, ϵ] → ( 1
2 , 1) is a function, in particular tmax > 1
2 .

(c) (Starting from T ′ and T ′′.) Γ ′
0(u) ∈ YT ′(Cµ′(u)) and Γ ′′
0 (u) ∈ YT ′′(Cµ′(u)).

(d) (No ramiﬁcation until tmax.) For (t, u) ∈ K with t < tmax(u), Γ ′
t (u) and Γ ′′
t (u) are
reduced points of the ﬁbre Y (Gt(u)).

(e) (Paths join at tmax.) For t = tmax(u), Γ ′
t (u) = Γ ′′
t (u) is a double point of the ﬁbre
Y (Gt(u)).

(f) (Compatibility with real structure.) Γ ′
t (u) ∈ Y λ(Rσ′) for t ∈ [0, 1
2 ], and Γ ′
t (u) ∈
Y λ(Rσ) for t ∈ [ 1
2 , tmax(u)]. The same holds for Γ ′′.

(g) (Crossing Z λ and Z λ .) Either π(Γ ′
1/2(u)) ∈ Z λ and π(Γ ′′
1/2(u)) ∈ Z λ for all u > 0,
or vice-versa.

Proof. First, we compute YT (Gt(0)), for t ∈ (0, 1]. Proceeding as in Lemma 4.15, we
ﬁnd that YT (Gt(0)) consists of two distinct ξσ′-ﬁxed points if t ∈ (0, 1
2 ]. The limit
ﬁbre limt→0 YT (Gt(0)) = YT ′(Cµ′(0)) ∪ YT ′′(Cµ′(0)); again we have two distinct ξσ′-ﬁxed

41

points. For t ∈ [ 1
2 , 1], the discriminant in Lemma 2.8 for computing Y (b)
T (Gt(0)) is equal
to L−2 − sin2  π(t − 1
2 )
; hence YT (Gt(0)) consists of:

• two distinct ξσ-ﬁxed points if t < 1
2 + 1
π arcsin(L−1);
• a double ξσ-ﬁxed point if t = 1
2 + 1
π arcsin(L−1);
• two distinct ξσ-conjugate points if t > 1
2 + 1
π arcsin(L−1).

where L is the distance between the entries b and b + 1 in T ′.
Let J ⊂ M 0,n+3 denote the image of the map [0, 1] → M 0,n+3, t 7→ Gt(0). Then
Ψ −1(J) ∩ Q T is the union of all YT (Gt(0)), t ∈ (0, 1], together with limt→0 YT (Gt(0)) =
YT ′(Cµ′(0)) ∪ YT ′′(Cµ′(0)). Since Ψ −1(J) ∩ Q T is a closed subset of Ψ −1(J), we can ﬁnd
an open subset U ⊂ Y λ, containing Ψ −1(J) ∩ Q T such that U is a component on
Ψ(Ψ −1(U )).
Assuming ϵ > 0 is sufﬁciently small, Y (Gt(u))∩U is then a ﬁnite scheme of length 2,
for all (t, u) ∈ [0, 1] × [0, ϵ]. Hence this is either two distinct points, or a (non-reduced)
double point. By the same argument as in Lemma 4.17, Y (Gt(u)) ∩ U consists of two
distinct points in Y λ(Rσ′) for t ∈ [0, 1
2 ], u > 0. Moreover, for t = 1
2 , u > 0, the two
points of Y (Gt(u)) ∩ U are also in Y λ(Rσ′), and for t = 1 they are not in Y λ(Rσ′). This
implies that for all u there exists a t ∈ ( 1
2 , 1) such that Y (Gt(u)) ∩ U is a double point.
We put tmax(u) := min{t ∈ [0, 1] | Y (Gt(u)) ∩ U is a double point} ,

and take (b) to be the deﬁnition of K. Note that K is simply connected, and therefore
Ψ : Ψ −1(K) ∩ U → K is a topologicially trivial two-to-one covering map away from
t = tmax(u).
We can therefore deﬁne Γ ′ : K → Y λ to be the unique map such that Γ ′
0(0) is the
unique point in YT ′(Cµ′(0)), and Γ ′
t (u) ∈ P(Gt(u)) ∩ U for all (t, u) ∈ K. Similarly we
deﬁne Γ ′′ : K → Y λ, with T ′′ in place of T ′. Properties (a), (c), (d), (e) are immediate,
and the proof of (f) is identical to the proof of (d) in Lemma 4.17.
When t = 1
2 , the curve G1/2(0) has a double marked point ac = ac+1, c = µb. By
Corollary 4.8, either πc(Γ ′
1/2(0)) ∈ X (1) ∩ Q(b)
T or πc(Γ ′
1/2(0)) ∈ X (1) ∩ Q(b)
T , and the

same is true for Γ ′′. By Lemma 2.2, both X (1) ∩ Q(b)
T and X (1) ∩ Q(b)
T consist of a sin-
gle point. Recall that YT (G1/2(0)) is identiﬁed with ∏k
i=1 Y (i)
T (G1/2(0)). By Lemmas 2.7
and 2.8, every term in this product consists of a single point, except Y (b)
T (G1/2(0)) which
has two points. Γ ′
1/2(0) and Γ ′′
1/2(0) are distinct points of YT (G1/2(0)), and the only co-
ordinate on which they can differ is Γ ′
1/2(0)
(b) ̸= Γ ′′
1/2(0)
(b). Equivalently πc(Γ ′
1/2(0)) ̸=

πc(Γ ′′
1/2(0)). It follows that we have either πµb(Γ ′
1/2(0)) ∈ X (1)∩Q(b)
T and πµb(Γ ′′
1/2(0)) ∈

X (1) ∩ Q(b)
T , or the other way around. Arguing now as in the proof of Lemma 4.17, we
deduce (g).

Remark 4.19. With a more thorough analysis of YT (Gt(0)), t ∈ [0, 1
2 ], property (g) in
Lemma 4.17 can be replaced by the following stronger statement. If b is left of b + 1 in

42

T ′ then π(Γ ′
1/2(u)) ∈ Z λ and π(Γ ′′
1/2(u)) ∈ Z λ. If b is right of b + 1, the identiﬁcation is
the other way around. We omit the proof, since we do not actually need this fact here.
Note that in each case, the two boxes b, b +1 rectify to the corresponding domino shape
(compare with [24, Theorem 6.4] and [30, Theorem 4.4]).

Proof of Lemma 3.16. Let K, tmax, Γ ′
t (u) and Γ ′′
t (u) be as in Lemma 4.18. We deﬁne the
path γ : [0, 1] → X λ(C) by joining together the paths π(Γ ′
t (ϵ)) and π(Γ ′′
t (ϵ)):

γt :=
 




π(Γ ′
2t(ϵ)) for t ∈ [0, 1
4 ]

π(Γ ′
1/2+(tmax(ϵ)−1/2)(4t−1)(ϵ)) for t ∈ [ 1
4 , 1
2 ]

π(Γ ′′
1/2+(tmax(ϵ)−1/2)(3−4t)(ϵ)) for t ∈ [ 1
2 , 3
4 ]

π(Γ ′′
2−2t(ϵ)) for t ∈ [ 3
4 , 1].

Let gt = Wr(γt); note that gt = g1−t.
Many pieces of the argument are essentially the same as in the proof of Lemma 3.15.
By property (f), γt ∈ X λ(R) for all t ∈ [0, 1]. By property (c), γ0 = π(Γ ′
0(ϵ)) = wT ′ and
γ1 = π(Γ ′′
0 (ϵ)) = wT ′′. By property (g), one of γ1/4 = π(Γ ′
1/2(ϵ)) and γ3/4 = π(Γ ′′
1/2(ϵ))
is in Z λ (R) and the other is in Z λ(R), and these are the only points γt in either of these
varieties. These are simple crossings of Z λ (R) and Z λ(R), by the same reasoning as in
the proof of Lemma 3.15.
We now consider crossings of R
λ(R). By property (e), γ1/2 = π(Γ ′
1/2(ϵ)) = π(Γ ′
1/2(ϵ))
is a double point of Wr
−1(g1/2); thus γ1/2 ∈ R
λ(R). This is certainly a crossing, because
γ1/2−ε and γ1/2+ε are two different points of the ﬁbre over g1/2−ε = g1/2+ε, and therefore
in different components of some neighbourhood of Wr
−1(g1/2)\R
λ(R). By Lemma 3.14,
γ1/2 is a smooth point of R
λ(R), and therefore this is a simple crossing. By property (d),
γt /∈ R
λ for t ̸= 1
2 .

5 Upper and lower bounds

5.1 Bounds from Theorem 1.3

For g ∈ Pn(R), let Ng denote the number of real points in the ﬁbre Wr−1(g), counted
with algebraic multiplicity. One consequence of Theorem 1.3 is that we obtain bounds
on Ng. When the lower bound is non-zero, this gives a proof of the existence of real
solutions to the equation Wr( f1, . . . , fd) = g.

Corollary 1.4. If g ∈ Pn(µ), then
 |χ λ(µ)| ≤ Ng ≤ f λ .

Proof. If g ∈ Pn(µ) and g is a regular value of the Wronski map, the the multiplicities
of the points in Wr−1(g) are all 1, and the topological degree of the map Wr : X λ(µ) →

43

Pn(µ) is a signed count of the points in Wr
−1(g). Thus in this case, the lower bound
Ng ≥ |χ λ(µ)| holds. Since Ng is an upper semi-continuous function of g, the result
remains true if we pass to the closure.
For the upper bound, note that f λ is the number of complex points in any ﬁbre of the
map Wr : X λ(C) → Pn(C), and the real points in the ﬁbre are subset of the complex
points.

If g ∈ Pn(µ) for more than one µ (which occurs when g has repeated real roots),
then we get more than one lower bound. In general, there does not appear to be any
simple rule as to which µ will give the best lower bound. Of course, if all the roots of
g are all real, the best lower bound comes from µ = 1n, and Ng = f λ, regardless of
whether g has repeated roots. In particular, the upper bound in Corollary 1.4 is tight
for all µ, since it is achieved when all roots of g are real, and such g exist in Pn(µ).
Moreover, we can ﬁnd such g such that Wr−1(g) is reduced, which implies that the
upper bound can also be achieved by polynomials properly in Pn(µ), by starting with a
polynomial with only real roots in the closure, and perturbing.
In some cases, we can also see that the lower bound is tight.

Theorem 5.1. Let µ = (µ1, . . . , µk) be a composition of n, with µi ∈ {1, 2}. If all tableaux
in MN(λ; µ) have the same sign, then the lower bound in Corollary 1.4 is tight. That is,
there exists a polynomial g ∈ Pn(µ) such that Ng = |χ λ(µ)|.

Proof. Consider hµ ∈ Pn(µ). By Corollary 2.16, Nhµ = #MN(λ; µ). But if all tableaux
in MN(λ; µ) have the same sign, then #MN(λ; µ) = |χ λ(µ)|.

Note that for a given partition, there are many compositions with that associated
partition. If any one of these compositions satisﬁes the hypothesis of Theorem 5.1, then
we conclude the lower bound is tight.

Example 5.2. Here a few noteworthy cases where all tableaux in MN(λ; µ) have the
same sign, and hence Theorem 5.1 tells us that the lower bound is tight.

(i) If λ ⊢ n is any partition, and µ = (1n). This is the all real roots case, where the
lower bound is exact.

(ii) If |λ| is even, and µ = (2n2).

(iii) If |λ| is odd, and µ = (1, 2n2). Cases (ii) and (iii) are where we have the maximal
number of complex roots.

(iv) If λ = (λ1, λ2) ⊢ n is any 2-part partition, and µ = (1, 2l, 1n−2l−1), 0 ≤ l < n/2.
This, together with (ii), shows the lower bound is always tight if λ has two parts.

(v) If λ = md is a rectangle with dm even, and µ = (1, 2dm/2−1, 1).

44

(vi) If λ = (d, d − 1, . . . , 2, 1) is a staircase, and µ = (µ1, . . . , µk) is any composition
such that µk = 2. This, together with (i), shows that the lower bound is always
tight if λ is a staircase.

(vii) If λ = (λ1, . . . , λd) ⊢ n is any partition such that λi − λi+1 is odd for all i =
1, . . . , d − 1, and µ = (1n1, 2n2), where n1 + 2n2 = n. This generalizes (vi): the
lower bound is tight for all such partitions λ.

In case (vi), χ λ(µ) = #MN(λ; µ) = 0, and Theorem 5.1 is asserting that the Wronski
map Wr : X λ(µ) → Pn(µ) is not surjective. This also happens in (v), in the case where
m and d are both even, as was ﬁrst shown in [5].

5.2 Eremenko and Gabrielov’s lower bound

Eremenko and Gabrielov computed degrees of real Wronski maps in [4]. Their result is
stated for the projective real Wronski map Wr : Gr(d, Rd+m) → Pdm(R), but as is pointed
out in [33], the computation can be done on any Schubert cell and we state the result
as such here. We include a concise proof, based on Lemma 3.16.

Deﬁnition 5.3. Let T ∈ SYT(λ). An inversion in T is a pair of cells (i, j), (i′, j′) ∈ λ
such that i < i′ and T (i, j) > T (i′, j′). Let inv(T ) denote the number of inversions in T .

Theorem 5.4 (Eremenko–Gabrielov). With respect to the ambient orientation, the topo-
logical degree of the Wronski map Wr : X λ(R) → Pn(R) is

Iλ := ∑

T ∈SYT(λ)
(−1)
inv(T ) .

Proof. We claim that for every tableau T ∈ SYT(λ), asgn(wT ) = (−1)
inv(T ). If T =
T0, this is certainly true. Suppose T, T ′ ∈ SYT(λ) are two tableaux related as in
Lemma 3.16. There is path joining wT to wT ′, along which the ambient sign changes
exactly once, at the simple crossing of Rλ(R). Therefore asgn(wT ) = −asgn(wT ′). We
also have inv(T ) = inv(T ′)±1, and the claim follows. Therefore, the topological degree
of the Wronski map is ∑

x∈Wr−1(h1n ) asgn(x) = ∑

T ∈SYT(λ) asgn(wT ) = Iλ .

This also yields a lower bound for the number of real points in the ﬁbre of the
Wronski map.

Corollary 5.5 (Eremenko–Gabrielov). For every g ∈ Pn(R), we have

|Iλ| ≤ Ng .

45

In the case of a rectangle, λ = md, the Schubert cell X λ(R) is an open dense subset
of Gr(d, Rd+m). If m + d is odd, then both Gr(d, Rd+m) and Pdm(R) are non-orientable.
Eremenko and Gabrielov showed that the real projective Wronski map lifts to a map be-
tween the oriented double covers of these spaces, and hence has a well-deﬁned degree
up to sign, which is ±Iλ. In this case, Iλ ̸= 0 [36]. However, if m + d is even, m, d ≥ 2,
then Iλ = 0. If m and d are both even, this can be attributed to the fact that Gr(d, Rd+m)
is orientable but Pdm(R) is not, and the degree of the real projective Wronski map can-
not be deﬁned. Example 5.2 also shows that the real Wronski map is not surjective in
this case. But if m and d are both odd, then both spaces are orientable, and there is no
obvious geometric reason why the topological degree is 0.
By comparing the lower bounds in Corollaries 1.4 and 5.5, one can see that in gen-
eral, neither lower bound is tight. We include two examples, which ﬁrst appeared in
[17].

Example 5.6. Let λ = 3
5. Then |χ λ(µ)| ≥ 6 for every partition µ of the form 2n21n1.
(The minimum value of |χ λ(µ)| occurs for µ = 2
417.) Thus, Ng ≥ 6 for every g ∈
P15(R). As noted above, Iλ = 0 in this case, which shows that the Eremenko–Gabrielov
lower bound is not tight.

Example 5.7. Let λ = 3
6. Then Iλ = 12, which means Ng ≥ 12 for all g ∈ P18(R).
On the other hand, if µ = 2
61
6 or µ = 2
71
4, then χ λ(µ) = 0, so the bound from
Corollary 1.4 is not tight.

5.3 Mukhin and Tarasov’s lower bound

As mentioned in the introduction, the lower bound in Corollary 1.4 is a special case of a
more general inequality. Let a1, . . . , ak be distinct real numbers, and let b1, b1, . . . , bl, bl
be distinct complex numbers. Consider a 0-dimensional intersection of the form

X α1(a1) ∩ · · · ∩ X αk(ak) ∩ X β 1(b1) ∩ · · · ∩ X β l (bl) ∩ X β 1(b1) ∩ · · · ∩ X β l (bl) (5.1)

inside the Grassmannian Gr(d, Cd+m−1[z]). (Here, α
1, . . . , αk, β 1, . . . , β l are partitions.)
In [17], Mukhin and Tarasov gave a lower bound for the number of real points of such
an intersection, which depends only on the discrete data (k, l, α
1, . . . , αk, β 1, . . . , β l).
In the case where, α
1 = λ∨, α
2 = · · · = αk = β 1 = · · · = β l = , and a1 = ∞, the
intersection (5.1) is precisely Wr−1(g), where

g(z) =
 k∏

i=2 (z + ai) ·
 l∏

j=1 (z + b j)(z + b j) .

The lower bound in Corollary 1.4 coincides with the Mukhin–Tarasov lower bound in
this special case. (This equivalence is not completely obvious the way things are stated
in [17], but it is not hard to show using standard results in symmetric function theory.)

46

The two proofs, however, are completely different. Mukhin and Tarasov obtain their
inequality using the fact that the number of real eigenvalues of an operator that is self-
adjoint with respect to an indeﬁnite Hermitian form is at least the absolute value of the
signature of the form. The machinery in [19] identiﬁes the points of intersection (5.1)
with one-dimensional eigenspaces of an algebra commuting self-adjoint operators; the
point is real if and only if the associated eigenvalues are real. Hence, they obtain a
lower bound by computing the signature of the associated form. Since the signature of
the form depends only on the discrete data, it is an invariant for the problem. We do not
know why this invariant coincides with the topological degree of the restricted Wronski
map with the character orientation. It is fairly natural to conjecture that the sign of a
real intersection point is equal to the signature of the Hermitian form restricted to the
associated eigenspace.
In the general case, by Lemma 2.1, intersection (5.1) is contained in the ﬁbre Wr
−1(g)

g(z) =
 k∏

i=1 (z + ai)
|αi | ·
 l∏

j=1
  (z + b j)(z + b j)
|β j | ,

and we might try to use this to count the points of (5.1) with signs. Unfortunately,
these signs will not always be deﬁned, either because g /∈ Pn(µ) for any µ, or because
g is a critical value of the Wronski map. It is nevertheless possible to give a topological
proof of the Mukhin–Tarasov lower bound in its full generality, using Theorem 1.3 in
combination with results from [24, 26]. Although the argument is too long to include
here in full detail, we give a brief sketch of how this can be done.
Let λ = md, so X λ(R) is an open dense subset of Gr(d, Rd+m). The real points of
the intersection (5.1) will be X λ(R), and as noted above, speciﬁcally contained in the
ﬁbre Wr
−1(g). Perturb g ∈ Pn(R) to a nearby polynomial g ′ which is a regular value
of the Wronski map with distinct roots, in such a way that the number of real roots
does not change. For any point x in the intersection (5.1), we can consider all points
x
′ ∈ Wr−1(g) that perturbations of x. By properties of g ′ each such x
′ has a well-deﬁned
sign. We deﬁne the weight of x to be the average of the signs of all x
′ ∈ Wr−1(g ′)
that are perturbations of x. One can show the sum of the weights of the points in the
intersection (5.1) is an invariant (i.e. it depends only on the discrete data), by relating
to the topological degree of a restriction of the Wronski map. Moreover, since the weight
of x is a rational number in the interval [−1, 1], this invariant gives a lower bound on
the number of points in the intersection.
It remains to compute the invariant. It sufﬁces to compute it for a single tuple of
parameters (a1, . . . , ak, b1, . . . bl), and a speciﬁc perturbation g. We take ai = ui, and
b j = i uk+ j, where (at the end of the day) u will be evaluated at some small parameter
ϵ > 0, and we perturb the roots of g in such a way that all roots remain either real
or pure imaginary. Using [26, Theorem 3.15] and degeneration arguments similar to
Section 4, we can label the points of the intersection by certain equivalence classes of
tableaux, and we can say which of these points are real. The tableaux themselves label
the perturbed points, and the equivalence classes tell us which points of Wr
−1(g ′) are

47

perturbations of of the same point in Wr
−1(g). As in Section 3, we can compute the signs
of the signs of the points in Wr
−1(g ′) from the associated tableaux, and hence compute
the weights of the points in (5.1). (It turns out that, for this ﬁbre, all perturbations
of the same point have the same sign, so the weights are in fact ±1.) This gives a
combinatorial formula for the sum of the weights of the points in the intersection. We
note that when there are no complex points (l = 0), this argument reproduces the proof
of the Littlewood-Richardson rule in [24]. Finally, using known results from symmetric
function theory, one can identify this combinatorial formula as equivalent to the formula
given by Mukhin and Tarasov.
We note that proof of [26, Theorem 3.15] referenced above uses Theorem 1.1 in
an essential way. As such, to prove the stronger theorem independently of Mukhin–
Tarasov–Varchenko’s work, one needs to establish the weaker Theorem 1.3 ﬁrst.

6 Concluding remarks

6.1 Generalization to Richardson varieties

With a few small changes, Theorem 1.3 generalizes to the open Richardson variety.
Let λ/λ′ be a skew shape such that |λ/λ′| = n. The open Richardson variety is the
intersection of Schubert cells X λ/λ′ := X ◦
λ∨(∞) ∩ X ◦
λ′(0). This is a smooth afﬁne variety.
Let P ◦
n := {g ∈ Pn | g(0) ̸= 0}. The Wronski map induces a ﬁnite proper map

Wrλ/λ′ : X λ/λ′ → P ◦
n
x 7→ z−|λ′| Wr(x, z) .

For a partition µ = 2n21n1 ⊢ n, we deﬁne P ◦
n (µ) := Pn(µ) ∩ P ◦
n (R), and X λ/λ′(µ) :=
Wr−1
λ/λ′(P ◦
n (µ)). As before, Wrλ/λ′ restricts to a proper map Wrλ/λ′ : X λ/λ′(µ) → P ◦
n (µ)
for each µ.
To proceed further, we use the following technical fact about X λ/λ′ (see [22]).

Lemma 6.1. The divisor class group of X λ/λ′(R) is trivial.

We can now deﬁne a character orientation function on X λ/λ′(R), with the following
modiﬁcations to the discussion in Section 3. We work over T1 = A1 \ {0} instead of A
1.
For a partition κ, let Y λ/λ′

κ ⊂ X λ/λ′ × T1 be the total space of the family of X κ(a)∩ X λ/λ′,
a ∈ T1. Then deﬁne Z λ/λ′

κ ⊂ X λ/λ′ to the image of the projection onto the ﬁrst factor. For
|κ| = 2, Z λ/λ′

κ ⊂ X λ/λ′ is a hypersurface. By Lemma 6.1, it is the zero locus of a single
real polynomial function Φλ/λ′

κ . From here, we can proceed exactly as in Section 3, using

Φλ/λ′ to deﬁne the character orientation of X λ/λ′(µ).

One can then compute the topological degree of Wrλ/λ′ : X λ/λ′(µ) → P ◦
n (µ) with
respect to the character orientation. The entire proof of Theorem 1.3 works almost

48

verbatim if we simply replace λ by λ/λ′ throughout. The biggest modiﬁcation is in
Section 4.1, where we need to replace the family (4.1) by

Y λ/λ′ := eX (a1) ∩ · · · ∩ eX (an) ∩ eX λ∨(∞) ∩ eX λ′(0) .

In this way, we obtain the following theorem.

Theorem 6.2. With the character orientation, the topological degree of the map Wrλ/λ′ :
X λ/λ′(µ) → P ◦
n (µ) is equal to χ λ/λ′(µ).

Here χ λ/λ′ denotes the skew symmetric group character (see [8]). We therefore also
obtain analogues of Corollaries 1.4 and 1.5.

Corollary 6.3. For g ∈ P ◦
n (R), let Ng be the number of real points in the ﬁbre Wr
−1
λ/λ′(g),

counted with algebraic multiplicity. If g ∈ P ◦
n (µ), then

|χ λ/λ′(µ)| ≤ Ng ≤ f λ/λ′ .

Corollary 6.4. Wrλ/λ′ : X λ/λ′(1n) → P ◦
n (1n) is a topologically trivial covering map of
degree f λ/λ′.

Corollary 6.4 can also be deduced without Theorem 6.2, as we explain next, in
Section 6.2.

Remark 6.5. It is important that Z λ ⊂ X λ/λ′ is a principal divisor over R. To see why,
recall that our goal is to construct an orientation of X (R) \ V (R), where X is a smooth
afﬁne variety over R and V ⊂ X is a hypersurface, such that the orientation reverses
along V (R). If X (R) is orientable, this implies the real line bundle associated to V (R)
must also be orientable, which, in our case, is guaranteed by Lemma 6.1. As an example
of what could go wrong, consider the circle X = Spec F[x, y]/〈x 2 + y 2 −1〉, and let V be
the point (1, 0). If F = R, V (R) is not a principal divisor on X (R), and clearly we cannot
orient X (R)\V (R) in such a way that the orientation reverses along V (R). Nevertheless
V (R) is locally principal, and its complexiﬁcation V (C) is a principal divisor of X (C),
so neither of these criteria is sufﬁcient.

6.2 Transversality

Since some of the known applications of the Shapiro–Shapiro conjecture rely on some
form of transversality or reducedness property, such as Corollary 1.5, we give a brief
account of those that are known to follow from Theorem 1.1. The strongest known
transversality theorem for Shapiro-type Schubert intersections is Mukhin, Tarasov and
Varchenko’s theorem in [19], which does not appear to follow easily from Theorem 1.1.
However, we do get some important special cases. These are deduced via the following
lemma (see [32, Theorem 13.2]).
 49

Lemma 6.6. Let ψ : X → Y be a ﬁnite morphism of smooth varieties deﬁned over R. If
U ⊂ Y (R) is an analytic open subset such that every point of ψ−1(U ) is real, then ψ is
unramiﬁed over U .

For example, taking ψ to be the Wronski map Wr : X λ → Pn, and U = Pn(1n)
yields Corollary 1.5.
We can also take ψ to be the map Wrλ/λ′ : X λ/λ′ → P ◦
n , and U = P ◦
n (1n), which
gives Corollary 6.4. Restated in terms of Schubert intersections, this says the following.

Corollary 6.7. Let α, β be partitions and let a1, a2, . . . , an+2 ∈ P1(R) be distinct, where
|α| + |β| + n = dm. Then the intersection

X (a1) ∩ · · · ∩ X (an) ∩ X α(an+1) ∩ X β (an+2)

in Gr(d, d + m) is transverse.

For the orthogonal Grassmannian OG(n, 2n+1), there is a ﬁnite map to projective
space which is an analogue of the Wronski map. In [25], the second author showed
that Theorem 1.1 implies an analogous reality theorem for OG(n, 2n+1), and thus
Lemma 6.6 can also be applied to OG(n, 2n+1). In particular, Theorem 1.1 implies
the analogue of Corollary 6.7 for OG(n, 2n+1). It is interesting to note that we do not
have an obvious analogue of Theorem 1.3 for OG(n, 2n+1), as there is only a single
codimension 2 Schubert variety in OG(n, 2n+1).

6.3 Open questions

Quite a few generalizations of Theorem 1.1 have been conjectured, supported by large
quantities of computational evidence. We will not give a complete overview of these
here, but instead refer the reader to the discussion in [32, Ch. 13 & 14]. Although it
is not immediately obvious how to generalize Theorem 1.3 to these other settings, we
hope that it will lead to new ideas toward solving these problems.
Since a large part of the proof of Theorem 1.3 involved the moduli space of sta-
ble curves, it is natural to wonder if there is an a statement analogous to Theorem 1.3
involving the ﬁnite family Ψ : Y λ → M 0,n+1, instead of the Wronski map. The semi-
algebraic sets X λ(µ) and Pn(µ) would be replaced by actual real loci Y λ(Rσ) and
M 0,n+1(Rσ) respectively. One would then expect the character orientation function to
be replaced by a section of the anticanonical bundle, which naturally deﬁnes an orien-
tation. This would be very nice, but there are some difﬁculties with this idea, not the
least of which is the fact that M 0,n+1(Rσ) is not always orientable.
Another possible approach to proving Theorem 1.3 would be to determine the char-
acter orientation function Φλ explicitly. With this, it should be possible to compute the
signs of the points wT directly, i.e. without using Lemmas 3.15 and 3.16. Conceivably,
this could yield a more concise proof. It would also be interesting to see if the ideas in
[17] can be used to obtain an alternate proof of Theorem 1.3.

50

Finally, the obvious question: is there a similar interpretation of χ λ(µ) if µ is an
arbitrary partition of n? We propose that the general answer should take the following
form. If σ ∈ Sn is a permutation of cycle type µ, and C ∈ M σ

0,n+1 is a σ-ﬁxed curve,
then χ λ(µ) = ∑

y∈Ψ−1(C)σ sgn(y)

where Ψ −1(C)
σ denotes the σ-ﬁxed subscheme of the ﬁbre of the map Ψ : Y λ →
M 0,n+1, and sgn(y) ∈ {±1} is some geometrically meaningful sign assigned to y. If
C is a P1-chain without double marked points, it is not hard to show that #Ψ −1(C)
σ =
#MN(λ; µ′) for some composition µ
′ with associated partition µ, so in this case, there
is some way to assign signs so that this equation is true. However, not all σ-ﬁxed curves
are of this form, and without some sort of geometric interpretation for the signs, this is
not particularly deep. The crux of the question is to explain the geometric meaning of
the signs in the Murnaghan–Nakayama rule.

References

[1] S. Billey and R. Vakil, Intersections of Schubert varieties and other permutation array
schemes, Algorithms in algebraic geometry (A. Dickenstein, F.-O. Schreyer, and A.
J. Sommese, eds.), IMA Vol. Math. Appl., 146, Springer, New York, 2008, pp.
21–54.

[2] M. Chan, A. López Martın, N. Pﬂueger and M. Teixidor i Bigas, Genera of Brill-
Noether curves and staircase paths in Young tableaux, Trans. Amer. Math. Soc., 370
(2018), 3405–3439.

[3] S. Devadoss, Combinatorial equivalence of real moduli spaces, Notices Amer. Math.
Soc., 51 (2004) no. 6, 620–628.

[4] A. Eremenko and A. Gabrielov, Degrees of real Wronski maps, Disc. Comp. Geom.,
28 (2002), 331–347.

[5] A. Eremenko and A. Gabrielov, Counterexamples to pole placement by static output
feedback. Linear Algebra Appl., 351/352 (2002), 211–218.

[6] D. Eisenbud and J. Harris, Divisors on general curves and cuspidal rational curves,
Invent. Math., 74 (1983), 371–418.

[7] J. M. Frame, G. d. B. Robinson and R. M. Thrall, The hook graphs of the symmetric
group, Canad. J. Math., 6 (1954), 316–325.

[8] A. Garsia and M. Wachs, Combinatorial aspects of skew representations of the sym-
metric group, J. Combin. Theory Ser. A, 50 (1989) no. 1, 47–81.

51

[9] M. Gillespie and J. Levinson, K-theory and monodromy of Schubert curves via gen-
eralized jeu de taquin, J. Alg. Comb., 45 (2017) no. 1, 191–243.

[10] I. Halacheva, J. Kamnitzer, L. Rybnikov, A. Weekes, Crystals and monodromy of
Bethe vectors, preprint (2017), arXiv:1708.05105.

[11] J. Hauenstein, N. Hein, A. Martín del Campo, and F. Sottile, Beyond the
Shapiro Conjecture and Eremenko-Gabrielov lower bounds, website (2010).
www.math.tamu.edu/∼frank.sottile/research/pages/lower_Shapiro/

[12] N. Hein, C. Hillar, and F. Sottile, Lower Bounds in Real Schubert Calculus, São Paulo
J. Math. Sci., 7 (2013) no. 1, 33–58.

[13] S. L. Kleiman, The transversality of a general translate, Compositio Math., 28
(1974), 287–297.

[14] V. Kharlamov and F. Sottile, Maximally inﬂected real rational curves, Mosc. Math.
J., 3 (2003), no. 3, 947–987, 1199–1200.

[15] A. Leykin and F. Sottile, Galois groups of Schubert problems via homotopy continu-
ation, Math. Comput., 28 (2009) no. 267, 1749-1765.

[16] K. Lu, E. Mukhin and A. Varchenko, Self-dual Grassmannian, Wronski map, and
representations of glN , sp2r, so2r+1, Pure Appl. Math. Q., 13 (2017), no. 2, 291–
335.

[17] E. Mukhin and V. Tarasov, Lower bounds for numbers of real solutions in problems
of Schubert calculus, Acta Math., 217, (2016), no. 1, 177–193.

[18] E. Mukhin, V. Tarasov and A. Varchenko, The B. and M. Shapiro conjecture in real
algebraic geometry and the Bethe Ansatz, Ann. Math., 170 (2009), no. 2, 863–881.

[19] E. Mukhin, V. Tarasov and A. Varchenko, Schubert calculus and representations of
general linear group, J. Amer. Math. Soc., 22 (2009), no. 4, 909–940.

[20] E. Mukhin, V. Tarasov and A. Varchenko, On reality property of Wronski maps,
Conﬂuentes Math., 1 (2009), no. 2, 225–247.

[21] J. Levinson, One-dimensional Schubert problems with respect to osculating ﬂags,
Canad. J. Math., 69 (2016), 143–177.

[22] J. Levinson and K. Purbhoo, Class groups of open Richardson varieties in the Grass-
mannian are trivial, J. Commut. Algebra, to appear.

[23] B. Osserman, A limit linear series moduli scheme, Ann. Inst. Four., 56 (2006) no.
4, 1165–1205.
 52

[24] K. Purbhoo, Jeu de taquin and a monodromy problem for Wronksians of polynomi-
als, Adv. Math., 224 (2010) no. 3, 827–862.

[25] K. Purbhoo, Reality and transversality for Schubert calculus in OG(n, 2n+1), Math.
Res. Lett., 17 (2010) no. 6, 1041–1046.

[26] K. Purbhoo, Wronskians, cyclic group actions, and ribbon tableaux, Trans. Amer.
Math. Soc., 365 (2013), 1977–2030.

[27] K. Purbhoo, A marvellous embedding of the Lagrangian Grassmannian, J. Combin.
Theory Ser. A, 155 (2018), 1–26.

[28] J. Rosenthal and F. Sottile, Some remarks on real and complex output feedback, Sys.
& Control Lett., 33 (1998), 73–80.

[29] L. Rybnikov, Cactus group and monodromy of Bethe vectors. Int. Math. Res. Not.,
2018 (2016) no. 1, 202–235.

[30] D. Speyer, Schubert problems with respect to osculating ﬂags of stable rational curves,
Alg. Geom., 1 (2014) no. 1, 14–45.

[31] F. Sottile, Frontiers of reality in Schubert calculus, Bull. Amer. Math. Soc., 47
(2010), no. 1, 31–71.

[32] F. Sottile, Real Solutions to Equations From Geometry, University Lecture Series,
57, AMS, 2011.

[33] F. Sottile and E. Soprunova, Lower Bounds for Real Solutions to Sparse Polynomial
Systems, Adv. Math., 204, (2006), no. 1, 116–151.

[34] F. Sottile and J. White, Double transitivity of Galois groups in Schubert calculus of
Grassmannians, Alg. Geom., 2 (2015), no. 4, 422–445.

[35] R. Vakil, Schubert induction, Ann. Math., 164 (2006), 489–512.

[36] D. White, Sign-balanced posets, J. Combin. Theory, 95 (2001), 1–38.

[37] N. White, The monodromy of real Bethe vectors for the Gaudin model, preprint
(2015), arXiv:1511.04740.

J. LEVINSON, MATHEMATICS DEPARTMENT, SIMON FRASER UNIVERSITY, BURNABY, BC, V5A 1S6, CANADA.
jake_levinson@sfu.ca.

K. PURBHOO, COMBINATORICS AND OPTIMIZATION DEPARTMENT, UNIVERSITY OF WATERLOO, WATERLOO,
ON, N2L 3G1, CANADA. kpurbhoo@uwaterloo.ca.

53
