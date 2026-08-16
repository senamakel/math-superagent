<!-- source: https://web.archive.org/web/2020/https://scholar.rose-hulman.edu/cgi/viewcontent.cgi?article=1090&context=rhumj | converted from PDF -->

Rose-Hulman Undergraduate Mathematics Journal Rose-Hulman Undergraduate Mathematics Journal

Volume 13
Issue 1  Article 2

Convex Hulls and the Casas-Alvero Conjecture for the Complex Convex Hulls and the Casas-Alvero Conjecture for the Complex
Plane Plane

Thomas Polstra
Georgia State University, thomaspolstra@gmail.com

Follow this and additional works at: https://scholar.rose-hulman.edu/rhumj

Recommended Citation Recommended Citation
Polstra, Thomas (2012) "Convex Hulls and the Casas-Alvero Conjecture for the Complex Plane," Rose-
Hulman Undergraduate Mathematics Journal: Vol. 13 : Iss. 1 , Article 2.
Available at: https://scholar.rose-hulman.edu/rhumj/vol13/iss1/2

Rose-
Hulman
Undergraduate
Mathematics
Journal

Sponsored by

Rose-Hulman Institute of Technology

Department of Mathematics

Terre Haute, IN 47803

Email: mathjournal@rose-hulman.edu

http://www.rose-hulman.edu/mathjournal
 Convex Hulls and The
Casas-Alvero Conjecture for
the Complex Plane

Thomas Polstraa

Volume 13, No. 1, Spring 2012

aGeorgia State University

Rose-Hulman Undergraduate Mathematics Journal

Volume 13, No. 1, Spring 2012

Convex Hulls and The Casas-Alvero
Conjecture for the Complex Plane

Thomas Polstra

Abstract. It has been conjectured by Casas-Alvero that polynomials of degree n
over ﬁelds of characteristic 0, share roots with each of its n − 1 derivatives if and
only if those polynomials have one root of degree n.
In this paper, using the analytic theory of polynomials, an equivalent formulation of
the Casas-Alvero Conjecture is established for polynomials over the complex plane
together with several special cases of it.

Acknowledgements: I would like to thank Florian Enescu for suggesting this project
and mentoring me as part of the RIMMES program at Georgia State University.

Page 34 RHIT Undergrad. Math. J., Vol. 13, No. 1

1 Introduction

In 2001 Eduardo Casas-Alvero, in relation to his work on the geometry of plane curves,
conjectured that certain classes of polynomials will share a root with each of its derivatives
if and only if these polynomials have one unique root [1]. The conjecture is formally stated
below.

Conjecture 1.1. (Casas-Alvero) Let k be a ﬁeld of characteristic 0. Any polynomial of
degree n in k[x] shares a root with each of its n−1 derivatives iﬀ f has one root of multiplicity
n, i.e. f is in the form of f (z) = α(z − z0)n.

Due to its elementary statement, the conjecture has immediately generated interest
among mathematicians, but it has remained open. Computational methods have been used
to prove the conjecture for small degrees [2], and work has been done to prove the conjec-
ture for all polynomials of degree that is a power of a prime, pn, or twice the power of a
prime, 2pn, [3]. The smallest degree for which the Casas-Alvero Conjecture not known is for
polynomials of degree 12.

In Section 2 we discuss the terminology used in the statement of the Casas-Alvero Conjec-
ture and discuss background material about polynomials over the complex plane. In Section
3 we develop an equivalent statement to the Casas-Alvero Conjecture for polynomials over
the complex plane while in Section 4 we give an equivalent condition to the conjecture for
polynomials with only real roots.

2 Background

A ﬁeld of characteristic 0 is a ﬁeld containing a copy of the rationals Q. Some common
examples of ﬁelds of characteristic 0 include Q, R, C and Q(X), the ﬁeld of rational functions
f (x)
g(x) where f (x) and g(x) are polynomials with coeﬃcients in Q. An example of a ﬁeld that
is not of characteristic 0 is Zp = Z/pZ, where p is a prime number.

Let k[x] be the collection of all polynomials in x with coeﬃcients in k. For a polynomial
f ∈ k[x] let f (i) denote the ith derivative of f . We can recall that f has a root of multiplicity
j at x0 if and only if f (i)(x0) = 0 for all 0 ≤ i ≤ j − 1 and f (j)(x0) ̸= 0. We say that x0 is a
simple root of f if x0 is a root of multiplicity 1, i.e. f (x0) = 0 and f ′(x0) ̸= 0.

The reason why the conjecture is stated over a ﬁeld of characteristic 0 is because coun-
terexamples to the conjecture in characteristic p are readily available. For example, the
polynomial f = x3 − 1 with coeﬃcients in Z3 has roots at 0 and 1, but the polynomials
f ′ = 3x2 = 0 and f ′′ = 0 both have roots at 0. In other words, this particular degree 3
polynomial shares a root with each of its ﬁrst two derivatives, but it does not have one root
of multiplicity 3.

The rest of this paper examines polynomials over the complex plane C for the purpose
of giving an interesting reformulation of the conjecture for this important case.

RHIT Undergrad. Math. J., Vol. 13, No. 1 Page 35

For what follows, given a set C ⊂ C, we say that z ∈ C is called a boundary point of C
if and only if z is contained in no open subset of C. All other points of C are called interior
points. The collection of all boundary points is the boundary of C, denoted ∂C, and that
the collection of all interior points is the interior of C, denoted int(C). The exterior of C is
C \ C and is denoted ext(C).

We can recall that a set C of the complex plane is called convex if z1, z2 ∈ C and
t ∈ (0, 1) implies tz1 + (1 − t)z2 ∈ C. This deﬁnition captures the feature that the line
segment connecting z1, z2 must be a part of C. A convex set C is called strictly convex if it
has the additional property that if z1, z2 ∈ C then for all t ∈ (0, 1), tz1 + (1 − t)z2 must be
an interior point of C. A circle in the plane is an example of a strictly convex set.

The Fundamental Theorem of Algebra implies that a polynomial f of degree n has at
most n complex roots and exactly n roots if multiplicity is counted. Using this, one can
deﬁne what a convex hull of a polynomial is.

Deﬁnition 2.1. The convex hull of a polynomial f (x) with coeﬃcients in C is the intersec-
tion of all convex sets that contain the roots of f , denoted by Cf . That is, Cf is the convex
hull of the roots of f .

As a visual illustration of what a convex hull would look like, in the images in Figure 1
the dots represent some polynomial’s roots which lie in the complex plane, the structures
containing these dots represent the convex hull of that polynomial.

Another way to visualize a convex hull of a polynomial is to imagine that the roots of
a polynomial were represented by pegs lying in the complex plane, and a rubber band is
stretched around those pegs. If the rubber band is allowed to contract then it will catch
onto those pegs in a manner forming a convex structure. This structure will represent the
convex hull of that polynomial.

Figure 1: Examples of Convex Hulls

We denote the convex hulls of f, f ′, ..., f (n−1) as Cf , Cf ′, ..., Cf (n−1) respectively. A stan-
dard result on the theory of polynomials with complex coeﬃcients is given below.

Page 36 RHIT Undergrad. Math. J., Vol. 13, No. 1

Theorem 2.2. (Gauss-Lucas,[5])
If f (x) is a polynomial with complex coeﬃcients, then the roots of f ′(x) are contained in
Cf .
An immediate result from the Gauss-Lucas Theorem relates the convex hull of f to those
of its derivatives.

Corollary 2.3. ([5])
If f (x) is a polynomial with complex coeﬃcients, then Cf (n−1) ⊆ ... ⊆ Cf ′ ⊆ Cf .

Another standard result in the study of polynomials is credited to Augustin-Louis Cauchy.
It gives a description of the roots of a particular class of monic polynomials, where a monic
polynomial is a polynomial whose leading coeﬃcient is 1.

Theorem 2.4. (Cauchy’s Theorem, pg. 243, [5], pg. 2-3, [4])
Let f (x) = xn + an−1xn−1 + · · · + a1x + a0, where ai ∈ R≤0 and at least one of them is
nonzero. Then f (x) has one positive root p, it is simple, and all other roots have absolute
value less than or equal to p.

Under these conditions, f (x) will have one positive root of multiplicity 1, x0 ∈ R>0, and
all other roots will lie in the disc centered at the origin with radius x0. In Section 4 we will
apply Theorem 2.4 to establish several cases of the Casas-Alvero conjecture.

By relating the roots of a polynomial to the vertices of its convex hull we give an equivalent
reformulation of the Casas-Alvero Conjecture in Theorem 3.1. In order to prove Theorem
3.1 we must ﬁrst look at some additional properties of the convex hull of a polynomial.

Intuitively, when considering a polygon in the plane, we sometimes think of a vertex
being a boundary point where two edges of that polygon meet. But a vertex of a polygon
has the feature that a line segment containing the vertex must be such that at least one of
the endpoints is not a part of the polygon’s boundary nor the interior. This intuition is the
motivation of the following deﬁnition.

Deﬁnition 2.5. Let C ⊆ C be any set in the complex plane and v ∈ C. Then v is a vertex
for C if it has the property that, for any z1, z2 ∈ C with tz1 +(1−t)z2 = v for some t ∈ (0, 1),
then either z1 ̸∈ C or z2 ̸∈ C.

Note that the contrapositive of this deﬁnition says that if v is a vertex of C, z1, z2 ∈ C,
then tz1 + (1 − t)z2 ̸= v for any t ∈ (0, 1). In other words, no line segment contained in C
can contain v as an interior point.

Proposition 2.6. If v is a vertex of Cf , then v ∈ ∂Cf .

Proof. Suppose by a contradiction that v ∈ int(Cf ). This implies there exists D, a disc,
around v s.t. D ⊆ Cf . But that implies each diameter of D, a line segment containing v as
an interior point is in Cf , contradicting v being a vertex.

RHIT Undergrad. Math. J., Vol. 13, No. 1 Page 37

Proposition 2.7. A convex set, γ ⊆ Cf , will contain a vertex, v, of Cf if and only if v is
also a vertex of γ.

Proof. Suppose by a contradiction that v is not a vertex of γ, hence there exists z1, z2 ∈
γ ⊆ Cf and t ∈ (0, 1) such that tz1 + (1 − t)z2 = v. This immediately contradicts v being a
vertex of Cf . If v is indeed a vertex of γ then it is trivial that v ∈ γ.

Proposition 2.8. If f is a polynomial with complex coeﬃcients, then every vertex of the
convex hull of f , Cf , must be a root of f .

Proof. Suppose by a contradiction that a vertex, v ∈ Cf , is such that it is not a root of f ,
i.e. v ̸∈ R where R is the set of all roots of f . All that is needed to contradict this scenario
is the existence of another convex set, C, such that R ⊆ C ⊂ Cf where v ̸∈ C. Consider the
set C = Cf \ {v}, it is clear that v ̸∈ C, and that R ⊆ C ⊂ Cf , so the only thing left to
show is that C is a convex set.

Consider two points z1, z2 ∈ C ⊂ Cf , then by convexity of Cf , we have for all t ∈ (0, 1)
that tz1 + (1 − t)z2 ∈ Cf . But note that tz1 + (1 − t)z2 ̸= v since v is a vertex of Cf , therefore
tz1 + (1 − t)z2 ∈ C = Cf \ {v}; implying that C is indeed a convex set.

Therefore all vertices of a polynomial’s convex hull must be among the roots of that
polynomial.

3 An approach to the Casas-Alvero Conjecture

We can now state the main contribution of the paper, which is an equivalent formulation of
the Casas-Alvero conjecture that could provide new insights on the conjecture for the complex
plane. This formulation relies on the characterization of the vertices of a polynomial’s convex
hull.

Theorem 3.1. If f is a polynomial that shares a root with each of its n − 1 derivatives then
each root is a vertex of Cf if and only if f has only one root of multiplicity n.

Proof. If f has only one root of multiplicity n, then it is clear that f shares a root with each
of its n − 1 derivatives and that each root, i.e. the only root, is a vertex of Cf .

Let f share a root with each of its n − 1 derivatives. We can assume that each root of f
is a vertex of Cf . By the Gauss-Lucas Theorem and Corollary 2.3 we have, Cf (n−1) ⊆ ... ⊆
Cf ′ ⊆ Cf . Thus, if f (n−1)(z0) = 0 then z0 lies in the convex hull of all derivatives of f (z),
i.e. z0 ∈ Cf (i) for all i. Also, we know that f (z0) = f (n−1)(z0) = 0, since f shares a root with
each of its n − 1 derivatives and the (n − 1)st derivative f (n−1) of a degree n polynomial is
a degree 1 polynomial, and hence has only one root. In particular, we know z0 ∈ Cf ′, but

Page 38 RHIT Undergrad. Math. J., Vol. 13, No. 1

since z0 is a vertex of Cf , by Proposition 2.7 we know z0 is a vertex of Cf ′. By Proposition
2.8, z0 must be a root of f ′.

Since z0 ∈ Cf ′′ and z0 is now known to be a vertex of Cf ′, this implies by the same
reasons that f ′(z0) = 0 that f ′′(z0) = 0.

Continuing this process shows that z0 must be a root of all n − 1 derivatives of f (z),
implying that f (z) has only one root, z0, of multiplicity n.

Based upon Theorem 3.1, we know that in order to prove the Casas-Alvero Conjecture
for polynomials over the complex plane, it is enough to show that a complex polynomial of
degree n which shares a root with each of its n − 1 derivatives must be such that each root
is a vertex of its convex hull.

Before we can give a proof of the Casas-Alvero Conjecture under some additional as-
sumptions given in Corollary 3.5, we need to develop a few Lemmas.

Lemma 3.2. If w ∈ ∂C, where C is a convex set, and w is not a vertex of C, then any
segment, l, contained in C and containing w as an interior point must be such that l ⊆ ∂C
i.e. l contains no interior point of C.

Proof. Suppose by a contradiction that there exists a line, l, contained in C in which w is
an interior point and that l contains an interior point of C, namely i. This implies there
exists a line segment, l′, containing i as one of its end points and w as an interior point of l′.
But w is a boundary point of C meaning that any neighborhood, Ω, around w must contain
points in the exterior of C and in the interior of C. So consider the disc, Γ, centered around
w and whose boundary contains i. The boundary of Cf contained in Γ separates the region
of Γ into two separate areas, one area is part of int(C) and the other is in ext(C). The line
l′ contains w ∈ ∂C implies that l′ must pass through the boundary of C, since l′ contains an
interior point of C, and that it must contain points in the exterior of C, a contradiction.

Lemma 3.3. If γ is a strictly convex set and v ∈ ∂γ, then v is a vertex of γ.

Proof. Suppose by a contradiction that v ∈ ∂γ but is not a vertex. This implies there exists
l, a line segment, such that v ∈ int(l) and that l ⊆ γ. By Lemma 3.2 l can contain no
interior point of γ, thus the end points of l must be elements of ∂γ. But γ is strictly convex
which implies that no points that are part of int(l) can be in ∂γ; since v is in both, we have
a contradiction.

Theorem 3.4. If f is a polynomial with complex coeﬃcients of degree n such that its roots
lie on the boundary of a strictly convex set, Γ, then each root of f is a vertex of Cf .

Proof. Each root of f lies on the ∂Γ implies each root of f is a vertex of Γ. Since Cf is the
intersection of all convex sets containing the roots of f , and Γ is convex, thus Cf ⊆ Γ and
by Proposition 2.7 each root of f must be a vertex of Cf .

RHIT Undergrad. Math. J., Vol. 13, No. 1 Page 39

Corollary 3.5. If f is a polynomial with complex coeﬃcients of degree n such that its roots
lie on the boundary of a strictly convex set, Γ, then f has only one root of multiplicity n.

Proof. This is immediate by Theorems 3.1 and 3.4.

A potential, but seemingly diﬃcult, method to prove the Casas-Alvero Conjecture would
be as follows. Let z1, z2, ..., zn be roots of a degree n polynomial f that shares a root with
each of its n − 1 derivatives. If we can somehow show that for every point z ∈ C that the
distance from z to zi is the same, then we can conclude that z1 = z2 = · · · = zn. Corollary
3.5 gives a simpler version of this method. If we can show there exists at least one point
in z ∈ C such that the distance from z to zi is the same, then all the roots of f lie on the
boundary of a disc, a strictly convex set, which would prove the Casas-Alvero Conjecture
for the complex plane.

4 Polynomial Functions with only Real Roots

4.1 Polynomials with real roots

Using methods diﬀerent from the previous sections, we can show an equivalent condition to
the Casas-Alvero Conjecture for polynomials having only real roots. It should be noted that
it is not necessarily the case that a polynomial with real roots will have real coeﬃcients;
such an assumption is not made until Theorem 4.5. It will be shown in Theorem 4.3 that if
f = ∑n
i=0 aixi shares a root with each of its n − 1 derivatives, and f (n−2) has only one root
of multiplicity 2, then f has only one root of multiplicity n. The proof of Theorem 4.3 relies
on Viete’s Relations, formulas that relate the coeﬃcients of a polynomial to its roots.

Theorem 4.1. (Viete’s Relations, [4])
Let f = ∑n
i=0 aixi be a monic polynomial with roots x1, x2, ..., xn. Then we have the
following
 (−1)kan−k = ∑

1≤i1≤i2≤···≤ik≤n xi1xi2 · · · xik.

In particular, using the above notations,

−an−1 = x1 + x2 + · · · + xn

an−2 = x1x2 + x1x3 + · · · + x1xn + x2x3 + · · · + xn−1xn
= x1(x2 + x3 + · · · xn) + x2(x3 + · · · + xn) + · · · + xn−1(xn).

Page 40 RHIT Undergrad. Math. J., Vol. 13, No. 1

Proposition 4.2. Let f = ∑n
i=0 aixi be a monic polynomial such that f (0) = an−1 = an−2 =
0 and let x1, · · · , xn be the roots of f , then x2
1 + · · · + x2
n = 0.

Proof. Since an−1 = an−2 = 0 we have that by Theorem 4.1, x1 + x2 + · · · + xn = 0 and
x1(x2 + x3 + · · · xn) + x2(x3 + · · · + xn) + · · · + xn−1xn = 0. In particular, we have that
(x1 + x2 + · · · xn)2 = 0. Hence

0 = (x1 + x2 + · · · xn)2

= x2
1 + x2
2 + · · · + x2
n + x1(x2 + x3 + · · · + xn)
+ x2(x3 + · · · + xn) + · · · + xn−1(xn)
= x2
1 + x2
2 + · · · + x2
n + an−2
= x2
1 + x2
2 + · · · + x2
n.

Using Proposition 4.2 we can give an equivalent reformulation of the Casas-Alvero Con-
jecture for polynomials that only have real roots.

Theorem 4.3. If f a polynomial of degree n with only real roots and it shares a root with
each of its n − 1 derivatives, then f (n−2) has only one root of multiplicity 2 if and only if f
has one root of multiplicity n.

Proof. If f has only one root of multiplicity n, then it is clear that f must share a root with
each of its n − 1 derivatives and that f (n−2) has only one root of multiplicity 2.

Without loss of generality, let f be a monic polynomial. Suppose that f shares a root
with each of its n − 1 derivatives, and that f (n−2) has only one root of multiplicity 2, say w0,
then f (w0) = f (n−2)(w0) = 0.

Let g(x) = f (x + w0) = ∑n
i=0 aixi. It is clear that whenever z0 is a root of g(i) then
z0 + w0 is a root for f (i). In particular, we have that g also shares a root with each of its
n − 1 derivatives and that all the roots of g must be real. But we have that g(0) = f (w0) =
f (n−2)(w0) = f (n−1)(w0) = 0; i.e. g(0) = g(n−2)(0) = g(n−1)(0) = 0.

Note that g(n−2)(x) = n!
2 x2 + an−1(n − 1)!x + an−2(n − 2)!, but g(n−2)(0) = 0 implies
an−2 = 0. Also g(n−1)(x) = n!x + an−1(n − 1)!, so g(n−1)(0) = 0 implies that an−1 = 0.
We now have that g(0) = an−2 = an−1 = 0. By Theorem 4.2 we have that for the roots
x1, x2, ..., xn of g, satisﬁes x2
1 + x2
2 + · · · + x2
n = 0. Since all roots of g are real, this implies
x1 = x2 = · · · = xn = 0. Therefore g has only one root of multiplicity n at 0, which implies
that f has only one root of multiplicity n at w0.

RHIT Undergrad. Math. J., Vol. 13, No. 1 Page 41

4.2 Even and Odd Polynomial Functions

This subsection gives a proof of the Casas-Alvero conjecture for even and odd polynomial
functions with real roots and under some additional assumptions. Recall that an even
function is a function such that f (z) = f (−z) for all z ∈ C and that an odd function is a
function such that f (z) = −f (z) for all z ∈ C.

Proposition 4.4. A polynomial, f (x) = ∑n
i=0 aixi, is an even function if and only if ai = 0
for all i odd.

Proof. If ai = 0 for all i odd then it is clear that f (x) is even function. Consider a polynomial
f (x) that is an even function. Let g(x) = ∑n
i=0 bixi where bi = ai for i even and bi = 0 for i
odd. It is clear g(x) is an even function; it is also clear that h(x) = f (x) − g(x) is an even
function. But the only nonzero coeﬃcients h(x) can have is at the x’s with odd powers. So if
there are nonzero coeﬃcients, then h(x) will have nonzero coeﬃcients at odd powers, clearly
making h(x) not an even function, a contradiction.

An identical proof can be used to show that for f (x) = ∑n
i=0 aixi is an odd polynomial
function if and only if ai = 0 for i even. In addition, by Proposition 4.4 we can readily
see that the derivative of an even polynomial function is odd and the derivative of an odd
polynomial function is even.

Theorem 4.5. If f (x) = ∑n
i=0 aixi is an even or odd monic polynomial function that shares
a root with each of its n − 1 derivatives, has only real roots, and an−1, an−2, ..., a0 ≤ 0, then
f (x) has only one root at 0 of multiplicity n.

Proof. Assume that f is an even polynomial function. To show that f has a root at 0 consider
f (n−1)(x) = n!x, which has a root at 0. Recall that by Proposition 4.4 that an−1 = 0. Hence
f (n−1)(x) has its only root at 0, therefore f (x) must have a root at 0 as well.

Suppose by a contradiction that f (x) shares a root with each of its n − 1 derivatives and
that 0 is not the only root of f (x); i.e, for some ai, a coeﬃcient of f (x), is nonzero.

All coeﬃcients of f (x) are negative or equal to zero, with at least one being nonzero.
Thus by Theorem 2.4, f (x) has only one positive root p and it is simple. Since f (x) is an
even function, f (−p) = 0. We also have that −p is a simple root of f (x), if not, then f ′(x)
is an odd function such that f (−p) = 0, which would imply f ′(p) = 0, contradicting that p
is a simple root of f (x).

We now have that f (x) = (x − p)(x + p)xn−2. Since 0 is a root of multiplicity n − 2
for f we have that f (0) = f ′(0) = · · · = f (n−3)(0) = f (n−1)(0) = 0, so f (n−2)(x) is the only
derivative in question to having a root at 0. But note that Cf , the convex hull of the roots of
f (x), is the line segment [−p, p]. Hence p and −p are vertices of Cf , so if f (n−2)(x) has a root
at p or −p then f (p) = f ′(p) = · · · f (n−2)(p) = 0 or f (−p) = f ′(−p) = · · · f (n−2)(−p) = 0,

Page 42 RHIT Undergrad. Math. J., Vol. 13, No. 1

see Theorem 3.1. Therefore if the root shared by f (x) and f (n−2)(x) is at p or −p then f (x)
will have a root of multiplicity n − 1 at p or −p, a contradiction to p and −p being simple.

The proof of this Theorem for f an odd polynomial function is identical to the case when
f is an even polynomial function.

5 Conclusions

This paper examined the properties a polynomial f over C for the purpose to restate the
Casas-Alvero Conjecture in terms of the location of the roots of f with respect to its convex
hull. In particular, a degree n polynomial f that shares a root with each of its n − 1
derivatives will have only one root if and only if every root of f is a vertex of the convex
hull of f . Using this reformulation of the conjecture, it might be possible use computational
methods to prove the conjecture for degree 12 polynomials.

A reformulation of the Casas-Alvero Conjecture for polynomials with only real roots is
given in Section 4. Theorem 4.3 shows that to prove the Casas-Alvero Conjecture for a
polynomial f of degree n with real roots, it is enough to show that the (n − 2)nd derivative
of f has only one root of multiplicity 2.

References

[1] Eduardo Casas-Alvero. Higher order polar germs. Journal of Algebra, 240:226–237, 2001.

[2] Laureano Gonzalez-Vega Gema Diaz-Toca. On a conjecture about univariate polynomials
and their roots. Algorithimic Algebra and Logic, pages 83–90, 2005.

[3] Josef Schicho Christiaan van Woestijne Hans-Christian Graf von Bothmer, Oliver Labs.
The casas-alvero conjecture for inﬁnitely many degrees. Journal of Algebra, 316:224–230,
2007.

[4] Victor V. Prasolov. Polynomials, volume 11 of Algorithms and Computation in Mathe-
matics. Springer-Verlag, Berlin, 2004.

[5] G Schmeisser Q Rahman. Analytic Theory of Polynomials, volume 26 of London Math-
ematical Society Monographs. Oxford Science Publications, London, 2002.
